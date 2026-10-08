"""
Tests for the ARObject class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 6.1).
"""

import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    AbstractGlobalTimeDomainProps,
    ARObject,
    BinaryManifestItemValue,
    BusMirrorCanIdRangeMapping,
    BusMirrorCanIdToCanIdMapping,
    BusMirrorLinPidToCanIdMapping,
    CalibrationParameterValue,
    CanGlobalTimeDomainProps,
    ClientServerOperationComProps,
    CpSoftwareClusterCommunicationResourceProps,
    DataComProps,
    DdsCpProvidedServiceInstance,
    DdsCpServiceInstanceEvent,
    DdsCpServiceInstanceOperation,
    DdsDeadline,
    DdsDestinationOrder,
    DdsDurability,
    DdsDurabilityService,
    DdsHistory,
    DdsLatencyBudget,
    DdsLifespan,
    DdsLiveliness,
    DdsOwnership,
    DdsOwnershipStrength,
    DdsReliability,
    DdsResourceLimits,
    DdsTopicData,
    DdsTransportPriority,
    DiagnosticAbstractParameter,
    DiagnosticComControlSpecificChannel,
    DiagnosticComControlSubNodeChannel,
    DiagnosticCommonProps,
    DiagnosticConnectedIndicator,
    DiagnosticControlEnableMaskBit,
    DiagnosticEventWindow,
    DiagnosticFunctionIdentifierInhibit,
    DiagnosticIumprGroupIdentifier,
    DiagnosticMemoryDestination,
    DiagnosticMemoryDestinationUserDefined,
    DiagnosticParameter,
    DiagnosticParameterSupportInfo,
    DiagnosticPeriodicRate,
    DiagnosticSupportInfoByte,
    DiagnosticTestIdentifier,
    DiagnosticTroubleCodeObd,
    DiagnosticTroubleCodeProps,
    DiagnosticTroubleCodeUds,
    EthGlobalTimeDomainProps,
    EthGlobalTimeManagedCouplingPort,
    EthTSynCrcFlags,
    EthTSynSubTlvConfig,
    EventObdReadinessGroup,
    FrGlobalTimeDomainProps,
    GlobalTimeCorrectionProps,
    NetworkSegmentIdentification,
    PhysicalDimensionMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDebounceAlgorithmProps, DiagnosticFunctionInhibitSource, DiagnosticParameterElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    ByteOrderEnum,
    DataConsistencyPolicyEnum,
    DateTime,
    DdsDestinationOrderKindEnum,
    DdsDurabilityKindEnum,
    DdsDurabilityServiceHistoryKindEnum,
    DdsHistoryKindEnum,
    DdsLivenessKindEnum,
    DdsOwnershipKindEnum,
    DdsReliabilityKindEnum,
    DiagnosticClearDtcLimitationEnum,
    DiagnosticConnectedIndicatorBehaviorEnum,
    DiagnosticEventCombinationBehaviorEnum,
    DiagnosticEventCombinationReportingBehaviorEnum,
    DiagnosticEventDisplacementStrategyEnum,
    DiagnosticEventWindowTimeEnum,
    DiagnosticInhibitionMaskEnum,
    DiagnosticMemoryEntryStorageTriggerEnum,
    DiagnosticOccurrenceCounterProcessingEnum,
    DiagnosticPeriodicRateCategoryEnum,
    DiagnosticSignificanceEnum,
    DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum,
    DiagnosticTypeOfFreezeFrameRecordNumerationEnum,
    DiagnosticUdsSeverityEnum,
    DiagnosticWwhObdDtcClassEnum,
    EthGlobalTimeMessageFormatEnum,
    Float,
    GlobalTimePortRoleEnum,
    MacAddressString,
    NameToken,
    PositiveInteger,
    RefType,
    SendIndicationEnum,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable


class ConcreteARObject(ARObject):
    pass


