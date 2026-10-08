"""Writer/reader round-trip tests for the GlobalTimeMaster reusable helper (Table 9.4, p.860)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeMaster
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    GlobalTimeIcvSupportEnum,
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class ConcreteGlobalTimeMaster(GlobalTimeMaster):
    pass


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


def _new_master():
    master = ConcreteGlobalTimeMaster(None, "master1")
    master.setUuid(String().setValue("3c4d5e6f-7a8b-49aa-bbbc-2e3f4a5b6c7d"))
    ref = RefType()
    ref.setValue("/Clusters/Cluster1/Connector1")
    ref.setDest("CAN-COMMUNICATION-CONNECTOR")
    master.setCommunicationConnectorRef(ref)
    master.setIcvSecured(GlobalTimeIcvSupportEnum().setValue(GlobalTimeIcvSupportEnum.ICV_SUPPORTED))
    master.setImmediateResumeTime(TimeValue().setValue("2.0"))
    master.setIsSystemWideGlobalTimeMaster(Boolean().setValue(True))
    master.setSyncPeriod(TimeValue().setValue("0.2"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(String().setValue("vpMaster"))
    master.setVariationPoint(variation_point)
    return master


class TestWriteGlobalTimeMaster:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the Identifiable level, the five group elements in the XSD
        sequenceOffset order and the VARIATION-POINT tail last.
        """
        element = ET.Element("GLOBAL-TIME-CAN-MASTER")
        writer.writeGlobalTimeMaster(element, _new_master())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-1] == "VARIATION-POINT"
        assert tags[-6:] == [
            "COMMUNICATION-CONNECTOR-REF",
            "ICV-SECURED",
            "IMMEDIATE-RESUME-TIME",
            "IS-SYSTEM-WIDE-GLOBAL-TIME-MASTER",
            "SYNC-PERIOD",
            "VARIATION-POINT",
        ]
        assert element.attrib["UUID"] == "3c4d5e6f-7a8b-49aa-bbbc-2e3f4a5b6c7d"
        assert element.find("COMMUNICATION-CONNECTOR-REF").text == "/Clusters/Cluster1/Connector1"
        assert element.find("COMMUNICATION-CONNECTOR-REF").attrib["DEST"] == "CAN-COMMUNICATION-CONNECTOR"
        assert element.find("ICV-SECURED").text == "ICV-SUPPORTED"
        assert element.find("IMMEDIATE-RESUME-TIME").text == "2.0"
        assert element.find("IS-SYSTEM-WIDE-GLOBAL-TIME-MASTER").text == "true"
        assert element.find("SYNC-PERIOD").text == "0.2"
        assert element.find("VARIATION-POINT").find("SHORT-LABEL").text == "vpMaster"

    def test_write_empty_element(self, writer):
        """
        An unset master emits no group content beyond the SHORT-NAME and no VARIATION-POINT.
        """
        element = ET.Element("USER-DEFINED-GLOBAL-TIME-MASTER")
        writer.writeGlobalTimeMaster(element, ConcreteGlobalTimeMaster(None, "master2"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("VARIATION-POINT") is None


class TestGlobalTimeMasterRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the variation point.
        """
        element = ET.Element("GLOBAL-TIME-CAN-MASTER")
        writer.writeGlobalTimeMaster(element, _new_master())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        master = parser.readGlobalTimeMaster(parsed_element, ConcreteGlobalTimeMaster(None, "master1"))

        assert master.getShortName() == "master1"
        assert master.getUuid().getValue() == "3c4d5e6f-7a8b-49aa-bbbc-2e3f4a5b6c7d"
        assert master.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector1"
        assert master.getCommunicationConnectorRef().getDest() == "CAN-COMMUNICATION-CONNECTOR"
        assert master.getIcvSecured().getValue() == "ICV-SUPPORTED"
        assert master.getImmediateResumeTime().getValue() == pytest.approx(2.0)
        assert master.getIsSystemWideGlobalTimeMaster().getValue() is True
        assert master.getSyncPeriod().getValue() == pytest.approx(0.2)
        assert master.getVariationPoint().getShortLabel().getValue() == "vpMaster"
