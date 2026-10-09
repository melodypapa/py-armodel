"""Tests for the writeIEEE1722TpAcfBusPart handler (R23-11 IEEE1722TpAcfBusPart, Table 6.292, p.658)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import PduCollectionTriggerEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import IEEE1722TpAcfCanPart
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


def _trigger(value):
    trigger = PduCollectionTriggerEnum()
    trigger.setValue(value)
    return trigger


class TestWriteIEEE1722TpAcfBusPart:
    """Tests for writeIEEE1722TpAcfBusPart handler (R23-11 IEEE1722TpAcfBusPart, Table 6.292, p.658)."""

    def test_children_in_xsd_order(self, writer):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        part.setCollectionTrigger(_trigger(PduCollectionTriggerEnum.ALWAYS))

        parent = ET.Element("PARENT")
        writer.writeIEEE1722TpAcfCanPart(parent, part)
        child = parent.find("IEEE-1722-TP-ACF-CAN-PART")
        assert child is not None
        assert [element.tag for element in child] == ["SHORT-NAME", "COLLECTION-TRIGGER"]

    def test_empty_part_writes_only_short_name(self, writer):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")

        parent = ET.Element("PARENT")
        writer.writeIEEE1722TpAcfCanPart(parent, part)
        child = parent.find("IEEE-1722-TP-ACF-CAN-PART")
        assert child is not None
        assert [element.tag for element in child] == ["SHORT-NAME"]

    def test_variation_point_written_last(self, writer):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        part.setCollectionTrigger(_trigger(PduCollectionTriggerEnum.NEVER))
        part.setVariationPoint(VariationPoint())

        parent = ET.Element("PARENT")
        writer.writeIEEE1722TpAcfCanPart(parent, part)
        child = parent.find("IEEE-1722-TP-ACF-CAN-PART")
        assert [element.tag for element in child] == ["SHORT-NAME", "COLLECTION-TRIGGER", "VARIATION-POINT"]
        assert len(child.findall("VARIATION-POINT")) == 1

    def test_round_trip(self, writer, parser):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        part.setCollectionTrigger(_trigger(PduCollectionTriggerEnum.ALWAYS))

        parent = ET.Element("PARENT")
        writer.writeIEEE1722TpAcfCanPart(parent, part)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpAcfCanPart(None, "CanPart1")
        parser.readIEEE1722TpAcfCanPart(element, reloaded)
        assert reloaded.getShortName() == "CanPart1"
        assert reloaded.getCollectionTrigger() is not None
        assert reloaded.getCollectionTrigger().getValue() == PduCollectionTriggerEnum.ALWAYS

    def test_bus_level_round_trip_with_parts(self, writer, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import IEEE1722TpAcfBus

        class _Bus(IEEE1722TpAcfBus):
            pass

        bus = _Bus(None, "CanBus")
        can_part = bus.createIEEE1722TpAcfCanPart("CanPart1")
        can_part.setCollectionTrigger(_trigger(PduCollectionTriggerEnum.ALWAYS))
        lin_part = bus.createIEEE1722TpAcfLinPart("LinPart1")
        lin_part.setCollectionTrigger(_trigger(PduCollectionTriggerEnum.NEVER))
        bus_id = PositiveInteger()
        bus_id.setValue(7)
        bus.setBusId(bus_id)

        parent = ET.Element("PARENT")
        writer.writeIEEE1722TpAcfBus(parent, bus)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = _Bus(None, "CanBus")
        parser.readIEEE1722TpAcfBus(element, reloaded)
        parts = reloaded.getAcfParts()
        assert len(parts) == 2
        assert parts[0].getShortName() == "CanPart1"
        assert parts[0].getCollectionTrigger().getValue() == PduCollectionTriggerEnum.ALWAYS
        assert parts[1].getShortName() == "LinPart1"
        assert parts[1].getCollectionTrigger().getValue() == PduCollectionTriggerEnum.NEVER
        assert reloaded.getBusId().getValue() == 7
