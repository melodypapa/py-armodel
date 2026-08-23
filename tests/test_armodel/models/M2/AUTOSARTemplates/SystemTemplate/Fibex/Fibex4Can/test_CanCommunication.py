"""
Test suite for CAN Communication classes in AUTOSAR System Template.

This module contains comprehensive unit tests for CAN communication-related
classes including RxIdentifierRange, CanFrame, and CanFrameTriggering.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrame,
    CanFrameRxBehaviorEnum,
    CanFrameTriggering,
    CanFrameTxBehaviorEnum,
    CanXlFrameTriggeringProps,
    RxIdentifierRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication import TtcanAbsolutelyScheduledTiming
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering


class MockParent(ARObject):
    """
    Mock parent class for testing purposes.

    This class extends ARObject to provide a concrete implementation
    that can be used as a parent for testing classes that require
    an ARObject instance during initialization.
    """

    def __init__(self):
        super().__init__()


class Test_Fibex4CanCommunication:
    """
    Test class for CAN Communication module functionality.

    This class contains test methods for validating the behavior of
    CAN communication classes, including their initialization,
    inheritance relationships, and property accessors.
    """

    def test_CanAddressingModeType(self):
        """Test CanAddressingModeType enum (Table 6.111)."""
        enum = CanAddressingModeType()
        assert enum is not None
        enum.setValue(CanAddressingModeType.ENUM_EXTENDED)
        assert enum.getValue() == "EXTENDED"

        assert CanAddressingModeType.ENUM_EXTENDED == "EXTENDED"
        assert CanAddressingModeType.ENUM_STANDARD == "STANDARD"

        assert CanAddressingModeType.ENUM_EXTENDED in enum.getEnumValues()
        assert CanAddressingModeType.ENUM_STANDARD in enum.getEnumValues()
        assert len(enum.getEnumValues()) == 2

    def test_RxIdentifierRange_initialization(self):
        """Test RxIdentifierRange default state (Table 6.112)."""
        range_obj = RxIdentifierRange()

        assert isinstance(range_obj, ARObject)
        assert range_obj.getLowerCanId() is None
        assert range_obj.getUpperCanId() is None

    def test_RxIdentifierRange_get_set(self):
        """Test RxIdentifierRange getter/setter with None no-op (Table 6.112)."""
        range_obj = RxIdentifierRange()

        assert range_obj == range_obj.setLowerCanId(PositiveInteger().setValue(0x100))
        assert range_obj.getLowerCanId().getValue() == 0x100
        assert range_obj == range_obj.setLowerCanId(None)
        assert range_obj.getLowerCanId().getValue() == 0x100

        assert range_obj == range_obj.setUpperCanId(PositiveInteger().setValue(0x1FF))
        assert range_obj.getUpperCanId().getValue() == 0x1FF
        assert range_obj == range_obj.setUpperCanId(None)
        assert range_obj.getUpperCanId().getValue() == 0x1FF

    def test_CanFrame(self):
        """Test CanFrame class functionality (Table 6.109)."""
        parent = MockParent()
        frame = CanFrame(parent, "CanFrame")

        assert isinstance(frame, ARObject)
        assert isinstance(frame, Frame)

    def test_CanFrameTriggering_initialization(self):
        """Test CanFrameTriggering default state (Table 6.110)."""
        parent = MockParent()
        triggering = CanFrameTriggering(parent, "CanFrameTriggering")

        assert isinstance(triggering, FrameTriggering)
        assert triggering.getAbsolutelyScheduledTimings() == []
        assert triggering.getCanAddressingMode() is None
        assert triggering.getCanFrameRxBehavior() is None
        assert triggering.getCanFrameTxBehavior() is None
        assert triggering.getCanXlFrameTriggeringProps() is None
        assert triggering.getIdentifier() is None
        assert triggering.getJ1939requestable() is None
        assert triggering.getRxIdentifierRange() is None
        assert triggering.getRxMask() is None
        assert triggering.getTxMask() is None

    def test_CanFrameTriggering_get_set_attributes(self):
        """Test CanFrameTriggering attribute getters/setters with None no-op (Table 6.110)."""
        parent = MockParent()
        triggering = CanFrameTriggering(parent, "CanFrameTriggering")

        mode = ARLiteral()
        mode.setValue("STANDARD")
        assert triggering == triggering.setCanAddressingMode(mode)
        assert triggering.getCanAddressingMode() == mode
        assert triggering == triggering.setCanAddressingMode(None)
        assert triggering.getCanAddressingMode() == mode

        rx = ARLiteral()
        rx.setValue(CanFrameRxBehaviorEnum.ENUM_CAN_FD)
        assert triggering == triggering.setCanFrameRxBehavior(rx)
        assert triggering.getCanFrameRxBehavior() == rx

        tx = ARLiteral()
        tx.setValue(CanFrameTxBehaviorEnum.ENUM_CAN_20)
        assert triggering == triggering.setCanFrameTxBehavior(tx)
        assert triggering.getCanFrameTxBehavior() == tx

        assert triggering == triggering.setIdentifier(Integer().setValue(0x100))
        assert triggering.getIdentifier().getValue() == 0x100
        assert triggering == triggering.setIdentifier(None)
        assert triggering.getIdentifier().getValue() == 0x100

        assert triggering == triggering.setJ1939requestable(Boolean().setValue(True))
        assert triggering.getJ1939requestable().getValue() is True

        assert triggering == triggering.setRxMask(PositiveInteger().setValue(0x7FF))
        assert triggering.getRxMask().getValue() == 0x7FF
        assert triggering == triggering.setRxMask(None)
        assert triggering.getRxMask().getValue() == 0x7FF

        assert triggering == triggering.setTxMask(PositiveInteger().setValue(0x100))
        assert triggering.getTxMask().getValue() == 0x100

    def test_CanFrameTriggering_aggregations(self):
        """Test CanFrameTriggering aggregation members (Table 6.110)."""
        parent = MockParent()
        triggering = CanFrameTriggering(parent, "CanFrameTriggering")

        rng = RxIdentifierRange()
        rng.setLowerCanId(PositiveInteger().setValue(0x100))
        assert triggering == triggering.setRxIdentifierRange(rng)
        assert triggering.getRxIdentifierRange() == rng
        assert triggering == triggering.setRxIdentifierRange(None)
        assert triggering.getRxIdentifierRange() == rng

        timing = CanXlFrameTriggeringProps()
        assert triggering == triggering.setCanXlFrameTriggeringProps(timing)
        assert triggering.getCanXlFrameTriggeringProps() == timing

        ttcan_timing = TtcanAbsolutelyScheduledTiming()
        assert triggering == triggering.addAbsolutelyScheduledTiming(ttcan_timing)
        assert triggering.getAbsolutelyScheduledTimings() == [ttcan_timing]
        assert triggering == triggering.addAbsolutelyScheduledTiming(None)
        assert triggering.getAbsolutelyScheduledTimings() == [ttcan_timing]

        result = triggering.setCanFrameTxBehavior("tx_behavior")
        assert triggering.getCanFrameTxBehavior() == "tx_behavior"
        assert result == triggering  # Test method chaining

        result = triggering.setCanXlFrameTriggeringProps("xl_props")
        assert triggering.getCanXlFrameTriggeringProps() == "xl_props"
        assert result == triggering  # Test method chaining

        result = triggering.setIdentifier(123)
        assert triggering.getIdentifier() == 123
        assert result == triggering  # Test method chaining

        result = triggering.setJ1939requestable(True)
        assert triggering.getJ1939requestable() is True
        assert result == triggering  # Test method chaining

        result = triggering.setRxMask("rx_mask")
        assert triggering.getRxMask() == "rx_mask"
        assert result == triggering  # Test method chaining

        result = triggering.setTxMask("tx_mask")
        assert triggering.getTxMask() == "tx_mask"
        assert result == triggering  # Test method chaining

    def test_CanFrameRxBehaviorEnum(self):
        """Test CanFrameRxBehaviorEnum enum (Table 6.113)."""
        enum = CanFrameRxBehaviorEnum()
        assert enum is not None
        enum.setValue(CanFrameRxBehaviorEnum.ENUM_ANY)
        assert enum.getValue() == "ANY"

        assert CanFrameRxBehaviorEnum.ENUM_ANY == "ANY"
        assert CanFrameRxBehaviorEnum.ENUM_CAN_20 == "CAN-20"
        assert CanFrameRxBehaviorEnum.ENUM_CAN_FD == "CAN-FD"

        assert CanFrameRxBehaviorEnum.ENUM_ANY in enum.getEnumValues()
        assert CanFrameRxBehaviorEnum.ENUM_CAN_20 in enum.getEnumValues()
        assert CanFrameRxBehaviorEnum.ENUM_CAN_FD in enum.getEnumValues()
        assert len(enum.getEnumValues()) == 3

    def test_CanFrameTxBehaviorEnum(self):
        """Test CanFrameTxBehaviorEnum enum (Table 6.114)."""
        enum = CanFrameTxBehaviorEnum()
        assert enum is not None
        enum.setValue(CanFrameTxBehaviorEnum.ENUM_CAN_20)
        assert enum.getValue() == "CAN-20"

        assert CanFrameTxBehaviorEnum.ENUM_CAN_20 == "CAN-20"
        assert CanFrameTxBehaviorEnum.ENUM_CAN_FD == "CAN-FD"

        assert CanFrameTxBehaviorEnum.ENUM_CAN_20 in enum.getEnumValues()
        assert CanFrameTxBehaviorEnum.ENUM_CAN_FD in enum.getEnumValues()
        assert len(enum.getEnumValues()) == 2

    def test_CanXlFrameTriggeringProps_initialization(self):
        """Test CanXlFrameTriggeringProps default state (Table F.27)."""
        obj = CanXlFrameTriggeringProps()

        assert isinstance(obj, ARObject)
        assert obj.getAcceptanceField() is None
        assert obj.getPriorityId() is None
        assert obj.getSduType() is None
        assert obj.getVcid() is None

    def test_CanXlFrameTriggeringProps_get_set(self):
        """Test CanXlFrameTriggeringProps getter/setter with None no-op (Table F.27)."""
        obj = CanXlFrameTriggeringProps()

        assert obj == obj.setAcceptanceField(PositiveInteger().setValue(1))
        assert obj.getAcceptanceField().getValue() == 1
        assert obj == obj.setAcceptanceField(None)
        assert obj.getAcceptanceField().getValue() == 1

        assert obj == obj.setPriorityId(PositiveInteger().setValue(2))
        assert obj.getPriorityId().getValue() == 2
        assert obj == obj.setPriorityId(None)
        assert obj.getPriorityId().getValue() == 2

        assert obj == obj.setSduType(PositiveInteger().setValue(3))
        assert obj.getSduType().getValue() == 3
        assert obj == obj.setSduType(None)
        assert obj.getSduType().getValue() == 3

        assert obj == obj.setVcid(PositiveInteger().setValue(4))
        assert obj.getVcid().getValue() == 4
        assert obj == obj.setVcid(None)
        assert obj.getVcid().getValue() == 4
