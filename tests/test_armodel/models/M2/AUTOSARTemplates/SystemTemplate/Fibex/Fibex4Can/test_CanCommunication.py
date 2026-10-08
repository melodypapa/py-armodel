"""
Test suite for CAN Communication classes in AUTOSAR System Template.

This module contains comprehensive unit tests for CAN communication-related
classes including RxIdentifierRange, CanFrame, and CanFrameTriggering.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

import inspect
import sys
from typing import List, Optional, get_type_hints

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger
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

        mode = CanAddressingModeType()
        mode.setValue(CanAddressingModeType.ENUM_STANDARD)
        assert triggering == triggering.setCanAddressingMode(mode)
        assert isinstance(triggering.getCanAddressingMode(), CanAddressingModeType)
        assert triggering.getCanAddressingMode() == mode
        assert triggering == triggering.setCanAddressingMode(None)
        assert triggering.getCanAddressingMode() == mode

        rx = CanFrameRxBehaviorEnum()
        rx.setValue(CanFrameRxBehaviorEnum.ENUM_CAN_FD)
        assert triggering == triggering.setCanFrameRxBehavior(rx)
        assert isinstance(triggering.getCanFrameRxBehavior(), CanFrameRxBehaviorEnum)
        assert triggering.getCanFrameRxBehavior() == rx

        tx = CanFrameTxBehaviorEnum()
        tx.setValue(CanFrameTxBehaviorEnum.ENUM_CAN_20)
        assert triggering == triggering.setCanFrameTxBehavior(tx)
        assert isinstance(triggering.getCanFrameTxBehavior(), CanFrameTxBehaviorEnum)
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

        mode = CanAddressingModeType()
        mode.setValue(CanAddressingModeType.ENUM_EXTENDED)
        assert triggering == triggering.setCanAddressingMode(mode)
        assert triggering.getCanAddressingMode() == mode
        assert triggering == triggering.setCanAddressingMode(None)
        assert triggering.getCanAddressingMode() == mode

        rx = CanFrameRxBehaviorEnum()
        rx.setValue(CanFrameRxBehaviorEnum.ENUM_ANY)
        assert triggering == triggering.setCanFrameRxBehavior(rx)
        assert triggering.getCanFrameRxBehavior() == rx

        tx = CanFrameTxBehaviorEnum()
        tx.setValue(CanFrameTxBehaviorEnum.ENUM_CAN_FD)
        assert triggering == triggering.setCanFrameTxBehavior(tx)
        assert triggering.getCanFrameTxBehavior() == tx

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


CAN_ADDRESSING_MODE_TYPE_CLASS_NOTE = "Indicates whether standard or extended CAN identifiers are used"


class TestCanAddressingModeType:
    """Test cases for CanAddressingModeType (Table 6.111, p.443)."""

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 6.111)"""
        assert CanAddressingModeType.__doc__.strip() == CAN_ADDRESSING_MODE_TYPE_CLASS_NOTE

    def test_literal_values_are_xsd_facets(self):
        """Test the member values are the exact XSD --SIMPLE enumeration facets (Table 6.111)"""
        assert CanAddressingModeType.ENUM_EXTENDED == "EXTENDED"
        assert CanAddressingModeType.ENUM_STANDARD == "STANDARD"

    def test_literal_comments_carry_spec_description_and_tags(self):
        """Test the literal comments carry the spec description + Tags verbatim (Table 6.111)"""
        source = inspect.getsource(CanAddressingModeType)
        assert "Extended 29-bit-identifiers are used (CAN 2.0B) Tags: atp.EnumerationLiteralIndex=0" in source
        assert "Standard 11-bit-identifiers are used (CAN 2.0A) Tags: atp.EnumerationLiteralIndex=1" in source

    def test_instantiability_and_facet_order(self):
        """Test the enum is instantiable and the tuple follows the XSD facet order (Table 6.111)"""
        enum = CanAddressingModeType()
        assert enum.getValue() == ""

        assert enum.setValue(CanAddressingModeType.ENUM_EXTENDED) is enum
        assert enum.getValue() == "EXTENDED"
        assert enum.setValue(CanAddressingModeType.ENUM_STANDARD) is enum
        assert enum.getValue() == "STANDARD"

        assert enum.getEnumValues() == ["EXTENDED", "STANDARD"]


