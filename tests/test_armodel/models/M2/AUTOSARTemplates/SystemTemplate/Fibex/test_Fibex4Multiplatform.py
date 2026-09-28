import inspect
from typing import Optional, get_type_hints

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import DefaultValueElement, FrameMapping, Gateway, IPduMapping, ISignalMapping, PduMappingDefaultValue, TargetIPduRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_Fibex4Multiplatform:
    """Test cases for Fibex4Multiplatform classes."""

    def test_FrameMapping(self):
        """Test FrameMapping class functionality."""
        mapping = FrameMapping()

        assert isinstance(mapping, ARObject)

        # Test default values
        assert mapping.getIntroduction() is None
        assert mapping.getSourceFrameRef() is None
        assert mapping.getTargetFrameRef() is None

        # Test setter/getter methods
        mapping.setIntroduction("Introduction text")
        assert mapping.getIntroduction() == "Introduction text"

    def test_ISignalMapping(self):
        """Test ISignalMapping class functionality."""
        mapping = ISignalMapping()

        assert isinstance(mapping, ARObject)

        # Test default values
        assert mapping.getIntroduction() is None
        assert mapping.getSourceSignalRef() is None
        assert mapping.getTargetSignalRef() is None

    def test_DefaultValueElement(self):
        """Test DefaultValueElement class functionality."""
        element = DefaultValueElement()

        assert isinstance(element, ARObject)

        # Test default values
        assert element.getElementByteValue() is None
        assert element.getElementPosition() is None

    def test_PduMappingDefaultValue(self):
        """Test PduMappingDefaultValue class functionality."""
        default_value = PduMappingDefaultValue()

        assert isinstance(default_value, ARObject)

        # Test default values
        assert default_value.getDefaultValueElements() == []

    def test_TargetIPduRef(self):
        """Test TargetIPduRef class functionality."""
        ref = TargetIPduRef()

        assert isinstance(ref, ARObject)

        # Test default values
        assert ref.getDefaultValue() is None
        assert ref.getTargetIPduRef() is None

    def test_IPduMapping(self):
        """Test IPduMapping class functionality."""
        mapping = IPduMapping()

        assert isinstance(mapping, ARObject)

        # Test default values
        assert mapping.getIntroduction() is None
        assert mapping.getPdurTpChunkSize() is None
        assert mapping.getSourceIPduRef() is None
        assert mapping.getTargetIPdu() is None

    def test_Gateway(self):
        """Test Gateway class functionality."""
        parent = MockParent()
        gateway = Gateway(parent, "test_gateway")

        assert isinstance(gateway, FibexElement)

        # Test default values
        assert gateway.getEcuRef() is None
        assert gateway.getFrameMappings() == []
        assert gateway.getIPduMappings() == []
        assert gateway.getSignalMappings() == []


DEFAULT_VALUE_ELEMENT_CLASS_NOTE = "The default value consists of a number of elements. Each element is one byte long and the number of elements is specified by SduLength."
ELEMENT_BYTE_VALUE_NOTE = "The integer value of a freely defined data byte."
ELEMENT_POSITION_NOTE = "This attribute specifies the byte position of the element within the default value"


class TestDefaultValueElement:
    """Spec-synced tests for DefaultValueElement (AUTOSAR_CP_TPS_SystemTemplate Table 8.6)."""

    def _make(self) -> DefaultValueElement:
        return DefaultValueElement()

    def _assert_docstring(self, method, note, attr_name=None):
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def test_initialization(self):
        element = self._make()

        assert isinstance(element, ARObject)
        assert element.getElementByteValue() is None
        assert element.getElementPosition() is None

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(DefaultValueElement.__doc__).strip() == DEFAULT_VALUE_ELEMENT_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert DefaultValueElement.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(DefaultValueElement.__init__)
        assert source.index("self.elementByteValue:") < source.index("self.elementPosition:")

    def test_get_set_element_byte_value(self):
        element = self._make()

        assert element.getElementByteValue() is None

        value = Integer()
        value.setValue(171)
        assert element == element.setElementByteValue(value)
        assert element.getElementByteValue() is value

        assert element == element.setElementByteValue(None)
        assert element.getElementByteValue() is value

        getter_hints = get_type_hints(DefaultValueElement.getElementByteValue)
        assert getter_hints.get("return") == Optional[Integer]

        setter_hints = get_type_hints(DefaultValueElement.setElementByteValue)
        assert setter_hints.get("value") == Optional[Integer]
        assert setter_hints.get("return") is DefaultValueElement

    def test_get_set_element_position(self):
        element = self._make()

        assert element.getElementPosition() is None

        value = Integer()
        value.setValue(7)
        assert element == element.setElementPosition(value)
        assert element.getElementPosition() is value

        assert element == element.setElementPosition(None)
        assert element.getElementPosition() is value

        getter_hints = get_type_hints(DefaultValueElement.getElementPosition)
        assert getter_hints.get("return") == Optional[Integer]

        setter_hints = get_type_hints(DefaultValueElement.setElementPosition)
        assert setter_hints.get("value") == Optional[Integer]
        assert setter_hints.get("return") is DefaultValueElement

    def test_element_byte_value_docstrings_are_spec_note(self):
        self._assert_docstring(DefaultValueElement.getElementByteValue, ELEMENT_BYTE_VALUE_NOTE)
        self._assert_docstring(DefaultValueElement.setElementByteValue, ELEMENT_BYTE_VALUE_NOTE, "elementByteValue")

    def test_element_position_docstrings_are_spec_note(self):
        self._assert_docstring(DefaultValueElement.getElementPosition, ELEMENT_POSITION_NOTE)
        self._assert_docstring(DefaultValueElement.setElementPosition, ELEMENT_POSITION_NOTE, "elementPosition")


