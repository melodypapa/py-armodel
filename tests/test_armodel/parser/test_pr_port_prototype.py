"""Reader/writer round-trip tests for PRPortPrototype."""

import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestPRPortPrototypeRoundTrip:
    def _build(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")
        port = swc.createPRPortPrototype("TestPort")
        port.setProvidedRequiredInterfaceTRef(_ref("/Interface/Ref", "PORT-INTERFACE"))
        return document

    def test_round_trip_with_interface_tref(self):
        document = self._build()
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            port_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0].getPRPortPrototypes()[0]
            tref = port_2.getProvidedRequiredInterfaceTRef()
            assert tref is not None
            assert tref.getValue() == "/Interface/Ref"
            assert tref.getDest() == "PORT-INTERFACE"
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_without_interface_tref(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")
        swc.createPRPortPrototype("TestPort")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            port_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0].getPRPortPrototypes()[0]
            assert port_2.getProvidedRequiredInterfaceTRef() is None
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)
