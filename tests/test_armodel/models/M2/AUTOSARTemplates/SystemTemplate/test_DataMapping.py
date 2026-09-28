import inspect
from typing import Optional, get_type_hints

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    DataMapping,
    IndexedArrayElement,
    SenderRecArrayElementMapping,
    SenderRecArrayTypeMapping,
    SenderRecCompositeTypeMapping,
    SenderReceiverToSignalGroupMapping,
    SenderReceiverToSignalMapping,
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommunicationDirectionType,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class Test_DataMapping:
    """Test cases for DataMapping class and related data mapping classes."""

    def test_DataMapping(self):
        """Test DataMapping abstract class instantiation."""
        with pytest.raises(TypeError):
            DataMapping()

    def test_SenderReceiverToSignalMapping(self):
        """Test SenderReceiverToSignalMapping class functionality."""
        mapping = SenderReceiverToSignalMapping()

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, DataMapping)

        # Test default values
        assert mapping.getCommunicationDirection() is None
        assert mapping.getDataElementIRef() is None
        assert mapping.getSenderToSignalTextTableMapping() is None
        assert mapping.getSignalToReceiverTextTableMapping() is None
        assert mapping.getSystemSignalRef() is None

        # Test setter methods
        mock_direction = CommunicationDirectionType()
        result = mapping.setCommunicationDirection(mock_direction)
        assert mapping.getCommunicationDirection() == mock_direction
        assert result is mapping  # Test method chaining

        mock_data_element = "TestRef"  # Using a simple string as VariableDataPrototypeInSystemInstanceRef
        result = mapping.setDataElementIRef(mock_data_element)
        assert mapping.getDataElementIRef() == mock_data_element
        assert result is mapping  # Test method chaining

        mock_text_mapping = "TextTableMapping"  # Using a simple string as TextTableMapping
        result = mapping.setSenderToSignalTextTableMapping(mock_text_mapping)
        assert mapping.getSenderToSignalTextTableMapping() == mock_text_mapping
        assert result is mapping  # Test method chaining

        result = mapping.setSignalToReceiverTextTableMapping(mock_text_mapping)
        assert mapping.getSignalToReceiverTextTableMapping() == mock_text_mapping
        assert result is mapping  # Test method chaining

        mock_system_signal = "SystemSignalRef"  # Using a simple string as RefType
        result = mapping.setSystemSignalRef(mock_system_signal)
        assert mapping.getSystemSignalRef() == mock_system_signal
        assert result is mapping  # Test method chaining

        # Test DataMapping methods inherited by SenderReceiverToSignalMapping
        assert mapping.getIntroduction() is None
        mapping.setIntroduction("Test introduction")
        assert mapping.getIntroduction() == "Test introduction"

    def test_SenderRecCompositeTypeMapping(self):
        """Test SenderRecCompositeTypeMapping abstract class instantiation."""
        with pytest.raises(TypeError):
            SenderRecCompositeTypeMapping()

        # Verbatim spec Note (AUTOSAR_CP_TPS_SystemTemplate Table 5.27)
        assert SenderRecCompositeTypeMapping.__doc__ == (
            'Two mappings exist for the composite data types: "ArrayTypeMapping" and "RecordTypeMapping". '
            "In both, a primitive datatype will be mapped to a system signal. "
            'But it is also possible to combine the arrays and the records, so that an "array" could be an element of a "record" '
            'and in the same manner a "record" could be an element of an "array". '
            "Nesting these data types is also possible. "
            'If an element of a composite data type is again a composite one, the "CompositeTypeMapping" element will be used one more time '
            "(aggregation between the ArrayElementMapping and CompositeTypeMapping or aggregation between the RecordElementMapping and CompositeTypeMapping)."
        )
        assert SenderRecCompositeTypeMapping.__init__.__doc__ is None
        assert issubclass(SenderRecArrayTypeMapping, SenderRecCompositeTypeMapping)
        assert issubclass(SenderRecRecordTypeMapping, SenderRecCompositeTypeMapping)

    def test_SenderRecRecordElementMapping(self):
        """Test SenderRecRecordElementMapping class functionality."""
        mapping = SenderRecRecordElementMapping()

        assert isinstance(mapping, ARObject)

        # Test default values
        assert mapping.getApplicationRecordElementRef() is None
        assert mapping.getComplexTypeMapping() is None
        assert mapping.getImplementationRecordElementRef() is None
        assert mapping.getSenderToSignalTextTableMapping() is None
        assert mapping.getSignalToReceiverTextTableMapping() is None
        assert mapping.getSystemSignalRef() is None

        # Test setter methods with values
        mock_ref = "TestRef"
        result = mapping.setApplicationRecordElementRef(mock_ref)
        assert mapping.getApplicationRecordElementRef() == mock_ref
        assert result is mapping  # Test method chaining

        # Test setter methods with None (should not change the value)
        mapping.setApplicationRecordElementRef(None)
        assert mapping.getApplicationRecordElementRef() == mock_ref  # Should remain unchanged

        mock_complex = SenderRecRecordTypeMapping()  # Using a concrete implementation
        result = mapping.setComplexTypeMapping(mock_complex)
        assert mapping.getComplexTypeMapping() == mock_complex
        assert result is mapping  # Test method chaining

        mapping.setComplexTypeMapping(None)
        assert mapping.getComplexTypeMapping() == mock_complex  # Should remain unchanged

        mock_impl_ref = "ImplRef"
        result = mapping.setImplementationRecordElementRef(mock_impl_ref)
        assert mapping.getImplementationRecordElementRef() == mock_impl_ref
        assert result is mapping  # Test method chaining

        mapping.setImplementationRecordElementRef(None)
        assert mapping.getImplementationRecordElementRef() == mock_impl_ref  # Should remain unchanged

        mock_text_mapping = "TextMapping"
        result = mapping.setSenderToSignalTextTableMapping(mock_text_mapping)
        assert mapping.getSenderToSignalTextTableMapping() == mock_text_mapping
        assert result is mapping  # Test method chaining

        mapping.setSenderToSignalTextTableMapping(None)
        assert mapping.getSenderToSignalTextTableMapping() == mock_text_mapping  # Should remain unchanged

        result = mapping.setSignalToReceiverTextTableMapping(mock_text_mapping)
        assert mapping.getSignalToReceiverTextTableMapping() == mock_text_mapping
        assert result is mapping  # Test method chaining

        mapping.setSignalToReceiverTextTableMapping(None)
        assert mapping.getSignalToReceiverTextTableMapping() == mock_text_mapping  # Should remain unchanged

        mock_system_ref = "SystemRef"
        result = mapping.setSystemSignalRef(mock_system_ref)
        assert mapping.getSystemSignalRef() == mock_system_ref
        assert result is mapping  # Test method chaining

        mapping.setSystemSignalRef(None)
        assert mapping.getSystemSignalRef() == mock_system_ref  # Should remain unchanged

    def test_SenderRecRecordTypeMapping(self):
        """Test SenderRecRecordTypeMapping class functionality."""
        mapping = SenderRecRecordTypeMapping()

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, SenderRecCompositeTypeMapping)

        # Test default values
        assert mapping.getRecordElementMappings() == []

        # Test adding record element mapping
        mock_element = SenderRecRecordElementMapping()
        mapping.addRecordElementMapping(mock_element)
        assert mapping.getRecordElementMappings() == [mock_element]

    def test_IndexedArrayElement(self):
        """Test IndexedArrayElement class functionality."""
        element = IndexedArrayElement()

        assert isinstance(element, ARObject)

        # Test default values
        assert element.getApplicationArrayElementRef() is None
        assert element.getImplementationArrayElementRef() is None
        assert element.getIndex() is None

        # Test setter methods with values
        mock_ref = "TestRef"
        result = element.setApplicationArrayElementRef(mock_ref)
        assert element.getApplicationArrayElementRef() == mock_ref
        assert result is element  # Test method chaining

        # Test setter methods with None (should not change the value)
        element.setApplicationArrayElementRef(None)
        assert element.getApplicationArrayElementRef() == mock_ref  # Should remain unchanged

        mock_impl_ref = "ImplRef"
        result = element.setImplementationArrayElementRef(mock_impl_ref)
        assert element.getImplementationArrayElementRef() == mock_impl_ref
        assert result is element  # Test method chaining

        element.setImplementationArrayElementRef(None)
        assert element.getImplementationArrayElementRef() == mock_impl_ref  # Should remain unchanged

        mock_index = 42
        result = element.setIndex(mock_index)
        assert element.getIndex() == mock_index
        assert result is element  # Test method chaining

        element.setIndex(None)
        assert element.getIndex() == mock_index  # Should remain unchanged

    def test_SenderRecArrayElementMapping(self):
        """Test SenderRecArrayElementMapping class functionality."""
        mapping = SenderRecArrayElementMapping()

        assert isinstance(mapping, ARObject)

        # Test default values
        assert mapping.getComplexTypeMapping() is None
        assert mapping.getIndexedArrayElement() is None
        assert mapping.getSystemSignalRef() is None

        # Test setter methods with values and None
        mock_mapping = SenderRecRecordTypeMapping()  # Using a concrete implementation
        result = mapping.setComplexTypeMapping(mock_mapping)
        assert mapping.getComplexTypeMapping() == mock_mapping
        assert result is mapping  # Test method chaining

        mapping.setComplexTypeMapping(None)
        assert mapping.getComplexTypeMapping() == mock_mapping  # Should remain unchanged

        mock_element = IndexedArrayElement()
        result = mapping.setIndexedArrayElement(mock_element)
        assert mapping.getIndexedArrayElement() == mock_element
        assert result is mapping  # Test method chaining

        mapping.setIndexedArrayElement(None)
        assert mapping.getIndexedArrayElement() == mock_element  # Should remain unchanged

        mock_system_ref = "SystemRef"
        result = mapping.setSystemSignalRef(mock_system_ref)
        assert mapping.getSystemSignalRef() == mock_system_ref
        assert result is mapping  # Test method chaining

        mapping.setSystemSignalRef(None)
        assert mapping.getSystemSignalRef() == mock_system_ref  # Should remain unchanged

    def test_SenderRecArrayTypeMapping(self):
        """Test SenderRecArrayTypeMapping class functionality."""
        mapping = SenderRecArrayTypeMapping()

        # Verbatim spec Note (AUTOSAR_CP_TPS_SystemTemplate Table 5.28)
        assert SenderRecArrayTypeMapping.__doc__ == ('If the ApplicationCompositeDataType is an Array, the "ArrayTypeMapping" will be used.')
        assert SenderRecArrayTypeMapping.__init__.__doc__ is None

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, SenderRecCompositeTypeMapping)

        # Test default values
        assert mapping.getArrayElementMappings() == []
        assert mapping.getSenderToSignalTextTableMapping() is None
        assert mapping.getSignalToReceiverTextTableMapping() is None

        # Test array element mapping adder: appends, None no-op, method chaining
        mock_mapping = SenderRecArrayElementMapping()
        assert mapping == mapping.addArrayElementMapping(mock_mapping)
        assert mapping.getArrayElementMappings() == [mock_mapping]
        assert mapping == mapping.addArrayElementMapping(None)
        assert mapping.getArrayElementMappings() == [mock_mapping]

        text_mapping = TextTableMapping()
        result = mapping.setSenderToSignalTextTableMapping(text_mapping)
        assert mapping.getSenderToSignalTextTableMapping() == text_mapping
        assert result is mapping  # Test method chaining

        mapping.setSenderToSignalTextTableMapping(None)
        assert mapping.getSenderToSignalTextTableMapping() == text_mapping  # Should remain unchanged

        result = mapping.setSignalToReceiverTextTableMapping(text_mapping)
        assert mapping.getSignalToReceiverTextTableMapping() == text_mapping
        assert result is mapping  # Test method chaining

        mapping.setSignalToReceiverTextTableMapping(None)
        assert mapping.getSignalToReceiverTextTableMapping() == text_mapping  # Should remain unchanged

    def test_SenderReceiverToSignalGroupMapping(self):
        """Test SenderReceiverToSignalGroupMapping class functionality."""
        mapping = SenderReceiverToSignalGroupMapping()

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, DataMapping)

        # Test default values
        assert mapping.getDataElementIRef() is None
        assert mapping.getSignalGroupRef() is None
        assert mapping.getTypeMapping() is None

        # Test setter methods
        mock_ref = "TestRef"
        result = mapping.setDataElementIRef(mock_ref)
        assert mapping.getDataElementIRef() == mock_ref
        assert result is mapping  # Test method chaining

        mock_signal_group = "SignalGroupRef"
        result = mapping.setSignalGroupRef(mock_signal_group)
        assert mapping.getSignalGroupRef() == mock_signal_group
        assert result is mapping  # Test method chaining

        mock_type_mapping = SenderRecRecordTypeMapping()
        result = mapping.setTypeMapping(mock_type_mapping)
        assert mapping.getTypeMapping() == mock_type_mapping
        assert result is mapping  # Test method chaining

        # Test DataMapping methods inherited by SenderReceiverToSignalGroupMapping
        assert mapping.getIntroduction() is None
        result = mapping.setIntroduction("Test introduction")
        assert mapping.getIntroduction() == "Test introduction"
        assert result is mapping  # Test method chaining


