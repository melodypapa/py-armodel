"""Reader tests for GlobalTimeCanMaster (Table 9.8, p.864)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeCanMaster
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


class TestReadGlobalTimeCanMaster:
    def test_read_all_elements(self, parser):
        """
        The two GLOBAL-TIME-CAN-MASTER group elements plus the Table 9.4 base group
        (via readGlobalTimeMaster: COMMUNICATION-CONNECTOR-REF ... SYNC-PERIOD, SHORT-NAME,
        UUID, VARIATION-POINT) are read into the object.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-CAN-MASTER xmlns='%s' UUID='5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f'>"
            "<SHORT-NAME>canMaster</SHORT-NAME>"
            "<COMMUNICATION-CONNECTOR-REF DEST='CAN-COMMUNICATION-CONNECTOR'>/Clusters/Cluster1/Connector1</COMMUNICATION-CONNECTOR-REF>"
            "<SYNC-PERIOD>0.2</SYNC-PERIOD>"
            "<CRC-SECURED>CRC-SUPPORTED</CRC-SECURED>"
            "<SYNC-CONFIRMATION-TIMEOUT>1.0</SYNC-CONFIRMATION-TIMEOUT>"
            "<VARIATION-POINT><SHORT-LABEL>vpCanMaster</SHORT-LABEL></VARIATION-POINT>"
            "</GLOBAL-TIME-CAN-MASTER>" % NS
        )

        master = parser.readGlobalTimeCanMaster(element, GlobalTimeCanMaster(None, "canMaster"))

        assert master.getShortName() == "canMaster"
        assert master.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert master.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector1"
        assert master.getSyncPeriod().getValue() == pytest.approx(0.2)
        assert master.getCrcSecured().getValue() == "CRC-SUPPORTED"
        assert master.getSyncConfirmationTimeout().getValue() == pytest.approx(1.0)
        assert master.getVariationPoint().getShortLabel().getValue() == "vpCanMaster"

    def test_read_empty_element(self, parser):
        """
        A GLOBAL-TIME-CAN-MASTER element without group content leaves the fields unset.
        """
        element = ET.fromstring("<GLOBAL-TIME-CAN-MASTER xmlns='%s'></GLOBAL-TIME-CAN-MASTER>" % NS)

        master = parser.readGlobalTimeCanMaster(element, GlobalTimeCanMaster(None, "canMaster"))

        assert master.getCrcSecured() is None
        assert master.getSyncConfirmationTimeout() is None
        assert master.getCommunicationConnectorRef() is None
        assert master.getVariationPoint() is None
