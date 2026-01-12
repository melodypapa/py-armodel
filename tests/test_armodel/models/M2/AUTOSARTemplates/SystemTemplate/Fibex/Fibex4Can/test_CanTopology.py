import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
    AbstractCanCommunicationControllerAttributes,
    CanControllerConfigurationRequirements,
    AbstractCanCommunicationController,
    CanCommunicationController,
    AbstractCanCommunicationConnector,
    CanCommunicationConnector
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    """Mock parent class to allow instantiation of classes that require a parent ARObject."""
    def __init__(self):
        super().__init__()


class Test_Fibex4CanTopology:
    """Test cases for Fibex4Can Topology classes."""
    
    def test_CanControllerFdConfiguration(self):
        """Test CanControllerFdConfiguration class functionality."""
        config = CanControllerFdConfiguration()

        assert isinstance(config, ARObject)
        
        # Test default values
        assert config.getPaddingValue() is None
        assert config.getPropSeg() is None
        assert config.getSspOffset() is None
        assert config.getSyncJumpWidth() is None
        assert config.getTimeSeg1() is None
        assert config.getTimeSeg2() is None
        assert config.getTxBitRateSwitch() is None
        
        # Test setter/getter methods
        config.setPaddingValue(8)
        assert config.getPaddingValue() == 8
        
        config.setPropSeg(5)
        assert config.getPropSeg() == 5

    def test_CanControllerFdConfigurationRequirements(self):
        """Test CanControllerFdConfigurationRequirements class functionality."""
        reqs = CanControllerFdConfigurationRequirements()

        assert isinstance(reqs, ARObject)
        
        # Test default values
        assert reqs.getMaxNumberOfTimeQuantaPerBit() is None
        assert reqs.getMaxSamplePoint() is None
        assert reqs.getMaxSyncJumpWidth() is None
        assert reqs.getMaxTrcvDelayCompensationOffset() is None
        assert reqs.getMinNumberOfTimeQuantaPerBit() is None
        assert reqs.getMinSamplePoint() is None
        assert reqs.getMinSyncJumpWidth() is None
        assert reqs.getMinTrcvDelayCompensationOffset() is None
        assert reqs.getPaddingValue() is None
        assert reqs.getTxBitRateSwitch() is None

    def test_AbstractCanCommunicationControllerAttributes(self):
        """Test AbstractCanCommunicationControllerAttributes class functionality."""
        attrs = AbstractCanCommunicationControllerAttributes()

        assert isinstance(attrs, ARObject)

    def test_CanControllerConfigurationRequirements(self):
        """Test CanControllerConfigurationRequirements class functionality."""
        reqs = CanControllerConfigurationRequirements()

        assert isinstance(reqs, AbstractCanCommunicationControllerAttributes)

    def test_AbstractCanCommunicationController(self):
        """Test AbstractCanCommunicationController abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            AbstractCanCommunicationController(parent, "test_abstract_controller")

    def test_CanCommunicationController(self):
        """Test CanCommunicationController class functionality."""
        parent = MockParent()
        controller = CanCommunicationController(parent, "test_can_comm_controller")

        assert isinstance(controller, CommunicationController)

    def test_AbstractCanCommunicationConnector(self):
        """Test AbstractCanCommunicationConnector abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            AbstractCanCommunicationConnector(parent, "test_abstract_connector")

    def test_CanCommunicationConnector(self):
        """Test CanCommunicationConnector class functionality."""
        parent = MockParent()
        connector = CanCommunicationConnector(parent, "test_can_comm_connector")

        assert isinstance(connector, CommunicationConnector)
        
        # Test default values
        assert connector.getPncWakeupCanId() is None
        assert connector.getPncWakeupCanIdExtended() is None
        assert connector.getPncWakeupCanIdMask() is None
        assert connector.getPncWakeupDataMask() is None
        assert connector.getPncWakeupDlc() is None
        
        # Test setter/getter methods
        connector.setPncWakeupCanId(123)
        assert connector.getPncWakeupCanId() == 123
        
        connector.setPncWakeupCanIdExtended(True)
        assert connector.getPncWakeupCanIdExtended() is True