DATAMAPPING_CLASS_NOTE = "Mapping of port elements (data elements and parameters) to frames and signals."
INTRODUCTION_NOTE = "This represents introductory documentation about the data mapping."


class TestDataMapping:
    """Spec-synced tests for the abstract DataMapping base (AUTOSAR_CP_TPS_SystemTemplate Table 5.22)."""

    class _ConcreteDataMapping(DataMapping):
        pass

    def _make(self) -> "TestDataMapping._ConcreteDataMapping":
        return TestDataMapping._ConcreteDataMapping()

    def _assert_docstring(self, method, note, attr_name=None):
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            DataMapping()

    def test_initialization(self):
        mapping = self._make()

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, DataMapping)
        assert mapping.getIntroduction() is None

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(DataMapping.__doc__).strip() == DATAMAPPING_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert DataMapping.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(DataMapping.__init__)
        assert "self.introduction: Optional[DocumentationBlock] = None" in source

    def test_get_set_introduction(self):
        mapping = self._make()

        assert mapping.getIntroduction() is None

        block = DocumentationBlock()
        assert mapping == mapping.setIntroduction(block)
        assert mapping.getIntroduction() is block

        assert mapping == mapping.setIntroduction(None)
        assert mapping.getIntroduction() is block

        getter_hints = get_type_hints(DataMapping.getIntroduction)
        assert getter_hints.get("return") == Optional[DocumentationBlock]

        setter_hints = get_type_hints(DataMapping.setIntroduction)
        assert setter_hints.get("value") == Optional[DocumentationBlock]
        assert setter_hints.get("return") is DataMapping

    def test_introduction_docstrings_are_spec_note(self):
        self._assert_docstring(DataMapping.getIntroduction, INTRODUCTION_NOTE)
        self._assert_docstring(DataMapping.setIntroduction, INTRODUCTION_NOTE, "introduction")


