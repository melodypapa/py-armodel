"""
Tests for writing DIAGNOSTIC-FUNCTION-IDENTIFIER elements —
DiagnosticFunctionIdentifier, Table 4.214 (p.215, R23-11).

DiagnosticFunctionIdentifier carries NO own Attribute rows (the XSD group
DIAGNOSTIC-FUNCTION-IDENTIFIER, AUTOSAR_00052.xsd l.37879, is an empty
xsd:sequence), so writeDiagnosticFunctionIdentifier emits the element with
the inherited Identifiable content only (SHORT-NAME, DESC, ...).
The dispatch entry is writeARPackageElement → writeDiagnosticFunctionIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_function_identifier.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFunctionIdentifier
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticFunctionIdentifier:
    """Tests for writeDiagnosticFunctionIdentifier — inherited Identifiable field values (Table 4.214)."""

    def _make_identifier(self, short_name: str = "FID1") -> DiagnosticFunctionIdentifier:
        package = AUTOSAR.getInstance().createARPackage("DiagnosticFunctionIdentifiers")
        return package.createDiagnosticFunctionIdentifier(short_name)

    def _populate_desc(self, identifier: DiagnosticFunctionIdentifier) -> DiagnosticFunctionIdentifier:
        desc = MultiLanguageOverviewParagraph()
        l2 = LOverviewParagraph()
        l2.l = "EN"
        l2.value = "FID description"
        desc.addL2(l2)
        identifier.setDesc(desc)
        return identifier

    def test_write_desc_in_element(self):
        """Test that the populated DESC is emitted with the spec value after SHORT-NAME."""
        identifier = self._populate_desc(self._make_identifier())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFunctionIdentifier(parent, identifier)

        child = parent.find("DIAGNOSTIC-FUNCTION-IDENTIFIER")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME", "DESC"]
        assert child.find("SHORT-NAME").text == "FID1"
        assert child.find("DESC/L-2").text == "FID description"

    def test_write_unset_fields_emit_no_children(self):
        """Test that an unpopulated DiagnosticFunctionIdentifier emits no own children (empty wrapper case)."""
        self._make_identifier()

        parent = ET.Element("PARENT")
        identifier = AUTOSAR.getInstance().getARPackages()[0].getReferrableElement("FID1", DiagnosticFunctionIdentifier)
        ARXMLWriter().writeDiagnosticFunctionIdentifier(parent, identifier)

        child = parent.find("DIAGNOSTIC-FUNCTION-IDENTIFIER")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("DESC") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticFunctionIdentifier to a DIAGNOSTIC-FUNCTION-IDENTIFIER element."""
        identifier = self._populate_desc(self._make_identifier())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, identifier)

        child = parent.find("DIAGNOSTIC-FUNCTION-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "FID1"
        assert child.find("DESC/L-2").text == "FID description"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticFunctionIdentifiers")
        self._populate_desc(package.createDiagnosticFunctionIdentifier("FID1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            identifier_2 = package_2.getReferrableElement("FID1", DiagnosticFunctionIdentifier)
            assert identifier_2 is not None
            assert identifier_2.getShortName() == "FID1"
            assert identifier_2.getDesc() is not None
            assert identifier_2.getDesc().getL2s()[0].getValue() == "FID description"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticFunctionIdentifier without own fields round-trips with unset fields."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticFunctionIdentifiers")
        package.createDiagnosticFunctionIdentifier("FID1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            identifier_2 = package_2.getReferrableElement("FID1", DiagnosticFunctionIdentifier)
            assert identifier_2 is not None
            assert isinstance(identifier_2, DiagnosticFunctionIdentifier)
            assert identifier_2.getDesc() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
