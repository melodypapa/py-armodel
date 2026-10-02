"""Writer/reader round-trip tests for ApplicationInterface (APPLICATION-INTERFACE)."""

import os
import tempfile

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AbstractPlatform import ApplicationInterface
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface import Field
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ClientServerOperation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestApplicationInterfaceRoundTrip:
    def test_application_interface_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        interface = ar_root.createApplicationInterface("AppInterface1")

        field = Field(interface, "Field1")
        field.setHasGetter(True)
        field.setHasSetter(True)
        operation = ClientServerOperation(interface, "Operation1")
        indication = VariableDataPrototype(interface, "Indication1")
        interface.setAttributes([field])
        interface.setCommands([operation])
        interface.setIndications([indication])

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            parsed_pkg = document_2.getARPackages()[0]
            parsed_interfaces = [el for el in parsed_pkg.getReferrableElements() if isinstance(el, ApplicationInterface)]
            assert len(parsed_interfaces) == 1
            parsed = parsed_interfaces[0]
            assert parsed.getShortName() == "AppInterface1"

            attributes = parsed.getAttributes()
            assert len(attributes) == 1
            assert isinstance(attributes[0], Field)
            assert attributes[0].getShortName() == "Field1"
            assert attributes[0].getHasGetter().getValue() is True
            assert attributes[0].getHasSetter().getValue() is True

            commands = parsed.getCommands()
            assert len(commands) == 1
            assert isinstance(commands[0], ClientServerOperation)
            assert commands[0].getShortName() == "Operation1"

            indications = parsed.getIndications()
            assert len(indications) == 1
            assert isinstance(indications[0], VariableDataPrototype)
            assert indications[0].getShortName() == "Indication1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_application_interface_empty_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        ar_root.createApplicationInterface("EmptyInterface")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            parsed_pkg = document_2.getARPackages()[0]
            parsed_interfaces = [el for el in parsed_pkg.getReferrableElements() if isinstance(el, ApplicationInterface)]
            assert len(parsed_interfaces) == 1
            assert parsed_interfaces[0].getAttributes() == []
            assert parsed_interfaces[0].getCommands() == []
            assert parsed_interfaces[0].getIndications() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
