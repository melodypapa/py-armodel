"""Tests for the writeIEEE1722TpAcfCanPart handler (R23-11 IEEE1722TpAcfCanPart, Table 6.294, p.661)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrameTxBehaviorEnum,
    RxIdentifierRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfCanPart,
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


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _enum(enum_cls, value):
    enum = enum_cls()
    enum.setValue(value)
    return enum


def _fill_part(part: IEEE1722TpAcfCanPart) -> IEEE1722TpAcfCanPart:
    part.setCanAddressingMode(_enum(CanAddressingModeType, CanAddressingModeType.ENUM_EXTENDED))
    part.setCanBitRateSwitch(_bool(True))
    part.setCanFrameTxBehavior(_enum(CanFrameTxBehaviorEnum, CanFrameTxBehaviorEnum.ENUM_CAN_FD))
    part.setCanIdentifier(_pos_int(23))
    part.setCanIdentifierMask(_pos_int(4095))
    identifier_range = RxIdentifierRange()
    identifier_range.setLowerCanId(_pos_int(0))
    identifier_range.setUpperCanId(_pos_int(3000))
    part.setCanIdentifierRange(identifier_range)
    sdu_ref = RefType()
    sdu_ref.setDest("PDU-TRIGGERING-REF")
    sdu_ref.setValue("/Pkg/PduTriggering")
    part.setSduRef(sdu_ref)
    return part


class TestWriteIEEE1722TpAcfCanPart:
    """Tests for writeIEEE1722TpAcfCanPart handler (R23-11 IEEE1722TpAcfCanPart, Table 6.294, p.661)."""

    def test_children_in_xsd_order(self, writer):
        part = _fill_part(IEEE1722TpAcfCanPart(None, "CanPart1"))

        parent = _parent()
        writer.writeIEEE1722TpAcfCanPart(parent, part)
        child = parent.find("IEEE-1722-TP-ACF-CAN-PART")
        child_tags = [element.tag for element in child]
        assert child_tags == [
            "SHORT-NAME",
            "CAN-ADDRESSING-MODE",
            "CAN-BIT-RATE-SWITCH",
            "CAN-FRAME-TX-BEHAVIOR",
            "CAN-IDENTIFIER",
            "CAN-IDENTIFIER-MASK",
            "CAN-IDENTIFIER-RANGE",
            "SDU-REF",
        ]

    def test_field_values_in_xml(self, writer):
        part = _fill_part(IEEE1722TpAcfCanPart(None, "CanPart1"))

        parent = _parent()
        writer.writeIEEE1722TpAcfCanPart(parent, part)
        child = parent.find("IEEE-1722-TP-ACF-CAN-PART")
        assert child.find("CAN-ADDRESSING-MODE").text == "EXTENDED"
        assert child.find("CAN-BIT-RATE-SWITCH").text == "true"
        assert child.find("CAN-FRAME-TX-BEHAVIOR").text == "CAN-FD"
        assert child.find("CAN-IDENTIFIER").text == "23"
        assert child.find("CAN-IDENTIFIER-MASK").text == "4095"
        assert child.find("CAN-IDENTIFIER-RANGE/UPPER-CAN-ID").text == "3000"
        sdu_ref = child.find("SDU-REF")
        assert sdu_ref.text == "/Pkg/PduTriggering"
        assert sdu_ref.attrib["DEST"] == "PDU-TRIGGERING-REF"

    def test_empty_part_writes_only_short_name(self, writer):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")

        parent = _parent()
        writer.writeIEEE1722TpAcfCanPart(parent, part)
        child = parent.find("IEEE-1722-TP-ACF-CAN-PART")
        assert [element.tag for element in child] == ["SHORT-NAME"]

    def test_round_trip(self, writer, parser):
        part = _fill_part(IEEE1722TpAcfCanPart(None, "CanPart1"))

        parent = _parent()
        writer.writeIEEE1722TpAcfCanPart(parent, part)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpAcfCanPart(None, "CanPart1")
        parser.readIEEE1722TpAcfCanPart(element, reloaded)
        assert reloaded.getCanAddressingMode().getValue() == "EXTENDED"
        assert reloaded.getCanBitRateSwitch().getValue() is True
        assert reloaded.getCanFrameTxBehavior().getValue() == "CAN-FD"
        assert reloaded.getCanIdentifier().getValue() == 23
        assert reloaded.getCanIdentifierMask().getValue() == 4095
        assert reloaded.getCanIdentifierRange().getLowerCanId().getValue() == 0
        assert reloaded.getCanIdentifierRange().getUpperCanId().getValue() == 3000
        assert reloaded.getSduRef().getValue() == "/Pkg/PduTriggering"
        assert reloaded.getSduRef().getDest() == "PDU-TRIGGERING-REF"

    def test_round_trip_via_acf_bus_dispatch(self, writer, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
            IEEE1722TpAcfBus,
        )

        class _Bus(IEEE1722TpAcfBus):
            pass

        bus = _Bus(None, "CanBus")
        part = bus.createIEEE1722TpAcfCanPart("CanPart1")
        part.setCanIdentifier(_pos_int(23))
        sdu_ref = RefType()
        sdu_ref.setDest("PDU-TRIGGERING-REF")
        sdu_ref.setValue("/Pkg/PduTriggering")
        part.setSduRef(sdu_ref)
        bus.setBusId(_pos_int(4))

        parent = _parent()
        writer.writeIEEE1722TpAcfBus(parent, bus)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = _Bus(None, "CanBus")
        parser.readIEEE1722TpAcfBus(element, reloaded)
        parts = reloaded.getAcfParts()
        assert len(parts) == 1
        assert isinstance(parts[0], IEEE1722TpAcfCanPart)
        assert parts[0].getCanIdentifier().getValue() == 23
        assert parts[0].getSduRef().getValue() == "/Pkg/PduTriggering"
        assert reloaded.getBusId().getValue() == 4
