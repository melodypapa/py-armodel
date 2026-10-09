"""Reader tests for GlobalTimeEthSlave (Table 9.13, p.867)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeEthSlave
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


class TestReadGlobalTimeEthSlave:
    def test_read_all_elements(self, parser):
        """
        The GLOBAL-TIME-ETH-SLAVE group element plus the Table 9.5 base group (via
        readGlobalTimeSlave: COMMUNICATION-CONNECTOR-REF ... TIME-LEAP-PAST-THRESHOLD,
        SHORT-NAME, UUID, VARIATION-POINT) are read into the object.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-ETH-SLAVE xmlns='%s' UUID='5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f'>"
            "<SHORT-NAME>ethSlave</SHORT-NAME>"
            "<COMMUNICATION-CONNECTOR-REF DEST='ETHERNET-COMMUNICATION-CONNECTOR'>/Clusters/Cluster1/Connector2</COMMUNICATION-CONNECTOR-REF>"
            "<FOLLOW-UP-TIMEOUT-VALUE>0.05</FOLLOW-UP-TIMEOUT-VALUE>"
            "<CRC-VALIDATED>CRC-VALIDATED</CRC-VALIDATED>"
            "<VARIATION-POINT><SHORT-LABEL>vpEthSlave</SHORT-LABEL></VARIATION-POINT>"
            "</GLOBAL-TIME-ETH-SLAVE>" % NS
        )

        slave = parser.readGlobalTimeEthSlave(element, GlobalTimeEthSlave(None, "ethSlave"))

        assert slave.getShortName() == "ethSlave"
        assert slave.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert slave.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector2"
        assert slave.getFollowUpTimeoutValue().getValue() == pytest.approx(0.05)
        assert slave.getCrcValidated().getValue() == "CRC-VALIDATED"
        assert slave.getVariationPoint().getShortLabel().getValue() == "vpEthSlave"

    def test_read_empty_element(self, parser):
        """
        A GLOBAL-TIME-ETH-SLAVE element without group content leaves the fields unset.
        """
        element = ET.fromstring("<GLOBAL-TIME-ETH-SLAVE xmlns='%s'></GLOBAL-TIME-ETH-SLAVE>" % NS)

        slave = parser.readGlobalTimeEthSlave(element, GlobalTimeEthSlave(None, "ethSlave"))

        assert slave.getCrcValidated() is None
        assert slave.getCommunicationConnectorRef() is None
        assert slave.getVariationPoint() is None