class TestARObject:
    def test_abstract_initialization(self):
        """
        ARObject is abstract and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            ARObject()

    def test_initialization(self):
        """
        A concrete ARObject initializes all members to None.
        """
        obj = ConcreteARObject()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.parent is None

    def test_get_set_checksum(self):
        """
        Round-trips the checksum member; None is a no-op.
        """
        obj = ConcreteARObject()

        value = String()
        value.setValue("abc123")
        obj.setChecksum(value)
        assert obj.getChecksum() is value

        obj.setChecksum(None)
        assert obj.getChecksum() is value

    def test_get_set_timestamp(self):
        """
        Round-trips the timestamp member; None is a no-op.
        """
        obj = ConcreteARObject()

        value = DateTime()
        value.setValue("2009-07-23T13:38:00Z")
        obj.setTimestamp(value)
        assert obj.getTimestamp() is value

        obj.setTimestamp(None)
        assert obj.getTimestamp() is value

    def test_get_tag_name(self):
        """
        getTagName strips the namespace prefix from a tag name.
        """
        obj = ConcreteARObject()

        nsmap = {"xmlns": "http://www.example.com/ns"}
        assert obj.getTagName("{http://www.example.com/ns}elementName", nsmap) == "elementName"
        assert obj.getTagName("simpleTag", nsmap) == "simpleTag"


class TestDiagnosticParameter:
    """
    Test class for DiagnosticParameter functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.5, p.36
    (Base DiagnosticAbstractParameter is an un-synced stub queued for a later
    batch — only DiagnosticParameter's own Table 4.5 rows are exercised here.)
    """

    def _create_parameter(self) -> DiagnosticParameter:
        return DiagnosticParameter()

    def test_initialization(self):
        """
        Test that DiagnosticParameter is initialized with the spec defaults.
        """
        obj = self._create_parameter()

        assert obj.getIdent() is None
        assert obj.getSupportInfo() is None

    def test_create_ident(self):
        """
        Test createIdent creates, returns self-contained ident and returns the existing one for a duplicate short name.
        """
        obj = self._create_parameter()

        ident = obj.createIdent("Pid1")
        assert ident is not None
        assert ident.getShortName() == "Pid1"
        assert obj.getIdent() is ident

        duplicate = obj.createIdent("Pid1")
        assert duplicate is ident  # duplicate short name returns the existing ident

    def test_get_set_support_info(self):
        """
        Test getSupportInfo and setSupportInfo round-trip and None no-op.
        """
        obj = self._create_parameter()

        support_info = DiagnosticParameterSupportInfo()
        result = obj.setSupportInfo(support_info)
        assert result is obj  # method chaining
        assert obj.getSupportInfo() is support_info

        result = obj.setSupportInfo(None)
        assert result is obj  # method chaining with None
        assert obj.getSupportInfo() is support_info  # None is a no-op

    def test_variation_point_mixin(self):
        """
        Test the VariationPointCapable mixin accessors (VP-capable per Rule 0020: XSD group DIAGNOSTIC-PARAMETER carries VARIATION-POINT).
        """
        obj = self._create_parameter()

        assert obj.getVariationPoint() is None


class TestDiagnosticAbstractParameter:
    """
    Test class for DiagnosticAbstractParameter functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.8, p.37
    (abstract; subclasses DiagnosticParameter and DiagnosticParameterElement —
    base accessors exercised through DiagnosticParameter per the abstract-class
    test convention.)
    """

    def test_abstract_initialization(self):
        """
        DiagnosticAbstractParameter is abstract and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            DiagnosticAbstractParameter()

    def test_base_properties(self):
        """
        Exercises every base getter/setter through the concrete DiagnosticParameter:
        chaining, round-trip, and a final None no-op for the whole set.
        """
        obj = DiagnosticParameter()

        assert obj.getBitOffset() is None
        assert obj.getDataElement() is None
        assert obj.getParameterSize() is None

        bit_offset = PositiveInteger()
        bit_offset.setValue("8")
        assert obj.setBitOffset(bit_offset) is obj
        assert obj.getBitOffset() is bit_offset

        data_element = obj.createDataElement("De1")
        assert data_element is not None
        assert data_element.getShortName() == "De1"
        assert data_element.getParent() is obj
        assert obj.getDataElement() is data_element

        parameter_size = PositiveInteger()
        parameter_size.setValue("16")
        assert obj.setParameterSize(parameter_size) is obj
        assert obj.getParameterSize() is parameter_size

        obj.setBitOffset(None)
        assert obj.getBitOffset() is bit_offset  # None is a no-op
        obj.setParameterSize(None)
        assert obj.getParameterSize() is parameter_size  # None is a no-op

    def test_create_data_element_duplicate(self):
        """
        Test createDataElement returns the existing element for a duplicate short name.
        """
        obj = DiagnosticParameter()

        data_element = obj.createDataElement("De1")
        duplicate = obj.createDataElement("De1")
        assert duplicate is data_element  # duplicate short name returns the existing element

        replaced = obj.createDataElement("De2")
        assert replaced is not data_element
        assert obj.getDataElement() is replaced

    def test_get_set_bit_offset_type_hints(self):
        """
        Pin the bitOffset accessor annotations to the spec type (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticAbstractParameter.getBitOffset)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(DiagnosticAbstractParameter.setBitOffset)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is DiagnosticAbstractParameter

    def test_get_set_parameter_size_type_hints(self):
        """
        Pin the parameterSize accessor annotations to the spec type (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticAbstractParameter.getParameterSize)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(DiagnosticAbstractParameter.setParameterSize)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is DiagnosticAbstractParameter

    def test_subclass_inherits_base_fields(self):
        """
        Both subclasses initialize the inherited base fields via their __init__ chains.
        """
        parameter = DiagnosticParameter()
        assert parameter.getBitOffset() is None
        assert parameter.getDataElement() is None
        assert parameter.getParameterSize() is None

        element = DiagnosticParameterElement(AUTOSAR.getInstance(), "Elem1")
        assert element.getBitOffset() is None
        assert element.getDataElement() is None
        assert element.getParameterSize() is None
        assert element.getShortName() == "Elem1"


class TestDiagnosticCommonProps:
    """
    Test class for DiagnosticCommonProps functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.19, p.65
    """

    def _create_props(self) -> DiagnosticCommonProps:
        return DiagnosticCommonProps()

    def test_initialization(self):
        """
        Test that DiagnosticCommonProps is initialized with the spec defaults.
        """
        obj = self._create_props()

        assert obj.getAuthenticationTimeout() is None
        assert obj.getDebounceAlgorithmProps() == []
        assert obj.getDefaultEndianness() is None
        assert obj.getEventCombinationReportingBehavior() is None
        assert obj.getMaxNumberOfRequestCorrectlyReceivedResponsePending() is None
        assert obj.getOccurrenceCounterProcessing() is None
        assert obj.getResetConfirmedBitOnOverflow() is None
        assert obj.getResetPendingBitOnOverflow() is None
        assert obj.getResponseOnAllRequestSids() is None
        assert obj.getResponseOnSecondDeclinedRequest() is None
        assert obj.getTypeOfEventCombinationSupported() is None

    def test_get_set_authentication_timeout(self):
        """
        Test getAuthenticationTimeout and setAuthenticationTimeout round-trip and None no-op.
        """
        obj = self._create_props()

        timeout = TimeValue()
        timeout.setValue(0.5)
        result = obj.setAuthenticationTimeout(timeout)
        assert result is obj  # method chaining
        assert obj.getAuthenticationTimeout() is timeout

        result = obj.setAuthenticationTimeout(None)
        assert result is obj  # method chaining with None
        assert obj.getAuthenticationTimeout() is timeout  # None is a no-op

    def test_create_debounce_algorithm_props(self):
        """
        Test createDebounceAlgorithmProps creates, appends and returns the existing one for a duplicate short name.
        """
        obj = self._create_props()

        props = obj.createDebounceAlgorithmProps("Deb1")
        assert props is not None
        assert isinstance(props, DiagnosticDebounceAlgorithmProps)
        assert props.getShortName() == "Deb1"
        assert props.getParent() is obj
        assert obj.getDebounceAlgorithmProps() == [props]

        duplicate = obj.createDebounceAlgorithmProps("Deb1")
        assert duplicate is props  # duplicate short name returns the existing element

    def test_get_set_default_endianness(self):
        """
        Test getDefaultEndianness and setDefaultEndianness round-trip and None no-op.
        """
        obj = self._create_props()

        endianness = ByteOrderEnum().setValue(ByteOrderEnum.OPAQUE)
        result = obj.setDefaultEndianness(endianness)
        assert result is obj  # method chaining
        assert obj.getDefaultEndianness() is endianness
        assert obj.getDefaultEndianness().getValue() == ByteOrderEnum.OPAQUE

        result = obj.setDefaultEndianness(None)
        assert result is obj  # method chaining with None
        assert obj.getDefaultEndianness() is endianness  # None is a no-op

    def test_get_set_max_number_of_request_correctly_received_response_pending(self):
        """
        Test getMaxNumberOfRequestCorrectlyReceivedResponsePending and its setter round-trip and None no-op.
        """
        obj = self._create_props()

        max_number = PositiveInteger()
        max_number.setValue("10")
        result = obj.setMaxNumberOfRequestCorrectlyReceivedResponsePending(max_number)
        assert result is obj  # method chaining
        assert obj.getMaxNumberOfRequestCorrectlyReceivedResponsePending() is max_number
        assert obj.getMaxNumberOfRequestCorrectlyReceivedResponsePending().getValue() == 10

        result = obj.setMaxNumberOfRequestCorrectlyReceivedResponsePending(None)
        assert result is obj  # method chaining with None
        assert obj.getMaxNumberOfRequestCorrectlyReceivedResponsePending() is max_number  # None is a no-op

    def test_get_set_occurrence_counter_processing(self):
        """
        Test getOccurrenceCounterProcessing and setOccurrenceCounterProcessing round-trip and None no-op.
        """
        obj = self._create_props()

        processing = DiagnosticOccurrenceCounterProcessingEnum().setValue(DiagnosticOccurrenceCounterProcessingEnum.CONFIRMED_DTC_BIT)
        result = obj.setOccurrenceCounterProcessing(processing)
        assert result is obj  # method chaining
        assert obj.getOccurrenceCounterProcessing() is processing
        assert obj.getOccurrenceCounterProcessing().getValue() == DiagnosticOccurrenceCounterProcessingEnum.CONFIRMED_DTC_BIT

        result = obj.setOccurrenceCounterProcessing(None)
        assert result is obj  # method chaining with None
        assert obj.getOccurrenceCounterProcessing() is processing  # None is a no-op

    def test_get_set_reset_confirmed_bit_on_overflow(self):
        """
        Test getResetConfirmedBitOnOverflow and setResetConfirmedBitOnOverflow round-trip and None no-op.
        """
        obj = self._create_props()

        value = Boolean()
        value.setValue(True)
        result = obj.setResetConfirmedBitOnOverflow(value)
        assert result is obj  # method chaining
        assert obj.getResetConfirmedBitOnOverflow() is value

        result = obj.setResetConfirmedBitOnOverflow(None)
        assert result is obj  # method chaining with None
        assert obj.getResetConfirmedBitOnOverflow() is value  # None is a no-op

    def test_get_set_reset_pending_bit_on_overflow(self):
        """
        Test getResetPendingBitOnOverflow and setResetPendingBitOnOverflow round-trip and None no-op.
        """
        obj = self._create_props()

        value = Boolean()
        value.setValue(False)
        result = obj.setResetPendingBitOnOverflow(value)
        assert result is obj  # method chaining
        assert obj.getResetPendingBitOnOverflow() is value

        result = obj.setResetPendingBitOnOverflow(None)
        assert result is obj  # method chaining with None
        assert obj.getResetPendingBitOnOverflow() is value  # None is a no-op

    def test_get_set_response_on_all_request_sids(self):
        """
        Test getResponseOnAllRequestSids and setResponseOnAllRequestSids round-trip and None no-op.
        """
        obj = self._create_props()

        value = Boolean()
        value.setValue(False)
        result = obj.setResponseOnAllRequestSids(value)
        assert result is obj  # method chaining
        assert obj.getResponseOnAllRequestSids() is value

        result = obj.setResponseOnAllRequestSids(None)
        assert result is obj  # method chaining with None
        assert obj.getResponseOnAllRequestSids() is value  # None is a no-op

    def test_get_set_event_combination_reporting_behavior(self):
        """
        Test getEventCombinationReportingBehavior and setEventCombinationReportingBehavior round-trip and None no-op.
        """
        obj = self._create_props()

        behavior = DiagnosticEventCombinationReportingBehaviorEnum().setValue(DiagnosticEventCombinationReportingBehaviorEnum.REPORTING_IN_CHRONLOGICAL_ORDER_OLDEST_FIRST)
        result = obj.setEventCombinationReportingBehavior(behavior)
        assert result is obj  # method chaining
        assert obj.getEventCombinationReportingBehavior() is behavior
        assert obj.getEventCombinationReportingBehavior().getValue() == DiagnosticEventCombinationReportingBehaviorEnum.REPORTING_IN_CHRONLOGICAL_ORDER_OLDEST_FIRST

        result = obj.setEventCombinationReportingBehavior(None)
        assert result is obj  # method chaining with None
        assert obj.getEventCombinationReportingBehavior() is behavior  # None is a no-op

    def test_get_set_type_of_event_combination_supported(self):
        """
        Test getTypeOfEventCombinationSupported and setTypeOfEventCombinationSupported round-trip and None no-op.
        """
        obj = self._create_props()

        behavior = DiagnosticEventCombinationBehaviorEnum().setValue(DiagnosticEventCombinationBehaviorEnum.EVENT_COMBINATION_ON_STORAGE)
        result = obj.setTypeOfEventCombinationSupported(behavior)
        assert result is obj  # method chaining
        assert obj.getTypeOfEventCombinationSupported() is behavior
        assert obj.getTypeOfEventCombinationSupported().getValue() == DiagnosticEventCombinationBehaviorEnum.EVENT_COMBINATION_ON_STORAGE

        result = obj.setTypeOfEventCombinationSupported(None)
        assert result is obj  # method chaining with None
        assert obj.getTypeOfEventCombinationSupported() is behavior  # None is a no-op

    def test_get_set_response_on_second_declined_request(self):
        """
        Test getResponseOnSecondDeclinedRequest and setResponseOnSecondDeclinedRequest round-trip and None no-op.
        """
        obj = self._create_props()

        value = Boolean()
        value.setValue(True)
        result = obj.setResponseOnSecondDeclinedRequest(value)
        assert result is obj  # method chaining
        assert obj.getResponseOnSecondDeclinedRequest() is value

        result = obj.setResponseOnSecondDeclinedRequest(None)
        assert result is obj  # method chaining with None
        assert obj.getResponseOnSecondDeclinedRequest() is value  # None is a no-op


class TestDiagnosticComControlSpecificChannel:
    """
    Test class for DiagnosticComControlSpecificChannel functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.65, p.109
    """

    def _create_channel(self) -> DiagnosticComControlSpecificChannel:
        return DiagnosticComControlSpecificChannel()

    def test_initialization(self):
        """
        Test that a new DiagnosticComControlSpecificChannel initializes all attributes to None.
        """
        obj = self._create_channel()

        assert obj.getSpecificChannel() is None
        assert obj.getSpecificPhysicalChannel() is None
        assert obj.getSubnetNumber() is None

    def test_get_set_specific_channel(self):
        """
        Test getSpecificChannel and setSpecificChannel round-trip and None no-op.
        """
        obj = self._create_channel()

        ref = RefType()
        ref.setDest("COMMUNICATION-CLUSTER")
        ref.setValue("/System/Clusters/Cluster1")
        result = obj.setSpecificChannel(ref)
        assert result is obj  # method chaining
        assert obj.getSpecificChannel() is ref
        assert obj.getSpecificChannel().getValue() == "/System/Clusters/Cluster1"
        assert obj.getSpecificChannel().getDest() == "COMMUNICATION-CLUSTER"

        result = obj.setSpecificChannel(None)
        assert result is obj  # method chaining with None
        assert obj.getSpecificChannel() is ref  # None is a no-op

    def test_get_set_specific_physical_channel(self):
        """
        Test getSpecificPhysicalChannel and setSpecificPhysicalChannel round-trip and None no-op.
        """
        obj = self._create_channel()

        ref = RefType()
        ref.setDest("ETHERNET-PHYSICAL-CHANNEL")
        ref.setValue("/System/EthernetClusters/Cluster1/Vlan1")
        result = obj.setSpecificPhysicalChannel(ref)
        assert result is obj  # method chaining
        assert obj.getSpecificPhysicalChannel() is ref
        assert obj.getSpecificPhysicalChannel().getValue() == "/System/EthernetClusters/Cluster1/Vlan1"

        result = obj.setSpecificPhysicalChannel(None)
        assert result is obj  # method chaining with None
        assert obj.getSpecificPhysicalChannel() is ref  # None is a no-op

    def test_get_set_subnet_number(self):
        """
        Test getSubnetNumber and setSubnetNumber round-trip and None no-op.
        """
        obj = self._create_channel()

        value = PositiveInteger()
        value.setValue("3")
        result = obj.setSubnetNumber(value)
        assert result is obj  # method chaining
        assert obj.getSubnetNumber() is value
        assert obj.getSubnetNumber().getValue() == 3

        result = obj.setSubnetNumber(None)
        assert result is obj  # method chaining with None
        assert obj.getSubnetNumber() is value  # None is a no-op

    def test_get_set_specific_channel_type_hints(self):
        """
        Pin the specificChannel accessor annotations to the spec type (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticComControlSpecificChannel.getSpecificChannel)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(DiagnosticComControlSpecificChannel.setSpecificChannel)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is DiagnosticComControlSpecificChannel

    def test_get_set_subnet_number_type_hints(self):
        """
        Pin the subnetNumber accessor annotations to the spec type (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticComControlSpecificChannel.getSubnetNumber)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(DiagnosticComControlSpecificChannel.setSubnetNumber)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is DiagnosticComControlSpecificChannel


class TestDiagnosticComControlSubNodeChannel:
    """
    Test class for DiagnosticComControlSubNodeChannel functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.67, p.110
    """

    def _create_channel(self) -> DiagnosticComControlSubNodeChannel:
        return DiagnosticComControlSubNodeChannel()

    def test_initialization(self):
        """
        Test that a new DiagnosticComControlSubNodeChannel initializes all attributes to None.
        """
        obj = self._create_channel()

        assert obj.getSubNodeChannel() is None
        assert obj.getSubNodeNumber() is None
        assert obj.getSubNodePhysicalChannel() is None

    def test_get_set_sub_node_channel(self):
        """
        Test getSubNodeChannel and setSubNodeChannel round-trip and None no-op.
        """
        obj = self._create_channel()

        ref = RefType()
        ref.setDest("COMMUNICATION-CLUSTER")
        ref.setValue("/System/Clusters/Cluster1")
        result = obj.setSubNodeChannel(ref)
        assert result is obj  # method chaining
        assert obj.getSubNodeChannel() is ref
        assert obj.getSubNodeChannel().getValue() == "/System/Clusters/Cluster1"
        assert obj.getSubNodeChannel().getDest() == "COMMUNICATION-CLUSTER"

        result = obj.setSubNodeChannel(None)
        assert result is obj  # method chaining with None
        assert obj.getSubNodeChannel() is ref  # None is a no-op

    def test_get_set_sub_node_number(self):
        """
        Test getSubNodeNumber and setSubNodeNumber round-trip and None no-op.
        """
        obj = self._create_channel()

        value = PositiveInteger()
        value.setValue("7")
        result = obj.setSubNodeNumber(value)
        assert result is obj  # method chaining
        assert obj.getSubNodeNumber() is value
        assert obj.getSubNodeNumber().getValue() == 7

        result = obj.setSubNodeNumber(None)
        assert result is obj  # method chaining with None
        assert obj.getSubNodeNumber() is value  # None is a no-op

    def test_get_set_sub_node_physical_channel(self):
        """
        Test getSubNodePhysicalChannel and setSubNodePhysicalChannel round-trip and None no-op.
        """
        obj = self._create_channel()

        ref = RefType()
        ref.setDest("ETHERNET-PHYSICAL-CHANNEL")
        ref.setValue("/System/EthernetClusters/Cluster1/Vlan2")
        result = obj.setSubNodePhysicalChannel(ref)
        assert result is obj  # method chaining
        assert obj.getSubNodePhysicalChannel() is ref
        assert obj.getSubNodePhysicalChannel().getValue() == "/System/EthernetClusters/Cluster1/Vlan2"
        assert obj.getSubNodePhysicalChannel().getDest() == "ETHERNET-PHYSICAL-CHANNEL"

        result = obj.setSubNodePhysicalChannel(None)
        assert result is obj  # method chaining with None
        assert obj.getSubNodePhysicalChannel() is ref  # None is a no-op

    def test_get_set_sub_node_channel_type_hints(self):
        """
        Pin the subNodeChannel accessor annotations to the spec type (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticComControlSubNodeChannel.getSubNodeChannel)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = typing.get_type_hints(DiagnosticComControlSubNodeChannel.setSubNodeChannel)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is DiagnosticComControlSubNodeChannel

    def test_get_set_sub_node_number_type_hints(self):
        """
        Pin the subNodeNumber accessor annotations to the spec type (Rule 0003).
        """
        getter_hints = typing.get_type_hints(DiagnosticComControlSubNodeChannel.getSubNodeNumber)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(DiagnosticComControlSubNodeChannel.setSubNodeNumber)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is DiagnosticComControlSubNodeChannel


class TestDiagnosticControlEnableMaskBit:
    """
    Test class for DiagnosticControlEnableMaskBit functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.83, p.119
    """

    CLASS_NOTE = "This meta-class has the ability to represent one bit in the control enable mask record."
    BIT_NUMBER_NOTE = (
        "This attribute represents the bit number of the bit in the control mask record." " Bit number 0 is the most significant bit (MSB) in the first byte of the CEMR in the network presentation."
    )
    CONTROLLED_DATA_ELEMENT_NOTE = "This reference represents the collection of DiagnosticDataElements that are controlled by this bit of the control mask record."

    def _create_mask_bit(self) -> DiagnosticControlEnableMaskBit:
        return DiagnosticControlEnableMaskBit()

    def test_initialization(self):
        """
        Test that a new DiagnosticControlEnableMaskBit initializes all attributes to their defaults.
        """
        obj = self._create_mask_bit()

        assert obj.getBitNumber() is None
        assert obj.getControlledDataElements() == []

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticControlEnableMaskBit derives from ARObject (Table 4.83 Base).
        """
        assert issubclass(DiagnosticControlEnableMaskBit, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticControlEnableMaskBit.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticControlEnableMaskBit.__init__.__doc__ is None

    def test_get_set_bit_number(self):
        """
        Test getBitNumber and setBitNumber round-trip and None no-op.
        """
        obj = self._create_mask_bit()

        value = PositiveInteger()
        value.setValue("7")
        result = obj.setBitNumber(value)
        assert result is obj  # method chaining
        assert obj.getBitNumber() is value
        assert obj.getBitNumber().getValue() == 7

        result = obj.setBitNumber(None)
        assert result is obj  # method chaining with None
        assert obj.getBitNumber() is value  # None is a no-op

    def test_add_controlled_data_element(self):
        """
        Test addControlledDataElement append and None no-op.
        """
        obj = self._create_mask_bit()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-DATA-ELEMENT")
        ref.setValue("/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1")
        result = obj.addControlledDataElement(ref)
        assert result is obj  # method chaining
        assert obj.getControlledDataElements() == [ref]
        assert obj.getControlledDataElements()[0].getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/DID1/DataElement1"
        assert obj.getControlledDataElements()[0].getDest() == "DIAGNOSTIC-DATA-ELEMENT"

        result = obj.addControlledDataElement(None)
        assert result is obj  # method chaining with None
        assert obj.getControlledDataElements() == [ref]  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter/setter/adder docstrings carry the spec Note verbatim (setters/adder + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticControlEnableMaskBit.getBitNumber.__doc__) == self.BIT_NUMBER_NOTE
        assert inspect.cleandoc(DiagnosticControlEnableMaskBit.setBitNumber.__doc__) == (self.BIT_NUMBER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing bitNumber.")
        assert inspect.cleandoc(DiagnosticControlEnableMaskBit.getControlledDataElements.__doc__) == self.CONTROLLED_DATA_ELEMENT_NOTE
        assert inspect.cleandoc(DiagnosticControlEnableMaskBit.addControlledDataElement.__doc__) == (
            self.CONTROLLED_DATA_ELEMENT_NOTE + "\n\nA None value is a no-op and does not append a controlledDataElement."
        )


class TestDiagnosticPeriodicRate:
    """
    Test class for DiagnosticPeriodicRate functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.99, p.131
    """

    CLASS_NOTE = 'This represents the ability to define a periodic rate for the specification of the "read data by periodic ID" diagnostic service.'
    PERIOD_NOTE = "This represents the period of the DiagnosticPeriodicRate in seconds."
    PERIODIC_RATE_CATEGORY_NOTE = "This attribute represents the category of the periodic rate."

    def _create_periodic_rate(self) -> DiagnosticPeriodicRate:
        return DiagnosticPeriodicRate()

    def test_initialization(self):
        """
        Test that a new DiagnosticPeriodicRate initializes all attributes to their defaults.
        """
        obj = self._create_periodic_rate()

        assert obj.getPeriod() is None
        assert obj.getPeriodicRateCategory() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticPeriodicRate derives from ARObject (Table 4.99 Base).
        """
        assert issubclass(DiagnosticPeriodicRate, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticPeriodicRate.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticPeriodicRate.__init__.__doc__ is None

    def test_get_set_period(self):
        """
        Test getPeriod and setPeriod round-trip and None no-op.
        """
        obj = self._create_periodic_rate()

        value = TimeValue().setValue(0.5)
        result = obj.setPeriod(value)
        assert result is obj  # method chaining
        assert obj.getPeriod() is value
        assert obj.getPeriod().getValue() == 0.5

        result = obj.setPeriod(None)
        assert result is obj  # method chaining with None
        assert obj.getPeriod() is value  # None is a no-op

    def test_get_set_periodic_rate_category(self):
        """
        Test getPeriodicRateCategory and setPeriodicRateCategory round-trip and None no-op.
        """
        obj = self._create_periodic_rate()

        value = DiagnosticPeriodicRateCategoryEnum().setValue(DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_MEDIUM)
        result = obj.setPeriodicRateCategory(value)
        assert result is obj  # method chaining
        assert obj.getPeriodicRateCategory() is value
        assert obj.getPeriodicRateCategory().getValue() == DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_MEDIUM

        result = obj.setPeriodicRateCategory(None)
        assert result is obj  # method chaining with None
        assert obj.getPeriodicRateCategory() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticPeriodicRate.getPeriod.__doc__) == self.PERIOD_NOTE
        assert inspect.cleandoc(DiagnosticPeriodicRate.setPeriod.__doc__) == (self.PERIOD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing period.")
        assert inspect.cleandoc(DiagnosticPeriodicRate.getPeriodicRateCategory.__doc__) == self.PERIODIC_RATE_CATEGORY_NOTE
        assert inspect.cleandoc(DiagnosticPeriodicRate.setPeriodicRateCategory.__doc__) == (
            self.PERIODIC_RATE_CATEGORY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing periodicRateCategory."
        )


class TestDiagnosticEventWindow:
    """
    Test class for DiagnosticEventWindow functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.103, p.133
    """

    CLASS_NOTE = "This represents the ability to define the characteristics of the applicable event window"
    EVENT_WINDOW_TIME_NOTE = "This attribute clarifies the validity of the eventWindow"

    def _create_event_window(self) -> DiagnosticEventWindow:
        return DiagnosticEventWindow()

    def test_initialization(self):
        """
        Test that a new DiagnosticEventWindow initializes all attributes to their defaults.
        """
        obj = self._create_event_window()

        assert obj.getEventWindowTime() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticEventWindow derives from ARObject (Table 4.103 Base).
        """
        assert issubclass(DiagnosticEventWindow, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticEventWindow.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticEventWindow.__init__.__doc__ is None

    def test_get_set_event_window_time(self):
        """
        Test getEventWindowTime and setEventWindowTime round-trip and None no-op.
        """
        obj = self._create_event_window()

        value = DiagnosticEventWindowTimeEnum().setValue(DiagnosticEventWindowTimeEnum.INFINITE_TIME_TO_RESPONSE)
        result = obj.setEventWindowTime(value)
        assert result is obj  # method chaining
        assert obj.getEventWindowTime() is value
        assert obj.getEventWindowTime().getValue() == DiagnosticEventWindowTimeEnum.INFINITE_TIME_TO_RESPONSE

        result = obj.setEventWindowTime(None)
        assert result is obj  # method chaining with None
        assert obj.getEventWindowTime() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticEventWindow.getEventWindowTime.__doc__) == self.EVENT_WINDOW_TIME_NOTE
        assert inspect.cleandoc(DiagnosticEventWindow.setEventWindowTime.__doc__) == (self.EVENT_WINDOW_TIME_NOTE + "\n\nA None value is a no-op and does not overwrite an existing eventWindowTime.")


class TestDiagnosticParameterSupportInfo:
    """
    Test class for DiagnosticParameterSupportInfo functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.128, p.149
    """

    CLASS_NOTE = "This represents a way to define which bit of the supportInfo is representing this part of the PID"
    SUPPORT_INFO_BIT_NOTE = "defines the bit in the SupportInfo byte, which represents the PID DataElement pidSize / position / size. Unit: byte."

    def _create_support_info(self) -> DiagnosticParameterSupportInfo:
        return DiagnosticParameterSupportInfo()

    def test_initialization(self):
        """
        Test that a new DiagnosticParameterSupportInfo initializes all attributes to their defaults.
        """
        obj = self._create_support_info()

        assert obj.getSupportInfoBit() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticParameterSupportInfo derives from ARObject (Table 4.128 Base).
        """
        assert issubclass(DiagnosticParameterSupportInfo, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticParameterSupportInfo.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticParameterSupportInfo.__init__.__doc__ is None

    def test_get_set_support_info_bit(self):
        """
        Test getSupportInfoBit and setSupportInfoBit round-trip and None no-op.
        """
        obj = self._create_support_info()

        value = PositiveInteger()
        value.setValue("3")
        result = obj.setSupportInfoBit(value)
        assert result is obj  # method chaining
        assert obj.getSupportInfoBit() is value
        assert obj.getSupportInfoBit().getValue() == 3

        result = obj.setSupportInfoBit(None)
        assert result is obj  # method chaining with None
        assert obj.getSupportInfoBit() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticParameterSupportInfo.getSupportInfoBit.__doc__) == self.SUPPORT_INFO_BIT_NOTE
        assert inspect.cleandoc(DiagnosticParameterSupportInfo.setSupportInfoBit.__doc__) == (
            self.SUPPORT_INFO_BIT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing supportInfoBit."
        )


class TestDiagnosticSupportInfoByte:
    """
    Test class for DiagnosticSupportInfoByte functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.129, p.150
    """

    CLASS_NOTE = "This meta-class defines the support information (typically byte A) to declare the usability of the Data Elements within the so-called packeted PIDs (e.g. PID$68)."
    POSITION_NOTE = "This represents the position of the supportInfo in the PID. Unit: byte."
    SIZE_NOTE = "This represents the size of the supportInfo within the PID. Unit: byte."

    def _create_support_info_byte(self) -> DiagnosticSupportInfoByte:
        return DiagnosticSupportInfoByte()

    def test_initialization(self):
        """
        Test that a new DiagnosticSupportInfoByte initializes all attributes to their defaults.
        """
        obj = self._create_support_info_byte()

        assert obj.getPosition() is None
        assert obj.getSize() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticSupportInfoByte derives from ARObject (Table 4.129 Base).
        """
        assert issubclass(DiagnosticSupportInfoByte, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticSupportInfoByte.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticSupportInfoByte.__init__.__doc__ is None

    def test_get_set_position(self):
        """
        Test getPosition and setPosition round-trip and None no-op.
        """
        obj = self._create_support_info_byte()

        value = PositiveInteger()
        value.setValue("1")
        result = obj.setPosition(value)
        assert result is obj  # method chaining
        assert obj.getPosition() is value
        assert obj.getPosition().getValue() == 1

        result = obj.setPosition(None)
        assert result is obj  # method chaining with None
        assert obj.getPosition() is value  # None is a no-op

    def test_get_set_size(self):
        """
        Test getSize and setSize round-trip and None no-op.
        """
        obj = self._create_support_info_byte()

        value = PositiveInteger()
        value.setValue("2")
        result = obj.setSize(value)
        assert result is obj  # method chaining
        assert obj.getSize() is value
        assert obj.getSize().getValue() == 2

        result = obj.setSize(None)
        assert result is obj  # method chaining with None
        assert obj.getSize() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticSupportInfoByte.getPosition.__doc__) == self.POSITION_NOTE
        assert inspect.cleandoc(DiagnosticSupportInfoByte.setPosition.__doc__) == (self.POSITION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing position.")
        assert inspect.cleandoc(DiagnosticSupportInfoByte.getSize.__doc__) == self.SIZE_NOTE
        assert inspect.cleandoc(DiagnosticSupportInfoByte.setSize.__doc__) == (self.SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing size.")


class TestDiagnosticConnectedIndicator:
    """
    Test class for DiagnosticConnectedIndicator functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.152, p.167
    """

    CLASS_NOTE = "Description of indicators that are defined per DiagnosticEvent."
    BEHAVIOR_NOTE = "Behavior of the linked indicator."
    HEALING_CYCLE_NOTE = (
        "The deactivation of indicators per event is defined as healing of a diagnostic event. The operation cycle in which the warning indicator will be switched off is defined here."
    )
    HEALING_CYCLE_COUNTER_THRESHOLD_NOTE = "This attribute defines the number of healing cycles for the WarningIndicatorOffCriteria Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"
    INDICATOR_NOTE = "Reference to the used indicator."
    INDICATOR_FAILURE_CYCLE_COUNTER_THRESHOLD_NOTE = (
        "This attribute defines the number of failure cycles for the WarningIndicatorOnCriteria. Please note that this attribute is not relevant for the Adaptive Platform."
    )

    def _create_connected_indicator(self) -> DiagnosticConnectedIndicator:
        return DiagnosticConnectedIndicator()

    def test_initialization(self):
        """
        Test that a new DiagnosticConnectedIndicator initializes all attributes to their defaults.
        """
        obj = self._create_connected_indicator()

        assert obj.getBehavior() is None
        assert obj.getHealingCycleRef() is None
        assert obj.getHealingCycleCounterThreshold() is None
        assert obj.getIndicatorRef() is None
        assert obj.getIndicatorFailureCycleCounterThreshold() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticConnectedIndicator derives from ARObject (confirmed queue row Base; the spec Base chain's Referrable/Identifiable is unreachable from ArObject.py).
        """
        assert issubclass(DiagnosticConnectedIndicator, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticConnectedIndicator.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticConnectedIndicator.__init__.__doc__ is None

    def test_get_set_behavior(self):
        """
        Test getBehavior and setBehavior round-trip and None no-op.
        """
        obj = self._create_connected_indicator()

        value = DiagnosticConnectedIndicatorBehaviorEnum().setValue(DiagnosticConnectedIndicatorBehaviorEnum.BLINK_MODE)
        result = obj.setBehavior(value)
        assert result is obj  # method chaining
        assert obj.getBehavior() is value
        assert obj.getBehavior().getValue() == DiagnosticConnectedIndicatorBehaviorEnum.BLINK_MODE

        result = obj.setBehavior(None)
        assert result is obj  # method chaining with None
        assert obj.getBehavior() is value  # None is a no-op

    def test_get_set_healing_cycle_ref(self):
        """
        Test getHealingCycleRef and setHealingCycleRef round-trip and None no-op.
        """
        obj = self._create_connected_indicator()

        value = RefType().setValue("/Dem/DiagnosticOperationCycle")
        result = obj.setHealingCycleRef(value)
        assert result is obj  # method chaining
        assert obj.getHealingCycleRef() is value
        assert obj.getHealingCycleRef().getValue() == "/Dem/DiagnosticOperationCycle"

        result = obj.setHealingCycleRef(None)
        assert result is obj  # method chaining with None
        assert obj.getHealingCycleRef() is value  # None is a no-op

    def test_get_set_healing_cycle_counter_threshold(self):
        """
        Test getHealingCycleCounterThreshold and setHealingCycleCounterThreshold round-trip and None no-op.
        """
        obj = self._create_connected_indicator()

        value = PositiveInteger().setValue("3")
        result = obj.setHealingCycleCounterThreshold(value)
        assert result is obj  # method chaining
        assert obj.getHealingCycleCounterThreshold() is value
        assert obj.getHealingCycleCounterThreshold().getValue() == 3

        result = obj.setHealingCycleCounterThreshold(None)
        assert result is obj  # method chaining with None
        assert obj.getHealingCycleCounterThreshold() is value  # None is a no-op

    def test_get_set_indicator_ref(self):
        """
        Test getIndicatorRef and setIndicatorRef round-trip and None no-op.
        """
        obj = self._create_connected_indicator()

        value = RefType().setValue("/Dem/DiagnosticIndicator")
        result = obj.setIndicatorRef(value)
        assert result is obj  # method chaining
        assert obj.getIndicatorRef() is value
        assert obj.getIndicatorRef().getValue() == "/Dem/DiagnosticIndicator"

        result = obj.setIndicatorRef(None)
        assert result is obj  # method chaining with None
        assert obj.getIndicatorRef() is value  # None is a no-op

    def test_get_set_indicator_failure_cycle_counter_threshold(self):
        """
        Test getIndicatorFailureCycleCounterThreshold and setIndicatorFailureCycleCounterThreshold round-trip and None no-op.
        """
        obj = self._create_connected_indicator()

        value = PositiveInteger().setValue("2")
        result = obj.setIndicatorFailureCycleCounterThreshold(value)
        assert result is obj  # method chaining
        assert obj.getIndicatorFailureCycleCounterThreshold() is value
        assert obj.getIndicatorFailureCycleCounterThreshold().getValue() == 2

        result = obj.setIndicatorFailureCycleCounterThreshold(None)
        assert result is obj  # method chaining with None
        assert obj.getIndicatorFailureCycleCounterThreshold() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticConnectedIndicator.getBehavior.__doc__) == self.BEHAVIOR_NOTE
        assert inspect.cleandoc(DiagnosticConnectedIndicator.setBehavior.__doc__) == (self.BEHAVIOR_NOTE + "\n\nA None value is a no-op and does not overwrite an existing behavior.")
        assert inspect.cleandoc(DiagnosticConnectedIndicator.getHealingCycleRef.__doc__) == self.HEALING_CYCLE_NOTE
        assert inspect.cleandoc(DiagnosticConnectedIndicator.setHealingCycleRef.__doc__) == (
            self.HEALING_CYCLE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing healingCycleRef."
        )
        assert inspect.cleandoc(DiagnosticConnectedIndicator.getHealingCycleCounterThreshold.__doc__) == self.HEALING_CYCLE_COUNTER_THRESHOLD_NOTE
        assert inspect.cleandoc(DiagnosticConnectedIndicator.setHealingCycleCounterThreshold.__doc__) == (
            self.HEALING_CYCLE_COUNTER_THRESHOLD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing healingCycleCounterThreshold."
        )
        assert inspect.cleandoc(DiagnosticConnectedIndicator.getIndicatorRef.__doc__) == self.INDICATOR_NOTE
        assert inspect.cleandoc(DiagnosticConnectedIndicator.setIndicatorRef.__doc__) == (self.INDICATOR_NOTE + "\n\nA None value is a no-op and does not overwrite an existing indicatorRef.")
        assert inspect.cleandoc(DiagnosticConnectedIndicator.getIndicatorFailureCycleCounterThreshold.__doc__) == self.INDICATOR_FAILURE_CYCLE_COUNTER_THRESHOLD_NOTE
        assert inspect.cleandoc(DiagnosticConnectedIndicator.setIndicatorFailureCycleCounterThreshold.__doc__) == (
            self.INDICATOR_FAILURE_CYCLE_COUNTER_THRESHOLD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing indicatorFailureCycleCounterThreshold."
        )


class TestDiagnosticFunctionIdentifierInhibit:
    """
    Test class for DiagnosticFunctionIdentifierInhibit functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.215, p.216
    """

    CLASS_NOTE = "This meta-class represents the ability to define the inhibition of a specific function identifier within the Fim configuration. Tags: atp.recommendedPackage=DiagnosticFunctionIdentifierInhibits"
    FUNCTION_IDENTIFIER_NOTE = "This represents the corresponding function identifier."
    INHIBITION_MASK_NOTE = "This represents the value of the inhibition mask behavior."
    INHIBIT_SOURCE_NOTE = "This represents a collection of DiagnosticFunctionInhibitSource that contribute to the configuration of the enclosing DiagnosticFunctionIdentiferInhibit."

    def _create_inhibit(self) -> DiagnosticFunctionIdentifierInhibit:
        return DiagnosticFunctionIdentifierInhibit()

    def _create_inhibit_source(self) -> DiagnosticFunctionInhibitSource:
        return DiagnosticFunctionInhibitSource(AUTOSAR.getInstance(), "InhibitSource")

    def test_initialization(self):
        """
        Test that a new DiagnosticFunctionIdentifierInhibit initializes all attributes to their defaults.
        """
        obj = self._create_inhibit()

        assert obj.getFunctionIdentifierRef() is None
        assert obj.getInhibitionMask() is None
        assert obj.getInhibitSources() == []

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticFunctionIdentifierInhibit derives from ARObject (confirmed queue row Base; the spec Base chain's Referrable/Identifiable is unreachable from ArObject.py).
        """
        assert issubclass(DiagnosticFunctionIdentifierInhibit, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticFunctionIdentifierInhibit.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticFunctionIdentifierInhibit.__init__.__doc__ is None

    def test_get_set_function_identifier_ref(self):
        """
        Test getFunctionIdentifierRef and setFunctionIdentifierRef round-trip and None no-op.
        """
        obj = self._create_inhibit()

        value = RefType().setValue("/Fim/DiagnosticFunctionIdentifiers/FID1")
        result = obj.setFunctionIdentifierRef(value)
        assert result is obj  # method chaining
        assert obj.getFunctionIdentifierRef() is value
        assert obj.getFunctionIdentifierRef().getValue() == "/Fim/DiagnosticFunctionIdentifiers/FID1"

        result = obj.setFunctionIdentifierRef(None)
        assert result is obj  # method chaining with None
        assert obj.getFunctionIdentifierRef() is value  # None is a no-op

    def test_get_set_inhibition_mask(self):
        """
        Test getInhibitionMask and setInhibitionMask round-trip and None no-op.
        """
        obj = self._create_inhibit()

        value = DiagnosticInhibitionMaskEnum().setValue(DiagnosticInhibitionMaskEnum.TESTED_AND_FAILED)
        result = obj.setInhibitionMask(value)
        assert result is obj  # method chaining
        assert obj.getInhibitionMask() is value
        assert obj.getInhibitionMask().getValue() == DiagnosticInhibitionMaskEnum.TESTED_AND_FAILED

        result = obj.setInhibitionMask(None)
        assert result is obj  # method chaining with None
        assert obj.getInhibitionMask() is value  # None is a no-op

    def test_add_inhibit_source(self):
        """
        Test addInhibitSource appends to the collection and None is a no-op.
        """
        obj = self._create_inhibit()

        source = self._create_inhibit_source()
        result = obj.addInhibitSource(source)
        assert result is obj  # method chaining
        assert obj.getInhibitSources() == [source]

        result = obj.addInhibitSource(None)
        assert result is obj  # method chaining with None
        assert obj.getInhibitSources() == [source]  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticFunctionIdentifierInhibit.getFunctionIdentifierRef.__doc__) == self.FUNCTION_IDENTIFIER_NOTE
        assert inspect.cleandoc(DiagnosticFunctionIdentifierInhibit.setFunctionIdentifierRef.__doc__) == (
            self.FUNCTION_IDENTIFIER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing functionIdentifierRef."
        )
        assert inspect.cleandoc(DiagnosticFunctionIdentifierInhibit.getInhibitionMask.__doc__) == self.INHIBITION_MASK_NOTE
        assert inspect.cleandoc(DiagnosticFunctionIdentifierInhibit.setInhibitionMask.__doc__) == (
            self.INHIBITION_MASK_NOTE + "\n\nA None value is a no-op and does not overwrite an existing inhibitionMask."
        )
        assert inspect.cleandoc(DiagnosticFunctionIdentifierInhibit.addInhibitSource.__doc__) == (self.INHIBIT_SOURCE_NOTE + "\n\nA None value is a no-op and does not append an inhibitSource.")
        assert inspect.cleandoc(DiagnosticFunctionIdentifierInhibit.getInhibitSources.__doc__) == self.INHIBIT_SOURCE_NOTE


class TestDiagnosticIumprGroupIdentifier:
    """
    Test class for DiagnosticIumprGroupIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.210, p.211
    """

    CLASS_NOTE = "This meta-class provides the ability to the define the group identifier for an IumprGroup."
    GROUP_ID_NOTE = "This attribute shall be taken to define an identifier for the IUMPR group. Please note that the value of this identifier is driven by regulations outside the scope of AUTOSAR and can therefore not be limited to the set of characters suitable for a shortName. Stereotypes: atpIdentityContributor"

    def _create_identifier(self) -> DiagnosticIumprGroupIdentifier:
        return DiagnosticIumprGroupIdentifier()

    def test_initialization(self):
        """
        Test that a new DiagnosticIumprGroupIdentifier initializes all attributes to their defaults.
        """
        obj = self._create_identifier()

        assert obj.getGroupId() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticIumprGroupIdentifier derives from ARObject (spec Base row; ARObject is the most-derived reachable base — nested value container, not Identifiable).
        """
        assert issubclass(DiagnosticIumprGroupIdentifier, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticIumprGroupIdentifier.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticIumprGroupIdentifier.__init__.__doc__ is None

    def test_get_set_group_id(self):
        """
        Test getGroupId and setGroupId round-trip and None no-op.
        """
        obj = self._create_identifier()

        value = NameToken().setValue("IUMPR_GROUP_1")
        result = obj.setGroupId(value)
        assert result is obj  # method chaining
        assert obj.getGroupId() is value
        assert obj.getGroupId().getValue() == "IUMPR_GROUP_1"

        result = obj.setGroupId(None)
        assert result is obj  # method chaining with None
        assert obj.getGroupId() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticIumprGroupIdentifier.getGroupId.__doc__) == self.GROUP_ID_NOTE
        assert inspect.cleandoc(DiagnosticIumprGroupIdentifier.setGroupId.__doc__) == (self.GROUP_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing groupId.")


class ConcreteDiagnosticMemoryDestination(DiagnosticMemoryDestination):
    pass


class TestDiagnosticMemoryDestination:
    """
    Test class for DiagnosticMemoryDestination functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.167, p.182

    DiagnosticMemoryDestination is abstract (spec Class row marks it
    "(abstract)"; subclasses: DiagnosticMemoryDestinationPrimary,
    DiagnosticMemoryDestinationUserDefined — both queued later in Group25), so
    __init__ defaults and base accessors are exercised through the minimal
    concrete subclass ConcreteDiagnosticMemoryDestination (Rule 0006
    abstract-class clause). Its XML flows through the concrete subclass
    elements (XSD group DIAGNOSTIC-MEMORY-DESTINATION, AUTOSAR_00052.xsd
    l.39458), so the reusable reader/writer helpers are round-tripped in
    tests/test_armodel/parser/test_diagnostic_memory_destination.py and
    tests/test_armodel/writer/test_writer_diagnostic_memory_destination.py.
    The Base row's Identifiable branch is unreachable from ArObject.py —
    ARObject (nested value container) is the most-derived reachable base.
    memoryEntryStorageTrigger, statusBitHandlingTestFailedSinceLastClear and
    typeOfFreezeFrameRecordNumeration are typed by their spec enums, which are
    still stubs queued later in Group25 — tests construct them with the
    interim raw-literal shape until they gain their literals.
    """

    CLASS_NOTE = "This abstract meta-class represents a possible memory destination for a diagnostic event."
    AGING_REQUIRES_TESTED_CYCLE_NOTE = "Defines whether the aging cycle counter is processed every aging cycles or else only tested aging cycle are considered. If the attribute is set to TRUE: only tested aging cycle are considered for aging cycle counter. If the attribute is set to FALSE: aging cycle counter is processed every aging cycle. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination."
    CLEAR_DTC_LIMITATION_NOTE = "Defines the scope of the DEM_ClearDTC Api. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination."
    DTC_STATUS_AVAILABILITY_MASK_NOTE = "Mask for the supported DTC status bits by the Dem."
    EVENT_DISPLACEMENT_STRATEGY_NOTE = "This attribute defines, whether support for event displacement is enabled or not, and which displacement strategy is followed."
    MAX_NUMBER_OF_EVENT_ENTRIES_NOTE = "This attribute fixes the maximum number of event entries in the fault memory."
    MEMORY_ENTRY_STORAGE_TRIGGER_NOTE = "Describes the trigger to allocate an event memory entry."
    STATUS_BIT_HANDLING_TEST_FAILED_SINCE_LAST_CLEAR_NOTE = 'This attribute defines, whether the aging and displacement mechanism shall be applied to the "TestFailedSinceLastClear" status bits. On the classic platform, the value of this attribute has to be identical for each DiagnosticMemoryDestination.'
    STATUS_BIT_STORAGE_TEST_FAILED_NOTE = 'This parameter is used to activate/deactivate the permanent storage of the "TestFailed" status bits. true: storage activated false: storage deactivated'
    TYPE_OF_FREEZE_FRAME_RECORD_NUMERATION_NOTE = "This attribute defines the type of assigning freeze frame record numbers for event-specific freeze frame records."

    def _create_destination(self) -> DiagnosticMemoryDestination:
        return ConcreteDiagnosticMemoryDestination()

    def test_abstract_instantiation_blocked(self):
        """
        Test that instantiating the abstract DiagnosticMemoryDestination directly raises TypeError.
        """
        with pytest.raises(TypeError):
            DiagnosticMemoryDestination()

    def test_initialization(self):
        """
        Test that a concrete subclass initializes all attributes to their defaults.
        """
        obj = self._create_destination()

        assert obj.getAgingRequiresTestedCycle() is None
        assert obj.getClearDtcLimitation() is None
        assert obj.getDtcStatusAvailabilityMask() is None
        assert obj.getEventDisplacementStrategy() is None
        assert obj.getMaxNumberOfEventEntries() is None
        assert obj.getMemoryEntryStorageTrigger() is None
        assert obj.getStatusBitHandlingTestFailedSinceLastClear() is None
        assert obj.getStatusBitStorageTestFailed() is None
        assert obj.getTypeOfFreezeFrameRecordNumeration() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticMemoryDestination derives from ARObject (confirmed queue row Base; nested value container, not Identifiable).
        """
        assert issubclass(DiagnosticMemoryDestination, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticMemoryDestination.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticMemoryDestination.__init__.__doc__ is None

    def test_get_set_aging_requires_tested_cycle(self):
        """
        Test getAgingRequiresTestedCycle and setAgingRequiresTestedCycle round-trip and None no-op.
        """
        obj = self._create_destination()

        value = Boolean().setValue(True)
        result = obj.setAgingRequiresTestedCycle(value)
        assert result is obj  # method chaining
        assert obj.getAgingRequiresTestedCycle() is value
        assert obj.getAgingRequiresTestedCycle().value is True

        result = obj.setAgingRequiresTestedCycle(None)
        assert result is obj  # method chaining with None
        assert obj.getAgingRequiresTestedCycle() is value  # None is a no-op

    def test_get_set_clear_dtc_limitation(self):
        """
        Test getClearDtcLimitation and setClearDtcLimitation round-trip and None no-op.
        """
        obj = self._create_destination()

        value = DiagnosticClearDtcLimitationEnum().setValue(DiagnosticClearDtcLimitationEnum.ALL_SUPPORTED_DTCS)
        result = obj.setClearDtcLimitation(value)
        assert result is obj  # method chaining
        assert obj.getClearDtcLimitation() is value
        assert obj.getClearDtcLimitation().getValue() == DiagnosticClearDtcLimitationEnum.ALL_SUPPORTED_DTCS

        result = obj.setClearDtcLimitation(None)
        assert result is obj  # method chaining with None
        assert obj.getClearDtcLimitation() is value  # None is a no-op

    def test_get_set_dtc_status_availability_mask(self):
        """
        Test getDtcStatusAvailabilityMask and setDtcStatusAvailabilityMask round-trip and None no-op.
        """
        obj = self._create_destination()

        value = PositiveInteger().setValue(255)
        result = obj.setDtcStatusAvailabilityMask(value)
        assert result is obj  # method chaining
        assert obj.getDtcStatusAvailabilityMask() is value
        assert obj.getDtcStatusAvailabilityMask().getValue() == 255

        result = obj.setDtcStatusAvailabilityMask(None)
        assert result is obj  # method chaining with None
        assert obj.getDtcStatusAvailabilityMask() is value  # None is a no-op

    def test_get_set_event_displacement_strategy(self):
        """
        Test getEventDisplacementStrategy and setEventDisplacementStrategy round-trip and None no-op.
        """
        obj = self._create_destination()

        value = DiagnosticEventDisplacementStrategyEnum().setValue(DiagnosticEventDisplacementStrategyEnum.PRIO_OCC)
        result = obj.setEventDisplacementStrategy(value)
        assert result is obj  # method chaining
        assert obj.getEventDisplacementStrategy() is value
        assert obj.getEventDisplacementStrategy().getValue() == DiagnosticEventDisplacementStrategyEnum.PRIO_OCC

        result = obj.setEventDisplacementStrategy(None)
        assert result is obj  # method chaining with None
        assert obj.getEventDisplacementStrategy() is value  # None is a no-op

    def test_get_set_max_number_of_event_entries(self):
        """
        Test getMaxNumberOfEventEntries and setMaxNumberOfEventEntries round-trip and None no-op.
        """
        obj = self._create_destination()

        value = PositiveInteger().setValue(10)
        result = obj.setMaxNumberOfEventEntries(value)
        assert result is obj  # method chaining
        assert obj.getMaxNumberOfEventEntries() is value
        assert obj.getMaxNumberOfEventEntries().getValue() == 10

        result = obj.setMaxNumberOfEventEntries(None)
        assert result is obj  # method chaining with None
        assert obj.getMaxNumberOfEventEntries() is value  # None is a no-op

    def test_get_set_memory_entry_storage_trigger(self):
        """
        Test getMemoryEntryStorageTrigger and setMemoryEntryStorageTrigger round-trip and None no-op.
        """
        obj = self._create_destination()

        value = DiagnosticMemoryEntryStorageTriggerEnum().setValue(DiagnosticMemoryEntryStorageTriggerEnum.CONFIRMED)
        result = obj.setMemoryEntryStorageTrigger(value)
        assert result is obj  # method chaining
        assert obj.getMemoryEntryStorageTrigger() is value
        assert obj.getMemoryEntryStorageTrigger().getValue() == "CONFIRMED"

        result = obj.setMemoryEntryStorageTrigger(None)
        assert result is obj  # method chaining with None
        assert obj.getMemoryEntryStorageTrigger() is value  # None is a no-op

    def test_get_set_status_bit_handling_test_failed_since_last_clear(self):
        """
        Test getStatusBitHandlingTestFailedSinceLastClear and setStatusBitHandlingTestFailedSinceLastClear round-trip and None no-op.
        """
        obj = self._create_destination()

        value = DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum().setValue(DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum.STATUS_BIT_NORMAL)
        result = obj.setStatusBitHandlingTestFailedSinceLastClear(value)
        assert result is obj  # method chaining
        assert obj.getStatusBitHandlingTestFailedSinceLastClear() is value
        assert obj.getStatusBitHandlingTestFailedSinceLastClear().getValue() == DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum.STATUS_BIT_NORMAL

        result = obj.setStatusBitHandlingTestFailedSinceLastClear(None)
        assert result is obj  # method chaining with None
        assert obj.getStatusBitHandlingTestFailedSinceLastClear() is value  # None is a no-op

    def test_get_set_status_bit_storage_test_failed(self):
        """
        Test getStatusBitStorageTestFailed and setStatusBitStorageTestFailed round-trip and None no-op.
        """
        obj = self._create_destination()

        value = Boolean().setValue(False)
        result = obj.setStatusBitStorageTestFailed(value)
        assert result is obj  # method chaining
        assert obj.getStatusBitStorageTestFailed() is value
        assert obj.getStatusBitStorageTestFailed().value is False

        result = obj.setStatusBitStorageTestFailed(None)
        assert result is obj  # method chaining with None
        assert obj.getStatusBitStorageTestFailed() is value  # None is a no-op

    def test_get_set_type_of_freeze_frame_record_numeration(self):
        """
        Test getTypeOfFreezeFrameRecordNumeration and setTypeOfFreezeFrameRecordNumeration round-trip and None no-op.
        """
        obj = self._create_destination()

        value = DiagnosticTypeOfFreezeFrameRecordNumerationEnum().setValue(DiagnosticTypeOfFreezeFrameRecordNumerationEnum.CALCULATED)
        result = obj.setTypeOfFreezeFrameRecordNumeration(value)
        assert result is obj  # method chaining
        assert obj.getTypeOfFreezeFrameRecordNumeration() is value
        assert obj.getTypeOfFreezeFrameRecordNumeration().getValue() == DiagnosticTypeOfFreezeFrameRecordNumerationEnum.CALCULATED

        result = obj.setTypeOfFreezeFrameRecordNumeration(None)
        assert result is obj  # method chaining with None
        assert obj.getTypeOfFreezeFrameRecordNumeration() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticMemoryDestination.getAgingRequiresTestedCycle.__doc__) == self.AGING_REQUIRES_TESTED_CYCLE_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestination.setAgingRequiresTestedCycle.__doc__) == (
            self.AGING_REQUIRES_TESTED_CYCLE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing agingRequiresTestedCycle."
        )
        assert inspect.cleandoc(DiagnosticMemoryDestination.getClearDtcLimitation.__doc__) == self.CLEAR_DTC_LIMITATION_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestination.setClearDtcLimitation.__doc__) == (
            self.CLEAR_DTC_LIMITATION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing clearDtcLimitation."
        )
        assert inspect.cleandoc(DiagnosticMemoryDestination.getDtcStatusAvailabilityMask.__doc__) == self.DTC_STATUS_AVAILABILITY_MASK_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestination.setDtcStatusAvailabilityMask.__doc__) == (
            self.DTC_STATUS_AVAILABILITY_MASK_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dtcStatusAvailabilityMask."
        )
        assert inspect.cleandoc(DiagnosticMemoryDestination.getEventDisplacementStrategy.__doc__) == self.EVENT_DISPLACEMENT_STRATEGY_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestination.setEventDisplacementStrategy.__doc__) == (
            self.EVENT_DISPLACEMENT_STRATEGY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing eventDisplacementStrategy."
        )
        assert inspect.cleandoc(DiagnosticMemoryDestination.getMaxNumberOfEventEntries.__doc__) == self.MAX_NUMBER_OF_EVENT_ENTRIES_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestination.setMaxNumberOfEventEntries.__doc__) == (
            self.MAX_NUMBER_OF_EVENT_ENTRIES_NOTE + "\n\nA None value is a no-op and does not overwrite an existing maxNumberOfEventEntries."
        )
        assert inspect.cleandoc(DiagnosticMemoryDestination.getMemoryEntryStorageTrigger.__doc__) == self.MEMORY_ENTRY_STORAGE_TRIGGER_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestination.setMemoryEntryStorageTrigger.__doc__) == (
            self.MEMORY_ENTRY_STORAGE_TRIGGER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing memoryEntryStorageTrigger."
        )
        assert inspect.cleandoc(DiagnosticMemoryDestination.getStatusBitHandlingTestFailedSinceLastClear.__doc__) == self.STATUS_BIT_HANDLING_TEST_FAILED_SINCE_LAST_CLEAR_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestination.setStatusBitHandlingTestFailedSinceLastClear.__doc__) == (
            self.STATUS_BIT_HANDLING_TEST_FAILED_SINCE_LAST_CLEAR_NOTE + "\n\nA None value is a no-op and does not overwrite an existing statusBitHandlingTestFailedSinceLastClear."
        )
        assert inspect.cleandoc(DiagnosticMemoryDestination.getStatusBitStorageTestFailed.__doc__) == self.STATUS_BIT_STORAGE_TEST_FAILED_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestination.setStatusBitStorageTestFailed.__doc__) == (
            self.STATUS_BIT_STORAGE_TEST_FAILED_NOTE + "\n\nA None value is a no-op and does not overwrite an existing statusBitStorageTestFailed."
        )
        assert inspect.cleandoc(DiagnosticMemoryDestination.getTypeOfFreezeFrameRecordNumeration.__doc__) == self.TYPE_OF_FREEZE_FRAME_RECORD_NUMERATION_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestination.setTypeOfFreezeFrameRecordNumeration.__doc__) == (
            self.TYPE_OF_FREEZE_FRAME_RECORD_NUMERATION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing typeOfFreezeFrameRecordNumeration."
        )


