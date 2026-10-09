"""Reader tests for GlobalTimeFrSlave (Table 9.21, p.878)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeFrSlave
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


class TestReadGlobalTimeFrSlave:
    def test_read_all_elements(self, parser):
        """
        The two GLOBAL-TIME-FR-SLAVE group elements plus the Table 9.5 base group (via
        readGlobalTimeSlave: COMMUNICATION-CONNECTOR-REF ... TIME-LEAP-PAST-THRESHOLD,
        SHORT-NAME, UUID, VARIATION-POINT) are read into the object.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-FR-SLAVE xmlns='%s' UUID='5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f'>"
            "<SHORT-NAME>frSlave</SHORT-NAME>"
            "<COMMUNICATION-CONNECTOR-REF DEST='FLEXRAY-COMMUNICATION-CONNECTOR'>/Clusters/Cluster1/Connector4</COMMUNICATION-CONNECTOR-REF>"
            "<TIME-LEAP-PAST-THRESHOLD>0.4</TIME-LEAP-PAST-THRESHOLD>"
            "<CRC-VALIDATED>CRC-VALIDATED</CRC-VALIDATED>"
            "<SEQUENCE-COUNTER-JUMP-WIDTH>2</SEQUENCE-COUNTER-JUMP-WIDTH>"
            "<VARIATION-POINT><SHORT-LABEL>vpFrSlave</SHORT-LABEL></VARIATION-POINT>"
            "</GLOBAL-TIME-FR-SLAVE>" % NS
        )

        slave = parser.readGlobalTimeFrSlave(element, GlobalTimeFrSlave(None, "frSlave"))

        assert slave.getShortName() == "frSlave"
        assert slave.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert slave.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector4"
        assert slave.getTimeLeapPastThreshold().getValue() == pytest.approx(0.4)
        assert slave.getCrcValidated().getValue() == "CRC-VALIDATED"
        assert slave.getSequenceCounterJumpWidth().getValue() == 2
        assert slave.getVariationPoint().getShortLabel().getValue() == "vpFrSlave"

    def test_read_empty_element(self, parser):
        """
        A GLOBAL-TIME-FR-SLAVE element without group content leaves the fields unset.
        """
        element = ET.fromstring("<GLOBAL-TIME-FR-SLAVE xmlns='%s'></GLOBAL-TIME-FR-SLAVE>" % NS)

        slave = parser.readGlobalTimeFrSlave(element, GlobalTimeFrSlave(None, "frSlave"))

        assert slave.getCrcValidated() is None
        assert slave.getSequenceCounterJumpWidth() is None
        assert slave.getCommunicationConnectorRef() is None
        assert slave.getVariationPoint() is None
