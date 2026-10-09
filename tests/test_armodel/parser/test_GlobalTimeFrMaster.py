"""Reader tests for GlobalTimeFrMaster (Table 9.20, p.877)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeFrMaster
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


class TestReadGlobalTimeFrMaster:
    def test_read_all_elements(self, parser):
        """
        The GLOBAL-TIME-FR-MASTER group element plus the Table 9.4 base group (via
        readGlobalTimeMaster: COMMUNICATION-CONNECTOR-REF ... SYNC-PERIOD, SHORT-NAME,
        UUID, VARIATION-POINT) are read into the object.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-FR-MASTER xmlns='%s' UUID='5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f'>"
            "<SHORT-NAME>frMaster</SHORT-NAME>"
            "<COMMUNICATION-CONNECTOR-REF DEST='FLEXRAY-COMMUNICATION-CONNECTOR'>/Clusters/Cluster1/Connector3</COMMUNICATION-CONNECTOR-REF>"
            "<SYNC-PERIOD>0.2</SYNC-PERIOD>"
            "<CRC-SECURED>CRC-SUPPORTED</CRC-SECURED>"
            "<VARIATION-POINT><SHORT-LABEL>vpFrMaster</SHORT-LABEL></VARIATION-POINT>"
            "</GLOBAL-TIME-FR-MASTER>" % NS
        )

        master = parser.readGlobalTimeFrMaster(element, GlobalTimeFrMaster(None, "frMaster"))

        assert master.getShortName() == "frMaster"
        assert master.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert master.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector3"
        assert master.getSyncPeriod().getValue() == pytest.approx(0.2)
        assert master.getCrcSecured().getValue() == "CRC-SUPPORTED"
        assert master.getVariationPoint().getShortLabel().getValue() == "vpFrMaster"

    def test_read_empty_element(self, parser):
        """
        A GLOBAL-TIME-FR-MASTER element without group content leaves the fields unset.
        """
        element = ET.fromstring("<GLOBAL-TIME-FR-MASTER xmlns='%s'></GLOBAL-TIME-FR-MASTER>" % NS)

        master = parser.readGlobalTimeFrMaster(element, GlobalTimeFrMaster(None, "frMaster"))

        assert master.getCrcSecured() is None
        assert master.getCommunicationConnectorRef() is None
        assert master.getVariationPoint() is None