class TestDiagnosticMemoryDestinationUserDefined:
    """
    Test class for DiagnosticMemoryDestinationUserDefined functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.174, p.185

    DiagnosticMemoryDestinationUserDefined is the concrete ARObject-homed branch
    of the abstract DiagnosticMemoryDestination (Table 4.167, synced in
    ArObject.py): the class derives directly from the base and inherits its nine
    attributes, adding its own authRole reference collection (* ref, XSD wrapper
    AUTH-ROLE-REFS with AUTH-ROLE-REF entries) and memoryId attribute (XSD group
    DIAGNOSTIC-MEMORY-DESTINATION-USER-DEFINED, AUTOSAR_00052.xsd l.39699). The
    XSD's AUTHENTICATION-ROLE-REF element carries atp.Status="removed" and is not
    modeled (Rule 0015).
    """

    CLASS_NOTE = "This represents a user-defined memory for a diagnostic event. Tags: atp.recommendedPackage=DiagnosticMemoryDestinations"
    AUTH_ROLE_NOTE = "This reference identifies the collection of applicable DiagnosticAuthRole Stereotypes: atpSplitable Tags: atp.Splitkey=authRole"
    MEMORY_ID_NOTE = "This represents the identifier of the user-defined memory."

    def _make_obj(self) -> DiagnosticMemoryDestinationUserDefined:
        return DiagnosticMemoryDestinationUserDefined()

    def test_initialization(self):
        """
        Test that the concrete class instantiates with its own and the inherited base defaults.
        """
        obj = self._make_obj()

        assert isinstance(obj, DiagnosticMemoryDestinationUserDefined)
        assert isinstance(obj, DiagnosticMemoryDestination)
        assert isinstance(obj, ARObject)
        assert obj.getAuthRoleRefs() == []
        assert obj.getMemoryId() is None
        assert obj.getAgingRequiresTestedCycle() is None
        assert obj.getClearDtcLimitation() is None
        assert obj.getDtcStatusAvailabilityMask() is None
        assert obj.getEventDisplacementStrategy() is None
        assert obj.getMaxNumberOfEventEntries() is None
        assert obj.getMemoryEntryStorageTrigger() is None
        assert obj.getStatusBitHandlingTestFailedSinceLastClear() is None
        assert obj.getStatusBitStorageTestFailed() is None
        assert obj.getTypeOfFreezeFrameRecordNumeration() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticMemoryDestinationUserDefined.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticMemoryDestinationUserDefined.__init__.__doc__ is None

    def test_add_auth_role_ref(self):
        """
        Test addAuthRoleRef append and None no-op.
        """
        obj = self._make_obj()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-AUTH-ROLE")
        ref.setValue("/AUTOSAR/DiagnosticAuthRoles/AuthRole1")
        result = obj.addAuthRoleRef(ref)
        assert result is obj  # method chaining
        assert obj.getAuthRoleRefs() == [ref]
        assert obj.getAuthRoleRefs()[0].getValue() == "/AUTOSAR/DiagnosticAuthRoles/AuthRole1"
        assert obj.getAuthRoleRefs()[0].getDest() == "DIAGNOSTIC-AUTH-ROLE"

        ref2 = RefType()
        ref2.setDest("DIAGNOSTIC-AUTH-ROLE")
        ref2.setValue("/AUTOSAR/DiagnosticAuthRoles/AuthRole2")
        obj.addAuthRoleRef(ref2)
        assert obj.getAuthRoleRefs() == [ref, ref2]

        result = obj.addAuthRoleRef(None)
        assert result is obj  # method chaining with None
        assert obj.getAuthRoleRefs() == [ref, ref2]  # None is a no-op

    def test_get_set_memory_id(self):
        """
        Test getMemoryId and setMemoryId round-trip and None no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger().setValue(1)
        result = obj.setMemoryId(value)
        assert result is obj  # method chaining
        assert obj.getMemoryId() is value
        assert obj.getMemoryId().getValue() == 1

        result = obj.setMemoryId(None)
        assert result is obj  # method chaining with None
        assert obj.getMemoryId() is value  # None is a no-op

    def test_get_set_inherited_attribute(self):
        """
        Spot-checks the inherited base attribute maxNumberOfEventEntries (Table 4.167); None is a no-op.
        """
        obj = self._make_obj()

        value = PositiveInteger().setValue(10)
        result = obj.setMaxNumberOfEventEntries(value)
        assert result is obj  # method chaining
        assert obj.getMaxNumberOfEventEntries() is value
        assert obj.getMaxNumberOfEventEntries().getValue() == 10

        result = obj.setMaxNumberOfEventEntries(None)
        assert result is obj  # method chaining with None
        assert obj.getMaxNumberOfEventEntries() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter/setter/adder docstrings carry the spec Note verbatim (setters/adder + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticMemoryDestinationUserDefined.addAuthRoleRef.__doc__) == self.AUTH_ROLE_NOTE + "\n\nA None value is a no-op and does not extend the authRoleRefs list."
        assert inspect.cleandoc(DiagnosticMemoryDestinationUserDefined.getAuthRoleRefs.__doc__) == self.AUTH_ROLE_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestinationUserDefined.getMemoryId.__doc__) == self.MEMORY_ID_NOTE
        assert inspect.cleandoc(DiagnosticMemoryDestinationUserDefined.setMemoryId.__doc__) == (self.MEMORY_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing memoryId.")


class TestDiagnosticTestIdentifier:
    """
    Test class for DiagnosticTestIdentifier functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.203, p.205
    """

    CLASS_NOTE = "This meta-class represents the ability to create a diagnostic test identifier."
    ID_NOTE = "This represents the numerical id associated with the diagnostic test identifier. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"
    UAS_ID_NOTE = "This represents the unit and scaling Id of the diagnostic test result. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"

    def _create_identifier(self) -> DiagnosticTestIdentifier:
        return DiagnosticTestIdentifier()

    def test_initialization(self):
        """
        Test that a new DiagnosticTestIdentifier initializes all attributes to their defaults.
        """
        obj = self._create_identifier()

        assert obj.getId() is None
        assert obj.getUasId() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticTestIdentifier derives from ARObject (spec Base row; ARObject is the most-derived reachable base — nested value container, not Identifiable).
        """
        assert issubclass(DiagnosticTestIdentifier, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticTestIdentifier.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTestIdentifier.__init__.__doc__ is None

    def test_get_set_id(self):
        """
        Test getId and setId round-trip and None no-op.
        """
        obj = self._create_identifier()

        value = PositiveInteger().setValue("30511")
        result = obj.setId(value)
        assert result is obj  # method chaining
        assert obj.getId() is value
        assert obj.getId().getValue() == 30511

        result = obj.setId(None)
        assert result is obj  # method chaining with None
        assert obj.getId() is value  # None is a no-op

    def test_get_set_uas_id(self):
        """
        Test getUasId and setUasId round-trip and None no-op.
        """
        obj = self._create_identifier()

        value = PositiveInteger().setValue("42")
        result = obj.setUasId(value)
        assert result is obj  # method chaining
        assert obj.getUasId() is value
        assert obj.getUasId().getValue() == 42

        result = obj.setUasId(None)
        assert result is obj  # method chaining with None
        assert obj.getUasId() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticTestIdentifier.getId.__doc__) == self.ID_NOTE
        assert inspect.cleandoc(DiagnosticTestIdentifier.setId.__doc__) == (self.ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing id.")
        assert inspect.cleandoc(DiagnosticTestIdentifier.getUasId.__doc__) == self.UAS_ID_NOTE
        assert inspect.cleandoc(DiagnosticTestIdentifier.setUasId.__doc__) == (self.UAS_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing uasId.")


class TestDiagnosticTroubleCodeObd:
    """
    Test class for DiagnosticTroubleCodeObd functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.159, p.175
    """

    CLASS_NOTE = "This element is used to define OBD-relevant DTCs. Tags: atp.recommendedPackage=DiagnosticTroubleCodes"
    CONSIDER_PTO_STATUS_NOTE = (
        "This attribute describes the affection of the event by the Dem PTO handling.\n\n"
        "true: the event is affected by the Dem PTO handling.\n\n"
        "false: the event is not affected by the Dem PTO handling."
    )
    DTC_PROPS_REF_NOTE = "Defined properties associated with the DemDTC."
    EVENT_READINESS_GROUP_NOTE = "This aggregation allows for the variant definition of the attribute eventObdReadinessGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=eventReadinessGroup.eventObdReadiness Group, eventReadinessGroup.variationPoint.shortLabel vh.latestBindingTime=postBuild"
    OBD_DTC_VALUE_NOTE = "Unique Diagnostic Trouble Code value for OBD. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"

    def _create_trouble_code(self) -> DiagnosticTroubleCodeObd:
        return DiagnosticTroubleCodeObd()

    def test_initialization(self):
        """
        Test that a new DiagnosticTroubleCodeObd initializes all attributes to their defaults.
        """
        obj = self._create_trouble_code()

        assert obj.getConsiderPtoStatus() is None
        assert obj.getDtcPropsRef() is None
        assert obj.getEventReadinessGroup() is None
        assert obj.getObdDtcValue() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticTroubleCodeObd derives from ARObject (confirmed queue row; ARObject is the most-derived reachable base — nested value container, not Identifiable).
        """
        assert issubclass(DiagnosticTroubleCodeObd, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticTroubleCodeObd.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTroubleCodeObd.__init__.__doc__ is None

    def test_get_set_consider_pto_status(self):
        """
        Test getConsiderPtoStatus and setConsiderPtoStatus round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        value = Boolean().setValue(True)
        result = obj.setConsiderPtoStatus(value)
        assert result is obj  # method chaining
        assert obj.getConsiderPtoStatus() is value
        assert obj.getConsiderPtoStatus().getValue() is True

        result = obj.setConsiderPtoStatus(None)
        assert result is obj  # method chaining with None
        assert obj.getConsiderPtoStatus() is value  # None is a no-op

    def test_get_set_dtc_props_ref(self):
        """
        Test getDtcPropsRef and setDtcPropsRef round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-TROUBLE-CODE-PROPS")
        ref.setValue("/AUTOSAR/DiagnosticTroubleCodeProps/DtcProps1")
        result = obj.setDtcPropsRef(ref)
        assert result is obj  # method chaining
        assert obj.getDtcPropsRef() is ref
        assert obj.getDtcPropsRef().getValue() == "/AUTOSAR/DiagnosticTroubleCodeProps/DtcProps1"
        assert obj.getDtcPropsRef().getDest() == "DIAGNOSTIC-TROUBLE-CODE-PROPS"

        result = obj.setDtcPropsRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDtcPropsRef() is ref  # None is a no-op

    def test_get_set_event_readiness_group(self):
        """
        Test getEventReadinessGroup and setEventReadinessGroup round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        value = EventObdReadinessGroup()
        result = obj.setEventReadinessGroup(value)
        assert result is obj  # method chaining
        assert obj.getEventReadinessGroup() is value

        result = obj.setEventReadinessGroup(None)
        assert result is obj  # method chaining with None
        assert obj.getEventReadinessGroup() is value  # None is a no-op

    def test_get_set_obd_dtc_value(self):
        """
        Test getObdDtcValue and setObdDtcValue round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        value = PositiveInteger().setValue(30511)
        result = obj.setObdDtcValue(value)
        assert result is obj  # method chaining
        assert obj.getObdDtcValue() is value
        assert obj.getObdDtcValue().getValue() == 30511

        result = obj.setObdDtcValue(None)
        assert result is obj  # method chaining with None
        assert obj.getObdDtcValue() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticTroubleCodeObd.getConsiderPtoStatus.__doc__) == self.CONSIDER_PTO_STATUS_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeObd.setConsiderPtoStatus.__doc__) == (
            self.CONSIDER_PTO_STATUS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing considerPtoStatus."
        )
        assert inspect.cleandoc(DiagnosticTroubleCodeObd.getDtcPropsRef.__doc__) == self.DTC_PROPS_REF_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeObd.setDtcPropsRef.__doc__) == (self.DTC_PROPS_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dtcProps reference.")
        assert inspect.cleandoc(DiagnosticTroubleCodeObd.getEventReadinessGroup.__doc__) == self.EVENT_READINESS_GROUP_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeObd.setEventReadinessGroup.__doc__) == (
            self.EVENT_READINESS_GROUP_NOTE + "\n\nA None value is a no-op and does not overwrite an existing eventReadinessGroup."
        )
        assert inspect.cleandoc(DiagnosticTroubleCodeObd.getObdDtcValue.__doc__) == self.OBD_DTC_VALUE_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeObd.setObdDtcValue.__doc__) == (self.OBD_DTC_VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing obdDtcValue.")


class TestDiagnosticTroubleCodeObdPendingReferences:
    """
    Test class for the still-stub reference targets of DiagnosticTroubleCodeObd.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.159, p.175

    DiagnosticTroubleCodeProps (Table 4.175) and EventObdReadinessGroup (Table 4.160)
    are queued later in Group25 and still empty stubs; the typed fields reference them
    directly (same module, ArObject.py).
    """

    def test_reference_targets_are_stub_classes(self):
        """
        Test that the referenced types exist and are ARObject-family stubs.
        """
        assert issubclass(DiagnosticTroubleCodeProps, ARObject)
        assert issubclass(EventObdReadinessGroup, ARObject)


class TestDiagnosticTroubleCodeProps:
    """
    Test class for DiagnosticTroubleCodeProps functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.175, p.186
    """

    CLASS_NOTE = "This element defines common Dtc properties that can be reused by different non OBD-relevant DTCs. Tags: atp.recommendedPackage=DiagnosticTroubleCodePropss"
    AGING_REF_NOTE = "Reference to an aging algorithm in case that an aging/ unlearning of the event is allowed. Stereotypes: atpSplitable Tags: atp.Splitkey=aging"
    DIAGNOSTIC_MEMORY_REF_NOTE = "Reference to the applicable DiagnosticMemory Destination. Stereotypes: atpSplitable Tags: atp.Splitkey=diagnosticMemory"
    EXTENDED_DATA_RECORD_NOTE = "Defines the links to an extended data class sampler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=extendedDataRecord.diagnosticExtended DataRecord, extendedDataRecord.variationPoint.short Label vh.latestBindingTime=preCompileTime"
    FREEZE_FRAME_NOTE = "Define the links to a freeze frame class sampler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=freezeFrame.diagnosticFreezeFrame, freeze Frame.variationPoint.shortLabel vh.latestBindingTime=preCompileTime"
    IMMEDIATE_NV_DATA_STORAGE_NOTE = 'Change description for Class immediateNvDataStorage in table "Table A.111: DiagnosticTroubleCodeProps": Switch to enable immediate storage triggering of an according event memory entry persistently to NVRAM. true: immediate non-volatile storage triggering on first occurrence and shutdown. false: immediate non-volatile storage triggering on shutdown.'
    LEGISLATED_FREEZE_FRAME_CONTENT_UDS_OBD_REF_NOTE = "This reference identifies the layout of legislated freeze frames used for emission related diagnostics over the UDS protocol such as OBDonUDS or WWH-OBD. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=legislatedFreezeFrameContentUds Obd.diagnosticDataIdentifierSet, legislatedFreezeFrame ContentUdsObd.variationPoint.shortLabel vh.latestBindingTime=preCompileTime"
    MAX_NUMBER_FREEZE_FRAME_RECORDS_NOTE = (
        "This attribute defines the number of according freeze frame records, which can maximal be stored for this event. Therefore all these freeze frame records have the same freeze frame class."
    )
    PRIORITY_NOTE = "Priority of the event, in view of full event buffer. A lower value means higher priority. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"
    SIGNIFICANCE_NOTE = "Significance of the event, which indicates additional information concerning fault classification and resolution."
    SNAPSHOT_RECORD_CONTENT_REF_NOTE = "This represents the freeze frame layout as a set of DIDs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=snapshotRecordContent.diagnosticData IdentifierSet, snapshotRecordContent.variationPoint.short Label vh.latestBindingTime=preCompileTime"

    def _create_props(self) -> DiagnosticTroubleCodeProps:
        return DiagnosticTroubleCodeProps()

    def test_initialization(self):
        """
        Test that a new DiagnosticTroubleCodeProps initializes all attributes to their defaults.
        """
        obj = self._create_props()

        assert obj.getAgingRef() is None
        assert obj.getDiagnosticMemoryRef() is None
        assert obj.getExtendedDataRecordRefs() == []
        assert obj.getFreezeFrameRefs() == []
        assert obj.getImmediateNvDataStorage() is None
        assert obj.getLegislatedFreezeFrameContentUdsObdRef() is None
        assert obj.getMaxNumberFreezeFrameRecords() is None
        assert obj.getPriority() is None
        assert obj.getSignificance() is None
        assert obj.getSnapshotRecordContentRef() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticTroubleCodeProps derives from ARObject (confirmed queue row; ARObject is the most-derived reachable base — nested value container, not Identifiable).
        """
        assert issubclass(DiagnosticTroubleCodeProps, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTroubleCodeProps.__init__.__doc__ is None

    def test_get_set_aging_ref(self):
        """
        Test getAgingRef and setAgingRef round-trip and None no-op.
        """
        obj = self._create_props()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-AGING")
        ref.setValue("/AUTOSAR/DiagnosticAgings/Aging1")
        result = obj.setAgingRef(ref)
        assert result is obj  # method chaining
        assert obj.getAgingRef() is ref
        assert obj.getAgingRef().getValue() == "/AUTOSAR/DiagnosticAgings/Aging1"
        assert obj.getAgingRef().getDest() == "DIAGNOSTIC-AGING"

        result = obj.setAgingRef(None)
        assert result is obj  # method chaining with None
        assert obj.getAgingRef() is ref  # None is a no-op

    def test_get_set_diagnostic_memory_ref(self):
        """
        Test getDiagnosticMemoryRef and setDiagnosticMemoryRef round-trip and None no-op.
        """
        obj = self._create_props()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-MEMORY-DESTINATION-USER-DEFINED")
        ref.setValue("/AUTOSAR/DiagnosticMemoryDestinations/Memory1")
        result = obj.setDiagnosticMemoryRef(ref)
        assert result is obj  # method chaining
        assert obj.getDiagnosticMemoryRef() is ref
        assert obj.getDiagnosticMemoryRef().getValue() == "/AUTOSAR/DiagnosticMemoryDestinations/Memory1"
        assert obj.getDiagnosticMemoryRef().getDest() == "DIAGNOSTIC-MEMORY-DESTINATION-USER-DEFINED"

        result = obj.setDiagnosticMemoryRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDiagnosticMemoryRef() is ref  # None is a no-op

    def test_add_get_extended_data_record_refs(self):
        """
        Test addExtendedDataRecordRef append and None no-op.
        """
        obj = self._create_props()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-EXTENDED-DATA-RECORD")
        ref.setValue("/AUTOSAR/DiagnosticExtendedDataRecords/Edr1")
        result = obj.addExtendedDataRecordRef(ref)
        assert result is obj  # method chaining
        assert obj.getExtendedDataRecordRefs() == [ref]
        assert obj.getExtendedDataRecordRefs()[0].getValue() == "/AUTOSAR/DiagnosticExtendedDataRecords/Edr1"
        assert obj.getExtendedDataRecordRefs()[0].getDest() == "DIAGNOSTIC-EXTENDED-DATA-RECORD"

        ref2 = RefType()
        ref2.setDest("DIAGNOSTIC-EXTENDED-DATA-RECORD")
        ref2.setValue("/AUTOSAR/DiagnosticExtendedDataRecords/Edr2")
        obj.addExtendedDataRecordRef(ref2)
        assert obj.getExtendedDataRecordRefs() == [ref, ref2]

        result = obj.addExtendedDataRecordRef(None)
        assert result is obj  # method chaining with None
        assert obj.getExtendedDataRecordRefs() == [ref, ref2]  # None is a no-op

    def test_add_get_freeze_frame_refs(self):
        """
        Test addFreezeFrameRef append and None no-op.
        """
        obj = self._create_props()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-FREEZE-FRAME")
        ref.setValue("/AUTOSAR/DiagnosticFreezeFrames/Ff1")
        result = obj.addFreezeFrameRef(ref)
        assert result is obj  # method chaining
        assert obj.getFreezeFrameRefs() == [ref]
        assert obj.getFreezeFrameRefs()[0].getValue() == "/AUTOSAR/DiagnosticFreezeFrames/Ff1"
        assert obj.getFreezeFrameRefs()[0].getDest() == "DIAGNOSTIC-FREEZE-FRAME"

        ref2 = RefType()
        ref2.setDest("DIAGNOSTIC-FREEZE-FRAME")
        ref2.setValue("/AUTOSAR/DiagnosticFreezeFrames/Ff2")
        obj.addFreezeFrameRef(ref2)
        assert obj.getFreezeFrameRefs() == [ref, ref2]

        result = obj.addFreezeFrameRef(None)
        assert result is obj  # method chaining with None
        assert obj.getFreezeFrameRefs() == [ref, ref2]  # None is a no-op

    def test_get_set_immediate_nv_data_storage(self):
        """
        Test getImmediateNvDataStorage and setImmediateNvDataStorage round-trip and None no-op.
        """
        obj = self._create_props()

        value = Boolean().setValue(True)
        result = obj.setImmediateNvDataStorage(value)
        assert result is obj  # method chaining
        assert obj.getImmediateNvDataStorage() is value
        assert obj.getImmediateNvDataStorage().getValue() is True

        result = obj.setImmediateNvDataStorage(None)
        assert result is obj  # method chaining with None
        assert obj.getImmediateNvDataStorage() is value  # None is a no-op

    def test_get_set_legislated_freeze_frame_content_uds_obd_ref(self):
        """
        Test getLegislatedFreezeFrameContentUdsObdRef and setLegislatedFreezeFrameContentUdsObdRef round-trip and None no-op.
        """
        obj = self._create_props()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-DATA-IDENTIFIER-SET")
        ref.setValue("/AUTOSAR/DiagnosticDataIdentifierSets/DidSet1")
        result = obj.setLegislatedFreezeFrameContentUdsObdRef(ref)
        assert result is obj  # method chaining
        assert obj.getLegislatedFreezeFrameContentUdsObdRef() is ref
        assert obj.getLegislatedFreezeFrameContentUdsObdRef().getValue() == "/AUTOSAR/DiagnosticDataIdentifierSets/DidSet1"
        assert obj.getLegislatedFreezeFrameContentUdsObdRef().getDest() == "DIAGNOSTIC-DATA-IDENTIFIER-SET"

        result = obj.setLegislatedFreezeFrameContentUdsObdRef(None)
        assert result is obj  # method chaining with None
        assert obj.getLegislatedFreezeFrameContentUdsObdRef() is ref  # None is a no-op

    def test_get_set_max_number_freeze_frame_records(self):
        """
        Test getMaxNumberFreezeFrameRecords and setMaxNumberFreezeFrameRecords round-trip and None no-op.
        """
        obj = self._create_props()

        value = PositiveInteger().setValue(3)
        result = obj.setMaxNumberFreezeFrameRecords(value)
        assert result is obj  # method chaining
        assert obj.getMaxNumberFreezeFrameRecords() is value
        assert obj.getMaxNumberFreezeFrameRecords().getValue() == 3

        result = obj.setMaxNumberFreezeFrameRecords(None)
        assert result is obj  # method chaining with None
        assert obj.getMaxNumberFreezeFrameRecords() is value  # None is a no-op

    def test_get_set_priority(self):
        """
        Test getPriority and setPriority round-trip and None no-op.
        """
        obj = self._create_props()

        value = PositiveInteger().setValue(10)
        result = obj.setPriority(value)
        assert result is obj  # method chaining
        assert obj.getPriority() is value
        assert obj.getPriority().getValue() == 10

        result = obj.setPriority(None)
        assert result is obj  # method chaining with None
        assert obj.getPriority() is value  # None is a no-op

    def test_get_set_significance(self):
        """
        Test getSignificance and setSignificance round-trip and None no-op.
        """
        obj = self._create_props()

        value = DiagnosticSignificanceEnum().setValue(DiagnosticSignificanceEnum.FAULT)
        result = obj.setSignificance(value)
        assert result is obj  # method chaining
        assert obj.getSignificance() is value
        assert obj.getSignificance().getValue() == DiagnosticSignificanceEnum.FAULT

        result = obj.setSignificance(None)
        assert result is obj  # method chaining with None
        assert obj.getSignificance() is value  # None is a no-op

    def test_get_set_snapshot_record_content_ref(self):
        """
        Test getSnapshotRecordContentRef and setSnapshotRecordContentRef round-trip and None no-op.
        """
        obj = self._create_props()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-DATA-IDENTIFIER-SET")
        ref.setValue("/AUTOSAR/DiagnosticDataIdentifierSets/DidSet2")
        result = obj.setSnapshotRecordContentRef(ref)
        assert result is obj  # method chaining
        assert obj.getSnapshotRecordContentRef() is ref
        assert obj.getSnapshotRecordContentRef().getValue() == "/AUTOSAR/DiagnosticDataIdentifierSets/DidSet2"
        assert obj.getSnapshotRecordContentRef().getDest() == "DIAGNOSTIC-DATA-IDENTIFIER-SET"

        result = obj.setSnapshotRecordContentRef(None)
        assert result is obj  # method chaining with None
        assert obj.getSnapshotRecordContentRef() is ref  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter/setter/adder docstrings carry the spec Note verbatim (setters/adders append the None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.getAgingRef.__doc__) == self.AGING_REF_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.setAgingRef.__doc__) == (self.AGING_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing aging reference.")
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.getDiagnosticMemoryRef.__doc__) == self.DIAGNOSTIC_MEMORY_REF_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.setDiagnosticMemoryRef.__doc__) == (
            self.DIAGNOSTIC_MEMORY_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing diagnosticMemory reference."
        )
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.addExtendedDataRecordRef.__doc__) == (
            self.EXTENDED_DATA_RECORD_NOTE + "\n\nA None value is a no-op and does not extend the extendedDataRecordRefs list."
        )
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.getExtendedDataRecordRefs.__doc__) == self.EXTENDED_DATA_RECORD_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.addFreezeFrameRef.__doc__) == (self.FREEZE_FRAME_NOTE + "\n\nA None value is a no-op and does not extend the freezeFrameRefs list.")
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.getFreezeFrameRefs.__doc__) == self.FREEZE_FRAME_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.getImmediateNvDataStorage.__doc__) == self.IMMEDIATE_NV_DATA_STORAGE_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.setImmediateNvDataStorage.__doc__) == (
            self.IMMEDIATE_NV_DATA_STORAGE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing immediateNvDataStorage."
        )
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.getLegislatedFreezeFrameContentUdsObdRef.__doc__) == self.LEGISLATED_FREEZE_FRAME_CONTENT_UDS_OBD_REF_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.setLegislatedFreezeFrameContentUdsObdRef.__doc__) == (
            self.LEGISLATED_FREEZE_FRAME_CONTENT_UDS_OBD_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing legislatedFreezeFrameContentUdsObd reference."
        )
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.getMaxNumberFreezeFrameRecords.__doc__) == self.MAX_NUMBER_FREEZE_FRAME_RECORDS_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.setMaxNumberFreezeFrameRecords.__doc__) == (
            self.MAX_NUMBER_FREEZE_FRAME_RECORDS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing maxNumberFreezeFrameRecords."
        )
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.getPriority.__doc__) == self.PRIORITY_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.setPriority.__doc__) == (self.PRIORITY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing priority.")
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.getSignificance.__doc__) == self.SIGNIFICANCE_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.setSignificance.__doc__) == (self.SIGNIFICANCE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing significance.")
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.getSnapshotRecordContentRef.__doc__) == self.SNAPSHOT_RECORD_CONTENT_REF_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeProps.setSnapshotRecordContentRef.__doc__) == (
            self.SNAPSHOT_RECORD_CONTENT_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing snapshotRecordContent reference."
        )


