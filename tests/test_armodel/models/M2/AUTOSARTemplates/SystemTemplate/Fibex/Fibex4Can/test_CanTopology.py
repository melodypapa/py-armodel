import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
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

        # Test setter/getter methods with method chaining - with None
        assert config == config.setPaddingValue(None)  # Test method chaining with None
        assert config.getPaddingValue() is None  # Should remain None

        assert config == config.setPropSeg(None)  # Test method chaining with None
        assert config.getPropSeg() is None  # Should remain None

        assert config == config.setSspOffset(None)  # Test method chaining with None
        assert config.getSspOffset() is None  # Should remain None

        assert config == config.setSyncJumpWidth(None)  # Test method chaining with None
        assert config.getSyncJumpWidth() is None  # Should remain None

        assert config == config.setTimeSeg1(None)  # Test method chaining with None
        assert config.getTimeSeg1() is None  # Should remain None

        assert config == config.setTimeSeg2(None)  # Test method chaining with None
        assert config.getTimeSeg2() is None  # Should remain None

        assert config == config.setTxBitRateSwitch(None)  # Test method chaining with None
        assert config.getTxBitRateSwitch() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        config.setPaddingValue(8)
        assert config.getPaddingValue() == 8
        assert config == config.setPaddingValue(8)  # Test method chaining

        config.setPropSeg(5)
        assert config.getPropSeg() == 5
        assert config == config.setPropSeg(5)  # Test method chaining

        config.setSspOffset(3)
        assert config.getSspOffset() == 3
        assert config == config.setSspOffset(3)  # Test method chaining

        config.setSyncJumpWidth(4)
        assert config.getSyncJumpWidth() == 4
        assert config == config.setSyncJumpWidth(4)  # Test method chaining

        config.setTimeSeg1(6)
        assert config.getTimeSeg1() == 6
        assert config == config.setTimeSeg1(6)  # Test method chaining

        config.setTimeSeg2(7)
        assert config.getTimeSeg2() == 7
        assert config == config.setTimeSeg2(7)  # Test method chaining

        config.setTxBitRateSwitch(True)
        assert config.getTxBitRateSwitch() is True
        assert config == config.setTxBitRateSwitch(True)  # Test method chaining

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

        # Test setter/getter methods with method chaining - with None
        assert reqs == reqs.setMaxNumberOfTimeQuantaPerBit(None)  # Test method chaining with None
        assert reqs.getMaxNumberOfTimeQuantaPerBit() is None  # Should remain None

        assert reqs == reqs.setMaxSamplePoint(None)  # Test method chaining with None
        assert reqs.getMaxSamplePoint() is None  # Should remain None

        assert reqs == reqs.setMaxSyncJumpWidth(None)  # Test method chaining with None
        assert reqs.getMaxSyncJumpWidth() is None  # Should remain None

        assert reqs == reqs.setMaxTrcvDelayCompensationOffset(None)  # Test method chaining with None
        assert reqs.getMaxTrcvDelayCompensationOffset() is None  # Should remain None

        assert reqs == reqs.setMinNumberOfTimeQuantaPerBit(None)  # Test method chaining with None
        assert reqs.getMinNumberOfTimeQuantaPerBit() is None  # Should remain None

        assert reqs == reqs.setMinSamplePoint(None)  # Test method chaining with None
        assert reqs.getMinSamplePoint() is None  # Should remain None

        assert reqs == reqs.setMinSyncJumpWidth(None)  # Test method chaining with None
        assert reqs.getMinSyncJumpWidth() is None  # Should remain None

        assert reqs == reqs.setMinTrcvDelayCompensationOffset(None)  # Test method chaining with None
        assert reqs.getMinTrcvDelayCompensationOffset() is None  # Should remain None

        assert reqs == reqs.setPaddingValue(None)  # Test method chaining with None
        assert reqs.getPaddingValue() is None  # Should remain None

        assert reqs == reqs.setTxBitRateSwitch(None)  # Test method chaining with None
        assert reqs.getTxBitRateSwitch() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        reqs.setMaxNumberOfTimeQuantaPerBit(10)
        assert reqs.getMaxNumberOfTimeQuantaPerBit() == 10
        assert reqs == reqs.setMaxNumberOfTimeQuantaPerBit(10)  # Test method chaining

        reqs.setMaxSamplePoint(0.8)
        assert reqs.getMaxSamplePoint() == 0.8
        assert reqs == reqs.setMaxSamplePoint(0.8)  # Test method chaining

        reqs.setMaxSyncJumpWidth(0.2)
        assert reqs.getMaxSyncJumpWidth() == 0.2
        assert reqs == reqs.setMaxSyncJumpWidth(0.2)  # Test method chaining

        reqs.setMaxTrcvDelayCompensationOffset(1000)
        assert reqs.getMaxTrcvDelayCompensationOffset() == 1000
        assert reqs == reqs.setMaxTrcvDelayCompensationOffset(1000)  # Test method chaining

        reqs.setMinNumberOfTimeQuantaPerBit(5)
        assert reqs.getMinNumberOfTimeQuantaPerBit() == 5
        assert reqs == reqs.setMinNumberOfTimeQuantaPerBit(5)  # Test method chaining

        reqs.setMinSamplePoint(0.4)
        assert reqs.getMinSamplePoint() == 0.4
        assert reqs == reqs.setMinSamplePoint(0.4)  # Test method chaining

        reqs.setMinSyncJumpWidth(0.1)
        assert reqs.getMinSyncJumpWidth() == 0.1
        assert reqs == reqs.setMinSyncJumpWidth(0.1)  # Test method chaining

        reqs.setMinTrcvDelayCompensationOffset(500)
        assert reqs.getMinTrcvDelayCompensationOffset() == 500
        assert reqs == reqs.setMinTrcvDelayCompensationOffset(500)  # Test method chaining

        reqs.setPaddingValue(16)
        assert reqs.getPaddingValue() == 16
        assert reqs == reqs.setPaddingValue(16)  # Test method chaining

        reqs.setTxBitRateSwitch(True)
        assert reqs.getTxBitRateSwitch() is True
        assert reqs == reqs.setTxBitRateSwitch(True)  # Test method chaining

    def test_CanControllerXlConfiguration(self):
        """Test CanControllerXlConfiguration class functionality."""
        config = CanControllerXlConfiguration()

        assert isinstance(config, ARObject)

        # Test default values
        assert config.getArbitrationPhaseSeg1() is None
        assert config.getArbitrationPhaseSeg2() is None
        assert config.getArbitrationSJW() is None
        assert config.getDataPhaseSeg1() is None
        assert config.getDataPhaseSeg2() is None
        assert config.getDataSJW() is None
        assert config.getMinArbitrationBitTime() is None
        assert config.getMinDataBitTime() is None
        assert config.getPaddingValue() is None
        assert config.getTimeSeg1Arbitration() is None
        assert config.getTimeSeg1Data() is None
        assert config.getTimeSeg2Arbitration() is None
        assert config.getTimeSeg2Data() is None
        assert config.getXlBitRateSwitch() is None

        # Test setter/getter methods with method chaining - with None
        assert config == config.setArbitrationPhaseSeg1(None)  # Test method chaining with None
        assert config.getArbitrationPhaseSeg1() is None  # Should remain None

        assert config == config.setArbitrationPhaseSeg2(None)  # Test method chaining with None
        assert config.getArbitrationPhaseSeg2() is None  # Should remain None

        assert config == config.setArbitrationSJW(None)  # Test method chaining with None
        assert config.getArbitrationSJW() is None  # Should remain None

        assert config == config.setDataPhaseSeg1(None)  # Test method chaining with None
        assert config.getDataPhaseSeg1() is None  # Should remain None

        assert config == config.setDataPhaseSeg2(None)  # Test method chaining with None
        assert config.getDataPhaseSeg2() is None  # Should remain None

        assert config == config.setDataSJW(None)  # Test method chaining with None
        assert config.getDataSJW() is None  # Should remain None

        assert config == config.setMinArbitrationBitTime(None)  # Test method chaining with None
        assert config.getMinArbitrationBitTime() is None  # Should remain None

        assert config == config.setMinDataBitTime(None)  # Test method chaining with None
        assert config.getMinDataBitTime() is None  # Should remain None

        assert config == config.setPaddingValue(None)  # Test method chaining with None
        assert config.getPaddingValue() is None  # Should remain None

        assert config == config.setTimeSeg1Arbitration(None)  # Test method chaining with None
        assert config.getTimeSeg1Arbitration() is None  # Should remain None

        assert config == config.setTimeSeg1Data(None)  # Test method chaining with None
        assert config.getTimeSeg1Data() is None  # Should remain None

        assert config == config.setTimeSeg2Arbitration(None)  # Test method chaining with None
        assert config.getTimeSeg2Arbitration() is None  # Should remain None

        assert config == config.setTimeSeg2Data(None)  # Test method chaining with None
        assert config.getTimeSeg2Data() is None  # Should remain None

        assert config == config.setXlBitRateSwitch(None)  # Test method chaining with None
        assert config.getXlBitRateSwitch() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        config.setArbitrationPhaseSeg1(8)
        assert config.getArbitrationPhaseSeg1() == 8
        assert config == config.setArbitrationPhaseSeg1(8)  # Test method chaining

        config.setArbitrationPhaseSeg2(6)
        assert config.getArbitrationPhaseSeg2() == 6
        assert config == config.setArbitrationPhaseSeg2(6)  # Test method chaining

        config.setArbitrationSJW(4)
        assert config.getArbitrationSJW() == 4
        assert config == config.setArbitrationSJW(4)  # Test method chaining

        config.setDataPhaseSeg1(10)
        assert config.getDataPhaseSeg1() == 10
        assert config == config.setDataPhaseSeg1(10)  # Test method chaining

        config.setDataPhaseSeg2(8)
        assert config.getDataPhaseSeg2() == 8
        assert config == config.setDataPhaseSeg2(8)  # Test method chaining

        config.setDataSJW(5)
        assert config.getDataSJW() == 5
        assert config == config.setDataSJW(5)  # Test method chaining

        config.setMinArbitrationBitTime(1000)
        assert config.getMinArbitrationBitTime() == 1000
        assert config == config.setMinArbitrationBitTime(1000)  # Test method chaining

        config.setMinDataBitTime(500)
        assert config.getMinDataBitTime() == 500
        assert config == config.setMinDataBitTime(500)  # Test method chaining

        config.setPaddingValue(16)
        assert config.getPaddingValue() == 16
        assert config == config.setPaddingValue(16)  # Test method chaining

        config.setTimeSeg1Arbitration(7)
        assert config.getTimeSeg1Arbitration() == 7
        assert config == config.setTimeSeg1Arbitration(7)  # Test method chaining

        config.setTimeSeg1Data(9)
        assert config.getTimeSeg1Data() == 9
        assert config == config.setTimeSeg1Data(9)  # Test method chaining

        config.setTimeSeg2Arbitration(5)
        assert config.getTimeSeg2Arbitration() == 5
        assert config == config.setTimeSeg2Arbitration(5)  # Test method chaining

        config.setTimeSeg2Data(7)
        assert config.getTimeSeg2Data() == 7
        assert config == config.setTimeSeg2Data(7)  # Test method chaining

        config.setXlBitRateSwitch(True)
        assert config.getXlBitRateSwitch() is True
        assert config == config.setXlBitRateSwitch(True)  # Test method chaining

    def test_CanControllerXlConfigurationRequirements(self):
        """Test CanControllerXlConfigurationRequirements class functionality."""
        reqs = CanControllerXlConfigurationRequirements()

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
        assert reqs.getXlBitRateSwitch() is None

        # Test setter/getter methods with method chaining - with None
        assert reqs == reqs.setMaxNumberOfTimeQuantaPerBit(None)  # Test method chaining with None
        assert reqs.getMaxNumberOfTimeQuantaPerBit() is None  # Should remain None

        assert reqs == reqs.setMaxSamplePoint(None)  # Test method chaining with None
        assert reqs.getMaxSamplePoint() is None  # Should remain None

        assert reqs == reqs.setMaxSyncJumpWidth(None)  # Test method chaining with None
        assert reqs.getMaxSyncJumpWidth() is None  # Should remain None

        assert reqs == reqs.setMaxTrcvDelayCompensationOffset(None)  # Test method chaining with None
        assert reqs.getMaxTrcvDelayCompensationOffset() is None  # Should remain None

        assert reqs == reqs.setMinNumberOfTimeQuantaPerBit(None)  # Test method chaining with None
        assert reqs.getMinNumberOfTimeQuantaPerBit() is None  # Should remain None

        assert reqs == reqs.setMinSamplePoint(None)  # Test method chaining with None
        assert reqs.getMinSamplePoint() is None  # Should remain None

        assert reqs == reqs.setMinSyncJumpWidth(None)  # Test method chaining with None
        assert reqs.getMinSyncJumpWidth() is None  # Should remain None

        assert reqs == reqs.setMinTrcvDelayCompensationOffset(None)  # Test method chaining with None
        assert reqs.getMinTrcvDelayCompensationOffset() is None  # Should remain None

        assert reqs == reqs.setPaddingValue(None)  # Test method chaining with None
        assert reqs.getPaddingValue() is None  # Should remain None

        assert reqs == reqs.setXlBitRateSwitch(None)  # Test method chaining with None
        assert reqs.getXlBitRateSwitch() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        reqs.setMaxNumberOfTimeQuantaPerBit(15)
        assert reqs.getMaxNumberOfTimeQuantaPerBit() == 15
        assert reqs == reqs.setMaxNumberOfTimeQuantaPerBit(15)  # Test method chaining

        reqs.setMaxSamplePoint(0.9)
        assert reqs.getMaxSamplePoint() == 0.9
        assert reqs == reqs.setMaxSamplePoint(0.9)  # Test method chaining

        reqs.setMaxSyncJumpWidth(0.3)
        assert reqs.getMaxSyncJumpWidth() == 0.3
        assert reqs == reqs.setMaxSyncJumpWidth(0.3)  # Test method chaining

        reqs.setMaxTrcvDelayCompensationOffset(1500)
        assert reqs.getMaxTrcvDelayCompensationOffset() == 1500
        assert reqs == reqs.setMaxTrcvDelayCompensationOffset(1500)  # Test method chaining

        reqs.setMinNumberOfTimeQuantaPerBit(6)
        assert reqs.getMinNumberOfTimeQuantaPerBit() == 6
        assert reqs == reqs.setMinNumberOfTimeQuantaPerBit(6)  # Test method chaining

        reqs.setMinSamplePoint(0.3)
        assert reqs.getMinSamplePoint() == 0.3
        assert reqs == reqs.setMinSamplePoint(0.3)  # Test method chaining

        reqs.setMinSyncJumpWidth(0.05)
        assert reqs.getMinSyncJumpWidth() == 0.05
        assert reqs == reqs.setMinSyncJumpWidth(0.05)  # Test method chaining

        reqs.setMinTrcvDelayCompensationOffset(750)
        assert reqs.getMinTrcvDelayCompensationOffset() == 750
        assert reqs == reqs.setMinTrcvDelayCompensationOffset(750)  # Test method chaining

        reqs.setPaddingValue(32)
        assert reqs.getPaddingValue() == 32
        assert reqs == reqs.setPaddingValue(32)  # Test method chaining

        reqs.setXlBitRateSwitch(True)
        assert reqs.getXlBitRateSwitch() is True
        assert reqs == reqs.setXlBitRateSwitch(True)  # Test method chaining

    def test_AbstractCanCommunicationControllerAttributes(self):
        """Test AbstractCanCommunicationControllerAttributes class functionality."""
        attrs = CanControllerConfigurationRequirements()

        assert isinstance(attrs, ARObject)

        # Test default values
        assert attrs.getCanControllerFdAttributes() is None
        assert attrs.getCanControllerFdRequirements() is None
        assert attrs.getCanControllerXlAttributes() is None
        assert attrs.getCanControllerXlRequirements() is None

        # Test setter/getter methods with method chaining
        fd_attrs = CanControllerFdConfiguration()
        attrs.setCanControllerFdAttributes(fd_attrs)
        assert attrs.getCanControllerFdAttributes() == fd_attrs
        assert attrs == attrs.setCanControllerFdAttributes(fd_attrs)  # Test method chaining

        fd_reqs = CanControllerFdConfigurationRequirements()
        attrs.setCanControllerFdRequirements(fd_reqs)
        assert attrs.getCanControllerFdRequirements() == fd_reqs
        assert attrs == attrs.setCanControllerFdRequirements(fd_reqs)  # Test method chaining

        xl_attrs = CanControllerXlConfiguration()
        attrs.setCanControllerXlAttributes(xl_attrs)
        assert attrs.getCanControllerXlAttributes() == xl_attrs
        assert attrs == attrs.setCanControllerXlAttributes(xl_attrs)  # Test method chaining

        xl_reqs = CanControllerXlConfigurationRequirements()
        attrs.setCanControllerXlRequirements(xl_reqs)
        assert attrs.getCanControllerXlRequirements() == xl_reqs
        assert attrs == attrs.setCanControllerXlRequirements(xl_reqs)  # Test method chaining

    def test_CanControllerConfigurationRequirements(self):
        """Test CanControllerConfigurationRequirements class functionality."""
        reqs = CanControllerConfigurationRequirements()

        assert isinstance(reqs, AbstractCanCommunicationControllerAttributes)

        # Test default values
        assert reqs.getMaxNumberOfTimeQuantaPerBit() is None
        assert reqs.getMaxSamplePoint() is None
        assert reqs.getMaxSyncJumpWidth() is None
        assert reqs.getMinNumberOfTimeQuantaPerBit() is None
        assert reqs.getMinSamplePoint() is None
        assert reqs.getMinSyncJumpWidth() is None

        # Test setter/getter methods with method chaining
        reqs.setMaxNumberOfTimeQuantaPerBit(20)
        assert reqs.getMaxNumberOfTimeQuantaPerBit() == 20
        assert reqs == reqs.setMaxNumberOfTimeQuantaPerBit(20)  # Test method chaining

        reqs.setMaxSamplePoint(0.95)
        assert reqs.getMaxSamplePoint() == 0.95
        assert reqs == reqs.setMaxSamplePoint(0.95)  # Test method chaining

        reqs.setMaxSyncJumpWidth(0.4)
        assert reqs.getMaxSyncJumpWidth() == 0.4
        assert reqs == reqs.setMaxSyncJumpWidth(0.4)  # Test method chaining

        reqs.setMinNumberOfTimeQuantaPerBit(8)
        assert reqs.getMinNumberOfTimeQuantaPerBit() == 8
        assert reqs == reqs.setMinNumberOfTimeQuantaPerBit(8)  # Test method chaining

        reqs.setMinSamplePoint(0.2)
        assert reqs.getMinSamplePoint() == 0.2
        assert reqs == reqs.setMinSamplePoint(0.2)  # Test method chaining

        reqs.setMinSyncJumpWidth(0.02)
        assert reqs.getMinSyncJumpWidth() == 0.02
        assert reqs == reqs.setMinSyncJumpWidth(0.02)  # Test method chaining

    def test_AbstractCanCommunicationController(self):
        """Test AbstractCanCommunicationController abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
            AbstractCanCommunicationController(parent, "test_abstract_controller")

    def test_CanCommunicationController(self):
        """Test CanCommunicationController class functionality."""
        parent = MockParent()
        controller = CanCommunicationController(parent, "test_can_comm_controller")

        assert isinstance(controller, CommunicationController)

        # Test default values
        assert controller.getCanControllerAttributes() is None

        # Test setter/getter methods with method chaining
        attrs = CanControllerConfigurationRequirements()
        controller.setCanControllerAttributes(attrs)
        assert controller.getCanControllerAttributes() == attrs
        assert controller == controller.setCanControllerAttributes(attrs)  # Test method chaining

    def test_AbstractCanCommunicationConnector(self):
        """Test AbstractCanCommunicationConnector abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
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

        # Test setter/getter methods with method chaining - with None
        assert connector == connector.setPncWakeupCanId(None)  # Test method chaining with None
        assert connector.getPncWakeupCanId() is None  # Should remain None

        assert connector == connector.setPncWakeupCanIdExtended(None)  # Test method chaining with None
        assert connector.getPncWakeupCanIdExtended() is None  # Should remain None

        assert connector == connector.setPncWakeupCanIdMask(None)  # Test method chaining with None
        assert connector.getPncWakeupCanIdMask() is None  # Should remain None

        assert connector == connector.setPncWakeupDataMask(None)  # Test method chaining with None
        assert connector.getPncWakeupDataMask() is None  # Should remain None

        assert connector == connector.setPncWakeupDlc(None)  # Test method chaining with None
        assert connector.getPncWakeupDlc() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        connector.setPncWakeupCanId(123)
        assert connector.getPncWakeupCanId() == 123
        assert connector == connector.setPncWakeupCanId(123)  # Test method chaining

        connector.setPncWakeupCanIdExtended(True)
        assert connector.getPncWakeupCanIdExtended() is True
        assert connector == connector.setPncWakeupCanIdExtended(True)  # Test method chaining

        connector.setPncWakeupCanIdMask(0xFF)
        assert connector.getPncWakeupCanIdMask() == 0xFF
        assert connector == connector.setPncWakeupCanIdMask(0xFF)  # Test method chaining

        connector.setPncWakeupDataMask(0x0F)
        assert connector.getPncWakeupDataMask() == 0x0F
        assert connector == connector.setPncWakeupDataMask(0x0F)  # Test method chaining

        connector.setPncWakeupDlc(8)
        assert connector.getPncWakeupDlc() == 8
        assert connector == connector.setPncWakeupDlc(8)  # Test method chaining