FRAME_MAPPING_CLASS_NOTE = (
    "The entire source frame is mapped as it is onto the target frame (what in general is only possible inside of a common platform). "
    "In this case source and target frame should be the identical object. Each pair consists in a SOURCE and a TARGET referencing to a FrameTriggering. "
    "The Frame Mapping is not supported by the Autosar BSW. The existence is optional and has been incorporated into the System Template mainly for compatibility "
    "in order to allow interchange between FIBEX and AUTOSAR descriptions."
)
FRAME_MAPPING_CONSTRAINTS = (
    "[constr_9289] Existence of FrameMapping.sourceFrame: For each FrameMapping, the reference to FrameTriggering in the role sourceFrame shall exist at the time when the System Description is complete.\n"
    "\n"
    "[constr_9290] Existence of FrameMapping.targetFrame: For each FrameMapping, the reference to FrameTriggering in the role targetFrame shall exist at the time when the System Description is complete."
)
INTRODUCTION_NOTE = "This represents introductory documentation about the frame mapping."
SOURCE_FRAME_NOTE = "Source destination of the referencing mapping."
TARGET_FRAME_NOTE = "Target destination of the referencing mapping."


class TestFrameMapping:
    """Spec-synced tests for FrameMapping (AUTOSAR_CP_TPS_SystemTemplate Table 8.2)."""

    def _make(self) -> FrameMapping:
        return FrameMapping()

    def _assert_docstring(self, method, note, attr_name=None):
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def test_initialization(self):
        mapping = self._make()

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, VariationPointCapable)
        assert mapping.getIntroduction() is None
        assert mapping.getSourceFrameRef() is None
        assert mapping.getTargetFrameRef() is None

    def test_class_docstring_is_spec_note(self):
        expected = FRAME_MAPPING_CLASS_NOTE + "\n\n" + FRAME_MAPPING_CONSTRAINTS
        assert inspect.cleandoc(FrameMapping.__doc__).strip() == expected

    def test_init_has_no_docstring(self):
        assert FrameMapping.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(FrameMapping.__init__)
        assert source.index("self.introduction:") < source.index("self.sourceFrameRef:")
        assert source.index("self.sourceFrameRef:") < source.index("self.targetFrameRef:")

    def test_get_set_introduction(self):
        mapping = self._make()

        assert mapping.getIntroduction() is None

        block = DocumentationBlock()
        assert mapping == mapping.setIntroduction(block)
        assert mapping.getIntroduction() is block

        assert mapping == mapping.setIntroduction(None)
        assert mapping.getIntroduction() is block

        getter_hints = get_type_hints(FrameMapping.getIntroduction)
        assert getter_hints.get("return") == Optional[DocumentationBlock]

        setter_hints = get_type_hints(FrameMapping.setIntroduction)
        assert setter_hints.get("value") == Optional[DocumentationBlock]
        assert setter_hints.get("return") is FrameMapping

    def test_get_set_source_frame_ref(self):
        mapping = self._make()

        assert mapping.getSourceFrameRef() is None

        ref = RefType()
        ref.setValue("/Gateway/SourceTriggering")
        assert mapping == mapping.setSourceFrameRef(ref)
        assert mapping.getSourceFrameRef() is ref

        assert mapping == mapping.setSourceFrameRef(None)
        assert mapping.getSourceFrameRef() is ref

        getter_hints = get_type_hints(FrameMapping.getSourceFrameRef)
        assert getter_hints.get("return") == Optional[RefType]

        setter_hints = get_type_hints(FrameMapping.setSourceFrameRef)
        assert setter_hints.get("value") == Optional[RefType]
        assert setter_hints.get("return") is FrameMapping

    def test_get_set_target_frame_ref(self):
        mapping = self._make()

        assert mapping.getTargetFrameRef() is None

        ref = RefType()
        ref.setValue("/Gateway/TargetTriggering")
        assert mapping == mapping.setTargetFrameRef(ref)
        assert mapping.getTargetFrameRef() is ref

        assert mapping == mapping.setTargetFrameRef(None)
        assert mapping.getTargetFrameRef() is ref

        getter_hints = get_type_hints(FrameMapping.getTargetFrameRef)
        assert getter_hints.get("return") == Optional[RefType]

        setter_hints = get_type_hints(FrameMapping.setTargetFrameRef)
        assert setter_hints.get("value") == Optional[RefType]
        assert setter_hints.get("return") is FrameMapping

    def test_introduction_docstrings_are_spec_note(self):
        self._assert_docstring(FrameMapping.getIntroduction, INTRODUCTION_NOTE)
        self._assert_docstring(FrameMapping.setIntroduction, INTRODUCTION_NOTE, "introduction")

    def test_source_frame_ref_docstrings_are_spec_note(self):
        self._assert_docstring(FrameMapping.getSourceFrameRef, SOURCE_FRAME_NOTE)
        self._assert_docstring(FrameMapping.setSourceFrameRef, SOURCE_FRAME_NOTE, "sourceFrameRef")

    def test_target_frame_ref_docstrings_are_spec_note(self):
        self._assert_docstring(FrameMapping.getTargetFrameRef, TARGET_FRAME_NOTE)
        self._assert_docstring(FrameMapping.setTargetFrameRef, TARGET_FRAME_NOTE, "targetFrameRef")
