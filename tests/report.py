#!/usr/bin/env python3
"""
Coverage report generator
This script runs pytest with coverage and generates a simple coverage report
containing only source file names and coverage percentages.
"""

import argparse
import logging
import re
import subprocess
import sys
import time
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tests/coverage_generation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def run_pytest_with_coverage(include_slow_tests=True, test_path="tests/test_armodel", exclude_patterns=None):
    """Run pytest with coverage and return the output"""
    try:
        logger.info(f"Starting pytest with coverage on {test_path}...")

        # Build command with options
        cmd = [
            sys.executable, '-m', 'pytest',
            test_path,
            '--cov=src/armodel',
            '--cov-report=term-missing',
            '--tb=short',
            '--maxfail=1'  # Stop after first failure to prevent long execution
        ]

        # If we want to skip slow tests, add markers to exclude them
        if not include_slow_tests:
            cmd.extend(['-m', 'not slow'])
            logger.info("Excluding slow tests from coverage run")

        # Add exclusion pattern if provided
        if exclude_patterns:
            for pattern in exclude_patterns:
                cmd.extend(['--ignore', pattern])
            logger.info(f"Excluding patterns: {exclude_patterns}")

        logger.debug(f"Executing command: {' '.join(cmd)}")

        start_time = time.time()
        result = subprocess.run(cmd, capture_output=True, text=True, cwd='.', timeout=300)  # 5 minute timeout
        execution_time = time.time() - start_time

        logger.info(f"Pytest completed in {execution_time:.2f} seconds")
        logger.debug(f"Pytest exit code: {result.returncode}")

        if result.returncode != 0:
            logger.error("Error running pytest with coverage:")
            logger.error(result.stderr)
            return None

        logger.info("Pytest with coverage completed successfully")
        logger.debug(f"Coverage output length: {len(result.stdout)} characters")

        return result.stdout
    except subprocess.TimeoutExpired:
        logger.error("Pytest with coverage timed out after 5 minutes")
        return None
    except Exception as e:
        logger.error(f"Error running pytest: {e}")
        return None


def extract_coverage_data(coverage_output):
    """Extract source file names and coverage percentages from coverage output"""
    logger.info("Starting coverage data extraction...")
    lines = coverage_output.split('\n')
    coverage_data = []

    # Pattern to match coverage lines: file_path statements miss coverage%
    coverage_pattern = r'^\s*(src[/\\].*\.py)\s+(\d+)\s+(\d+)\s+(\d+)%'

    extracted_files = 0
    # Reduce logging during extraction to improve performance
    for i, line in enumerate(lines):
        match = re.match(coverage_pattern, line)
        if match:
            file_path = match.group(1).replace('\\', '/')
            coverage_percent = match.group(4)
            coverage_data.append((file_path, int(coverage_percent)))
            extracted_files += 1
            # Only log every 10th file to reduce log spam during extraction
            if extracted_files % 10 == 0:
                logger.debug(f"Extracted coverage for {extracted_files} files so far...")

    logger.info(f"Extraction complete. Found coverage data for {extracted_files} files")
    return coverage_data


