"""
Tests for the ARObject class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 6.1).
"""

import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    DiagnosticAbstractParameter,
    DiagnosticComControlSpecificChannel,
    DiagnosticCommonProps,
    DiagnosticParameter,
    DiagnosticParameterSupportInfo,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDebounceAlgorithmProps, DiagnosticParameterElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    ByteOrderEnum,
    DateTime,
    DiagnosticEventCombinationBehaviorEnum,
    DiagnosticEventCombinationReportingBehaviorEnum,
    DiagnosticOccurrenceCounterProcessingEnum,
    PositiveInteger,
    RefType,
    String,
    TimeValue,
)


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
        assert obj.getDefaultEndianness().getValue() == "opaque"

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
        assert obj.getOccurrenceCounterProcessing().getValue() == "confirmedDtcBit"

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
        assert obj.getEventCombinationReportingBehavior().getValue() == "reportingInChronlogicalOrderOldestFirst"

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
        assert obj.getTypeOfEventCombinationSupported().getValue() == "eventCombinationOnStorage"

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
