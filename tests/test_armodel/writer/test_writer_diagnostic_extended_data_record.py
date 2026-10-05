"""
Tests for writing DIAGNOSTIC-EXTENDED-DATA-RECORD elements —
DiagnosticExtendedDataRecord, Table 4.181 (p.190, R23-11).

The XSD group DIAGNOSTIC-EXTENDED-DATA-RECORD (AUTOSAR_00052.xsd l.37166) fixes
the element order CUSTOM-TRIGGER → RECORD-ELEMENTS (wrapper of
DIAGNOSTIC-PARAMETER) → RECORD-NUMBER → TRIGGER → UPDATE.
The dispatch entry is writeARPackageElement → writeDiagnosticExtendedDataRecord.

TRIGGER round-trips as the typed DiagnosticRecordTriggerEnum (Table 4.182)
literal — the enum value maps back to its TRIGGER XSD token.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_extended_data_record.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticExtendedDataRecord
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


class TestWriteDiagnosticExtendedDataRecord:
    """Tests for writeDiagnosticExtendedDataRecord — own element field values (Table 4.181)."""

    def _make_record(self, short_name: str = "Record1") -> DiagnosticExtendedDataRecord:
        package = AUTOSAR.getInstance().createARPackage("DiagnosticExtendedDataRecords")
        return package.createDiagnosticExtendedDataRecord(short_name)

    def _populate(self, record: DiagnosticExtendedDataRecord) -> DiagnosticExtendedDataRecord:
        record.setCustomTrigger(String().setValue("custom trigger description"))
        parameter = DiagnosticParameter()
        parameter.createIdent("Param1")
        record.addRecordElement(parameter)
        record.setRecordNumber(PositiveInteger().setValue(40))
        record.setTrigger(DiagnosticRecordTriggerEnum().setValue(DiagnosticRecordTriggerEnum.CONFIRMED))
        record.setUpdate(Boolean().setValue(True))
        return record

    def test_write_all_fields_in_xsd_order(self):
        """Test that the populated fields are emitted in the XSD group element order with the spec values."""
        record = self._populate(self._make_record())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticExtendedDataRecord(parent, record)

        child = parent.find("DIAGNOSTIC-EXTENDED-DATA-RECORD")
        assert child is not None
        assert [c.tag for c in child] == [
            "SHORT-NAME",
            "CUSTOM-TRIGGER",
            "RECORD-ELEMENTS",
            "RECORD-NUMBER",
            "TRIGGER",
            "UPDATE",
        ]
        assert child.find("SHORT-NAME").text == "Record1"
        assert child.find("CUSTOM-TRIGGER").text == "custom trigger description"
        record_elements = child.find("RECORD-ELEMENTS")
        assert record_elements is not None
        assert record_elements[0].tag == "DIAGNOSTIC-PARAMETER"
        assert record_elements[0].find("IDENT/SHORT-NAME").text == "Param1"
        assert child.find("RECORD-NUMBER").text == "40"
        assert child.find("TRIGGER").text == "CONFIRMED"
        assert child.find("UPDATE").text == "true"

    def test_write_unset_fields_emit_no_children(self):
        """Test that an unpopulated DiagnosticExtendedDataRecord emits no own children (empty wrapper case)."""
        self._make_record()

        parent = ET.Element("PARENT")
        record = AUTOSAR.getInstance().getARPackages()[0].getReferrableElement("Record1", DiagnosticExtendedDataRecord)
        ARXMLWriter().writeDiagnosticExtendedDataRecord(parent, record)

        child = parent.find("DIAGNOSTIC-EXTENDED-DATA-RECORD")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("RECORD-ELEMENTS") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticExtendedDataRecord to a DIAGNOSTIC-EXTENDED-DATA-RECORD element."""
        record = self._populate(self._make_record())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, record)

        child = parent.find("DIAGNOSTIC-EXTENDED-DATA-RECORD")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Record1"
        assert child.find("RECORD-NUMBER").text == "40"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticExtendedDataRecords")
        self._populate(package.createDiagnosticExtendedDataRecord("Record1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            record_2 = package_2.getReferrableElement("Record1", DiagnosticExtendedDataRecord)
            assert record_2 is not None
            assert record_2.getShortName() == "Record1"
            assert record_2.getCustomTrigger() is not None
            assert record_2.getCustomTrigger().getValue() == "custom trigger description"
            record_elements = record_2.getRecordElements()
            assert len(record_elements) == 1
            assert record_elements[0].getIdent() is not None
            assert record_elements[0].getIdent().getShortName() == "Param1"
            assert record_2.getRecordNumber() is not None
            assert record_2.getRecordNumber().value == 40
            assert record_2.getTrigger() is not None
            assert isinstance(record_2.getTrigger(), DiagnosticRecordTriggerEnum)
            assert record_2.getTrigger().getValue() == "confirmed"
            assert record_2.getUpdate() is not None
            assert record_2.getUpdate().value is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticExtendedDataRecord without own fields round-trips with unset fields and an empty list."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticExtendedDataRecords")
        package.createDiagnosticExtendedDataRecord("Record1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            record_2 = package_2.getReferrableElement("Record1", DiagnosticExtendedDataRecord)
            assert record_2 is not None
            assert record_2.getCustomTrigger() is None
            assert record_2.getRecordElements() == []
            assert record_2.getRecordNumber() is None
            assert record_2.getTrigger() is None
            assert record_2.getUpdate() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