def write_coverage_report(coverage_data, output_file):
    """Write the coverage data to a markdown file"""
    logger.info(f"Writing coverage report to {output_file}...")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Code Coverage Report\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("This report shows the code coverage for the AUTOSAR model library.\n\n")

        # Filter only files that don't have 100% coverage
        incomplete_coverage = [(file_path, coverage_percent) for file_path, coverage_percent in coverage_data if coverage_percent < 100]

        if incomplete_coverage:
            f.write("## Files with Incomplete Coverage\n\n")
            f.write("The following source files do not reach 100% coverage:\n\n")

            # Write standard markdown table header and separator
            f.write("| Source File | Coverage |\n")
            f.write("|-------------|----------|\n")

            # Sort by coverage percentage (ascending) to highlight the most problematic files first
            incomplete_coverage.sort(key=lambda x: x[1])

            # Write data rows for files with incomplete coverage
            for file_path, coverage_percent in incomplete_coverage:
                # Ensure proper table formatting by limiting path length
                display_path = file_path if len(file_path) <= 100 else file_path[:97] + "..."
                f.write(f"| {display_path} | {coverage_percent}% |\n")

            f.write(f"\nThere are {len(incomplete_coverage)} files that do not reach 100% coverage.\n\n")
        else:
            f.write("## Complete Coverage Achieved\n\n")
            f.write("All source files have reached 100% coverage!\n\n")

        # Write full table with all files
        f.write("## Full Coverage Summary\n\n")
        f.write("| Source File | Coverage |\n")
        f.write("|-------------|----------|\n")

        # Sort by coverage percentage (ascending) for consistency
        coverage_data.sort(key=lambda x: x[1])

        for file_path, coverage_percent in coverage_data:
            display_path = file_path if len(file_path) <= 100 else file_path[:97] + "..."
            f.write(f"| {display_path} | {coverage_percent}% |\n")

    logger.info(f"Coverage report successfully written to {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Generate coverage report')
    parser.add_argument('--skip-slow-tests', action='store_true',
                        help='Skip slow tests to reduce execution time')
    parser.add_argument('--test-path', default='tests/test_armodel',
                        help='Specify which tests to run (default: tests/test_armodel)')
    parser.add_argument('--exclude', action='append', default=[],
                        help='Patterns to exclude from testing (can be used multiple times)')
    parser.add_argument('--log-level', default='INFO',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                        help='Set logging level')

    args = parser.parse_args()

    # Update logging level based on argument
    logging.getLogger().setLevel(getattr(logging, args.log_level.upper()))

    logger.info("Starting coverage report generation process")

    # Default exclude patterns to avoid known failing tests
    exclude_patterns = args.exclude
    if not exclude_patterns:
        # Add the known failing test to exclusions
        exclude_patterns = []

    start_time = time.time()
    logger.info(f"Running pytest with coverage on {args.test_path}...")
    coverage_output = run_pytest_with_coverage(
        include_slow_tests=not args.skip_slow_tests,
        test_path=args.test_path,
        exclude_patterns=exclude_patterns
    )

    if coverage_output is None:
        logger.error("Failed to run pytest with coverage. Exiting.")
        sys.exit(1)

    logger.info("Extracting coverage data...")
    coverage_data = extract_coverage_data(coverage_output)

    if not coverage_data:
        logger.error("No coverage data found. The coverage output might be in an unexpected format.")
        logger.debug("Coverage output:\n" + coverage_output)
        sys.exit(1)

    output_file = "tests/coverage.md"
    logger.info(f"Writing coverage report to {output_file}...")
    write_coverage_report(coverage_data, output_file)

    total_time = time.time() - start_time
    logger.info(f"Coverage report generated successfully in {total_time:.2f} seconds")

    # Print summary
    total_files = len(coverage_data)
    incomplete_files = len([file_path for file_path, coverage_percent in coverage_data if coverage_percent < 100])
    complete_files = total_files - incomplete_files
    total_coverage = sum(coverage_percent for file_path, coverage_percent in coverage_data)
    avg_coverage = total_coverage / total_files if total_files > 0 else 0

    logger.info("Coverage Summary:")
    logger.info(f"- Total files: {total_files}")
    logger.info(f"- Files with complete coverage (100%): {complete_files}")
    logger.info(f"- Files with incomplete coverage: {incomplete_files}")
    logger.info(f"- Average coverage: {avg_coverage:.1f}%")
    logger.info(f"- Total execution time: {total_time:.2f} seconds")

    print("\nSummary:")
    print(f"- Total files: {total_files}")
    print(f"- Files with complete coverage (100%): {complete_files}")
    print(f"- Files with incomplete coverage: {incomplete_files}")
    print(f"- Average coverage: {avg_coverage:.1f}%")
    print(f"- Total execution time: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
