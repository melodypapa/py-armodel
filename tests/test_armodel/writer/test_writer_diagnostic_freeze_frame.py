"""
Tests for writing DIAGNOSTIC-FREEZE-FRAME elements —
DiagnosticFreezeFrame, Table 4.183 (p.192, R23-11).

The XSD group DIAGNOSTIC-FREEZE-FRAME (AUTOSAR_00052.xsd l.37772) fixes
the element order CUSTOM-TRIGGER → RECORD-NUMBER (wrapper of
POSITIVE-INTEGER-VALUE-VARIATION-POINT) → TRIGGER → UPDATE.
The dispatch entry is writeARPackageElement → writeDiagnosticFreezeFrame.

recordNumber — markdown Type PositiveInteger wins over the XSD element type
POSITIVE-INTEGER-VALUE-VARIATION-POINT (Rule 0015); the value is written
through the wrapper element (DiagnosticConnectedIndicator HEALING-CYCLE-COUNTER-THRESHOLD
precedent).

TRIGGER round-trips as the typed DiagnosticRecordTriggerEnum (Table 4.182)
literal — the enum value maps back to its TRIGGER XSD token.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_freeze_frame.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFreezeFrame
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    DiagnosticRecordTriggerEnum,
    PositiveInteger,
    String,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticFreezeFrame:
    """Tests for writeDiagnosticFreezeFrame — own element field values (Table 4.183)."""

    def _make_freeze_frame(self, short_name: str = "FreezeFrame1") -> DiagnosticFreezeFrame:
        package = AUTOSAR.getInstance().createARPackage("DiagnosticFreezeFrames")
        return package.createDiagnosticFreezeFrame(short_name)

    def _populate(self, freeze_frame: DiagnosticFreezeFrame) -> DiagnosticFreezeFrame:
        freeze_frame.setCustomTrigger(String().setValue("custom trigger description"))
        freeze_frame.setRecordNumber(PositiveInteger().setValue(40))
        freeze_frame.setTrigger(DiagnosticRecordTriggerEnum().setValue(DiagnosticRecordTriggerEnum.CONFIRMED))
        freeze_frame.setUpdate(Boolean().setValue(True))
        return freeze_frame

    def test_write_all_fields_in_xsd_order(self):
        """Test that the populated fields are emitted in the XSD group element order with the spec values."""
        freeze_frame = self._populate(self._make_freeze_frame())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFreezeFrame(parent, freeze_frame)

        child = parent.find("DIAGNOSTIC-FREEZE-FRAME")
        assert child is not None
        assert [c.tag for c in child] == [
            "SHORT-NAME",
            "CUSTOM-TRIGGER",
            "RECORD-NUMBER",
            "TRIGGER",
            "UPDATE",
        ]
        assert child.find("SHORT-NAME").text == "FreezeFrame1"
        assert child.find("CUSTOM-TRIGGER").text == "custom trigger description"
        record_number = child.find("RECORD-NUMBER")
        assert record_number is not None
        assert record_number.find("POSITIVE-INTEGER-VALUE-VARIATION-POINT").text == "40"
        assert child.find("TRIGGER").text == "CONFIRMED"
        assert child.find("UPDATE").text == "true"

    def test_write_unset_fields_emit_no_children(self):
        """Test that an unpopulated DiagnosticFreezeFrame emits no own children (empty wrapper case)."""
        self._make_freeze_frame()

        parent = ET.Element("PARENT")
        freeze_frame = AUTOSAR.getInstance().getARPackages()[0].getReferrableElement("FreezeFrame1", DiagnosticFreezeFrame)
        ARXMLWriter().writeDiagnosticFreezeFrame(parent, freeze_frame)

        child = parent.find("DIAGNOSTIC-FREEZE-FRAME")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("RECORD-NUMBER") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticFreezeFrame to a DIAGNOSTIC-FREEZE-FRAME element."""
        freeze_frame = self._populate(self._make_freeze_frame())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, freeze_frame)

        child = parent.find("DIAGNOSTIC-FREEZE-FRAME")
        assert child is not None
        assert child.find("SHORT-NAME").text == "FreezeFrame1"
        assert child.find("RECORD-NUMBER/POSITIVE-INTEGER-VALUE-VARIATION-POINT").text == "40"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticFreezeFrames")
        self._populate(package.createDiagnosticFreezeFrame("FreezeFrame1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter(options={"validate": False}).save(
                file_path, document
            )  # known writer defect: writer nests attribute value in POSITIVE-INTEGER-VALUE-VARIATION-POINT child element the schema does not allow (docs/plan/xsd-validation-known-writer-defects.md)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser(options={"validate": False}).load(
                file_path, document_2
            )  # known writer defect: writer nests attribute value in POSITIVE-INTEGER-VALUE-VARIATION-POINT child element the schema does not allow (docs/plan/xsd-validation-known-writer-defects.md)
            package_2 = document_2.getARPackages()[0]
            freeze_frame_2 = package_2.getReferrableElement("FreezeFrame1", DiagnosticFreezeFrame)
            assert freeze_frame_2 is not None
            assert freeze_frame_2.getShortName() == "FreezeFrame1"
            assert freeze_frame_2.getCustomTrigger() is not None
            assert freeze_frame_2.getCustomTrigger().getValue() == "custom trigger description"
            assert freeze_frame_2.getRecordNumber() is not None
            assert freeze_frame_2.getRecordNumber().value == 40
            assert freeze_frame_2.getTrigger() is not None
            assert isinstance(freeze_frame_2.getTrigger(), DiagnosticRecordTriggerEnum)
            assert freeze_frame_2.getTrigger().getValue() == "confirmed"
            assert freeze_frame_2.getUpdate() is not None
            assert freeze_frame_2.getUpdate().value is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticFreezeFrame without own fields round-trips with unset fields."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticFreezeFrames")
        package.createDiagnosticFreezeFrame("FreezeFrame1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            freeze_frame_2 = package_2.getReferrableElement("FreezeFrame1", DiagnosticFreezeFrame)
            assert freeze_frame_2 is not None
            assert freeze_frame_2.getCustomTrigger() is None
            assert freeze_frame_2.getRecordNumber() is None
            assert freeze_frame_2.getTrigger() is None
            assert freeze_frame_2.getUpdate() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
