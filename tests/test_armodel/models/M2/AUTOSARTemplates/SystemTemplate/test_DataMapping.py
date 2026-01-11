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
        mapping.setCommunicationDirection(mock_direction)
        assert mapping.getCommunicationDirection() == mock_direction

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

    def test_SenderRecArrayElementMapping(self):
        """Test SenderRecArrayElementMapping class functionality."""
        mapping = SenderRecArrayElementMapping()

        assert isinstance(mapping, ARObject)
        
        # Test default values
        assert mapping.getComplexTypeMapping() is None
        assert mapping.getIndexedArrayElement() is None
        assert mapping.getSystemSignalRef() is None

    def test_SenderRecArrayTypeMapping(self):
        """Test SenderRecArrayTypeMapping class functionality."""
        mapping = SenderRecArrayTypeMapping()

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, SenderRecCompositeTypeMapping)
        
        # Test default values
        assert mapping.getArrayElementMappings() == []
        assert mapping.getSenderToSignal() is None
        assert mapping.getSignalToReceiverTextTableMapping() is None

    def test_SenderReceiverToSignalGroupMapping(self):
        """Test SenderReceiverToSignalGroupMapping class functionality."""
        mapping = SenderReceiverToSignalGroupMapping()

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, DataMapping)
        
        # Test default values
        assert mapping.getDataElementIRef() is None
        assert mapping.getSignalGroupRef() is None
        assert mapping.getTypeMapping() is None