import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanCommunicationConnector,
    AbstractCanCommunicationController,
    AbstractCanCommunicationControllerAttributes,
    CanCommunicationConnector,
    CanCommunicationController,
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController


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
        """Test CanControllerXlConfiguration class functionality (Table 3.18, R23-11)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger

        config = CanControllerXlConfiguration()

        assert isinstance(config, ARObject)

        # Test default values
        assert config.getErrorSignalingEnabled() is None
        assert config.getPropSeg() is None
        assert config.getPwmL() is None
        assert config.getPwmO() is None
        assert config.getPwmS() is None
        assert config.getSspOffset() is None
        assert config.getSyncJumpWidth() is None
        assert config.getTimeSeg1() is None
        assert config.getTimeSeg2() is None
        assert config.getTrcvPwmModeEnabled() is None

        # Test setter/getter methods with method chaining - with None
        assert config == config.setErrorSignalingEnabled(None)
        assert config.getErrorSignalingEnabled() is None
        assert config == config.setPropSeg(None)
        assert config.getPropSeg() is None
        assert config == config.setTrcvPwmModeEnabled(None)
        assert config.getTrcvPwmModeEnabled() is None

        # Test setter/getter methods with method chaining - with actual values
        config.setErrorSignalingEnabled(Boolean().setValue("true"))
        assert config.getErrorSignalingEnabled().getValue() is True
        assert config == config.setErrorSignalingEnabled(Boolean().setValue("true"))

        config.setPropSeg(PositiveInteger().setValue("4"))
        assert config.getPropSeg().getValue() == 4
        assert config == config.setPropSeg(PositiveInteger().setValue("4"))

        config.setPwmL(PositiveInteger().setValue("5"))
        assert config.getPwmL().getValue() == 5
        assert config == config.setPwmL(PositiveInteger().setValue("5"))

        config.setPwmO(PositiveInteger().setValue("6"))
        assert config.getPwmO().getValue() == 6
        assert config == config.setPwmO(PositiveInteger().setValue("6"))

        config.setPwmS(PositiveInteger().setValue("7"))
        assert config.getPwmS().getValue() == 7
        assert config == config.setPwmS(PositiveInteger().setValue("7"))

        config.setSspOffset(PositiveInteger().setValue("8"))
        assert config.getSspOffset().getValue() == 8
        assert config == config.setSspOffset(PositiveInteger().setValue("8"))

        config.setSyncJumpWidth(PositiveInteger().setValue("1"))
        assert config.getSyncJumpWidth().getValue() == 1
        assert config == config.setSyncJumpWidth(PositiveInteger().setValue("1"))

        config.setTimeSeg1(PositiveInteger().setValue("13"))
        assert config.getTimeSeg1().getValue() == 13
        assert config == config.setTimeSeg1(PositiveInteger().setValue("13"))

        config.setTimeSeg2(PositiveInteger().setValue("2"))
        assert config.getTimeSeg2().getValue() == 2
        assert config == config.setTimeSeg2(PositiveInteger().setValue("2"))

        config.setTrcvPwmModeEnabled(Boolean().setValue("true"))
        assert config.getTrcvPwmModeEnabled().getValue() is True
        assert config == config.setTrcvPwmModeEnabled(Boolean().setValue("true"))

    def test_CanControllerXlConfigurationRequirements(self):
        """Test CanControllerXlConfigurationRequirements class functionality (Table 3.19, R23-11)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            Boolean,
            Float,
            Integer,
            PositiveInteger,
            TimeValue,
        )

        reqs = CanControllerXlConfigurationRequirements()

        assert isinstance(reqs, ARObject)

        # Test default values
        assert reqs.getErrorSignalingEnabled() is None
        assert reqs.getMaxNumberOfTimeQuantaPerBit() is None
        assert reqs.getMaxPwmL() is None
        assert reqs.getMaxPwmO() is None
        assert reqs.getMaxPwmS() is None
        assert reqs.getMaxSamplePoint() is None
        assert reqs.getMaxSyncJumpWidth() is None
        assert reqs.getMaxTrcvDelayCompensationOffset() is None
        assert reqs.getMinNumberOfTimeQuantaPerBit() is None
        assert reqs.getMinPwmL() is None
        assert reqs.getMinPwmO() is None
        assert reqs.getMinPwmS() is None
        assert reqs.getMinSamplePoint() is None
        assert reqs.getMinSyncJumpWidth() is None
        assert reqs.getMinTrcvDelayCompensationOffset() is None
        assert reqs.getTrcvPwmModeEnabled() is None

        # Test setter/getter methods with method chaining - with None
        assert reqs == reqs.setErrorSignalingEnabled(None)
        assert reqs.getErrorSignalingEnabled() is None
        assert reqs == reqs.setMaxNumberOfTimeQuantaPerBit(None)
        assert reqs.getMaxNumberOfTimeQuantaPerBit() is None
        assert reqs == reqs.setTrcvPwmModeEnabled(None)
        assert reqs.getTrcvPwmModeEnabled() is None

        # Test setter/getter methods with method chaining - with actual values
        reqs.setErrorSignalingEnabled(Boolean().setValue("false"))
        assert reqs.getErrorSignalingEnabled().getValue() is False
        assert reqs == reqs.setErrorSignalingEnabled(Boolean().setValue("false"))

        reqs.setMaxNumberOfTimeQuantaPerBit(Integer().setValue("15"))
        assert reqs.getMaxNumberOfTimeQuantaPerBit().getValue() == 15
        assert reqs == reqs.setMaxNumberOfTimeQuantaPerBit(Integer().setValue("15"))

        reqs.setMaxPwmL(PositiveInteger().setValue("5"))
        assert reqs.getMaxPwmL().getValue() == 5
        assert reqs == reqs.setMaxPwmL(PositiveInteger().setValue("5"))

        reqs.setMaxPwmO(PositiveInteger().setValue("6"))
        assert reqs.getMaxPwmO().getValue() == 6
        assert reqs == reqs.setMaxPwmO(PositiveInteger().setValue("6"))

        reqs.setMaxPwmS(PositiveInteger().setValue("7"))
        assert reqs.getMaxPwmS().getValue() == 7
        assert reqs == reqs.setMaxPwmS(PositiveInteger().setValue("7"))

        reqs.setMaxSamplePoint(Float().setValue("0.9"))
        assert reqs.getMaxSamplePoint().getValue() == 0.9
        assert reqs == reqs.setMaxSamplePoint(Float().setValue("0.9"))

        reqs.setMaxSyncJumpWidth(Float().setValue("0.3"))
        assert reqs.getMaxSyncJumpWidth().getValue() == 0.3
        assert reqs == reqs.setMaxSyncJumpWidth(Float().setValue("0.3"))

        reqs.setMaxTrcvDelayCompensationOffset(TimeValue().setValue("1500"))
        assert reqs.getMaxTrcvDelayCompensationOffset().getValue() == 1500
        assert reqs == reqs.setMaxTrcvDelayCompensationOffset(TimeValue().setValue("1500"))

        reqs.setMinNumberOfTimeQuantaPerBit(Integer().setValue("6"))
        assert reqs.getMinNumberOfTimeQuantaPerBit().getValue() == 6
        assert reqs == reqs.setMinNumberOfTimeQuantaPerBit(Integer().setValue("6"))

        reqs.setMinPwmL(PositiveInteger().setValue("1"))
        assert reqs.getMinPwmL().getValue() == 1
        assert reqs == reqs.setMinPwmL(PositiveInteger().setValue("1"))

        reqs.setMinPwmO(PositiveInteger().setValue("2"))
        assert reqs.getMinPwmO().getValue() == 2
        assert reqs == reqs.setMinPwmO(PositiveInteger().setValue("2"))

        reqs.setMinPwmS(PositiveInteger().setValue("3"))
        assert reqs.getMinPwmS().getValue() == 3
        assert reqs == reqs.setMinPwmS(PositiveInteger().setValue("3"))

        reqs.setMinSamplePoint(Float().setValue("0.3"))
        assert reqs.getMinSamplePoint().getValue() == 0.3
        assert reqs == reqs.setMinSamplePoint(Float().setValue("0.3"))

        reqs.setMinSyncJumpWidth(Float().setValue("0.05"))
        assert reqs.getMinSyncJumpWidth().getValue() == 0.05
        assert reqs == reqs.setMinSyncJumpWidth(Float().setValue("0.05"))

        reqs.setMinTrcvDelayCompensationOffset(TimeValue().setValue("750"))
        assert reqs.getMinTrcvDelayCompensationOffset().getValue() == 750
        assert reqs == reqs.setMinTrcvDelayCompensationOffset(TimeValue().setValue("750"))

        reqs.setTrcvPwmModeEnabled(Boolean().setValue("true"))
        assert reqs.getTrcvPwmModeEnabled().getValue() is True
        assert reqs == reqs.setTrcvPwmModeEnabled(Boolean().setValue("true"))

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
        """Test AbstractCanCommunicationController abstract class instantiation (Rule 0001.2)."""
        parent = MockParent()
        with pytest.raises(TypeError):
            AbstractCanCommunicationController(parent, "test_abstract_controller")

        # Verify inherited accessors via a concrete subclass (CanCommunicationController).
        controller = CanCommunicationController(parent, "test_can_comm_controller_base")

        assert controller.getCanControllerAttributes() is None

        attrs = CanControllerConfigurationRequirements()
        assert controller == controller.setCanControllerAttributes(attrs)
        assert controller.getCanControllerAttributes() == attrs

    def test_CanCommunicationController(self):
        """Test CanCommunicationController class functionality."""
        parent = MockParent()
        controller = CanCommunicationController(parent, "test_can_comm_controller")

        assert isinstance(controller, CommunicationController)
        assert isinstance(controller, AbstractCanCommunicationController)

        # Test default values
        assert controller.getCanControllerAttributes() is None

        # Test setter/getter methods with method chaining - with None
        assert controller == controller.setCanControllerAttributes(None)  # Test method chaining with None
        assert controller.getCanControllerAttributes() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        attrs = CanControllerConfigurationRequirements()
        controller.setCanControllerAttributes(attrs)
        assert controller.getCanControllerAttributes() == attrs
        assert controller == controller.setCanControllerAttributes(attrs)  # Test method chaining

    def test_AbstractCanCommunicationConnector(self):
        """Test AbstractCanCommunicationConnector abstract class instantiation (Table 3.22)."""
        parent = MockParent()
        with pytest.raises(TypeError):
            AbstractCanCommunicationConnector(parent, "test_abstract_connector")

    def test_CanCommunicationConnector(self):
        """Test CanCommunicationConnector class functionality."""
        parent = MockParent()
        connector = CanCommunicationConnector(parent, "test_can_comm_connector")

        assert isinstance(connector, CommunicationConnector)
        assert isinstance(connector, AbstractCanCommunicationConnector)

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
