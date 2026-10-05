import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, PositiveUnlimitedInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanCommunicationConnector,
    AbstractCanCommunicationController,
    AbstractCanCommunicationControllerAttributes,
    AbstractCanPhysicalChannel,
    CanClusterBusOffRecovery,
    CanCommunicationConnector,
    CanCommunicationController,
    CanControllerConfiguration,
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
    CanPhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController, PhysicalChannel


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


SPEC_CLASS_NOTE = "This element contains the attributes that are used to configure the CAN bus off monitoring / recovery at system level."
BOR_COUNTER_L1_TO_L2_NOTE = "This threshold defines the count of bus-offs until the bus-off recovery switches from level 1 (short recovery time) to level 2 (long recovery time)."
BOR_TIME_L1_NOTE = "This attribute defines the duration of the bus-off recovery time in level 1 (short recovery time) in seconds."
BOR_TIME_L2_NOTE = "This attribute defines the duration of the bus-off recovery time in level 2 (long recovery time) in seconds."
BOR_TIME_TX_ENSURED_NOTE = "This attribute defines the duration of the bus-off event check in seconds."
MAIN_FUNCTION_PERIOD_NOTE = "This attribute defines the cycle time of the function Can SM_MainFunction in seconds."


class TestCanClusterBusOffRecovery:
    def test_initialization(self):
        """Test that all __init__ fields default to None"""
        recovery = CanClusterBusOffRecovery()

        assert isinstance(recovery, ARObject)
        assert recovery.getBorCounterL1ToL2() is None
        assert recovery.getBorTimeL1() is None
        assert recovery.getBorTimeL2() is None
        assert recovery.getBorTimeTxEnsured() is None
        assert recovery.getMainFunctionPeriod() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.10)"""
        assert inspect.cleandoc(CanClusterBusOffRecovery.__doc__).strip() == SPEC_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanClusterBusOffRecovery.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.10)"""
        source = inspect.getsource(CanClusterBusOffRecovery.__init__)
        assert source.index("self.borCounterL1ToL2") < source.index("self.borTimeL1")
        assert source.index("self.borTimeL1") < source.index("self.borTimeL2")
        assert source.index("self.borTimeL2") < source.index("self.borTimeTxEnsured")
        assert source.index("self.borTimeTxEnsured") < source.index("self.mainFunctionPeriod")

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_get_set_bor_counter_l1_to_l2(self):
        """Test borCounterL1ToL2 default, guarded set chaining, None no-op and typing"""
        recovery = CanClusterBusOffRecovery()

        assert recovery.getBorCounterL1ToL2() is None

        counter = PositiveInteger()
        counter.setValue("4")
        assert recovery == recovery.setBorCounterL1ToL2(counter)
        assert recovery.getBorCounterL1ToL2() == counter

        assert recovery == recovery.setBorCounterL1ToL2(None)
        assert recovery.getBorCounterL1ToL2() == counter

        getter_hints = typing.get_type_hints(CanClusterBusOffRecovery.getBorCounterL1ToL2)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanClusterBusOffRecovery.setBorCounterL1ToL2)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanClusterBusOffRecovery

    def test_bor_counter_l1_to_l2_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.10)"""
        self._assert_docstring(CanClusterBusOffRecovery.getBorCounterL1ToL2, BOR_COUNTER_L1_TO_L2_NOTE)
        self._assert_docstring(CanClusterBusOffRecovery.setBorCounterL1ToL2, BOR_COUNTER_L1_TO_L2_NOTE, "borCounterL1ToL2")

    def test_get_set_bor_time_l1(self):
        """Test borTimeL1 default, guarded set chaining, None no-op and typing"""
        recovery = CanClusterBusOffRecovery()

        assert recovery.getBorTimeL1() is None

        bor_time_l1 = TimeValue()
        bor_time_l1.setValue("0.5")
        assert recovery == recovery.setBorTimeL1(bor_time_l1)
        assert recovery.getBorTimeL1() == bor_time_l1

        assert recovery == recovery.setBorTimeL1(None)
        assert recovery.getBorTimeL1() == bor_time_l1

        getter_hints = typing.get_type_hints(CanClusterBusOffRecovery.getBorTimeL1)
        assert getter_hints.get("return") == typing.Optional[TimeValue]

        setter_hints = typing.get_type_hints(CanClusterBusOffRecovery.setBorTimeL1)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is CanClusterBusOffRecovery

    def test_bor_time_l1_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.10)"""
        self._assert_docstring(CanClusterBusOffRecovery.getBorTimeL1, BOR_TIME_L1_NOTE)
        self._assert_docstring(CanClusterBusOffRecovery.setBorTimeL1, BOR_TIME_L1_NOTE, "borTimeL1")

    def test_get_set_bor_time_l2(self):
        """Test borTimeL2 default, guarded set chaining, None no-op and typing"""
        recovery = CanClusterBusOffRecovery()

        assert recovery.getBorTimeL2() is None

        bor_time_l2 = TimeValue()
        bor_time_l2.setValue("1.5")
        assert recovery == recovery.setBorTimeL2(bor_time_l2)
        assert recovery.getBorTimeL2() == bor_time_l2

        assert recovery == recovery.setBorTimeL2(None)
        assert recovery.getBorTimeL2() == bor_time_l2

        getter_hints = typing.get_type_hints(CanClusterBusOffRecovery.getBorTimeL2)
        assert getter_hints.get("return") == typing.Optional[TimeValue]

        setter_hints = typing.get_type_hints(CanClusterBusOffRecovery.setBorTimeL2)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is CanClusterBusOffRecovery

    def test_bor_time_l2_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.10)"""
        self._assert_docstring(CanClusterBusOffRecovery.getBorTimeL2, BOR_TIME_L2_NOTE)
        self._assert_docstring(CanClusterBusOffRecovery.setBorTimeL2, BOR_TIME_L2_NOTE, "borTimeL2")

    def test_get_set_bor_time_tx_ensured(self):
        """Test borTimeTxEnsured default, guarded set chaining, None no-op and typing"""
        recovery = CanClusterBusOffRecovery()

        assert recovery.getBorTimeTxEnsured() is None

        bor_time_tx_ensured = TimeValue()
        bor_time_tx_ensured.setValue("0.2")
        assert recovery == recovery.setBorTimeTxEnsured(bor_time_tx_ensured)
        assert recovery.getBorTimeTxEnsured() == bor_time_tx_ensured

        assert recovery == recovery.setBorTimeTxEnsured(None)
        assert recovery.getBorTimeTxEnsured() == bor_time_tx_ensured

        getter_hints = typing.get_type_hints(CanClusterBusOffRecovery.getBorTimeTxEnsured)
        assert getter_hints.get("return") == typing.Optional[TimeValue]

        setter_hints = typing.get_type_hints(CanClusterBusOffRecovery.setBorTimeTxEnsured)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is CanClusterBusOffRecovery

    def test_bor_time_tx_ensured_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.10)"""
        self._assert_docstring(CanClusterBusOffRecovery.getBorTimeTxEnsured, BOR_TIME_TX_ENSURED_NOTE)
        self._assert_docstring(CanClusterBusOffRecovery.setBorTimeTxEnsured, BOR_TIME_TX_ENSURED_NOTE, "borTimeTxEnsured")

    def test_get_set_main_function_period(self):
        """Test mainFunctionPeriod default, guarded set chaining, None no-op and typing"""
        recovery = CanClusterBusOffRecovery()

        assert recovery.getMainFunctionPeriod() is None

        period = TimeValue()
        period.setValue("0.01")
        assert recovery == recovery.setMainFunctionPeriod(period)
        assert recovery.getMainFunctionPeriod() == period

        assert recovery == recovery.setMainFunctionPeriod(None)
        assert recovery.getMainFunctionPeriod() == period

        getter_hints = typing.get_type_hints(CanClusterBusOffRecovery.getMainFunctionPeriod)
        assert getter_hints.get("return") == typing.Optional[TimeValue]

        setter_hints = typing.get_type_hints(CanClusterBusOffRecovery.setMainFunctionPeriod)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is CanClusterBusOffRecovery

    def test_main_function_period_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.10)"""
        self._assert_docstring(CanClusterBusOffRecovery.getMainFunctionPeriod, MAIN_FUNCTION_PERIOD_NOTE)
        self._assert_docstring(CanClusterBusOffRecovery.setMainFunctionPeriod, MAIN_FUNCTION_PERIOD_NOTE, "mainFunctionPeriod")


CAN_COMMUNICATION_CONNECTOR_CLASS_NOTE = "CAN bus specific communication connector attributes."
PNC_WAKEUP_CAN_ID_NOTE = "CAN Identifier used to configure the CAN Transceiver for partial network wakeup."
PNC_WAKEUP_CAN_ID_EXTENDED_NOTE = "Defines whether pncWakeupCanId and pncWakeupCanIdMask shall be interpreted as extended or standard CAN ID."
PNC_WAKEUP_CAN_ID_MASK_NOTE = "Bit mask for CAN Identifier used to configure the CAN Transceiver for partial network wakeup."
PNC_WAKEUP_DATA_MASK_NOTE = "Bit mask for CAN Payload used to configure the CAN Transceiver for partial network wakeup."
PNC_WAKEUP_DLC_NOTE = "Data Length of the remote data frame used to configure the CAN Transceiver for partial network wakeup in Bytes."


class TestCanCommunicationConnector:
    def _make(self) -> CanCommunicationConnector:
        return CanCommunicationConnector(MockParent(), "test_can_comm_connector")

    def test_initialization(self):
        """Test that all __init__ fields default to None and the base shape follows Table 3.23"""
        connector = self._make()

        assert isinstance(connector, AbstractCanCommunicationConnector)
        assert isinstance(connector, CommunicationConnector)
        assert connector.getPncWakeupCanId() is None
        assert connector.getPncWakeupCanIdExtended() is None
        assert connector.getPncWakeupCanIdMask() is None
        assert connector.getPncWakeupDataMask() is None
        assert connector.getPncWakeupDlc() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.23)"""
        assert inspect.cleandoc(CanCommunicationConnector.__doc__).strip() == CAN_COMMUNICATION_CONNECTOR_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanCommunicationConnector.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.23)"""
        source = inspect.getsource(CanCommunicationConnector.__init__)
        assert source.index("self.pncWakeupCanId:") < source.index("self.pncWakeupCanIdExtended:")
        assert source.index("self.pncWakeupCanIdExtended:") < source.index("self.pncWakeupCanIdMask:")
        assert source.index("self.pncWakeupCanIdMask:") < source.index("self.pncWakeupDataMask:")
        assert source.index("self.pncWakeupDataMask:") < source.index("self.pncWakeupDlc:")

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_get_set_pnc_wakeup_can_id(self):
        """Test pncWakeupCanId default, guarded set chaining, None no-op and typing"""
        connector = self._make()

        assert connector.getPncWakeupCanId() is None

        can_id = PositiveInteger()
        can_id.setValue("401")
        assert connector == connector.setPncWakeupCanId(can_id)
        assert connector.getPncWakeupCanId() == can_id

        assert connector == connector.setPncWakeupCanId(None)
        assert connector.getPncWakeupCanId() == can_id

        getter_hints = typing.get_type_hints(CanCommunicationConnector.getPncWakeupCanId)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanCommunicationConnector.setPncWakeupCanId)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanCommunicationConnector

    def test_pnc_wakeup_can_id_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.23)"""
        self._assert_docstring(CanCommunicationConnector.getPncWakeupCanId, PNC_WAKEUP_CAN_ID_NOTE)
        self._assert_docstring(CanCommunicationConnector.setPncWakeupCanId, PNC_WAKEUP_CAN_ID_NOTE, "pncWakeupCanId")

    def test_get_set_pnc_wakeup_can_id_extended(self):
        """Test pncWakeupCanIdExtended default, guarded set chaining, None no-op and typing"""
        connector = self._make()

        assert connector.getPncWakeupCanIdExtended() is None

        extended = Boolean()
        extended.setValue(True)
        assert connector == connector.setPncWakeupCanIdExtended(extended)
        assert connector.getPncWakeupCanIdExtended() == extended

        assert connector == connector.setPncWakeupCanIdExtended(None)
        assert connector.getPncWakeupCanIdExtended() == extended

        getter_hints = typing.get_type_hints(CanCommunicationConnector.getPncWakeupCanIdExtended)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(CanCommunicationConnector.setPncWakeupCanIdExtended)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is CanCommunicationConnector

    def test_pnc_wakeup_can_id_extended_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.23)"""
        self._assert_docstring(CanCommunicationConnector.getPncWakeupCanIdExtended, PNC_WAKEUP_CAN_ID_EXTENDED_NOTE)
        self._assert_docstring(CanCommunicationConnector.setPncWakeupCanIdExtended, PNC_WAKEUP_CAN_ID_EXTENDED_NOTE, "pncWakeupCanIdExtended")

    def test_get_set_pnc_wakeup_can_id_mask(self):
        """Test pncWakeupCanIdMask default, guarded set chaining, None no-op and typing"""
        connector = self._make()

        assert connector.getPncWakeupCanIdMask() is None

        mask = PositiveInteger()
        mask.setValue("255")
        assert connector == connector.setPncWakeupCanIdMask(mask)
        assert connector.getPncWakeupCanIdMask() == mask

        assert connector == connector.setPncWakeupCanIdMask(None)
        assert connector.getPncWakeupCanIdMask() == mask

        getter_hints = typing.get_type_hints(CanCommunicationConnector.getPncWakeupCanIdMask)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanCommunicationConnector.setPncWakeupCanIdMask)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanCommunicationConnector

    def test_pnc_wakeup_can_id_mask_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.23)"""
        self._assert_docstring(CanCommunicationConnector.getPncWakeupCanIdMask, PNC_WAKEUP_CAN_ID_MASK_NOTE)
        self._assert_docstring(CanCommunicationConnector.setPncWakeupCanIdMask, PNC_WAKEUP_CAN_ID_MASK_NOTE, "pncWakeupCanIdMask")

    def test_get_set_pnc_wakeup_data_mask(self):
        """Test pncWakeupDataMask default, guarded set chaining, None no-op and typing"""
        connector = self._make()

        assert connector.getPncWakeupDataMask() is None

        data_mask = PositiveUnlimitedInteger()
        data_mask.setValue("255")
        assert connector == connector.setPncWakeupDataMask(data_mask)
        assert connector.getPncWakeupDataMask() == data_mask

        assert connector == connector.setPncWakeupDataMask(None)
        assert connector.getPncWakeupDataMask() == data_mask

        getter_hints = typing.get_type_hints(CanCommunicationConnector.getPncWakeupDataMask)
        assert getter_hints.get("return") == typing.Optional[PositiveUnlimitedInteger]

        setter_hints = typing.get_type_hints(CanCommunicationConnector.setPncWakeupDataMask)
        assert setter_hints.get("value") == typing.Optional[PositiveUnlimitedInteger]
        assert setter_hints.get("return") is CanCommunicationConnector

    def test_pnc_wakeup_data_mask_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.23)"""
        self._assert_docstring(CanCommunicationConnector.getPncWakeupDataMask, PNC_WAKEUP_DATA_MASK_NOTE)
        self._assert_docstring(CanCommunicationConnector.setPncWakeupDataMask, PNC_WAKEUP_DATA_MASK_NOTE, "pncWakeupDataMask")

    def test_get_set_pnc_wakeup_dlc(self):
        """Test pncWakeupDlc default, guarded set chaining, None no-op and typing"""
        connector = self._make()

        assert connector.getPncWakeupDlc() is None

        dlc = PositiveInteger()
        dlc.setValue("8")
        assert connector == connector.setPncWakeupDlc(dlc)
        assert connector.getPncWakeupDlc() == dlc

        assert connector == connector.setPncWakeupDlc(None)
        assert connector.getPncWakeupDlc() == dlc

        getter_hints = typing.get_type_hints(CanCommunicationConnector.getPncWakeupDlc)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CanCommunicationConnector.setPncWakeupDlc)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CanCommunicationConnector

    def test_pnc_wakeup_dlc_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.23)"""
        self._assert_docstring(CanCommunicationConnector.getPncWakeupDlc, PNC_WAKEUP_DLC_NOTE)
        self._assert_docstring(CanCommunicationConnector.setPncWakeupDlc, PNC_WAKEUP_DLC_NOTE, "pncWakeupDlc")


