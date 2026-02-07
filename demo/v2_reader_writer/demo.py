#!/usr/bin/env python3
"""
V2 ARXML Reader/Writer Demo

Run this from the project root using: python -m demo.v2_reader_writer.demo

Demonstrates the new V2 architecture for ARXML reading and writing:
- Models are pure data holders (no serialization logic)
- Reader/Writer use reflection to serialize/deserialize
- Schema-driven mappings (hardcoded for demo)
- V1-compatible error handling
"""
import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from demo.v2_reader_writer.models.models import AUTOSAR, ARPackage, SwComponentType
from demo.v2_reader_writer.reader.base_reader import ARXMLReader
from demo.v2_reader_writer.writer.base_writer import ARXMLWriter


def print_separator(title: str):
    """Print a separator with title."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def demo_read():
    """Demo: Read ARXML file."""
    print_separator("DEMO 1: Reading ARXML File")

    input_file = Path(__file__).parent / "sample_input.arxml"

    # Create AUTOSAR document
    document = AUTOSAR()

    # Read ARXML file
    print(f"Reading: {input_file}")
    reader = ARXMLReader()
    reader.load(str(input_file), document)

    # Display what was read
    print("\n✅ Successfully read ARXML file!")
    print(f"Number of packages: {len(document.ar_packages)}")

    for pkg in document.ar_packages:
        print(f"\n📦 Package: {pkg.short_name}")
        print(f"   Sub-packages: {len(pkg.ar_packages)}")
        print(f"   Elements: {len(pkg.elements)}")

        for elem in pkg.elements:
            if isinstance(elem, SwComponentType):
                print(f"\n   🔧 Component: {elem.short_name}")
                print(f"      Category: {elem.category}")
                print(f"      UUID: {elem.uuid}")


def demo_write():
    """Demo: Write ARXML file."""
    print_separator("DEMO 2: Writing ARXML File")

    # Create AUTOSAR document manually
    document = AUTOSAR()

    # Create package
    pkg = ARPackage()
    pkg.short_name = "TestPackage"

    # Create component
    comp = SwComponentType()
    comp.short_name = "TestComponent"
    comp.category = "APPLICATION"
    comp.uuid = "abc-123-def"

    # Add component to package
    pkg.elements.append(comp)

    # Add package to document
    document.ar_packages.append(pkg)

    # Write to file
    output_file = Path(__file__).parent / "sample_output.arxml"
    print(f"Writing: {output_file}")

    writer = ARXMLWriter(options={"format": True})
    writer.save(str(output_file), document)

    print("\n✅ Successfully wrote ARXML file!")
    print(f"Output: {output_file}")


def demo_roundtrip():
    """Demo: Round-trip (read -> write -> read)."""
    print_separator("DEMO 3: Round-Trip Test")

    input_file = Path(__file__).parent / "sample_input.arxml"
    temp_file = Path(__file__).parent / "sample_roundtrip.arxml"

    # Step 1: Read original file
    print(f"Step 1: Reading {input_file}")
    document1 = AUTOSAR()
    reader1 = ARXMLReader()
    reader1.load(str(input_file), document1)

    # Extract data
    original_pkg_name = document1.ar_packages[0].short_name
    original_comp_name = document1.ar_packages[0].elements[0].short_name
    original_comp_category = document1.ar_packages[0].elements[0].category

    print(f"   Package: {original_pkg_name}")
    print(f"   Component: {original_comp_name} ({original_comp_category})")

    # Step 2: Write to temp file
    print(f"\nStep 2: Writing to {temp_file}")
    writer = ARXMLWriter()
    writer.save(str(temp_file), document1)
    print("   ✅ Written successfully")

    # Step 3: Read temp file and verify
    print(f"\nStep 3: Reading {temp_file} for verification")
    document2 = AUTOSAR()
    reader2 = ARXMLReader()
    reader2.load(str(temp_file), document2)

    # Verify data integrity
    new_pkg_name = document2.ar_packages[0].short_name
    new_comp_name = document2.ar_packages[0].elements[0].short_name
    new_comp_category = document2.ar_packages[0].elements[0].category

    print(f"   Package: {new_pkg_name}")
    print(f"   Component: {new_comp_name} ({new_comp_category})")

    # Compare
    print("\n📊 Data Integrity Check:")
    if (original_pkg_name == new_pkg_name and
        original_comp_name == new_comp_name and
        original_comp_category == new_comp_category):
        print("   ✅ ROUND-TRIP SUCCESSFUL! All data preserved.")
    else:
        print("   ❌ ROUND-TRIP FAILED! Data mismatch.")

    # Cleanup
    if temp_file.exists():
        temp_file.unlink()
        print(f"\n   Cleaned up {temp_file}")


def main():
    """Run all demos."""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  V2 ARXML Reader/Writer Demo".center(58) + "║")
    print("║" + "  Java-Style POJO Pattern with Reflection".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")

    try:
        demo_read()
        demo_write()
        demo_roundtrip()

        print_separator("All Demos Completed!")
        print("✅ V2 reader/writer is working correctly!")
        print("\nKey Features Demonstrated:")
        print("  • Models are pure data holders (no serialization logic)")
        print("  • Reader/Writer use reflection for serialization")
        print("  • Schema-driven mappings (hardcoded for demo)")
        print("  • Round-trip preservation of data")
        print("  • V1-compatible error handling")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
