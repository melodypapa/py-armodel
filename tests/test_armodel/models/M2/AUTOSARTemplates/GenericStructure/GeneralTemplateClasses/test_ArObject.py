"""
Tests for the ARObject class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 6.1).
"""

import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    DiagnosticAbstractParameter,
    DiagnosticComControlSpecificChannel,
    DiagnosticComControlSubNodeChannel,
    DiagnosticCommonProps,
    DiagnosticConnectedIndicator,
    DiagnosticControlEnableMaskBit,
    DiagnosticEventWindow,
    DiagnosticFunctionIdentifierInhibit,
    DiagnosticIumprGroupIdentifier,
    DiagnosticParameter,
    DiagnosticParameterSupportInfo,
    DiagnosticPeriodicRate,
    DiagnosticSupportInfoByte,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDebounceAlgorithmProps, DiagnosticFunctionInhibitSource, DiagnosticParameterElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    ByteOrderEnum,
    DateTime,
    DiagnosticConnectedIndicatorBehaviorEnum,
    DiagnosticEventCombinationBehaviorEnum,
    DiagnosticEventCombinationReportingBehaviorEnum,
    DiagnosticEventWindowTimeEnum,
    DiagnosticInhibitionMaskEnum,
    DiagnosticOccurrenceCounterProcessingEnum,
    DiagnosticPeriodicRateCategoryEnum,
    NameToken,
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
        assert obj.getPeriodicRateCategory().getValue() == "periodicRateMedium"

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
        assert obj.getEventWindowTime().getValue() == "infiniteTimeToResponse"

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
        assert obj.getBehavior().getValue() == "blinkMode"

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
        assert obj.getInhibitionMask().getValue() == "testedAndFailed"

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
