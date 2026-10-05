"""Writer/reader round-trip tests for the ComSpec family (PPortComSpec / RPortComSpec / ReceiverComSpec)."""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import NumericalValueSpecification, TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter, DataFilterTypeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DateTime, Numerical, PositiveInteger, RefType, String, TimeValue, VerbatimString
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    ClientComSpec,
    CompositeNetworkRepresentation,
    HandleOutOfRangeEnum,
    HandleOutOfRangeStatusEnum,
    HandleTimeoutEnum,
    NonqueuedReceiverComSpec,
    NonqueuedSenderComSpec,
    ParameterProvideComSpec,
    ReceptionComSpecProps,
    ServerComSpec,
    TransmissionAcknowledgementRequest,
    TransmissionComSpecProps,
    TransmissionModeDefinitionEnum,
    UserDefinedTransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationComSpecProps
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_document_with_ports():
    AUTOSAR.getInstance().setARRelease("R23-11")
    document = AUTOSAR.getInstance()
    document.clear()
    pkg = document.createARPackage("AUTOSAR")
    swc = pkg.createApplicationSwComponentType("App")
    return document, swc.createPPortPrototype("PP"), swc.createRPortPrototype("RP")


def _round_trip_ports(document):
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)

        swc = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
        return swc.getPPortPrototypes()[0], swc.getRPortPrototypes()[0]
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


class TestPPortComSpecRoundTrip:
    def test_server_com_spec_round_trip(self):
        """PPortComSpec has no own XML elements; coverage flows through a concrete subclass dispatch (writePPortComSpec)."""
        _, p_port, _ = _new_document_with_ports()

        com_spec = ServerComSpec()
        com_spec.setOperationRef(_ref("/Swc/Iface/Op", "CLIENT-SERVER-OPERATION"))
        queue = PositiveInteger()
        queue.setValue("4")
        com_spec.setQueueLength(queue)
        com_spec.addTransformationComSpecProps(UserDefinedTransformationComSpecProps())
        p_port.addProvidedComSpec(com_spec)

        p_port_2, _ = _round_trip_ports(AUTOSAR.getInstance())

        com_specs = p_port_2.getProvidedComSpecs()
        assert len(com_specs) == 1
        assert com_specs[0].getOperationRef().getValue() == "/Swc/Iface/Op"
        assert com_specs[0].getOperationRef().getDest() == "CLIENT-SERVER-OPERATION"
        assert com_specs[0].getQueueLength().getValue() == 4
        transformation_props = com_specs[0].getTransformationComSpecProps()
        assert len(transformation_props) == 1
        assert isinstance(transformation_props[0], UserDefinedTransformationComSpecProps)

    def test_server_com_spec_xml_element_order_matches_xsd(self):
        """Writer emission order follows the XSD SERVER-COM-SPEC group sequence (Rule 0001.11)."""
        document, p_port, _ = _new_document_with_ports()

        com_spec = ServerComSpec()
        com_spec.setOperationRef(_ref("/Swc/Iface/Op", "CLIENT-SERVER-OPERATION"))
        queue = PositiveInteger()
        queue.setValue("4")
        com_spec.setQueueLength(queue)
        com_spec.addTransformationComSpecProps(UserDefinedTransformationComSpecProps())
        p_port.addProvidedComSpec(com_spec)

        root = _write_and_load_raw(document)
        com_spec_element = root.find(".//{*}P-PORT-PROTOTYPE/{*}PROVIDED-COM-SPECS/{*}SERVER-COM-SPEC")
        tags = [child.tag.split("}")[-1] for child in com_spec_element]
        server_tags = [
            "OPERATION-REF",
            "QUEUE-LENGTH",
            "TRANSFORMATION-COM-SPEC-PROPSS",
        ]
        emitted = [tag for tag in tags if tag in server_tags]
        assert emitted == server_tags

    def test_empty_provided_com_specs(self):
        _, p_port, _ = _new_document_with_ports()

        p_port_2, _ = _round_trip_ports(AUTOSAR.getInstance())

        assert p_port_2.getProvidedComSpecs() == []