CAN_CONTROLLER_CONFIGURATION_CLASS_NOTE = "This element is used for the specification of the exact CAN Bit Timing configuration parameter values."
PROP_SEG_NOTE = "Specifies propagation delay in time quantas."
SYNC_JUMP_WIDTH_NOTE = "The number of quanta in the Synchronization Jump Width, SJW. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors."
TIME_SEG_1_NOTE = "Specifies phase segment 1 in time quantas. timeSeg1 = Phase_Seg1"
TIME_SEG_2_NOTE = "Specifies phase segment 2 in time quantas. timeSeg2 = Phase_Seg2"


class TestCanControllerConfiguration:
    def test_initialization(self):
        """Test that all __init__ fields default to None, incl. inherited base fields"""
        config = CanControllerConfiguration()

        assert isinstance(config, ARObject)
        assert isinstance(config, AbstractCanCommunicationControllerAttributes)
        assert config.getPropSeg() is None
        assert config.getSyncJumpWidth() is None
        assert config.getTimeSeg1() is None
        assert config.getTimeSeg2() is None
        assert config.getCanControllerFdAttributes() is None
        assert config.getCanControllerFdRequirements() is None
        assert config.getCanControllerXlAttributes() is None
        assert config.getCanControllerXlRequirements() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.14)"""
        assert inspect.cleandoc(CanControllerConfiguration.__doc__).strip() == CAN_CONTROLLER_CONFIGURATION_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanControllerConfiguration.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.14)"""
        source = inspect.getsource(CanControllerConfiguration.__init__)
        assert source.index("self.propSeg") < source.index("self.syncJumpWidth")
        assert source.index("self.syncJumpWidth") < source.index("self.timeSeg1")
        assert source.index("self.timeSeg1") < source.index("self.timeSeg2")

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_get_set_prop_seg(self):
        """Test propSeg default, guarded set chaining, None no-op and typing"""
        config = CanControllerConfiguration()

        assert config.getPropSeg() is None

        prop_seg = Integer()
        prop_seg.setValue("8")
        assert config == config.setPropSeg(prop_seg)
        assert config.getPropSeg() == prop_seg

        assert config == config.setPropSeg(None)
        assert config.getPropSeg() == prop_seg

        getter_hints = typing.get_type_hints(CanControllerConfiguration.getPropSeg)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(CanControllerConfiguration.setPropSeg)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is CanControllerConfiguration

    def test_prop_seg_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.14)"""
        self._assert_docstring(CanControllerConfiguration.getPropSeg, PROP_SEG_NOTE)
        self._assert_docstring(CanControllerConfiguration.setPropSeg, PROP_SEG_NOTE, "propSeg")

    def test_get_set_sync_jump_width(self):
        """Test syncJumpWidth default, guarded set chaining, None no-op and typing"""
        config = CanControllerConfiguration()

        assert config.getSyncJumpWidth() is None

        sjw = Integer()
        sjw.setValue("2")
        assert config == config.setSyncJumpWidth(sjw)
        assert config.getSyncJumpWidth() == sjw

        assert config == config.setSyncJumpWidth(None)
        assert config.getSyncJumpWidth() == sjw

        getter_hints = typing.get_type_hints(CanControllerConfiguration.getSyncJumpWidth)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(CanControllerConfiguration.setSyncJumpWidth)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is CanControllerConfiguration

    def test_sync_jump_width_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.14)"""
        self._assert_docstring(CanControllerConfiguration.getSyncJumpWidth, SYNC_JUMP_WIDTH_NOTE)
        self._assert_docstring(CanControllerConfiguration.setSyncJumpWidth, SYNC_JUMP_WIDTH_NOTE, "syncJumpWidth")

    def test_get_set_time_seg1(self):
        """Test timeSeg1 default, guarded set chaining, None no-op and typing"""
        config = CanControllerConfiguration()

        assert config.getTimeSeg1() is None

        time_seg1 = Integer()
        time_seg1.setValue("13")
        assert config == config.setTimeSeg1(time_seg1)
        assert config.getTimeSeg1() == time_seg1

        assert config == config.setTimeSeg1(None)
        assert config.getTimeSeg1() == time_seg1

        getter_hints = typing.get_type_hints(CanControllerConfiguration.getTimeSeg1)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(CanControllerConfiguration.setTimeSeg1)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is CanControllerConfiguration

    def test_time_seg1_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.14)"""
        self._assert_docstring(CanControllerConfiguration.getTimeSeg1, TIME_SEG_1_NOTE)
        self._assert_docstring(CanControllerConfiguration.setTimeSeg1, TIME_SEG_1_NOTE, "timeSeg1")

    def test_get_set_time_seg2(self):
        """Test timeSeg2 default, guarded set chaining, None no-op and typing"""
        config = CanControllerConfiguration()

        assert config.getTimeSeg2() is None

        time_seg2 = Integer()
        time_seg2.setValue("2")
        assert config == config.setTimeSeg2(time_seg2)
        assert config.getTimeSeg2() == time_seg2

        assert config == config.setTimeSeg2(None)
        assert config.getTimeSeg2() == time_seg2

        getter_hints = typing.get_type_hints(CanControllerConfiguration.getTimeSeg2)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(CanControllerConfiguration.setTimeSeg2)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is CanControllerConfiguration

    def test_time_seg2_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.14)"""
        self._assert_docstring(CanControllerConfiguration.getTimeSeg2, TIME_SEG_2_NOTE)
        self._assert_docstring(CanControllerConfiguration.setTimeSeg2, TIME_SEG_2_NOTE, "timeSeg2")


