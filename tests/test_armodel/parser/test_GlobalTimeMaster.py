"""Reader tests for the GlobalTimeMaster reusable helper (Table 9.4, p.860)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeMaster
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class ConcreteGlobalTimeMaster(GlobalTimeMaster):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadGlobalTimeMaster:
    def test_read_all_elements(self, parser):
        """
        All five GLOBAL-TIME-MASTER group elements plus the Identifiable level (SHORT-NAME, UUID)
        and the trailing VARIATION-POINT are read into the object.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-CAN-MASTER xmlns='%s' UUID='3c4d5e6f-7a8b-49aa-bbbc-2e3f4a5b6c7d'>"
            "<SHORT-NAME>master1</SHORT-NAME>"
            "<COMMUNICATION-CONNECTOR-REF DEST='CAN-COMMUNICATION-CONNECTOR'>/Clusters/Cluster1/Connector1</COMMUNICATION-CONNECTOR-REF>"
            "<ICV-SECURED>ICV-SUPPORTED</ICV-SECURED>"
            "<IMMEDIATE-RESUME-TIME>2.0</IMMEDIATE-RESUME-TIME>"
            "<IS-SYSTEM-WIDE-GLOBAL-TIME-MASTER>true</IS-SYSTEM-WIDE-GLOBAL-TIME-MASTER>"
            "<SYNC-PERIOD>0.2</SYNC-PERIOD>"
            "<VARIATION-POINT><SHORT-LABEL>vpMaster</SHORT-LABEL></VARIATION-POINT>"
            "</GLOBAL-TIME-CAN-MASTER>" % NS
        )

        master = parser.readGlobalTimeMaster(element, ConcreteGlobalTimeMaster(None, "master1"))

        assert master.getShortName() == "master1"
        assert master.getUuid().getValue() == "3c4d5e6f-7a8b-49aa-bbbc-2e3f4a5b6c7d"
        assert master.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector1"
        assert master.getCommunicationConnectorRef().getDest() == "CAN-COMMUNICATION-CONNECTOR"
        assert master.getIcvSecured().getValue() == "ICV-SUPPORTED"
        assert master.getImmediateResumeTime().getValue() == pytest.approx(2.0)
        assert master.getIsSystemWideGlobalTimeMaster().getValue() is True
        assert master.getSyncPeriod().getValue() == pytest.approx(0.2)
        assert master.getVariationPoint().getShortLabel().getValue() == "vpMaster"

    def test_read_empty_element(self, parser):
        """
        A concrete subclass element without group content leaves the fields unset.
        """
        element = ET.fromstring("<USER-DEFINED-GLOBAL-TIME-MASTER xmlns='%s'></USER-DEFINED-GLOBAL-TIME-MASTER>" % NS)

        master = parser.readGlobalTimeMaster(element, ConcreteGlobalTimeMaster(None, "master2"))

        assert master.getCommunicationConnectorRef() is None
        assert master.getIcvSecured() is None
        assert master.getImmediateResumeTime() is None
        assert master.getIsSystemWideGlobalTimeMaster() is None
        assert master.getSyncPeriod() is None
        assert master.getVariationPoint() is None
