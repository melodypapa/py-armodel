import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerFdConfigurationRequirements

CLASS_NOTE = "This element allows the specification of ranges for the CanFD bit timing configuration parameters. These ranges are taken as requirements and shall be respected by the ECU developer."
MAX_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE = "Maximum number of time quanta in the bit time."
MAX_SAMPLE_POINT_NOTE = "The max. value of the sample point as a percentage of the total bit time."
MAX_SYNC_JUMP_WIDTH_NOTE = "The max. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors."
MAX_TRCV_DELAY_COMPENSATION_OFFSET_NOTE = "Specifies the maximum Transceiver Delay Compensation Offset in seconds. If not specified Transceiver Delay Compensation is disabled."
MIN_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE = "Minimum number of time quanta in the bit time."
MIN_SAMPLE_POINT_NOTE = "The min. value of the sample point as a percentage of the total bit time."
MIN_SYNC_JUMP_WIDTH_NOTE = "The min. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors."
MIN_TRCV_DELAY_COMPENSATION_OFFSET_NOTE = "Specifies the minimum Transceiver Delay Compensation Offset in seconds. If not specified Transceiver Delay Compensation is disabled."
PADDING_VALUE_NOTE = "Specifies the value which is used to pad unused data in CAN FD frames which are bigger than 8 byte if the length of a Pdu which was requested to be sent does not match the allowed DLC values of CAN FD."
TX_BIT_RATE_SWITCH_NOTE = (
    "Specifies if the bit rate switching shall be used for transmissions. TRUE: CAN FD frames shall be sent with bit rate switching. FALSE: CAN FD frames shall be sent without bit rate switching."
)


