"""Writer/reader round-trip tests for the ComSpec family (PPortComSpec / RPortComSpec / ReceiverComSpec)."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ServerComSpec
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
