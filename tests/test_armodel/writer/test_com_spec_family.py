"""Writer/reader round-trip tests for the ComSpec family (PPortComSpec / RPortComSpec / ReceiverComSpec)."""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import NumericalValueSpecification, TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter, DataFilterTypeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Numerical, PositiveInteger, RefType, TimeValue, VerbatimString
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    ClientComSpec,
    HandleOutOfRangeEnum,
    HandleOutOfRangeStatusEnum,
    HandleTimeoutEnum,
    NonqueuedReceiverComSpec,
    ReceptionComSpecProps,
    ServerComSpec,
)
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
        p_port.addProvidedComSpec(com_spec)

        p_port_2, _ = _round_trip_ports(AUTOSAR.getInstance())

        com_specs = p_port_2.getProvidedComSpecs()
        assert len(com_specs) == 1
        assert com_specs[0].getOperationRef().getValue() == "/Swc/Iface/Op"
        assert com_specs[0].getOperationRef().getDest() == "CLIENT-SERVER-OPERATION"
        assert com_specs[0].getQueueLength().getValue() == 4

    def test_empty_provided_com_specs(self):
        _, p_port, _ = _new_document_with_ports()

        p_port_2, _ = _round_trip_ports(AUTOSAR.getInstance())

        assert p_port_2.getProvidedComSpecs() == []


class TestRPortComSpecRoundTrip:
    def test_client_com_spec_round_trip(self):
        """RPortComSpec has no own XML elements; coverage flows through a concrete subclass dispatch (writeRPortComSpec)."""
        _, _, r_port = _new_document_with_ports()

        com_spec = ClientComSpec()
        com_spec.setOperationRef(_ref("/Swc/Iface/Op", "CLIENT-SERVER-OPERATION"))
        r_port.addRequiredComSpec(com_spec)

        _, r_port_2 = _round_trip_ports(AUTOSAR.getInstance())

        com_specs = r_port_2.getRequiredComSpecs()
        assert len(com_specs) == 1
        assert com_specs[0].getOperationRef().getValue() == "/Swc/Iface/Op"
        assert com_specs[0].getOperationRef().getDest() == "CLIENT-SERVER-OPERATION"

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

    def test_nonqueued_receiver_com_spec_schema_valid_output(self):
        """A save carrying HANDLE-TIMEOUT-TYPE must pass the bundled R23-11 XSD when schema location is set."""
        document, _, r_port = _new_document_with_ports()
        document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"

        com_spec = NonqueuedReceiverComSpec()
        com_spec.setAliveTimeout(TimeValue().setValue("1.5"))
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
