#!/usr/bin/env python3
"""
Performance benchmark for ARXML Parser.

Measures parsing performance for various ARXML file sizes.
Compares performance across multiple runs to detect anomalies.
"""
import time
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from statistics import mean, stdev

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from armodel.parser.arxml_parser import ARXMLParser
from armodel.models import AUTOSAR


def benchmark_parse(file_path: str, warmup: bool = False) -> float:
    """
    Benchmark parsing a single ARXML file.

    Args:
        file_path: Path to ARXML file
        warmup: If True, don't measure (warmup run)

    Returns:
        Elapsed time in seconds
    """
    parser = ARXMLParser()

    # Clear any previous data
    document = AUTOSAR.getInstance()
    document.clear()  # Call instance method instead

    start = time.time()
    parser.parse_from_file(file_path, document)
    end = time.time()

    elapsed = end - start

    if not warmup:
        # Verify the parse was successful
        assert document is not None, f"Failed to parse {file_path}"

    return elapsed


def benchmark_file(file_path: str, runs: int = 3) -> Dict[str, float]:
    """
    Benchmark a file multiple times.

    Args:
        file_path: Path to ARXML file
        runs: Number of benchmark runs

    Returns:
        Dictionary with min, max, avg, std dev times
    """
    print(f"\n{'='*70}")
    print(f"Benchmarking: {Path(file_path).name}")
    print(f"{'='*70}")

    # Warmup run (but don't call clear() during warmup)
    print("  Warmup run...", end='', flush=True)
    AUTOSAR.getInstance().clear()
    benchmark_parse(file_path, warmup=True)
    print(" ✓")

    # Benchmark runs
    times: List[float] = []
    for i in range(runs):
        elapsed = benchmark_parse(file_path)
        times.append(elapsed)
        print(f"  Run {i+1}/{runs}: {elapsed:.3f}s")

    # Calculate statistics
    min_time = min(times)
    max_time = max(times)
    avg_time = mean(times)
    std_dev = stdev(times) if len(times) > 1 else 0.0

    # Get file info
    file_size = Path(file_path).stat().st_size
    size_mb = file_size / (1024 * 1024)

    # Calculate throughput
    throughput = size_mb / avg_time if avg_time > 0 else 0

    print(f"\n  File size: {size_mb:.2f} MB")
    print(f"  Min time: {min_time:.3f}s")
    print(f"  Max time: {max_time:.3f}s")
    print(f"  Avg time: {avg_time:.3f}s")
    print(f"  Std dev:   {std_dev:.3f}s")
    print(f"  Throughput: {throughput:.2f} MB/s")

    return {
        'file': file_path,
        'size_mb': size_mb,
        'min_time': min_time,
        'max_time': max_time,
        'avg_time': avg_time,
        'std_dev': std_dev,
        'throughput': throughput,
    }


def main():
    """Run performance benchmarks on all test ARXML files."""
    print("="*70)
    print("ARXML Parser Performance Benchmark")
    print("="*70)

    # Find test ARXML files
    test_files_dir = Path(__file__).parent.parent / 'tests' / 'integration_tests' / 'test_files'
    arxml_files = sorted(test_files_dir.glob('*.arxml'))

    if not arxml_files:
        print(f"No ARXML files found in {test_files_dir}")
        return

    print(f"\nFound {len(arxml_files)} ARXML files to benchmark")
    print(f"Test files directory: {test_files_dir}")

    # Benchmark each file
    results: List[Dict] = []
    for file_path in arxml_files:
        try:
            result = benchmark_file(str(file_path), runs=3)
            results.append(result)
        except Exception as e:
            print(f"  ✗ Error: {e}")

    # Summary statistics
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")

    if results:
        total_size = sum(r['size_mb'] for r in results)
        total_time = sum(r['avg_time'] for r in results)
        overall_throughput = total_size / total_time if total_time > 0 else 0

        print(f"\n  Files parsed: {len(results)}")
        print(f"  Total size:   {total_size:.2f} MB")
        print(f"  Total time:   {total_time:.2f}s")
        print(f"  Avg per file: {total_time / len(results):.3f}s")
        print(f"  Overall throughput: {overall_throughput:.2f} MB/s")

        # Categorize by file size
        small_files = [r for r in results if r['size_mb'] < 0.1]
        medium_files = [r for r in results if 0.1 <= r['size_mb'] < 1.0]
        large_files = [r for r in results if r['size_mb'] >= 1.0]

        print(f"\n  Small files (<100KB): {len(small_files)}")
        if small_files:
            avg_time = mean(r['avg_time'] for r in small_files)
            print(f"    Avg time: {avg_time:.3f}s")

        print(f"\n  Medium files (100KB-1MB): {len(medium_files)}")
        if medium_files:
            avg_time = mean(r['avg_time'] for r in medium_files)
            print(f"    Avg time: {avg_time:.3f}s")

        print(f"\n  Large files (>=1MB): {len(large_files)}")
        if large_files:
            avg_time = mean(r['avg_time'] for r in large_files)
            print(f"    Avg time: {avg_time:.3f}s")

        # Performance guidelines
        print(f"\n{'='*70}")
        print("PERFORMANCE GUIDELINES")
        print(f"{'='*70}")
        print("""
  Small files (<100KB):  < 100ms  ✓ Excellent
                         100-200ms  ✓ Good
                         > 200ms   ⚠ Review

  Medium files (100KB-1MB): < 500ms  ✓ Excellent
                            500ms-1s  ✓ Good
                            > 1s      ⚠ Review

  Large files (>=1MB):    < 2s     ✓ Excellent
                           2s-5s     ✓ Good
                           > 5s      ⚠ Review
        """)

        # Detect potential issues
        print(f"\n{'='*70}")
        print("PERFORMANCE ANALYSIS")
        print(f"{'='*70}")

        for result in results:
            size_mb = result['size_mb']
            avg_time = result['avg_time']
            std_dev = result['std_dev']

            # Check if time is reasonable for file size
            if size_mb < 0.1 and avg_time > 0.2:
                print(f"  ⚠ {Path(result['file']).name}: Slow for size ({avg_time:.3f}s)")
            elif size_mb >= 1.0 and avg_time > 5.0:
                print(f"  ⚠ {Path(result['file']).name}: Slow for size ({avg_time:.3f}s)")

            # Check for high variance
            if std_dev > 0 and std_dev / avg_time > 0.2:
                print(f"  ⚠ {Path(result['file']).name}: High variance ({std_dev:.3f}s)")

    print(f"\n{'='*70}")
    print("Benchmark complete!")
    print(f"{'='*70}\n")


if __name__ == '__main__':
    main()
