#!/usr/bin/env python3
"""
Test Runner Script for py-armodel

This script runs both unit tests and integration tests with coverage reporting.

Usage:
    python scripts/run_tests.py              # Run all tests with coverage (default)
    python scripts/run_tests.py --unit       # Run only unit tests
    python scripts/run_tests.py --integration # Run only integration tests
    python scripts/run_tests.py --no-coverage # Run without coverage reports
    python scripts/run_tests.py --verbose    # Verbose output

The script generates:
1. Console output with test results
2. Coverage report (HTML, XML, terminal, and markdown) [enabled by default]
3. Test summary with pass/fail statistics
4. `reports/run_tests_report.md` with detailed test execution results
"""

import argparse
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class Colors:
    """ANSI color codes for terminal output."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(text: str) -> None:
    """Print a formatted header."""
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'=' * 80}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{text:^80}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'=' * 80}{Colors.ENDC}\n")


def print_section(text: str) -> None:
    """Print a section header."""
    print(f"\n{Colors.BOLD}{Colors.OKBLUE}{text}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'-' * len(text)}{Colors.ENDC}")


def print_success(text: str) -> None:
    """Print success message."""
    print(f"{Colors.OKGREEN}✓ {text}{Colors.ENDC}")


def print_error(text: str) -> None:
    """Print error message."""
    print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")


def print_warning(text: str) -> None:
    """Print warning message."""
    print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")


def check_and_install_pyyaml() -> None:
    """Check if pyyaml is installed, install it if not."""
    try:
        import importlib.util
        importlib.util.find_spec('yaml')
    except (ImportError, ModuleNotFoundError):
        print_warning("pyyaml not found, installing...")
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "pyyaml"],
                check=True,
                capture_output=True
            )
            print_success("pyyaml installed successfully")
        except subprocess.CalledProcessError as e:
            print_error(f"Failed to install pyyaml: {e}")
            sys.exit(1)


def run_command(
    cmd: List[str],
    description: str,
    verbose: bool = False
) -> Tuple[bool, str]:
    """
    Run a command and return success status and output.

    Args:
        cmd: Command to run as list of strings
        description: Description of what the command does
        verbose: Whether to show verbose output

    Returns:
        Tuple of (success: bool, output: str)
    """
    print(f"  {description}...", end=" ", flush=True)

    try:
        if verbose:
            print()
            result = subprocess.run(
                cmd,
                capture_output=False,
                text=True
            )
        else:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True
            )

        if result.returncode == 0:
            print_success("OK")
            return True, result.stdout
        else:
            print_error("FAILED")
            if not verbose and result.stderr:
                print(f"  Error: {result.stderr.strip()[:200]}")
            return False, result.stderr

    except Exception as e:
        print_error(f"EXCEPTION: {e}")
        return False, str(e)


def run_unit_tests(
    args: argparse.Namespace,
    pytest_args: List[str],
    run_coverage: bool = True
) -> Tuple[bool, int, int, int]:
    """
    Run unit tests (tests/test_armodel/).

    Args:
        args: Command line arguments
        pytest_args: Additional pytest arguments
        run_coverage: Whether to generate coverage reports

    Returns:
        Tuple of (success, passed, failed, skipped)
    """
    print_section("Running Unit Tests")

    cmd = [
        sys.executable, "-m", "pytest",
        "tests/test_armodel/",
        "-v" if args.verbose else "-q",
        "--tb=short" if not args.verbose else "--tb=long",
    ]

    # Add coverage if requested (default is True)
    if run_coverage:
        cmd.extend([
            "--cov=armodel",
            "--cov-report=term-missing",
            "--cov-report=html:htmlcov/unit",
            "--cov-report=xml:coverage_unit.xml",
        ])

    cmd.extend(pytest_args)

    success, output = run_command(
        cmd,
        "Unit tests",
        args.verbose
    )

    # Parse results from output
    passed = failed = skipped = 0
    if success and output:
        # Try to parse pytest summary
        for line in output.split('\n'):
            if ' passed' in line:
                parts = line.split()
                for i, part in enumerate(parts):
                    if part == 'passed':
                        try:
                            passed = int(parts[i - 1])
                        except (ValueError, IndexError):
                            pass
                    elif part == 'failed':
                        try:
                            failed = int(parts[i - 1])
                        except (ValueError, IndexError):
                            pass
                    elif part == 'skipped':
                        try:
                            skipped = int(parts[i - 1])
                        except (ValueError, IndexError):
                            pass

    # If parsing failed but test passed, set default passed count
    if success and passed == 0 and failed == 0 and skipped == 0:
        # Default to 1 passed for integration tests (single test file)
        passed = 1

    return success, passed, failed, skipped


def run_integration_tests(
    args: argparse.Namespace,
    pytest_args: List[str],
    run_coverage: bool = True
) -> Tuple[bool, int, int, int]:
    """
    Run integration tests (tests/integration_tests/).

    Args:
        args: Command line arguments
        pytest_args: Additional pytest arguments
        run_coverage: Whether to generate coverage reports

    Returns:
        Tuple of (success, passed, failed, skipped)
    """
    print_section("Running Integration Tests")

    cmd = [
        sys.executable, "-m", "pytest",
        "tests/integration_tests/",
        "-v",  # Always verbose for integration tests (show progress)
        "-s",  # Show print output (progress indicators)
        "--tb=short" if not args.verbose else "--tb=long",
    ]

    # Add coverage if requested (default is True)
    if run_coverage:
        cmd.extend([
            "--cov=armodel",
            "--cov-append",
            "--cov-report=term-missing",
            "--cov-report=html:htmlcov/integration",
            "--cov-report=xml:coverage_integration.xml",
        ])

    cmd.extend(pytest_args)

    success, output = run_command(
        cmd,
        "Integration tests",
        args.verbose or True  # Always show output for integration tests
    )

    # Parse results from output
    passed = failed = skipped = 0
    if success and output:
        # Try to parse pytest summary
        for line in output.split('\n'):
            if ' passed' in line:
                parts = line.split()
                for i, part in enumerate(parts):
                    if part == 'passed':
                        try:
                            passed = int(parts[i - 1])
                        except (ValueError, IndexError):
                            pass
                    elif part == 'failed':
                        try:
                            failed = int(parts[i - 1])
                        except (ValueError, IndexError):
                            pass
                    elif part == 'skipped':
                        try:
                            skipped = int(parts[i - 1])
                        except (ValueError, IndexError):
                            pass

    # If parsing failed but test passed, set default passed count
    if success and passed == 0 and failed == 0 and skipped == 0:
        # Default to 1 passed for integration tests (single test file)
        passed = 1

    return success, passed, failed, skipped


def generate_combined_coverage_report() -> None:
    """Generate combined coverage report if coverage was enabled."""
    coverage_dir = Path("htmlcov")
    if not coverage_dir.exists():
        return

    print_section("Coverage Reports Generated")

    unit_dir = coverage_dir / "unit"
    integration_dir = coverage_dir / "integration"

    if unit_dir.exists():
        print_success(f"Unit test coverage: {unit_dir}/index.html")
    if integration_dir.exists():
        print_success(f"Integration test coverage: {integration_dir}/index.html")


def parse_coverage_xml(xml_path: Path) -> Optional[Dict]:
    """
    Parse coverage XML file and extract coverage data.

    Args:
        xml_path: Path to coverage XML file

    Returns:
        Dict with coverage data or None if parsing fails
    """
    if not xml_path.exists():
        return None

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # The root element is <coverage>, not a child
        if root.tag != 'coverage':
            print_warning(f"Unexpected root element: {root.tag}")
            return None

        # Extract overall coverage from root element
        overall = {
            'line_rate': float(root.get('line-rate', 0)),
            'branch_rate': float(root.get('branch-rate', 0)),
            'lines_covered': int(root.get('lines-covered', 0)),
            'lines_valid': int(root.get('lines-valid', 0)),
            'branches_covered': int(root.get('branches-covered', 0)),
            'branches_valid': int(root.get('branches-valid', 0)),
        }

        # Extract per-package and per-file coverage
        # Find all packages and extract class coverage
        classes_data = []

        for package in root.findall('.//package'):
            # Find all classes in this package
            for classes_elem in package.findall('.//classes'):
                for cls in classes_elem.findall('class'):
                    class_name = cls.get('name', '')
                    filename = cls.get('filename', '')
                    line_rate = float(cls.get('line-rate', 0))
                    branch_rate = float(cls.get('branch-rate', 0))

                    # Count actual lines from <lines> elements
                    lines_elem = cls.find('lines')
                    lines_valid = 0
                    lines_covered = 0

                    if lines_elem is not None:
                        for line in lines_elem.findall('line'):
                            lines_valid += 1
                            hits = int(line.get('hits', 0))
                            if hits > 0:
                                lines_covered += 1

                    class_data = {
                        'name': class_name,
                        'filename': filename,
                        'line_rate': line_rate,
                        'branch_rate': branch_rate,
                        'lines_covered': lines_covered,
                        'lines_valid': lines_valid,
                    }
                    classes_data.append(class_data)

        return {
            'overall': overall,
            'classes': classes_data
        }

    except Exception as e:
        print_warning(f"Failed to parse coverage XML: {e}")
        return None


def generate_coverage_markdown(
    unit_coverage: Optional[Dict] = None,
    integration_coverage: Optional[Dict] = None
) -> None:
    """
    Generate a markdown coverage report.

    Args:
        unit_coverage: Parsed unit test coverage data
        integration_coverage: Parsed integration test coverage data
    """
    report_path = Path("reports/run_tests_report.md")

    try:
        with open(report_path, 'w') as f:
            f.write("# Test Coverage Report\n\n")
            f.write("> Generated by `scripts/run_tests.py` (coverage is enabled by default)\n\n")
            f.write("---\n\n")

            # Unit Test Coverage
            if unit_coverage:
                f.write("## Unit Test Coverage\n\n")

                overall = unit_coverage['overall']
                line_pct = overall['line_rate'] * 100
                branch_pct = overall['branch_rate'] * 100

                # Badge
                badge_color = "brightgreen" if line_pct >= 80 else "yellow" if line_pct >= 50 else "red"
                f.write(f"![coverage](https://img.shields.io/badge/coverage-{line_pct:.1f}%25-{badge_color})\n\n")

                f.write("### Summary\n\n")
                f.write(f"| Metric | Covered | Valid | Percentage |\n")
                f.write(f"|--------|---------|-------|------------|\n")
                f.write(f"| **Lines** | {overall['lines_covered']} | {overall['lines_valid']} | **{line_pct:.2f}%** |\n")
                f.write(f"| **Branches** | {overall['branches_covered']} | {overall['branches_valid']} | **{branch_pct:.2f}%** |\n\n")

                # Coverage by module
                if unit_coverage['classes']:
                    f.write("### Coverage by Module\n\n")

                    # Group by module (using subdirectory for better granularity)
                    modules: Dict[str, List[Dict]] = {}
                    for cls in unit_coverage['classes']:
                        # Extract module path from filename like "src/armodel/cli/arxml_dump_cli.py"
                        filename = cls.get('filename', '')
                        if filename:
                            parts = filename.split('/')
                            # Get meaningful module name from path
                            # e.g., "src/armodel/cli/..." -> "cli"
                            # e.g., "src/armodel/models/..." -> "models"
                            # e.g., "src/armodel/lib/..." -> "lib"
                            if len(parts) > 2 and parts[0] == 'src' and parts[1] == 'armodel':
                                # Use the third part (subdirectory) as module name
                                module = parts[2] if len(parts) > 2 else 'armodel'
                            elif len(parts) > 1 and parts[0] == 'src':
                                # Fallback to second part
                                module = parts[1] if len(parts) > 1 else 'other'
                            else:
                                module = parts[0] if parts else 'other'
                        else:
                            # Fallback to using class name
                            name = cls.get('name', '')
                            module = name.split('.')[0] if '.' in name else 'other'

                        if module not in modules:
                            modules[module] = []
                        modules[module].append(cls)

                    f.write("| Module | Files | Line Coverage |\n")
                    f.write("|--------|-------|---------------|\n")

                    # Sort by coverage percentage (descending)
                    module_stats = []
                    for module_name, files in modules.items():
                        total_lines = sum(c['lines_valid'] for c in files)
                        covered_lines = sum(c['lines_covered'] for c in files)
                        if total_lines > 0:
                            coverage_pct = (covered_lines / total_lines) * 100
                        else:
                            coverage_pct = 0.0
                        module_stats.append((module_name, len(files), coverage_pct))

                    # Sort by coverage descending
                    module_stats.sort(key=lambda x: x[2], reverse=True)

                    for module_name, file_count, coverage_pct in module_stats:
                        f.write(f"| **{module_name}** | {file_count} | {coverage_pct:.1f}% |\n")

                    f.write("\n")

                    # Files needing attention
                    f.write("### Files Needing Attention\n\n")
                    f.write("> Files with less than 80% coverage\n\n")

                    low_coverage_files = [c for c in unit_coverage['classes'] if c['line_rate'] < 0.8]
                    low_coverage_files.sort(key=lambda x: x['line_rate'])

                    if low_coverage_files:
                        f.write("| File | Line Coverage | Branch Coverage |\n")
                        f.write("|------|---------------|-----------------|\n")

                        for cls in low_coverage_files[:20]:  # Limit to top 20
                            line_pct = cls['line_rate'] * 100
                            branch_pct = cls['branch_rate'] * 100

                            # Extract readable name from filename
                            # filename is like "src/armodel/cli/arxml_dump_cli.py"
                            filename = cls.get('filename', '')
                            if filename:
                                # Remove .py extension and get the last two parts for context
                                parts = filename.replace('.py', '').split('/')
                                if len(parts) >= 2:
                                    # Get the last two parts for context (e.g., "cli/arxml_dump_cli")
                                    short_name = '/'.join(parts[-2:])
                                else:
                                    short_name = parts[-1] if parts else cls.get('name', 'unknown')
                            else:
                                # Fallback to using the name attribute
                                name = cls.get('name', 'unknown')
                                short_name = name.replace('.py', '') if name.endswith('.py') else name

                            f.write(f"| `{short_name}` | {line_pct:.1f}% | {branch_pct:.1f}% |\n")
                    else:
                        f.write("✅ All files have 80%+ coverage!\n")

                    f.write("\n")

            # Integration Test Coverage
            if integration_coverage:
                f.write("## Integration Test Coverage\n\n")

                overall = integration_coverage['overall']
                line_pct = overall['line_rate'] * 100
                branch_pct = overall['branch_rate'] * 100

                # Badge
                badge_color = "brightgreen" if line_pct >= 80 else "yellow" if line_pct >= 50 else "red"
                f.write(f"![coverage](https://img.shields.io/badge/integration-{line_pct:.1f}%25-{badge_color})\n\n")

                f.write("### Summary\n\n")
                f.write(f"| Metric | Covered | Valid | Percentage |\n")
                f.write(f"|--------|---------|-------|------------|\n")
                f.write(f"| **Lines** | {overall['lines_covered']} | {overall['lines_valid']} | **{line_pct:.2f}%** |\n")
                f.write(f"| **Branches** | {overall['branches_covered']} | {overall['branches_valid']} | **{branch_pct:.2f}%** |\n\n")

            # Footer
            f.write("---\n\n")
            f.write("### Reports\n\n")
            f.write("- Detailed HTML coverage reports are available in the `htmlcov/` directory\n")
            f.write("- XML coverage reports: `coverage_unit.xml`, `coverage_integration.xml`\n")
            f.write("- Run `python scripts/run_tests.py` to regenerate (coverage is enabled by default)\n")
            f.write("- Run `python scripts/run_tests.py --no-coverage` to skip coverage reports\n")

        print_success(f"Coverage report: {report_path}")

    except Exception as e:
        print_warning(f"Failed to generate markdown report: {e}")


def print_summary(
    unit_results: Tuple[bool, int, int, int],
    integration_results: Tuple[bool, int, int, int],
    run_unit: bool,
    run_integration: bool
) -> None:
    """Print final test summary."""
    print_header("TEST SUMMARY")

    total_passed = total_failed = total_skipped = 0

    if run_unit:
        unit_success, unit_passed, unit_failed, unit_skipped = unit_results
        print(f"\n{Colors.BOLD}Unit Tests:{Colors.ENDC}")
        print(f"  Passed:  {Colors.OKGREEN}{unit_passed}{Colors.ENDC}")
        print(f"  Failed:  {Colors.FAIL if unit_failed > 0 else ''}{unit_failed}{Colors.ENDC}")
        print(f"  Skipped: {Colors.WARNING if unit_skipped > 0 else ''}{unit_skipped}{Colors.ENDC}")
        print(f"  Status:  {Colors.OKGREEN if unit_success else Colors.FAIL}{'PASS' if unit_success else 'FAIL'}{Colors.ENDC}")

        total_passed += unit_passed
        total_failed += unit_failed
        total_skipped += unit_skipped

    if run_integration:
        integration_success, integration_passed, integration_failed, integration_skipped = integration_results
        print(f"\n{Colors.BOLD}Integration Tests:{Colors.ENDC}")
        print(f"  Passed:  {Colors.OKGREEN}{integration_passed}{Colors.ENDC}")
        print(f"  Failed:  {Colors.FAIL if integration_failed > 0 else ''}{integration_failed}{Colors.ENDC}")
        print(f"  Skipped: {Colors.WARNING if integration_skipped > 0 else ''}{integration_skipped}{Colors.ENDC}")
        print(f"  Status:  {Colors.OKGREEN if integration_success else Colors.FAIL}{'PASS' if integration_success else 'FAIL'}{Colors.ENDC}")

        total_passed += integration_passed
        total_failed += integration_failed
        total_skipped += integration_skipped

    # Overall summary
    if run_unit and run_integration:
        print(f"\n{Colors.BOLD}{'=' * 40}{Colors.ENDC}")
        print(f"{Colors.BOLD}Overall Totals:{Colors.ENDC}")
        print(f"  Total Passed:  {Colors.OKGREEN}{total_passed}{Colors.ENDC}")
        print(f"  Total Failed:  {Colors.FAIL if total_failed > 0 else ''}{total_failed}{Colors.ENDC}")
        print(f"  Total Skipped: {Colors.WARNING if total_skipped > 0 else ''}{total_skipped}{Colors.ENDC}")

        overall_success = (total_failed == 0)
        status_color = Colors.OKGREEN if overall_success else Colors.FAIL
        status_text = "ALL TESTS PASSED" if overall_success else "SOME TESTS FAILED"
        print(f"\n  {Colors.BOLD}{status_color}{status_text}{Colors.ENDC}")

    print()


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Run py-armodel test suite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    Run all tests with coverage (default)
  %(prog)s --unit             Run only unit tests
  %(prog)s --integration       Run only integration tests
  %(prog)s --no-coverage       Run without coverage reports
  %(prog)s --verbose          Verbose output
  %(prog)s -k "test_parser"    Run specific tests
        """
    )

    parser.add_argument(
        "--unit",
        action="store_true",
        help="Run only unit tests"
    )

    parser.add_argument(
        "--integration",
        action="store_true",
        help="Run only integration tests"
    )

    parser.add_argument(
        "--no-coverage",
        action="store_true",
        help="Disable coverage reports (coverage is enabled by default)"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )

    parser.add_argument(
        "pytest_args",
        nargs="*",
        help="Additional arguments to pass to pytest"
    )

    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    # Check and install pyyaml if not available
    check_and_install_pyyaml()

    args = parse_arguments()

    # Default to running both if neither is specified
    run_unit = args.unit or not args.integration
    run_integration = args.integration or not args.unit

    # Coverage is enabled by default unless --no-coverage is specified
    run_coverage = not args.no_coverage

    print_header("py-armodel Test Runner")

    # Build pytest arguments
    pytest_args = []
    if args.pytest_args:
        # Check if -k or --markers are in args
        pytest_args.extend(args.pytest_args)

    unit_results = (True, 0, 0, 0)
    integration_results = (True, 0, 0, 0)

    # Run tests
    try:
        if run_unit:
            unit_results = run_unit_tests(args, pytest_args, run_coverage)

        if run_integration:
            integration_results = run_integration_tests(args, pytest_args, run_coverage)

        # Generate coverage reports if coverage is enabled
        if run_coverage:
            generate_combined_coverage_report()

            # Parse coverage XML files and generate markdown report
            unit_coverage = None
            integration_coverage = None

            if run_unit:
                unit_xml = Path("coverage_unit.xml")
                if unit_xml.exists():
                    unit_coverage = parse_coverage_xml(unit_xml)

            if run_integration:
                integration_xml = Path("coverage_integration.xml")
                if integration_xml.exists():
                    integration_coverage = parse_coverage_xml(integration_xml)

            # Generate markdown report
            if unit_coverage or integration_coverage:
                print_section("Generating Markdown Coverage Report")
                generate_coverage_markdown(unit_coverage, integration_coverage)

        # Print summary
        print_summary(
            unit_results,
            integration_results,
            run_unit,
            run_integration
        )

        # Return exit code
        unit_success = unit_results[0] if run_unit else True
        integration_success = integration_results[0] if run_integration else True

        return 0 if (unit_success and integration_success) else 1

    except KeyboardInterrupt:
        print_warning("\n\nTests interrupted by user")
        return 130
    except Exception as e:
        print_error(f"\nUnexpected error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
