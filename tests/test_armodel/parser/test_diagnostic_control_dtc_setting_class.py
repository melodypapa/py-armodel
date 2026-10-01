"""
Tests for reading the DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS element —
DiagnosticControlDTCSettingClass, Table 4.69 (p.111, R23-11).

DiagnosticControlDTCSettingClass (Base most-derived DiagnosticServiceClass,
concrete) defines one 0..1 attribute: controlOptionRecordPresent (Boolean,
CONTROL-OPTION-RECORD-PRESENT) — AUTOSAR_00052.xsd group
DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS l.33857 / complexType l.33873.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_control_dtc_setting_class.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticControlDTCSettingClass:
    """Tests for readDiagnosticControlDTCSettingClass — own element field values (Table 4.69)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticControlDTCSettingClass

        control_dtc_setting_class = DiagnosticControlDTCSettingClass(parent=MagicMock(), short_name="ControlDTCSettingClass")
        element = _snip(inner, root_tag="DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS")
        parser.readDiagnosticControlDTCSettingClass(element, control_dtc_setting_class)
        return control_dtc_setting_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        control_dtc_setting_class = self._read(parser, "<SHORT-NAME>ControlDTCSettingClass</SHORT-NAME>")
        assert control_dtc_setting_class.getShortName() == "ControlDTCSettingClass"

    def test_read_control_option_record_present_true(self, parser):
        """Test that CONTROL-OPTION-RECORD-PRESENT is read as a Boolean true."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean

        control_dtc_setting_class = self._read(parser, "<CONTROL-OPTION-RECORD-PRESENT>true</CONTROL-OPTION-RECORD-PRESENT>")
        value = control_dtc_setting_class.getControlOptionRecordPresent()
        assert value is not None
        assert isinstance(value, Boolean)
        assert value.getValue() is True

    def test_read_control_option_record_present_false(self, parser):
        """Test that CONTROL-OPTION-RECORD-PRESENT is read as a Boolean false."""
        control_dtc_setting_class = self._read(parser, "<CONTROL-OPTION-RECORD-PRESENT>false</CONTROL-OPTION-RECORD-PRESENT>")
        value = control_dtc_setting_class.getControlOptionRecordPresent()
        assert value is not None
        assert value.getValue() is False

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving controlOptionRecordPresent unset."""
        control_dtc_setting_class = self._read(parser, "")
        assert control_dtc_setting_class.getShortName() == "ControlDTCSettingClass"
        assert control_dtc_setting_class.getControlOptionRecordPresent() is None
