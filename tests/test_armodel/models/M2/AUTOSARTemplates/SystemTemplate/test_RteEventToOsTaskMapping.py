
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import AppOsTaskProxyToEcuTaskProxyMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_RteEventToOsTaskMapping:
    """Test cases for RteEventToOsTaskMapping-related classes."""
    
    def test_AppOsTaskProxyToEcuTaskProxyMapping(self):
        """Test AppOsTaskProxyToEcuTaskProxyMapping class functionality."""
        parent = MockParent()
        mapping = AppOsTaskProxyToEcuTaskProxyMapping(parent, "test_app_ecu_mapping")

        assert isinstance(mapping, Identifiable)
        
        # Test default values
        assert mapping.getAppTaskProxyRef() is None
        assert mapping.getEcuTaskProxyRef() is None
        assert mapping.getOffset() is None
        
        # Test setter/getter methods
        mock_app_task_ref = "mock_app_task_ref"
        mapping.setAppTaskProxyRef(mock_app_task_ref)
        assert mapping.getAppTaskProxyRef() == mock_app_task_ref
        
        mock_ecu_task_ref = "mock_ecu_task_ref"
        mapping.setEcuTaskProxyRef(mock_ecu_task_ref)
        assert mapping.getEcuTaskProxyRef() == mock_ecu_task_ref
        
        mock_offset = "mock_offset"
        mapping.setOffset(mock_offset)
        assert mapping.getOffset() == mock_offset