class TestDiagnosticTroubleCodeUds:
    """
    Test class for DiagnosticTroubleCodeUds functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.158, p.174
    """

    CLASS_NOTE = "This element is used to describe non OBD-relevant DTCs. Tags: atp.recommendedPackage=DiagnosticTroubleCodes"
    CONSIDER_PTO_STATUS_NOTE = (
        "This attribute describes the affection of the event by the Dem PTO handling.\n\n"
        "true: the event is affected by the Dem PTO handling.\n\n"
        "false: the event is not affected by the Dem PTO handling."
    )
    DTC_PROPS_REF_NOTE = "Defined properties associated with the DemDTC."
    EVENT_READINESS_GROUP_NOTE = "This attribute specifies the Event OBD Readiness group for PID $01 and PID $41 computation. This attribute is only applicable for emission-related ECUs. The upper multiplicity of this role has been increased to * due to resolving an atpVariation stereotype. The previous value was 1."
    FUNCTIONAL_UNIT_NOTE = "This attribute specifies a 1-byte value which identifies the corresponding basic vehicle / system function which reports the DTC. This parameter is necessary for the report of severity information. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"
    OBD_DTC_VALUE_3_BYTE_NOTE = "3 Byte OBD DTC value based on the definition from SAE J2012. The existence of this attribute is only required if separated UDS and OBD DTC values are used for SAE J1979-2. If this attribute does not exist, then UDS DTC values are used with J1979-2. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"
    SEVERITY_NOTE = "DTC severity according to ISO 14229-1. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"
    UDS_DTC_VALUE_NOTE = "Unique Diagnostic Trouble Code value for UDS. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"
    WWH_OBD_DTC_CLASS_NOTE = (
        "This attribute is used to identify (if applicable) the corresponding severity class of an WWH-OBD DTC. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"
    )

    def _create_trouble_code(self) -> DiagnosticTroubleCodeUds:
        return DiagnosticTroubleCodeUds()

    def test_initialization(self):
        """
        Test that a new DiagnosticTroubleCodeUds initializes all attributes to their defaults.
        """
        obj = self._create_trouble_code()

        assert obj.getConsiderPtoStatus() is None
        assert obj.getDtcPropsRef() is None
        assert obj.getEventReadinessGroup() is None
        assert obj.getFunctionalUnit() is None
        assert obj.getObdDtcValue3Byte() is None
        assert obj.getSeverity() is None
        assert obj.getUdsDtcValue() is None
        assert obj.getWwhObdDtcClass() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DiagnosticTroubleCodeUds derives from ARObject (confirmed queue row; ARObject is the most-derived reachable base — nested value container, not Identifiable).
        """
        assert issubclass(DiagnosticTroubleCodeUds, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DiagnosticTroubleCodeUds.__init__.__doc__ is None

    def test_get_set_consider_pto_status(self):
        """
        Test getConsiderPtoStatus and setConsiderPtoStatus round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        value = Boolean().setValue(True)
        result = obj.setConsiderPtoStatus(value)
        assert result is obj  # method chaining
        assert obj.getConsiderPtoStatus() is value
        assert obj.getConsiderPtoStatus().getValue() is True

        result = obj.setConsiderPtoStatus(None)
        assert result is obj  # method chaining with None
        assert obj.getConsiderPtoStatus() is value  # None is a no-op

    def test_get_set_dtc_props_ref(self):
        """
        Test getDtcPropsRef and setDtcPropsRef round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        ref = RefType()
        ref.setDest("DIAGNOSTIC-TROUBLE-CODE-PROPS")
        ref.setValue("/AUTOSAR/DiagnosticTroubleCodeProps/DtcProps1")
        result = obj.setDtcPropsRef(ref)
        assert result is obj  # method chaining
        assert obj.getDtcPropsRef() is ref
        assert obj.getDtcPropsRef().getValue() == "/AUTOSAR/DiagnosticTroubleCodeProps/DtcProps1"
        assert obj.getDtcPropsRef().getDest() == "DIAGNOSTIC-TROUBLE-CODE-PROPS"

        result = obj.setDtcPropsRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDtcPropsRef() is ref  # None is a no-op

    def test_get_set_event_readiness_group(self):
        """
        Test getEventReadinessGroup and setEventReadinessGroup round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        value = EventObdReadinessGroup()
        result = obj.setEventReadinessGroup(value)
        assert result is obj  # method chaining
        assert obj.getEventReadinessGroup() is value

        result = obj.setEventReadinessGroup(None)
        assert result is obj  # method chaining with None
        assert obj.getEventReadinessGroup() is value  # None is a no-op

    def test_get_set_functional_unit(self):
        """
        Test getFunctionalUnit and setFunctionalUnit round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        value = PositiveInteger().setValue(4)
        result = obj.setFunctionalUnit(value)
        assert result is obj  # method chaining
        assert obj.getFunctionalUnit() is value
        assert obj.getFunctionalUnit().getValue() == 4

        result = obj.setFunctionalUnit(None)
        assert result is obj  # method chaining with None
        assert obj.getFunctionalUnit() is value  # None is a no-op

    def test_get_set_obd_dtc_value_3_byte(self):
        """
        Test getObdDtcValue3Byte and setObdDtcValue3Byte round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        value = PositiveInteger().setValue(30511)
        result = obj.setObdDtcValue3Byte(value)
        assert result is obj  # method chaining
        assert obj.getObdDtcValue3Byte() is value
        assert obj.getObdDtcValue3Byte().getValue() == 30511

        result = obj.setObdDtcValue3Byte(None)
        assert result is obj  # method chaining with None
        assert obj.getObdDtcValue3Byte() is value  # None is a no-op

    def test_get_set_severity(self):
        """
        Test getSeverity and setSeverity round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        value = DiagnosticUdsSeverityEnum().setValue(DiagnosticUdsSeverityEnum.CHECK_AT_NEXT_HALT)
        result = obj.setSeverity(value)
        assert result is obj  # method chaining
        assert obj.getSeverity() is value

        result = obj.setSeverity(None)
        assert result is obj  # method chaining with None
        assert obj.getSeverity() is value  # None is a no-op

    def test_get_set_uds_dtc_value(self):
        """
        Test getUdsDtcValue and setUdsDtcValue round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        value = PositiveInteger().setValue(1234567)
        result = obj.setUdsDtcValue(value)
        assert result is obj  # method chaining
        assert obj.getUdsDtcValue() is value
        assert obj.getUdsDtcValue().getValue() == 1234567

        result = obj.setUdsDtcValue(None)
        assert result is obj  # method chaining with None
        assert obj.getUdsDtcValue() is value  # None is a no-op

    def test_get_set_wwh_obd_dtc_class(self):
        """
        Test getWwhObdDtcClass and setWwhObdDtcClass round-trip and None no-op.
        """
        obj = self._create_trouble_code()

        value = DiagnosticWwhObdDtcClassEnum().setValue(DiagnosticWwhObdDtcClassEnum.DEM_DTC_WWH_OBD_CLASS_A)
        result = obj.setWwhObdDtcClass(value)
        assert result is obj  # method chaining
        assert obj.getWwhObdDtcClass() is value

        result = obj.setWwhObdDtcClass(None)
        assert result is obj  # method chaining with None
        assert obj.getWwhObdDtcClass() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setters + None-no-op sentence).
        """
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.getConsiderPtoStatus.__doc__) == self.CONSIDER_PTO_STATUS_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.setConsiderPtoStatus.__doc__) == (
            self.CONSIDER_PTO_STATUS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing considerPtoStatus."
        )
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.getDtcPropsRef.__doc__) == self.DTC_PROPS_REF_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.setDtcPropsRef.__doc__) == (self.DTC_PROPS_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dtcProps reference.")
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.getEventReadinessGroup.__doc__) == self.EVENT_READINESS_GROUP_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.setEventReadinessGroup.__doc__) == (
            self.EVENT_READINESS_GROUP_NOTE + "\n\nA None value is a no-op and does not overwrite an existing eventReadinessGroup."
        )
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.getFunctionalUnit.__doc__) == self.FUNCTIONAL_UNIT_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.setFunctionalUnit.__doc__) == (self.FUNCTIONAL_UNIT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing functionalUnit.")
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.getObdDtcValue3Byte.__doc__) == self.OBD_DTC_VALUE_3_BYTE_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.setObdDtcValue3Byte.__doc__) == (
            self.OBD_DTC_VALUE_3_BYTE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing obdDtcValue3Byte."
        )
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.getSeverity.__doc__) == self.SEVERITY_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.setSeverity.__doc__) == (self.SEVERITY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing severity.")
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.getUdsDtcValue.__doc__) == self.UDS_DTC_VALUE_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.setUdsDtcValue.__doc__) == (self.UDS_DTC_VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing udsDtcValue.")
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.getWwhObdDtcClass.__doc__) == self.WWH_OBD_DTC_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticTroubleCodeUds.setWwhObdDtcClass.__doc__) == (self.WWH_OBD_DTC_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing wwhObdDtcClass.")


class TestDiagnosticTroubleCodeUdsPendingReferences:
    """
    Test class for the still-stub reference targets of DiagnosticTroubleCodeUds.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.158, p.174

    EventObdReadinessGroup (Table 4.160), DiagnosticUdsSeverityEnum (Table 4.177) and
    DiagnosticWwhObdDtcClassEnum (Table 4.179) are queued later in Group25 and still
    empty stubs; the typed fields reference them directly (ArObject.py /
    PrimitiveTypes.py).
    """

    def test_reference_targets_are_stub_classes(self):
        """
        Test that the referenced types exist as stubs of their spec families.
        """
        assert issubclass(EventObdReadinessGroup, ARObject)
        assert issubclass(DiagnosticUdsSeverityEnum, AREnum)
        assert issubclass(DiagnosticWwhObdDtcClassEnum, AREnum)


class TestEventObdReadinessGroup:
    """
    Test class for EventObdReadinessGroup functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.160, p.176
    """

    CLASS_NOTE = "This meta-class represents the ability to define the value of attribute eventObdReadinessGroup. It is only introduced to allow for a variant modeling of this attribute."
    EVENT_OBD_READINESS_GROUP_NOTE = "This attribute specifies the Event OBD Readiness group for PID $01 and PID $41 computation. This attribute is only applicable for emission-related ECUs."

    def _create_group(self) -> EventObdReadinessGroup:
        return EventObdReadinessGroup()

    def test_initialization(self):
        """
        Test that a new EventObdReadinessGroup initializes all attributes to their defaults.
        """
        obj = self._create_group()

        assert obj.getEventObdReadinessGroup() is None

    def test_is_ar_object_subclass(self):
        """
        Test that EventObdReadinessGroup derives from ARObject (confirmed queue row; ARObject is the most-derived reachable base — nested value container, not Identifiable).
        """
        assert issubclass(EventObdReadinessGroup, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(EventObdReadinessGroup.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert EventObdReadinessGroup.__init__.__doc__ is None

    def test_get_set_event_obd_readiness_group(self):
        """
        Test getEventObdReadinessGroup and setEventObdReadinessGroup round-trip and None no-op.
        """
        obj = self._create_group()

        value = NameToken().setValue("OBD_READINESS_GROUP_1")
        result = obj.setEventObdReadinessGroup(value)
        assert result is obj  # method chaining
        assert obj.getEventObdReadinessGroup() is value
        assert obj.getEventObdReadinessGroup().getValue() == "OBD_READINESS_GROUP_1"

        result = obj.setEventObdReadinessGroup(None)
        assert result is obj  # method chaining with None
        assert obj.getEventObdReadinessGroup() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(EventObdReadinessGroup.getEventObdReadinessGroup.__doc__) == self.EVENT_OBD_READINESS_GROUP_NOTE
        assert inspect.cleandoc(EventObdReadinessGroup.setEventObdReadinessGroup.__doc__) == (
            self.EVENT_OBD_READINESS_GROUP_NOTE + "\n\nA None value is a no-op and does not overwrite an existing eventObdReadinessGroup."
        )


class TestPhysicalDimensionMapping:
    """
    Test class for PhysicalDimensionMapping functionality.

    Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.77, p.399
    """

    CLASS_NOTE = "This class represents a specific mapping between two PhysicalDimensions."
    FIRST_PHYSICAL_DIMENSION_NOTE = "This represents the first PhysicalDimension of the enclosing PhysicalDimensionMapping."
    SECOND_PHYSICAL_DIMENSION_NOTE = "This represents the first PhysicalDimension of the enclosing PhysicalDimensionMapping."

    def _create_mapping(self) -> PhysicalDimensionMapping:
        return PhysicalDimensionMapping()

    def test_initialization(self):
        """
        Test that a new PhysicalDimensionMapping initializes all attributes to their defaults.
        """
        obj = self._create_mapping()

        assert obj.getFirstPhysicalDimensionRef() is None
        assert obj.getSecondPhysicalDimensionRef() is None

    def test_is_ar_object_subclass(self):
        """
        Test that PhysicalDimensionMapping derives from ARObject per the Table 5.77 Base row.
        """
        assert issubclass(PhysicalDimensionMapping, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(PhysicalDimensionMapping.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert PhysicalDimensionMapping.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 5.77 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in PhysicalDimensionMapping.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getFirstPhysicalDimensionRef",
            "setFirstPhysicalDimensionRef",
            "getSecondPhysicalDimensionRef",
            "setSecondPhysicalDimensionRef",
        ]

    def test_annotations_are_optional_ref_type(self):
        """
        Test that the ref accessors carry the spec Optional[RefType] hints (0..1 ref rows).
        """
        hints_get_first = typing.get_type_hints(PhysicalDimensionMapping.getFirstPhysicalDimensionRef)
        assert hints_get_first["return"] == typing.Optional[RefType]

        hints_set_first = typing.get_type_hints(PhysicalDimensionMapping.setFirstPhysicalDimensionRef)
        assert hints_set_first["value"] == typing.Optional[RefType]
        assert hints_set_first["return"] == PhysicalDimensionMapping

        hints_get_second = typing.get_type_hints(PhysicalDimensionMapping.getSecondPhysicalDimensionRef)
        assert hints_get_second["return"] == typing.Optional[RefType]

        hints_set_second = typing.get_type_hints(PhysicalDimensionMapping.setSecondPhysicalDimensionRef)
        assert hints_set_second["value"] == typing.Optional[RefType]
        assert hints_set_second["return"] == PhysicalDimensionMapping

    def test_get_set_first_physical_dimension_ref(self):
        """
        Test getFirstPhysicalDimensionRef and setFirstPhysicalDimensionRef round-trip and None no-op.
        """
        obj = self._create_mapping()

        value = RefType().setValue("/PhysicalDimensions/Time")
        result = obj.setFirstPhysicalDimensionRef(value)
        assert result is obj  # method chaining
        assert obj.getFirstPhysicalDimensionRef() is value
        assert obj.getFirstPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Time"

        result = obj.setFirstPhysicalDimensionRef(None)
        assert result is obj  # method chaining with None
        assert obj.getFirstPhysicalDimensionRef() is value  # None is a no-op

    def test_get_set_second_physical_dimension_ref(self):
        """
        Test getSecondPhysicalDimensionRef and setSecondPhysicalDimensionRef round-trip and None no-op.
        """
        obj = self._create_mapping()

        value = RefType().setValue("/PhysicalDimensions/Duration")
        result = obj.setSecondPhysicalDimensionRef(value)
        assert result is obj  # method chaining
        assert obj.getSecondPhysicalDimensionRef() is value
        assert obj.getSecondPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Duration"

        result = obj.setSecondPhysicalDimensionRef(None)
        assert result is obj  # method chaining with None
        assert obj.getSecondPhysicalDimensionRef() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(PhysicalDimensionMapping.getFirstPhysicalDimensionRef.__doc__) == self.FIRST_PHYSICAL_DIMENSION_NOTE
        assert inspect.cleandoc(PhysicalDimensionMapping.setFirstPhysicalDimensionRef.__doc__) == (
            self.FIRST_PHYSICAL_DIMENSION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing firstPhysicalDimensionRef."
        )
        assert inspect.cleandoc(PhysicalDimensionMapping.getSecondPhysicalDimensionRef.__doc__) == self.SECOND_PHYSICAL_DIMENSION_NOTE
        assert inspect.cleandoc(PhysicalDimensionMapping.setSecondPhysicalDimensionRef.__doc__) == (
            self.SECOND_PHYSICAL_DIMENSION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing secondPhysicalDimensionRef."
        )


class TestCalibrationParameterValue:
    """
    Test class for CalibrationParameterValue functionality.

    Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.138, p.478
    """

    CLASS_NOTE = (
        "Specifies instance specific calibration parameter values used to initialize the memory objects implementing calibration parameters in the generated RTE code. "
        "RTE generator will use the implInitValue to override the initial values specified for the DataPrototypes of a component type. "
        "The applInitValue is used to exchange init values with the component vendor not publishing the transformation algorithm between ApplicationDataTypes and ImplementationDataTypes or defining an instance specific initialization of components which are only defined with ApplicationDataTypes. "
        "Note: If both representations of init values are available these need to represent the same content. "
        "Note further that in this case an explicit mapping of ValueSpecification is not implemented because calibration parameters are delivered back after the calibration phase."
        "\n\n"
        "[constr_1933] Existence of CalibrationParameterValue.initializedParameter: For each CalibrationParameterValue, the reference to meta-class ConstantSpecification in the role initializedParameter shall exist at the time when the contract phase generation is executed."
    )
    APPL_INIT_VALUE_NOTE = "This is the initial value specification structured according to the ApplicationDataType"
    IMPL_INIT_VALUE_NOTE = "This is the initial value specification structured according to the ImplementationDataType"
    INITIALIZED_PARAMETER_NOTE = "This represents the parameter that is initialized by the CalibrationParameterValue."

    def _create_value(self) -> CalibrationParameterValue:
        return CalibrationParameterValue()

    def test_initialization(self):
        """
        Test that a new CalibrationParameterValue initializes all attributes to their defaults.
        """
        obj = self._create_value()

        assert obj.getApplInitValue() is None
        assert obj.getImplInitValue() is None
        assert obj.getInitializedParameterRef() is None
        assert obj.getVariationPoint() is None

    def test_is_ar_object_subclass_with_variation_point_capable(self):
        """
        Test that CalibrationParameterValue derives from ARObject per the Table 5.138 Base row
        and from VariationPointCapable (the atpVariation on the owning Set row makes the member
        class VP-capable; the XSD CALIBRATION-PARAMETER-VALUE group carries VARIATION-POINT).
        """
        assert issubclass(CalibrationParameterValue, ARObject)
        assert issubclass(CalibrationParameterValue, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim plus the class-level constraint.
        """
        assert inspect.cleandoc(CalibrationParameterValue.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CalibrationParameterValue.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 5.138 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in CalibrationParameterValue.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getApplInitValue",
            "setApplInitValue",
            "getImplInitValue",
            "setImplInitValue",
            "getInitializedParameterRef",
            "setInitializedParameterRef",
        ]

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec Optional[T] hints (0..1 rows).

        The ValueSpecification members are pinned via the raw PEP 563 annotation strings:
        the Constants package imports ARObject back from this module, so a runtime import
        into ArObject.py would invert the module load order (the DiagnosticParameter.ident
        precedent for cross-package types in this module).
        """
        assert CalibrationParameterValue.getApplInitValue.__annotations__["return"] == "Optional[ValueSpecification]"
        assert CalibrationParameterValue.setApplInitValue.__annotations__["value"] == "Optional[ValueSpecification]"
        assert CalibrationParameterValue.setApplInitValue.__annotations__["return"] == "CalibrationParameterValue"

        assert CalibrationParameterValue.getImplInitValue.__annotations__["return"] == "Optional[ValueSpecification]"
        assert CalibrationParameterValue.setImplInitValue.__annotations__["value"] == "Optional[ValueSpecification]"
        assert CalibrationParameterValue.setImplInitValue.__annotations__["return"] == "CalibrationParameterValue"

        hints_get_ref = typing.get_type_hints(CalibrationParameterValue.getInitializedParameterRef)
        assert hints_get_ref["return"] == typing.Optional[RefType]

        hints_set_ref = typing.get_type_hints(CalibrationParameterValue.setInitializedParameterRef)
        assert hints_set_ref["value"] == typing.Optional[RefType]
        assert hints_set_ref["return"] == CalibrationParameterValue

    def test_get_set_appl_init_value(self):
        """
        Test getApplInitValue and setApplInitValue round-trip and None no-op.
        """
        obj = self._create_value()

        value = TextValueSpecification()
        result = obj.setApplInitValue(value)
        assert result is obj  # method chaining
        assert obj.getApplInitValue() is value

        result = obj.setApplInitValue(None)
        assert result is obj  # method chaining with None
        assert obj.getApplInitValue() is value  # None is a no-op

    def test_get_set_impl_init_value(self):
        """
        Test getImplInitValue and setImplInitValue round-trip and None no-op.
        """
        obj = self._create_value()

        value = TextValueSpecification()
        result = obj.setImplInitValue(value)
        assert result is obj  # method chaining
        assert obj.getImplInitValue() is value

        result = obj.setImplInitValue(None)
        assert result is obj  # method chaining with None
        assert obj.getImplInitValue() is value  # None is a no-op

    def test_get_set_initialized_parameter_ref(self):
        """
        Test getInitializedParameterRef and setInitializedParameterRef round-trip and None no-op.
        """
        obj = self._create_value()

        value = RefType().setDest("FLAT-INSTANCE-DESCRIPTOR").setValue("/Pkg/FlatInstanceDescriptors/FID")
        result = obj.setInitializedParameterRef(value)
        assert result is obj  # method chaining
        assert obj.getInitializedParameterRef() is value
        assert obj.getInitializedParameterRef().getValue() == "/Pkg/FlatInstanceDescriptors/FID"
        assert obj.getInitializedParameterRef().getDest() == "FLAT-INSTANCE-DESCRIPTOR"

        result = obj.setInitializedParameterRef(None)
        assert result is obj  # method chaining with None
        assert obj.getInitializedParameterRef() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(CalibrationParameterValue.getApplInitValue.__doc__) == self.APPL_INIT_VALUE_NOTE
        assert inspect.cleandoc(CalibrationParameterValue.setApplInitValue.__doc__) == (self.APPL_INIT_VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing applInitValue.")
        assert inspect.cleandoc(CalibrationParameterValue.getImplInitValue.__doc__) == self.IMPL_INIT_VALUE_NOTE
        assert inspect.cleandoc(CalibrationParameterValue.setImplInitValue.__doc__) == (self.IMPL_INIT_VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing implInitValue.")
        assert inspect.cleandoc(CalibrationParameterValue.getInitializedParameterRef.__doc__) == self.INITIALIZED_PARAMETER_NOTE
        assert inspect.cleandoc(CalibrationParameterValue.setInitializedParameterRef.__doc__) == (
            self.INITIALIZED_PARAMETER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing initializedParameterRef."
        )


class TestDdsCpServiceInstanceOperation:
    """
    Test class for DdsCpServiceInstanceOperation functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.156, p.476
    """

    CLASS_NOTE = "This element represents an operation as part of the Provided Service Instance. Tags: atp.Status=candidate"
    REQUEST_TRIGGERING_NOTE = "Reference to the PduTriggering used for the upper layer transport of this DdsOperation request message. Tags: atp.Status=candidate"
    RESPONSE_TRIGGERING_NOTE = "Reference to the PduTriggering used for the upper layer transport of this DdsOperation response message. Tags: atp.Status=candidate"

    def _create_operation(self) -> DdsCpServiceInstanceOperation:
        return DdsCpServiceInstanceOperation()

    def test_initialization(self):
        """
        Test that a new DdsCpServiceInstanceOperation initializes all attributes to their defaults.
        """
        obj = self._create_operation()

        assert obj.getDdsOperationRequestTriggeringRef() is None
        assert obj.getDdsOperationResponseTriggeringRef() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsCpServiceInstanceOperation derives from ARObject and is VP-capable (XSD group DDS-CP-SERVICE-INSTANCE-OPERATION carries VARIATION-POINT, Rule 0020).
        """
        assert issubclass(DdsCpServiceInstanceOperation, ARObject)
        assert issubclass(DdsCpServiceInstanceOperation, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsCpServiceInstanceOperation.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsCpServiceInstanceOperation.__init__.__doc__ is None

    def test_get_set_dds_operation_request_triggering_ref(self):
        """
        Test getDdsOperationRequestTriggeringRef and setDdsOperationRequestTriggeringRef round-trip and None no-op.
        """
        obj = self._create_operation()

        value = RefType().setDest("PDU-TRIGGERING").setValue("/Fibex/Ecu1/PduTriggerings/RequestTriggering")
        result = obj.setDdsOperationRequestTriggeringRef(value)
        assert result is obj  # method chaining
        assert obj.getDdsOperationRequestTriggeringRef() is value
        assert obj.getDdsOperationRequestTriggeringRef().getValue() == "/Fibex/Ecu1/PduTriggerings/RequestTriggering"
        assert obj.getDdsOperationRequestTriggeringRef().getDest() == "PDU-TRIGGERING"

        result = obj.setDdsOperationRequestTriggeringRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDdsOperationRequestTriggeringRef() is value  # None is a no-op

    def test_get_set_dds_operation_response_triggering_ref(self):
        """
        Test getDdsOperationResponseTriggeringRef and setDdsOperationResponseTriggeringRef round-trip and None no-op.
        """
        obj = self._create_operation()

        value = RefType().setDest("PDU-TRIGGERING").setValue("/Fibex/Ecu1/PduTriggerings/ResponseTriggering")
        result = obj.setDdsOperationResponseTriggeringRef(value)
        assert result is obj  # method chaining
        assert obj.getDdsOperationResponseTriggeringRef() is value
        assert obj.getDdsOperationResponseTriggeringRef().getValue() == "/Fibex/Ecu1/PduTriggerings/ResponseTriggering"
        assert obj.getDdsOperationResponseTriggeringRef().getDest() == "PDU-TRIGGERING"

        result = obj.setDdsOperationResponseTriggeringRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDdsOperationResponseTriggeringRef() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsCpServiceInstanceOperation.getDdsOperationRequestTriggeringRef.__doc__) == self.REQUEST_TRIGGERING_NOTE
        assert inspect.cleandoc(DdsCpServiceInstanceOperation.setDdsOperationRequestTriggeringRef.__doc__) == (
            self.REQUEST_TRIGGERING_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ddsOperationRequestTriggeringRef."
        )
        assert inspect.cleandoc(DdsCpServiceInstanceOperation.getDdsOperationResponseTriggeringRef.__doc__) == self.RESPONSE_TRIGGERING_NOTE
        assert inspect.cleandoc(DdsCpServiceInstanceOperation.setDdsOperationResponseTriggeringRef.__doc__) == (
            self.RESPONSE_TRIGGERING_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ddsOperationResponseTriggeringRef."
        )