class TestParameterProvideComSpecRoundTrip:
    def test_parameter_provide_com_spec_round_trip(self):
        """ParameterProvideComSpec attributes round-trip with field values intact (writePPortComSpec dispatch)."""
        document, p_port, _ = _new_document_with_ports()

        com_spec = ParameterProvideComSpec()
        com_spec.setInitValue(TextValueSpecification().setValue(VerbatimString().setValue("init")))
        com_spec.setParameterRef(_ref("/Swc/Iface/Param", "PARAMETER-DATA-PROTOTYPE"))
        p_port.addProvidedComSpec(com_spec)

        p_port_2, _ = _round_trip_ports(document)

        com_specs = p_port_2.getProvidedComSpecs()
        assert len(com_specs) == 1
        assert isinstance(com_specs[0], ParameterProvideComSpec)
        assert isinstance(com_specs[0].getInitValue(), TextValueSpecification)
        assert com_specs[0].getInitValue().getValue().getValue() == "init"
        assert com_specs[0].getParameterRef().getValue() == "/Swc/Iface/Param"
        assert com_specs[0].getParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"

    def test_parameter_provide_com_spec_xml_element_order_matches_xsd(self):
        """Writer emission order follows the XSD PARAMETER-PROVIDE-COM-SPEC group sequence (Rule 0001.11)."""
        document, p_port, _ = _new_document_with_ports()

        com_spec = ParameterProvideComSpec()
        com_spec.setInitValue(TextValueSpecification().setValue(VerbatimString().setValue("init")))
        com_spec.setParameterRef(_ref("/Swc/Iface/Param", "PARAMETER-DATA-PROTOTYPE"))
        p_port.addProvidedComSpec(com_spec)

        root = _write_and_load_raw(document)
        com_spec_element = root.find(".//{*}P-PORT-PROTOTYPE/{*}PROVIDED-COM-SPECS/{*}PARAMETER-PROVIDE-COM-SPEC")
        tags = [child.tag.split("}")[-1] for child in com_spec_element]
        provide_tags = [
            "INIT-VALUE",
            "PARAMETER-REF",
        ]
        emitted = [tag for tag in tags if tag in provide_tags]
        assert emitted == provide_tags


