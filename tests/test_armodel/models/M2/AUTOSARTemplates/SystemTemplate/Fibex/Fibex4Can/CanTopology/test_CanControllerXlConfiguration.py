import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerXlConfiguration

CLASS_NOTE = "This meta-class represents the CAN XL-specific controller attributes."
ERROR_SIGNALING_ENABLED_NOTE = "Specifies if error signaling shall be enabled. This is not possible when the transceiver is switched to PWM mode (trcvPwmModeEnabled set to TRUE). TRUE: Error signaling shall be enabled. FALSE: Error signaling shall be disabled."
PROP_SEG_NOTE = "Specifies propagation delay in time quantas."
PWM_L_NOTE = "Specifies the PWM long phase length."
PWM_O_NOTE = "Specifies the PWM time offset."
PWM_S_NOTE = "Specifies the PWM short phase length."
SSP_OFFSET_NOTE = "Specifies the Transmitter Delay Compensation Offset in minimum time quanta. Transmitter Delay Compensation Offset is used to adjust the position of the Secondary Sample Point (SSP), relative to the beginning of the received bit. If this parameter is configured, the Transmitter Delay Compensation is done by measurement of the CAN controller. If not specified Transmitter Delay Compensation is disabled."
SYNC_JUMP_WIDTH_NOTE = "Specifies the synchronization jump width for the controller in time quantas."
TIME_SEG1_NOTE = "Specifies phase segment 1 in time quantas."
TIME_SEG2_NOTE = "Specifies phase segment 2 in time quantas."
TRCV_PWM_MODE_ENABLED_NOTE = "Specifies if the transceiver shall be set to the PWM mode. TRUE: The transceiver shall be switched to PWM mode. FALSE: The transceiver shall work in classic CAN mode."