class TestDdsCpServiceInstanceEvent:
    """
    Test class for DdsCpServiceInstanceEvent functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.155, p.475
    """

    CLASS_NOTE = "This element represents an event as part of the Provided Service Instance. Tags: atp.Status=candidate"
    DDS_EVENT_NOTE = "Reference to the PduTriggerung used for the upper layer transport of this DdsEvent message. Tags: atp.Status=candidate"
    DDS_EVENT_QOS_PROFILE_NOTE = "Reference to the QOS Profile used for this Event. Tags: atp.Status=candidate"
    DDS_EVENT_TOPIC_NOTE = "Reference to the DDS Topic used for this Event. Tags: atp.Status=candidate"

    def _create_event(self) -> DdsCpServiceInstanceEvent:
        return DdsCpServiceInstanceEvent()

    def test_initialization(self):
        """
        Test that a new DdsCpServiceInstanceEvent initializes all attributes to their defaults.
        """
        obj = self._create_event()

        assert obj.getDdsEventRef() is None
        assert obj.getDdsEventQosProfileRef() is None
        assert obj.getDdsEventTopicRef() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsCpServiceInstanceEvent derives from ARObject and is VP-capable (XSD group DDS-CP-SERVICE-INSTANCE-EVENT carries VARIATION-POINT, Rule 0020).
        """
        assert issubclass(DdsCpServiceInstanceEvent, ARObject)
        assert issubclass(DdsCpServiceInstanceEvent, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim (including the spec's own "PduTriggerung" spelling in the ddsEvent Note).
        """
        assert inspect.cleandoc(DdsCpServiceInstanceEvent.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsCpServiceInstanceEvent.__init__.__doc__ is None

    def test_get_set_dds_event_ref(self):
        """
        Test getDdsEventRef and setDdsEventRef round-trip and None no-op.
        """
        obj = self._create_event()

        value = RefType().setDest("PDU-TRIGGERING").setValue("/Fibex/Ecu1/PduTriggerings/DdsEvent")
        result = obj.setDdsEventRef(value)
        assert result is obj  # method chaining
        assert obj.getDdsEventRef() is value
        assert obj.getDdsEventRef().getValue() == "/Fibex/Ecu1/PduTriggerings/DdsEvent"
        assert obj.getDdsEventRef().getDest() == "PDU-TRIGGERING"

        result = obj.setDdsEventRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDdsEventRef() is value  # None is a no-op

    def test_get_set_dds_event_qos_profile_ref(self):
        """
        Test getDdsEventQosProfileRef and setDdsEventQosProfileRef round-trip and None no-op.
        """
        obj = self._create_event()

        value = RefType().setDest("DDS-CP-QOS-PROFILE").setValue("/DdsCpConfig/QosProfiles/Profile1")
        result = obj.setDdsEventQosProfileRef(value)
        assert result is obj  # method chaining
        assert obj.getDdsEventQosProfileRef() is value
        assert obj.getDdsEventQosProfileRef().getValue() == "/DdsCpConfig/QosProfiles/Profile1"
        assert obj.getDdsEventQosProfileRef().getDest() == "DDS-CP-QOS-PROFILE"

        result = obj.setDdsEventQosProfileRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDdsEventQosProfileRef() is value  # None is a no-op

    def test_get_set_dds_event_topic_ref(self):
        """
        Test getDdsEventTopicRef and setDdsEventTopicRef round-trip and None no-op.
        """
        obj = self._create_event()

        value = RefType().setDest("DDS-CP-TOPIC").setValue("/DdsCpConfig/Domains/Domain1/Topics/Topic1")
        result = obj.setDdsEventTopicRef(value)
        assert result is obj  # method chaining
        assert obj.getDdsEventTopicRef() is value
        assert obj.getDdsEventTopicRef().getValue() == "/DdsCpConfig/Domains/Domain1/Topics/Topic1"
        assert obj.getDdsEventTopicRef().getDest() == "DDS-CP-TOPIC"

        result = obj.setDdsEventTopicRef(None)
        assert result is obj  # method chaining with None
        assert obj.getDdsEventTopicRef() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsCpServiceInstanceEvent.getDdsEventRef.__doc__) == self.DDS_EVENT_NOTE
        assert inspect.cleandoc(DdsCpServiceInstanceEvent.setDdsEventRef.__doc__) == (self.DDS_EVENT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ddsEventRef.")
        assert inspect.cleandoc(DdsCpServiceInstanceEvent.getDdsEventQosProfileRef.__doc__) == self.DDS_EVENT_QOS_PROFILE_NOTE
        assert inspect.cleandoc(DdsCpServiceInstanceEvent.setDdsEventQosProfileRef.__doc__) == (
            self.DDS_EVENT_QOS_PROFILE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ddsEventQosProfileRef."
        )
        assert inspect.cleandoc(DdsCpServiceInstanceEvent.getDdsEventTopicRef.__doc__) == self.DDS_EVENT_TOPIC_NOTE
        assert inspect.cleandoc(DdsCpServiceInstanceEvent.setDdsEventTopicRef.__doc__) == (
            self.DDS_EVENT_TOPIC_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ddsEventTopicRef."
        )


class TestDdsTopicData:
    """
    Test class for DdsTopicData functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.180, p.529
    """

    CLASS_NOTE = "Describes the DDS TOPIC_DATA QoS policy. Tags: atp.Status=candidate"
    TOPIC_DATA_NOTE = 'See "TOPIC_DATA" chapter in DDS. Tags: atp.Status=candidate'

    def _create_topic_data(self) -> DdsTopicData:
        return DdsTopicData()

    def test_initialization(self):
        """
        Test that a new DdsTopicData initializes all attributes to their defaults.
        """
        obj = self._create_topic_data()

        assert obj.getTopicData() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsTopicData derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsTopicData, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsTopicData.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsTopicData.__init__.__doc__ is None

    def test_get_set_topic_data(self):
        """
        Test getTopicData and setTopicData round-trip and None no-op.
        """
        obj = self._create_topic_data()

        value = String().setValue("topic-data-payload")
        result = obj.setTopicData(value)
        assert result is obj  # method chaining
        assert obj.getTopicData() is value
        assert obj.getTopicData().getValue() == "topic-data-payload"

        result = obj.setTopicData(None)
        assert result is obj  # method chaining with None
        assert obj.getTopicData() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsTopicData.getTopicData.__doc__) == self.TOPIC_DATA_NOTE
        assert inspect.cleandoc(DdsTopicData.setTopicData.__doc__) == (self.TOPIC_DATA_NOTE + "\n\nA None value is a no-op and does not overwrite an existing topicData.")


class TestDdsCpProvidedServiceInstance:
    """
    Test class for DdsCpProvidedServiceInstance functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.153, p.473
    """

    CLASS_NOTE = "This meta-class represents the ability to describe the existence and configuration of a provided service instance in a concrete implementation on top of DDS."
    LOCAL_UNICAST_ADDRESS_NOTE = (
        "The local address over which the Service is provided. Stereotypes: atpSplitable; atpVariation Tags: "
        "atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel "
        "atp.Status=candidate vh.latestBindingTime=systemDesignTime xml.namePlural=LOCAL-UNICAST-ADDRESSES"
    )
    MINOR_VERSION_NOTE = "Minor Version of the Service that is provided by this Dds CpProvidedServiceInstance."
    PROVIDED_DDS_OPERATION_NOTE = (
        "Collection of provided operations. Stereotypes: atpSplitable; atpVariation Tags: "
        "atp.Splitkey=providedDdsOperation, providedDds Operation.variationPoint.shortLabel "
        "atp.Status=candidate vh.latestBindingTime=systemDesignTime"
    )
    PROVIDED_DDS_SERVICE_INSTANCE_EVENT_NOTE = (
        "Collection of provided events. Stereotypes: atpSplitable; atpVariation Tags: "
        "atp.Splitkey=providedDdsServiceInstanceEvent, provided DdsServiceInstanceEvent.variationPoint.shortLabel "
        "atp.Status=candidate vh.latestBindingTime=systemDesignTime"
    )
    STATIC_REMOTE_MULTICAST_ADDRESS_NOTE = (
        "This reference defines the remote multicast address of Service consumers. This reference shall ONLY be used "
        "if the remote multicast address of the clients is determined from the configuration and not at runtime. "
        "Stereotypes: atpSplitable; atpVariation Tags: "
        "atp.Splitkey=staticRemoteMulticastAddress.application Endpoint, staticRemoteMulticastAddress.variation "
        "Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime "
        "xml.namePlural=STATIC-REMOTE-MULTICAST-ADDRESSES"
    )
    STATIC_REMOTE_UNICAST_ADDRESS_NOTE = (
        "This reference defines the remote unicast addresses of Service consumers. This reference shall ONLY be used "
        "if the remote unicast address of the clients is determined from the configuration and not at runtime. "
        "Stereotypes: atpSplitable; atpVariation Tags: "
        "atp.Splitkey=staticRemoteUnicastAddress.application Endpoint, staticRemoteMulticastAddress.variation "
        "Point.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime "
        "xml.namePlural=STATIC-REMOTE-UNICAST-ADDRESSES"
    )

    def _create_instance(self) -> DdsCpProvidedServiceInstance:
        return DdsCpProvidedServiceInstance()

    def test_initialization(self):
        """
        Test that a new DdsCpProvidedServiceInstance initializes all attributes to their defaults.
        """
        obj = self._create_instance()

        assert obj.getLocalUnicastAddressRef() is None
        assert obj.getMinorVersion() is None
        assert obj.getProvidedDdsOperations() == []
        assert obj.getProvidedDdsServiceInstanceEvents() == []
        assert obj.getStaticRemoteMulticastAddressRef() is None
        assert obj.getStaticRemoteUnicastAddressRefs() == []

    def test_is_ar_object_subclass(self):
        """
        Test that DdsCpProvidedServiceInstance derives from ARObject (the Base row's AbstractServiceInstance/DdsCpServiceInstance branch is unsynced — queued Table 6.152/6.158).
        """
        assert issubclass(DdsCpProvidedServiceInstance, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsCpProvidedServiceInstance.__init__.__doc__ is None

    def test_get_set_local_unicast_address_ref(self):
        """
        Test getLocalUnicastAddressRef and setLocalUnicastAddressRef round-trip and None no-op.
        """
        obj = self._create_instance()

        value = RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Ethernet/Endpoints/LocalEp")
        result = obj.setLocalUnicastAddressRef(value)
        assert result is obj  # method chaining
        assert obj.getLocalUnicastAddressRef() is value
        assert obj.getLocalUnicastAddressRef().getValue() == "/Cluster/Ethernet/Endpoints/LocalEp"
        assert obj.getLocalUnicastAddressRef().getDest() == "APPLICATION-ENDPOINT"

        result = obj.setLocalUnicastAddressRef(None)
        assert result is obj  # method chaining with None
        assert obj.getLocalUnicastAddressRef() is value  # None is a no-op

    def test_get_set_minor_version(self):
        """
        Test getMinorVersion and setMinorVersion round-trip and None no-op.
        """
        obj = self._create_instance()

        value = PositiveInteger().setValue("4")
        result = obj.setMinorVersion(value)
        assert result is obj  # method chaining
        assert obj.getMinorVersion() is value
        assert obj.getMinorVersion().getValue() == 4

        result = obj.setMinorVersion(None)
        assert result is obj  # method chaining with None
        assert obj.getMinorVersion() is value  # None is a no-op

    def test_add_get_provided_dds_operations(self):
        """
        Test addProvidedDdsOperation and getProvidedDdsOperations appending, return value and None no-op.
        """
        obj = self._create_instance()

        assert obj.getProvidedDdsOperations() == []

        operation = DdsCpServiceInstanceOperation()
        result = obj.addProvidedDdsOperation(operation)
        assert result is obj  # method chaining
        assert obj.getProvidedDdsOperations() == [operation]

        assert obj.addProvidedDdsOperation(None) is obj  # None is a no-op
        assert obj.getProvidedDdsOperations() == [operation]

    def test_add_get_provided_dds_service_instance_events(self):
        """
        Test addProvidedDdsServiceInstanceEvent and getProvidedDdsServiceInstanceEvents appending, return value and None no-op.
        """
        obj = self._create_instance()

        assert obj.getProvidedDdsServiceInstanceEvents() == []

        event = DdsCpServiceInstanceEvent()
        result = obj.addProvidedDdsServiceInstanceEvent(event)
        assert result is obj  # method chaining
        assert obj.getProvidedDdsServiceInstanceEvents() == [event]

        assert obj.addProvidedDdsServiceInstanceEvent(None) is obj  # None is a no-op
        assert obj.getProvidedDdsServiceInstanceEvents() == [event]

    def test_get_set_static_remote_multicast_address_ref(self):
        """
        Test getStaticRemoteMulticastAddressRef and setStaticRemoteMulticastAddressRef round-trip and None no-op.
        """
        obj = self._create_instance()

        value = RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Ethernet/Endpoints/MulticastEp")
        result = obj.setStaticRemoteMulticastAddressRef(value)
        assert result is obj  # method chaining
        assert obj.getStaticRemoteMulticastAddressRef() is value
        assert obj.getStaticRemoteMulticastAddressRef().getValue() == "/Cluster/Ethernet/Endpoints/MulticastEp"
        assert obj.getStaticRemoteMulticastAddressRef().getDest() == "APPLICATION-ENDPOINT"

        result = obj.setStaticRemoteMulticastAddressRef(None)
        assert result is obj  # method chaining with None
        assert obj.getStaticRemoteMulticastAddressRef() is value  # None is a no-op

    def test_add_get_static_remote_unicast_address_refs(self):
        """
        Test addStaticRemoteUnicastAddressRef and getStaticRemoteUnicastAddressRefs appending, return value and None no-op.
        """
        obj = self._create_instance()

        assert obj.getStaticRemoteUnicastAddressRefs() == []

        ref = RefType().setDest("APPLICATION-ENDPOINT").setValue("/Cluster/Ethernet/Endpoints/UnicastEp1")
        result = obj.addStaticRemoteUnicastAddressRef(ref)
        assert result is obj  # method chaining
        assert obj.getStaticRemoteUnicastAddressRefs() == [ref]

        assert obj.addStaticRemoteUnicastAddressRef(None) is obj  # None is a no-op
        assert obj.getStaticRemoteUnicastAddressRefs() == [ref]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.getLocalUnicastAddressRef.__doc__) == self.LOCAL_UNICAST_ADDRESS_NOTE
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.setLocalUnicastAddressRef.__doc__) == (
            self.LOCAL_UNICAST_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing localUnicastAddressRef."
        )
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.getMinorVersion.__doc__) == self.MINOR_VERSION_NOTE
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.setMinorVersion.__doc__) == (self.MINOR_VERSION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing minorVersion.")
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.addProvidedDdsOperation.__doc__) == (
            self.PROVIDED_DDS_OPERATION_NOTE + "\n\nA None value is a no-op and does not extend the providedDdsOperations list."
        )
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.getProvidedDdsOperations.__doc__) == self.PROVIDED_DDS_OPERATION_NOTE
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.addProvidedDdsServiceInstanceEvent.__doc__) == (
            self.PROVIDED_DDS_SERVICE_INSTANCE_EVENT_NOTE + "\n\nA None value is a no-op and does not extend the providedDdsServiceInstanceEvents list."
        )
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.getProvidedDdsServiceInstanceEvents.__doc__) == self.PROVIDED_DDS_SERVICE_INSTANCE_EVENT_NOTE
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.getStaticRemoteMulticastAddressRef.__doc__) == self.STATIC_REMOTE_MULTICAST_ADDRESS_NOTE
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.setStaticRemoteMulticastAddressRef.__doc__) == (
            self.STATIC_REMOTE_MULTICAST_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing staticRemoteMulticastAddressRef."
        )
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.addStaticRemoteUnicastAddressRef.__doc__) == (
            self.STATIC_REMOTE_UNICAST_ADDRESS_NOTE + "\n\nA None value is a no-op and does not extend the staticRemoteUnicastAddressRefs list."
        )
        assert inspect.cleandoc(DdsCpProvidedServiceInstance.getStaticRemoteUnicastAddressRefs.__doc__) == self.STATIC_REMOTE_UNICAST_ADDRESS_NOTE


class TestDdsDurability:
    """
    Test class for DdsDurability functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.181, p.530
    """

    CLASS_NOTE = "Describes the DDS DURABILITY QoS policy. Tags: atp.Status=candidate"
    DURABILITY_KIND_NOTE = 'See "DURABILITY" chapter in DDS. Tags: atp.Status=candidate'

    def _create_durability(self) -> DdsDurability:
        return DdsDurability()

    def test_initialization(self):
        """
        Test that a new DdsDurability initializes all attributes to their defaults.
        """
        obj = self._create_durability()

        assert obj.getDurabilityKind() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsDurability derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsDurability, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsDurability.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsDurability.__init__.__doc__ is None

    def test_get_set_durability_kind(self):
        """
        Test getDurabilityKind and setDurabilityKind round-trip and None no-op.
        """
        obj = self._create_durability()

        value = DdsDurabilityKindEnum().setValue(DdsDurabilityKindEnum.TRANSIENT_LOCAL)
        result = obj.setDurabilityKind(value)
        assert result is obj  # method chaining
        assert obj.getDurabilityKind() is value
        assert obj.getDurabilityKind().getValue() == DdsDurabilityKindEnum.TRANSIENT_LOCAL

        result = obj.setDurabilityKind(None)
        assert result is obj  # method chaining with None
        assert obj.getDurabilityKind() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsDurability.getDurabilityKind.__doc__) == self.DURABILITY_KIND_NOTE
        assert inspect.cleandoc(DdsDurability.setDurabilityKind.__doc__) == (self.DURABILITY_KIND_NOTE + "\n\nA None value is a no-op and does not overwrite an existing durabilityKind.")


class TestDdsDurabilityService:
    """
    Test class for DdsDurabilityService functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.183, p.531
    """

    CLASS_NOTE = "Describes the DDS DURABILITY_SERVICE QoS policy. Tags: atp.Status=candidate"
    CLEANUP_DELAY_NOTE = 'See "DURABILITY_SERVICE" chapter in DDS. Time given in seconds. Tags: atp.Status=candidate'
    HISTORY_DEPTH_NOTE = 'See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate'
    HISTORY_KIND_NOTE = 'See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate'
    MAX_INSTANCES_NOTE = 'See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate'
    MAX_SAMPLES_NOTE = 'See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate'
    MAX_SAMPLES_PER_INSTANCE_NOTE = 'See "DURABILITY_SERVICE" chapter in DDS. Tags: atp.Status=candidate'

    def _create_durability_service(self) -> DdsDurabilityService:
        return DdsDurabilityService()

    def test_initialization(self):
        """
        Test that a new DdsDurabilityService initializes all attributes to their defaults.
        """
        obj = self._create_durability_service()

        assert obj.getDurabilityServiceCleanupDelay() is None
        assert obj.getDurabilityServiceHistoryDepth() is None
        assert obj.getDurabilityServiceHistoryKind() is None
        assert obj.getDurabilityServiceMaxInstances() is None
        assert obj.getDurabilityServiceMaxSamples() is None
        assert obj.getDurabilityServiceMaxSamplesPerInstance() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsDurabilityService derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsDurabilityService, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsDurabilityService.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsDurabilityService.__init__.__doc__ is None

    def test_get_set_durability_service_cleanup_delay(self):
        """
        Test getDurabilityServiceCleanupDelay and setDurabilityServiceCleanupDelay round-trip and None no-op.
        """
        obj = self._create_durability_service()

        value = Float().setValue("1.5")
        result = obj.setDurabilityServiceCleanupDelay(value)
        assert result is obj  # method chaining
        assert obj.getDurabilityServiceCleanupDelay() is value
        assert obj.getDurabilityServiceCleanupDelay().getValue() == 1.5

        result = obj.setDurabilityServiceCleanupDelay(None)
        assert result is obj  # method chaining with None
        assert obj.getDurabilityServiceCleanupDelay() is value  # None is a no-op

    def test_get_set_durability_service_history_depth(self):
        """
        Test getDurabilityServiceHistoryDepth and setDurabilityServiceHistoryDepth round-trip and None no-op.
        """
        obj = self._create_durability_service()

        value = PositiveInteger().setValue("4")
        result = obj.setDurabilityServiceHistoryDepth(value)
        assert result is obj  # method chaining
        assert obj.getDurabilityServiceHistoryDepth() is value
        assert obj.getDurabilityServiceHistoryDepth().getValue() == 4

        result = obj.setDurabilityServiceHistoryDepth(None)
        assert result is obj  # method chaining with None
        assert obj.getDurabilityServiceHistoryDepth() is value  # None is a no-op

    def test_get_set_durability_service_history_kind(self):
        """
        Test getDurabilityServiceHistoryKind and setDurabilityServiceHistoryKind round-trip and None no-op.
        """
        obj = self._create_durability_service()

        value = DdsDurabilityServiceHistoryKindEnum().setValue(DdsDurabilityServiceHistoryKindEnum.KEEP_LAST)
        result = obj.setDurabilityServiceHistoryKind(value)
        assert result is obj  # method chaining
        assert obj.getDurabilityServiceHistoryKind() is value
        assert obj.getDurabilityServiceHistoryKind().getValue() == DdsDurabilityServiceHistoryKindEnum.KEEP_LAST

        result = obj.setDurabilityServiceHistoryKind(None)
        assert result is obj  # method chaining with None
        assert obj.getDurabilityServiceHistoryKind() is value  # None is a no-op

    def test_get_set_durability_service_max_instances(self):
        """
        Test getDurabilityServiceMaxInstances and setDurabilityServiceMaxInstances round-trip and None no-op.
        """
        obj = self._create_durability_service()

        value = PositiveInteger().setValue("8")
        result = obj.setDurabilityServiceMaxInstances(value)
        assert result is obj  # method chaining
        assert obj.getDurabilityServiceMaxInstances() is value
        assert obj.getDurabilityServiceMaxInstances().getValue() == 8

        result = obj.setDurabilityServiceMaxInstances(None)
        assert result is obj  # method chaining with None
        assert obj.getDurabilityServiceMaxInstances() is value  # None is a no-op

    def test_get_set_durability_service_max_samples(self):
        """
        Test getDurabilityServiceMaxSamples and setDurabilityServiceMaxSamples round-trip and None no-op.
        """
        obj = self._create_durability_service()

        value = PositiveInteger().setValue("16")
        result = obj.setDurabilityServiceMaxSamples(value)
        assert result is obj  # method chaining
        assert obj.getDurabilityServiceMaxSamples() is value
        assert obj.getDurabilityServiceMaxSamples().getValue() == 16

        result = obj.setDurabilityServiceMaxSamples(None)
        assert result is obj  # method chaining with None
        assert obj.getDurabilityServiceMaxSamples() is value  # None is a no-op

    def test_get_set_durability_service_max_samples_per_instance(self):
        """
        Test getDurabilityServiceMaxSamplesPerInstance and setDurabilityServiceMaxSamplesPerInstance round-trip and None no-op.
        """
        obj = self._create_durability_service()

        value = PositiveInteger().setValue("32")
        result = obj.setDurabilityServiceMaxSamplesPerInstance(value)
        assert result is obj  # method chaining
        assert obj.getDurabilityServiceMaxSamplesPerInstance() is value
        assert obj.getDurabilityServiceMaxSamplesPerInstance().getValue() == 32

        result = obj.setDurabilityServiceMaxSamplesPerInstance(None)
        assert result is obj  # method chaining with None
        assert obj.getDurabilityServiceMaxSamplesPerInstance() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(DdsDurabilityService.getDurabilityServiceCleanupDelay.__doc__) == self.CLEANUP_DELAY_NOTE
        assert inspect.cleandoc(DdsDurabilityService.setDurabilityServiceCleanupDelay.__doc__) == (self.CLEANUP_DELAY_NOTE + none_no_op % "durabilityServiceCleanupDelay")
        assert inspect.cleandoc(DdsDurabilityService.getDurabilityServiceHistoryDepth.__doc__) == self.HISTORY_DEPTH_NOTE
        assert inspect.cleandoc(DdsDurabilityService.setDurabilityServiceHistoryDepth.__doc__) == (self.HISTORY_DEPTH_NOTE + none_no_op % "durabilityServiceHistoryDepth")
        assert inspect.cleandoc(DdsDurabilityService.getDurabilityServiceHistoryKind.__doc__) == self.HISTORY_KIND_NOTE
        assert inspect.cleandoc(DdsDurabilityService.setDurabilityServiceHistoryKind.__doc__) == (self.HISTORY_KIND_NOTE + none_no_op % "durabilityServiceHistoryKind")
        assert inspect.cleandoc(DdsDurabilityService.getDurabilityServiceMaxInstances.__doc__) == self.MAX_INSTANCES_NOTE
        assert inspect.cleandoc(DdsDurabilityService.setDurabilityServiceMaxInstances.__doc__) == (self.MAX_INSTANCES_NOTE + none_no_op % "durabilityServiceMaxInstances")
        assert inspect.cleandoc(DdsDurabilityService.getDurabilityServiceMaxSamples.__doc__) == self.MAX_SAMPLES_NOTE
        assert inspect.cleandoc(DdsDurabilityService.setDurabilityServiceMaxSamples.__doc__) == (self.MAX_SAMPLES_NOTE + none_no_op % "durabilityServiceMaxSamples")
        assert inspect.cleandoc(DdsDurabilityService.getDurabilityServiceMaxSamplesPerInstance.__doc__) == self.MAX_SAMPLES_PER_INSTANCE_NOTE
        assert inspect.cleandoc(DdsDurabilityService.setDurabilityServiceMaxSamplesPerInstance.__doc__) == (self.MAX_SAMPLES_PER_INSTANCE_NOTE + none_no_op % "durabilityServiceMaxSamplesPerInstance")


class TestDdsDeadline:
    """
    Test class for DdsDeadline functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.185, p.532
    """

    CLASS_NOTE = "Describes the DDS DEADLINE QoS policy. Tags: atp.Status=candidate"
    DEADLINE_PERIOD_NOTE = 'See "DEADLINE" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate'

    def _create_deadline(self) -> DdsDeadline:
        return DdsDeadline()

    def test_initialization(self):
        """
        Test that a new DdsDeadline initializes all attributes to their defaults.
        """
        obj = self._create_deadline()

        assert obj.getDeadlinePeriod() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsDeadline derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsDeadline, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsDeadline.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsDeadline.__init__.__doc__ is None

    def test_get_set_deadline_period(self):
        """
        Test getDeadlinePeriod and setDeadlinePeriod round-trip and None no-op.
        """
        obj = self._create_deadline()

        value = Float().setValue("0.5")
        result = obj.setDeadlinePeriod(value)
        assert result is obj  # method chaining
        assert obj.getDeadlinePeriod() is value
        assert obj.getDeadlinePeriod().getValue() == 0.5

        result = obj.setDeadlinePeriod(None)
        assert result is obj  # method chaining with None
        assert obj.getDeadlinePeriod() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsDeadline.getDeadlinePeriod.__doc__) == self.DEADLINE_PERIOD_NOTE
        assert inspect.cleandoc(DdsDeadline.setDeadlinePeriod.__doc__) == (self.DEADLINE_PERIOD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing deadlinePeriod.")


class TestDdsLatencyBudget:
    """
    Test class for DdsLatencyBudget functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.186, p.532
    """

    CLASS_NOTE = "Describes the DDS LATENCY_BUDGET QoS policy. Tags: atp.Status=candidate"
    LATENCY_BUDGET_DURATION_NOTE = 'See "LATENCY_BUDGET" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate'

    def _create_latency_budget(self) -> DdsLatencyBudget:
        return DdsLatencyBudget()

    def test_initialization(self):
        """
        Test that a new DdsLatencyBudget initializes all attributes to their defaults.
        """
        obj = self._create_latency_budget()

        assert obj.getLatencyBudgetDuration() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsLatencyBudget derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsLatencyBudget, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsLatencyBudget.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsLatencyBudget.__init__.__doc__ is None

    def test_get_set_latency_budget_duration(self):
        """
        Test getLatencyBudgetDuration and setLatencyBudgetDuration round-trip and None no-op.
        """
        obj = self._create_latency_budget()

        value = Float().setValue("0.1")
        result = obj.setLatencyBudgetDuration(value)
        assert result is obj  # method chaining
        assert obj.getLatencyBudgetDuration() is value
        assert obj.getLatencyBudgetDuration().getValue() == 0.1

        result = obj.setLatencyBudgetDuration(None)
        assert result is obj  # method chaining with None
        assert obj.getLatencyBudgetDuration() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsLatencyBudget.getLatencyBudgetDuration.__doc__) == self.LATENCY_BUDGET_DURATION_NOTE
        assert inspect.cleandoc(DdsLatencyBudget.setLatencyBudgetDuration.__doc__) == (
            self.LATENCY_BUDGET_DURATION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing latencyBudgetDuration."
        )


class TestDdsOwnership:
    """
    Test class for DdsOwnership functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.187, p.532
    """

    CLASS_NOTE = "Describes the DDS OWNERSHIP QoS policy. Tags: atp.Status=candidate"
    OWNERSHIP_KIND_NOTE = 'See "OWNERSHIP" chapter of DDS. Tags: atp.Status=candidate'

    def _create_ownership(self) -> DdsOwnership:
        return DdsOwnership()

    def test_initialization(self):
        """
        Test that a new DdsOwnership initializes all attributes to their defaults.
        """
        obj = self._create_ownership()

        assert obj.getOwnershipKind() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsOwnership derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsOwnership, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsOwnership.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsOwnership.__init__.__doc__ is None

    def test_get_set_ownership_kind(self):
        """
        Test getOwnershipKind and setOwnershipKind round-trip and None no-op.
        """
        obj = self._create_ownership()

        value = DdsOwnershipKindEnum().setValue(DdsOwnershipKindEnum.EXCLUSIVE)
        result = obj.setOwnershipKind(value)
        assert result is obj  # method chaining
        assert obj.getOwnershipKind() is value
        assert obj.getOwnershipKind().getValue() == DdsOwnershipKindEnum.EXCLUSIVE

        result = obj.setOwnershipKind(None)
        assert result is obj  # method chaining with None
        assert obj.getOwnershipKind() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsOwnership.getOwnershipKind.__doc__) == self.OWNERSHIP_KIND_NOTE
        assert inspect.cleandoc(DdsOwnership.setOwnershipKind.__doc__) == (self.OWNERSHIP_KIND_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ownershipKind.")


class TestDdsOwnershipStrength:
    """
    Test class for DdsOwnershipStrength functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.189, p.533
    """

    CLASS_NOTE = "Describes the DDS OWNERSHIP_STRENGTH QoS policy. Tags: atp.Status=candidate"
    OWNERSHIP_STRENGTH_NOTE = 'See "OWNERSHIP_STRENGTH" chapter of DDS. Tags: atp.Status=candidate'

    def _create_ownership_strength(self) -> DdsOwnershipStrength:
        return DdsOwnershipStrength()

    def test_initialization(self):
        """
        Test that a new DdsOwnershipStrength initializes all attributes to their defaults.
        """
        obj = self._create_ownership_strength()

        assert obj.getOwnershipStrength() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsOwnershipStrength derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsOwnershipStrength, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsOwnershipStrength.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsOwnershipStrength.__init__.__doc__ is None

    def test_get_set_ownership_strength(self):
        """
        Test getOwnershipStrength and setOwnershipStrength round-trip and None no-op.
        """
        obj = self._create_ownership_strength()

        value = PositiveInteger().setValue("5")
        result = obj.setOwnershipStrength(value)
        assert result is obj  # method chaining
        assert obj.getOwnershipStrength() is value
        assert obj.getOwnershipStrength().getValue() == 5

        result = obj.setOwnershipStrength(None)
        assert result is obj  # method chaining with None
        assert obj.getOwnershipStrength() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DdsOwnershipStrength.getOwnershipStrength.__doc__) == self.OWNERSHIP_STRENGTH_NOTE
        assert inspect.cleandoc(DdsOwnershipStrength.setOwnershipStrength.__doc__) == (
            self.OWNERSHIP_STRENGTH_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ownershipStrength."
        )