class TestRPortComSpecRoundTrip:
    def test_client_com_spec_round_trip(self):
        """RPortComSpec has no own XML elements; coverage flows through a concrete subclass dispatch (writeRPortComSpec)."""
        _, _, r_port = _new_document_with_ports()

        com_spec = ClientComSpec()
        com_spec.setEndToEndCallResponseTimeout(TimeValue().setValue("1.5"))
        com_spec.setOperationRef(_ref("/Swc/Iface/Op", "CLIENT-SERVER-OPERATION"))
        com_spec.addTransformationComSpecProps(UserDefinedTransformationComSpecProps())
        e2e_props = EndToEndTransformationComSpecProps()
        max_delta_counter = PositiveInteger()
        max_delta_counter.setValue("2")
        e2e_props.setMaxDeltaCounter(max_delta_counter)
        com_spec.addTransformationComSpecProps(e2e_props)
        r_port.addRequiredComSpec(com_spec)

        _, r_port_2 = _round_trip_ports(AUTOSAR.getInstance())

        com_specs = r_port_2.getRequiredComSpecs()
        assert len(com_specs) == 1
        assert com_specs[0].getEndToEndCallResponseTimeout().getValue() == 1.5
        assert com_specs[0].getOperationRef().getValue() == "/Swc/Iface/Op"
        assert com_specs[0].getOperationRef().getDest() == "CLIENT-SERVER-OPERATION"
        transformation_props = com_specs[0].getTransformationComSpecProps()
        assert len(transformation_props) == 2
        assert isinstance(transformation_props[0], UserDefinedTransformationComSpecProps)
        assert isinstance(transformation_props[1], EndToEndTransformationComSpecProps)
        assert transformation_props[1].getMaxDeltaCounter().getValue() == 2

    def test_client_com_spec_xml_element_order_matches_xsd(self):
        """Writer emission order follows the XSD CLIENT-COM-SPEC group sequence (Rule 0001.11)."""
        document, _, r_port = _new_document_with_ports()

        com_spec = ClientComSpec()
        com_spec.setEndToEndCallResponseTimeout(TimeValue().setValue("1.5"))
        com_spec.setOperationRef(_ref("/Swc/Iface/Op", "CLIENT-SERVER-OPERATION"))
        com_spec.addTransformationComSpecProps(UserDefinedTransformationComSpecProps())
        r_port.addRequiredComSpec(com_spec)

        root = _write_and_load_raw(document)
        com_spec_element = root.find(".//{*}R-PORT-PROTOTYPE/{*}REQUIRED-COM-SPECS/{*}CLIENT-COM-SPEC")
        tags = [child.tag.split("}")[-1] for child in com_spec_element]
        client_tags = [
            "END-TO-END-CALL-RESPONSE-TIMEOUT",
            "OPERATION-REF",
            "TRANSFORMATION-COM-SPEC-PROPSS",
        ]
        emitted = [tag for tag in tags if tag in client_tags]
        assert emitted == client_tags

    def test_client_com_spec_empty_props_no_wrapper(self):
        """A ClientComSpec without transformationComSpecProps emits no TRANSFORMATION-COM-SPEC-PROPSS wrapper and re-parses to []."""
        document, _, r_port = _new_document_with_ports()

        com_spec = ClientComSpec()
        com_spec.setOperationRef(_ref("/Swc/Iface/Op", "CLIENT-SERVER-OPERATION"))
        r_port.addRequiredComSpec(com_spec)

        root = _write_and_load_raw(document)
        com_spec_element = root.find(".//{*}CLIENT-COM-SPEC")
        assert com_spec_element.find("{*}TRANSFORMATION-COM-SPEC-PROPSS") is None

        _, r_port_2 = _round_trip_ports(document)
        assert r_port_2.getRequiredComSpecs()[0].getTransformationComSpecProps() == []

    def test_empty_required_com_specs(self):
        _, _, r_port = _new_document_with_ports()

        _, r_port_2 = _round_trip_ports(AUTOSAR.getInstance())

        assert r_port_2.getRequiredComSpecs() == []


def _write_and_load_raw(document):
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, document)
        return ET.parse(file_path).getroot()
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def _new_nonqueued_com_spec():
    com_spec = NonqueuedReceiverComSpec()
    com_spec.setDataElementRef(_ref("/Swc/Vdp", "VARIABLE-DATA-PROTOTYPE"))
    com_spec.setHandleOutOfRange(HandleOutOfRangeEnum().setValue(HandleOutOfRangeEnum.EXTERNAL_REPLACEMENT))
    com_spec.setHandleOutOfRangeStatus(HandleOutOfRangeStatusEnum().setValue(HandleOutOfRangeStatusEnum.INDICATE))
    max_delta = PositiveInteger()
    max_delta.setValue("2")
    com_spec.setMaxDeltaCounterInit(max_delta)
    max_no_new = PositiveInteger()
    max_no_new.setValue("3")
    com_spec.setMaxNoNewOrRepeatedData(max_no_new)
    com_spec.setReceptionProps(ReceptionComSpecProps().setTimeout(TimeValue().setValue("0.5")))
    uses_e2e = Boolean()
    uses_e2e.setValue(True)
    com_spec.setUsesEndToEndProtection(uses_e2e)
    sync_counter = PositiveInteger()
    sync_counter.setValue("1")
    com_spec.setSyncCounterInit(sync_counter)
    com_spec.setAliveTimeout(TimeValue().setValue("1.5"))
    enable_update = Boolean()
    enable_update.setValue(False)
    com_spec.setEnableUpdate(enable_update)
    data_filter = DataFilter()
    data_filter.setDataFilterType(DataFilterTypeEnum().setValue(DataFilterTypeEnum.ONE_EVERY_N))
    com_spec.setFilter(data_filter)
    handle_data_status = Boolean()
    handle_data_status.setValue(True)
    com_spec.setHandleDataStatus(handle_data_status)
    handle_never = Boolean()
    handle_never.setValue(True)
    com_spec.setHandleNeverReceived(handle_never)
    com_spec.setHandleTimeoutType(HandleTimeoutEnum().setValue(HandleTimeoutEnum.REPLACE_BY_TIMEOUT_SUBSTITUTION_VALUE))
    com_spec.setInitValue(TextValueSpecification().setValue(VerbatimString().setValue("42")))
    com_spec.setTimeoutSubstitutionValue(NumericalValueSpecification().setValue(Numerical().setValue("7")))
    return com_spec


