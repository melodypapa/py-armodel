import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    FibexElement,
    PduToFrameMapping,
    Frame,
    ContainedIPduProps,
    ISignalGroup,
    ISignalIPduGroup,
    Pdu,
    IPdu,
    SecureCommunicationProps,
    SecuredIPdu,
    ISignalToIPduMapping,
    NmPdu,
    NPdu,
    DcmIPdu,
    IPduTiming,
    ISignalIPdu,
    ISignal,
    PduTriggering,
    FrameTriggering,
    SystemSignal,
    SystemSignalGroup,
    ISignalTriggering
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, ARElement, Describable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_FibexCoreCommunication:
    """Test cases for FibexCore Communication classes."""
    
    def test_FibexElement(self):
        """Test FibexElement abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            FibexElement(parent, "test_fibex_element")

    def test_PduToFrameMapping(self):
        """Test PduToFrameMapping class functionality."""
        parent = MockParent()
        mapping = PduToFrameMapping(parent, "test_pdu_to_frame_mapping")

        assert isinstance(mapping, Identifiable)
        
        # Test default values
        assert mapping.getPackingByteOrder() is None
        assert mapping.getPduRef() is None
        assert mapping.getStartPosition() is None
        assert mapping.getUpdateIndicationBitPosition() is None
        
        # Test setter/getter methods
        mapping.setPackingByteOrder("MOST_SIGNIFICANT_BYTE_FIRST")
        assert mapping.getPackingByteOrder() == "MOST_SIGNIFICANT_BYTE_FIRST"

    def test_Frame(self):
        """Test Frame abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            Frame(parent, "test_frame")

    def test_ContainedIPduProps(self):
        """Test ContainedIPduProps class functionality."""
        props = ContainedIPduProps()

        assert isinstance(props, ARObject)
        
        # Test default values
        assert props.getCollectionSemantics() is None
        assert props.getHeaderIdLongHeader() is None
        assert props.getHeaderIdShortHeader() is None
        assert props.getOffset() is None
        assert props.getTimeout() is None
        assert props.getTrigger() is None
        assert props.getUpdateIndicationBitPosition() is None

    def test_ISignalGroup(self):
        """Test ISignalGroup class functionality."""
        parent = MockParent()
        group = ISignalGroup(parent, "test_isignal_group")

        assert isinstance(group, FibexElement)
        
        # Test default values
        assert group.getComBasedSignalGroupTransformationRefs() == []
        assert group.getISignalRefs() == []
        assert group.getSystemSignalGroupRef() is None
        assert group.getTransformationISignalProps() is None

    def test_ISignalIPduGroup(self):
        """Test ISignalIPduGroup class functionality."""
        parent = MockParent()
        group = ISignalIPduGroup(parent, "test_isignal_ipdu_group")

        assert isinstance(group, FibexElement)
        
        # Test default values
        assert group.getCommunicationDirection() is None
        assert group.getCommunicationMode() is None
        assert group.getContainedISignalIPduGroupRefs() == []
        assert group.getISignalIPduRefs() == []
        assert group.getNmPduRefs() == []

    def test_Pdu(self):
        """Test Pdu abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            Pdu(parent, "test_pdu")

    def test_IPdu(self):
        """Test IPdu abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            IPdu(parent, "test_ipdu")

    def test_SecureCommunicationProps(self):
        """Test SecureCommunicationProps class functionality."""
        props = SecureCommunicationProps()

        assert isinstance(props, ARObject)
        
        # Test default values
        assert props.getAuthDataFreshnessLength() is None
        assert props.getAuthDataFreshnessStartPosition() is None
        assert props.getAuthInfoTxLength() is None
        assert props.getAuthenticationBuildAttempts() is None
        assert props.getAuthenticationRetries() is None
        assert props.getDataId() is None
        assert props.getFreshnessValueId() is None
        assert props.getFreshnessValueLength() is None
        assert props.getFreshnessValueTxLength() is None
        assert props.getMessageLinkLength() is None
        assert props.getMessageLinkPosition() is None
        assert props.getSecondaryFreshnessValueId() is None
        assert props.getSecuredAreaLength() is None
        assert props.getSecuredAreaOffset() is None

    def test_SecuredIPdu(self):
        """Test SecuredIPdu class functionality."""
        parent = MockParent()
        ipdu = SecuredIPdu(parent, "test_secured_ipdu")

        assert isinstance(ipdu, IPdu)

    def test_ISignalToIPduMapping(self):
        """Test ISignalToIPduMapping class functionality."""
        parent = MockParent()
        mapping = ISignalToIPduMapping(parent, "test_isignal_to_ipdu_mapping")

        assert isinstance(mapping, Identifiable)
        
        # Test default values
        assert mapping.getISignalRef() is None
        assert mapping.getISignalGroupRef() is None
        assert mapping.getPackingByteOrder() is None
        assert mapping.getStartPosition() is None
        assert mapping.getTransferProperty() is None
        assert mapping.getUpdateIndicationBitPosition() is None

    def test_NmPdu(self):
        """Test NmPdu class functionality."""
        parent = MockParent()
        pdu = NmPdu(parent, "test_nm_pdu")

        assert isinstance(pdu, Pdu)

    def test_NPdu(self):
        """Test NPdu class functionality."""
        parent = MockParent()
        pdu = NPdu(parent, "test_n_pdu")

        assert isinstance(pdu, IPdu)

    def test_DcmIPdu(self):
        """Test DcmIPdu class functionality."""
        parent = MockParent()
        pdu = DcmIPdu(parent, "test_dcm_ipdu")

        assert isinstance(pdu, IPdu)

    def test_IPduTiming(self):
        """Test IPduTiming class functionality."""
        timing = IPduTiming()

        assert isinstance(timing, Describable)

    def test_ISignalIPdu(self):
        """Test ISignalIPdu class functionality."""
        parent = MockParent()
        ipdu = ISignalIPdu(parent, "test_isignal_ipdu")

        assert isinstance(ipdu, IPdu)

    def test_ISignal(self):
        """Test ISignal class functionality."""
        parent = MockParent()
        signal = ISignal(parent, "test_isignal")

        assert isinstance(signal, FibexElement)

    def test_PduTriggering(self):
        """Test PduTriggering class functionality."""
        parent = MockParent()
        triggering = PduTriggering(parent, "test_pdu_triggering")

        assert isinstance(triggering, Identifiable)

    def test_FrameTriggering(self):
        """Test FrameTriggering abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            FrameTriggering(parent, "test_frame_triggering")

    def test_SystemSignal(self):
        """Test SystemSignal class functionality."""
        parent = MockParent()
        signal = SystemSignal(parent, "test_system_signal")

        assert isinstance(signal, ARElement)

    def test_SystemSignalGroup(self):
        """Test SystemSignalGroup class functionality."""
        parent = MockParent()
        group = SystemSignalGroup(parent, "test_system_signal_group")

        assert isinstance(group, ARElement)

    def test_ISignalTriggering(self):
        """Test ISignalTriggering class functionality."""
        parent = MockParent()
        triggering = ISignalTriggering(parent, "test_isignal_triggering")

        assert isinstance(triggering, Identifiable)