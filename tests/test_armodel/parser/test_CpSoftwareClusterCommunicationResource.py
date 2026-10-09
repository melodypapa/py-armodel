"""Reader tests for CpSoftwareClusterCommunicationResource (Table 11.8, p.902)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ClientServerOperationComProps,
    DataComProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CpSoftwareClusterCommunicationResource
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


class TestReadCpSoftwareClusterCommunicationResource:
    def test_read_data_com_props(self, parser):
        """
        The base CpSoftwareClusterResource group (via readCpSoftwareClusterResource:
        SHORT-NAME, UUID, DEPENDENT-RESOURCE-SS, GLOBAL-RESOURCE-ID, IS-MANDATORY) is read
        into the object and the COMMUNICATION-RESOURCE-PROPS wrapper's inner DATA-COM-PROPS
        choice dispatches to readDataComProps.
        """
        element = ET.fromstring(
            "<CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE xmlns='%s' UUID='1a2b3c4d-5e6f-4a7b-8c9d-0e1f2a3b4c5d'>"
            "<SHORT-NAME>commResource</SHORT-NAME>"
            "<GLOBAL-RESOURCE-ID>7</GLOBAL-RESOURCE-ID>"
            "<IS-MANDATORY>true</IS-MANDATORY>"
            "<COMMUNICATION-RESOURCE-PROPS>"
            "<DATA-COM-PROPS>"
            "<DATA-CONSISTENCY-POLICY>CONSISTENCY-MECHANISM-REQUIRED</DATA-CONSISTENCY-POLICY>"
            "<SEND-INDICATION>SEND-INDICATION-ON</SEND-INDICATION>"
            "</DATA-COM-PROPS>"
            "</COMMUNICATION-RESOURCE-PROPS>"
            "</CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE>" % NS
        )

        resource = parser.readCpSoftwareClusterCommunicationResource(element, CpSoftwareClusterCommunicationResource(None, "commResource"))

        assert resource.getShortName() == "commResource"
        assert resource.getGlobalResourceId().getValue() == 7
        assert resource.getIsMandatory().getValue() is True
        props = resource.getCommunicationResourceProps()
        assert isinstance(props, DataComProps)
        assert props.getDataConsistencyPolicy().getValue() == "CONSISTENCY-MECHANISM-REQUIRED"
        assert props.getSendIndication().getValue() == "SEND-INDICATION-ON"

    def test_read_client_server_operation_com_props(self, parser):
        """
        The COMMUNICATION-RESOURCE-PROPS wrapper's inner CLIENT-SERVER-OPERATION-COM-PROPS
        choice dispatches to readClientServerOperationComProps.
        """
        element = ET.fromstring(
            "<CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE xmlns='%s'>"
            "<SHORT-NAME>csResource</SHORT-NAME>"
            "<COMMUNICATION-RESOURCE-PROPS>"
            "<CLIENT-SERVER-OPERATION-COM-PROPS>"
            "<QUEUE-LENGTH>8</QUEUE-LENGTH>"
            "</CLIENT-SERVER-OPERATION-COM-PROPS>"
            "</COMMUNICATION-RESOURCE-PROPS>"
            "</CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE>" % NS
        )

        resource = parser.readCpSoftwareClusterCommunicationResource(element, CpSoftwareClusterCommunicationResource(None, "csResource"))

        props = resource.getCommunicationResourceProps()
        assert isinstance(props, ClientServerOperationComProps)
        assert props.getQueueLength().getValue() == 8

    def test_read_empty_element(self, parser):
        """
        A CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE element without group content leaves
        the fields unset.
        """
        element = ET.fromstring("<CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE xmlns='%s'></CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE>" % NS)

        resource = parser.readCpSoftwareClusterCommunicationResource(element, CpSoftwareClusterCommunicationResource(None, "commResource"))

        assert resource.getGlobalResourceId() is None
        assert resource.getIsMandatory() is None
        assert resource.getCommunicationResourceProps() is None

    def test_read_removed_com_props_is_ignored(self, parser):
        """
        COM-PROPS carries atp.Status=\"removed\" and has no Table 11.8 Attribute row
        (Rule 0015) — its presence on the wire does not populate any field.
        """
        element = ET.fromstring(
            "<CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE xmlns='%s'>"
            "<SHORT-NAME>commResource</SHORT-NAME>"
            "<COM-PROPS>"
            "<DATA-CONSISTENCY-POLICY>CONSISTENCY-MECHANISM-REQUIRED</DATA-CONSISTENCY-POLICY>"
            "</COM-PROPS>"
            "</CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE>" % NS
        )

        resource = parser.readCpSoftwareClusterCommunicationResource(element, CpSoftwareClusterCommunicationResource(None, "commResource"))

        assert resource.getCommunicationResourceProps() is None