RX_IDENTIFIER_RANGE_CLASS_NOTE = "Optional definition of a CanId range to reduce the effort of specifying every possible FrameTriggering within the defined Id range during reception. All frames received within a range are mapped to the same Pdu that is passed to a upper layer module (e.g. Nm, CDD, PduR)."
RX_IDENTIFIER_RANGE_LOWER_NOTE = "This attribute can be used together with the upperCanId attribute to define a range of CanIds."
RX_IDENTIFIER_RANGE_UPPER_NOTE = "This attribute can be used together with the lowerCanId attribute to define a range of CanIds."


class TestRxIdentifierRange:
    """Test cases for RxIdentifierRange (Table 6.112, p.444)."""

    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 6.112: Base = ARObject)"""
        assert issubclass(RxIdentifierRange, ARObject)

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 6.112)"""
        assert inspect.cleandoc(RxIdentifierRange.__doc__).strip() == RX_IDENTIFIER_RANGE_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert RxIdentifierRange.__init__.__doc__ is None

    def test_initialization(self):
        range_obj = RxIdentifierRange()

        assert isinstance(range_obj, ARObject)
        assert range_obj.getLowerCanId() is None
        assert range_obj.getUpperCanId() is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 6.112: lowerCanId, upperCanId)"""
        source = inspect.getsource(RxIdentifierRange.__init__)
        assert source.index("self.lowerCanId") < source.index("self.upperCanId")

    def test_get_set_lower_can_id(self):
        range_obj = RxIdentifierRange()

        assert range_obj == range_obj.setLowerCanId(PositiveInteger().setValue(0x100))
        assert range_obj.getLowerCanId().getValue() == 0x100
        assert range_obj == range_obj.setLowerCanId(None)
        assert range_obj.getLowerCanId().getValue() == 0x100

    def test_get_set_upper_can_id(self):
        range_obj = RxIdentifierRange()

        assert range_obj == range_obj.setUpperCanId(PositiveInteger().setValue(0x1FF))
        assert range_obj.getUpperCanId().getValue() == 0x1FF
        assert range_obj == range_obj.setUpperCanId(None)
        assert range_obj.getUpperCanId().getValue() == 0x1FF

    def _assert_docstring(self, method, note, suffix=None):
        doc = method.__doc__
        expected = note if suffix is None else note + "\n" + suffix
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_member_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 6.112)"""
        none_no_op = "A None value is a no-op and does not overwrite an existing %s."
        self._assert_docstring(RxIdentifierRange.getLowerCanId, RX_IDENTIFIER_RANGE_LOWER_NOTE)
        self._assert_docstring(RxIdentifierRange.setLowerCanId, RX_IDENTIFIER_RANGE_LOWER_NOTE, none_no_op % "lowerCanId")
        self._assert_docstring(RxIdentifierRange.getUpperCanId, RX_IDENTIFIER_RANGE_UPPER_NOTE)
        self._assert_docstring(RxIdentifierRange.setUpperCanId, RX_IDENTIFIER_RANGE_UPPER_NOTE, none_no_op % "upperCanId")

    def test_type_annotations(self):
        import ast

        getter_hints = get_type_hints(RxIdentifierRange.getLowerCanId)
        assert getter_hints["return"] == Optional[PositiveInteger]

        setter_hints = get_type_hints(RxIdentifierRange.setUpperCanId)
        assert setter_hints["value"] == Optional[PositiveInteger]
        assert setter_hints["return"] == RxIdentifierRange

        src = inspect.getsource(sys.modules[RxIdentifierRange.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "RxIdentifierRange")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["lowerCanId"] == "Optional[PositiveInteger]"
        assert annotations["upperCanId"] == "Optional[PositiveInteger]"


CAN_FRAME_RX_BEHAVIOR_ENUM_CLASS_NOTE = "Defines different CAN protocols for frame reception behavior."


class TestCanFrameRxBehaviorEnum:
    """Test cases for CanFrameRxBehaviorEnum (Table 6.113, p.444)."""

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 6.113)"""
        assert CanFrameRxBehaviorEnum.__doc__.strip() == CAN_FRAME_RX_BEHAVIOR_ENUM_CLASS_NOTE

    def test_literal_values_are_xsd_facets(self):
        """Test the member values are the exact XSD --SIMPLE enumeration facets (Table 6.113)"""
        assert CanFrameRxBehaviorEnum.ENUM_ANY == "ANY"
        assert CanFrameRxBehaviorEnum.ENUM_CAN_20 == "CAN-20"
        assert CanFrameRxBehaviorEnum.ENUM_CAN_FD == "CAN-FD"

    def test_literal_comments_carry_spec_description_and_tags(self):
        """Test the literal comments carry the spec description + Tags verbatim (Table 6.113)"""
        source = inspect.getsource(CanFrameRxBehaviorEnum)
        assert "This CAN frame may be received as both, CAN 2.0 and CAN FD. Tags: atp.EnumerationLiteralIndex=0" in source
        assert "This CAN frame shall be received as CAN 2.0 only. In case the CAN frame is received as CAN FD it is discarded during reception. Tags: atp.EnumerationLiteralIndex=1" in source
        assert "This CAN frame shall be received as CAN FD only. In case the CAN frame is received as CAN 2.0 it is discarded during reception. Tags: atp.EnumerationLiteralIndex=2" in source

    def test_instantiability_and_facet_order(self):
        """Test the enum is instantiable and the tuple follows the XSD facet order (Table 6.113)"""
        enum = CanFrameRxBehaviorEnum()
        assert enum.getValue() == ""

        assert enum.setValue(CanFrameRxBehaviorEnum.ENUM_ANY) is enum
        assert enum.getValue() == "ANY"
        assert enum.setValue(CanFrameRxBehaviorEnum.ENUM_CAN_20) is enum
        assert enum.getValue() == "CAN-20"
        assert enum.setValue(CanFrameRxBehaviorEnum.ENUM_CAN_FD) is enum
        assert enum.getValue() == "CAN-FD"

        assert enum.getEnumValues() == ["ANY", "CAN-20", "CAN-FD"]


CAN_FRAME_TX_BEHAVIOR_ENUM_CLASS_NOTE = "Defines different CAN protocols for frame transmission behavior."


class TestCanFrameTxBehaviorEnum:
    """Test cases for CanFrameTxBehaviorEnum (Table 6.114, p.445)."""

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 6.114)"""
        assert CanFrameTxBehaviorEnum.__doc__.strip() == CAN_FRAME_TX_BEHAVIOR_ENUM_CLASS_NOTE

    def test_literal_values_are_xsd_facets(self):
        """Test the member values are the exact XSD --SIMPLE enumeration facets (Table 6.114)"""
        assert CanFrameTxBehaviorEnum.ENUM_CAN_20 == "CAN-20"
        assert CanFrameTxBehaviorEnum.ENUM_CAN_FD == "CAN-FD"

    def test_literal_comments_carry_spec_description_and_tags(self):
        """Test the literal comments carry the spec description + Tags verbatim (Table 6.114)"""
        source = inspect.getsource(CanFrameTxBehaviorEnum)
        assert "This CAN frame shall be sent as CAN 2.0 only. Tags: atp.EnumerationLiteralIndex=0" in source
        assert "This CAN frame shall be sent as CAN FD. Tags: atp.EnumerationLiteralIndex=1" in source

    def test_instantiability_and_facet_order(self):
        """Test the enum is instantiable and the tuple follows the XSD facet order (Table 6.114)"""
        enum = CanFrameTxBehaviorEnum()
        assert enum.getValue() == ""

        assert enum.setValue(CanFrameTxBehaviorEnum.ENUM_CAN_20) is enum
        assert enum.getValue() == "CAN-20"
        assert enum.setValue(CanFrameTxBehaviorEnum.ENUM_CAN_FD) is enum
        assert enum.getValue() == "CAN-FD"

        assert enum.getEnumValues() == ["CAN-20", "CAN-FD"]


