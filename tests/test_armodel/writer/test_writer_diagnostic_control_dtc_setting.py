"""
Tests for writing DIAGNOSTIC-CONTROL-DTC-SETTING elements —
DiagnosticControlDTCSetting, Table 4.68 (p.111, R23-11).

DiagnosticControlDTCSetting (concrete ARElement; Table 4.68 is a minimal 2-row
table) defines one 0..1 attribute: dtcSettingClass (ref, DTC-SETTING-CLASS-REF) —
AUTOSAR_00052.xsd group DIAGNOSTIC-CONTROL-DTC-SETTING l.33804 / complexType
l.33835. The dispatch entry is writeARPackageElement →
writeDiagnosticControlDTCSetting.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_control_dtc_setting.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticControlDTCSetting
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


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteDiagnosticControlDTCSetting:
    """Tests for writeDiagnosticControlDTCSetting — own element field values (Table 4.68)."""

    def _write(self, control_dtc_setting: DiagnosticControlDTCSetting) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticControlDTCSetting(parent, control_dtc_setting)
        return parent.find("DIAGNOSTIC-CONTROL-DTC-SETTING")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticControlDTCSetting without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticControlDtcSettings")
        package.createDiagnosticControlDTCSetting("ControlDTCSetting1")

        child = self._write(package.getReferrableElement("ControlDTCSetting1", DiagnosticControlDTCSetting))
        assert child is not None
        assert child.find("SHORT-NAME").text == "ControlDTCSetting1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_dtc_setting_class_ref(self):
        """Test that the DTC-SETTING-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticControlDtcSettings")
        control_dtc_setting = package.createDiagnosticControlDTCSetting("ControlDTCSetting1")
        control_dtc_setting.setDtcSettingClass(_ref("DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS", "/AUTOSAR/DiagnosticControlDtcSettings/ControlDTCSettingClass"))

        child = self._write(control_dtc_setting)
        assert child is not None
        ref = child.find("DTC-SETTING-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticControlDtcSettings/ControlDTCSettingClass"
        assert ref.get("DEST") == "DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS"

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticControlDTCSetting to a DIAGNOSTIC-CONTROL-DTC-SETTING element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticControlDtcSettings")
        package.createDiagnosticControlDTCSetting("ControlDTCSetting1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("ControlDTCSetting1", DiagnosticControlDTCSetting))

        child = parent.find("DIAGNOSTIC-CONTROL-DTC-SETTING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ControlDTCSetting1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field value."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticControlDtcSettings")
        control_dtc_setting = package.createDiagnosticControlDTCSetting("ControlDTCSetting1")
        control_dtc_setting.setDtcSettingClass(_ref("DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS", "/AUTOSAR/DiagnosticControlDtcSettings/ControlDTCSettingClass"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            control_dtc_setting_2 = package_2.getReferrableElement("ControlDTCSetting1", DiagnosticControlDTCSetting)
            assert control_dtc_setting_2 is not None
            assert control_dtc_setting_2.getShortName() == "ControlDTCSetting1"
            ref = control_dtc_setting_2.getDtcSettingClass()
            assert ref is not None
            assert ref.getValue() == "/AUTOSAR/DiagnosticControlDtcSettings/ControlDTCSettingClass"
            assert ref.getDest() == "DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
