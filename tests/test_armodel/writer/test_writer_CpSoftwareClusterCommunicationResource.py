"""Writer/reader round-trip tests for CpSoftwareClusterCommunicationResource (Table 11.8, p.902)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ClientServerOperationComProps,
    DataComProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CpSoftwareClusterCommunicationResource
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    DataConsistencyPolicyEnum,
    PositiveInteger,
    SendIndicationEnum,
    String,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


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


def _new_resource_with_data_com_props():
    resource = CpSoftwareClusterCommunicationResource(None, "commResource")
    resource.setUuid(String().setValue("1a2b3c4d-5e6f-4a7b-8c9d-0e1f2a3b4c5d"))
    resource.setGlobalResourceId(PositiveInteger().setValue(7))
    resource.setIsMandatory(Boolean().setValue(True))
    props = DataComProps()
    props.setDataConsistencyPolicy(DataConsistencyPolicyEnum().setValue(DataConsistencyPolicyEnum.CONSISTENCY_MECHANISM_REQUIRED))
    props.setSendIndication(SendIndicationEnum().setValue(SendIndicationEnum.ANY_SEND_OPERATION))
    resource.setCommunicationResourceProps(props)
    return resource


def _new_resource_with_client_server_operation_com_props():
    resource = CpSoftwareClusterCommunicationResource(None, "csResource")
    props = ClientServerOperationComProps()
    props.setQueueLength(PositiveInteger().setValue(8))
    resource.setCommunicationResourceProps(props)
    return resource


class TestWriteCpSoftwareClusterCommunicationResource:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the CpSoftwareClusterResource base group first (via
        writeCpSoftwareClusterResource) and then the own group's COMMUNICATION-RESOURCE-PROPS
        wrapper with the inner DATA-COM-PROPS choice element (AUTOSAR_00052.xsd l.24239);
        the atp.Status=removed COM-PROPS element is not written.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE")
        writer.writeCpSoftwareClusterCommunicationResource(element, _new_resource_with_data_com_props())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-1] == "COMMUNICATION-RESOURCE-PROPS"
        assert element.attrib["UUID"] == "1a2b3c4d-5e6f-4a7b-8c9d-0e1f2a3b4c5d"
        assert element.find("GLOBAL-RESOURCE-ID").text == "7"
        assert element.find("IS-MANDATORY").text == "true"
        assert element.find("COM-PROPS") is None
        props_element = element.find("COMMUNICATION-RESOURCE-PROPS")
        assert props_element.find("DATA-COM-PROPS").find("DATA-CONSISTENCY-POLICY").text == "CONSISTENCY-MECHANISM-REQUIRED"
        assert props_element.find("DATA-COM-PROPS").find("SEND-INDICATION").text == "ANY-SEND-OPERATION"

    def test_write_client_server_operation_com_props_choice(self, writer):
        """
        The wrapper's inner choice names CLIENT-SERVER-OPERATION-COM-PROPS for the
        ClientServerOperationComProps value.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE")
        writer.writeCpSoftwareClusterCommunicationResource(element, _new_resource_with_client_server_operation_com_props())

        props_element = element.find("COMMUNICATION-RESOURCE-PROPS")
        assert props_element.find("CLIENT-SERVER-OPERATION-COM-PROPS").find("QUEUE-LENGTH").text == "8"
        assert props_element.find("DATA-COM-PROPS") is None

    def test_write_empty_element(self, writer):
        """
        An unset resource emits no COMMUNICATION-RESOURCE-PROPS wrapper.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE")
        writer.writeCpSoftwareClusterCommunicationResource(element, CpSoftwareClusterCommunicationResource(None, "commResource"))

        assert element.find("COMMUNICATION-RESOURCE-PROPS") is None


class TestCpSoftwareClusterCommunicationResourceRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the aggregated
        DataComProps behind the inner-choice wrapper.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE")
        writer.writeCpSoftwareClusterCommunicationResource(element, _new_resource_with_data_com_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        resource = parser.readCpSoftwareClusterCommunicationResource(parsed_element, CpSoftwareClusterCommunicationResource(None, "commResource"))

        assert resource.getShortName() == "commResource"
        assert resource.getUuid().getValue() == "1a2b3c4d-5e6f-4a7b-8c9d-0e1f2a3b4c5d"
        assert resource.getGlobalResourceId().getValue() == 7
        assert resource.getIsMandatory().getValue() is True
        props = resource.getCommunicationResourceProps()
        assert isinstance(props, DataComProps)
        assert props.getDataConsistencyPolicy().getValue() == "CONSISTENCY-MECHANISM-REQUIRED"
        assert props.getSendIndication().getValue() == "ANY-SEND-OPERATION"

    def test_round_trip_empty_wrapper_list_case(self, writer, parser):
        """
        An empty wrapper case: unset optional group elements serialize to nothing and
        re-parse to None fields.
        """
        element = ET.Element("CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE")
        writer.writeCpSoftwareClusterCommunicationResource(element, CpSoftwareClusterCommunicationResource(None, "commResource"))
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        resource = parser.readCpSoftwareClusterCommunicationResource(parsed_element, CpSoftwareClusterCommunicationResource(None, "commResource"))

        assert resource.getCommunicationResourceProps() is None