ABSTRACT_CAN_COMMUNICATION_CONTROLLER_CLASS_NOTE = "Abstract class that is used to collect the common TtCAN and CAN Controller attributes."
CAN_CONTROLLER_ATTRIBUTES_NOTE = "CAN Bit Timing configuration"


class ConcreteAbstractCanCommunicationController(AbstractCanCommunicationController):
    pass


class TestAbstractCanCommunicationController:
    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 3.12: ARObject, CommunicationController, Identifiable, MultilanguageReferrable, Referrable)"""
        assert issubclass(AbstractCanCommunicationController, CommunicationController)
        assert issubclass(AbstractCanCommunicationController, Identifiable)
        assert issubclass(AbstractCanCommunicationController, ARObject)

    def test_abstract_guard(self):
        """Test the class cannot be instantiated directly (abstract per Table 3.12)"""
        with pytest.raises(TypeError, match="AbstractCanCommunicationController is an abstract class"):
            AbstractCanCommunicationController(MockParent(), "test_abstract_controller")

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.12)"""
        assert inspect.cleandoc(AbstractCanCommunicationController.__doc__).strip() == ABSTRACT_CAN_COMMUNICATION_CONTROLLER_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert AbstractCanCommunicationController.__init__.__doc__ is None

    def test_initialization_defaults(self):
        """Test that all __init__ fields default to None, incl. inherited base fields"""
        controller = ConcreteAbstractCanCommunicationController(MockParent(), "ctrl")

        assert isinstance(controller, AbstractCanCommunicationController)
        assert isinstance(controller, CommunicationController)
        assert controller.getCanControllerAttributes() is None
        assert controller.getWakeUpByControllerSupported() is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.12)"""
        source = inspect.getsource(AbstractCanCommunicationController.__init__)
        assert source.index("self.canControllerAttributes") >= 0

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_get_set_can_controller_attributes(self):
        """Test canControllerAttributes default, guarded set chaining, None no-op and typing"""
        controller = ConcreteAbstractCanCommunicationController(MockParent(), "ctrl")

        assert controller.getCanControllerAttributes() is None

        attrs = CanControllerConfiguration()
        assert controller == controller.setCanControllerAttributes(attrs)
        assert controller.getCanControllerAttributes() is attrs

        assert controller == controller.setCanControllerAttributes(None)
        assert controller.getCanControllerAttributes() is attrs

        getter_hints = typing.get_type_hints(AbstractCanCommunicationController.getCanControllerAttributes)
        assert getter_hints.get("return") == typing.Optional[AbstractCanCommunicationControllerAttributes]

        setter_hints = typing.get_type_hints(AbstractCanCommunicationController.setCanControllerAttributes)
        assert setter_hints.get("value") == typing.Optional[AbstractCanCommunicationControllerAttributes]
        assert setter_hints.get("return") is AbstractCanCommunicationController

    def test_can_controller_attributes_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.12)"""
        self._assert_docstring(AbstractCanCommunicationController.getCanControllerAttributes, CAN_CONTROLLER_ATTRIBUTES_NOTE)
        self._assert_docstring(AbstractCanCommunicationController.setCanControllerAttributes, CAN_CONTROLLER_ATTRIBUTES_NOTE, "canControllerAttributes")


