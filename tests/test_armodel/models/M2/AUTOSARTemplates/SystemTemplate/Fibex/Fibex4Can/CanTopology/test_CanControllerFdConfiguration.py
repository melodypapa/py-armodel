import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerFdConfiguration

CLASS_NOTE = "Bit timing related configuration of a CAN controller for payload and CRC of a CAN FD frame."
PADDING_VALUE_NOTE = "Specifies the value which is used to pad unused data in CAN FD frames which are bigger than 8 byte if the length of a Pdu which was requested to be sent does not match the allowed DLC values of CAN FD."
PROP_SEG_NOTE = "Specifies propagation delay in time quantas."
SSP_OFFSET_NOTE = "Specifies the Transmitter Delay Compensation Offset in minimum time quanta. Transmitter Delay Compensation Offset is used to adjust the position of the Secondary Sample Point (SSP), relative to the beginning of the received bit. If this parameter is configured, the Transmitter Delay Compensation is done by measurement of the CAN controller. If not specified Transmitter Delay Compensation is disabled."
SYNC_JUMP_WIDTH_NOTE = "Specifies the synchronization jump width for the controller in time quantas."
TIME_SEG1_NOTE = "Specifies phase segment 1 in time quantas."
TIME_SEG2_NOTE = "Specifies phase segment 2 in time quantas."
TX_BIT_RATE_SWITCH_NOTE = (
    "Specifies if the bit rate switching shall be used for transmissions. TRUE: CAN FD frames shall be sent with bit rate switching. FALSE: CAN FD frames shall be sent without bit rate switching."
)


