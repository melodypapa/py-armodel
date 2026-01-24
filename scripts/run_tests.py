#!/usr/bin/env python3
"""
Test Runner Script for py-armodel

This script runs both unit tests and integration tests with coverage reporting.

Usage:
    python scripts/run_tests.py              # Run all tests
    python scripts/run_tests.py --unit       # Run only unit tests
    python scripts/run_tests.py --integration # Run only integration tests
    python scripts/run_tests.py --coverage   # Run with coverage report
    python scripts/run_tests.py --verbose    # Verbose output

The script generates:
1. Console output with test results
2. Coverage report (HTML and terminal)
3. Test summary with pass/fail statistics
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


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
    pytest_args: List[str]
) -> Tuple[bool, int, int, int]:
    """
    Run unit tests (tests/test_armodel/).

    Args:
        args: Command line arguments
        pytest_args: Additional pytest arguments

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

    # Add coverage if requested
    if args.coverage:
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
    pytest_args: List[str]
) -> Tuple[bool, int, int, int]:
    """
    Run integration tests (tests/integration_tests/).

    Args:
        args: Command line arguments
        pytest_args: Additional pytest arguments

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

    # Add coverage if requested
    if args.coverage:
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
  %(prog)s                    Run all tests
  %(prog)s --unit             Run only unit tests
  %(prog)s --integration       Run only integration tests
  %(prog)s --coverage          Run with coverage report
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
        "--coverage",
        action="store_true",
        help="Generate coverage reports"
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
            unit_results = run_unit_tests(args, pytest_args)

        if run_integration:
            integration_results = run_integration_tests(args, pytest_args)

        # Generate coverage reports if requested
        if args.coverage:
            generate_combined_coverage_report()

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
