import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import (
    FrameMapping,
    ISignalMapping,
    DefaultValueElement,
    PduMappingDefaultValue,
    TargetIPduRef,
    IPduMapping,
    Gateway
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


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
        assert ref.getTargetIPdu() is None

    def test_IPduMapping(self):
        """Test IPduMapping class functionality."""
        mapping = IPduMapping()

        assert isinstance(mapping, ARObject)
        
        # Test default values
        assert mapping.getIntroduction() is None
        assert mapping.getPdurTpChunkSize() is None
        assert mapping.getSourceIpduRef() is None
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