class TestCanControllerXlConfiguration:
    """Tests for CanControllerXlConfiguration (Table 3.18, R23-11)."""

    def test_initialization(self):
        """Test that all __init__ fields default to None"""
        configuration = CanControllerXlConfiguration()

        assert isinstance(configuration, ARObject)
        assert configuration.getErrorSignalingEnabled() is None
        assert configuration.getPropSeg() is None
        assert configuration.getPwmL() is None
        assert configuration.getPwmO() is None
        assert configuration.getPwmS() is None
        assert configuration.getSspOffset() is None
        assert configuration.getSyncJumpWidth() is None
        assert configuration.getTimeSeg1() is None
        assert configuration.getTimeSeg2() is None
        assert configuration.getTrcvPwmModeEnabled() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.18)"""
        assert inspect.cleandoc(CanControllerXlConfiguration.__doc__).strip() == CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanControllerXlConfiguration.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.18)"""
        source = inspect.getsource(CanControllerXlConfiguration.__init__)
        assert source.index("self.errorSignalingEnabled") < source.index("self.propSeg")
        assert source.index("self.propSeg") < source.index("self.pwmL")
        assert source.index("self.pwmL") < source.index("self.pwmO")
        assert source.index("self.pwmO") < source.index("self.pwmS")
        assert source.index("self.pwmS") < source.index("self.sspOffset")
        assert source.index("self.sspOffset") < source.index("self.syncJumpWidth")
        assert source.index("self.syncJumpWidth") < source.index("self.timeSeg1")
        assert source.index("self.timeSeg1") < source.index("self.timeSeg2")
        assert source.index("self.timeSeg2") < source.index("self.trcvPwmModeEnabled")

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_get_set_error_signaling_enabled(self):
        """Test errorSignalingEnabled default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerXlConfiguration()

        assert configuration.getErrorSignalingEnabled() is None

        value = Boolean()
        value.setValue("true")
        assert configuration == configuration.setErrorSignalingEnabled(value)
        assert configuration.getErrorSignalingEnabled() == value

        assert configuration == configuration.setErrorSignalingEnabled(None)
        assert configuration.getErrorSignalingEnabled() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfiguration.getErrorSignalingEnabled)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(CanControllerXlConfiguration.setErrorSignalingEnabled)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is CanControllerXlConfiguration

    def test_error_signaling_enabled_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.18)"""
        self._assert_docstring(CanControllerXlConfiguration.getErrorSignalingEnabled, ERROR_SIGNALING_ENABLED_NOTE)
        self._assert_docstring(CanControllerXlConfiguration.setErrorSignalingEnabled, ERROR_SIGNALING_ENABLED_NOTE, "errorSignalingEnabled")

    def test_get_set_prop_seg(self):
        """Test propSeg default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerXlConfiguration()

        assert configuration.getPropSeg() is None

        value = PositiveInteger()
        value.setValue("4")
        assert configuration == configuration.setPropSeg(value)
        assert configuration.getPropSeg() == value

        assert configuration == configuration.setPropSeg(None)
        assert configuration.getPropSeg() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfiguration.getPropSeg)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfiguration.setPropSeg)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfiguration

    def test_prop_seg_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.18)"""
        self._assert_docstring(CanControllerXlConfiguration.getPropSeg, PROP_SEG_NOTE)
        self._assert_docstring(CanControllerXlConfiguration.setPropSeg, PROP_SEG_NOTE, "propSeg")

    def test_get_set_pwm_l(self):
        """Test pwmL default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerXlConfiguration()

        assert configuration.getPwmL() is None

        value = PositiveInteger()
        value.setValue("100")
        assert configuration == configuration.setPwmL(value)
        assert configuration.getPwmL() == value

        assert configuration == configuration.setPwmL(None)
        assert configuration.getPwmL() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfiguration.getPwmL)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfiguration.setPwmL)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfiguration

    def test_pwm_l_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.18)"""
        self._assert_docstring(CanControllerXlConfiguration.getPwmL, PWM_L_NOTE)
        self._assert_docstring(CanControllerXlConfiguration.setPwmL, PWM_L_NOTE, "pwmL")

    def test_get_set_pwm_o(self):
        """Test pwmO default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerXlConfiguration()

        assert configuration.getPwmO() is None

        value = PositiveInteger()
        value.setValue("20")
        assert configuration == configuration.setPwmO(value)
        assert configuration.getPwmO() == value

        assert configuration == configuration.setPwmO(None)
        assert configuration.getPwmO() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfiguration.getPwmO)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfiguration.setPwmO)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfiguration

    def test_pwm_o_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.18)"""
        self._assert_docstring(CanControllerXlConfiguration.getPwmO, PWM_O_NOTE)
        self._assert_docstring(CanControllerXlConfiguration.setPwmO, PWM_O_NOTE, "pwmO")

    def test_get_set_pwm_s(self):
        """Test pwmS default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerXlConfiguration()

        assert configuration.getPwmS() is None

        value = PositiveInteger()
        value.setValue("30")
        assert configuration == configuration.setPwmS(value)
        assert configuration.getPwmS() == value

        assert configuration == configuration.setPwmS(None)
        assert configuration.getPwmS() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfiguration.getPwmS)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfiguration.setPwmS)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfiguration

    def test_pwm_s_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.18)"""
        self._assert_docstring(CanControllerXlConfiguration.getPwmS, PWM_S_NOTE)
        self._assert_docstring(CanControllerXlConfiguration.setPwmS, PWM_S_NOTE, "pwmS")

    def test_get_set_ssp_offset(self):
        """Test sspOffset default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerXlConfiguration()

        assert configuration.getSspOffset() is None

        value = PositiveInteger()
        value.setValue("5")
        assert configuration == configuration.setSspOffset(value)
        assert configuration.getSspOffset() == value

        assert configuration == configuration.setSspOffset(None)
        assert configuration.getSspOffset() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfiguration.getSspOffset)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfiguration.setSspOffset)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfiguration

    def test_ssp_offset_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.18)"""
        self._assert_docstring(CanControllerXlConfiguration.getSspOffset, SSP_OFFSET_NOTE)
        self._assert_docstring(CanControllerXlConfiguration.setSspOffset, SSP_OFFSET_NOTE, "sspOffset")

    def test_get_set_sync_jump_width(self):
        """Test syncJumpWidth default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerXlConfiguration()

        assert configuration.getSyncJumpWidth() is None

        value = PositiveInteger()
        value.setValue("1")
        assert configuration == configuration.setSyncJumpWidth(value)
        assert configuration.getSyncJumpWidth() == value

        assert configuration == configuration.setSyncJumpWidth(None)
        assert configuration.getSyncJumpWidth() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfiguration.getSyncJumpWidth)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfiguration.setSyncJumpWidth)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfiguration

    def test_sync_jump_width_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.18)"""
        self._assert_docstring(CanControllerXlConfiguration.getSyncJumpWidth, SYNC_JUMP_WIDTH_NOTE)
        self._assert_docstring(CanControllerXlConfiguration.setSyncJumpWidth, SYNC_JUMP_WIDTH_NOTE, "syncJumpWidth")

    def test_get_set_time_seg1(self):
        """Test timeSeg1 default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerXlConfiguration()

        assert configuration.getTimeSeg1() is None

        value = PositiveInteger()
        value.setValue("61")
        assert configuration == configuration.setTimeSeg1(value)
        assert configuration.getTimeSeg1() == value

        assert configuration == configuration.setTimeSeg1(None)
        assert configuration.getTimeSeg1() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfiguration.getTimeSeg1)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfiguration.setTimeSeg1)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfiguration

    def test_time_seg1_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.18)"""
        self._assert_docstring(CanControllerXlConfiguration.getTimeSeg1, TIME_SEG1_NOTE)
        self._assert_docstring(CanControllerXlConfiguration.setTimeSeg1, TIME_SEG1_NOTE, "timeSeg1")

    def test_get_set_time_seg2(self):
        """Test timeSeg2 default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerXlConfiguration()

        assert configuration.getTimeSeg2() is None

        value = PositiveInteger()
        value.setValue("14")
        assert configuration == configuration.setTimeSeg2(value)
        assert configuration.getTimeSeg2() == value

        assert configuration == configuration.setTimeSeg2(None)
        assert configuration.getTimeSeg2() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfiguration.getTimeSeg2)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfiguration.setTimeSeg2)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfiguration

    def test_time_seg2_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.18)"""
        self._assert_docstring(CanControllerXlConfiguration.getTimeSeg2, TIME_SEG2_NOTE)
        self._assert_docstring(CanControllerXlConfiguration.setTimeSeg2, TIME_SEG2_NOTE, "timeSeg2")

    def test_get_set_trcv_pwm_mode_enabled(self):
        """Test trcvPwmModeEnabled default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerXlConfiguration()

        assert configuration.getTrcvPwmModeEnabled() is None

        value = Boolean()
        value.setValue("false")
        assert configuration == configuration.setTrcvPwmModeEnabled(value)
        assert configuration.getTrcvPwmModeEnabled() == value

        assert configuration == configuration.setTrcvPwmModeEnabled(None)
        assert configuration.getTrcvPwmModeEnabled() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfiguration.getTrcvPwmModeEnabled)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(CanControllerXlConfiguration.setTrcvPwmModeEnabled)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is CanControllerXlConfiguration

    def test_trcv_pwm_mode_enabled_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.18)"""
        self._assert_docstring(CanControllerXlConfiguration.getTrcvPwmModeEnabled, TRCV_PWM_MODE_ENABLED_NOTE)
        self._assert_docstring(CanControllerXlConfiguration.setTrcvPwmModeEnabled, TRCV_PWM_MODE_ENABLED_NOTE, "trcvPwmModeEnabled")
