import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIp import (
    AbstractDoIpLogicAddressProps,
    DoIpLogicTargetAddressProps,
    DoIpLogicTesterAddressProps
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_DoIp:
    """Test cases for DoIP-related classes."""
    
    def test_AbstractDoIpLogicAddressProps(self):
        """Test AbstractDoIpLogicAddressProps abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
            AbstractDoIpLogicAddressProps(parent, "test_abstract")

    def test_DoIpLogicTargetAddressProps(self):
        """Test DoIpLogicTargetAddressProps class functionality."""
        parent = MockParent()
        props = DoIpLogicTargetAddressProps(parent, "test_target_addr")

        assert isinstance(props, Identifiable)
        assert isinstance(props, AbstractDoIpLogicAddressProps)
        
        # Test default values
        assert props.getShortName() == "test_target_addr"

    def test_DoIpLogicTesterAddressProps(self):
        """Test DoIpLogicTesterAddressProps class functionality."""
        parent = MockParent()
        props = DoIpLogicTesterAddressProps(parent, "test_tester_addr")

        assert isinstance(props, Identifiable)
        assert isinstance(props, AbstractDoIpLogicAddressProps)
        
        # Test default values
        assert props.getDoIpTesterRoutingActivationRef() is None
        
        # Test setter/getter
        mock_ref = "mock_ref"
        props.setDoIpTesterRoutingActivationRef(mock_ref)
        assert props.getDoIpTesterRoutingActivationRef() == mock_ref