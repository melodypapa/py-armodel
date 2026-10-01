"""
Tests for reading the DIAGNOSTIC-CONTROL-DTC-SETTING element —
DiagnosticControlDTCSetting, Table 4.68 (p.111, R23-11).

DiagnosticControlDTCSetting (concrete ARElement; Table 4.68 is a minimal 2-row
table) defines one 0..1 attribute: dtcSettingClass (ref, DEST
DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS--SUBTYPES-ENUM, DTC-SETTING-CLASS-REF) —
AUTOSAR_00052.xsd group DIAGNOSTIC-CONTROL-DTC-SETTING l.33804 / complexType
l.33835. The R23-11-removed DTC-SETTING-PARAMETER (atp.Status="removed") is not
modeled and is dropped on read by design.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_control_dtc_setting.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticControlDTCSetting:
    """Tests for readDiagnosticControlDTCSetting — own element field values (Table 4.68)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticControlDTCSetting

        control_dtc_setting = DiagnosticControlDTCSetting(parent=MagicMock(), short_name="ControlDTCSetting")
        element = _snip(inner, root_tag="DIAGNOSTIC-CONTROL-DTC-SETTING")
        parser.readDiagnosticControlDTCSetting(element, control_dtc_setting)
        return control_dtc_setting

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        control_dtc_setting = self._read(parser, "<SHORT-NAME>ControlDTCSetting</SHORT-NAME>")
        assert control_dtc_setting.getShortName() == "ControlDTCSetting"

    def test_read_dtc_setting_class_ref(self, parser):
        """Test that the DTC-SETTING-CLASS-REF is read with its DEST attribute."""
        inner = '<DTC-SETTING-CLASS-REF DEST="DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS">/AUTOSAR/DiagnosticControlDtcSettings/ControlDTCSettingClass</DTC-SETTING-CLASS-REF>'
        control_dtc_setting = self._read(parser, inner)
        assert control_dtc_setting.getDtcSettingClass() is not None
        assert control_dtc_setting.getDtcSettingClass().getValue() == "/AUTOSAR/DiagnosticControlDtcSettings/ControlDTCSettingClass"
        assert control_dtc_setting.getDtcSettingClass().getDest() == "DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving dtcSettingClass unset."""
        control_dtc_setting = self._read(parser, "")
        assert control_dtc_setting.getShortName() == "ControlDTCSetting"
        assert control_dtc_setting.getDtcSettingClass() is None