class TestReceiverComSpecRoundTrip:
    def test_nonqueued_receiver_com_spec_round_trip(self):
        """ReceiverComSpec + NonqueuedReceiverComSpec attributes round-trip with field values intact."""
        document, _, r_port = _new_document_with_ports()

        r_port.addRequiredComSpec(_new_nonqueued_com_spec())

        _, r_port_2 = _round_trip_ports(document)

        com_specs = r_port_2.getRequiredComSpecs()
        assert len(com_specs) == 1
        com_spec = com_specs[0]
        assert isinstance(com_spec, NonqueuedReceiverComSpec)
        assert com_spec.getDataElementRef().getValue() == "/Swc/Vdp"
        assert com_spec.getDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert com_spec.getHandleOutOfRange().getValue() == "externalReplacement"
        assert com_spec.getHandleOutOfRangeStatus().getValue() == "indicate"
        assert com_spec.getMaxDeltaCounterInit().getValue() == 2
        assert com_spec.getMaxNoNewOrRepeatedData().getValue() == 3
        assert com_spec.getReceptionProps().getTimeout().getValue() == 0.5
        assert com_spec.getUsesEndToEndProtection().getValue() is True
        assert com_spec.getSyncCounterInit().getValue() == 1
        assert isinstance(com_spec.getAliveTimeout(), TimeValue)
        assert com_spec.getAliveTimeout().getValue() == 1.5
        assert com_spec.getEnableUpdate().getValue() is False
        assert com_spec.getFilter().getDataFilterType().getValue() == "ONE-EVERY-N"
        assert com_spec.getHandleDataStatus().getValue() is True
        assert com_spec.getHandleNeverReceived().getValue() is True
        assert com_spec.getHandleTimeoutType().getValue() == "replaceByTimeoutSubstitutionValue"
        assert isinstance(com_spec.getInitValue(), TextValueSpecification)
        assert com_spec.getInitValue().getValue().getValue() == "42"
        assert isinstance(com_spec.getTimeoutSubstitutionValue(), NumericalValueSpecification)
        assert com_spec.getTimeoutSubstitutionValue().getValue().getValue() == 7
        assert com_spec.getCompositeNetworkRepresentations() == []
        assert com_spec.getNetworkRepresentation() is None
        assert com_spec.getReplaceWith() is None
        assert com_spec.getTransformationComSpecProps() == []

    def test_handle_timeout_type_xml_carries_xsd_token(self):
        """HANDLE-TIMEOUT-TYPE is written as the XSD token and read back as the camelCase literal (HANDLE_TIMEOUT_XML_MAP)."""
        document, _, r_port = _new_document_with_ports()

        com_spec = NonqueuedReceiverComSpec()
        com_spec.setHandleTimeoutType(HandleTimeoutEnum().setValue(HandleTimeoutEnum.REPLACE_BY_TIMEOUT_SUBSTITUTION_VALUE))
        r_port.addRequiredComSpec(com_spec)

        root = _write_and_load_raw(document)
        timeout_type_element = root.find(".//{*}NONQUEUED-RECEIVER-COM-SPEC/{*}HANDLE-TIMEOUT-TYPE")
        assert timeout_type_element.text == "REPLACE-BY-TIMEOUT-SUBSTITUTION-VALUE"

        _, r_port_2 = _round_trip_ports(document)
        com_spec_2 = r_port_2.getRequiredComSpecs()[0]
        assert com_spec_2.getHandleTimeoutType().getValue() == "replaceByTimeoutSubstitutionValue"

    def test_handle_out_of_range_xml_carries_xsd_token(self):
        """HANDLE-OUT-OF-RANGE is written as the XSD token and read back as the camelCase literal (HANDLE_OUT_OF_RANGE_XML_MAP)."""
        document, p_port, r_port = _new_document_with_ports()

        sender = NonqueuedSenderComSpec()
        sender.setHandleOutOfRange(HandleOutOfRangeEnum().setValue(HandleOutOfRangeEnum.EXTERNAL_REPLACEMENT))
        p_port.addProvidedComSpec(sender)

        receiver = NonqueuedReceiverComSpec()
        receiver.setHandleOutOfRange(HandleOutOfRangeEnum().setValue(HandleOutOfRangeEnum.SATURATE))
        r_port.addRequiredComSpec(receiver)

        root = _write_and_load_raw(document)
        assert root.find(".//{*}NONQUEUED-SENDER-COM-SPEC/{*}HANDLE-OUT-OF-RANGE").text == "EXTERNAL-REPLACEMENT"
        assert root.find(".//{*}NONQUEUED-RECEIVER-COM-SPEC/{*}HANDLE-OUT-OF-RANGE").text == "SATURATE"

        p_port_2, r_port_2 = _round_trip_ports(document)
        assert p_port_2.getProvidedComSpecs()[0].getHandleOutOfRange().getValue() == "externalReplacement"
        assert r_port_2.getRequiredComSpecs()[0].getHandleOutOfRange().getValue() == "saturate"

    def test_nonqueued_receiver_com_spec_schema_valid_output(self):
        """A save carrying HANDLE-TIMEOUT-TYPE must pass the bundled R23-11 XSD when schema location is set."""
        document, _, r_port = _new_document_with_ports()
        document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"

        com_spec = NonqueuedReceiverComSpec()
        com_spec.setAliveTimeout(TimeValue().setValue("1.5"))
        com_spec.setHandleOutOfRange(HandleOutOfRangeEnum().setValue(HandleOutOfRangeEnum.NONE))
        com_spec.setHandleTimeoutType(HandleTimeoutEnum().setValue(HandleTimeoutEnum.REPLACE))
        r_port.addRequiredComSpec(com_spec)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

        com_spec_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0].getRPortPrototypes()[0].getRequiredComSpecs()[0]
        assert com_spec_2.getHandleTimeoutType().getValue() == "replace"
        assert com_spec_2.getHandleOutOfRange().getValue() == "none"
        assert com_spec_2.getAliveTimeout().getValue() == 1.5

    def test_receiver_com_spec_xml_element_order_matches_xsd(self):
        """Writer emission order follows the XSD RECEIVER-COM-SPEC / NONQUEUED-RECEIVER-COM-SPEC group sequences (Rule 0001.11)."""
        document, _, r_port = _new_document_with_ports()

        r_port.addRequiredComSpec(_new_nonqueued_com_spec())

        root = _write_and_load_raw(document)
        com_spec_element = root.find(".//{*}R-PORT-PROTOTYPE/{*}REQUIRED-COM-SPECS/{*}NONQUEUED-RECEIVER-COM-SPEC")
        tags = [child.tag for child in com_spec_element]
        receiver_tags = [
            "COMPOSITE-NETWORK-REPRESENTATIONS",
            "DATA-ELEMENT-REF",
            "HANDLE-OUT-OF-RANGE",
            "HANDLE-OUT-OF-RANGE-STATUS",
            "MAX-DELTA-COUNTER-INIT",
            "MAX-NO-NEW-OR-REPEATED-DATA",
            "NETWORK-REPRESENTATION",
            "RECEPTION-PROPS",
            "REPLACE-WITH",
            "SYNC-COUNTER-INIT",
            "TRANSFORMATION-COM-SPEC-PROPSS",
            "USES-END-TO-END-PROTECTION",
            "ALIVE-TIMEOUT",
            "ENABLE-UPDATE",
            "FILTER",
            "HANDLE-DATA-STATUS",
            "HANDLE-NEVER-RECEIVED",
            "HANDLE-TIMEOUT-TYPE",
            "INIT-VALUE",
            "TIMEOUT-SUBSTITUTION-VALUE",
        ]
        emitted = [tag for tag in tags if tag in receiver_tags]
        expected = [tag for tag in receiver_tags if tag in set(tags)]
        assert emitted == expected

    def test_empty_required_com_specs(self):
        _, _, r_port = _new_document_with_ports()

        _, r_port_2 = _round_trip_ports(AUTOSAR.getInstance())

        assert r_port_2.getRequiredComSpecs() == []


