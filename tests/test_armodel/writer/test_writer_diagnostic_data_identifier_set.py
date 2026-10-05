"""
Tests for writing DIAGNOSTIC-DATA-IDENTIFIER-SET elements —
DiagnosticDataIdentifierSet, Table 4.178 (p.187, R23-11).

DiagnosticDataIdentifierSet (Base most-derived DiagnosticCommonElement) carries one
* ref attribute — dataIdentifier (ordered), written as the XSD wrapper
DATA-IDENTIFIER-REFS of DATA-IDENTIFIER-REF items (DEST
DIAGNOSTIC-DATA-IDENTIFIER--SUBTYPES-ENUM) — XSD group
DIAGNOSTIC-DATA-IDENTIFIER-SET, AUTOSAR_00052.xsd l.34388. The writer reads the model
via the get* getters; the dispatch entry is writeARPackageElement →
writeDiagnosticDataIdentifierSet.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_data_identifier_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifierSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _data_identifier_ref(value: str) -> RefType:
    ref = RefType()
    ref.setDest("DIAGNOSTIC-DATA-IDENTIFIER")
    ref.setValue(value)
    return ref


class TestWriteDiagnosticDataIdentifierSet:
    """Tests for writeDiagnosticDataIdentifierSet — own element field values (Table 4.178)."""

    def test_write_refs_in_xsd_order(self):
        """Test that DATA-IDENTIFIER-REFS wraps the refs in list order."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDataIdentifierSets")
        data_identifier_set = package.createDiagnosticDataIdentifierSet("Set1")
        data_identifier_set.addDataIdentifierRef(_data_identifier_ref("/AUTOSAR/DiagnosticDataIdentifiers/DID1"))
        data_identifier_set.addDataIdentifierRef(_data_identifier_ref("/AUTOSAR/DiagnosticDataIdentifiers/DID2"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataIdentifierSet(parent, data_identifier_set)

        child = parent.find("DIAGNOSTIC-DATA-IDENTIFIER-SET")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Set1"
        ref_elements = child.findall("DATA-IDENTIFIER-REFS/DATA-IDENTIFIER-REF")
        assert len(ref_elements) == 2
        assert ref_elements[0].text == "/AUTOSAR/DiagnosticDataIdentifiers/DID1"
        assert ref_elements[0].get("DEST") == "DIAGNOSTIC-DATA-IDENTIFIER"
        assert ref_elements[1].text == "/AUTOSAR/DiagnosticDataIdentifiers/DID2"
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["DATA-IDENTIFIER-REFS"]

    def test_write_empty_set_omits_wrapper(self):
        """Test that a set without refs emits no DATA-IDENTIFIER-REFS wrapper element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDataIdentifierSets")
        package.createDiagnosticDataIdentifierSet("Set1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataIdentifierSet(parent, package.getReferrableElement("Set1", DiagnosticDataIdentifierSet))

        child = parent.find("DIAGNOSTIC-DATA-IDENTIFIER-SET")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("DATA-IDENTIFIER-REFS") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticDataIdentifierSet to a DIAGNOSTIC-DATA-IDENTIFIER-SET element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDataIdentifierSets")
        data_identifier_set = package.createDiagnosticDataIdentifierSet("Set1")
        data_identifier_set.addDataIdentifierRef(_data_identifier_ref("/AUTOSAR/DiagnosticDataIdentifiers/DID1"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, data_identifier_set)

        child = parent.find("DIAGNOSTIC-DATA-IDENTIFIER-SET")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Set1"
        assert child.find("DATA-IDENTIFIER-REFS/DATA-IDENTIFIER-REF").text == "/AUTOSAR/DiagnosticDataIdentifiers/DID1"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticDataIdentifierSets")
        data_identifier_set = package.createDiagnosticDataIdentifierSet("Set1")
        data_identifier_set.addDataIdentifierRef(_data_identifier_ref("/AUTOSAR/DiagnosticDataIdentifiers/DID1"))
        data_identifier_set.addDataIdentifierRef(_data_identifier_ref("/AUTOSAR/DiagnosticDataIdentifiers/DID2"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            data_identifier_set_2 = package_2.getReferrableElement("Set1", DiagnosticDataIdentifierSet)
            assert data_identifier_set_2 is not None
            refs = data_identifier_set_2.getDataIdentifierRefs()
            assert len(refs) == 2
            assert refs[0].getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"
            assert refs[0].getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/DID1"
            assert refs[1].getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"
            assert refs[1].getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/DID2"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticDataIdentifierSet without refs round-trips with an empty list."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticDataIdentifierSets")
        package.createDiagnosticDataIdentifierSet("Set1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            data_identifier_set_2 = package_2.getReferrableElement("Set1", DiagnosticDataIdentifierSet)
            assert data_identifier_set_2 is not None
            assert data_identifier_set_2.getDataIdentifierRefs() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
