"""Reader tests for UserDefinedGlobalTimeMaster (Table 9.23, p.879)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import UserDefinedGlobalTimeMaster
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


class TestReadUserDefinedGlobalTimeMaster:
    def test_read_base_group_elements(self, parser):
        """
        The Table 9.4 base group (via readGlobalTimeMaster: COMMUNICATION-CONNECTOR-REF ...
        SYNC-PERIOD, SHORT-NAME, UUID, VARIATION-POINT) is read into the object; the XSD
        USER-DEFINED-GLOBAL-TIME-MASTER group has an empty sequence, so the helper owns only
        the base level.
        """
        element = ET.fromstring(
            "<USER-DEFINED-GLOBAL-TIME-MASTER xmlns='%s' UUID='5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f'>"
            "<SHORT-NAME>userDefinedMaster</SHORT-NAME>"
            "<COMMUNICATION-CONNECTOR-REF DEST='COMMUNICATION-CONNECTOR'>/Clusters/Cluster1/Connector5</COMMUNICATION-CONNECTOR-REF>"
            "<SYNC-PERIOD>0.2</SYNC-PERIOD>"
            "<VARIATION-POINT><SHORT-LABEL>vpUdMaster</SHORT-LABEL></VARIATION-POINT>"
            "</USER-DEFINED-GLOBAL-TIME-MASTER>" % NS
        )

        master = parser.readUserDefinedGlobalTimeMaster(element, UserDefinedGlobalTimeMaster(None, "userDefinedMaster"))

        assert master.getShortName() == "userDefinedMaster"
        assert master.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert master.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector5"
        assert master.getSyncPeriod().getValue() == pytest.approx(0.2)
        assert master.getVariationPoint().getShortLabel().getValue() == "vpUdMaster"

    def test_read_empty_element(self, parser):
        """
        A USER-DEFINED-GLOBAL-TIME-MASTER element without group content leaves the fields unset.
        """
        element = ET.fromstring("<USER-DEFINED-GLOBAL-TIME-MASTER xmlns='%s'></USER-DEFINED-GLOBAL-TIME-MASTER>" % NS)

        master = parser.readUserDefinedGlobalTimeMaster(element, UserDefinedGlobalTimeMaster(None, "userDefinedMaster"))

        assert master.getCommunicationConnectorRef() is None
        assert master.getSyncPeriod() is None
        assert master.getVariationPoint() is None