INDEXED_ARRAY_ELEMENT_CLASS_NOTE = (
    "This element represents exactly one indexed element in the array. Either the applicationArrayElement or implementationArrayElement reference shall be used.\n"
    "\n"
    "[constr_5471] Existence of SenderRecArrayElementMapping.indexedArrayElement: For each SenderRecArrayElementMapping, the aggregation in the role indexedArrayElement shall exist at the time when the Ecu Extract is complete.\n"
    "\n"
    "[constr_5472] Existence of IndexedArrayElement.index: For each IndexedArrayElement, the attribute index shall exist at the time when the Ecu Extract is complete.\n"
    "\n"
    "[constr_3231] Usage of IndexedArrayElement.applicationArrayElement: IndexedArrayElement.applicationArrayElement shall only be used if the referenced context element (VariableDataPrototype that is referenced by the SenderReceiverToSignalGroupMapping.dataElement) is typed by an ApplicationDataType.\n"
    "\n"
    "[constr_3245] Usage of IndexedArrayElement.implementationArrayElement: IndexedArrayElement.implementationArrayElement shall only be used if the referenced context element (VariableDataPrototype that is referenced by the SenderReceiverToSignalGroupMapping.dataElement) is typed by an ImplementationDataType."
)
APPLICATION_ARRAY_ELEMENT_NOTE = "Reference to an ApplicationArrayElement in an array."
IMPLEMENTATION_ARRAY_ELEMENT_NOTE = "Reference to an ImplementationDataTypeElement in an array."
INDEX_NOTE = "Position of an element in an array. Starting position is 0."