CAN_COMMUNICATION_CONTROLLER_CLASS_NOTE = "CAN bus specific communication port attributes."


class TestCanCommunicationController:
    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 3.11: ARObject, AbstractCanCommunicationController, CommunicationController, Identifiable, MultilanguageReferrable, Referrable)"""
        assert issubclass(CanCommunicationController, AbstractCanCommunicationController)
        assert issubclass(CanCommunicationController, CommunicationController)
        assert issubclass(CanCommunicationController, Identifiable)
        assert issubclass(CanCommunicationController, ARObject)

    def test_initialization_defaults(self):
        """Test that the concrete class instantiates and all inherited fields default to None (Table 3.11 has no own attribute rows)"""
        controller = CanCommunicationController(MockParent(), "ctrl")

        assert isinstance(controller, CanCommunicationController)
        assert isinstance(controller, AbstractCanCommunicationController)
        assert controller.getCanControllerAttributes() is None
        assert controller.getWakeUpByControllerSupported() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.11)"""
        assert inspect.cleandoc(CanCommunicationController.__doc__).strip() == CAN_COMMUNICATION_CONTROLLER_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanCommunicationController.__init__.__doc__ is None

    def test_no_own_members(self):
        """Test that the class declares no own fields or accessors (Table 3.11 has no attribute rows)"""
        own_methods = [name for name in CanCommunicationController.__dict__ if inspect.isfunction(getattr(CanCommunicationController, name, None))]
        assert own_methods == ["__init__"]

        source = inspect.getsource(CanCommunicationController.__init__)
        assert "self." not in source


