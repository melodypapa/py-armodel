"""
V2 integration test for AUTOSAR_Datatypes.arxml.

This test validates that the V2 ARXML reader can parse a real AUTOSAR 4.0.3
file with complex nested structures including:
- SW-BASE-TYPE elements
- COMPU-METHOD elements
- DATA-CONSTR elements
- IMPLEMENTATION-DATA-TYPE elements
"""
import pytest
from pathlib import Path

from armodel.v2.models import AUTOSAR
from armodel.v2.reader.base_reader import ARXMLReader
from armodel.v2.writer.base_writer import ARXMLWriter


class TestV2DatatypesArxml:
    """Integration tests for V2 ARXML reader/writer with AUTOSAR_Datatypes.arxml."""

    def test_read_datatypes_arxml(self, autosar_reset, datatypes_arxml_file: Path) -> None:
        """Test reading AUTOSAR_Datatypes.arxml with V2 reader.

        Args:
            datatypes_arxml_file: Path to AUTOSAR_Datatypes.arxml test file
        """
        # Create new AUTOSAR document
        document = AUTOSAR()

        # Read ARXML file using V2 reader
        reader = ARXMLReader()
        reader.load(str(datatypes_arxml_file), document)

        # Verify top-level package structure
        assert len(document.ar_package) >= 1
        top_package = document.ar_package[0]
        assert top_package.short_name is not None
        assert top_package.short_name.value == "AUTOSAR_Platform"

    def test_roundtrip_datatypes_arxml(self, autosar_reset, datatypes_arxml_file: Path, tmp_path: Path) -> None:
        """Test round-trip parsing and writing for AUTOSAR_Datatypes.arxml.

        Args:
            datatypes_arxml_file: Path to AUTOSAR_Datatypes.arxml test file
            tmp_path: Temporary directory path
        """
        # Create document and read original file
        document1 = AUTOSAR()
        reader1 = ARXMLReader()
        reader1.load(str(datatypes_arxml_file), document1)

        # Write to temporary file
        output_file = tmp_path / "AUTOSAR_Datatypes_output.arxml"
        writer = ARXMLWriter()
        writer.save(str(output_file), document1)

        # Read the written file
        document2 = AUTOSAR()
        reader2 = ARXMLReader()
        reader2.load(str(output_file), document2)

        # Verify basic structure is preserved
        assert len(document1.ar_package) == len(document2.ar_package)

        # Verify top-level package
        pkg1 = document1.ar_package[0]
        pkg2 = document2.ar_package[0]
        assert pkg1.short_name.value == pkg2.short_name.value
        assert pkg1.short_name.value == "AUTOSAR_Platform"

        # Verify category is preserved if present
        if pkg1.category:
            assert pkg2.category is not None
            assert pkg1.category.value == pkg2.category.value

        # Verify nested packages structure exists
        assert len(pkg1.ar_packages) > 0
        assert len(pkg2.ar_packages) > 0
