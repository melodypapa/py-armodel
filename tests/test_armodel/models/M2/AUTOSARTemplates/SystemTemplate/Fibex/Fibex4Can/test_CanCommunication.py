"""
Test suite for CAN Communication classes in AUTOSAR System Template.

This module contains comprehensive unit tests for CAN communication-related
classes including RxIdentifierRange, CanFrame, and CanFrameTriggering.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrame,
    CanFrameRxBehaviorEnum,
    CanFrameTriggering,
    CanFrameTxBehaviorEnum,
    RxIdentifierRange,
)
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

    def test_RxIdentifierRange(self):
        """
        Test RxIdentifierRange class functionality.

        This test validates that RxIdentifierRange can be instantiated,
        properly inherits from ARObject, and that its setter/getter methods
        work correctly for lower and upper CAN ID values.
        """
        range_obj = RxIdentifierRange()

        assert isinstance(range_obj, ARObject)

        # Test default values
        assert range_obj.getLowerCanId() is None
        assert range_obj.getUpperCanId() is None

        # Test setter/getter methods
        range_obj.setLowerCanId(100)
        assert range_obj.getLowerCanId() == 100

        range_obj.setUpperCanId(200)
        assert range_obj.getUpperCanId() == 200

    def test_CanFrame(self):
        """
        Test CanFrame class functionality.

        This test verifies that CanFrame can be instantiated with a parent
        object and short name, properly inherits from both ARObject and Frame,
        and that its default properties are correctly initialized.
        """
        parent = MockParent()
        frame = CanFrame(parent, "test_can_frame")

        assert isinstance(frame, ARObject)
        assert isinstance(frame, Frame)

        # Test default values
        assert frame.getFrameLength() is None
        assert frame.getPduToFrameMappings() == []

    def test_CanFrameTriggering(self):
        """
        Test CanFrameTriggering class functionality.

        This test ensures that CanFrameTriggering is properly instantiated,
        inherits from FrameTriggering, and all its properties can be set
        and retrieved correctly. It tests both simple properties and
        object references.
        """
        parent = MockParent()
        triggering = CanFrameTriggering(parent, "test_can_frame_triggering")

        assert isinstance(triggering, FrameTriggering)

        # Test default values
        assert triggering.getAbsolutelyScheduledTimings() == []
        assert triggering.getCanAddressingMode() is None
        assert triggering.getCanFdFrameSupport() is None
        assert triggering.getCanFrameRxBehavior() is None
        assert triggering.getCanFrameTxBehavior() is None
        assert triggering.getCanXlFrameTriggeringProps() is None
        assert triggering.getIdentifier() is None
        assert triggering.getJ1939requestable() is None
        assert triggering.getRxIdentifierRange() is None
        assert triggering.getRxMask() is None
        assert triggering.getTxMask() is None

        # Test setter/getter methods
        triggering.setCanAddressingMode("standard")
        assert triggering.getCanAddressingMode() == "standard"

        triggering.setCanFdFrameSupport(True)
        assert triggering.getCanFdFrameSupport() is True

        mock_range = RxIdentifierRange()
        triggering.setRxIdentifierRange(mock_range)
        assert triggering.getRxIdentifierRange() == mock_range

        # Test additional setter methods and method chaining functionality
        result = triggering.setAbsolutelyScheduledTimings(["timing1", "timing2"])
        assert triggering.getAbsolutelyScheduledTimings() == ["timing1", "timing2"]
        assert result == triggering  # Test method chaining

        result = triggering.setCanFrameRxBehavior("rx_behavior")
        assert triggering.getCanFrameRxBehavior() == "rx_behavior"
        assert result == triggering  # Test method chaining

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
