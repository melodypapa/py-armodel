import inspect
from typing import List, Optional, get_type_hints

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
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
        assert mapping.getDataElementIRef() is None
        assert mapping.getSenderToSignalTextTableMapping() is None
        assert mapping.getSignalToReceiverTextTableMapping() is None
        assert mapping.getSystemSignalRef() is None

        # Test setter methods
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


SENDER_REC_RECORD_ELEMENT_MAPPING_CLASS_NOTE = (
    "Mapping of a primitive record element to a SystemSignal. "
    "If the VariableDataPrototype that is referenced by SenderReceiverToSignalGroupMapping is typed by an ApplicationDataType the reference application RecordElement shall be used. "
    "If the VariableDataPrototype is typed by the ImplementationDataType the reference implementationRecordElement shall be used. "
    "Either the implementationRecordElement or applicationRecordElement reference shall be used. "
    "If the element is composite, there will be no mapping to the SystemSignal (multiplicity 0). "
    "In this case the RecordElementMapping element will aggregate the complexTypeMapping element. "
    "In that way also the composite datatypes can be mapped to SystemSignals."
)
APPLICATION_RECORD_ELEMENT_NOTE = "Reference to an ApplicationRecordElement in the context of the dataElement or in the context of a composite element."
COMPLEX_TYPE_MAPPING_NOTE = "This aggregation will be used if the element is composite."
IMPLEMENTATION_RECORD_ELEMENT_NOTE = "Reference to an ImplementationRecordElement in the context of the dataElement or in the context of a composite element."
SENDER_TO_SIGNAL_TEXT_TABLE_MAPPING_NOTE = (
    "This mapping allows for the text-table translation between the sending DataPrototype that is defined in the Port Prototype and the physicalProps defined for the System Signal."
)
SIGNAL_TO_RECEIVER_TEXT_TABLE_MAPPING_NOTE = (
    "This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the Port Prototype."
)
SYSTEM_SIGNAL_NOTE = "Reference to the system signal used to carry the primitive ApplicationRecordElement."


