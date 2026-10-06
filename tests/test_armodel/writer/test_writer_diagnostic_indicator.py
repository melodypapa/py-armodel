"""
Tests for writing DIAGNOSTIC-INDICATOR elements —
DiagnosticIndicator, Table 4.199 (p.203, R23-11).

The XSD group DIAGNOSTIC-INDICATOR (AUTOSAR_00052.xsd l.38096) fixes
the element order TYPE; the preceding HEALING-CYCLE-COUNTER-THRESHOLD
carries atp.Status="removed" and is not modeled (Rule 0015).
The dispatch entry is writeARPackageElement → writeDiagnosticIndicator.

type — markdown Type DiagnosticIndicatorTypeEnum wins over the XSD element
type DIAGNOSTIC-INDICATOR-TYPE-ENUM-VALUE-VARIATION-POINT (atpMixedString —
value carried as element text, Rule 0015); the literal is written as the
TYPE element text (DiagnosticAging THRESHOLD flattened precedent).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_indicator.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticIndicatorTypeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIndicator
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticIndicator:
    """Tests for writeDiagnosticIndicator — own element field values (Table 4.199)."""

    def _make_indicator(self, short_name: str = "Indicator1") -> DiagnosticIndicator:
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIndicators")
        return package.createDiagnosticIndicator(short_name)

    def _populate(self, indicator: DiagnosticIndicator) -> DiagnosticIndicator:
        indicator.setType(DiagnosticIndicatorTypeEnum().setValue(DiagnosticIndicatorTypeEnum.MALFUNCTION))
        return indicator

    def test_write_all_fields_in_xsd_order(self):
        """Test that the populated fields are emitted in the XSD group element order with the spec values."""
        indicator = self._populate(self._make_indicator())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticIndicator(parent, indicator)

        child = parent.find("DIAGNOSTIC-INDICATOR")
        assert child is not None
        assert [c.tag for c in child] == [
            "SHORT-NAME",
            "TYPE",
        ]
        assert child.find("SHORT-NAME").text == "Indicator1"
        assert child.find("TYPE").text == "MALFUNCTION"

    def test_write_unset_fields_emit_no_children(self):
        """Test that an unpopulated DiagnosticIndicator emits no own children (empty wrapper case)."""
        self._make_indicator()

        parent = ET.Element("PARENT")
        indicator = AUTOSAR.getInstance().getARPackages()[0].getReferrableElement("Indicator1", DiagnosticIndicator)
        ARXMLWriter().writeDiagnosticIndicator(parent, indicator)

        child = parent.find("DIAGNOSTIC-INDICATOR")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("TYPE") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticIndicator to a DIAGNOSTIC-INDICATOR element."""
        indicator = self._populate(self._make_indicator())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, indicator)

        child = parent.find("DIAGNOSTIC-INDICATOR")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Indicator1"
        assert child.find("TYPE").text == "MALFUNCTION"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticIndicators")
        self._populate(package.createDiagnosticIndicator("Indicator1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            indicator_2 = package_2.getReferrableElement("Indicator1", DiagnosticIndicator)
            assert indicator_2 is not None
            assert indicator_2.getShortName() == "Indicator1"
            assert indicator_2.getType() is not None
            assert indicator_2.getType().getValue() == DiagnosticIndicatorTypeEnum.MALFUNCTION
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticIndicator without own fields round-trips with unset fields."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticIndicators")
        package.createDiagnosticIndicator("Indicator1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            indicator_2 = package_2.getReferrableElement("Indicator1", DiagnosticIndicator)
            assert indicator_2 is not None
            assert indicator_2.getType() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