CAN_FRAME_CLASS_NOTE = "CAN specific Frame element. This element shall also be used for TTCan. Tags: atp.recommendedPackage=Frames"


class TestCanFrame:
    """Test cases for CanFrame (Table 6.109, p.442)."""

    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 6.109: Base = ARObject, CollectableElement, FibexElement, Frame, Identifiable, MultilanguageReferrable, PackageableElement, Referrable)"""
        assert issubclass(CanFrame, Frame)

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim including the Tags tail (Table 6.109)"""
        assert inspect.cleandoc(CanFrame.__doc__).strip() == CAN_FRAME_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanFrame.__init__.__doc__ is None

    def test_initialization(self):
        parent = MockParent()
        frame = CanFrame(parent, "CanFrame")

        assert isinstance(frame, Frame)
        assert frame.getShortName() == "CanFrame"


CAN_FRAME_TRIGGERING_CLASS_NOTE = "CAN specific attributes to the FrameTriggering"
CAN_FRAME_TRIGGERING_ABSOLUTELY_SCHEDULED_TIMING_NOTE = "Each frame in TTCAN is identified by its slot id and communication cycle. A description is provided by the usage of AbsolutelyScheduledTiming."
CAN_FRAME_TRIGGERING_CAN_ADDRESSING_MODE_NOTE = "The CAN protocol supports two types of frame formats. The standard frame format uses 11-bit identifiers and is defined in the CAN specification 2.0 A. Additionally the extended frame format allows 29-bit identifiers and is defined in the CAN specification 2.0 B."
CAN_FRAME_TRIGGERING_RX_BEHAVIOR_NOTE = "Defines which CAN protocol shall be expected for frame reception."
CAN_FRAME_TRIGGERING_TX_BEHAVIOR_NOTE = "Defines which CAN protocol shall be used for frame transmission."
CAN_FRAME_TRIGGERING_XL_PROPS_NOTE = "Definition of CAN XL specific attributes in case the frame is a CAN XL frame."
CAN_FRAME_TRIGGERING_IDENTIFIER_NOTE = "This attribute is used to define the identifier this frame shall use on the CAN network."
CAN_FRAME_TRIGGERING_J1939_NOTE = "Frame can be triggered by the J1939 request message."
CAN_FRAME_TRIGGERING_RX_IDENTIFIER_RANGE_NOTE = "Optional definition of a CanId range."
CAN_FRAME_TRIGGERING_RX_MASK_NOTE = "Identifier mask which denotes the relevant bits in the CAN Identifier. Together with the identifier, this parameter defines a CAN identifier range."
CAN_FRAME_TRIGGERING_TX_MASK_NOTE = "Identifier mask which denotes static bits in the CAN identifier. The other bits can be set dynamically."