ABSTRACT_CAN_PHYSICAL_CHANNEL_CLASS_NOTE = "Abstract class that is used to collect the common TtCAN and CAN PhysicalChannel attributes."


class TestAbstractCanPhysicalChannel:
    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 3.20: ARObject, Identifiable, MultilanguageReferrable, PhysicalChannel, Referrable)"""
        assert issubclass(AbstractCanPhysicalChannel, PhysicalChannel)
        assert issubclass(AbstractCanPhysicalChannel, Identifiable)
        assert issubclass(AbstractCanPhysicalChannel, ARObject)

    def test_abstract_guard(self):
        """Test the class cannot be instantiated directly (abstract per Table 3.20)"""
        with pytest.raises(TypeError, match="AbstractCanPhysicalChannel is an abstract class"):
            AbstractCanPhysicalChannel(MockParent(), "test_abstract_can_physical_channel")

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.20)"""
        assert inspect.cleandoc(AbstractCanPhysicalChannel.__doc__).strip() == ABSTRACT_CAN_PHYSICAL_CHANNEL_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert AbstractCanPhysicalChannel.__init__.__doc__ is None

    def test_no_own_members(self):
        """Test that the class declares no own fields or accessors (Table 3.20 has no attribute rows)"""
        own_methods = [name for name in AbstractCanPhysicalChannel.__dict__ if inspect.isfunction(getattr(AbstractCanPhysicalChannel, name, None))]
        assert own_methods == ["__init__"]

        source = inspect.getsource(AbstractCanPhysicalChannel.__init__)
        assert "self." not in source

    def test_initialization_defaults_via_concrete_subclass(self):
        """Test __init__ + the inherited PhysicalChannel accessors through the concrete subclass CanPhysicalChannel (Table 3.20 is abstract)"""
        channel = CanPhysicalChannel(MockParent(), "ch")

        assert isinstance(channel, AbstractCanPhysicalChannel)
        assert isinstance(channel, PhysicalChannel)
        assert channel.getCommConnectorRefs() == []
        assert channel.getFrameTriggerings() == []
        assert channel.getISignalTriggerings() == []
        assert channel.getManagedPhysicalChannelRefs() == []
        assert channel.getPduTriggerings() == []
