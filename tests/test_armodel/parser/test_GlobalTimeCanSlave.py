"""Reader tests for GlobalTimeCanSlave (Table 9.9, p.864)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeCanSlave
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


class TestReadGlobalTimeCanSlave:
    def test_read_all_elements(self, parser):
        """
        The two GLOBAL-TIME-CAN-SLAVE group elements plus the Table 9.5 base group (via
        readGlobalTimeSlave: COMMUNICATION-CONNECTOR-REF ... TIME-LEAP-PAST-THRESHOLD,
        SHORT-NAME, UUID, VARIATION-POINT) are read into the object.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-CAN-SLAVE xmlns='%s' UUID='6f7a8b9c-0d1e-4cdd-eeef-5b6c7d8e9f0a'>"
            "<SHORT-NAME>canSlave</SHORT-NAME>"
            "<COMMUNICATION-CONNECTOR-REF DEST='CAN-COMMUNICATION-CONNECTOR'>/Clusters/Cluster1/Connector2</COMMUNICATION-CONNECTOR-REF>"
            "<TIME-LEAP-HEALING-COUNTER>4</TIME-LEAP-HEALING-COUNTER>"
            "<CRC-VALIDATED>CRC-VALIDATED</CRC-VALIDATED>"
            "<SEQUENCE-COUNTER-JUMP-WIDTH>2</SEQUENCE-COUNTER-JUMP-WIDTH>"
            "<VARIATION-POINT><SHORT-LABEL>vpCanSlave</SHORT-LABEL></VARIATION-POINT>"
            "</GLOBAL-TIME-CAN-SLAVE>" % NS
        )

        slave = parser.readGlobalTimeCanSlave(element, GlobalTimeCanSlave(None, "canSlave"))

        assert slave.getShortName() == "canSlave"
        assert slave.getUuid().getValue() == "6f7a8b9c-0d1e-4cdd-eeef-5b6c7d8e9f0a"
        assert slave.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector2"
        assert slave.getTimeLeapHealingCounter().getValue() == 4
        assert slave.getCrcValidated().getValue() == "CRC-VALIDATED"
        assert slave.getSequenceCounterJumpWidth().getValue() == 2
        assert slave.getVariationPoint().getShortLabel().getValue() == "vpCanSlave"

    def test_read_empty_element(self, parser):
        """
        A GLOBAL-TIME-CAN-SLAVE element without group content leaves the fields unset.
        """
        element = ET.fromstring("<GLOBAL-TIME-CAN-SLAVE xmlns='%s'></GLOBAL-TIME-CAN-SLAVE>" % NS)

        slave = parser.readGlobalTimeCanSlave(element, GlobalTimeCanSlave(None, "canSlave"))

        assert slave.getCrcValidated() is None
        assert slave.getSequenceCounterJumpWidth() is None
        assert slave.getCommunicationConnectorRef() is None
        assert slave.getVariationPoint() is None
