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
    ISignalTriggering,
    SegmentPosition,
    MultiplexedPart,
    StaticPart,
    DynamicPartAlternative,
    DynamicPart,
    MultiplexedIPdu,
    GeneralPurposePdu,
    GeneralPurposeIPdu,
    SecureCommunicationPropsSet,
    UserDefinedPdu,
    UserDefinedIPdu,
    SecureCommunicationAuthenticationProps,
    SecureCommunicationFreshnessProps
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
        assert mapping == mapping.setPackingByteOrder("MOST_SIGNIFICANT_BYTE_FIRST")  # Test method chaining

        ref = object()
        mapping.setPduRef(ref)
        assert mapping.getPduRef() == ref
        assert mapping == mapping.setPduRef(ref)  # Test method chaining

        mapping.setStartPosition(10)
        assert mapping.getStartPosition() == 10
        assert mapping == mapping.setStartPosition(10)  # Test method chaining

        mapping.setUpdateIndicationBitPosition(5)
        assert mapping.getUpdateIndicationBitPosition() == 5
        assert mapping == mapping.setUpdateIndicationBitPosition(5)  # Test method chaining

    def test_Frame(self):
        """Test Frame abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            Frame(parent, "test_frame")

    def test_Frame_methods(self):
        """Test Frame abstract class methods."""
        class ConcreteFrame(Frame):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = MockParent()
        frame = ConcreteFrame(parent, "test_frame")

        # Test default values
        assert frame.getFrameLength() is None
        assert frame.getPduToFrameMappings() == []

        # Test setter/getter methods with method chaining
        frame.setFrameLength(100)
        assert frame.getFrameLength() == 100
        assert frame == frame.setFrameLength(100)  # Test method chaining

        # Test PduToFrameMapping creation methods
        mapping = frame.createPduToFrameMapping("test_mapping")
        assert isinstance(mapping, PduToFrameMapping)
        assert len(frame.getPduToFrameMappings()) == 1

        # Try creating the same mapping again (should return existing)
        mapping2 = frame.createPduToFrameMapping("test_mapping")
        assert mapping == mapping2  # Should return the same instance

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

        # Test setter/getter methods with method chaining
        props.setCollectionSemantics("TRIGGER_ON_SEND")
        assert props.getCollectionSemantics() == "TRIGGER_ON_SEND"
        assert props == props.setCollectionSemantics("TRIGGER_ON_SEND")  # Test method chaining

        props.setHeaderIdLongHeader(100)
        assert props.getHeaderIdLongHeader() == 100
        assert props == props.setHeaderIdLongHeader(100)  # Test method chaining

        props.setHeaderIdShortHeader(200)
        assert props.getHeaderIdShortHeader() == 200
        assert props == props.setHeaderIdShortHeader(200)  # Test method chaining

        props.setOffset(50)
        assert props.getOffset() == 50
        assert props == props.setOffset(50)  # Test method chaining

        props.setTimeout(1000)
        assert props.getTimeout() == 1000
        assert props == props.setTimeout(1000)  # Test method chaining

        props.setTrigger("TRIGGER_IMMEDIATE")
        assert props.getTrigger() == "TRIGGER_IMMEDIATE"
        assert props == props.setTrigger("TRIGGER_IMMEDIATE")  # Test method chaining

        props.setUpdateIndicationBitPosition(25)
        assert props.getUpdateIndicationBitPosition() == 25
        assert props == props.setUpdateIndicationBitPosition(25)  # Test method chaining

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

        # Test setter/getter methods with method chaining
        ref1 = object()
        group.addComBasedSignalGroupTransformationRef(ref1)
        assert ref1 in group.getComBasedSignalGroupTransformationRefs()
        assert group == group.addComBasedSignalGroupTransformationRef(ref1)  # Test method chaining

        ref2 = object()
        group.addISignalRef(ref2)
        assert ref2 in group.getISignalRefs()
        assert group == group.addISignalRef(ref2)  # Test method chaining

        ref3 = object()
        group.setSystemSignalGroupRef(ref3)
        assert group.getSystemSignalGroupRef() == ref3
        assert group == group.setSystemSignalGroupRef(ref3)  # Test method chaining

        ref4 = object()
        group.setTransformationISignalProps(ref4)
        assert group.getTransformationISignalProps() == ref4
        assert group == group.setTransformationISignalProps(ref4)  # Test method chaining

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

        # Test setter/getter methods with method chaining
        group.setCommunicationDirection("IN")
        assert group.getCommunicationDirection() == "IN"
        assert group == group.setCommunicationDirection("IN")  # Test method chaining

        group.setCommunicationMode("TRIGGERED")
        assert group.getCommunicationMode() == "TRIGGERED"
        assert group == group.setCommunicationMode("TRIGGERED")  # Test method chaining

        ref1 = object()
        group.addContainedISignalIPduGroupRef(ref1)
        assert ref1 in group.getContainedISignalIPduGroupRefs()
        assert group == group.addContainedISignalIPduGroupRef(ref1)  # Test method chaining

        ref2 = object()
        group.addISignalIPduRef(ref2)
        assert ref2 in group.getISignalIPduRefs()
        assert group == group.addISignalIPduRef(ref2)  # Test method chaining

        ref3 = object()
        group.addNmPduRef(ref3)
        assert ref3 in group.getNmPduRefs()
        assert group == group.addNmPduRef(ref3)  # Test method chaining

    def test_Pdu(self):
        """Test Pdu abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            Pdu(parent, "test_pdu")

    def test_Pdu_methods(self):
        """Test Pdu class methods."""
        class ConcretePdu(Pdu):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = MockParent()
        pdu = ConcretePdu(parent, "test_pdu")

        # Test default values
        assert pdu.getHasDynamicLength() is None
        assert pdu.getLength() is None

        # Test setter/getter methods with method chaining - with None value
        assert pdu == pdu.setHasDynamicLength(None)  # Test method chaining with None
        assert pdu.getHasDynamicLength() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual value
        pdu.setHasDynamicLength(True)
        assert pdu.getHasDynamicLength() is True
        assert pdu == pdu.setHasDynamicLength(True)  # Test method chaining

        pdu.setLength(100)
        assert pdu.getLength() == 100
        assert pdu == pdu.setLength(100)  # Test method chaining

    def test_IPdu(self):
        """Test IPdu abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            IPdu(parent, "test_ipdu")

    def test_IPdu_methods(self):
        """Test IPdu class methods."""
        class ConcreteIPdu(IPdu):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = MockParent()
        ipdu = ConcreteIPdu(parent, "test_ipdu")

        # Test default values
        assert ipdu.getContainedIPduProps() is None

        # Test setter/getter methods with method chaining - with None value
        assert ipdu == ipdu.setContainedIPduProps(None)  # Test method chaining with None
        assert ipdu.getContainedIPduProps() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual value
        props = ContainedIPduProps()
        ipdu.setContainedIPduProps(props)
        assert ipdu.getContainedIPduProps() == props
        assert ipdu == ipdu.setContainedIPduProps(props)  # Test method chaining

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

        # Test setter/getter methods with method chaining
        props.setAuthDataFreshnessLength(10)
        assert props.getAuthDataFreshnessLength() == 10
        assert props == props.setAuthDataFreshnessLength(10)  # Test method chaining

        props.setAuthDataFreshnessStartPosition(20)
        assert props.getAuthDataFreshnessStartPosition() == 20
        assert props == props.setAuthDataFreshnessStartPosition(20)  # Test method chaining

        props.setAuthInfoTxLength(30)
        assert props.getAuthInfoTxLength() == 30
        assert props == props.setAuthInfoTxLength(30)  # Test method chaining

        props.setAuthenticationBuildAttempts(5)
        assert props.getAuthenticationBuildAttempts() == 5
        assert props == props.setAuthenticationBuildAttempts(5)  # Test method chaining

        props.setAuthenticationRetries(3)
        assert props.getAuthenticationRetries() == 3
        assert props == props.setAuthenticationRetries(3)  # Test method chaining

        props.setDataId(42)
        assert props.getDataId() == 42
        assert props == props.setDataId(42)  # Test method chaining

        props.setFreshnessValueId(100)
        assert props.getFreshnessValueId() == 100
        assert props == props.setFreshnessValueId(100)  # Test method chaining

        props.setFreshnessValueLength(50)
        assert props.getFreshnessValueLength() == 50
        assert props == props.setFreshnessValueLength(50)  # Test method chaining

        props.setFreshnessValueTxLength(60)
        assert props.getFreshnessValueTxLength() == 60
        assert props == props.setFreshnessValueTxLength(60)  # Test method chaining

        props.setMessageLinkLength(70)
        assert props.getMessageLinkLength() == 70
        assert props == props.setMessageLinkLength(70)  # Test method chaining

        props.setMessageLinkPosition(80)
        assert props.getMessageLinkPosition() == 80
        assert props == props.setMessageLinkPosition(80)  # Test method chaining

        props.setSecondaryFreshnessValueId(200)
        assert props.getSecondaryFreshnessValueId() == 200
        assert props == props.setSecondaryFreshnessValueId(200)  # Test method chaining

        props.setSecuredAreaLength(90)
        assert props.getSecuredAreaLength() == 90
        assert props == props.setSecuredAreaLength(90)  # Test method chaining

        props.setSecuredAreaOffset(100)
        assert props.getSecuredAreaOffset() == 100
        assert props == props.setSecuredAreaOffset(100)  # Test method chaining

    def test_SecuredIPdu(self):
        """Test SecuredIPdu class functionality."""
        parent = MockParent()
        ipdu = SecuredIPdu(parent, "test_secured_ipdu")

        assert isinstance(ipdu, IPdu)

        # Test default values
        assert ipdu.getAuthenticationPropsRef() is None
        assert ipdu.getDynamicRuntimeLengthHandling() is None
        assert ipdu.getFreshnessPropsRef() is None
        assert ipdu.getPayloadRef() is None
        assert ipdu.getSecureCommunicationProps() is None
        assert ipdu.getUseAsCryptographicIPdu() is None
        assert ipdu.getUseSecuredPduHeader() is None

        # Test setter/getter methods with method chaining
        ref1 = object()
        ipdu.setAuthenticationPropsRef(ref1)
        assert ipdu.getAuthenticationPropsRef() == ref1
        assert ipdu == ipdu.setAuthenticationPropsRef(ref1)  # Test method chaining

        ipdu.setDynamicRuntimeLengthHandling(True)
        assert ipdu.getDynamicRuntimeLengthHandling() is True
        assert ipdu == ipdu.setDynamicRuntimeLengthHandling(True)  # Test method chaining

        ref2 = object()
        ipdu.setFreshnessPropsRef(ref2)
        assert ipdu.getFreshnessPropsRef() == ref2
        assert ipdu == ipdu.setFreshnessPropsRef(ref2)  # Test method chaining

        ref3 = object()
        ipdu.setPayloadRef(ref3)
        assert ipdu.getPayloadRef() == ref3
        assert ipdu == ipdu.setPayloadRef(ref3)  # Test method chaining

        props = SecureCommunicationProps()
        ipdu.setSecureCommunicationProps(props)
        assert ipdu.getSecureCommunicationProps() == props
        assert ipdu == ipdu.setSecureCommunicationProps(props)  # Test method chaining

        ipdu.setUseAsCryptographicIPdu(False)
        assert ipdu.getUseAsCryptographicIPdu() is False
        assert ipdu == ipdu.setUseAsCryptographicIPdu(False)  # Test method chaining

        ipdu.setUseSecuredPduHeader("SECURED_HEADER")
        assert ipdu.getUseSecuredPduHeader() == "SECURED_HEADER"
        assert ipdu == ipdu.setUseSecuredPduHeader("SECURED_HEADER")  # Test method chaining

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

        # Test setter/getter methods with method chaining
        ref1 = object()
        mapping.setISignalRef(ref1)
        assert mapping.getISignalRef() == ref1
        assert mapping == mapping.setISignalRef(ref1)  # Test method chaining

        ref2 = object()
        mapping.setISignalGroupRef(ref2)
        assert mapping.getISignalGroupRef() == ref2
        assert mapping == mapping.setISignalGroupRef(ref2)  # Test method chaining

        mapping.setPackingByteOrder("MOST_SIGNIFICANT_BYTE_FIRST")
        assert mapping.getPackingByteOrder() == "MOST_SIGNIFICANT_BYTE_FIRST"
        assert mapping == mapping.setPackingByteOrder("MOST_SIGNIFICANT_BYTE_FIRST")  # Test method chaining

        mapping.setStartPosition(100)
        assert mapping.getStartPosition() == 100
        assert mapping == mapping.setStartPosition(100)  # Test method chaining

        mapping.setTransferProperty("PENDING")
        assert mapping.getTransferProperty() == "PENDING"
        assert mapping == mapping.setTransferProperty("PENDING")  # Test method chaining

        mapping.setUpdateIndicationBitPosition(50)
        assert mapping.getUpdateIndicationBitPosition() == 50
        assert mapping == mapping.setUpdateIndicationBitPosition(50)  # Test method chaining

    def test_NmPdu(self):
        """Test NmPdu class functionality."""
        parent = MockParent()
        pdu = NmPdu(parent, "test_nm_pdu")

        assert isinstance(pdu, Pdu)

        # Test default values
        assert pdu.getISignalToIPduMappings() == []
        assert pdu.getNmDataInformation() is None
        assert pdu.getNmVoteInformation() is None
        assert pdu.getUnusedBitPattern() is None

        # Test setter/getter methods with method chaining
        ref1 = object()
        pdu.setNmDataInformation(True)
        assert pdu.getNmDataInformation() is True
        assert pdu == pdu.setNmDataInformation(True)  # Test method chaining

        pdu.setNmVoteInformation(False)
        assert pdu.getNmVoteInformation() is False
        assert pdu == pdu.setNmVoteInformation(False)  # Test method chaining

        pdu.setUnusedBitPattern(-1)
        assert pdu.getUnusedBitPattern() == -1
        assert pdu == pdu.setUnusedBitPattern(-1)  # Test method chaining

        # Test ISignalToIPduMapping creation method
        mapping = pdu.createISignalToIPduMapping("test_mapping")
        assert isinstance(mapping, ISignalToIPduMapping)
        assert len(pdu.getISignalToIPduMappings()) == 1

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

        # Test default values
        assert pdu.getDiagPduType() is None

        # Test setter/getter methods with method chaining
        pdu.setDiagPduType("REQUEST")
        assert pdu.getDiagPduType() == "REQUEST"
        assert pdu == pdu.setDiagPduType("REQUEST")  # Test method chaining

    def test_IPduTiming(self):
        """Test IPduTiming class functionality."""
        timing = IPduTiming()

        assert isinstance(timing, Describable)

        # Test default values
        assert timing.getMinimumDelay() is None
        assert timing.getTransmissionModeDeclaration() is None

        # Test setter/getter methods with method chaining
        ref1 = object()
        timing.setMinimumDelay(ref1)
        assert timing.getMinimumDelay() == ref1
        assert timing == timing.setMinimumDelay(ref1)  # Test method chaining

        ref2 = object()
        timing.setTransmissionModeDeclaration(ref2)
        assert timing.getTransmissionModeDeclaration() == ref2
        assert timing == timing.setTransmissionModeDeclaration(ref2)  # Test method chaining

    def test_ISignalIPdu(self):
        """Test ISignalIPdu class functionality."""
        parent = MockParent()
        ipdu = ISignalIPdu(parent, "test_isignal_ipdu")

        assert isinstance(ipdu, IPdu)

        # Test default values
        assert ipdu.getIPduTimingSpecification() is None
        assert ipdu.getISignalToPduMappings() == []
        assert ipdu.getUnusedBitPattern() is None

        # Test setter/getter methods with method chaining
        timing = IPduTiming()
        ipdu.setIPduTimingSpecification(timing)
        assert ipdu.getIPduTimingSpecification() == timing
        assert ipdu == ipdu.setIPduTimingSpecification(timing)  # Test method chaining

        ipdu.setUnusedBitPattern(255)
        assert ipdu.getUnusedBitPattern() == 255
        assert ipdu == ipdu.setUnusedBitPattern(255)  # Test method chaining

        # Test ISignalToPduMappings creation method
        mapping = ipdu.createISignalToPduMappings("test_mapping")
        assert isinstance(mapping, ISignalToIPduMapping)
        assert len(ipdu.getISignalToPduMappings()) == 1

    def test_ISignal(self):
        """Test ISignal class functionality."""
        parent = MockParent()
        signal = ISignal(parent, "test_isignal")

        assert isinstance(signal, FibexElement)

        # Test default values
        assert signal.getDataTransformationRef() is None
        assert signal.getDataTypePolicy() is None
        assert signal.getISignalProps() is None
        assert signal.getISignalType() is None
        assert signal.getInitValue() is None
        assert signal.getLength() is None
        assert signal.getNetworkRepresentationProps() is None
        assert signal.getSystemSignalRef() is None
        assert signal.getTimeoutSubstitutionValue() is None
        assert signal.getTransformationISignalProps() == []

        # Test setter/getter methods with method chaining
        ref1 = object()
        signal.setDataTransformationRef(ref1)
        assert signal.getDataTransformationRef() == ref1
        assert signal == signal.setDataTransformationRef(ref1)  # Test method chaining

        signal.setDataTypePolicy("FIXED_LENGTH")
        assert signal.getDataTypePolicy() == "FIXED_LENGTH"
        assert signal == signal.setDataTypePolicy("FIXED_LENGTH")  # Test method chaining

        ref2 = object()
        signal.setISignalProps(ref2)
        assert signal.getISignalProps() == ref2
        assert signal == signal.setISignalProps(ref2)  # Test method chaining

        signal.setISignalType("BOOLEAN")
        assert signal.getISignalType() == "BOOLEAN"
        assert signal == signal.setISignalType("BOOLEAN")  # Test method chaining

        signal.setInitValue(42)
        assert signal.getInitValue() == 42
        assert signal == signal.setInitValue(42)  # Test method chaining

        signal.setLength(100)
        assert signal.getLength() == 100
        assert signal == signal.setLength(100)  # Test method chaining

        ref3 = object()
        signal.setNetworkRepresentationProps(ref3)
        assert signal.getNetworkRepresentationProps() == ref3
        assert signal == signal.setNetworkRepresentationProps(ref3)  # Test method chaining

        ref4 = object()
        signal.setSystemSignalRef(ref4)
        assert signal.getSystemSignalRef() == ref4
        assert signal == signal.setSystemSignalRef(ref4)  # Test method chaining

        signal.setTimeoutSubstitutionValue(0)
        assert signal.getTimeoutSubstitutionValue() == 0
        assert signal == signal.setTimeoutSubstitutionValue(0)  # Test method chaining

        ref5 = object()
        signal.addTransformationISignalProps(ref5)
        assert ref5 in signal.getTransformationISignalProps()
        assert signal == signal.addTransformationISignalProps(ref5)  # Test method chaining

    def test_PduTriggering(self):
        """Test PduTriggering class functionality."""
        parent = MockParent()
        triggering = PduTriggering(parent, "test_pdu_triggering")

        assert isinstance(triggering, Identifiable)

        # Test default values
        assert triggering.getIPduRef() is None
        assert triggering.getIPduPortRefs() == []
        assert triggering.getISignalTriggeringRefs() == []
        assert triggering.getSecOcCryptoMappingRef() is None
        assert triggering.getTriggerIPduSendConditions() == []

        # Test setter/getter methods with method chaining
        ref1 = object()
        triggering.setIPduRef(ref1)
        assert triggering.getIPduRef() == ref1
        assert triggering == triggering.setIPduRef(ref1)  # Test method chaining

        ref2 = object()
        triggering.addIPduPortRef(ref2)
        assert ref2 in triggering.getIPduPortRefs()
        assert triggering == triggering.addIPduPortRef(ref2)  # Test method chaining

        ref3 = object()
        triggering.addISignalTriggeringRef(ref3)
        assert ref3 in triggering.getISignalTriggeringRefs()
        assert triggering == triggering.addISignalTriggeringRef(ref3)  # Test method chaining

        ref4 = object()
        triggering.setSecOcCryptoMappingRef(ref4)
        assert triggering.getSecOcCryptoMappingRef() == ref4
        assert triggering == triggering.setSecOcCryptoMappingRef(ref4)  # Test method chaining

        ref5 = object()
        triggering.addTriggerIPduSendCondition(ref5)
        assert ref5 in triggering.getTriggerIPduSendConditions()
        assert triggering == triggering.addTriggerIPduSendCondition(ref5)  # Test method chaining

        # Test getISignalTriggeringRefs which has commented code that should be covered
        # The method returns the list directly (unlike the commented sorted version)
        refs = triggering.getISignalTriggeringRefs()
        assert isinstance(refs, list)

    def test_FrameTriggering(self):
        """Test FrameTriggering abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            FrameTriggering(parent, "test_frame_triggering")

    def test_FrameTriggering_methods(self):
        """Test FrameTriggering concrete implementation."""
        class ConcreteFrameTriggering(FrameTriggering):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = MockParent()
        triggering = ConcreteFrameTriggering(parent, "test_frame_triggering")

        # Test default values
        assert triggering.getFrameRef() is None
        assert triggering.getFramePortRefs() == []
        assert triggering.getPduTriggeringRefs() == []  # This is the line with potential type annotation issue

        # Test setter/getter methods with method chaining
        ref1 = object()
        triggering.setFrameRef(ref1)
        assert triggering.getFrameRef() == ref1
        assert triggering == triggering.setFrameRef(ref1)  # Test method chaining

        ref2 = object()
        triggering.addFramePortRef(ref2)
        assert ref2 in triggering.getFramePortRefs()
        assert triggering == triggering.addFramePortRef(ref2)  # Test method chaining

        ref3 = object()
        triggering.addPduTriggeringRef(ref3)
        assert ref3 in triggering.getPduTriggeringRefs()
        assert triggering == triggering.addPduTriggeringRef(ref3)  # Test method chaining

    def test_SystemSignal(self):
        """Test SystemSignal class functionality."""
        parent = MockParent()
        signal = SystemSignal(parent, "test_system_signal")

        assert isinstance(signal, ARElement)

        # Test default values
        assert signal.getDynamicLength() is None
        assert signal.getPhysicalProps() is None

        # Test setter/getter methods with method chaining
        signal.setDynamicLength(True)
        assert signal.getDynamicLength() is True
        assert signal == signal.setDynamicLength(True)  # Test method chaining

        ref1 = object()
        signal.setPhysicalProps(ref1)
        assert signal.getPhysicalProps() == ref1
        assert signal == signal.setPhysicalProps(ref1)  # Test method chaining

    def test_SystemSignalGroup(self):
        """Test SystemSignalGroup class functionality."""
        parent = MockParent()
        group = SystemSignalGroup(parent, "test_system_signal_group")

        assert isinstance(group, ARElement)

        # Test default values
        assert group.getSystemSignalRefs() == []
        assert group.getTransformingSystemSignalRef() is None

        # Test setter/getter methods with method chaining
        ref1 = object()
        group.addSystemSignalRefs(ref1)
        assert ref1 in group.getSystemSignalRefs()
        assert group == group.addSystemSignalRefs(ref1)  # Test method chaining

        ref2 = object()
        group.setTransformingSystemSignalRef(ref2)
        assert group.getTransformingSystemSignalRef() == ref2
        assert group == group.setTransformingSystemSignalRef(ref2)  # Test method chaining

    def test_ISignalTriggering(self):
        """Test ISignalTriggering class functionality."""
        parent = MockParent()
        triggering = ISignalTriggering(parent, "test_isignal_triggering")

        assert isinstance(triggering, Identifiable)

        # Test default values
        assert triggering.getISignalRef() is None
        assert triggering.getISignalGroupRef() is None
        assert triggering.getISignalPortRefs() == []

        # Test setter/getter methods with method chaining
        ref1 = object()
        triggering.setISignalRef(ref1)
        assert triggering.getISignalRef() == ref1
        assert triggering == triggering.setISignalRef(ref1)  # Test method chaining

        ref2 = object()
        triggering.setISignalGroupRef(ref2)
        assert triggering.getISignalGroupRef() == ref2
        assert triggering == triggering.setISignalGroupRef(ref2)  # Test method chaining

        ref3 = object()
        triggering.addISignalPortRef(ref3)
        assert ref3 in triggering.getISignalPortRefs()
        assert triggering == triggering.addISignalPortRef(ref3)  # Test method chaining

    def test_SegmentPosition(self):
        """Test SegmentPosition class functionality."""
        segment = SegmentPosition()

        assert isinstance(segment, ARObject)

        # Test default values
        assert segment.getSegmentByteOrder() is None
        assert segment.getSegmentLength() is None
        assert segment.getSegmentPosition() is None

        # Test setter/getter methods with method chaining
        segment.setSegmentByteOrder("MOST_SIGNIFICANT_BYTE_FIRST")
        assert segment.getSegmentByteOrder() == "MOST_SIGNIFICANT_BYTE_FIRST"
        assert segment == segment.setSegmentByteOrder("MOST_SIGNIFICANT_BYTE_FIRST")  # Test method chaining

        segment.setSegmentLength(100)
        assert segment.getSegmentLength() == 100
        assert segment == segment.setSegmentLength(100)  # Test method chaining

        segment.setSegmentPosition(50)
        assert segment.getSegmentPosition() == 50
        assert segment == segment.setSegmentPosition(50)  # Test method chaining

    def test_MultiplexedPart(self):
        """Test MultiplexedPart abstract class instantiation."""
        with pytest.raises(NotImplementedError):
            MultiplexedPart()

    def test_MultiplexedPart_methods(self):
        """Test MultiplexedPart subclass methods."""
        class ConcreteMultiplexedPart(MultiplexedPart):
            def __init__(self):
                super().__init__()
        
        part = ConcreteMultiplexedPart()
        # Test default values
        assert part.getSegmentPositions() == []

        # Test addSegmentPosition with None value (should not add to list)
        part.addSegmentPosition(None)
        assert part.getSegmentPositions() == []  # List should remain empty
        assert part == part.addSegmentPosition(None)  # Test method chaining

        # Test addSegmentPosition with actual value
        segment = SegmentPosition()
        part.addSegmentPosition(segment)
        assert segment in part.getSegmentPositions()
        assert part == part.addSegmentPosition(segment)  # Test method chaining

    def test_StaticPart(self):
        """Test StaticPart class functionality."""
        static_part = StaticPart()

        assert isinstance(static_part, MultiplexedPart)

        # Test default values
        assert static_part.getIPduRef() is None

        # Test setter/getter methods with method chaining
        ref1 = object()
        static_part.setIPduRef(ref1)
        assert static_part.getIPduRef() == ref1
        assert static_part == static_part.setIPduRef(ref1)  # Test method chaining

    def test_DynamicPartAlternative(self):
        """Test DynamicPartAlternative class functionality."""
        alt = DynamicPartAlternative()

        assert isinstance(alt, ARObject)

        # Test default values
        assert alt.getInitialDynamicPart() is None
        assert alt.getIPduRef() is None
        assert alt.getSelectorFieldCode() is None

        # Test setter/getter methods with method chaining
        alt.setInitialDynamicPart(True)
        assert alt.getInitialDynamicPart() is True
        assert alt == alt.setInitialDynamicPart(True)  # Test method chaining

        ref1 = object()
        alt.setIPduRef(ref1)
        assert alt.getIPduRef() == ref1
        assert alt == alt.setIPduRef(ref1)  # Test method chaining

        alt.setSelectorFieldCode(42)
        assert alt.getSelectorFieldCode() == 42
        assert alt == alt.setSelectorFieldCode(42)  # Test method chaining

    def test_DynamicPart(self):
        """Test DynamicPart class functionality."""
        dynamic_part = DynamicPart()

        assert isinstance(dynamic_part, MultiplexedPart)

        # Test default values
        assert dynamic_part.getDynamicPartAlternatives() == []

        # Test setter/getter methods with method chaining
        alt = DynamicPartAlternative()
        dynamic_part.addDynamicPartAlternative(alt)
        assert alt in dynamic_part.getDynamicPartAlternatives()
        assert dynamic_part == dynamic_part.addDynamicPartAlternative(alt)  # Test method chaining

    def test_MultiplexedIPdu(self):
        """Test MultiplexedIPdu class functionality."""
        parent = MockParent()
        ipdu = MultiplexedIPdu(parent, "test_multiplexed_ipdu")

        assert isinstance(ipdu, IPdu)

        # Test default values
        assert ipdu.getDynamicPart() is None
        assert ipdu.getSelectorFieldByteOrder() is None
        assert ipdu.getSelectorFieldLength() is None
        assert ipdu.getSelectorFieldStartPosition() is None
        assert ipdu.getStaticPart() is None
        assert ipdu.getTriggerMode() is None
        assert ipdu.getUnusedBitPattern() is None

        # Test setter/getter methods with method chaining
        dynamic_part = DynamicPart()
        ipdu.setDynamicPart(dynamic_part)
        assert ipdu.getDynamicPart() == dynamic_part
        assert ipdu == ipdu.setDynamicPart(dynamic_part)  # Test method chaining

        ipdu.setSelectorFieldByteOrder("MOST_SIGNIFICANT_BYTE_FIRST")
        assert ipdu.getSelectorFieldByteOrder() == "MOST_SIGNIFICANT_BYTE_FIRST"
        assert ipdu == ipdu.setSelectorFieldByteOrder("MOST_SIGNIFICANT_BYTE_FIRST")  # Test method chaining

        ipdu.setSelectorFieldLength(10)
        assert ipdu.getSelectorFieldLength() == 10
        assert ipdu == ipdu.setSelectorFieldLength(10)  # Test method chaining

        ipdu.setSelectorFieldStartPosition(20)
        assert ipdu.getSelectorFieldStartPosition() == 20
        assert ipdu == ipdu.setSelectorFieldStartPosition(20)  # Test method chaining

        static_part = StaticPart()
        ipdu.setStaticPart(static_part)
        assert ipdu.getStaticPart() == static_part
        assert ipdu == ipdu.setStaticPart(static_part)  # Test method chaining

        ipdu.setTriggerMode("CYCLIC")
        assert ipdu.getTriggerMode() == "CYCLIC"
        assert ipdu == ipdu.setTriggerMode("CYCLIC")  # Test method chaining

        ipdu.setUnusedBitPattern(255)
        assert ipdu.getUnusedBitPattern() == 255
        assert ipdu == ipdu.setUnusedBitPattern(255)  # Test method chaining

    def test_GeneralPurposePdu(self):
        """Test GeneralPurposePdu class functionality."""
        parent = MockParent()
        pdu = GeneralPurposePdu(parent, "test_general_purpose_pdu")

        assert isinstance(pdu, Pdu)

    def test_GeneralPurposeIPdu(self):
        """Test GeneralPurposeIPdu class functionality."""
        parent = MockParent()
        ipdu = GeneralPurposeIPdu(parent, "test_general_purpose_ipdu")

        assert isinstance(ipdu, IPdu)

    def test_SecureCommunicationPropsSet(self):
        """Test SecureCommunicationPropsSet class functionality."""
        parent = MockParent()
        props_set = SecureCommunicationPropsSet(parent, "test_secure_com_props_set")

        assert isinstance(props_set, Identifiable)

        # Test default values
        assert props_set.secureComProps == []

    def test_UserDefinedPdu(self):
        """Test UserDefinedPdu class functionality."""
        parent = MockParent()
        pdu = UserDefinedPdu(parent, "test_user_defined_pdu")

        assert isinstance(pdu, Pdu)

    def test_UserDefinedIPdu(self):
        """Test UserDefinedIPdu class functionality."""
        parent = MockParent()
        ipdu = UserDefinedIPdu(parent, "test_user_defined_ipdu")

        assert isinstance(ipdu, IPdu)

    def test_SecureCommunicationAuthenticationProps(self):
        """Test SecureCommunicationAuthenticationProps class functionality."""
        parent = MockParent()
        auth_props = SecureCommunicationAuthenticationProps(parent, "test_auth_props")

        assert isinstance(auth_props, Identifiable)

        # Test default values
        assert auth_props.getAuthenticationBuildAttempts() is None
        assert auth_props.getAuthenticationRetries() is None
        assert auth_props.getDataId() is None
        assert auth_props.getSecuredComAuthenticationType() is None

        # Test setter/getter methods with method chaining (only when value is not None)
        auth_props.setAuthenticationBuildAttempts(5)
        assert auth_props.getAuthenticationBuildAttempts() == 5
        assert auth_props == auth_props.setAuthenticationBuildAttempts(5)  # Test method chaining

        auth_props.setAuthenticationRetries(3)
        assert auth_props.getAuthenticationRetries() == 3
        assert auth_props == auth_props.setAuthenticationRetries(3)  # Test method chaining

        auth_props.setDataId(42)
        assert auth_props.getDataId() == 42
        assert auth_props == auth_props.setDataId(42)  # Test method chaining

        auth_props.setSecuredComAuthenticationType("HMAC_SHA256")
        assert auth_props.getSecuredComAuthenticationType() == "HMAC_SHA256"
        assert auth_props == auth_props.setSecuredComAuthenticationType("HMAC_SHA256")  # Test method chaining

    def test_SecureCommunicationFreshnessProps(self):
        """Test SecureCommunicationFreshnessProps class functionality."""
        parent = MockParent()
        freshness_props = SecureCommunicationFreshnessProps(parent, "test_freshness_props")

        assert isinstance(freshness_props, Identifiable)

        # Test default values
        assert freshness_props.getFreshnessValueId() is None
        assert freshness_props.getFreshnessValueLength() is None
        assert freshness_props.getFreshnessValueTxLength() is None
        assert freshness_props.getMessageLinkLength() is None
        assert freshness_props.getMessageLinkPosition() is None
        assert freshness_props.getSecondaryFreshnessValueId() is None
        assert freshness_props.getSecuredComFreshnessType() is None

        # Test setter/getter methods with method chaining (only when value is not None)
        freshness_props.setFreshnessValueId(100)
        assert freshness_props.getFreshnessValueId() == 100
        assert freshness_props == freshness_props.setFreshnessValueId(100)  # Test method chaining

        freshness_props.setFreshnessValueLength(50)
        assert freshness_props.getFreshnessValueLength() == 50
        assert freshness_props == freshness_props.setFreshnessValueLength(50)  # Test method chaining

        freshness_props.setFreshnessValueTxLength(60)
        assert freshness_props.getFreshnessValueTxLength() == 60
        assert freshness_props == freshness_props.setFreshnessValueTxLength(60)  # Test method chaining

        freshness_props.setMessageLinkLength(70)
        assert freshness_props.getMessageLinkLength() == 70
        assert freshness_props == freshness_props.setMessageLinkLength(70)  # Test method chaining

        freshness_props.setMessageLinkPosition(80)
        assert freshness_props.getMessageLinkPosition() == 80
        assert freshness_props == freshness_props.setMessageLinkPosition(80)  # Test method chaining

        freshness_props.setSecondaryFreshnessValueId(200)
        assert freshness_props.getSecondaryFreshnessValueId() == 200
        assert freshness_props == freshness_props.setSecondaryFreshnessValueId(200)  # Test method chaining

        freshness_props.setSecuredComFreshnessType("COUNTER_BASED")
        assert freshness_props.getSecuredComFreshnessType() == "COUNTER_BASED"
        assert freshness_props == freshness_props.setSecuredComFreshnessType("COUNTER_BASED")  # Test method chaining