class TestSenderRecRecordElementMapping:
    """Spec-synced tests for SenderRecRecordElementMapping (AUTOSAR_CP_TPS_SystemTemplate Table 5.30)."""

    def _make(self) -> SenderRecRecordElementMapping:
        return SenderRecRecordElementMapping()

    def _assert_docstring(self, method, note, attr_name=None):
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def test_initialization(self):
        mapping = self._make()

        assert isinstance(mapping, ARObject)
        assert mapping.getApplicationRecordElementRef() is None
        assert mapping.getComplexTypeMapping() is None
        assert mapping.getImplementationRecordElementRef() is None
        assert mapping.getSenderToSignalTextTableMapping() is None
        assert mapping.getSignalToReceiverTextTableMapping() is None
        assert mapping.getSystemSignalRef() is None

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(SenderRecRecordElementMapping.__doc__).strip() == SENDER_REC_RECORD_ELEMENT_MAPPING_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert SenderRecRecordElementMapping.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(SenderRecRecordElementMapping.__init__)
        assert source.index("self.applicationRecordElementRef:") < source.index("self.complexTypeMapping:")
        assert source.index("self.complexTypeMapping:") < source.index("self.implementationRecordElementRef:")
        assert source.index("self.implementationRecordElementRef:") < source.index("self.senderToSignalTextTableMapping:")
        assert source.index("self.senderToSignalTextTableMapping:") < source.index("self.signalToReceiverTextTableMapping:")
        assert source.index("self.signalToReceiverTextTableMapping:") < source.index("self.systemSignalRef:")

    def test_get_set_application_record_element_ref(self):
        mapping = self._make()

        assert mapping.getApplicationRecordElementRef() is None

        ref = RefType()
        assert mapping == mapping.setApplicationRecordElementRef(ref)
        assert mapping.getApplicationRecordElementRef() is ref

        assert mapping == mapping.setApplicationRecordElementRef(None)
        assert mapping.getApplicationRecordElementRef() is ref

        getter_hints = get_type_hints(SenderRecRecordElementMapping.getApplicationRecordElementRef)
        assert getter_hints.get("return") == Optional[RefType]

        setter_hints = get_type_hints(SenderRecRecordElementMapping.setApplicationRecordElementRef)
        assert setter_hints.get("value") == Optional[RefType]
        assert setter_hints.get("return") is SenderRecRecordElementMapping

    def test_get_set_complex_type_mapping(self):
        mapping = self._make()

        assert mapping.getComplexTypeMapping() is None

        type_mapping = SenderRecRecordTypeMapping()
        assert mapping == mapping.setComplexTypeMapping(type_mapping)
        assert mapping.getComplexTypeMapping() is type_mapping

        assert mapping == mapping.setComplexTypeMapping(None)
        assert mapping.getComplexTypeMapping() is type_mapping

        getter_hints = get_type_hints(SenderRecRecordElementMapping.getComplexTypeMapping)
        assert getter_hints.get("return") == Optional[SenderRecCompositeTypeMapping]

        setter_hints = get_type_hints(SenderRecRecordElementMapping.setComplexTypeMapping)
        assert setter_hints.get("value") == Optional[SenderRecCompositeTypeMapping]
        assert setter_hints.get("return") is SenderRecRecordElementMapping

    def test_get_set_implementation_record_element_ref(self):
        mapping = self._make()

        assert mapping.getImplementationRecordElementRef() is None

        ref = RefType()
        assert mapping == mapping.setImplementationRecordElementRef(ref)
        assert mapping.getImplementationRecordElementRef() is ref

        assert mapping == mapping.setImplementationRecordElementRef(None)
        assert mapping.getImplementationRecordElementRef() is ref

        getter_hints = get_type_hints(SenderRecRecordElementMapping.getImplementationRecordElementRef)
        assert getter_hints.get("return") == Optional[RefType]

        setter_hints = get_type_hints(SenderRecRecordElementMapping.setImplementationRecordElementRef)
        assert setter_hints.get("value") == Optional[RefType]
        assert setter_hints.get("return") is SenderRecRecordElementMapping

    def test_get_set_sender_to_signal_text_table_mapping(self):
        mapping = self._make()

        assert mapping.getSenderToSignalTextTableMapping() is None

        text_mapping = TextTableMapping()
        assert mapping == mapping.setSenderToSignalTextTableMapping(text_mapping)
        assert mapping.getSenderToSignalTextTableMapping() is text_mapping

        assert mapping == mapping.setSenderToSignalTextTableMapping(None)
        assert mapping.getSenderToSignalTextTableMapping() is text_mapping

        getter_hints = get_type_hints(SenderRecRecordElementMapping.getSenderToSignalTextTableMapping)
        assert getter_hints.get("return") == Optional[TextTableMapping]

        setter_hints = get_type_hints(SenderRecRecordElementMapping.setSenderToSignalTextTableMapping)
        assert setter_hints.get("value") == Optional[TextTableMapping]
        assert setter_hints.get("return") is SenderRecRecordElementMapping

    def test_get_set_signal_to_receiver_text_table_mapping(self):
        mapping = self._make()

        assert mapping.getSignalToReceiverTextTableMapping() is None

        text_mapping = TextTableMapping()
        assert mapping == mapping.setSignalToReceiverTextTableMapping(text_mapping)
        assert mapping.getSignalToReceiverTextTableMapping() is text_mapping

        assert mapping == mapping.setSignalToReceiverTextTableMapping(None)
        assert mapping.getSignalToReceiverTextTableMapping() is text_mapping

        getter_hints = get_type_hints(SenderRecRecordElementMapping.getSignalToReceiverTextTableMapping)
        assert getter_hints.get("return") == Optional[TextTableMapping]

        setter_hints = get_type_hints(SenderRecRecordElementMapping.setSignalToReceiverTextTableMapping)
        assert setter_hints.get("value") == Optional[TextTableMapping]
        assert setter_hints.get("return") is SenderRecRecordElementMapping

    def test_get_set_system_signal_ref(self):
        mapping = self._make()

        assert mapping.getSystemSignalRef() is None

        ref = RefType()
        assert mapping == mapping.setSystemSignalRef(ref)
        assert mapping.getSystemSignalRef() is ref

        assert mapping == mapping.setSystemSignalRef(None)
        assert mapping.getSystemSignalRef() is ref

        getter_hints = get_type_hints(SenderRecRecordElementMapping.getSystemSignalRef)
        assert getter_hints.get("return") == Optional[RefType]

        setter_hints = get_type_hints(SenderRecRecordElementMapping.setSystemSignalRef)
        assert setter_hints.get("value") == Optional[RefType]
        assert setter_hints.get("return") is SenderRecRecordElementMapping

    def test_application_record_element_ref_docstrings_are_spec_note(self):
        self._assert_docstring(SenderRecRecordElementMapping.getApplicationRecordElementRef, APPLICATION_RECORD_ELEMENT_NOTE)
        self._assert_docstring(SenderRecRecordElementMapping.setApplicationRecordElementRef, APPLICATION_RECORD_ELEMENT_NOTE, "applicationRecordElementRef")

    def test_complex_type_mapping_docstrings_are_spec_note(self):
        self._assert_docstring(SenderRecRecordElementMapping.getComplexTypeMapping, COMPLEX_TYPE_MAPPING_NOTE)
        self._assert_docstring(SenderRecRecordElementMapping.setComplexTypeMapping, COMPLEX_TYPE_MAPPING_NOTE, "complexTypeMapping")

    def test_implementation_record_element_ref_docstrings_are_spec_note(self):
        self._assert_docstring(SenderRecRecordElementMapping.getImplementationRecordElementRef, IMPLEMENTATION_RECORD_ELEMENT_NOTE)
        self._assert_docstring(SenderRecRecordElementMapping.setImplementationRecordElementRef, IMPLEMENTATION_RECORD_ELEMENT_NOTE, "implementationRecordElementRef")

    def test_sender_to_signal_text_table_mapping_docstrings_are_spec_note(self):
        self._assert_docstring(SenderRecRecordElementMapping.getSenderToSignalTextTableMapping, SENDER_TO_SIGNAL_TEXT_TABLE_MAPPING_NOTE)
        self._assert_docstring(SenderRecRecordElementMapping.setSenderToSignalTextTableMapping, SENDER_TO_SIGNAL_TEXT_TABLE_MAPPING_NOTE, "senderToSignalTextTableMapping")

    def test_signal_to_receiver_text_table_mapping_docstrings_are_spec_note(self):
        self._assert_docstring(SenderRecRecordElementMapping.getSignalToReceiverTextTableMapping, SIGNAL_TO_RECEIVER_TEXT_TABLE_MAPPING_NOTE)
        self._assert_docstring(SenderRecRecordElementMapping.setSignalToReceiverTextTableMapping, SIGNAL_TO_RECEIVER_TEXT_TABLE_MAPPING_NOTE, "signalToReceiverTextTableMapping")

    def test_system_signal_ref_docstrings_are_spec_note(self):
        self._assert_docstring(SenderRecRecordElementMapping.getSystemSignalRef, SYSTEM_SIGNAL_NOTE)
        self._assert_docstring(SenderRecRecordElementMapping.setSystemSignalRef, SYSTEM_SIGNAL_NOTE, "systemSignalRef")