def _new_nonqueued_sender_com_spec():
    com_spec = NonqueuedSenderComSpec()
    com_spec.setDataElementRef(_ref("/Swc/Vdp", "VARIABLE-DATA-PROTOTYPE"))
    com_spec.setHandleOutOfRange(HandleOutOfRangeEnum().setValue(HandleOutOfRangeEnum.DEFAULT))
    com_spec.setNetworkRepresentation(SwDataDefProps())
    com_spec.setTransmissionAcknowledge(TransmissionAcknowledgementRequest().setTimeout(TimeValue().setValue("2.5")))
    com_spec.setTransmissionProps(TransmissionComSpecProps().setMinimumSendInterval(TimeValue().setValue("0.2")))
    uses_e2e = Boolean()
    uses_e2e.setValue(True)
    com_spec.setUsesEndToEndProtection(uses_e2e)
    representation = CompositeNetworkRepresentation()
    com_spec.addCompositeNetworkRepresentation(representation)
    data_filter = DataFilter()
    data_filter.setDataFilterType(DataFilterTypeEnum().setValue(DataFilterTypeEnum.ALWAYS))
    com_spec.setDataFilter(data_filter)
    com_spec.setInitValue(TextValueSpecification().setValue(VerbatimString().setValue("init")))
    return com_spec


