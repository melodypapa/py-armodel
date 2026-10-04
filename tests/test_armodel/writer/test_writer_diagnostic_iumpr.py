"""
Tests for writing DIAGNOSTIC-IUMPR elements —
DiagnosticIumpr, Table 4.207 (p.210, R23-11).

The XSD group DIAGNOSTIC-IUMPR (AUTOSAR_00052.xsd l.38622) fixes
the element order EVENT-REF; RATIO-KIND.
The dispatch entry is writeARPackageElement → writeDiagnosticIumpr.

ratioKind round-trips as the typed DiagnosticIumprKindEnum (Table 4.208)
literal — the enum value maps back to its RATIO-KIND XSD token.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_iumpr.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIumpr
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticIumprKindEnum, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticIumpr:
    """Tests for writeDiagnosticIumpr — own element field values (Table 4.207)."""

    def _make_iumpr(self, short_name: str = "Iumpr1") -> DiagnosticIumpr:
        package = AUTOSAR.getInstance().createARPackage("DiagnosticIumprs")
        return package.createDiagnosticIumpr(short_name)

    def _populate(self, iumpr: DiagnosticIumpr) -> DiagnosticIumpr:
        iumpr.setEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent").setDest("DIAGNOSTIC-EVENT"))
        iumpr.setRatioKind(DiagnosticIumprKindEnum().setValue(DiagnosticIumprKindEnum.OBSERVER_BASED))
        return iumpr

    def test_write_all_fields_in_xsd_order(self):
        """Test that the populated fields are emitted in the XSD group element order with the spec values."""
        iumpr = self._populate(self._make_iumpr())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticIumpr(parent, iumpr)

        child = parent.find("DIAGNOSTIC-IUMPR")
        assert child is not None
        assert [c.tag for c in child] == [
            "SHORT-NAME",
            "EVENT-REF",
            "RATIO-KIND",
        ]
        assert child.find("SHORT-NAME").text == "Iumpr1"
        assert child.find("EVENT-REF").text == "/AUTOSAR/DiagnosticEvent"
        assert child.find("EVENT-REF").attrib["DEST"] == "DIAGNOSTIC-EVENT"
        assert child.find("RATIO-KIND").text == "OBSERVER-BASED"

    def test_write_unset_fields_emit_no_children(self):
        """Test that an unpopulated DiagnosticIumpr emits no own children (empty wrapper case)."""
        self._make_iumpr()

        parent = ET.Element("PARENT")
        iumpr = AUTOSAR.getInstance().getARPackages()[0].getReferrableElement("Iumpr1", DiagnosticIumpr)
        ARXMLWriter().writeDiagnosticIumpr(parent, iumpr)

        child = parent.find("DIAGNOSTIC-IUMPR")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("EVENT-REF") is None
        assert child.find("RATIO-KIND") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticIumpr to a DIAGNOSTIC-IUMPR element."""
        iumpr = self._populate(self._make_iumpr())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, iumpr)

        child = parent.find("DIAGNOSTIC-IUMPR")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Iumpr1"
        assert child.find("EVENT-REF").text == "/AUTOSAR/DiagnosticEvent"
        assert child.find("RATIO-KIND").text == "OBSERVER-BASED"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticIumprs")
        self._populate(package.createDiagnosticIumpr("Iumpr1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            iumpr_2 = package_2.getReferrableElement("Iumpr1", DiagnosticIumpr)
            assert iumpr_2 is not None
            assert iumpr_2.getShortName() == "Iumpr1"
            assert iumpr_2.getEventRef() is not None
            assert iumpr_2.getEventRef().getValue() == "/AUTOSAR/DiagnosticEvent"
            assert iumpr_2.getEventRef().getDest() == "DIAGNOSTIC-EVENT"
            assert iumpr_2.getRatioKind() is not None
            assert isinstance(iumpr_2.getRatioKind(), DiagnosticIumprKindEnum)
            assert iumpr_2.getRatioKind().getValue() == "observerBased"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticIumpr without own fields round-trips with unset fields."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticIumprs")
        package.createDiagnosticIumpr("Iumpr1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            iumpr_2 = package_2.getReferrableElement("Iumpr1", DiagnosticIumpr)
            assert iumpr_2 is not None
            assert iumpr_2.getEventRef() is None
            assert iumpr_2.getRatioKind() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
