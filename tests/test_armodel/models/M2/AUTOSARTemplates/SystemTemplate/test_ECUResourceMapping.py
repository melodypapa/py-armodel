
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import ECUMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_ECUMapping:
    """Test cases for ECUMapping class."""
    
    def test_ECUMapping(self):
        """Test ECUMapping class functionality."""
        parent = MockParent()
        mapping = ECUMapping(parent, "test_ecu_mapping")

        assert isinstance(mapping, Identifiable)
        
        # Test default values
        assert mapping.getCommControllerMappings() == []
        assert mapping.getEcuRef() is None
        assert mapping.getEcuInstanceRef() is None
        assert mapping.getHwPortMappings() == []
        
        # Test setter/getter methods
        mock_comm_controller = "mock_comm_controller"
        mapping.setCommControllerMappings([mock_comm_controller])
        assert mapping.getCommControllerMappings() == [mock_comm_controller]
        
        mock_ecu_ref = "mock_ecu_ref"
        mapping.setEcuRef(mock_ecu_ref)
        assert mapping.getEcuRef() == mock_ecu_ref
        
        mock_ecu_instance_ref = "mock_ecu_instance_ref"
        mapping.setEcuInstanceRef(mock_ecu_instance_ref)
        assert mapping.getEcuInstanceRef() == mock_ecu_instance_ref
        
        mock_hw_port = "mock_hw_port"
        mapping.setHwPortMappings([mock_hw_port])
        assert mapping.getHwPortMappings() == [mock_hw_port]