class TestSenderComSpecRoundTrip:
    def test_nonqueued_sender_com_spec_round_trip(self):
        """SenderComSpec + NonqueuedSenderComSpec attributes round-trip with field values intact."""
        document, p_port, _ = _new_document_with_ports()

        p_port.addProvidedComSpec(_new_nonqueued_sender_com_spec())

        p_port_2, _ = _round_trip_ports(document)

        com_specs = p_port_2.getProvidedComSpecs()
        assert len(com_specs) == 1
        com_spec = com_specs[0]
        assert isinstance(com_spec, NonqueuedSenderComSpec)
        assert com_spec.getDataElementRef().getValue() == "/Swc/Vdp"
        assert com_spec.getDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert com_spec.getHandleOutOfRange().getValue() == "default"
        assert com_spec.getNetworkRepresentation() is not None
        assert com_spec.getTransmissionAcknowledge().getTimeout().getValue() == 2.5
        assert com_spec.getTransmissionProps().getMinimumSendInterval().getValue() == 0.2
        assert com_spec.getUsesEndToEndProtection().getValue() is True
        assert len(com_spec.getCompositeNetworkRepresentations()) == 1
        assert isinstance(com_spec.getCompositeNetworkRepresentations()[0], CompositeNetworkRepresentation)
        assert com_spec.getDataFilter().getDataFilterType().getValue() == "ALWAYS"
        assert isinstance(com_spec.getInitValue(), TextValueSpecification)
        assert com_spec.getInitValue().getValue().getValue() == "init"

    def test_sender_com_spec_xml_element_order_matches_xsd(self):
        """Writer emission order follows the XSD SENDER-COM-SPEC / NONQUEUED-SENDER-COM-SPEC group sequences (Rule 0001.11)."""
        document, p_port, _ = _new_document_with_ports()

        p_port.addProvidedComSpec(_new_nonqueued_sender_com_spec())

        root = _write_and_load_raw(document)
        com_spec_element = root.find(".//{*}P-PORT-PROTOTYPE/{*}PROVIDED-COM-SPECS/{*}NONQUEUED-SENDER-COM-SPEC")
        tags = [child.tag for child in com_spec_element]
        sender_tags = [
            "COMPOSITE-NETWORK-REPRESENTATIONS",
            "DATA-ELEMENT-REF",
            "HANDLE-OUT-OF-RANGE",
            "NETWORK-REPRESENTATION",
            "TRANSMISSION-ACKNOWLEDGE",
            "TRANSMISSION-PROPS",
            "USES-END-TO-END-PROTECTION",
            "DATA-FILTER",
            "INIT-VALUE",
        ]
        emitted = [tag for tag in tags if tag in sender_tags]
        expected = [tag for tag in sender_tags if tag in set(tags)]
        assert emitted == expected


