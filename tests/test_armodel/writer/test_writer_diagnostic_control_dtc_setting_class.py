"""
Tests for writing DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS elements —
DiagnosticControlDTCSettingClass, Table 4.69 (p.111, R23-11).

DiagnosticControlDTCSettingClass (Base most-derived DiagnosticServiceClass,
concrete) defines one 0..1 attribute: controlOptionRecordPresent (Boolean,
CONTROL-OPTION-RECORD-PRESENT) — AUTOSAR_00052.xsd group
DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS l.33857 / complexType l.33873.
The dispatch entry is writeARPackageElement → writeDiagnosticControlDTCSettingClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_control_dtc_setting_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticControlDTCSettingClass
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _boolean(value) -> Boolean:
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


class TestWriteDiagnosticControlDTCSettingClass:
    """Tests for writeDiagnosticControlDTCSettingClass — own element field values (Table 4.69)."""

    def _write(self, control_dtc_setting_class: DiagnosticControlDTCSettingClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticControlDTCSettingClass(parent, control_dtc_setting_class)
        return parent.find("DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticControlDTCSettingClass without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticControlDtcSettings")
        package.createDiagnosticControlDTCSettingClass("ControlDTCSettingClass1")

        child = self._write(package.getReferrableElement("ControlDTCSettingClass1", DiagnosticControlDTCSettingClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "ControlDTCSettingClass1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_control_option_record_present_true(self):
        """Test that CONTROL-OPTION-RECORD-PRESENT is emitted without spaces for true."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticControlDtcSettings")
        control_dtc_setting_class = package.createDiagnosticControlDTCSettingClass("ControlDTCSettingClass1")
        control_dtc_setting_class.setControlOptionRecordPresent(_boolean(True))

        child = self._write(control_dtc_setting_class)
        assert child is not None
        element = child.find("CONTROL-OPTION-RECORD-PRESENT")
        assert element is not None
        assert element.text == "true"

    def test_write_control_option_record_present_false(self):
        """Test that CONTROL-OPTION-RECORD-PRESENT is emitted without spaces for false."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticControlDtcSettings")
        control_dtc_setting_class = package.createDiagnosticControlDTCSettingClass("ControlDTCSettingClass1")
        control_dtc_setting_class.setControlOptionRecordPresent(_boolean(False))

        child = self._write(control_dtc_setting_class)
        element = child.find("CONTROL-OPTION-RECORD-PRESENT")
        assert element is not None
        assert element.text == "false"

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticControlDTCSettingClass to a DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticControlDtcSettings")
        package.createDiagnosticControlDTCSettingClass("ControlDTCSettingClass1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("ControlDTCSettingClass1", DiagnosticControlDTCSettingClass))

        child = parent.find("DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ControlDTCSettingClass1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field value."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticControlDtcSettings")
        control_dtc_setting_class = package.createDiagnosticControlDTCSettingClass("ControlDTCSettingClass1")
        control_dtc_setting_class.setControlOptionRecordPresent(_boolean(True))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            control_dtc_setting_class_2 = package_2.getReferrableElement("ControlDTCSettingClass1", DiagnosticControlDTCSettingClass)
            assert control_dtc_setting_class_2 is not None
            assert control_dtc_setting_class_2.getShortName() == "ControlDTCSettingClass1"
            value = control_dtc_setting_class_2.getControlOptionRecordPresent()
            assert value is not None
            assert value.getValue() is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