class TestDdsLiveliness:
    """
    Test class for DdsLiveliness functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.190, p.534
    """

    CLASS_NOTE = "Describes the DDS LIVELINESS QoS policy. Tags: atp.Status=candidate"
    LIVELINESS_LEASE_DURATION_NOTE = 'See "LIVELINESS" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate'
    LIVENESS_KIND_NOTE = 'See "LIVELINESS" chapter of DDS. Tags: atp.Status=candidate'

    def _create_liveliness(self) -> DdsLiveliness:
        return DdsLiveliness()

    def test_initialization(self):
        """
        Test that a new DdsLiveliness initializes all attributes to their defaults.
        """
        obj = self._create_liveliness()

        assert obj.getLivelinessLeaseDuration() is None
        assert obj.getLivenessKind() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsLiveliness derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsLiveliness, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsLiveliness.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsLiveliness.__init__.__doc__ is None

    def test_get_set_liveliness_lease_duration(self):
        """
        Test getLivelinessLeaseDuration and setLivelinessLeaseDuration round-trip and None no-op.
        """
        obj = self._create_liveliness()

        value = Float().setValue("10.0")
        result = obj.setLivelinessLeaseDuration(value)
        assert result is obj  # method chaining
        assert obj.getLivelinessLeaseDuration() is value
        assert obj.getLivelinessLeaseDuration().getValue() == 10.0

        result = obj.setLivelinessLeaseDuration(None)
        assert result is obj  # method chaining with None
        assert obj.getLivelinessLeaseDuration() is value  # None is a no-op

    def test_get_set_liveness_kind(self):
        """
        Test getLivenessKind and setLivenessKind round-trip and None no-op.
        """
        obj = self._create_liveliness()

        value = DdsLivenessKindEnum().setValue(DdsLivenessKindEnum.MANUAL_BY_TOPIC)
        result = obj.setLivenessKind(value)
        assert result is obj  # method chaining
        assert obj.getLivenessKind() is value
        assert obj.getLivenessKind().getValue() == DdsLivenessKindEnum.MANUAL_BY_TOPIC

        result = obj.setLivenessKind(None)
        assert result is obj  # method chaining with None
        assert obj.getLivenessKind() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(DdsLiveliness.getLivelinessLeaseDuration.__doc__) == self.LIVELINESS_LEASE_DURATION_NOTE
        assert inspect.cleandoc(DdsLiveliness.setLivelinessLeaseDuration.__doc__) == (self.LIVELINESS_LEASE_DURATION_NOTE + none_no_op % "livelinessLeaseDuration")
        assert inspect.cleandoc(DdsLiveliness.getLivenessKind.__doc__) == self.LIVENESS_KIND_NOTE
        assert inspect.cleandoc(DdsLiveliness.setLivenessKind.__doc__) == (self.LIVENESS_KIND_NOTE + none_no_op % "livenessKind")


class TestDdsReliability:
    """
    Test class for DdsReliability functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.192, p.535
    """

    CLASS_NOTE = "Describes the DDS RELIABILITY QoS policy. Tags: atp.Status=candidate"
    RELIABILITY_KIND_NOTE = 'See "RELIABILITY" chapter of DDS. Tags: atp.Status=candidate'
    RELIABILITY_MAX_BLOCKING_TIME_NOTE = 'See "RELIABILITY" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate'

    def _create_reliability(self) -> DdsReliability:
        return DdsReliability()

    def test_initialization(self):
        """
        Test that a new DdsReliability initializes all attributes to their defaults.
        """
        obj = self._create_reliability()

        assert obj.getReliabilityKind() is None
        assert obj.getReliabilityMaxBlockingTime() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsReliability derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsReliability, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsReliability.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsReliability.__init__.__doc__ is None

    def test_get_set_reliability_kind(self):
        """
        Test getReliabilityKind and setReliabilityKind round-trip and None no-op.
        """
        obj = self._create_reliability()

        value = DdsReliabilityKindEnum().setValue(DdsReliabilityKindEnum.RELIABLE)
        result = obj.setReliabilityKind(value)
        assert result is obj  # method chaining
        assert obj.getReliabilityKind() is value
        assert obj.getReliabilityKind().getValue() == DdsReliabilityKindEnum.RELIABLE

        result = obj.setReliabilityKind(None)
        assert result is obj  # method chaining with None
        assert obj.getReliabilityKind() is value  # None is a no-op

    def test_get_set_reliability_max_blocking_time(self):
        """
        Test getReliabilityMaxBlockingTime and setReliabilityMaxBlockingTime round-trip and None no-op.
        """
        obj = self._create_reliability()

        value = Float().setValue("0.5")
        result = obj.setReliabilityMaxBlockingTime(value)
        assert result is obj  # method chaining
        assert obj.getReliabilityMaxBlockingTime() is value
        assert obj.getReliabilityMaxBlockingTime().getValue() == 0.5

        result = obj.setReliabilityMaxBlockingTime(None)
        assert result is obj  # method chaining with None
        assert obj.getReliabilityMaxBlockingTime() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(DdsReliability.getReliabilityKind.__doc__) == self.RELIABILITY_KIND_NOTE
        assert inspect.cleandoc(DdsReliability.setReliabilityKind.__doc__) == (self.RELIABILITY_KIND_NOTE + none_no_op % "reliabilityKind")
        assert inspect.cleandoc(DdsReliability.getReliabilityMaxBlockingTime.__doc__) == self.RELIABILITY_MAX_BLOCKING_TIME_NOTE
        assert inspect.cleandoc(DdsReliability.setReliabilityMaxBlockingTime.__doc__) == (self.RELIABILITY_MAX_BLOCKING_TIME_NOTE + none_no_op % "reliabilityMaxBlockingTime")


class TestDdsTransportPriority:
    """
    Test class for DdsTransportPriority functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.194, p.535
    """

    CLASS_NOTE = "Describes the DDS TRANSPORT_PRIORITY QoS policy. Tags: atp.Status=candidate"
    TRANSPORT_PRIORITY_NOTE = 'See "TRANSPORT_PRIORITY" chapter of DDS. Tags: atp.Status=candidate'

    def _create_transport_priority(self) -> DdsTransportPriority:
        return DdsTransportPriority()

    def test_initialization(self):
        """
        Test that a new DdsTransportPriority initializes all attributes to their defaults.
        """
        obj = self._create_transport_priority()

        assert obj.getTransportPriority() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsTransportPriority derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsTransportPriority, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsTransportPriority.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsTransportPriority.__init__.__doc__ is None

    def test_get_set_transport_priority(self):
        """
        Test getTransportPriority and setTransportPriority round-trip and None no-op.
        """
        obj = self._create_transport_priority()

        value = PositiveInteger().setValue("4")
        result = obj.setTransportPriority(value)
        assert result is obj  # method chaining
        assert obj.getTransportPriority() is value
        assert obj.getTransportPriority().getValue() == 4

        result = obj.setTransportPriority(None)
        assert result is obj  # method chaining with None
        assert obj.getTransportPriority() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(DdsTransportPriority.getTransportPriority.__doc__) == self.TRANSPORT_PRIORITY_NOTE
        assert inspect.cleandoc(DdsTransportPriority.setTransportPriority.__doc__) == (self.TRANSPORT_PRIORITY_NOTE + none_no_op % "transportPriority")


class TestDdsLifespan:
    """
    Test class for DdsLifespan functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.195, p.536
    """

    CLASS_NOTE = "Describes the DDS LIFESPAN QoS policy. Tags: atp.Status=candidate"
    LIFESPAN_DURATION_NOTE = 'See "LIFESPAN" chapter of DDS. Time given in seconds. Tags: atp.Status=candidate'

    def _create_lifespan(self) -> DdsLifespan:
        return DdsLifespan()

    def test_initialization(self):
        """
        Test that a new DdsLifespan initializes all attributes to their defaults.
        """
        obj = self._create_lifespan()

        assert obj.getLifespanDuration() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsLifespan derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsLifespan, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsLifespan.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsLifespan.__init__.__doc__ is None

    def test_get_set_lifespan_duration(self):
        """
        Test getLifespanDuration and setLifespanDuration round-trip and None no-op.
        """
        obj = self._create_lifespan()

        value = Float().setValue("10.0")
        result = obj.setLifespanDuration(value)
        assert result is obj  # method chaining
        assert obj.getLifespanDuration() is value
        assert obj.getLifespanDuration().getValue() == 10.0

        result = obj.setLifespanDuration(None)
        assert result is obj  # method chaining with None
        assert obj.getLifespanDuration() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(DdsLifespan.getLifespanDuration.__doc__) == self.LIFESPAN_DURATION_NOTE
        assert inspect.cleandoc(DdsLifespan.setLifespanDuration.__doc__) == (self.LIFESPAN_DURATION_NOTE + none_no_op % "lifespanDuration")


class TestDdsDestinationOrder:
    """
    Test class for DdsDestinationOrder functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.196, p.536
    """

    CLASS_NOTE = "Describes the DDS DESTINATION_ORDER QoS policy. Tags: atp.Status=candidate"
    DESTINATION_ORDER_KIND_NOTE = 'See "DESTINATION_ORDER" chapter of DDS. Tags: atp.Status=candidate'

    def _create_destination_order(self) -> DdsDestinationOrder:
        return DdsDestinationOrder()

    def test_initialization(self):
        """
        Test that a new DdsDestinationOrder initializes all attributes to their defaults.
        """
        obj = self._create_destination_order()

        assert obj.getDestinationOrderKind() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsDestinationOrder derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsDestinationOrder, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsDestinationOrder.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsDestinationOrder.__init__.__doc__ is None

    def test_get_set_destination_order_kind(self):
        """
        Test getDestinationOrderKind and setDestinationOrderKind round-trip and None no-op.
        """
        obj = self._create_destination_order()

        value = DdsDestinationOrderKindEnum().setValue(DdsDestinationOrderKindEnum.BY_SOURCE_TIMESTAMP)
        result = obj.setDestinationOrderKind(value)
        assert result is obj  # method chaining
        assert obj.getDestinationOrderKind() is value
        assert obj.getDestinationOrderKind().getValue() == DdsDestinationOrderKindEnum.BY_SOURCE_TIMESTAMP

        result = obj.setDestinationOrderKind(None)
        assert result is obj  # method chaining with None
        assert obj.getDestinationOrderKind() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(DdsDestinationOrder.getDestinationOrderKind.__doc__) == self.DESTINATION_ORDER_KIND_NOTE
        assert inspect.cleandoc(DdsDestinationOrder.setDestinationOrderKind.__doc__) == (self.DESTINATION_ORDER_KIND_NOTE + none_no_op % "destinationOrderKind")


class TestDdsHistory:
    """
    Test class for DdsHistory functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.198, p.537
    """

    CLASS_NOTE = "Describes the DDS HISTORY QoS policy. Tags: atp.Status=candidate"
    HISTORY_KIND_NOTE = 'See "HISTORY" chapter of DDS. Tags: atp.Status=candidate'
    HISTORY_ORDER_DEPTH_NOTE = 'See "HISTORY" chapter of DDS. Tags: atp.Status=candidate'

    def _create_history(self) -> DdsHistory:
        return DdsHistory()

    def test_initialization(self):
        """
        Test that a new DdsHistory initializes all attributes to their defaults.
        """
        obj = self._create_history()

        assert obj.getHistoryKind() is None
        assert obj.getHistoryOrderDepth() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsHistory derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsHistory, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsHistory.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsHistory.__init__.__doc__ is None

    def test_get_set_history_kind(self):
        """
        Test getHistoryKind and setHistoryKind round-trip and None no-op.
        """
        obj = self._create_history()

        value = DdsHistoryKindEnum().setValue(DdsHistoryKindEnum.KEEP_LAST)
        result = obj.setHistoryKind(value)
        assert result is obj  # method chaining
        assert obj.getHistoryKind() is value
        assert obj.getHistoryKind().getValue() == DdsHistoryKindEnum.KEEP_LAST

        result = obj.setHistoryKind(None)
        assert result is obj  # method chaining with None
        assert obj.getHistoryKind() is value  # None is a no-op

    def test_get_set_history_order_depth(self):
        """
        Test getHistoryOrderDepth and setHistoryOrderDepth round-trip and None no-op.
        """
        obj = self._create_history()

        value = PositiveInteger().setValue("4")
        result = obj.setHistoryOrderDepth(value)
        assert result is obj  # method chaining
        assert obj.getHistoryOrderDepth() is value
        assert obj.getHistoryOrderDepth().getValue() == 4

        result = obj.setHistoryOrderDepth(None)
        assert result is obj  # method chaining with None
        assert obj.getHistoryOrderDepth() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(DdsHistory.getHistoryKind.__doc__) == self.HISTORY_KIND_NOTE
        assert inspect.cleandoc(DdsHistory.setHistoryKind.__doc__) == (self.HISTORY_KIND_NOTE + none_no_op % "historyKind")
        assert inspect.cleandoc(DdsHistory.getHistoryOrderDepth.__doc__) == self.HISTORY_ORDER_DEPTH_NOTE
        assert inspect.cleandoc(DdsHistory.setHistoryOrderDepth.__doc__) == (self.HISTORY_ORDER_DEPTH_NOTE + none_no_op % "historyOrderDepth")