def _new_transmission_com_spec_props():
    props = TransmissionComSpecProps()
    props.setDataUpdatePeriod(TimeValue().setValue("0.01"))
    props.setMinimumSendInterval(TimeValue().setValue("0.2"))
    props.setTransmissionMode(TransmissionModeDefinitionEnum().setValue(TransmissionModeDefinitionEnum.CYCLIC_AND_ON_CHANGE))
    return props


class TestTransmissionComSpecPropsRoundTrip:
    def test_transmission_com_spec_props_round_trip(self):
        """TransmissionComSpecProps attributes round-trip inside TRANSMISSION-PROPS with field values intact."""
        document, p_port, _ = _new_document_with_ports()

        com_spec = NonqueuedSenderComSpec()
        com_spec.setTransmissionProps(_new_transmission_com_spec_props())
        p_port.addProvidedComSpec(com_spec)

        p_port_2, _ = _round_trip_ports(document)

        com_spec_2 = p_port_2.getProvidedComSpecs()[0]
        props = com_spec_2.getTransmissionProps()
        assert isinstance(props, TransmissionComSpecProps)
        assert props.getDataUpdatePeriod().getValue() == 0.01
        assert props.getMinimumSendInterval().getValue() == 0.2
        assert props.getTransmissionMode().getValue() == "cyclicAndOnChange"

    def test_transmission_mode_xml_carries_xsd_token(self):
        """TRANSMISSION-MODE is written as the XSD token and read back as the camelCase literal (TRANSMISSION_MODE_DEFINITION_XML_MAP)."""
        document, p_port, _ = _new_document_with_ports()

        com_spec = NonqueuedSenderComSpec()
        com_spec.setTransmissionProps(_new_transmission_com_spec_props())
        p_port.addProvidedComSpec(com_spec)

        root = _write_and_load_raw(document)
        mode_element = root.find(".//{*}TRANSMISSION-PROPS/{*}TRANSMISSION-MODE")
        assert mode_element.text == "CYCLIC-AND-ON-CHANGE"

        p_port_2, _ = _round_trip_ports(document)
        props_2 = p_port_2.getProvidedComSpecs()[0].getTransmissionProps()
        assert props_2.getTransmissionMode().getValue() == "cyclicAndOnChange"

    def test_transmission_com_spec_props_schema_valid_output(self):
        """A save carrying TRANSMISSION-PROPS must pass the bundled R23-11 XSD when schema location is set."""
        document, p_port, _ = _new_document_with_ports()
        document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"

        com_spec = NonqueuedSenderComSpec()
        com_spec.setTransmissionAcknowledge(TransmissionAcknowledgementRequest().setTimeout(TimeValue().setValue("2.5")))
        com_spec.setTransmissionProps(_new_transmission_com_spec_props())
        p_port.addProvidedComSpec(com_spec)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

        com_spec_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0].getPPortPrototypes()[0].getProvidedComSpecs()[0]
        assert com_spec_2.getTransmissionAcknowledge().getTimeout().getValue() == 2.5
        props_2 = com_spec_2.getTransmissionProps()
        assert props_2.getDataUpdatePeriod().getValue() == 0.01
        assert props_2.getMinimumSendInterval().getValue() == 0.2
        assert props_2.getTransmissionMode().getValue() == "cyclicAndOnChange"

    def test_empty_transmission_props_round_trip(self):
        """A SenderComSpec without transmissionProps round-trips with the field unset."""
        document, p_port, _ = _new_document_with_ports()

        p_port.addProvidedComSpec(NonqueuedSenderComSpec())

        p_port_2, _ = _round_trip_ports(document)

        com_spec_2 = p_port_2.getProvidedComSpecs()[0]
        assert com_spec_2.getTransmissionProps() is None
        assert com_spec_2.getTransmissionAcknowledge() is None


