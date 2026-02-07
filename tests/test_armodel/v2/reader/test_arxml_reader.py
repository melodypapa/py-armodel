"""
Unit tests for V2 ARXMLReader.

Test-Driven Development: Write test first, watch it fail, then implement.

Following V1 test structure pattern from tests/test_armodel/parser/test_arxml_parser.py
"""
import pytest
import xml.etree.ElementTree as ET
from pathlib import Path
from armodel.v2.models.models import AUTOSAR, ARPackage
from armodel.v2.reader.base_reader import ARXMLReader


class TestARXMLReader:
    """Test ARXMLReader class methods."""

    def test_load_arxml_with_single_package(self, tmp_path):
        """
        Test loading ARXML file with one AR-PACKAGE.
        Minimal test: read structure, verify objects created correctly.
        """
        # Arrange: Create a simple ARXML file
        arxml_content = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/3.2.3">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""
        arxml_file = tmp_path / "test.arxml"
        arxml_file.write_text(arxml_content)

        # Act: Load the ARXML file
        document = AUTOSAR()
        reader = ARXMLReader()
        reader.load(str(arxml_file), document)

        # Assert: Verify the package was loaded
        assert len(document.ar_packages) == 1, "Should have one AR package"
        assert document.ar_packages[0].short_name == "TestPackage", "Package name should match"

    def test_load_arxml_with_multiple_packages(self, tmp_path):
        """
        Test loading ARXML file with multiple AR-PACKAGE elements.
        """
        # Arrange
        arxml_content = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/3.2.3">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Package1</SHORT-NAME>
    </AR-PACKAGE>
    <AR-PACKAGE>
      <SHORT-NAME>Package2</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""
        arxml_file = tmp_path / "test.arxml"
        arxml_file.write_text(arxml_content)

        # Act
        document = AUTOSAR()
        reader = ARXMLReader()
        reader.load(str(arxml_file), document)

        # Assert
        assert len(document.ar_packages) == 2, "Should have two AR packages"
        assert document.ar_packages[0].short_name == "Package1"
        assert document.ar_packages[1].short_name == "Package2"

    def test_load_arxml_with_nested_packages(self, tmp_path):
        """
        Test loading ARXML file with nested AR-PACKAGE elements.
        """
        # Arrange
        arxml_content = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/3.2.3">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>ParentPackage</SHORT-NAME>
      <AR-PACKAGES>
        <AR-PACKAGE>
          <SHORT-NAME>ChildPackage</SHORT-NAME>
        </AR-PACKAGE>
      </AR-PACKAGES>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""
        arxml_file = tmp_path / "test.arxml"
        arxml_file.write_text(arxml_content)

        # Act
        document = AUTOSAR()
        reader = ARXMLReader()
        reader.load(str(arxml_file), document)

        # Assert
        assert len(document.ar_packages) == 1, "Should have one top-level package"
        parent_pkg = document.ar_packages[0]
        assert parent_pkg.short_name == "ParentPackage"
        assert len(parent_pkg.ar_packages) == 1, "Should have one nested package"
        assert parent_pkg.ar_packages[0].short_name == "ChildPackage"
