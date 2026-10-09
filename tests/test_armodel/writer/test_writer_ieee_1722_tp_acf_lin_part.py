"""Tests for the writeIEEE1722TpAcfLinPart handler (R23-11 IEEE1722TpAcfLinPart, Table 6.297, p.667)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfBus,
    IEEE1722TpAcfLinPart,
)
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


def _parent():
    return ET.Element("PARENT")


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _sdu_ref():
    ref = RefType()
    ref.setDest("PDU-TRIGGERING-REF")
    ref.setValue("/Pkg/PduTriggering")
    return ref


def _fill_part(part: IEEE1722TpAcfLinPart) -> IEEE1722TpAcfLinPart:
    part.setLinIdentifier(_pos_int(17))
    part.setSduRef(_sdu_ref())
    return part


class TestWriteIEEE1722TpAcfLinPart:
    """Tests for writeIEEE1722TpAcfLinPart handler (R23-11 IEEE1722TpAcfLinPart, Table 6.297, p.667)."""

    def test_children_in_xsd_order(self, writer):
        part = _fill_part(IEEE1722TpAcfLinPart(None, "LinPart1"))

        parent = _parent()
        writer.writeIEEE1722TpAcfLinPart(parent, part)
        child = parent.find("IEEE-1722-TP-ACF-LIN-PART")
        child_tags = [element.tag for element in child]
        assert child_tags == ["SHORT-NAME", "LIN-IDENTIFIER", "SDU-REF"]

    def test_field_values_in_xml(self, writer):
        part = _fill_part(IEEE1722TpAcfLinPart(None, "LinPart1"))

        parent = _parent()
        writer.writeIEEE1722TpAcfLinPart(parent, part)
        child = parent.find("IEEE-1722-TP-ACF-LIN-PART")
        assert child.find("LIN-IDENTIFIER").text == "17"
        sdu_ref = child.find("SDU-REF")
        assert sdu_ref.text == "/Pkg/PduTriggering"
        assert sdu_ref.attrib["DEST"] == "PDU-TRIGGERING-REF"

    def test_empty_part_writes_only_short_name(self, writer):
        part = IEEE1722TpAcfLinPart(None, "LinPart1")

        parent = _parent()
        writer.writeIEEE1722TpAcfLinPart(parent, part)
        child = parent.find("IEEE-1722-TP-ACF-LIN-PART")
        assert [element.tag for element in child] == ["SHORT-NAME"]
        assert child.find("LIN-IDENTIFIER") is None
        assert child.find("SDU-REF") is None

    def test_round_trip(self, writer, parser):
        part = _fill_part(IEEE1722TpAcfLinPart(None, "LinPart1"))

        parent = _parent()
        writer.writeIEEE1722TpAcfLinPart(parent, part)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpAcfLinPart(None, "LinPart1")
        parser.readIEEE1722TpAcfLinPart(element, reloaded)
        assert reloaded.getLinIdentifier().getValue() == 17
        assert reloaded.getSduRef().getValue() == "/Pkg/PduTriggering"
        assert reloaded.getSduRef().getDest() == "PDU-TRIGGERING-REF"

    def test_round_trip_via_acf_bus_dispatch(self, writer, parser):
        class _Bus(IEEE1722TpAcfBus):
            pass

        bus = _Bus(None, "LinBus")
        part = bus.createIEEE1722TpAcfLinPart("LinPart1")
        part.setLinIdentifier(_pos_int(63))
        part.setSduRef(_sdu_ref())
        bus.setBusId(_pos_int(5))

        parent = _parent()
        writer.writeIEEE1722TpAcfBus(parent, bus)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = _Bus(None, "LinBus")
        parser.readIEEE1722TpAcfBus(element, reloaded)
        parts = reloaded.getAcfParts()
        assert len(parts) == 1
        assert isinstance(parts[0], IEEE1722TpAcfLinPart)
        assert parts[0].getLinIdentifier().getValue() == 63
        assert parts[0].getSduRef().getValue() == "/Pkg/PduTriggering"
        assert reloaded.getBusId().getValue() == 5