class TestTransmissionAcknowledgementRequestRoundTrip:
    def test_transmission_acknowledge_round_trip(self):
        """TransmissionAcknowledgementRequest (TRANSMISSION-ACKNOWLEDGE/TIMEOUT) round-trips with values and ARObject S/T intact."""
        document, p_port, _ = _new_document_with_ports()

        acknowledge = TransmissionAcknowledgementRequest()
        acknowledge.setTimeout(TimeValue().setValue("2.5"))
        checksum = String()
        checksum.setValue("ab12")
        acknowledge.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2023-11-15T08:00:00+00:00")
        acknowledge.setTimestamp(timestamp)
        com_spec = NonqueuedSenderComSpec()
        com_spec.setTransmissionAcknowledge(acknowledge)
        p_port.addProvidedComSpec(com_spec)

        p_port_2, _ = _round_trip_ports(document)

        acknowledge_2 = p_port_2.getProvidedComSpecs()[0].getTransmissionAcknowledge()
        assert isinstance(acknowledge_2, TransmissionAcknowledgementRequest)
        assert acknowledge_2.getTimeout().getValue() == 2.5
        assert acknowledge_2.getChecksum().getValue() == "ab12"
        assert acknowledge_2.getTimestamp().getValue() == "2023-11-15T08:00:00+00:00"

    def test_transmission_acknowledge_xml_element_order_matches_xsd(self):
        """The TRANSMISSION-ACKNOWLEDGE group sequence is S/T attributes then TIMEOUT (AUTOSAR_00052.xsd)."""
        document, p_port, _ = _new_document_with_ports()

        acknowledge = TransmissionAcknowledgementRequest()
        acknowledge.setTimeout(TimeValue().setValue("1.0"))
        checksum = String()
        checksum.setValue("ff")
        acknowledge.setChecksum(checksum)
        com_spec = NonqueuedSenderComSpec()
        com_spec.setTransmissionAcknowledge(acknowledge)
        p_port.addProvidedComSpec(com_spec)

        root = _write_and_load_raw(document)
        acknowledge_element = root.find(".//{*}TRANSMISSION-ACKNOWLEDGE")
        children = [child.tag.split("}")[-1] for child in acknowledge_element]
        assert "TIMEOUT" in children
        assert children.index("TIMEOUT") == len(children) - 1
        assert acknowledge_element.attrib.get("S") == "ff"
