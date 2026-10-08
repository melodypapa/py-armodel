"""Reader tests for the CpSoftwareClusterCommunicationResourceProps reusable helper (Table 11.9, p.902)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import CpSoftwareClusterCommunicationResourceProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class ConcreteComProps(CpSoftwareClusterCommunicationResourceProps):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadCpSoftwareClusterCommunicationResourceProps:
    def test_read_ar_object_level(self, parser):
        """
        The XSD CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE-PROPS group (AUTOSAR_00052.xsd l.24290)
        has an empty sequence and Table 11.9 declares no Attribute rows, so the helper owns the
        ARObject level of the concrete subclass element: the S checksum attribute is read.
        """
        element = ET.fromstring("<DATA-COM-PROPS xmlns='%s' S='21'></DATA-COM-PROPS>" % NS)

        props = parser.readCpSoftwareClusterCommunicationResourceProps(element, ConcreteComProps())

        assert props.getChecksum().getValue() == "21"

    def test_read_empty_element(self, parser):
        """
        A concrete subclass element without ARObject-level content leaves the state unset.
        """
        element = ET.fromstring("<CLIENT-SERVER-OPERATION-COM-PROPS xmlns='%s'></CLIENT-SERVER-OPERATION-COM-PROPS>" % NS)

        props = parser.readCpSoftwareClusterCommunicationResourceProps(element, ConcreteComProps())

        assert props.getChecksum() is None
        assert props.getTimestamp() is None