class TestBusMirrorCanIdRangeMapping:
    """
    Test class for BusMirrorCanIdRangeMapping functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.329, p.702
    """

    CLASS_NOTE = "This element defines a rule for remapping a set of CAN IDs."
    DESTINATION_BASE_ID_NOTE = "Base ID merged with the masked parts of the original CAN ID to form the mapped CAN ID."
    SOURCE_CAN_ID_CODE_NOTE = "Value to match masked original CAN IDs."
    SOURCE_CAN_ID_MASK_NOTE = "Mask applied to original CAN IDs before comparison."

    def _create_mapping(self) -> BusMirrorCanIdRangeMapping:
        return BusMirrorCanIdRangeMapping()

    def test_initialization(self):
        obj = self._create_mapping()

        assert obj.getDestinationBaseId() is None
        assert obj.getSourceCanIdCode() is None
        assert obj.getSourceCanIdMask() is None

    def test_is_ar_object_subclass(self):
        assert issubclass(BusMirrorCanIdRangeMapping, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(BusMirrorCanIdRangeMapping.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert BusMirrorCanIdRangeMapping.__init__.__doc__ is None

    def test_get_set_destination_base_id(self):
        obj = self._create_mapping()

        value = PositiveInteger().setValue("16")
        assert obj.setDestinationBaseId(value) is obj
        assert obj.getDestinationBaseId() is value
        assert obj.getDestinationBaseId().getValue() == 16

        obj.setDestinationBaseId(None)
        assert obj.getDestinationBaseId() is value

    def test_get_set_source_can_id_code(self):
        obj = self._create_mapping()

        value = PositiveInteger().setValue("40")
        assert obj.setSourceCanIdCode(value) is obj
        assert obj.getSourceCanIdCode() is value
        assert obj.getSourceCanIdCode().getValue() == 40

        obj.setSourceCanIdCode(None)
        assert obj.getSourceCanIdCode() is value

    def test_get_set_source_can_id_mask(self):
        obj = self._create_mapping()

        value = PositiveInteger().setValue("7")
        assert obj.setSourceCanIdMask(value) is obj
        assert obj.getSourceCanIdMask() is value
        assert obj.getSourceCanIdMask().getValue() == 7

        obj.setSourceCanIdMask(None)
        assert obj.getSourceCanIdMask() is value

    def test_accessor_docstrings_are_spec_note_verbatim(self):
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(BusMirrorCanIdRangeMapping.getDestinationBaseId.__doc__) == self.DESTINATION_BASE_ID_NOTE
        assert inspect.cleandoc(BusMirrorCanIdRangeMapping.setDestinationBaseId.__doc__) == (self.DESTINATION_BASE_ID_NOTE + none_no_op % "destinationBaseId")
        assert inspect.cleandoc(BusMirrorCanIdRangeMapping.getSourceCanIdCode.__doc__) == self.SOURCE_CAN_ID_CODE_NOTE
        assert inspect.cleandoc(BusMirrorCanIdRangeMapping.setSourceCanIdCode.__doc__) == (self.SOURCE_CAN_ID_CODE_NOTE + none_no_op % "sourceCanIdCode")
        assert inspect.cleandoc(BusMirrorCanIdRangeMapping.getSourceCanIdMask.__doc__) == self.SOURCE_CAN_ID_MASK_NOTE
        assert inspect.cleandoc(BusMirrorCanIdRangeMapping.setSourceCanIdMask.__doc__) == (self.SOURCE_CAN_ID_MASK_NOTE + none_no_op % "sourceCanIdMask")

    def test_type_hints_are_optional_positive_integer(self):
        getter_hints = typing.get_type_hints(BusMirrorCanIdRangeMapping.getDestinationBaseId)
        setter_hints = typing.get_type_hints(BusMirrorCanIdRangeMapping.setDestinationBaseId)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]


class TestBusMirrorCanIdToCanIdMapping:
    """
    Test class for BusMirrorCanIdToCanIdMapping functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.330, p.702
    """

    CLASS_NOTE = "This element defines a rule for remapping a single CAN ID."
    REMAPPED_CAN_ID_NOTE = "This attribute defines the CanId on the targetChannel."
    SOUCE_CAN_ID_NOTE = "This reference points to the sourceFrame with sourceCan Id on the sourceChannel."

    def _create_mapping(self) -> BusMirrorCanIdToCanIdMapping:
        return BusMirrorCanIdToCanIdMapping()

    def test_initialization(self):
        obj = self._create_mapping()

        assert obj.getRemappedCanId() is None
        assert obj.getSouceCanIdRef() is None

    def test_is_ar_object_subclass(self):
        assert issubclass(BusMirrorCanIdToCanIdMapping, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(BusMirrorCanIdToCanIdMapping.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert BusMirrorCanIdToCanIdMapping.__init__.__doc__ is None

    def test_get_set_remapped_can_id(self):
        obj = self._create_mapping()

        value = PositiveInteger().setValue("512")
        assert obj.setRemappedCanId(value) is obj
        assert obj.getRemappedCanId() is value
        assert obj.getRemappedCanId().getValue() == 512

        obj.setRemappedCanId(None)
        assert obj.getRemappedCanId() is value

    def test_get_set_souce_can_id_ref(self):
        obj = self._create_mapping()

        value = RefType().setValue("/Can/FrameTriggering")
        value.setDest("CAN-FRAME-TRIGGERING")
        assert obj.setSouceCanIdRef(value) is obj
        assert obj.getSouceCanIdRef() is value
        assert obj.getSouceCanIdRef().getValue() == "/Can/FrameTriggering"

        obj.setSouceCanIdRef(None)
        assert obj.getSouceCanIdRef() is value

    def test_accessor_docstrings_are_spec_note_verbatim(self):
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(BusMirrorCanIdToCanIdMapping.getRemappedCanId.__doc__) == self.REMAPPED_CAN_ID_NOTE
        assert inspect.cleandoc(BusMirrorCanIdToCanIdMapping.setRemappedCanId.__doc__) == (self.REMAPPED_CAN_ID_NOTE + none_no_op % "remappedCanId")
        assert inspect.cleandoc(BusMirrorCanIdToCanIdMapping.getSouceCanIdRef.__doc__) == self.SOUCE_CAN_ID_NOTE
        assert inspect.cleandoc(BusMirrorCanIdToCanIdMapping.setSouceCanIdRef.__doc__) == (self.SOUCE_CAN_ID_NOTE + none_no_op % "souceCanIdRef")

    def test_type_hints_are_spec_typed(self):
        getter_hints = typing.get_type_hints(BusMirrorCanIdToCanIdMapping.getSouceCanIdRef)
        setter_hints = typing.get_type_hints(BusMirrorCanIdToCanIdMapping.setSouceCanIdRef)
        assert getter_hints.get("return") == typing.Optional[RefType]
        assert setter_hints.get("value") == typing.Optional[RefType]


class TestBusMirrorLinPidToCanIdMapping:
    """
    Test class for BusMirrorLinPidToCanIdMapping functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.331, p.702
    """

    CLASS_NOTE = "This element defines a rule for remapping a single LIN Frame."
    REMAPPED_CAN_ID_NOTE = "This attribute defines the CanId on the targetChannel."
    SOURCE_LIN_PID_NOTE = "This reference points to the sourceFrame with sourceCan Id on the sourceChannel."

    def _create_mapping(self) -> BusMirrorLinPidToCanIdMapping:
        return BusMirrorLinPidToCanIdMapping()

    def test_initialization(self):
        obj = self._create_mapping()

        assert obj.getRemappedCanId() is None
        assert obj.getSourceLinPidRef() is None

    def test_is_ar_object_subclass(self):
        assert issubclass(BusMirrorLinPidToCanIdMapping, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(BusMirrorLinPidToCanIdMapping.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert BusMirrorLinPidToCanIdMapping.__init__.__doc__ is None

    def test_get_set_remapped_can_id(self):
        obj = self._create_mapping()

        value = PositiveInteger().setValue("768")
        assert obj.setRemappedCanId(value) is obj
        assert obj.getRemappedCanId() is value
        assert obj.getRemappedCanId().getValue() == 768

        obj.setRemappedCanId(None)
        assert obj.getRemappedCanId() is value

    def test_get_set_source_lin_pid_ref(self):
        obj = self._create_mapping()

        value = RefType().setValue("/Lin/FrameTriggering")
        value.setDest("LIN-FRAME-TRIGGERING")
        assert obj.setSourceLinPidRef(value) is obj
        assert obj.getSourceLinPidRef() is value
        assert obj.getSourceLinPidRef().getValue() == "/Lin/FrameTriggering"

        obj.setSourceLinPidRef(None)
        assert obj.getSourceLinPidRef() is value

    def test_accessor_docstrings_are_spec_note_verbatim(self):
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(BusMirrorLinPidToCanIdMapping.getRemappedCanId.__doc__) == self.REMAPPED_CAN_ID_NOTE
        assert inspect.cleandoc(BusMirrorLinPidToCanIdMapping.setRemappedCanId.__doc__) == (self.REMAPPED_CAN_ID_NOTE + none_no_op % "remappedCanId")
        assert inspect.cleandoc(BusMirrorLinPidToCanIdMapping.getSourceLinPidRef.__doc__) == self.SOURCE_LIN_PID_NOTE
        assert inspect.cleandoc(BusMirrorLinPidToCanIdMapping.setSourceLinPidRef.__doc__) == (self.SOURCE_LIN_PID_NOTE + none_no_op % "sourceLinPidRef")

    def test_type_hints_are_spec_typed(self):
        getter_hints = typing.get_type_hints(BusMirrorLinPidToCanIdMapping.getSourceLinPidRef)
        setter_hints = typing.get_type_hints(BusMirrorLinPidToCanIdMapping.setSourceLinPidRef)
        assert getter_hints.get("return") == typing.Optional[RefType]
        assert setter_hints.get("value") == typing.Optional[RefType]


class ConcreteAbstractGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    pass


class TestAbstractGlobalTimeDomainProps:
    """
    Test class for AbstractGlobalTimeDomainProps functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.2, p.859
    (abstract; subclasses CanGlobalTimeDomainProps, EthGlobalTimeDomainProps and
    FrGlobalTimeDomainProps — accessors exercised through a local concrete subclass
    per the abstract-class test convention. The table's Attribute column is a single
    "-" row, so the class owns no attributes of its own; the VARIATION-POINT slot of
    the XSD ABSTRACT-GLOBAL-TIME-DOMAIN-PROPS group is mixin-provided.)
    """

    CLASS_NOTE = "This abstract class enables a GlobalTimeDomain to specify additional properties."

    def test_abstract_initialization(self):
        """
        AbstractGlobalTimeDomainProps is abstract and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            AbstractGlobalTimeDomainProps()

    def test_is_ar_object_subclass_with_variation_point_capable(self):
        """
        Test that AbstractGlobalTimeDomainProps derives from ARObject per the Table 9.2 Base row
        and from VariationPointCapable (the atpVariation on the owning GlobalTimeDomain.globalTimeDomainProperty
        row makes the member class VP-capable; the XSD ABSTRACT-GLOBAL-TIME-DOMAIN-PROPS group carries
        VARIATION-POINT).
        """
        assert issubclass(AbstractGlobalTimeDomainProps, ARObject)
        assert issubclass(AbstractGlobalTimeDomainProps, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(AbstractGlobalTimeDomainProps.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert AbstractGlobalTimeDomainProps.__init__.__doc__ is None

    def test_no_own_methods(self):
        """
        Test that the class declares no accessors — Table 9.2 has no Attribute rows.
        """
        methods = [name for name, value in AbstractGlobalTimeDomainProps.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == []

    def test_concrete_subclass_initialization(self):
        """
        Test that a concrete subclass instantiates with all inherited state at defaults.
        """
        obj = ConcreteAbstractGlobalTimeDomainProps()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.getVariationPoint() is None

    def test_variation_point_base_accessors(self):
        """
        Exercise the inherited VariationPointCapable accessors: chaining, round-trip, None no-op.
        """
        obj = ConcreteAbstractGlobalTimeDomainProps()

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        variation_point = VariationPoint()
        assert obj.setVariationPoint(variation_point) is obj
        assert obj.getVariationPoint() is variation_point

        obj.setVariationPoint(None)
        assert obj.getVariationPoint() is variation_point  # None is a no-op


class TestNetworkSegmentIdentification:
    """
    Test class for NetworkSegmentIdentification functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.3, p.859
    """

    CLASS_NOTE = "This meta-class represents the ability to identify the PhysicalChannel on a system scope in a numerical way. " "One possible application of this approach is the Time Validation."
    NETWORK_SEGMENT_ID_NOTE = "This attribute represents the numerical identifier of a PhysicalChannel on system level scope."

    def _create_object(self) -> NetworkSegmentIdentification:
        return NetworkSegmentIdentification()

    def test_initialization(self):
        """
        Test that a new NetworkSegmentIdentification initializes all attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.getNetworkSegmentId() is None

    def test_is_ar_object_subclass(self):
        """
        Test that NetworkSegmentIdentification derives from ARObject per the Table 9.3 Base row.
        """
        assert issubclass(NetworkSegmentIdentification, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(NetworkSegmentIdentification.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert NetworkSegmentIdentification.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.3 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in NetworkSegmentIdentification.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getNetworkSegmentId",
            "setNetworkSegmentId",
        ]

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec PositiveInteger hint (0..1 row).
        """
        getter_hints = typing.get_type_hints(NetworkSegmentIdentification.getNetworkSegmentId)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(NetworkSegmentIdentification.setNetworkSegmentId)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is NetworkSegmentIdentification

    def test_get_set_network_segment_id(self):
        """
        Test getNetworkSegmentId and setNetworkSegmentId round-trip and None no-op.
        """
        obj = self._create_object()

        value = PositiveInteger()
        value.setValue("7")
        result = obj.setNetworkSegmentId(value)
        assert result is obj  # method chaining
        assert obj.getNetworkSegmentId() is value
        assert obj.getNetworkSegmentId().getValue() == 7

        result = obj.setNetworkSegmentId(None)
        assert result is obj  # method chaining with None
        assert obj.getNetworkSegmentId() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(NetworkSegmentIdentification.getNetworkSegmentId.__doc__) == self.NETWORK_SEGMENT_ID_NOTE
        assert inspect.cleandoc(NetworkSegmentIdentification.setNetworkSegmentId.__doc__) == (
            self.NETWORK_SEGMENT_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing networkSegmentId."
        )


class TestGlobalTimeCorrectionProps:
    """
    Test class for GlobalTimeCorrectionProps functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.7, p.862
    """

    CLASS_NOTE = "This meta-class defines the attributes for rate and offset correction."
    OFFSET_CORRECTION_ADAPTION_INTERVAL_NOTE = "Defines the interval during which the adaptive rate correction cancels out the rate- and time deviation."
    OFFSET_CORRECTION_JUMP_THRESHOLD_NOTE = (
        "Threshold for the correction method. Deviations below this value will be corrected by a linear reduction over a defined timespan. "
        "Values equal- and greater than this value will be corrected by immediately setting the correct time- and rate in form of a jump."
    )
    RATE_CORRECTION_MEASUREMENT_DURATION_NOTE = "Definition of the time span which is used to calculate the rate deviation."
    RATE_CORRECTIONS_PER_MEASUREMENT_DURATION_NOTE = "Defines the number of simultaneous rate measurements to determine the current rate deviation."

    def _create_object(self) -> GlobalTimeCorrectionProps:
        return GlobalTimeCorrectionProps()

    def test_initialization(self):
        """
        Test that a new GlobalTimeCorrectionProps initializes all attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getOffsetCorrectionAdaptionInterval() is None
        assert obj.getOffsetCorrectionJumpThreshold() is None
        assert obj.getRateCorrectionMeasurementDuration() is None
        assert obj.getRateCorrectionsPerMeasurementDuration() is None

    def test_is_ar_object_subclass(self):
        """
        Test that GlobalTimeCorrectionProps derives from ARObject per the Table 9.7 Base row.
        """
        assert issubclass(GlobalTimeCorrectionProps, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(GlobalTimeCorrectionProps.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert GlobalTimeCorrectionProps.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.7 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in GlobalTimeCorrectionProps.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getOffsetCorrectionAdaptionInterval",
            "setOffsetCorrectionAdaptionInterval",
            "getOffsetCorrectionJumpThreshold",
            "setOffsetCorrectionJumpThreshold",
            "getRateCorrectionMeasurementDuration",
            "setRateCorrectionMeasurementDuration",
            "getRateCorrectionsPerMeasurementDuration",
            "setRateCorrectionsPerMeasurementDuration",
        ]

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types (0..1 rows: TimeValue / PositiveInteger).
        """
        hints = typing.get_type_hints(GlobalTimeCorrectionProps.getOffsetCorrectionAdaptionInterval)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(GlobalTimeCorrectionProps.setOffsetCorrectionAdaptionInterval)
        assert hints.get("value") == typing.Optional[TimeValue]
        assert hints.get("return") is GlobalTimeCorrectionProps

        hints = typing.get_type_hints(GlobalTimeCorrectionProps.getOffsetCorrectionJumpThreshold)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(GlobalTimeCorrectionProps.getRateCorrectionMeasurementDuration)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(GlobalTimeCorrectionProps.getRateCorrectionsPerMeasurementDuration)
        assert hints.get("return") == typing.Optional[PositiveInteger]

    def test_get_set_offset_correction_adaption_interval(self):
        """
        Test getOffsetCorrectionAdaptionInterval and setOffsetCorrectionAdaptionInterval round-trip and None no-op.
        """
        obj = self._create_object()

        value = TimeValue()
        value.setValue("0.005")
        assert obj.setOffsetCorrectionAdaptionInterval(value) is obj
        assert obj.getOffsetCorrectionAdaptionInterval() is value
        assert obj.getOffsetCorrectionAdaptionInterval().getValue() == 0.005

        obj.setOffsetCorrectionAdaptionInterval(None)
        assert obj.getOffsetCorrectionAdaptionInterval() is value  # None is a no-op

    def test_get_set_offset_correction_jump_threshold(self):
        """
        Test getOffsetCorrectionJumpThreshold and setOffsetCorrectionJumpThreshold round-trip and None no-op.
        """
        obj = self._create_object()

        value = TimeValue()
        value.setValue("0.5")
        assert obj.setOffsetCorrectionJumpThreshold(value) is obj
        assert obj.getOffsetCorrectionJumpThreshold() is value

        obj.setOffsetCorrectionJumpThreshold(None)
        assert obj.getOffsetCorrectionJumpThreshold() is value  # None is a no-op

    def test_get_set_rate_correction_measurement_duration(self):
        """
        Test getRateCorrectionMeasurementDuration and setRateCorrectionMeasurementDuration round-trip and None no-op.
        """
        obj = self._create_object()

        value = TimeValue()
        value.setValue("2.0")
        assert obj.setRateCorrectionMeasurementDuration(value) is obj
        assert obj.getRateCorrectionMeasurementDuration() is value

        obj.setRateCorrectionMeasurementDuration(None)
        assert obj.getRateCorrectionMeasurementDuration() is value  # None is a no-op

    def test_get_set_rate_corrections_per_measurement_duration(self):
        """
        Test getRateCorrectionsPerMeasurementDuration and setRateCorrectionsPerMeasurementDuration round-trip and None no-op.
        """
        obj = self._create_object()

        value = PositiveInteger()
        value.setValue("3")
        assert obj.setRateCorrectionsPerMeasurementDuration(value) is obj
        assert obj.getRateCorrectionsPerMeasurementDuration() is value
        assert obj.getRateCorrectionsPerMeasurementDuration().getValue() == 3

        obj.setRateCorrectionsPerMeasurementDuration(None)
        assert obj.getRateCorrectionsPerMeasurementDuration() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(GlobalTimeCorrectionProps.getOffsetCorrectionAdaptionInterval.__doc__) == self.OFFSET_CORRECTION_ADAPTION_INTERVAL_NOTE
        assert inspect.cleandoc(GlobalTimeCorrectionProps.setOffsetCorrectionAdaptionInterval.__doc__) == (
            self.OFFSET_CORRECTION_ADAPTION_INTERVAL_NOTE + none_no_op % "offsetCorrectionAdaptionInterval"
        )
        assert inspect.cleandoc(GlobalTimeCorrectionProps.getOffsetCorrectionJumpThreshold.__doc__) == self.OFFSET_CORRECTION_JUMP_THRESHOLD_NOTE
        assert inspect.cleandoc(GlobalTimeCorrectionProps.setOffsetCorrectionJumpThreshold.__doc__) == (self.OFFSET_CORRECTION_JUMP_THRESHOLD_NOTE + none_no_op % "offsetCorrectionJumpThreshold")
        assert inspect.cleandoc(GlobalTimeCorrectionProps.getRateCorrectionMeasurementDuration.__doc__) == self.RATE_CORRECTION_MEASUREMENT_DURATION_NOTE
        assert inspect.cleandoc(GlobalTimeCorrectionProps.setRateCorrectionMeasurementDuration.__doc__) == (
            self.RATE_CORRECTION_MEASUREMENT_DURATION_NOTE + none_no_op % "rateCorrectionMeasurementDuration"
        )
        assert inspect.cleandoc(GlobalTimeCorrectionProps.getRateCorrectionsPerMeasurementDuration.__doc__) == self.RATE_CORRECTIONS_PER_MEASUREMENT_DURATION_NOTE
        assert inspect.cleandoc(GlobalTimeCorrectionProps.setRateCorrectionsPerMeasurementDuration.__doc__) == (
            self.RATE_CORRECTIONS_PER_MEASUREMENT_DURATION_NOTE + none_no_op % "rateCorrectionsPerMeasurementDuration"
        )


class TestDdsResourceLimits:
    """
    Test class for DdsResourceLimits functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.200, p.538
    """

    CLASS_NOTE = "Describes the DDS RESOURCE_LIMITS QoS policy. Tags: atp.Status=candidate"
    MAX_INSTANCES_NOTE = 'See "RESOURCE_LIMITS" chapter of DDS.'
    MAX_SAMPLES_NOTE = 'See "RESOURCE_LIMITS" chapter of DDS. Tags: atp.Status=candidate'
    MAX_SAMPLES_PER_INSTANCE_NOTE = 'See "RESOURCE_LIMITS" chapter of DDS.'

    def _create_resource_limits(self) -> DdsResourceLimits:
        return DdsResourceLimits()

    def test_initialization(self):
        """
        Test that a new DdsResourceLimits initializes all attributes to their defaults.
        """
        obj = self._create_resource_limits()

        assert obj.getMaxInstances() is None
        assert obj.getMaxSamples() is None
        assert obj.getMaxSamplesPerInstance() is None

    def test_is_ar_object_subclass(self):
        """
        Test that DdsResourceLimits derives from ARObject (confirmed queue row; Base column = ARObject only).
        """
        assert issubclass(DdsResourceLimits, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsResourceLimits.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsResourceLimits.__init__.__doc__ is None

    def test_get_set_max_instances(self):
        """
        Test getMaxInstances and setMaxInstances round-trip and None no-op.
        """
        obj = self._create_resource_limits()

        value = PositiveInteger().setValue("1")
        result = obj.setMaxInstances(value)
        assert result is obj
        assert obj.getMaxInstances() is value
        assert obj.getMaxInstances().getValue() == 1

        result = obj.setMaxInstances(None)
        assert result is obj
        assert obj.getMaxInstances() is value

    def test_get_set_max_samples(self):
        """
        Test getMaxSamples and setMaxSamples round-trip and None no-op.
        """
        obj = self._create_resource_limits()

        value = PositiveInteger().setValue("2")
        result = obj.setMaxSamples(value)
        assert result is obj
        assert obj.getMaxSamples() is value
        assert obj.getMaxSamples().getValue() == 2

        result = obj.setMaxSamples(None)
        assert result is obj
        assert obj.getMaxSamples() is value

    def test_get_set_max_samples_per_instance(self):
        """
        Test getMaxSamplesPerInstance and setMaxSamplesPerInstance round-trip and None no-op.
        """
        obj = self._create_resource_limits()

        value = PositiveInteger().setValue("4")
        result = obj.setMaxSamplesPerInstance(value)
        assert result is obj
        assert obj.getMaxSamplesPerInstance() is value
        assert obj.getMaxSamplesPerInstance().getValue() == 4

        result = obj.setMaxSamplesPerInstance(None)
        assert result is obj
        assert obj.getMaxSamplesPerInstance() is value

    def test_type_annotations(self):
        """
        Getter returns and setter parameters match the spec multiplicity (all 0..1 → Optional).
        """
        assert typing.get_type_hints(DdsResourceLimits.setMaxInstances)["value"] == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(DdsResourceLimits.getMaxInstances)["return"] == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(DdsResourceLimits.setMaxSamples)["value"] == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(DdsResourceLimits.setMaxSamplesPerInstance)["value"] == typing.Optional[PositiveInteger]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        none_no_op = "\n\nA None value is a no-op and does not overwrite an existing %s."
        assert inspect.cleandoc(DdsResourceLimits.getMaxInstances.__doc__) == self.MAX_INSTANCES_NOTE
        assert inspect.cleandoc(DdsResourceLimits.setMaxInstances.__doc__) == (self.MAX_INSTANCES_NOTE + none_no_op % "maxInstances")
        assert inspect.cleandoc(DdsResourceLimits.getMaxSamples.__doc__) == self.MAX_SAMPLES_NOTE
        assert inspect.cleandoc(DdsResourceLimits.setMaxSamples.__doc__) == (self.MAX_SAMPLES_NOTE + none_no_op % "maxSamples")
        assert inspect.cleandoc(DdsResourceLimits.getMaxSamplesPerInstance.__doc__) == self.MAX_SAMPLES_PER_INSTANCE_NOTE
        assert inspect.cleandoc(DdsResourceLimits.setMaxSamplesPerInstance.__doc__) == (self.MAX_SAMPLES_PER_INSTANCE_NOTE + none_no_op % "maxSamplesPerInstance")


class TestEthGlobalTimeManagedCouplingPort:
    """
    Test class for EthGlobalTimeManagedCouplingPort functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.17, p.875
    """

    CLASS_NOTE = "Specifies a CouplingPort which is managed by an Ethernet Global Time Domain."
    COUPLING_PORT_REF_NOTE = "Defines which CouplingPort is managed by this EthGlobalTimeManagedCouplingPort."
    GLOBAL_TIME_PORT_ROLE_NOTE = "This attribute defines the port behavior."
    GLOBAL_TIME_TX_PERIOD_NOTE = "This attribute defines the TX period in seconds"
    PDELAY_LATENCY_THRESHOLD_NOTE = "Threshold for calculated Pdelay. If a measured Pdelay exceeds pdelayLatencyThreshold, the measured Pdelay value is discarded."
    PDELAY_REQUEST_PERIOD_NOTE = "Defines the period for the pdelay request messages."
    PDELAY_RESP_AND_RESP_FOLLOW_UP_TIMEOUT_NOTE = "Timeout value for Pdelay_Resp and Pdelay_Resp_Follow_Up after a Pdelay_Req has been transmitted resp. a Pdelay_Resp has been received. A value of 0 or not defining this attribute deactivates this timeout observation."
    PDELAY_RESPONSE_ENABLED_NOTE = "Defines whether PDELAY RESPONSE and PDELAY RESPONSE FOLLOW UP shall be sent on this Coupling Port."

    def _create_object(self) -> EthGlobalTimeManagedCouplingPort:
        return EthGlobalTimeManagedCouplingPort()

    def test_initialization(self):
        """
        Test that a new EthGlobalTimeManagedCouplingPort initializes all attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.getCouplingPortRef() is None
        assert obj.getGlobalTimePortRole() is None
        assert obj.getGlobalTimeTxPeriod() is None
        assert obj.getPdelayLatencyThreshold() is None
        assert obj.getPdelayRequestPeriod() is None
        assert obj.getPdelayRespAndRespFollowUpTimeout() is None
        assert obj.getPdelayResponseEnabled() is None

    def test_is_ar_object_subclass(self):
        """
        Test that EthGlobalTimeManagedCouplingPort derives from ARObject per the Table 9.17 Base row.
        """
        assert issubclass(EthGlobalTimeManagedCouplingPort, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert EthGlobalTimeManagedCouplingPort.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.17 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in EthGlobalTimeManagedCouplingPort.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getCouplingPortRef",
            "setCouplingPortRef",
            "getGlobalTimePortRole",
            "setGlobalTimePortRole",
            "getGlobalTimeTxPeriod",
            "setGlobalTimeTxPeriod",
            "getPdelayLatencyThreshold",
            "setPdelayLatencyThreshold",
            "getPdelayRequestPeriod",
            "setPdelayRequestPeriod",
            "getPdelayRespAndRespFollowUpTimeout",
            "setPdelayRespAndRespFollowUpTimeout",
            "getPdelayResponseEnabled",
            "setPdelayResponseEnabled",
        ]

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types (0..1 rows).
        """
        hints = typing.get_type_hints(EthGlobalTimeManagedCouplingPort.getCouplingPortRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(EthGlobalTimeManagedCouplingPort.setCouplingPortRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is EthGlobalTimeManagedCouplingPort

        hints = typing.get_type_hints(EthGlobalTimeManagedCouplingPort.getGlobalTimePortRole)
        assert hints.get("return") == typing.Optional[GlobalTimePortRoleEnum]
        hints = typing.get_type_hints(EthGlobalTimeManagedCouplingPort.getGlobalTimeTxPeriod)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(EthGlobalTimeManagedCouplingPort.getPdelayLatencyThreshold)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(EthGlobalTimeManagedCouplingPort.getPdelayRequestPeriod)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(EthGlobalTimeManagedCouplingPort.getPdelayRespAndRespFollowUpTimeout)
        assert hints.get("return") == typing.Optional[TimeValue]
        hints = typing.get_type_hints(EthGlobalTimeManagedCouplingPort.getPdelayResponseEnabled)
        assert hints.get("return") == typing.Optional[Boolean]

    def test_get_set_coupling_port_ref(self):
        """
        Test getCouplingPortRef and setCouplingPortRef round-trip and None no-op.
        """
        obj = self._create_object()

        value = RefType()
        value.setValue("/Cluster/CouplingPort0")
        result = obj.setCouplingPortRef(value)
        assert result is obj
        assert obj.getCouplingPortRef() is value
        assert obj.getCouplingPortRef().getValue() == "/Cluster/CouplingPort0"

        result = obj.setCouplingPortRef(None)
        assert result is obj
        assert obj.getCouplingPortRef() is value

    def test_get_set_global_time_port_role(self):
        """
        Test getGlobalTimePortRole and setGlobalTimePortRole round-trip and None no-op.
        """
        obj = self._create_object()

        value = GlobalTimePortRoleEnum()
        value.setValue(GlobalTimePortRoleEnum.TIME_MASTER)
        result = obj.setGlobalTimePortRole(value)
        assert result is obj
        assert obj.getGlobalTimePortRole() is value
        assert obj.getGlobalTimePortRole().getValue() == GlobalTimePortRoleEnum.TIME_MASTER

        result = obj.setGlobalTimePortRole(None)
        assert result is obj
        assert obj.getGlobalTimePortRole() is value

    def test_get_set_time_valued_attributes(self):
        """
        Test the TimeValue getter/setter pairs round-trip and None no-op.
        """
        obj = self._create_object()

        tx_period = TimeValue().setValue("0.25")
        result = obj.setGlobalTimeTxPeriod(tx_period)
        assert result is obj
        assert obj.getGlobalTimeTxPeriod() is tx_period

        latency = TimeValue().setValue("0.001")
        result = obj.setPdelayLatencyThreshold(latency)
        assert result is obj
        assert obj.getPdelayLatencyThreshold() is latency

        request = TimeValue().setValue("1.0")
        result = obj.setPdelayRequestPeriod(request)
        assert result is obj
        assert obj.getPdelayRequestPeriod() is request

        timeout = TimeValue().setValue("0.5")
        result = obj.setPdelayRespAndRespFollowUpTimeout(timeout)
        assert result is obj
        assert obj.getPdelayRespAndRespFollowUpTimeout() is timeout

        result = obj.setGlobalTimeTxPeriod(None)
        assert result is obj
        assert obj.getGlobalTimeTxPeriod() is tx_period

    def test_get_set_pdelay_response_enabled(self):
        """
        Test getPdelayResponseEnabled and setPdelayResponseEnabled round-trip and None no-op.
        """
        obj = self._create_object()

        value = Boolean()
        value.setValue(True)
        result = obj.setPdelayResponseEnabled(value)
        assert result is obj
        assert obj.getPdelayResponseEnabled() is value

        result = obj.setPdelayResponseEnabled(None)
        assert result is obj
        assert obj.getPdelayResponseEnabled() is value

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.getCouplingPortRef.__doc__) == self.COUPLING_PORT_REF_NOTE
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.setCouplingPortRef.__doc__) == (
            self.COUPLING_PORT_REF_NOTE + "\n\nA None value is a no-op and does not overwrite an existing couplingPortRef."
        )
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.getGlobalTimePortRole.__doc__) == self.GLOBAL_TIME_PORT_ROLE_NOTE
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.setGlobalTimePortRole.__doc__) == (
            self.GLOBAL_TIME_PORT_ROLE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing globalTimePortRole."
        )
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.getGlobalTimeTxPeriod.__doc__) == self.GLOBAL_TIME_TX_PERIOD_NOTE
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.setGlobalTimeTxPeriod.__doc__) == (
            self.GLOBAL_TIME_TX_PERIOD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing globalTimeTxPeriod."
        )
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.getPdelayLatencyThreshold.__doc__) == self.PDELAY_LATENCY_THRESHOLD_NOTE
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.setPdelayLatencyThreshold.__doc__) == (
            self.PDELAY_LATENCY_THRESHOLD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing pdelayLatencyThreshold."
        )
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.getPdelayRequestPeriod.__doc__) == self.PDELAY_REQUEST_PERIOD_NOTE
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.setPdelayRequestPeriod.__doc__) == (
            self.PDELAY_REQUEST_PERIOD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing pdelayRequestPeriod."
        )
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.getPdelayRespAndRespFollowUpTimeout.__doc__) == self.PDELAY_RESP_AND_RESP_FOLLOW_UP_TIMEOUT_NOTE
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.setPdelayRespAndRespFollowUpTimeout.__doc__) == (
            self.PDELAY_RESP_AND_RESP_FOLLOW_UP_TIMEOUT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing pdelayRespAndRespFollowUpTimeout."
        )
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.getPdelayResponseEnabled.__doc__) == self.PDELAY_RESPONSE_ENABLED_NOTE
        assert inspect.cleandoc(EthGlobalTimeManagedCouplingPort.setPdelayResponseEnabled.__doc__) == (
            self.PDELAY_RESPONSE_ENABLED_NOTE + "\n\nA None value is a no-op and does not overwrite an existing pdelayResponseEnabled."
        )


class TestEthTSynSubTlvConfig:
    """
    Test class for EthTSynSubTlvConfig functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.12, p.867
    """

    CLASS_NOTE = "Defines the subTLV fields which shall be included in the time sync message."
    OFS_SUB_TLV_NOTE = "Defines whether an AUTOSAR Follow_Up TLV OFS Sub-TLV is used."
    STATUS_SUB_TLV_NOTE = "Defines whether an AUTOSAR Follow_Up TLV Status Sub-TLV is used."
    TIME_SUB_TLV_NOTE = "Defines whether an AUTOSAR Follow_Up TLV Time Sub-TLV is used."
    USER_DATA_SUB_TLV_NOTE = "Defines whether an AUTOSAR Follow_Up TLV UserData Sub-TLV is used."

    def _create_object(self) -> EthTSynSubTlvConfig:
        return EthTSynSubTlvConfig()

    def test_initialization(self):
        """
        Test that a new EthTSynSubTlvConfig initializes all attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.getOfsSubTlv() is None
        assert obj.getStatusSubTlv() is None
        assert obj.getTimeSubTlv() is None
        assert obj.getUserDataSubTlv() is None

    def test_is_ar_object_subclass(self):
        """
        Test that EthTSynSubTlvConfig derives from ARObject per the Table 9.12 Base row.
        """
        assert issubclass(EthTSynSubTlvConfig, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(EthTSynSubTlvConfig.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert EthTSynSubTlvConfig.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.12 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in EthTSynSubTlvConfig.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getOfsSubTlv",
            "setOfsSubTlv",
            "getStatusSubTlv",
            "setStatusSubTlv",
            "getTimeSubTlv",
            "setTimeSubTlv",
            "getUserDataSubTlv",
            "setUserDataSubTlv",
        ]

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec Boolean type (0..1 rows).
        """
        for getter, setter in [
            (EthTSynSubTlvConfig.getOfsSubTlv, EthTSynSubTlvConfig.setOfsSubTlv),
            (EthTSynSubTlvConfig.getStatusSubTlv, EthTSynSubTlvConfig.setStatusSubTlv),
            (EthTSynSubTlvConfig.getTimeSubTlv, EthTSynSubTlvConfig.setTimeSubTlv),
            (EthTSynSubTlvConfig.getUserDataSubTlv, EthTSynSubTlvConfig.setUserDataSubTlv),
        ]:
            hints = typing.get_type_hints(getter)
            assert hints.get("return") == typing.Optional[Boolean]
            hints = typing.get_type_hints(setter)
            assert hints.get("value") == typing.Optional[Boolean]
            assert hints.get("return") is EthTSynSubTlvConfig

    def test_get_set_sub_tlv_flags(self):
        """
        Test the four getter/setter pairs round-trip and None no-op.
        """
        obj = self._create_object()

        ofs = Boolean().setValue(True)
        result = obj.setOfsSubTlv(ofs)
        assert result is obj
        assert obj.getOfsSubTlv() is ofs

        status = Boolean().setValue(False)
        result = obj.setStatusSubTlv(status)
        assert result is obj
        assert obj.getStatusSubTlv() is status

        time = Boolean().setValue(True)
        result = obj.setTimeSubTlv(time)
        assert result is obj
        assert obj.getTimeSubTlv() is time

        user_data = Boolean().setValue(True)
        result = obj.setUserDataSubTlv(user_data)
        assert result is obj
        assert obj.getUserDataSubTlv() is user_data

        result = obj.setOfsSubTlv(None)
        assert result is obj
        assert obj.getOfsSubTlv() is ofs

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(EthTSynSubTlvConfig.getOfsSubTlv.__doc__) == self.OFS_SUB_TLV_NOTE
        assert inspect.cleandoc(EthTSynSubTlvConfig.setOfsSubTlv.__doc__) == (self.OFS_SUB_TLV_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ofsSubTlv.")
        assert inspect.cleandoc(EthTSynSubTlvConfig.getStatusSubTlv.__doc__) == self.STATUS_SUB_TLV_NOTE
        assert inspect.cleandoc(EthTSynSubTlvConfig.setStatusSubTlv.__doc__) == (self.STATUS_SUB_TLV_NOTE + "\n\nA None value is a no-op and does not overwrite an existing statusSubTlv.")
        assert inspect.cleandoc(EthTSynSubTlvConfig.getTimeSubTlv.__doc__) == self.TIME_SUB_TLV_NOTE
        assert inspect.cleandoc(EthTSynSubTlvConfig.setTimeSubTlv.__doc__) == (self.TIME_SUB_TLV_NOTE + "\n\nA None value is a no-op and does not overwrite an existing timeSubTlv.")
        assert inspect.cleandoc(EthTSynSubTlvConfig.getUserDataSubTlv.__doc__) == self.USER_DATA_SUB_TLV_NOTE
        assert inspect.cleandoc(EthTSynSubTlvConfig.setUserDataSubTlv.__doc__) == (self.USER_DATA_SUB_TLV_NOTE + "\n\nA None value is a no-op and does not overwrite an existing userDataSubTlv.")


class TestEthTSynCrcFlags:
    """
    Test class for EthTSynCrcFlags functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.15, p.868
    """

    CLASS_NOTE = "Defines the fields of the message which shall be taken into account for CRC calculation and verification."
    CRC_CORRECTION_FIELD_NOTE = "CorrectionField from the Follow_Up Message Header shall be included in CRC calculation."
    CRC_DOMAIN_NUMBER_NOTE = "DomainNumber from the Follow_Up Message Header shall be included in CRC calculation."
    CRC_MESSAGE_LENGTH_NOTE = "MessageLength from the Follow_Up Message Header shall be included in CRC calculation."
    CRC_PRECISE_ORIGIN_TIMESTAMP_NOTE = "PreciseOriginTimestamp from the Follow_Up Message Field shall be included in CRC calculation."
    CRC_SEQUENCE_ID_NOTE = "SequenceId from the Follow_Up Message Header shall be included in CRC calculation."
    CRC_SOURCE_PORT_IDENTITY_NOTE = "SourcePortIdentity from the Follow_Up Message Header shall be included in CRC calculation."

    def _create_object(self) -> EthTSynCrcFlags:
        return EthTSynCrcFlags()

    def test_initialization(self):
        """
        Test that a new EthTSynCrcFlags initializes all attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.getCrcCorrectionField() is None
        assert obj.getCrcDomainNumber() is None
        assert obj.getCrcMessageLength() is None
        assert obj.getCrcPreciseOriginTimestamp() is None
        assert obj.getCrcSequenceId() is None
        assert obj.getCrcSourcePortIdentity() is None

    def test_is_ar_object_subclass(self):
        """
        Test that EthTSynCrcFlags derives from ARObject per the Table 9.15 Base row.
        """
        assert issubclass(EthTSynCrcFlags, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(EthTSynCrcFlags.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert EthTSynCrcFlags.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.15 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in EthTSynCrcFlags.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getCrcCorrectionField",
            "setCrcCorrectionField",
            "getCrcDomainNumber",
            "setCrcDomainNumber",
            "getCrcMessageLength",
            "setCrcMessageLength",
            "getCrcPreciseOriginTimestamp",
            "setCrcPreciseOriginTimestamp",
            "getCrcSequenceId",
            "setCrcSequenceId",
            "getCrcSourcePortIdentity",
            "setCrcSourcePortIdentity",
        ]

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec Boolean type (0..1 rows).
        """
        for getter, setter in [
            (EthTSynCrcFlags.getCrcCorrectionField, EthTSynCrcFlags.setCrcCorrectionField),
            (EthTSynCrcFlags.getCrcDomainNumber, EthTSynCrcFlags.setCrcDomainNumber),
            (EthTSynCrcFlags.getCrcMessageLength, EthTSynCrcFlags.setCrcMessageLength),
            (EthTSynCrcFlags.getCrcPreciseOriginTimestamp, EthTSynCrcFlags.setCrcPreciseOriginTimestamp),
            (EthTSynCrcFlags.getCrcSequenceId, EthTSynCrcFlags.setCrcSequenceId),
            (EthTSynCrcFlags.getCrcSourcePortIdentity, EthTSynCrcFlags.setCrcSourcePortIdentity),
        ]:
            hints = typing.get_type_hints(getter)
            assert hints.get("return") == typing.Optional[Boolean]
            hints = typing.get_type_hints(setter)
            assert hints.get("value") == typing.Optional[Boolean]
            assert hints.get("return") is EthTSynCrcFlags

    def test_get_set_crc_flags(self):
        """
        Test the six getter/setter pairs round-trip and None no-op.
        """
        obj = self._create_object()

        correction = Boolean().setValue(True)
        result = obj.setCrcCorrectionField(correction)
        assert result is obj
        assert obj.getCrcCorrectionField() is correction

        domain = Boolean().setValue(True)
        result = obj.setCrcDomainNumber(domain)
        assert result is obj
        assert obj.getCrcDomainNumber() is domain

        length = Boolean().setValue(False)
        result = obj.setCrcMessageLength(length)
        assert result is obj
        assert obj.getCrcMessageLength() is length

        timestamp = Boolean().setValue(True)
        result = obj.setCrcPreciseOriginTimestamp(timestamp)
        assert result is obj
        assert obj.getCrcPreciseOriginTimestamp() is timestamp

        sequence = Boolean().setValue(True)
        result = obj.setCrcSequenceId(sequence)
        assert result is obj
        assert obj.getCrcSequenceId() is sequence

        port = Boolean().setValue(True)
        result = obj.setCrcSourcePortIdentity(port)
        assert result is obj
        assert obj.getCrcSourcePortIdentity() is port

        result = obj.setCrcCorrectionField(None)
        assert result is obj
        assert obj.getCrcCorrectionField() is correction

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(EthTSynCrcFlags.getCrcCorrectionField.__doc__) == self.CRC_CORRECTION_FIELD_NOTE
        assert inspect.cleandoc(EthTSynCrcFlags.setCrcCorrectionField.__doc__) == (
            self.CRC_CORRECTION_FIELD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing crcCorrectionField."
        )
        assert inspect.cleandoc(EthTSynCrcFlags.getCrcDomainNumber.__doc__) == self.CRC_DOMAIN_NUMBER_NOTE
        assert inspect.cleandoc(EthTSynCrcFlags.setCrcDomainNumber.__doc__) == (self.CRC_DOMAIN_NUMBER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing crcDomainNumber.")
        assert inspect.cleandoc(EthTSynCrcFlags.getCrcMessageLength.__doc__) == self.CRC_MESSAGE_LENGTH_NOTE
        assert inspect.cleandoc(EthTSynCrcFlags.setCrcMessageLength.__doc__) == (self.CRC_MESSAGE_LENGTH_NOTE + "\n\nA None value is a no-op and does not overwrite an existing crcMessageLength.")
        assert inspect.cleandoc(EthTSynCrcFlags.getCrcPreciseOriginTimestamp.__doc__) == self.CRC_PRECISE_ORIGIN_TIMESTAMP_NOTE
        assert inspect.cleandoc(EthTSynCrcFlags.setCrcPreciseOriginTimestamp.__doc__) == (
            self.CRC_PRECISE_ORIGIN_TIMESTAMP_NOTE + "\n\nA None value is a no-op and does not overwrite an existing crcPreciseOriginTimestamp."
        )
        assert inspect.cleandoc(EthTSynCrcFlags.getCrcSequenceId.__doc__) == self.CRC_SEQUENCE_ID_NOTE
        assert inspect.cleandoc(EthTSynCrcFlags.setCrcSequenceId.__doc__) == (self.CRC_SEQUENCE_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing crcSequenceId.")
        assert inspect.cleandoc(EthTSynCrcFlags.getCrcSourcePortIdentity.__doc__) == self.CRC_SOURCE_PORT_IDENTITY_NOTE
        assert inspect.cleandoc(EthTSynCrcFlags.setCrcSourcePortIdentity.__doc__) == (
            self.CRC_SOURCE_PORT_IDENTITY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing crcSourcePortIdentity."
        )


class TestCanGlobalTimeDomainProps:
    """
    Test class for CanGlobalTimeDomainProps functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.10, p.864
    """

    CLASS_NOTE = "Enables the definition of Can Global Time specific properties."
    FUP_DATA_ID_LIST_NOTE = "The DataIDList for FUP messages to calculate CRC."
    OFNS_DATA_ID_LIST_NOTE = "The DataIDList for OFNS messages to calculate CRC."
    OFS_DATA_ID_LIST_NOTE = "The DataIDList for OFS messages to calculate CRC."
    SYNC_DATA_ID_LIST_NOTE = "The DataIDList for SYNC messages to calculate CRC."

    def _create_object(self) -> CanGlobalTimeDomainProps:
        return CanGlobalTimeDomainProps()

    def test_initialization(self):
        """
        Test that a new CanGlobalTimeDomainProps initializes all attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.getVariationPoint() is None
        assert obj.getFupDataIDLists() == []
        assert obj.getOfnsDataIDLists() == []
        assert obj.getOfsDataIDLists() == []
        assert obj.getSyncDataIDLists() == []

    def test_is_abstract_global_time_domain_props_subclass(self):
        """
        Test that CanGlobalTimeDomainProps derives from AbstractGlobalTimeDomainProps per the
        Table 9.10 Base row (ARObject, AbstractGlobalTimeDomainProps — most-derived
        AbstractGlobalTimeDomainProps).
        """
        assert issubclass(CanGlobalTimeDomainProps, AbstractGlobalTimeDomainProps)
        assert issubclass(CanGlobalTimeDomainProps, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(CanGlobalTimeDomainProps.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CanGlobalTimeDomainProps.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.10 displayed row order (mutator first per attribute).
        """
        methods = [name for name, value in CanGlobalTimeDomainProps.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "addFupDataIDList",
            "getFupDataIDLists",
            "addOfnsDataIDList",
            "getOfnsDataIDLists",
            "addOfsDataIDList",
            "getOfsDataIDLists",
            "addSyncDataIDList",
            "getSyncDataIDLists",
        ]

    def test_annotations_are_list_typed(self):
        """
        Test that the accessors carry the spec PositiveInteger list type (0..16 rows).
        """
        hints = typing.get_type_hints(CanGlobalTimeDomainProps.addFupDataIDList)
        assert hints.get("value") == typing.Optional[PositiveInteger]
        assert hints.get("return") is CanGlobalTimeDomainProps
        for getter in [
            CanGlobalTimeDomainProps.getFupDataIDLists,
            CanGlobalTimeDomainProps.getOfnsDataIDLists,
            CanGlobalTimeDomainProps.getOfsDataIDLists,
            CanGlobalTimeDomainProps.getSyncDataIDLists,
        ]:
            hints = typing.get_type_hints(getter)
            assert hints.get("return") == typing.List[PositiveInteger]

    def test_add_get_fup_data_id_lists(self):
        """
        Test addFupDataIDList and getFupDataIDLists append, round-trip and None no-op.
        """
        obj = self._create_object()

        first = PositiveInteger().setValue("1")
        second = PositiveInteger().setValue("2")

        result = obj.addFupDataIDList(None)
        assert result is obj
        assert obj.getFupDataIDLists() == []

        result = obj.addFupDataIDList(first)
        assert result is obj
        result = obj.addFupDataIDList(second)
        assert result is obj

        data_id_lists = obj.getFupDataIDLists()
        assert len(data_id_lists) == 2
        assert data_id_lists[0] is first
        assert data_id_lists[1] is second
        assert data_id_lists[0].getValue() == 1
        assert data_id_lists[1].getValue() == 2

    def test_add_get_ofns_ofs_sync_data_id_lists(self):
        """
        Test the remaining DataIDList accessor pairs append, round-trip and None no-op.
        """
        obj = self._create_object()

        ofns = PositiveInteger().setValue("3")
        result = obj.addOfnsDataIDList(ofns)
        assert result is obj
        assert obj.getOfnsDataIDLists() == [ofns]
        assert obj.getOfnsDataIDLists()[0].getValue() == 3

        ofs = PositiveInteger().setValue("4")
        result = obj.addOfsDataIDList(ofs)
        assert result is obj
        assert obj.getOfsDataIDLists() == [ofs]
        assert obj.getOfsDataIDLists()[0].getValue() == 4

        sync = PositiveInteger().setValue("5")
        result = obj.addSyncDataIDList(sync)
        assert result is obj
        assert obj.getSyncDataIDLists() == [sync]
        assert obj.getSyncDataIDLists()[0].getValue() == 5

        result = obj.addOfnsDataIDList(None)
        assert result is obj
        assert len(obj.getOfnsDataIDLists()) == 1

    def test_variation_point_base_accessors(self):
        """
        Exercise the inherited VariationPointCapable accessors: chaining, round-trip, None no-op.
        """
        obj = self._create_object()

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        variation_point = VariationPoint()
        assert obj.setVariationPoint(variation_point) is obj
        assert obj.getVariationPoint() is variation_point

        obj.setVariationPoint(None)
        assert obj.getVariationPoint() is variation_point

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and adder docstrings carry the spec Note verbatim (adder + None-no-op sentence).
        """
        assert inspect.cleandoc(CanGlobalTimeDomainProps.addFupDataIDList.__doc__) == (self.FUP_DATA_ID_LIST_NOTE + "\n\nA None value is a no-op and does not append to fupDataIDLists.")
        assert inspect.cleandoc(CanGlobalTimeDomainProps.getFupDataIDLists.__doc__) == self.FUP_DATA_ID_LIST_NOTE
        assert inspect.cleandoc(CanGlobalTimeDomainProps.addOfnsDataIDList.__doc__) == (self.OFNS_DATA_ID_LIST_NOTE + "\n\nA None value is a no-op and does not append to ofnsDataIDLists.")
        assert inspect.cleandoc(CanGlobalTimeDomainProps.getOfnsDataIDLists.__doc__) == self.OFNS_DATA_ID_LIST_NOTE
        assert inspect.cleandoc(CanGlobalTimeDomainProps.addOfsDataIDList.__doc__) == (self.OFS_DATA_ID_LIST_NOTE + "\n\nA None value is a no-op and does not append to ofsDataIDLists.")
        assert inspect.cleandoc(CanGlobalTimeDomainProps.getOfsDataIDLists.__doc__) == self.OFS_DATA_ID_LIST_NOTE
        assert inspect.cleandoc(CanGlobalTimeDomainProps.addSyncDataIDList.__doc__) == (self.SYNC_DATA_ID_LIST_NOTE + "\n\nA None value is a no-op and does not append to syncDataIDLists.")
        assert inspect.cleandoc(CanGlobalTimeDomainProps.getSyncDataIDLists.__doc__) == self.SYNC_DATA_ID_LIST_NOTE


class TestEthGlobalTimeDomainProps:
    """
    Test class for EthGlobalTimeDomainProps functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.14, p.867
    """

    CLASS_NOTE = "Enables the definition of Ethernet Global Time specific properties."
    CLASS_CONSTRAINT = "[constr_9311] Existence of EthGlobalTimeDomainProps.messageCompliance: For each EthGlobalTimeDomainProps, the attribute messageCompliance shall exist at the time when the System Description is complete."
    CRC_FLAGS_NOTE = "Defines the fields of the message which shall be taken into account for CRC calculation and verification."
    DESTINATION_PHYSICAL_ADDRESS_NOTE = "Defines the MAC multicast address the Ethernet time sync messages are communicated on."
    FUP_DATA_ID_LIST_NOTE = "The DataIDList for FUP messages to calculate CRC."
    MANAGED_COUPLING_PORT_NOTE = "Collection of CouplingPorts which are managed in the scope of this Ethernet GlobalTimeDomain."
    MESSAGE_COMPLIANCE_NOTE = "Defines the compliance of the Ethernet time sync messages to specific standards."
    VLAN_PRIORITY_NOTE = "Defines which VLAN priority shall be assigned to a time sync message in case the message is sent using a VLAN tag."

    def _create_object(self) -> EthGlobalTimeDomainProps:
        return EthGlobalTimeDomainProps()

    def test_initialization(self):
        """
        Test that a new EthGlobalTimeDomainProps initializes all attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.getVariationPoint() is None
        assert obj.getCrcFlags() is None
        assert obj.getDestinationPhysicalAddress() is None
        assert obj.getFupDataIDLists() == []
        assert obj.getManagedCouplingPorts() == []
        assert obj.getMessageCompliance() is None
        assert obj.getVlanPriority() is None

    def test_is_abstract_global_time_domain_props_subclass(self):
        """
        Test that EthGlobalTimeDomainProps derives from AbstractGlobalTimeDomainProps per the
        Table 9.14 Base row (ARObject, AbstractGlobalTimeDomainProps — most-derived
        AbstractGlobalTimeDomainProps).
        """
        assert issubclass(EthGlobalTimeDomainProps, AbstractGlobalTimeDomainProps)
        assert issubclass(EthGlobalTimeDomainProps, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim plus the class-level constr_9311 row.
        """
        assert inspect.cleandoc(EthGlobalTimeDomainProps.__doc__) == (self.CLASS_NOTE + "\n\n" + self.CLASS_CONSTRAINT)

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert EthGlobalTimeDomainProps.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.14 displayed row order (getter first for scalars,
        mutator first for lists).
        """
        methods = [name for name, value in EthGlobalTimeDomainProps.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getCrcFlags",
            "setCrcFlags",
            "getDestinationPhysicalAddress",
            "setDestinationPhysicalAddress",
            "addFupDataIDList",
            "getFupDataIDLists",
            "addManagedCouplingPort",
            "getManagedCouplingPorts",
            "getMessageCompliance",
            "setMessageCompliance",
            "getVlanPriority",
            "setVlanPriority",
        ]

    def test_annotations_are_spec_typed(self):
        """
        Test that the accessors carry the spec types (Table 9.14 Type column).
        """
        hints = typing.get_type_hints(EthGlobalTimeDomainProps.getCrcFlags)
        assert hints.get("return") == typing.Optional[EthTSynCrcFlags]
        hints = typing.get_type_hints(EthGlobalTimeDomainProps.setCrcFlags)
        assert hints.get("value") == typing.Optional[EthTSynCrcFlags]
        assert hints.get("return") is EthGlobalTimeDomainProps

        hints = typing.get_type_hints(EthGlobalTimeDomainProps.getDestinationPhysicalAddress)
        assert hints.get("return") == typing.Optional[MacAddressString]
        hints = typing.get_type_hints(EthGlobalTimeDomainProps.setDestinationPhysicalAddress)
        assert hints.get("value") == typing.Optional[MacAddressString]
        assert hints.get("return") is EthGlobalTimeDomainProps

        hints = typing.get_type_hints(EthGlobalTimeDomainProps.addFupDataIDList)
        assert hints.get("value") == typing.Optional[PositiveInteger]
        assert hints.get("return") is EthGlobalTimeDomainProps
        hints = typing.get_type_hints(EthGlobalTimeDomainProps.getFupDataIDLists)
        assert hints.get("return") == typing.List[PositiveInteger]

        hints = typing.get_type_hints(EthGlobalTimeDomainProps.addManagedCouplingPort)
        assert hints.get("value") == typing.Optional[EthGlobalTimeManagedCouplingPort]
        assert hints.get("return") is EthGlobalTimeDomainProps
        hints = typing.get_type_hints(EthGlobalTimeDomainProps.getManagedCouplingPorts)
        assert hints.get("return") == typing.List[EthGlobalTimeManagedCouplingPort]

        hints = typing.get_type_hints(EthGlobalTimeDomainProps.getMessageCompliance)
        assert hints.get("return") == typing.Optional[EthGlobalTimeMessageFormatEnum]
        hints = typing.get_type_hints(EthGlobalTimeDomainProps.setMessageCompliance)
        assert hints.get("value") == typing.Optional[EthGlobalTimeMessageFormatEnum]
        assert hints.get("return") is EthGlobalTimeDomainProps

        hints = typing.get_type_hints(EthGlobalTimeDomainProps.getVlanPriority)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(EthGlobalTimeDomainProps.setVlanPriority)
        assert hints.get("value") == typing.Optional[PositiveInteger]
        assert hints.get("return") is EthGlobalTimeDomainProps

    def test_get_set_crc_flags(self):
        """
        Test setCrcFlags and getCrcFlags round-trip and None no-op.
        """
        obj = self._create_object()

        flags = EthTSynCrcFlags()
        flags.setCrcSequenceId(Boolean().setValue("true"))

        result = obj.setCrcFlags(None)
        assert result is obj
        assert obj.getCrcFlags() is None

        result = obj.setCrcFlags(flags)
        assert result is obj
        assert obj.getCrcFlags() is flags

        obj.setCrcFlags(None)
        assert obj.getCrcFlags() is flags

    def test_get_set_destination_physical_address(self):
        """
        Test setDestinationPhysicalAddress and getDestinationPhysicalAddress round-trip and None no-op.
        """
        obj = self._create_object()

        address = MacAddressString().setValue("01:80:C2:00:00:0E")

        result = obj.setDestinationPhysicalAddress(None)
        assert result is obj
        assert obj.getDestinationPhysicalAddress() is None

        result = obj.setDestinationPhysicalAddress(address)
        assert result is obj
        assert obj.getDestinationPhysicalAddress() is address
        assert obj.getDestinationPhysicalAddress().getValue() == "01:80:C2:00:00:0E"

        obj.setDestinationPhysicalAddress(None)
        assert obj.getDestinationPhysicalAddress() is address

    def test_add_get_fup_data_id_lists(self):
        """
        Test addFupDataIDList and getFupDataIDLists append, round-trip and None no-op.
        """
        obj = self._create_object()

        first = PositiveInteger().setValue("1")
        second = PositiveInteger().setValue("2")

        result = obj.addFupDataIDList(None)
        assert result is obj
        assert obj.getFupDataIDLists() == []

        result = obj.addFupDataIDList(first)
        assert result is obj
        result = obj.addFupDataIDList(second)
        assert result is obj

        data_id_lists = obj.getFupDataIDLists()
        assert len(data_id_lists) == 2
        assert data_id_lists[0] is first
        assert data_id_lists[1] is second
        assert data_id_lists[0].getValue() == 1
        assert data_id_lists[1].getValue() == 2

    def test_add_get_managed_coupling_ports(self):
        """
        Test addManagedCouplingPort and getManagedCouplingPorts append, round-trip and None no-op.
        """
        obj = self._create_object()

        first = EthGlobalTimeManagedCouplingPort()
        first.setCouplingPortRef(RefType().setValue("/CouplingPort/First"))
        second = EthGlobalTimeManagedCouplingPort()
        second.setCouplingPortRef(RefType().setValue("/CouplingPort/Second"))

        result = obj.addManagedCouplingPort(None)
        assert result is obj
        assert obj.getManagedCouplingPorts() == []

        result = obj.addManagedCouplingPort(first)
        assert result is obj
        result = obj.addManagedCouplingPort(second)
        assert result is obj

        ports = obj.getManagedCouplingPorts()
        assert len(ports) == 2
        assert ports[0] is first
        assert ports[1] is second
        assert ports[0].getCouplingPortRef().getValue() == "/CouplingPort/First"
        assert ports[1].getCouplingPortRef().getValue() == "/CouplingPort/Second"

    def test_get_set_message_compliance(self):
        """
        Test setMessageCompliance and getMessageCompliance round-trip and None no-op.
        """
        obj = self._create_object()

        compliance = EthGlobalTimeMessageFormatEnum().setValue(EthGlobalTimeMessageFormatEnum.IEEE802_1AS)

        result = obj.setMessageCompliance(None)
        assert result is obj
        assert obj.getMessageCompliance() is None

        result = obj.setMessageCompliance(compliance)
        assert result is obj
        assert obj.getMessageCompliance() is compliance
        assert obj.getMessageCompliance().getValue() == EthGlobalTimeMessageFormatEnum.IEEE802_1AS

        obj.setMessageCompliance(None)
        assert obj.getMessageCompliance() is compliance

    def test_get_set_vlan_priority(self):
        """
        Test setVlanPriority and getVlanPriority round-trip and None no-op.
        """
        obj = self._create_object()

        priority = PositiveInteger().setValue("5")

        result = obj.setVlanPriority(None)
        assert result is obj
        assert obj.getVlanPriority() is None

        result = obj.setVlanPriority(priority)
        assert result is obj
        assert obj.getVlanPriority() is priority
        assert obj.getVlanPriority().getValue() == 5

        obj.setVlanPriority(None)
        assert obj.getVlanPriority() is priority

    def test_variation_point_base_accessors(self):
        """
        Exercise the inherited VariationPointCapable accessors: chaining, round-trip, None no-op.
        """
        obj = self._create_object()

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        variation_point = VariationPoint()
        assert obj.setVariationPoint(variation_point) is obj
        assert obj.getVariationPoint() is variation_point

        obj.setVariationPoint(None)
        assert obj.getVariationPoint() is variation_point

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter/setter/adder docstrings carry the spec Note verbatim (setter/adder + None-no-op sentence).
        """
        assert inspect.cleandoc(EthGlobalTimeDomainProps.getCrcFlags.__doc__) == self.CRC_FLAGS_NOTE
        assert inspect.cleandoc(EthGlobalTimeDomainProps.setCrcFlags.__doc__) == (self.CRC_FLAGS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing crcFlags.")
        assert inspect.cleandoc(EthGlobalTimeDomainProps.getDestinationPhysicalAddress.__doc__) == self.DESTINATION_PHYSICAL_ADDRESS_NOTE
        assert inspect.cleandoc(EthGlobalTimeDomainProps.setDestinationPhysicalAddress.__doc__) == (
            self.DESTINATION_PHYSICAL_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing destinationPhysicalAddress."
        )
        assert inspect.cleandoc(EthGlobalTimeDomainProps.addFupDataIDList.__doc__) == (self.FUP_DATA_ID_LIST_NOTE + "\n\nA None value is a no-op and does not append to fupDataIDLists.")
        assert inspect.cleandoc(EthGlobalTimeDomainProps.getFupDataIDLists.__doc__) == self.FUP_DATA_ID_LIST_NOTE
        assert inspect.cleandoc(EthGlobalTimeDomainProps.addManagedCouplingPort.__doc__) == (
            self.MANAGED_COUPLING_PORT_NOTE + "\n\nA None value is a no-op and does not append to managedCouplingPorts."
        )
        assert inspect.cleandoc(EthGlobalTimeDomainProps.getManagedCouplingPorts.__doc__) == self.MANAGED_COUPLING_PORT_NOTE
        assert inspect.cleandoc(EthGlobalTimeDomainProps.getMessageCompliance.__doc__) == self.MESSAGE_COMPLIANCE_NOTE
        assert inspect.cleandoc(EthGlobalTimeDomainProps.setMessageCompliance.__doc__) == (
            self.MESSAGE_COMPLIANCE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing messageCompliance."
        )
        assert inspect.cleandoc(EthGlobalTimeDomainProps.getVlanPriority.__doc__) == self.VLAN_PRIORITY_NOTE
        assert inspect.cleandoc(EthGlobalTimeDomainProps.setVlanPriority.__doc__) == (self.VLAN_PRIORITY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing vlanPriority.")


class TestFrGlobalTimeDomainProps:
    """
    Test class for FrGlobalTimeDomainProps functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.22, p.878
    """

    CLASS_NOTE = "Enables the definition of Flexray GlobalTime specific properties."
    OFS_DATA_ID_LIST_NOTE = "The DataIDList for OFS messages to calculate CRC."
    SYNC_DATA_ID_LIST_NOTE = "The DataIDList for SYNC messages to calculate CRC."

    def _create_object(self) -> FrGlobalTimeDomainProps:
        return FrGlobalTimeDomainProps()

    def test_initialization(self):
        """
        Test that a new FrGlobalTimeDomainProps initializes all attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.getVariationPoint() is None
        assert obj.getOfsDataIDLists() == []
        assert obj.getSyncDataIDLists() == []

    def test_is_abstract_global_time_domain_props_subclass(self):
        """
        Test that FrGlobalTimeDomainProps derives from AbstractGlobalTimeDomainProps per the
        Table 9.22 Base row (ARObject, AbstractGlobalTimeDomainProps — most-derived
        AbstractGlobalTimeDomainProps).
        """
        assert issubclass(FrGlobalTimeDomainProps, AbstractGlobalTimeDomainProps)
        assert issubclass(FrGlobalTimeDomainProps, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(FrGlobalTimeDomainProps.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert FrGlobalTimeDomainProps.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 9.22 displayed row order (mutator first per attribute).
        """
        methods = [name for name, value in FrGlobalTimeDomainProps.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "addOfsDataIDList",
            "getOfsDataIDLists",
            "addSyncDataIDList",
            "getSyncDataIDLists",
        ]

    def test_annotations_are_list_typed(self):
        """
        Test that the accessors carry the spec PositiveInteger list type (0..16 rows).
        """
        hints = typing.get_type_hints(FrGlobalTimeDomainProps.addOfsDataIDList)
        assert hints.get("value") == typing.Optional[PositiveInteger]
        assert hints.get("return") is FrGlobalTimeDomainProps
        for getter in [FrGlobalTimeDomainProps.getOfsDataIDLists, FrGlobalTimeDomainProps.getSyncDataIDLists]:
            hints = typing.get_type_hints(getter)
            assert hints.get("return") == typing.List[PositiveInteger]

    def test_add_get_ofs_sync_data_id_lists(self):
        """
        Test addOfsDataIDList and addSyncDataIDList append, round-trip and None no-op.
        """
        obj = self._create_object()

        ofs = PositiveInteger().setValue("3")
        result = obj.addOfsDataIDList(ofs)
        assert result is obj
        assert obj.getOfsDataIDLists() == [ofs]
        assert obj.getOfsDataIDLists()[0].getValue() == 3

        sync = PositiveInteger().setValue("5")
        result = obj.addSyncDataIDList(sync)
        assert result is obj
        assert obj.getSyncDataIDLists() == [sync]
        assert obj.getSyncDataIDLists()[0].getValue() == 5

        result = obj.addOfsDataIDList(None)
        assert result is obj
        assert len(obj.getOfsDataIDLists()) == 1

        result = obj.addSyncDataIDList(None)
        assert result is obj
        assert len(obj.getSyncDataIDLists()) == 1

    def test_variation_point_base_accessors(self):
        """
        Exercise the inherited VariationPointCapable accessors: chaining, round-trip, None no-op.
        """
        obj = self._create_object()

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        variation_point = VariationPoint()
        assert obj.setVariationPoint(variation_point) is obj
        assert obj.getVariationPoint() is variation_point

        obj.setVariationPoint(None)
        assert obj.getVariationPoint() is variation_point

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter and adder docstrings carry the spec Note verbatim (adder + None-no-op sentence).
        """
        assert inspect.cleandoc(FrGlobalTimeDomainProps.addOfsDataIDList.__doc__) == (self.OFS_DATA_ID_LIST_NOTE + "\n\nA None value is a no-op and does not append to ofsDataIDLists.")
        assert inspect.cleandoc(FrGlobalTimeDomainProps.getOfsDataIDLists.__doc__) == self.OFS_DATA_ID_LIST_NOTE
        assert inspect.cleandoc(FrGlobalTimeDomainProps.addSyncDataIDList.__doc__) == (self.SYNC_DATA_ID_LIST_NOTE + "\n\nA None value is a no-op and does not append to syncDataIDLists.")
        assert inspect.cleandoc(FrGlobalTimeDomainProps.getSyncDataIDLists.__doc__) == self.SYNC_DATA_ID_LIST_NOTE


class TestCpSoftwareClusterCommunicationResourceProps:
    """
    Test class for CpSoftwareClusterCommunicationResourceProps functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.9, p.902
    """

    CLASS_NOTE = "Communication properties for cross cluster communication."

    def _create_object(self) -> CpSoftwareClusterCommunicationResourceProps:
        class ConcreteComProps(CpSoftwareClusterCommunicationResourceProps):
            pass

        return ConcreteComProps()

    def test_cannot_instantiate_abstract(self):
        """
        Test that the abstract Table 11.9 class cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            CpSoftwareClusterCommunicationResourceProps()

    def test_concrete_subclass_initialization(self):
        """
        Test that a concrete subclass initializes the inherited ARObject state to its defaults
        (Table 11.9 declares no Attribute rows of its own).
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None

    def test_is_ar_object_subclass(self):
        """
        Test that CpSoftwareClusterCommunicationResourceProps derives from ARObject per the
        Table 11.9 Base row (ARObject — most-derived, the class is abstract).
        """
        import abc

        assert issubclass(CpSoftwareClusterCommunicationResourceProps, ARObject)
        assert issubclass(CpSoftwareClusterCommunicationResourceProps, abc.ABC)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(CpSoftwareClusterCommunicationResourceProps.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CpSoftwareClusterCommunicationResourceProps.__init__.__doc__ is None


class TestDataComProps:
    """
    Test class for DataComProps functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.10, p.903
    """

    CLASS_NOTE = "Represents a single resource required or provided by a CP Software Cluster which relates to the port based communication on VFB level."
    DATA_CONSISTENCY_POLICY_NOTE = (
        "This attribute defines requirements on the data consistency mechanism in the cross cluster communication. If the attribute is not set, the default value consistencyMechanismRequired applies."
    )
    SEND_INDICATION_NOTE = "Send indication behavior for last-is-the best data communication."

    def _create_object(self) -> DataComProps:
        return DataComProps()

    def test_initialization(self):
        """
        Test that a new DataComProps initializes all attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.getDataConsistencyPolicy() is None
        assert obj.getSendIndication() is None

    def test_is_cp_software_cluster_communication_resource_props_subclass(self):
        """
        Test that DataComProps derives from CpSoftwareClusterCommunicationResourceProps per the
        Table 11.10 Base row (ARObject, CpSoftwareClusterCommunicationResourceProps — most-derived
        CpSoftwareClusterCommunicationResourceProps).
        """
        assert issubclass(DataComProps, CpSoftwareClusterCommunicationResourceProps)
        assert issubclass(DataComProps, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DataComProps.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DataComProps.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 11.10 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in DataComProps.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getDataConsistencyPolicy",
            "setDataConsistencyPolicy",
            "getSendIndication",
            "setSendIndication",
        ]

    def test_annotations_are_spec_typed(self):
        """
        Test that the accessors carry the spec enum types (Table 11.10 Type column).
        """
        hints = typing.get_type_hints(DataComProps.getDataConsistencyPolicy)
        assert hints.get("return") == typing.Optional[DataConsistencyPolicyEnum]
        hints = typing.get_type_hints(DataComProps.setDataConsistencyPolicy)
        assert hints.get("value") == typing.Optional[DataConsistencyPolicyEnum]
        assert hints.get("return") is DataComProps

        hints = typing.get_type_hints(DataComProps.getSendIndication)
        assert hints.get("return") == typing.Optional[SendIndicationEnum]
        hints = typing.get_type_hints(DataComProps.setSendIndication)
        assert hints.get("value") == typing.Optional[SendIndicationEnum]
        assert hints.get("return") is DataComProps

    def test_get_set_data_consistency_policy(self):
        """
        Test setDataConsistencyPolicy and getDataConsistencyPolicy round-trip and None no-op.
        """
        obj = self._create_object()

        policy = DataConsistencyPolicyEnum().setValue(DataConsistencyPolicyEnum.CONSISTENCY_MECHANISM_REQUIRED)

        result = obj.setDataConsistencyPolicy(None)
        assert result is obj
        assert obj.getDataConsistencyPolicy() is None

        result = obj.setDataConsistencyPolicy(policy)
        assert result is obj
        assert obj.getDataConsistencyPolicy() is policy
        assert obj.getDataConsistencyPolicy().getValue() == DataConsistencyPolicyEnum.CONSISTENCY_MECHANISM_REQUIRED

        obj.setDataConsistencyPolicy(None)
        assert obj.getDataConsistencyPolicy() is policy

    def test_get_set_send_indication(self):
        """
        Test setSendIndication and getSendIndication round-trip and None no-op.
        """
        obj = self._create_object()

        indication = SendIndicationEnum().setValue(SendIndicationEnum.ANY_SEND_OPERATION)

        result = obj.setSendIndication(None)
        assert result is obj
        assert obj.getSendIndication() is None

        result = obj.setSendIndication(indication)
        assert result is obj
        assert obj.getSendIndication() is indication
        assert obj.getSendIndication().getValue() == SendIndicationEnum.ANY_SEND_OPERATION

        obj.setSendIndication(None)
        assert obj.getSendIndication() is indication

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter/setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(DataComProps.getDataConsistencyPolicy.__doc__) == self.DATA_CONSISTENCY_POLICY_NOTE
        assert inspect.cleandoc(DataComProps.setDataConsistencyPolicy.__doc__) == (
            self.DATA_CONSISTENCY_POLICY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dataConsistencyPolicy."
        )
        assert inspect.cleandoc(DataComProps.getSendIndication.__doc__) == self.SEND_INDICATION_NOTE
        assert inspect.cleandoc(DataComProps.setSendIndication.__doc__) == (self.SEND_INDICATION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing sendIndication.")


class TestClientServerOperationComProps:
    """
    Test class for ClientServerOperationComProps functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.12, p.903
    """

    CLASS_NOTE = "Defines additional attributes for the implementation of Client Server communication between software clusters"
    QUEUE_LENGTH_NOTE = "Length of call request queue on the server side. The queue is implemented by the SwCluC. The value shall be greater or equal to 1. Setting the value of queueLength to 1 implies that incoming requests are rejected while another request that arrived earlier is being processed."

    def _create_object(self) -> ClientServerOperationComProps:
        return ClientServerOperationComProps()

    def test_initialization(self):
        """
        Test that a new ClientServerOperationComProps initializes all attributes to their defaults.
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.getQueueLength() is None

    def test_is_cp_software_cluster_communication_resource_props_subclass(self):
        """
        Test that ClientServerOperationComProps derives from CpSoftwareClusterCommunicationResourceProps
        per the Table 11.12 Base row (ARObject, CpSoftwareClusterCommunicationResourceProps —
        most-derived CpSoftwareClusterCommunicationResourceProps).
        """
        assert issubclass(ClientServerOperationComProps, CpSoftwareClusterCommunicationResourceProps)
        assert issubclass(ClientServerOperationComProps, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim (the Table 11.12 Note carries no
        trailing period).
        """
        assert inspect.cleandoc(ClientServerOperationComProps.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert ClientServerOperationComProps.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 11.12 displayed row order (getter first per attribute).
        """
        methods = [name for name, value in ClientServerOperationComProps.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getQueueLength",
            "setQueueLength",
        ]

    def test_annotations_are_spec_typed(self):
        """
        Test that the accessors carry the spec PositiveInteger type (Table 11.12 Type column).
        """
        hints = typing.get_type_hints(ClientServerOperationComProps.getQueueLength)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(ClientServerOperationComProps.setQueueLength)
        assert hints.get("value") == typing.Optional[PositiveInteger]
        assert hints.get("return") is ClientServerOperationComProps

    def test_get_set_queue_length(self):
        """
        Test setQueueLength and getQueueLength round-trip and None no-op.
        """
        obj = self._create_object()

        queue_length = PositiveInteger().setValue("3")

        result = obj.setQueueLength(None)
        assert result is obj
        assert obj.getQueueLength() is None

        result = obj.setQueueLength(queue_length)
        assert result is obj
        assert obj.getQueueLength() is queue_length
        assert obj.getQueueLength().getValue() == 3

        obj.setQueueLength(None)
        assert obj.getQueueLength() is queue_length

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Getter/setter docstrings carry the spec Note verbatim (setter + None-no-op sentence).
        """
        assert inspect.cleandoc(ClientServerOperationComProps.getQueueLength.__doc__) == self.QUEUE_LENGTH_NOTE
        assert inspect.cleandoc(ClientServerOperationComProps.setQueueLength.__doc__) == (self.QUEUE_LENGTH_NOTE + "\n\nA None value is a no-op and does not overwrite an existing queueLength.")


class TestBinaryManifestItemValue:
    """
    Test class for BinaryManifestItemValue functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.25, p.922
    (abstract; Table 11.25 declares no Attribute rows — the concrete subclasses
    BinaryManifestItemNumericalValue and BinaryManifestItemPointerValue carry the XML content,
    exercised in their own test classes.)
    """

    CLASS_NOTE = "This meta-class has the ability to act as an abstract base class for values of binary manifest item."

    def _create_object(self) -> BinaryManifestItemValue:
        class ConcreteItemValue(BinaryManifestItemValue):
            pass

        return ConcreteItemValue()

    def test_cannot_instantiate_abstract(self):
        """
        BinaryManifestItemValue is abstract per Table 11.25 and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            BinaryManifestItemValue()

    def test_is_ar_object_subclass(self):
        """
        Test that BinaryManifestItemValue derives from ARObject per the Table 11.25 Base row
        (ARObject — most-derived, the class is abstract).
        """
        import abc

        assert issubclass(BinaryManifestItemValue, ARObject)
        assert issubclass(BinaryManifestItemValue, abc.ABC)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(BinaryManifestItemValue.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert BinaryManifestItemValue.__init__.__doc__ is None

    def test_table_declares_no_attribute_rows(self):
        """
        Test that the class declares no own accessors (Table 11.25 Attribute row is '-').
        """
        methods = [name for name, value in BinaryManifestItemValue.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == []

    def test_concrete_subclass_initialization(self):
        """
        Test that a concrete subclass initializes the inherited ARObject state to its defaults.
        """
        obj = self._create_object()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
