"""Writer/reader round-trip tests for EthernetPriorityRegeneration (Table 3.74, p.128)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingPortDetails
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _details_with_regen():
    details = CouplingPortDetails()
    regen = details.createEthernetPriorityRegeneration("Regen1")
    regen.setIngressPriority(_pos_int("3"))
    regen.setRegeneratedPriority(_pos_int("7"))
    checksum = String()
    checksum.setValue("0x1")
    regen.setChecksum(checksum)
    timestamp = DateTime()
    timestamp.setValue("2024-01-01T00:00:00Z")
    regen.setTimestamp(timestamp)
    return details


def _reparse(writer, parser, details):
    parent = ET.Element("PARENT")
    writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
    return parser.getCouplingPortDetails(root[0], "COUPLING-PORT-DETAILS")


class TestEthernetPriorityRegenerationWriter:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", _details_with_regen())
        node = parent.find("COUPLING-PORT-DETAILS/ETHERNET-PRIORITY-REGENERATIONS/ETHERNET-PRIORITY-REGENERATION")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Regen1"
        assert node.find("INGRESS-PRIORITY").text == "3"
        assert node.find("REGENERATED-PRIORITY").text == "7"
        assert node.attrib["S"] == "0x1"
        assert node.attrib["T"] == "2024-01-01T00:00:00Z"


class TestEthernetPriorityRegenerationRoundTrip:
    def test_round_trip_preserves_values_short_name_and_arobject(self, writer, parser):
        parsed = _reparse(writer, parser, _details_with_regen())
        regens = parsed.getEthernetPriorityRegenerations()
        assert len(regens) == 1
        assert regens[0].getShortName() == "Regen1"
        assert regens[0].getIngressPriority().getValue() == 3
        assert regens[0].getRegeneratedPriority().getValue() == 7
        assert regens[0].getChecksum().getValue() == "0x1"
        assert regens[0].getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_round_trip_absent_optional_and_no_regenerations(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", CouplingPortDetails())
        assert parent.find("COUPLING-PORT-DETAILS/ETHERNET-PRIORITY-REGENERATIONS") is None
        parsed = _reparse(writer, parser, CouplingPortDetails())
        assert parsed.getEthernetPriorityRegenerations() == []

    def test_round_trip_empty_optional_fields(self, writer, parser):
        details = CouplingPortDetails()
        details.createEthernetPriorityRegeneration("Regen1")
        parsed = _reparse(writer, parser, details)
        regens = parsed.getEthernetPriorityRegenerations()
        assert len(regens) == 1
        assert regens[0].getIngressPriority() is None
        assert regens[0].getRegeneratedPriority() is None
