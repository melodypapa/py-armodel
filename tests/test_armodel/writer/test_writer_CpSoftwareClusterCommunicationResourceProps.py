"""Writer/reader round-trip tests for the CpSoftwareClusterCommunicationResourceProps reusable helper (Table 11.9, p.902)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import CpSoftwareClusterCommunicationResourceProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class ConcreteComProps(CpSoftwareClusterCommunicationResourceProps):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_props():
    props = ConcreteComProps()
    props.setChecksum(String().setValue("21"))
    return props


class TestWriteCpSoftwareClusterCommunicationResourceProps:
    def test_write_ar_object_level(self, writer):
        """
        The helper writes the ARObject level (S checksum attribute) onto the concrete subclass
        element passed by the caller and emits no own elements (empty XSD group).
        """
        element = ET.Element("DATA-COM-PROPS")
        writer.writeCpSoftwareClusterCommunicationResourceProps(element, _new_props())

        assert element.attrib["S"] == "21"
        assert len(element) == 0

    def test_write_without_ar_object_content(self, writer):
        """
        An unset ARObject state emits no attribute and no child elements.
        """
        element = ET.Element("CLIENT-SERVER-OPERATION-COM-PROPS")
        writer.writeCpSoftwareClusterCommunicationResourceProps(element, ConcreteComProps())

        assert "S" not in element.attrib
        assert len(element) == 0


class TestCpSoftwareClusterCommunicationResourcePropsRoundTrip:
    def test_round_trip_preserves_ar_object_level(self, writer, parser):
        """
        Write -> serialize -> parse keeps the ARObject-level content.
        """
        element = ET.Element("DATA-COM-PROPS")
        writer.writeCpSoftwareClusterCommunicationResourceProps(element, _new_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readCpSoftwareClusterCommunicationResourceProps(parsed_element, ConcreteComProps())

        assert props.getChecksum().getValue() == "21"
