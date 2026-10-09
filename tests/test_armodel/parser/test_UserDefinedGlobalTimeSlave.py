"""Reader tests for UserDefinedGlobalTimeSlave (Table 9.24, p.879)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import UserDefinedGlobalTimeSlave
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


class TestReadUserDefinedGlobalTimeSlave:
    def test_read_base_group_elements(self, parser):
        """
        The Table 9.5 base group (via readGlobalTimeSlave: COMMUNICATION-CONNECTOR-REF ...
        TIME-LEAP-PAST-THRESHOLD, SHORT-NAME, UUID, VARIATION-POINT) is read into the object;
        the XSD USER-DEFINED-GLOBAL-TIME-SLAVE group has an empty sequence, so the helper owns
        only the base level.
        """
        element = ET.fromstring(
            "<USER-DEFINED-GLOBAL-TIME-SLAVE xmlns='%s' UUID='5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f'>"
            "<SHORT-NAME>userDefinedSlave</SHORT-NAME>"
            "<COMMUNICATION-CONNECTOR-REF DEST='COMMUNICATION-CONNECTOR'>/Clusters/Cluster1/Connector6</COMMUNICATION-CONNECTOR-REF>"
            "<FOLLOW-UP-TIMEOUT-VALUE>0.05</FOLLOW-UP-TIMEOUT-VALUE>"
            "<VARIATION-POINT><SHORT-LABEL>vpUdSlave</SHORT-LABEL></VARIATION-POINT>"
            "</USER-DEFINED-GLOBAL-TIME-SLAVE>" % NS
        )

        slave = parser.readUserDefinedGlobalTimeSlave(element, UserDefinedGlobalTimeSlave(None, "userDefinedSlave"))

        assert slave.getShortName() == "userDefinedSlave"
        assert slave.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert slave.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector6"
        assert slave.getFollowUpTimeoutValue().getValue() == pytest.approx(0.05)
        assert slave.getVariationPoint().getShortLabel().getValue() == "vpUdSlave"

    def test_read_empty_element(self, parser):
        """
        A USER-DEFINED-GLOBAL-TIME-SLAVE element without group content leaves the fields unset.
        """
        element = ET.fromstring("<USER-DEFINED-GLOBAL-TIME-SLAVE xmlns='%s'></USER-DEFINED-GLOBAL-TIME-SLAVE>" % NS)

        slave = parser.readUserDefinedGlobalTimeSlave(element, UserDefinedGlobalTimeSlave(None, "userDefinedSlave"))

        assert slave.getCommunicationConnectorRef() is None
        assert slave.getFollowUpTimeoutValue() is None
        assert slave.getVariationPoint() is None