SENDER_REC_RECORD_TYPE_MAPPING_CLASS_NOTE = 'If the ApplicationCompositeDataType is a Record, the "RecordTypeMapping" will be used.'
RECORD_ELEMENT_MAPPING_NOTE = "Each ApplicationRecordElement shall be mapped on a SystemSignal."


class TestSenderRecRecordTypeMapping:
    """Spec-synced tests for SenderRecRecordTypeMapping (AUTOSAR_CP_TPS_SystemTemplate Table 5.29)."""

    def _make(self) -> SenderRecRecordTypeMapping:
        return SenderRecRecordTypeMapping()

    def _assert_docstring(self, method, note, attr_name=None):
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not extend the %s list." % attr_name
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def test_initialization(self):
        mapping = self._make()

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, SenderRecCompositeTypeMapping)
        assert mapping.getRecordElementMappings() == []

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(SenderRecRecordTypeMapping.__doc__).strip() == SENDER_REC_RECORD_TYPE_MAPPING_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert SenderRecRecordTypeMapping.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(SenderRecRecordTypeMapping.__init__)
        assert "self.recordElementMappings:" in source

    def test_get_add_record_element_mappings(self):
        mapping = self._make()

        assert mapping.getRecordElementMappings() == []

        first = SenderRecRecordElementMapping()
        second = SenderRecRecordElementMapping()
        assert mapping == mapping.addRecordElementMapping(first)
        assert mapping.getRecordElementMappings() == [first]
        assert mapping == mapping.addRecordElementMapping(second)
        assert mapping.getRecordElementMappings() == [first, second]

        assert mapping == mapping.addRecordElementMapping(None)
        assert mapping.getRecordElementMappings() == [first, second]

        getter_hints = get_type_hints(SenderRecRecordTypeMapping.getRecordElementMappings)
        assert getter_hints.get("return") == List[SenderRecRecordElementMapping]

        add_hints = get_type_hints(SenderRecRecordTypeMapping.addRecordElementMapping)
        assert add_hints.get("value") == Optional[SenderRecRecordElementMapping]
        assert add_hints.get("return") is SenderRecRecordTypeMapping

    def test_record_element_mappings_docstrings_are_spec_note(self):
        self._assert_docstring(SenderRecRecordTypeMapping.getRecordElementMappings, RECORD_ELEMENT_MAPPING_NOTE)
        self._assert_docstring(SenderRecRecordTypeMapping.addRecordElementMapping, RECORD_ELEMENT_MAPPING_NOTE, "recordElementMappings")


