import inspect
from typing import Optional, get_type_hints

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import DefaultValueElement, FrameMapping, Gateway, IPduMapping, ISignalMapping, PduMappingDefaultValue, TargetIPduRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement


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
