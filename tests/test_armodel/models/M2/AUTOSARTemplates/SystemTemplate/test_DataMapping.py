import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    DataMapping,
    SenderReceiverToSignalMapping,
    SenderRecCompositeTypeMapping,
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
    IndexedArrayElement,
    SenderRecArrayElementMapping,
    SenderRecArrayTypeMapping,
    SenderReceiverToSignalGroupMapping
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationDirectionType


class Test_DataMapping:
    """Test cases for DataMapping class and related data mapping classes."""
    
    def test_DataMapping(self):
        """Test DataMapping abstract class instantiation."""
        with pytest.raises(NotImplementedError):
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
        with pytest.raises(NotImplementedError):
            SenderRecCompositeTypeMapping()

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

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, SenderRecCompositeTypeMapping)
        
        # Test default values
        assert mapping.getArrayElementMappings() == []
        assert mapping.getSenderToSignal() is None
        assert mapping.getSignalToReceiverTextTableMapping() is None

        # Test setter methods
        mock_mappings = [SenderRecArrayElementMapping()]
        result = mapping.setArrayElementMappings(mock_mappings)
        assert mapping.getArrayElementMappings() == mock_mappings
        assert result is mapping  # Test method chaining

        mapping.setArrayElementMappings(None)
        assert mapping.getArrayElementMappings() == mock_mappings  # Should remain unchanged
        
        mock_text_mapping = "TextMapping"
        result = mapping.setSenderToSignal(mock_text_mapping)
        assert mapping.getSenderToSignal() == mock_text_mapping
        assert result is mapping  # Test method chaining

        mapping.setSenderToSignal(None)
        assert mapping.getSenderToSignal() == mock_text_mapping  # Should remain unchanged
        
        result = mapping.setSignalToReceiverTextTableMapping(mock_text_mapping)
        assert mapping.getSignalToReceiverTextTableMapping() == mock_text_mapping
        assert result is mapping  # Test method chaining

        mapping.setSignalToReceiverTextTableMapping(None)
        assert mapping.getSignalToReceiverTextTableMapping() == mock_text_mapping  # Should remain unchanged

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