SENDER_RECEIVER_TO_SIGNAL_MAPPING_CLASS_NOTE = (
    "Mapping of a sender receiver communication data element to a signal.\n"
    "\n"
    "[constr_5466] Existence of SenderReceiverToSignalMapping.dataElement: For each SenderReceiverToSignalMapping, the reference to VariableDataPrototype in the role dataElement shall exist at the time when the Ecu Extract is complete.\n"
    "\n"
    "[constr_5467] Existence of SenderReceiverToSignalMapping.systemSignal: For each SenderReceiverToSignalMapping, the reference to SystemSignal in the role systemSignal shall exist at the time when the Ecu Extract is complete."
)
DATA_ELEMENT_NOTE = "Reference to the data element. InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef"
SENDER_TO_SIGNAL_TEXT_TABLE_MAPPING_NOTE = "This mapping allows for the text-table translation between the sending DataPrototype that is defined in the Port Prototype and the physicalProps defined for the System Signal."
SIGNAL_TO_RECEIVER_TEXT_TABLE_MAPPING_NOTE = "This mapping allows for the text-table translation between the physicalProps defined for the SystemSignal and a receiving DataPrototype that is defined in the Port Prototype."
SYSTEM_SIGNAL_CARRY_NOTE = "Reference to the system signal used to carry the data element."