class TestIndexedArrayElement:
    """Spec-synced tests for IndexedArrayElement (AUTOSAR_CP_TPS_SystemTemplate Table 5.32)."""

    def _make(self) -> IndexedArrayElement:
        return IndexedArrayElement()

    def _assert_docstring(self, method, note, attr_name=None):
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def test_initialization(self):
        element = self._make()

        assert isinstance(element, ARObject)
        assert element.getApplicationArrayElementRef() is None
        assert element.getImplementationArrayElementRef() is None
        assert element.getIndex() is None

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(IndexedArrayElement.__doc__).strip() == INDEXED_ARRAY_ELEMENT_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert IndexedArrayElement.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(IndexedArrayElement.__init__)
        assert source.index("self.applicationArrayElementRef:") < source.index("self.implementationArrayElementRef:")
        assert source.index("self.implementationArrayElementRef:") < source.index("self.index:")

    def test_get_set_application_array_element_ref(self):
        element = self._make()

        assert element.getApplicationArrayElementRef() is None

        ref = RefType()
        assert element == element.setApplicationArrayElementRef(ref)
        assert element.getApplicationArrayElementRef() is ref

        assert element == element.setApplicationArrayElementRef(None)
        assert element.getApplicationArrayElementRef() is ref

        getter_hints = get_type_hints(IndexedArrayElement.getApplicationArrayElementRef)
        assert getter_hints.get("return") == Optional[RefType]

        setter_hints = get_type_hints(IndexedArrayElement.setApplicationArrayElementRef)
        assert setter_hints.get("value") == Optional[RefType]
        assert setter_hints.get("return") is IndexedArrayElement

    def test_get_set_implementation_array_element_ref(self):
        element = self._make()

        assert element.getImplementationArrayElementRef() is None

        ref = RefType()
        assert element == element.setImplementationArrayElementRef(ref)
        assert element.getImplementationArrayElementRef() is ref

        assert element == element.setImplementationArrayElementRef(None)
        assert element.getImplementationArrayElementRef() is ref

        getter_hints = get_type_hints(IndexedArrayElement.getImplementationArrayElementRef)
        assert getter_hints.get("return") == Optional[RefType]

        setter_hints = get_type_hints(IndexedArrayElement.setImplementationArrayElementRef)
        assert setter_hints.get("value") == Optional[RefType]
        assert setter_hints.get("return") is IndexedArrayElement

    def test_get_set_index(self):
        element = self._make()

        assert element.getIndex() is None

        index = Integer()
        index.setValue("3")
        assert element == element.setIndex(index)
        assert element.getIndex() is index

        assert element == element.setIndex(None)
        assert element.getIndex() is index

        getter_hints = get_type_hints(IndexedArrayElement.getIndex)
        assert getter_hints.get("return") == Optional[Integer]

        setter_hints = get_type_hints(IndexedArrayElement.setIndex)
        assert setter_hints.get("value") == Optional[Integer]
        assert setter_hints.get("return") is IndexedArrayElement

    def test_application_array_element_ref_docstrings_are_spec_note(self):
        self._assert_docstring(IndexedArrayElement.getApplicationArrayElementRef, APPLICATION_ARRAY_ELEMENT_NOTE)
        self._assert_docstring(IndexedArrayElement.setApplicationArrayElementRef, APPLICATION_ARRAY_ELEMENT_NOTE, "applicationArrayElementRef")

    def test_implementation_array_element_ref_docstrings_are_spec_note(self):
        self._assert_docstring(IndexedArrayElement.getImplementationArrayElementRef, IMPLEMENTATION_ARRAY_ELEMENT_NOTE)
        self._assert_docstring(IndexedArrayElement.setImplementationArrayElementRef, IMPLEMENTATION_ARRAY_ELEMENT_NOTE, "implementationArrayElementRef")

    def test_index_docstrings_are_spec_note(self):
        self._assert_docstring(IndexedArrayElement.getIndex, INDEX_NOTE)
        self._assert_docstring(IndexedArrayElement.setIndex, INDEX_NOTE, "index")
