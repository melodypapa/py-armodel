"""Writer/reader round-trip tests for the PortPrototype port-annotation classes."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import ParameterPortAnnotation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _round_trip(document):
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)

        return document_2.getARPackages()[0].getAtomicSwComponentTypes()[0].getPRPortPrototypes()[0]
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def _new_document_with_port():
    AUTOSAR.getInstance().setARRelease("R23-11")
    document = AUTOSAR.getInstance()
    document.clear()
    pkg = document.createARPackage("AUTOSAR")
    swc = pkg.createApplicationSwComponentType("App")
    return document, swc.createPRPortPrototype("Port")


class TestParameterPortAnnotationRoundTrip:
    def test_round_trip(self):
        _, port = _new_document_with_port()

        param = ParameterPortAnnotation()
        param.setParameterRef(_ref("/Swc/Param", "PARAMETER-DATA-PROTOTYPE"))
        port.addParameterPortAnnotation(param)

        port_2 = _round_trip(AUTOSAR.getInstance())

        param_list = port_2.getParameterPortAnnotations()
        assert len(param_list) == 1
        assert param_list[0].getParameterRef().getValue() == "/Swc/Param"
        assert param_list[0].getParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"

    def test_empty_wrapper_list(self):
        _, port = _new_document_with_port()

        port_2 = _round_trip(AUTOSAR.getInstance())

        assert port_2.getParameterPortAnnotations() == []