class TestSenderReceiverToSignalMapping:
    """Spec-synced tests for SenderReceiverToSignalMapping (AUTOSAR_CP_TPS_SystemTemplate Table 5.24)."""

    def _make(self) -> SenderReceiverToSignalMapping:
        return SenderReceiverToSignalMapping()

    def _assert_docstring(self, method, note, attr_name=None):
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def test_initialization(self):
        mapping = self._make()

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, DataMapping)
        assert mapping.getIntroduction() is None
        assert mapping.getDataElementIRef() is None
        assert mapping.getSenderToSignalTextTableMapping() is None
        assert mapping.getSignalToReceiverTextTableMapping() is None
        assert mapping.getSystemSignalRef() is None

    def test_removed_communication_direction(self):
        mapping = self._make()

        assert not hasattr(mapping, "getCommunicationDirection")
        assert not hasattr(mapping, "setCommunicationDirection")

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(SenderReceiverToSignalMapping.__doc__).strip() == SENDER_RECEIVER_TO_SIGNAL_MAPPING_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert SenderReceiverToSignalMapping.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(SenderReceiverToSignalMapping.__init__)
        assert source.index("self.dataElementIRef:") < source.index("self.senderToSignalTextTableMapping:")
        assert source.index("self.senderToSignalTextTableMapping:") < source.index("self.signalToReceiverTextTableMapping:")
        assert source.index("self.signalToReceiverTextTableMapping:") < source.index("self.systemSignalRef:")

    def test_get_set_data_element_iref(self):
        mapping = self._make()

        assert mapping.getDataElementIRef() is None

        iref = VariableDataPrototypeInSystemInstanceRef()
        assert mapping == mapping.setDataElementIRef(iref)
        assert mapping.getDataElementIRef() is iref

        assert mapping == mapping.setDataElementIRef(None)
        assert mapping.getDataElementIRef() is iref

        getter_hints = get_type_hints(SenderReceiverToSignalMapping.getDataElementIRef)
        assert getter_hints.get("return") == Optional[VariableDataPrototypeInSystemInstanceRef]

        setter_hints = get_type_hints(SenderReceiverToSignalMapping.setDataElementIRef)
        assert setter_hints.get("value") == Optional[VariableDataPrototypeInSystemInstanceRef]
        assert setter_hints.get("return") is SenderReceiverToSignalMapping

    def test_get_set_sender_to_signal_text_table_mapping(self):
        mapping = self._make()

        assert mapping.getSenderToSignalTextTableMapping() is None

        text_mapping = TextTableMapping()
        assert mapping == mapping.setSenderToSignalTextTableMapping(text_mapping)
        assert mapping.getSenderToSignalTextTableMapping() is text_mapping

        assert mapping == mapping.setSenderToSignalTextTableMapping(None)
        assert mapping.getSenderToSignalTextTableMapping() is text_mapping

        getter_hints = get_type_hints(SenderReceiverToSignalMapping.getSenderToSignalTextTableMapping)
        assert getter_hints.get("return") == Optional[TextTableMapping]

        setter_hints = get_type_hints(SenderReceiverToSignalMapping.setSenderToSignalTextTableMapping)
        assert setter_hints.get("value") == Optional[TextTableMapping]
        assert setter_hints.get("return") is SenderReceiverToSignalMapping

    def test_get_set_signal_to_receiver_text_table_mapping(self):
        mapping = self._make()

        assert mapping.getSignalToReceiverTextTableMapping() is None

        text_mapping = TextTableMapping()
        assert mapping == mapping.setSignalToReceiverTextTableMapping(text_mapping)
        assert mapping.getSignalToReceiverTextTableMapping() is text_mapping

        assert mapping == mapping.setSignalToReceiverTextTableMapping(None)
        assert mapping.getSignalToReceiverTextTableMapping() is text_mapping

        getter_hints = get_type_hints(SenderReceiverToSignalMapping.getSignalToReceiverTextTableMapping)
        assert getter_hints.get("return") == Optional[TextTableMapping]

        setter_hints = get_type_hints(SenderReceiverToSignalMapping.setSignalToReceiverTextTableMapping)
        assert setter_hints.get("value") == Optional[TextTableMapping]
        assert setter_hints.get("return") is SenderReceiverToSignalMapping

    def test_get_set_system_signal_ref(self):
        mapping = self._make()

        assert mapping.getSystemSignalRef() is None

        ref = RefType()
        assert mapping == mapping.setSystemSignalRef(ref)
        assert mapping.getSystemSignalRef() is ref

        assert mapping == mapping.setSystemSignalRef(None)
        assert mapping.getSystemSignalRef() is ref

        getter_hints = get_type_hints(SenderReceiverToSignalMapping.getSystemSignalRef)
        assert getter_hints.get("return") == Optional[RefType]

        setter_hints = get_type_hints(SenderReceiverToSignalMapping.setSystemSignalRef)
        assert setter_hints.get("value") == Optional[RefType]
        assert setter_hints.get("return") is SenderReceiverToSignalMapping

    def test_data_element_docstrings_are_spec_note(self):
        self._assert_docstring(SenderReceiverToSignalMapping.getDataElementIRef, DATA_ELEMENT_NOTE)
        self._assert_docstring(SenderReceiverToSignalMapping.setDataElementIRef, DATA_ELEMENT_NOTE, "dataElementIRef")

    def test_sender_to_signal_text_table_mapping_docstrings_are_spec_note(self):
        self._assert_docstring(SenderReceiverToSignalMapping.getSenderToSignalTextTableMapping, SENDER_TO_SIGNAL_TEXT_TABLE_MAPPING_NOTE)
        self._assert_docstring(SenderReceiverToSignalMapping.setSenderToSignalTextTableMapping, SENDER_TO_SIGNAL_TEXT_TABLE_MAPPING_NOTE, "senderToSignalTextTableMapping")

    def test_signal_to_receiver_text_table_mapping_docstrings_are_spec_note(self):
        self._assert_docstring(SenderReceiverToSignalMapping.getSignalToReceiverTextTableMapping, SIGNAL_TO_RECEIVER_TEXT_TABLE_MAPPING_NOTE)
        self._assert_docstring(SenderReceiverToSignalMapping.setSignalToReceiverTextTableMapping, SIGNAL_TO_RECEIVER_TEXT_TABLE_MAPPING_NOTE, "signalToReceiverTextTableMapping")

    def test_system_signal_ref_docstrings_are_spec_note(self):
        self._assert_docstring(SenderReceiverToSignalMapping.getSystemSignalRef, SYSTEM_SIGNAL_CARRY_NOTE)
        self._assert_docstring(SenderReceiverToSignalMapping.setSystemSignalRef, SYSTEM_SIGNAL_CARRY_NOTE, "systemSignalRef")

    def test_inherited_introduction_accessors(self):
        mapping = self._make()

        assert mapping.getIntroduction() is None

        block = DocumentationBlock()
        assert mapping == mapping.setIntroduction(block)
        assert mapping.getIntroduction() is block
