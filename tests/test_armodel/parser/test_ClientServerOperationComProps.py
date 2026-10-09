"""Reader tests for ClientServerOperationComProps (Table 11.12, p.903)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ClientServerOperationComProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadClientServerOperationComProps:
    def test_read_queue_length_and_ar_object_level(self, parser):
        """
        The Table 11.12 queueLength attribute is read from the CLIENT-SERVER-OPERATION-COM-PROPS
        element and the inherited CpSoftwareClusterCommunicationResourceProps helper reads the
        ARObject S attribute.
        """
        element = ET.fromstring("<CLIENT-SERVER-OPERATION-COM-PROPS xmlns='%s' S='41'>" "<QUEUE-LENGTH>3</QUEUE-LENGTH>" "</CLIENT-SERVER-OPERATION-COM-PROPS>" % NS)

        props = ClientServerOperationComProps()
        parser.readClientServerOperationComProps(element, props)

        assert props.getChecksum().getValue() == "41"
        assert props.getQueueLength().getValue() == 3

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset.
        """
        element = ET.fromstring("<CLIENT-SERVER-OPERATION-COM-PROPS xmlns='%s'></CLIENT-SERVER-OPERATION-COM-PROPS>" % NS)

        props = ClientServerOperationComProps()
        parser.readClientServerOperationComProps(element, props)

        assert props.getChecksum() is None
        assert props.getQueueLength() is None
