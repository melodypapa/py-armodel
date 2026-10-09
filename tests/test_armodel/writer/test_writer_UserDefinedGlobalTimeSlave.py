"""Writer/reader round-trip tests for UserDefinedGlobalTimeSlave (Table 9.24, p.879)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import UserDefinedGlobalTimeSlave
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


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


def _new_slave():
    slave = UserDefinedGlobalTimeSlave(None, "userDefinedSlave")
    slave.setUuid(String().setValue("5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"))
    ref = RefType()
    ref.setValue("/Clusters/Cluster1/Connector6")
    ref.setDest("COMMUNICATION-CONNECTOR")
    slave.setCommunicationConnectorRef(ref)
    slave.setFollowUpTimeoutValue(TimeValue().setValue("0.05"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(String().setValue("vpUdSlave"))
    slave.setVariationPoint(variation_point)
    return slave


class TestWriteUserDefinedGlobalTimeSlave:
    def test_write_base_group_elements(self, writer):
        """
        The helper writes the Table 9.5 base group ending in its VARIATION-POINT; the XSD
        USER-DEFINED-GLOBAL-TIME-SLAVE group (AUTOSAR_00052.xsd l.128845) has an empty
        sequence, so the helper owns only the base level reached through
        writeGlobalTimeSlave.
        """
        element = ET.Element("USER-DEFINED-GLOBAL-TIME-SLAVE")
        writer.writeUserDefinedGlobalTimeSlave(element, _new_slave())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-1] == "VARIATION-POINT"
        assert element.attrib["UUID"] == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert element.find("COMMUNICATION-CONNECTOR-REF").text == "/Clusters/Cluster1/Connector6"
        assert element.find("FOLLOW-UP-TIMEOUT-VALUE").text == "0.05"
        assert element.find("VARIATION-POINT").find("SHORT-LABEL").text == "vpUdSlave"

    def test_write_empty_element(self, writer):
        """
        An unset slave emits no group content beyond the SHORT-NAME and no VARIATION-POINT.
        """
        element = ET.Element("USER-DEFINED-GLOBAL-TIME-SLAVE")
        writer.writeUserDefinedGlobalTimeSlave(element, UserDefinedGlobalTimeSlave(None, "userDefinedSlave"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("VARIATION-POINT") is None


class TestUserDefinedGlobalTimeSlaveRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every inherited base group field value.
        """
        element = ET.Element("USER-DEFINED-GLOBAL-TIME-SLAVE")
        writer.writeUserDefinedGlobalTimeSlave(element, _new_slave())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        slave = parser.readUserDefinedGlobalTimeSlave(parsed_element, UserDefinedGlobalTimeSlave(None, "userDefinedSlave"))

        assert slave.getShortName() == "userDefinedSlave"
        assert slave.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert slave.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector6"
        assert slave.getFollowUpTimeoutValue().getValue() == pytest.approx(0.05)
        assert slave.getVariationPoint().getShortLabel().getValue() == "vpUdSlave"
