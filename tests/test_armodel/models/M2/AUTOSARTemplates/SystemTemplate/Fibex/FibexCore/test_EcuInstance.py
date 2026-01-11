import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.EcuInstance import EcuInstance
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_FibexCoreEcuInstance:
    """Test cases for FibexCore EcuInstance class."""
    
    def test_EcuInstance(self):
        """Test EcuInstance class functionality."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        assert isinstance(ecu, FibexElement)
        
        # Test default values
        assert ecu.getAssociatedComIPduGroupRefs() == []
        assert ecu.getAssociatedConsumedProvidedServiceInstanceGroupRefs() == []
        assert ecu.getAssociatedPdurIPduGroupRefs() == []
        assert ecu.getChannelSynchronousWakeup() is None
        assert ecu.getClientIdRange() is None
        assert ecu.getComConfigurationGwTimeBase() is None
        assert ecu.getComConfigurationRxTimeBase() is None
        assert ecu.getComConfigurationTxTimeBase() is None
        assert ecu.getComEnableMDTForCyclicTransmission() is None
        assert ecu.getCommControllers() == []
        assert ecu.getConnectors() == []
        assert ecu.getDiagnosticAddress() is None
        assert ecu.getDltConfig() is None
        assert ecu.getDoIpConfig() is None
        assert ecu.getEcuTaskProxyRefs() == []
        assert ecu.getEthSwitchPortGroupDerivation() is None
        assert ecu.getFirewallRuleRef() is None
        assert ecu.getPartitions() == []
        assert ecu.getPncNmRequest() is None
        assert ecu.getPncPrepareSleepTimer() is None
        assert ecu.getPncSynchronousWakeup() is None
        assert ecu.getPnResetTime() is None
        assert ecu.getSleepModeSupported() is None
        assert ecu.getTcpIpIcmpPropsRef() is None
        assert ecu.getTcpIpPropsRef() is None
        assert ecu.getV2xSupported() is None
        assert ecu.getWakeUpOverBusSupported() is None