class TestCanFrameTriggering:
    """Test cases for CanFrameTriggering (Table 6.110, p.443)."""

    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 6.110: Base = ARObject, FrameTriggering, Identifiable, MultilanguageReferrable, Referrable)"""
        assert issubclass(CanFrameTriggering, FrameTriggering)

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 6.110)"""
        assert inspect.cleandoc(CanFrameTriggering.__doc__).strip() == CAN_FRAME_TRIGGERING_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanFrameTriggering.__init__.__doc__ is None

    def test_initialization(self):
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

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 6.110)"""
        source = inspect.getsource(CanFrameTriggering.__init__)
        order = [
            "self.absolutelyScheduledTimings",
            "self.canAddressingMode",
            "self.canFrameRxBehavior",
            "self.canFrameTxBehavior",
            "self.canXlFrameTriggeringProps",
            "self.identifier",
            "self.j1939requestable",
            "self.rxIdentifierRange",
            "self.rxMask",
            "self.txMask",
        ]
        indices = [source.index(name) for name in order]
        assert indices == sorted(indices)

    def test_add_absolutely_scheduled_timing(self):
        parent = MockParent()
        triggering = CanFrameTriggering(parent, "CanFrameTriggering")

        first = TtcanAbsolutelyScheduledTiming()
        second = TtcanAbsolutelyScheduledTiming()

        assert triggering == triggering.addAbsolutelyScheduledTiming(first)
        assert triggering.getAbsolutelyScheduledTimings() == [first]
        assert triggering == triggering.addAbsolutelyScheduledTiming(second)
        assert triggering.getAbsolutelyScheduledTimings() == [first, second]

        assert triggering == triggering.addAbsolutelyScheduledTiming(None)
        assert triggering.getAbsolutelyScheduledTimings() == [first, second]

    def test_get_set_attributes(self):
        parent = MockParent()
        triggering = CanFrameTriggering(parent, "CanFrameTriggering")

        mode = CanAddressingModeType()
        mode.setValue(CanAddressingModeType.ENUM_STANDARD)
        assert triggering == triggering.setCanAddressingMode(mode)
        assert isinstance(triggering.getCanAddressingMode(), CanAddressingModeType)
        assert triggering == triggering.setCanAddressingMode(None)
        assert triggering.getCanAddressingMode() == mode

        rx = CanFrameRxBehaviorEnum()
        rx.setValue(CanFrameRxBehaviorEnum.ENUM_CAN_FD)
        assert triggering == triggering.setCanFrameRxBehavior(rx)
        assert triggering.getCanFrameRxBehavior() == rx
        assert triggering == triggering.setCanFrameRxBehavior(None)
        assert triggering.getCanFrameRxBehavior() == rx

        tx = CanFrameTxBehaviorEnum()
        tx.setValue(CanFrameTxBehaviorEnum.ENUM_CAN_20)
        assert triggering == triggering.setCanFrameTxBehavior(tx)
        assert triggering.getCanFrameTxBehavior() == tx
        assert triggering == triggering.setCanFrameTxBehavior(None)
        assert triggering.getCanFrameTxBehavior() == tx

        assert triggering == triggering.setIdentifier(Integer().setValue(0x100))
        assert triggering.getIdentifier().getValue() == 0x100
        assert triggering == triggering.setIdentifier(None)
        assert triggering.getIdentifier().getValue() == 0x100

        assert triggering == triggering.setJ1939requestable(Boolean().setValue(True))
        assert triggering.getJ1939requestable().getValue() is True
        assert triggering == triggering.setJ1939requestable(None)
        assert triggering.getJ1939requestable().getValue() is True

        rng = RxIdentifierRange()
        rng.setLowerCanId(PositiveInteger().setValue(0x100))
        assert triggering == triggering.setRxIdentifierRange(rng)
        assert triggering.getRxIdentifierRange() == rng
        assert triggering == triggering.setRxIdentifierRange(None)
        assert triggering.getRxIdentifierRange() == rng

        assert triggering == triggering.setRxMask(PositiveInteger().setValue(0x7FF))
        assert triggering.getRxMask().getValue() == 0x7FF
        assert triggering == triggering.setRxMask(None)
        assert triggering.getRxMask().getValue() == 0x7FF

        assert triggering == triggering.setTxMask(PositiveInteger().setValue(0x100))
        assert triggering.getTxMask().getValue() == 0x100
        assert triggering == triggering.setTxMask(None)
        assert triggering.getTxMask().getValue() == 0x100

        props = CanXlFrameTriggeringProps()
        props.setPriorityId(PositiveInteger().setValue(5))
        assert triggering == triggering.setCanXlFrameTriggeringProps(props)
        assert triggering.getCanXlFrameTriggeringProps() == props
        assert triggering == triggering.setCanXlFrameTriggeringProps(None)
        assert triggering.getCanXlFrameTriggeringProps() == props

    def _assert_docstring(self, method, note, suffix=None):
        doc = method.__doc__
        expected = note if suffix is None else note + "\n" + suffix
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_member_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 6.110)"""
        none_no_op = "A None value is a no-op and does not overwrite an existing %s."
        append_no_op = "A None value is a no-op and is not appended to absolutelyScheduledTimings."
        self._assert_docstring(CanFrameTriggering.getAbsolutelyScheduledTimings, CAN_FRAME_TRIGGERING_ABSOLUTELY_SCHEDULED_TIMING_NOTE)
        self._assert_docstring(CanFrameTriggering.addAbsolutelyScheduledTiming, CAN_FRAME_TRIGGERING_ABSOLUTELY_SCHEDULED_TIMING_NOTE, append_no_op)
        self._assert_docstring(CanFrameTriggering.getCanAddressingMode, CAN_FRAME_TRIGGERING_CAN_ADDRESSING_MODE_NOTE)
        self._assert_docstring(CanFrameTriggering.setCanAddressingMode, CAN_FRAME_TRIGGERING_CAN_ADDRESSING_MODE_NOTE, none_no_op % "canAddressingMode")
        self._assert_docstring(CanFrameTriggering.getCanFrameRxBehavior, CAN_FRAME_TRIGGERING_RX_BEHAVIOR_NOTE)
        self._assert_docstring(CanFrameTriggering.setCanFrameRxBehavior, CAN_FRAME_TRIGGERING_RX_BEHAVIOR_NOTE, none_no_op % "canFrameRxBehavior")
        self._assert_docstring(CanFrameTriggering.getCanFrameTxBehavior, CAN_FRAME_TRIGGERING_TX_BEHAVIOR_NOTE)
        self._assert_docstring(CanFrameTriggering.setCanFrameTxBehavior, CAN_FRAME_TRIGGERING_TX_BEHAVIOR_NOTE, none_no_op % "canFrameTxBehavior")
        self._assert_docstring(CanFrameTriggering.getCanXlFrameTriggeringProps, CAN_FRAME_TRIGGERING_XL_PROPS_NOTE)
        self._assert_docstring(CanFrameTriggering.setCanXlFrameTriggeringProps, CAN_FRAME_TRIGGERING_XL_PROPS_NOTE, none_no_op % "canXlFrameTriggeringProps")
        self._assert_docstring(CanFrameTriggering.getIdentifier, CAN_FRAME_TRIGGERING_IDENTIFIER_NOTE)
        self._assert_docstring(CanFrameTriggering.setIdentifier, CAN_FRAME_TRIGGERING_IDENTIFIER_NOTE, none_no_op % "identifier")
        self._assert_docstring(CanFrameTriggering.getJ1939requestable, CAN_FRAME_TRIGGERING_J1939_NOTE)
        self._assert_docstring(CanFrameTriggering.setJ1939requestable, CAN_FRAME_TRIGGERING_J1939_NOTE, none_no_op % "j1939requestable")
        self._assert_docstring(CanFrameTriggering.getRxIdentifierRange, CAN_FRAME_TRIGGERING_RX_IDENTIFIER_RANGE_NOTE)
        self._assert_docstring(CanFrameTriggering.setRxIdentifierRange, CAN_FRAME_TRIGGERING_RX_IDENTIFIER_RANGE_NOTE, none_no_op % "rxIdentifierRange")
        self._assert_docstring(CanFrameTriggering.getRxMask, CAN_FRAME_TRIGGERING_RX_MASK_NOTE)
        self._assert_docstring(CanFrameTriggering.setRxMask, CAN_FRAME_TRIGGERING_RX_MASK_NOTE, none_no_op % "rxMask")
        self._assert_docstring(CanFrameTriggering.getTxMask, CAN_FRAME_TRIGGERING_TX_MASK_NOTE)
        self._assert_docstring(CanFrameTriggering.setTxMask, CAN_FRAME_TRIGGERING_TX_MASK_NOTE, none_no_op % "txMask")

    def test_type_annotations(self):
        import ast

        list_getter_hints = get_type_hints(CanFrameTriggering.getAbsolutelyScheduledTimings)
        assert list_getter_hints["return"] == List[TtcanAbsolutelyScheduledTiming]

        adder_hints = get_type_hints(CanFrameTriggering.addAbsolutelyScheduledTiming)
        assert adder_hints["value"] == Optional[TtcanAbsolutelyScheduledTiming]
        assert adder_hints["return"] == CanFrameTriggering

        setter_hints = get_type_hints(CanFrameTriggering.setCanAddressingMode)
        assert setter_hints["value"] == Optional[CanAddressingModeType]
        assert setter_hints["return"] == CanFrameTriggering

        getter_hints = get_type_hints(CanFrameTriggering.getIdentifier)
        assert getter_hints["return"] == Optional[Integer]

        src = inspect.getsource(sys.modules[CanFrameTriggering.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "CanFrameTriggering")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["absolutelyScheduledTimings"] == "List[TtcanAbsolutelyScheduledTiming]"
        assert annotations["canAddressingMode"] == "Optional[CanAddressingModeType]"
        assert annotations["canFrameRxBehavior"] == "Optional[CanFrameRxBehaviorEnum]"
        assert annotations["canFrameTxBehavior"] == "Optional[CanFrameTxBehaviorEnum]"
        assert annotations["canXlFrameTriggeringProps"] == "Optional[CanXlFrameTriggeringProps]"
        assert annotations["identifier"] == "Optional[Integer]"
        assert annotations["j1939requestable"] == "Optional[Boolean]"
        assert annotations["rxIdentifierRange"] == "Optional[RxIdentifierRange]"
        assert annotations["rxMask"] == "Optional[PositiveInteger]"
        assert annotations["txMask"] == "Optional[PositiveInteger]"
