"""Reader tests for DataComProps (Table 11.10, p.903)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DataComProps
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


class TestReadDataComProps:
    def test_read_enum_elements_and_ar_object_level(self, parser):
        """
        The two Table 11.10 enum attributes are read from the DATA-COM-PROPS element and the
        inherited CpSoftwareClusterCommunicationResourceProps helper reads the ARObject S attribute.
        """
        element = ET.fromstring(
            "<DATA-COM-PROPS xmlns='%s' S='31'>"
            "<DATA-CONSISTENCY-POLICY>CONSISTENCY-MECHANISM-REQUIRED</DATA-CONSISTENCY-POLICY>"
            "<SEND-INDICATION>ANY-SEND-OPERATION</SEND-INDICATION>"
            "</DATA-COM-PROPS>" % NS
        )

        props = DataComProps()
        parser.readDataComProps(element, props)

        assert props.getChecksum().getValue() == "31"
        assert props.getDataConsistencyPolicy().getValue() == "CONSISTENCY-MECHANISM-REQUIRED"
        assert props.getSendIndication().getValue() == "ANY-SEND-OPERATION"

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset.
        """
        element = ET.fromstring("<DATA-COM-PROPS xmlns='%s'></DATA-COM-PROPS>" % NS)

        props = DataComProps()
        parser.readDataComProps(element, props)

        assert props.getChecksum() is None
        assert props.getDataConsistencyPolicy() is None
        assert props.getSendIndication() is None