class TestCanControllerFdConfiguration:
    """Tests for CanControllerFdConfiguration (Table 3.16, R23-11)."""

    def test_initialization(self):
        """Test that all __init__ fields default to None"""
        configuration = CanControllerFdConfiguration()

        assert isinstance(configuration, ARObject)
        assert configuration.getPaddingValue() is None
        assert configuration.getPropSeg() is None
        assert configuration.getSspOffset() is None
        assert configuration.getSyncJumpWidth() is None
        assert configuration.getTimeSeg1() is None
        assert configuration.getTimeSeg2() is None
        assert configuration.getTxBitRateSwitch() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.16)"""
        assert inspect.cleandoc(CanControllerFdConfiguration.__doc__).strip() == CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanControllerFdConfiguration.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.16)"""
        source = inspect.getsource(CanControllerFdConfiguration.__init__)
        assert source.index("self.paddingValue") < source.index("self.propSeg")
        assert source.index("self.propSeg") < source.index("self.sspOffset")
        assert source.index("self.sspOffset") < source.index("self.syncJumpWidth")
        assert source.index("self.syncJumpWidth") < source.index("self.timeSeg1")
        assert source.index("self.timeSeg1") < source.index("self.timeSeg2")
        assert source.index("self.timeSeg2") < source.index("self.txBitRateSwitch")

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_get_set_padding_value(self):
        """Test paddingValue default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerFdConfiguration()

        assert configuration.getPaddingValue() is None

        value = PositiveInteger()
        value.setValue("8")
        assert configuration == configuration.setPaddingValue(value)
        assert configuration.getPaddingValue() == value

        assert configuration == configuration.setPaddingValue(None)
        assert configuration.getPaddingValue() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfiguration.getPaddingValue)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerFdConfiguration.setPaddingValue)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerFdConfiguration

    def test_padding_value_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.16)"""
        self._assert_docstring(CanControllerFdConfiguration.getPaddingValue, PADDING_VALUE_NOTE)
        self._assert_docstring(CanControllerFdConfiguration.setPaddingValue, PADDING_VALUE_NOTE, "paddingValue")

    def test_get_set_prop_seg(self):
        """Test propSeg default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerFdConfiguration()

        assert configuration.getPropSeg() is None

        value = PositiveInteger()
        value.setValue("4")
        assert configuration == configuration.setPropSeg(value)
        assert configuration.getPropSeg() == value

        assert configuration == configuration.setPropSeg(None)
        assert configuration.getPropSeg() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfiguration.getPropSeg)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerFdConfiguration.setPropSeg)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerFdConfiguration

    def test_prop_seg_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.16)"""
        self._assert_docstring(CanControllerFdConfiguration.getPropSeg, PROP_SEG_NOTE)
        self._assert_docstring(CanControllerFdConfiguration.setPropSeg, PROP_SEG_NOTE, "propSeg")

    def test_get_set_ssp_offset(self):
        """Test sspOffset default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerFdConfiguration()

        assert configuration.getSspOffset() is None

        value = PositiveInteger()
        value.setValue("5")
        assert configuration == configuration.setSspOffset(value)
        assert configuration.getSspOffset() == value

        assert configuration == configuration.setSspOffset(None)
        assert configuration.getSspOffset() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfiguration.getSspOffset)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerFdConfiguration.setSspOffset)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerFdConfiguration

    def test_ssp_offset_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.16)"""
        self._assert_docstring(CanControllerFdConfiguration.getSspOffset, SSP_OFFSET_NOTE)
        self._assert_docstring(CanControllerFdConfiguration.setSspOffset, SSP_OFFSET_NOTE, "sspOffset")

    def test_get_set_sync_jump_width(self):
        """Test syncJumpWidth default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerFdConfiguration()

        assert configuration.getSyncJumpWidth() is None

        value = PositiveInteger()
        value.setValue("1")
        assert configuration == configuration.setSyncJumpWidth(value)
        assert configuration.getSyncJumpWidth() == value

        assert configuration == configuration.setSyncJumpWidth(None)
        assert configuration.getSyncJumpWidth() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfiguration.getSyncJumpWidth)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerFdConfiguration.setSyncJumpWidth)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerFdConfiguration

    def test_sync_jump_width_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.16)"""
        self._assert_docstring(CanControllerFdConfiguration.getSyncJumpWidth, SYNC_JUMP_WIDTH_NOTE)
        self._assert_docstring(CanControllerFdConfiguration.setSyncJumpWidth, SYNC_JUMP_WIDTH_NOTE, "syncJumpWidth")

    def test_get_set_time_seg1(self):
        """Test timeSeg1 default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerFdConfiguration()

        assert configuration.getTimeSeg1() is None

        value = PositiveInteger()
        value.setValue("13")
        assert configuration == configuration.setTimeSeg1(value)
        assert configuration.getTimeSeg1() == value

        assert configuration == configuration.setTimeSeg1(None)
        assert configuration.getTimeSeg1() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfiguration.getTimeSeg1)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerFdConfiguration.setTimeSeg1)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerFdConfiguration

    def test_time_seg1_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.16)"""
        self._assert_docstring(CanControllerFdConfiguration.getTimeSeg1, TIME_SEG1_NOTE)
        self._assert_docstring(CanControllerFdConfiguration.setTimeSeg1, TIME_SEG1_NOTE, "timeSeg1")

    def test_get_set_time_seg2(self):
        """Test timeSeg2 default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerFdConfiguration()

        assert configuration.getTimeSeg2() is None

        value = PositiveInteger()
        value.setValue("2")
        assert configuration == configuration.setTimeSeg2(value)
        assert configuration.getTimeSeg2() == value

        assert configuration == configuration.setTimeSeg2(None)
        assert configuration.getTimeSeg2() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfiguration.getTimeSeg2)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanControllerFdConfiguration.setTimeSeg2)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanControllerFdConfiguration

    def test_time_seg2_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.16)"""
        self._assert_docstring(CanControllerFdConfiguration.getTimeSeg2, TIME_SEG2_NOTE)
        self._assert_docstring(CanControllerFdConfiguration.setTimeSeg2, TIME_SEG2_NOTE, "timeSeg2")

    def test_get_set_tx_bit_rate_switch(self):
        """Test txBitRateSwitch default, guarded set chaining, None no-op and typing"""
        configuration = CanControllerFdConfiguration()

        assert configuration.getTxBitRateSwitch() is None

        value = Boolean()
        value.setValue("true")
        assert configuration == configuration.setTxBitRateSwitch(value)
        assert configuration.getTxBitRateSwitch() == value

        assert configuration == configuration.setTxBitRateSwitch(None)
        assert configuration.getTxBitRateSwitch() == value

        getter_hints = typing.get_type_hints(CanControllerFdConfiguration.getTxBitRateSwitch)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(CanControllerFdConfiguration.setTxBitRateSwitch)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is CanControllerFdConfiguration

    def test_tx_bit_rate_switch_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.16)"""
        self._assert_docstring(CanControllerFdConfiguration.getTxBitRateSwitch, TX_BIT_RATE_SWITCH_NOTE)
        self._assert_docstring(CanControllerFdConfiguration.setTxBitRateSwitch, TX_BIT_RATE_SWITCH_NOTE, "txBitRateSwitch")
