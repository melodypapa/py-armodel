import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerXlConfigurationRequirements

CLASS_NOTE = "This element allows the specification of ranges for the CAN XL configuration parameters. These ranges are taken as requirements and have to be respected by the ECU developer."
ERROR_SIGNALING_ENABLED_NOTE = "Specifies if error signaling shall be enabled. This is not possible when the transceiver is switched to PWM mode (trcvPwmModeEnabled set to TRUE). TRUE: Error signaling shall be enabled. FALSE: Error signaling shall be disabled."
MAX_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE = "Maximum number of time quanta in the bit time."
MAX_PWM_L_NOTE = "Specifies the maximum PWM long phase length."
MAX_PWM_O_NOTE = "Specifies the minimum PWM time offset."
MAX_PWM_S_NOTE = "Specifies the maximum PWM short phase length."
MAX_SAMPLE_POINT_NOTE = "The max. value of the sample point as a percentage of the total bit time."
MAX_SYNC_JUMP_WIDTH_NOTE = "The max. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors."
MAX_TRCV_DELAY_COMPENSATION_OFFSET_NOTE = "Specifies the maximum Transceiver Delay Compensation Offset in seconds. If not specified Transceiver Delay Compensation is disabled."
MIN_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE = "Minimum number of time quanta in the bit time."
MIN_PWM_L_NOTE = "Specifies the minimum PWM long phase length."
MIN_PWM_O_NOTE = "Specifies the maximum PWM time offset."
MIN_PWM_S_NOTE = "Specifies the minimum PWM short phase length."
MIN_SAMPLE_POINT_NOTE = "The min. value of the sample point as a percentage of the total bit time."
MIN_SYNC_JUMP_WIDTH_NOTE = "The min. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors."
MIN_TRCV_DELAY_COMPENSATION_OFFSET_NOTE = "Specifies the minimum Transceiver Delay Compensation Offset in seconds. If not specified Transceiver Delay Compensation is disabled."
TRCV_PWM_MODE_ENABLED_NOTE = "Specifies if the transceiver shall be set to the PWM mode. TRUE: The transceiver shall be switched to PWM mode. FALSE: The transceiver shall work in classic CAN mode."


