"""Round-trip integration tests for ARXML parser and writer.

This module tests the round-trip capability:
1. Parse ARXML file → AUTOSAR model
2. Write AUTOSAR model → ARXML file
3. Re-parse written ARXML file → AUTOSAR model
4. Compare original and re-parsed models for equality
"""
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pytest

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

# Global counter for progress tracking
_test_counter = 0
_total_tests = 0


# Known issues tracking - files with known parsing/round-trip issues
KNOWN_ISSUES: Dict[str, Dict[str, str]] = {
    # "SomeFile.arxml": {
    #     "reason": "Unsupported element XYZ",
    #     "issue_url": "https://github.com/melodypapa/py-armodel/issues/123"
    # }
}


def detect_autosar_version(
    file_path: Path,
    xsd_mapping: Dict[str, str],
    default_version: str
) -> str:
    """Detect AUTOSAR version from ARXML file's schema location.

    Args:
        file_path: Path to ARXML file
        xsd_mapping: Mapping from XSD filename to version
        default_version: Fallback version if detection fails

    Returns:
        AUTOSAR version string (e.g., "R23-11", "4.3.0")
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Check schemaLocation attribute
        schema_loc = root.attrib.get(
            "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation",
            ""
        )

        if schema_loc:
            # Extract XSD filename from schema location
            # Format: "http://autosar.org/schema/r4.0 AUTOSAR_00046.xsd"
            parts = schema_loc.split()
            if len(parts) >= 2:
                xsd_file = parts[1].split("/")[-1]
                if xsd_file in xsd_mapping:
                    return xsd_mapping[xsd_file]

        return default_version
    except Exception:
        return default_version


def assert_models_equal(
    original: Any,
    reparsed: Any,
    path: str = "",
    ignored_attrs: Optional[List[str]] = None
) -> None:
    """Recursively compare two AUTOSAR model objects for equality.

    Args:
        original: Original model object
        reparsed: Re-parsed model object
        path: Current path in the model (for error reporting)
        ignored_attrs: List of attribute names to ignore (e.g., ['parent'])

    Raises:
        AssertionError: If models don't match
    """
    ignored_attrs = ignored_attrs or ["parent"]

    # Check type
    if type(original) is not type(reparsed):
        raise AssertionError(
            f"Type mismatch at {path}:\n"
            f"  Expected: {type(original).__name__}\n"
            f"  Got: {type(reparsed).__name__}"
        )

    # If it's a basic type, compare directly
    if isinstance(original, (str, int, float, bool)) or original is None:
        if original != reparsed:
            raise AssertionError(
                f"Value mismatch at {path}:\n"
                f"  Expected: {original}\n"
                f"  Got: {reparsed}"
            )
        return

    # If it's a list, compare elements
    if isinstance(original, list):
        if len(original) != len(reparsed):
            raise AssertionError(
                f"List length mismatch at {path}:\n"
                f"  Expected: {len(original)} elements\n"
                f"  Got: {len(reparsed)} elements"
            )
        for i, (orig_item, reparsed_item) in enumerate(zip(original, reparsed)):
            assert_models_equal(
                orig_item,
                reparsed_item,
                f"{path}[{i}]",
                ignored_attrs
            )
        return

    # If it's an AUTOSAR object, compare attributes
    if hasattr(original, "__dict__"):
        orig_dict = original.__dict__
        reparsed_dict = reparsed.__dict__

        # Get all attributes from both objects
        all_keys = set(orig_dict.keys()) | set(reparsed_dict.keys())

        for key in all_keys:
            if key in ignored_attrs:
                continue

            orig_value = orig_dict.get(key)
            reparsed_value = reparsed_dict.get(key)

            new_path = f"{path}.{key}" if path else key

            # Handle None values
            if orig_value is None and reparsed_value is None:
                continue
            if orig_value is None or reparsed_value is None:
                raise AssertionError(
                    f"Attribute mismatch at {new_path}:\n"
                    f"  Expected: {orig_value}\n"
                    f"  Got: {reparsed_value}"
                )

            # Recursively compare
            assert_models_equal(orig_value, reparsed_value, new_path, ignored_attrs)


class TestRoundTrip:
    """Round-trip integration tests for parser and writer."""

    @pytest.mark.integration
    @pytest.mark.slow
    def test_roundtrip_all_files(
        self,
        arxml_files: List[Tuple[Path, str]],
        autosar_reset: Any,
        temp_file: Path,
        xsd_to_version_mapping: Dict[str, str],
        default_ar_version: str
    ) -> None:
        """Test round-trip parsing and writing for all ARXML files.

        This test iterates through all discovered ARXML files and
        performs round-trip validation.

        Args:
            arxml_files: List of (file_path, category) tuples
            autosar_reset: Fixture to reset AUTOSAR singleton
            temp_file: Fixture providing temporary file path
            xsd_to_version_mapping: Mapping from XSD to version
            default_ar_version: Default AUTOSAR version
        """
        global _test_counter, _total_tests
        _total_tests = len(arxml_files)
        _test_counter = 0

        print("\n" + "=" * 80)
        print(f"Starting round-trip tests for {_total_tests} ARXML files")
        print("=" * 80)

        start_time = time.time()
        results = {
            "passed": [],
            "failed": [],
            "skipped": []
        }

        for file_path, category in arxml_files:
            _test_counter += 1
            file_start_time = time.time()

            # Print file header
            print("\n" + "-" * 80)
            print(f"[{_test_counter}/{_total_tests}] Testing: {file_path.name}")
            print(f"  Category: {category}")
            print(f"  Path: {file_path}")

            # Check for known issues
            if file_path.name in KNOWN_ISSUES:
                issue = KNOWN_ISSUES[file_path.name]
                print(f"  ⚠️  SKIPPED (known issue): {issue['reason']}")
                results["skipped"].append(file_path.name)
                continue

            # Detect AUTOSAR version from file
            version = detect_autosar_version(
                file_path,
                xsd_to_version_mapping,
                default_ar_version
            )
            print(f"  AUTOSAR Version: {version}")

            # Step 1: Parse original file
            print("  Step 1/4: Parsing original file...", end=" ", flush=True)
            step_start = time.time()
            AUTOSAR.getInstance().setARRelease(version)
            original_doc = AUTOSAR.getInstance()
            original_doc.clear()
            parser = ARXMLParser()

            try:
                parser.load(str(file_path), original_doc)
                package_count = len(original_doc.getARPackages())
                step_time = time.time() - step_start
                print(f"✓ ({package_count} packages, {step_time:.2f}s)")
            except Exception as e:
                print("✗ FAILED")
                print(f"    Error: {e}")
                results["failed"].append((file_path.name, "parse", str(e)))
                continue

            # Capture the state of original document for comparison
            import copy
            original_packages = copy.deepcopy(original_doc.getARPackages())

            # Step 2: Write to temporary file
            print("  Step 2/4: Writing to temporary file...", end=" ", flush=True)
            step_start = time.time()
            writer = ARXMLWriter()

            try:
                writer.save(str(temp_file), original_doc)
                file_size = temp_file.stat().st_size / 1024  # KB
                step_time = time.time() - step_start
                print(f"✓ ({file_size:.1f} KB, {step_time:.2f}s)")
            except Exception as e:
                print("✗ FAILED")
                print(f"    Error: {e}")
                results["failed"].append((file_path.name, "write", str(e)))
                continue

            # Step 3: Reset and re-parse temporary file
            print("  Step 3/4: Re-parsing written file...", end=" ", flush=True)
            step_start = time.time()
            AUTOSAR.getInstance().new()
            AUTOSAR.getInstance().setARRelease(version)
            reparsed_doc = AUTOSAR.getInstance()
            reparsed_doc.clear()
            new_parser = ARXMLParser()

            try:
                new_parser.load(str(temp_file), reparsed_doc)
                package_count = len(reparsed_doc.getARPackages())
                step_time = time.time() - step_start
                print(f"✓ ({package_count} packages, {step_time:.2f}s)")
            except Exception as e:
                print("✗ FAILED")
                print(f"    Error: {e}")
                results["failed"].append((file_path.name, "re-parse", str(e)))
                continue

            # Step 4: Compare packages (the main content)
            print("  Step 4/5: Comparing models...", end=" ", flush=True)
            step_start = time.time()

            try:
                reparsed_packages = reparsed_doc.getARPackages()

                if len(original_packages) != len(reparsed_packages):
                    raise AssertionError(
                        f"Package count mismatch: "
                        f"{len(original_packages)} vs {len(reparsed_packages)}"
                    )

                assert_models_equal(
                    original_packages,
                    reparsed_packages,
                    path=f"RoundTrip({file_path.name})"
                )
                step_time = time.time() - step_start
                print(f"✓ ({step_time:.2f}s)")
            except AssertionError as e:
                print("✗ FAILED")
                print(f"    Error: {e}")
                print(f"    Temp file: {temp_file}")
                results["failed"].append((file_path.name, "compare", str(e)))
                continue

            # Step 5: Compare original file with generated file
            print("  Step 5/5: Comparing files...", end=" ", flush=True)
            step_start = time.time()

            try:
                # Read both files as text for line-by-line comparison
                with open(file_path, 'r', encoding='utf-8') as f:
                    original_lines = f.readlines()

                with open(temp_file, 'r', encoding='utf-8') as f:
                    generated_lines = f.readlines()

                # Compare line by line
                if len(original_lines) != len(generated_lines):
                    raise AssertionError(
                        f"File length mismatch:\n"
                        f"  Original: {len(original_lines)} lines\n"
                        f"  Generated: {len(generated_lines)} lines"
                    )

                # Find first differing line
                for i, (orig_line, gen_line) in enumerate(zip(original_lines, generated_lines)):
                    # Normalize XML entities for comparison (minidom converts &quot; to ")
                    orig_normalized = orig_line.replace('&quot;', '"').replace('&apos;', "'").replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
                    gen_normalized = gen_line.replace('&quot;', '"').replace('&apos;', "'").replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')

                    if orig_normalized != gen_normalized:
                        # Show context around the difference
                        context_start = max(0, i - 2)
                        context_end = min(len(original_lines), i + 3)

                        diff_context = []
                        for j in range(context_start, context_end):
                            prefix = ">>> " if j == i else "    "
                            line_num = j + 1
                            if j < len(original_lines):
                                orig = original_lines[j].rstrip()
                                diff_context.append(f"{prefix}Original line {line_num}: {orig}")
                            if j < len(generated_lines):
                                gen = generated_lines[j].rstrip()
                                diff_context.append(f"{prefix}Generated line {line_num}: {gen}")

                        raise AssertionError(
                            f"File content mismatch at line {i + 1}:\n"
                            f"  Original: {orig_normalized.rstrip()}\n"
                            f"  Generated: {gen_normalized.rstrip()}\n"
                            f"  Context:\n" + "\n".join(diff_context)
                        )

                step_time = time.time() - step_start
                file_time = time.time() - file_start_time
                print(f"✓ ({step_time:.2f}s, total: {file_time:.2f}s)")
                results["passed"].append(file_path.name)
            except AssertionError as e:
                print("✗ FAILED")
                print(f"    Error: {e}")
                print(f"    Temp file: {temp_file}")
                results["failed"].append((file_path.name, "file_compare", str(e)))
                continue

        # Print summary
        total_time = time.time() - start_time
        print("\n" + "=" * 80)
        print("ROUND-TRIP TEST SUMMARY")
        print("=" * 80)
        print(f"Total time: {total_time:.2f}s")
        print(f"Passed: {len(results['passed'])}/{_total_tests}")
        print(f"Failed: {len(results['failed'])}/{_total_tests}")
        print(f"Skipped: {len(results['skipped'])}/{_total_tests}")

        if results['failed']:
            print("\nFailed files:")
            for name, step, error in results['failed']:
                print(f"  - {name} ({step})")

        if results['skipped']:
            print("\nSkipped files:")
            for name in results['skipped']:
                print(f"  - {name}")

        print("=" * 80 + "\n")

        # Fail test if there were any failures
        if results['failed']:
            failed_count = len(results['failed'])
            pytest.fail(
                f"\n{failed_count} file(s) failed round-trip testing. "
                f"See above for details."
            )