class TestCanControllerFdConfigurationRequirements:
    """Tests for CanControllerFdConfigurationRequirements (Table 3.17, R23-11)."""

    def test_initialization(self):
        """Test that all __init__ fields default to None"""
        req = CanControllerFdConfigurationRequirements()

        assert isinstance(req, ARObject)
        assert req.getMaxNumberOfTimeQuantaPerBit() is None
        assert req.getMaxSamplePoint() is None
        assert req.getMaxSyncJumpWidth() is None
        assert req.getMaxTrcvDelayCompensationOffset() is None
        assert req.getMinNumberOfTimeQuantaPerBit() is None
        assert req.getMinSamplePoint() is None
        assert req.getMinSyncJumpWidth() is None
        assert req.getMinTrcvDelayCompensationOffset() is None
        assert req.getPaddingValue() is None
        assert req.getTxBitRateSwitch() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.17)"""
        assert inspect.cleandoc(CanControllerFdConfigurationRequirements.__doc__).strip() == CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanControllerFdConfigurationRequirements.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.17, pp.66-67)"""
        source = inspect.getsource(CanControllerFdConfigurationRequirements.__init__)
        assert source.index("self.maxNumberOfTimeQuantaPerBit") < source.index("self.maxSamplePoint")
        assert source.index("self.maxSamplePoint") < source.index("self.maxSyncJumpWidth")
        assert source.index("self.maxSyncJumpWidth") < source.index("self.maxTrcvDelayCompensationOffset")
        assert source.index("self.maxTrcvDelayCompensationOffset") < source.index("self.minNumberOfTimeQuantaPerBit")
        assert source.index("self.minNumberOfTimeQuantaPerBit") < source.index("self.minSamplePoint")
        assert source.index("self.minSamplePoint") < source.index("self.minSyncJumpWidth")
        assert source.index("self.minSyncJumpWidth") < source.index("self.minTrcvDelayCompensationOffset")
        assert source.index("self.minTrcvDelayCompensationOffset") < source.index("self.paddingValue")
        assert source.index("self.paddingValue") < source.index("self.txBitRateSwitch")

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_get_set_max_number_of_time_quanta_per_bit(self):
        """Test maxNumberOfTimeQuantaPerBit default, guarded set chaining, None no-op and typing"""
        req = CanControllerFdConfigurationRequirements()

        assert req.getMaxNumberOfTimeQuantaPerBit() is None

        value = Integer()
        value.setValue("32")
        assert req == req.setMaxNumberOfTimeQuantaPerBit(value)
        assert req.getMaxNumberOfTimeQuantaPerBit() == value

        assert req == req.setMaxNumberOfTimeQuantaPerBit(None)
        assert req.getMaxNumberOfTimeQuantaPerBit() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.getMaxNumberOfTimeQuantaPerBit)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.setMaxNumberOfTimeQuantaPerBit)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is CanControllerFdConfigurationRequirements

    def test_max_number_of_time_quanta_per_bit_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.17)"""
        self._assert_docstring(CanControllerFdConfigurationRequirements.getMaxNumberOfTimeQuantaPerBit, MAX_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE)
        self._assert_docstring(CanControllerFdConfigurationRequirements.setMaxNumberOfTimeQuantaPerBit, MAX_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE, "maxNumberOfTimeQuantaPerBit")

    def test_get_set_max_sample_point(self):
        """Test maxSamplePoint default, guarded set chaining, None no-op and typing"""
        req = CanControllerFdConfigurationRequirements()

        assert req.getMaxSamplePoint() is None

        value = Float()
        value.setValue("0.8")
        assert req == req.setMaxSamplePoint(value)
        assert req.getMaxSamplePoint() == value

        assert req == req.setMaxSamplePoint(None)
        assert req.getMaxSamplePoint() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.getMaxSamplePoint)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.setMaxSamplePoint)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerFdConfigurationRequirements

    def test_max_sample_point_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.17)"""
        self._assert_docstring(CanControllerFdConfigurationRequirements.getMaxSamplePoint, MAX_SAMPLE_POINT_NOTE)
        self._assert_docstring(CanControllerFdConfigurationRequirements.setMaxSamplePoint, MAX_SAMPLE_POINT_NOTE, "maxSamplePoint")

    def test_get_set_max_sync_jump_width(self):
        """Test maxSyncJumpWidth default, guarded set chaining, None no-op and typing"""
        req = CanControllerFdConfigurationRequirements()

        assert req.getMaxSyncJumpWidth() is None

        value = Float()
        value.setValue("0.2")
        assert req == req.setMaxSyncJumpWidth(value)
        assert req.getMaxSyncJumpWidth() == value

        assert req == req.setMaxSyncJumpWidth(None)
        assert req.getMaxSyncJumpWidth() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.getMaxSyncJumpWidth)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.setMaxSyncJumpWidth)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerFdConfigurationRequirements

    def test_max_sync_jump_width_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.17)"""
        self._assert_docstring(CanControllerFdConfigurationRequirements.getMaxSyncJumpWidth, MAX_SYNC_JUMP_WIDTH_NOTE)
        self._assert_docstring(CanControllerFdConfigurationRequirements.setMaxSyncJumpWidth, MAX_SYNC_JUMP_WIDTH_NOTE, "maxSyncJumpWidth")

    def test_get_set_max_trcv_delay_compensation_offset(self):
        """Test maxTrcvDelayCompensationOffset default, guarded set chaining, None no-op and typing"""
        req = CanControllerFdConfigurationRequirements()

        assert req.getMaxTrcvDelayCompensationOffset() is None

        value = TimeValue()
        value.setValue("0.001")
        assert req == req.setMaxTrcvDelayCompensationOffset(value)
        assert req.getMaxTrcvDelayCompensationOffset() == value

        assert req == req.setMaxTrcvDelayCompensationOffset(None)
        assert req.getMaxTrcvDelayCompensationOffset() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.getMaxTrcvDelayCompensationOffset)
        assert getter_hints.get("return") == typing.Optional[TimeValue]

        setter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.setMaxTrcvDelayCompensationOffset)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is CanControllerFdConfigurationRequirements

    def test_max_trcv_delay_compensation_offset_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.17)"""
        self._assert_docstring(CanControllerFdConfigurationRequirements.getMaxTrcvDelayCompensationOffset, MAX_TRCV_DELAY_COMPENSATION_OFFSET_NOTE)
        self._assert_docstring(CanControllerFdConfigurationRequirements.setMaxTrcvDelayCompensationOffset, MAX_TRCV_DELAY_COMPENSATION_OFFSET_NOTE, "maxTrcvDelayCompensationOffset")

    def test_get_set_min_number_of_time_quanta_per_bit(self):
        """Test minNumberOfTimeQuantaPerBit default, guarded set chaining, None no-op and typing"""
        req = CanControllerFdConfigurationRequirements()

        assert req.getMinNumberOfTimeQuantaPerBit() is None

        value = Integer()
        value.setValue("16")
        assert req == req.setMinNumberOfTimeQuantaPerBit(value)
        assert req.getMinNumberOfTimeQuantaPerBit() == value

        assert req == req.setMinNumberOfTimeQuantaPerBit(None)
        assert req.getMinNumberOfTimeQuantaPerBit() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.getMinNumberOfTimeQuantaPerBit)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.setMinNumberOfTimeQuantaPerBit)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is CanControllerFdConfigurationRequirements

    def test_min_number_of_time_quanta_per_bit_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.17)"""
        self._assert_docstring(CanControllerFdConfigurationRequirements.getMinNumberOfTimeQuantaPerBit, MIN_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE)
        self._assert_docstring(CanControllerFdConfigurationRequirements.setMinNumberOfTimeQuantaPerBit, MIN_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE, "minNumberOfTimeQuantaPerBit")

    def test_get_set_min_sample_point(self):
        """Test minSamplePoint default, guarded set chaining, None no-op and typing"""
        req = CanControllerFdConfigurationRequirements()

        assert req.getMinSamplePoint() is None

        value = Float()
        value.setValue("0.7")
        assert req == req.setMinSamplePoint(value)
        assert req.getMinSamplePoint() == value

        assert req == req.setMinSamplePoint(None)
        assert req.getMinSamplePoint() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.getMinSamplePoint)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.setMinSamplePoint)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerFdConfigurationRequirements

    def test_min_sample_point_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.17)"""
        self._assert_docstring(CanControllerFdConfigurationRequirements.getMinSamplePoint, MIN_SAMPLE_POINT_NOTE)
        self._assert_docstring(CanControllerFdConfigurationRequirements.setMinSamplePoint, MIN_SAMPLE_POINT_NOTE, "minSamplePoint")

    def test_get_set_min_sync_jump_width(self):
        """Test minSyncJumpWidth default, guarded set chaining, None no-op and typing"""
        req = CanControllerFdConfigurationRequirements()

        assert req.getMinSyncJumpWidth() is None

        value = Float()
        value.setValue("0.1")
        assert req == req.setMinSyncJumpWidth(value)
        assert req.getMinSyncJumpWidth() == value

        assert req == req.setMinSyncJumpWidth(None)
        assert req.getMinSyncJumpWidth() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.getMinSyncJumpWidth)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.setMinSyncJumpWidth)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerFdConfigurationRequirements

    def test_min_sync_jump_width_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.17)"""
        self._assert_docstring(CanControllerFdConfigurationRequirements.getMinSyncJumpWidth, MIN_SYNC_JUMP_WIDTH_NOTE)
        self._assert_docstring(CanControllerFdConfigurationRequirements.setMinSyncJumpWidth, MIN_SYNC_JUMP_WIDTH_NOTE, "minSyncJumpWidth")

    def test_get_set_min_trcv_delay_compensation_offset(self):
        """Test minTrcvDelayCompensationOffset default, guarded set chaining, None no-op and typing"""
        req = CanControllerFdConfigurationRequirements()

        assert req.getMinTrcvDelayCompensationOffset() is None

        value = TimeValue()
        value.setValue("0.0005")
        assert req == req.setMinTrcvDelayCompensationOffset(value)
        assert req.getMinTrcvDelayCompensationOffset() == value

        assert req == req.setMinTrcvDelayCompensationOffset(None)
        assert req.getMinTrcvDelayCompensationOffset() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.getMinTrcvDelayCompensationOffset)
        assert getter_hints.get("return") == typing.Optional[TimeValue]

        setter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.setMinTrcvDelayCompensationOffset)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is CanControllerFdConfigurationRequirements

    def test_min_trcv_delay_compensation_offset_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.17)"""
        self._assert_docstring(CanControllerFdConfigurationRequirements.getMinTrcvDelayCompensationOffset, MIN_TRCV_DELAY_COMPENSATION_OFFSET_NOTE)
        self._assert_docstring(CanControllerFdConfigurationRequirements.setMinTrcvDelayCompensationOffset, MIN_TRCV_DELAY_COMPENSATION_OFFSET_NOTE, "minTrcvDelayCompensationOffset")

    def test_get_set_padding_value(self):
        """Test paddingValue default, guarded set chaining, None no-op and typing"""
        req = CanControllerFdConfigurationRequirements()

        assert req.getPaddingValue() is None

        value = PositiveInteger()
        value.setValue("8")
        assert req == req.setPaddingValue(value)
        assert req.getPaddingValue() == value

        assert req == req.setPaddingValue(None)
        assert req.getPaddingValue() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.getPaddingValue)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.setPaddingValue)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerFdConfigurationRequirements

    def test_padding_value_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.17)"""
        self._assert_docstring(CanControllerFdConfigurationRequirements.getPaddingValue, PADDING_VALUE_NOTE)
        self._assert_docstring(CanControllerFdConfigurationRequirements.setPaddingValue, PADDING_VALUE_NOTE, "paddingValue")

    def test_get_set_tx_bit_rate_switch(self):
        """Test txBitRateSwitch default, guarded set chaining, None no-op and typing"""
        req = CanControllerFdConfigurationRequirements()

        assert req.getTxBitRateSwitch() is None

        value = Boolean()
        value.setValue("true")
        assert req == req.setTxBitRateSwitch(value)
        assert req.getTxBitRateSwitch() == value

        assert req == req.setTxBitRateSwitch(None)
        assert req.getTxBitRateSwitch() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.getTxBitRateSwitch)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(CanControllerFdConfigurationRequirements.setTxBitRateSwitch)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is CanControllerFdConfigurationRequirements

    def test_tx_bit_rate_switch_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.17)"""
        self._assert_docstring(CanControllerFdConfigurationRequirements.getTxBitRateSwitch, TX_BIT_RATE_SWITCH_NOTE)
        self._assert_docstring(CanControllerFdConfigurationRequirements.setTxBitRateSwitch, TX_BIT_RATE_SWITCH_NOTE, "txBitRateSwitch")