class TestCanControllerXlConfigurationRequirements:
    """Tests for CanControllerXlConfigurationRequirements (Table 3.19, R23-11)."""

    def test_initialization(self):
        """Test that all __init__ fields default to None"""
        requirements = CanControllerXlConfigurationRequirements()

        assert isinstance(requirements, ARObject)
        assert requirements.getErrorSignalingEnabled() is None
        assert requirements.getMaxNumberOfTimeQuantaPerBit() is None
        assert requirements.getMaxPwmL() is None
        assert requirements.getMaxPwmO() is None
        assert requirements.getMaxPwmS() is None
        assert requirements.getMaxSamplePoint() is None
        assert requirements.getMaxSyncJumpWidth() is None
        assert requirements.getMaxTrcvDelayCompensationOffset() is None
        assert requirements.getMinNumberOfTimeQuantaPerBit() is None
        assert requirements.getMinPwmL() is None
        assert requirements.getMinPwmO() is None
        assert requirements.getMinPwmS() is None
        assert requirements.getMinSamplePoint() is None
        assert requirements.getMinSyncJumpWidth() is None
        assert requirements.getMinTrcvDelayCompensationOffset() is None
        assert requirements.getTrcvPwmModeEnabled() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.19)"""
        assert inspect.cleandoc(CanControllerXlConfigurationRequirements.__doc__).strip() == CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanControllerXlConfigurationRequirements.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.19)"""
        source = inspect.getsource(CanControllerXlConfigurationRequirements.__init__)
        assert source.index("self.errorSignalingEnabled") < source.index("self.maxNumberOfTimeQuantaPerBit")
        assert source.index("self.maxNumberOfTimeQuantaPerBit") < source.index("self.maxPwmL")
        assert source.index("self.maxPwmL") < source.index("self.maxPwmO")
        assert source.index("self.maxPwmO") < source.index("self.maxPwmS")
        assert source.index("self.maxPwmS") < source.index("self.maxSamplePoint")
        assert source.index("self.maxSamplePoint") < source.index("self.maxSyncJumpWidth")
        assert source.index("self.maxSyncJumpWidth") < source.index("self.maxTrcvDelayCompensationOffset")
        assert source.index("self.maxTrcvDelayCompensationOffset") < source.index("self.minNumberOfTimeQuantaPerBit")
        assert source.index("self.minNumberOfTimeQuantaPerBit") < source.index("self.minPwmL")
        assert source.index("self.minPwmL") < source.index("self.minPwmO")
        assert source.index("self.minPwmO") < source.index("self.minPwmS")
        assert source.index("self.minPwmS") < source.index("self.minSamplePoint")
        assert source.index("self.minSamplePoint") < source.index("self.minSyncJumpWidth")
        assert source.index("self.minSyncJumpWidth") < source.index("self.minTrcvDelayCompensationOffset")
        assert source.index("self.minTrcvDelayCompensationOffset") < source.index("self.trcvPwmModeEnabled")

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_get_set_error_signaling_enabled(self):
        """Test errorSignalingEnabled default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getErrorSignalingEnabled() is None

        value = Boolean()
        value.setValue("true")
        assert requirements == requirements.setErrorSignalingEnabled(value)
        assert requirements.getErrorSignalingEnabled() == value

        assert requirements == requirements.setErrorSignalingEnabled(None)
        assert requirements.getErrorSignalingEnabled() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getErrorSignalingEnabled)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setErrorSignalingEnabled)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_error_signaling_enabled_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getErrorSignalingEnabled, ERROR_SIGNALING_ENABLED_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setErrorSignalingEnabled, ERROR_SIGNALING_ENABLED_NOTE, "errorSignalingEnabled")

    def test_get_set_max_number_of_time_quanta_per_bit(self):
        """Test maxNumberOfTimeQuantaPerBit default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMaxNumberOfTimeQuantaPerBit() is None

        value = Integer()
        value.setValue("32")
        assert requirements == requirements.setMaxNumberOfTimeQuantaPerBit(value)
        assert requirements.getMaxNumberOfTimeQuantaPerBit() == value

        assert requirements == requirements.setMaxNumberOfTimeQuantaPerBit(None)
        assert requirements.getMaxNumberOfTimeQuantaPerBit() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMaxNumberOfTimeQuantaPerBit)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMaxNumberOfTimeQuantaPerBit)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_max_number_of_time_quanta_per_bit_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMaxNumberOfTimeQuantaPerBit, MAX_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMaxNumberOfTimeQuantaPerBit, MAX_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE, "maxNumberOfTimeQuantaPerBit")

    def test_get_set_max_pwm_l(self):
        """Test maxPwmL default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMaxPwmL() is None

        value = PositiveInteger()
        value.setValue("100")
        assert requirements == requirements.setMaxPwmL(value)
        assert requirements.getMaxPwmL() == value

        assert requirements == requirements.setMaxPwmL(None)
        assert requirements.getMaxPwmL() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMaxPwmL)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMaxPwmL)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_max_pwm_l_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMaxPwmL, MAX_PWM_L_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMaxPwmL, MAX_PWM_L_NOTE, "maxPwmL")

    def test_get_set_max_pwm_o(self):
        """Test maxPwmO default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMaxPwmO() is None

        value = PositiveInteger()
        value.setValue("20")
        assert requirements == requirements.setMaxPwmO(value)
        assert requirements.getMaxPwmO() == value

        assert requirements == requirements.setMaxPwmO(None)
        assert requirements.getMaxPwmO() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMaxPwmO)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMaxPwmO)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_max_pwm_o_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMaxPwmO, MAX_PWM_O_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMaxPwmO, MAX_PWM_O_NOTE, "maxPwmO")

    def test_get_set_max_pwm_s(self):
        """Test maxPwmS default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMaxPwmS() is None

        value = PositiveInteger()
        value.setValue("30")
        assert requirements == requirements.setMaxPwmS(value)
        assert requirements.getMaxPwmS() == value

        assert requirements == requirements.setMaxPwmS(None)
        assert requirements.getMaxPwmS() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMaxPwmS)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMaxPwmS)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_max_pwm_s_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMaxPwmS, MAX_PWM_S_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMaxPwmS, MAX_PWM_S_NOTE, "maxPwmS")

    def test_get_set_max_sample_point(self):
        """Test maxSamplePoint default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMaxSamplePoint() is None

        value = Float()
        value.setValue("0.8")
        assert requirements == requirements.setMaxSamplePoint(value)
        assert requirements.getMaxSamplePoint() == value

        assert requirements == requirements.setMaxSamplePoint(None)
        assert requirements.getMaxSamplePoint() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMaxSamplePoint)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMaxSamplePoint)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_max_sample_point_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMaxSamplePoint, MAX_SAMPLE_POINT_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMaxSamplePoint, MAX_SAMPLE_POINT_NOTE, "maxSamplePoint")

    def test_get_set_max_sync_jump_width(self):
        """Test maxSyncJumpWidth default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMaxSyncJumpWidth() is None

        value = Float()
        value.setValue("0.2")
        assert requirements == requirements.setMaxSyncJumpWidth(value)
        assert requirements.getMaxSyncJumpWidth() == value

        assert requirements == requirements.setMaxSyncJumpWidth(None)
        assert requirements.getMaxSyncJumpWidth() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMaxSyncJumpWidth)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMaxSyncJumpWidth)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_max_sync_jump_width_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMaxSyncJumpWidth, MAX_SYNC_JUMP_WIDTH_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMaxSyncJumpWidth, MAX_SYNC_JUMP_WIDTH_NOTE, "maxSyncJumpWidth")

    def test_get_set_max_trcv_delay_compensation_offset(self):
        """Test maxTrcvDelayCompensationOffset default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMaxTrcvDelayCompensationOffset() is None

        value = TimeValue()
        value.setValue("0.001")
        assert requirements == requirements.setMaxTrcvDelayCompensationOffset(value)
        assert requirements.getMaxTrcvDelayCompensationOffset() == value

        assert requirements == requirements.setMaxTrcvDelayCompensationOffset(None)
        assert requirements.getMaxTrcvDelayCompensationOffset() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMaxTrcvDelayCompensationOffset)
        assert getter_hints.get("return") == typing.Optional[TimeValue]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMaxTrcvDelayCompensationOffset)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_max_trcv_delay_compensation_offset_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMaxTrcvDelayCompensationOffset, MAX_TRCV_DELAY_COMPENSATION_OFFSET_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMaxTrcvDelayCompensationOffset, MAX_TRCV_DELAY_COMPENSATION_OFFSET_NOTE, "maxTrcvDelayCompensationOffset")

    def test_get_set_min_number_of_time_quanta_per_bit(self):
        """Test minNumberOfTimeQuantaPerBit default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMinNumberOfTimeQuantaPerBit() is None

        value = Integer()
        value.setValue("16")
        assert requirements == requirements.setMinNumberOfTimeQuantaPerBit(value)
        assert requirements.getMinNumberOfTimeQuantaPerBit() == value

        assert requirements == requirements.setMinNumberOfTimeQuantaPerBit(None)
        assert requirements.getMinNumberOfTimeQuantaPerBit() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMinNumberOfTimeQuantaPerBit)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMinNumberOfTimeQuantaPerBit)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_min_number_of_time_quanta_per_bit_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMinNumberOfTimeQuantaPerBit, MIN_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMinNumberOfTimeQuantaPerBit, MIN_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE, "minNumberOfTimeQuantaPerBit")

    def test_get_set_min_pwm_l(self):
        """Test minPwmL default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMinPwmL() is None

        value = PositiveInteger()
        value.setValue("3")
        assert requirements == requirements.setMinPwmL(value)
        assert requirements.getMinPwmL() == value

        assert requirements == requirements.setMinPwmL(None)
        assert requirements.getMinPwmL() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMinPwmL)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMinPwmL)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_min_pwm_l_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMinPwmL, MIN_PWM_L_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMinPwmL, MIN_PWM_L_NOTE, "minPwmL")

    def test_get_set_min_pwm_o(self):
        """Test minPwmO default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMinPwmO() is None

        value = PositiveInteger()
        value.setValue("4")
        assert requirements == requirements.setMinPwmO(value)
        assert requirements.getMinPwmO() == value

        assert requirements == requirements.setMinPwmO(None)
        assert requirements.getMinPwmO() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMinPwmO)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMinPwmO)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_min_pwm_o_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMinPwmO, MIN_PWM_O_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMinPwmO, MIN_PWM_O_NOTE, "minPwmO")

    def test_get_set_min_pwm_s(self):
        """Test minPwmS default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMinPwmS() is None

        value = PositiveInteger()
        value.setValue("5")
        assert requirements == requirements.setMinPwmS(value)
        assert requirements.getMinPwmS() == value

        assert requirements == requirements.setMinPwmS(None)
        assert requirements.getMinPwmS() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMinPwmS)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMinPwmS)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_min_pwm_s_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMinPwmS, MIN_PWM_S_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMinPwmS, MIN_PWM_S_NOTE, "minPwmS")

    def test_get_set_min_sample_point(self):
        """Test minSamplePoint default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMinSamplePoint() is None

        value = Float()
        value.setValue("0.7")
        assert requirements == requirements.setMinSamplePoint(value)
        assert requirements.getMinSamplePoint() == value

        assert requirements == requirements.setMinSamplePoint(None)
        assert requirements.getMinSamplePoint() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMinSamplePoint)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMinSamplePoint)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_min_sample_point_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMinSamplePoint, MIN_SAMPLE_POINT_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMinSamplePoint, MIN_SAMPLE_POINT_NOTE, "minSamplePoint")

    def test_get_set_min_sync_jump_width(self):
        """Test minSyncJumpWidth default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMinSyncJumpWidth() is None

        value = Float()
        value.setValue("0.1")
        assert requirements == requirements.setMinSyncJumpWidth(value)
        assert requirements.getMinSyncJumpWidth() == value

        assert requirements == requirements.setMinSyncJumpWidth(None)
        assert requirements.getMinSyncJumpWidth() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMinSyncJumpWidth)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMinSyncJumpWidth)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_min_sync_jump_width_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMinSyncJumpWidth, MIN_SYNC_JUMP_WIDTH_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMinSyncJumpWidth, MIN_SYNC_JUMP_WIDTH_NOTE, "minSyncJumpWidth")

    def test_get_set_min_trcv_delay_compensation_offset(self):
        """Test minTrcvDelayCompensationOffset default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getMinTrcvDelayCompensationOffset() is None

        value = TimeValue()
        value.setValue("0.0005")
        assert requirements == requirements.setMinTrcvDelayCompensationOffset(value)
        assert requirements.getMinTrcvDelayCompensationOffset() == value

        assert requirements == requirements.setMinTrcvDelayCompensationOffset(None)
        assert requirements.getMinTrcvDelayCompensationOffset() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getMinTrcvDelayCompensationOffset)
        assert getter_hints.get("return") == typing.Optional[TimeValue]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setMinTrcvDelayCompensationOffset)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_min_trcv_delay_compensation_offset_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getMinTrcvDelayCompensationOffset, MIN_TRCV_DELAY_COMPENSATION_OFFSET_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setMinTrcvDelayCompensationOffset, MIN_TRCV_DELAY_COMPENSATION_OFFSET_NOTE, "minTrcvDelayCompensationOffset")

    def test_get_set_trcv_pwm_mode_enabled(self):
        """Test trcvPwmModeEnabled default, guarded set chaining, None no-op and typing"""
        requirements = CanControllerXlConfigurationRequirements()

        assert requirements.getTrcvPwmModeEnabled() is None

        value = Boolean()
        value.setValue("false")
        assert requirements == requirements.setTrcvPwmModeEnabled(value)
        assert requirements.getTrcvPwmModeEnabled() == value

        assert requirements == requirements.setTrcvPwmModeEnabled(None)
        assert requirements.getTrcvPwmModeEnabled() == value

        getter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.getTrcvPwmModeEnabled)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(CanControllerXlConfigurationRequirements.setTrcvPwmModeEnabled)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is CanControllerXlConfigurationRequirements

    def test_trcv_pwm_mode_enabled_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.19)"""
        self._assert_docstring(CanControllerXlConfigurationRequirements.getTrcvPwmModeEnabled, TRCV_PWM_MODE_ENABLED_NOTE)
        self._assert_docstring(CanControllerXlConfigurationRequirements.setTrcvPwmModeEnabled, TRCV_PWM_MODE_ENABLED_NOTE, "trcvPwmModeEnabled")
