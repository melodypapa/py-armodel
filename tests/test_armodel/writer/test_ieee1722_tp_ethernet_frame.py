"""Writer round-trip tests for Ieee1722TpEthernetFrame (Table 6.233, p.579)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import AbstractEthernetFrame, Ieee1722TpEthernetFrame
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _build_document():
    document = AUTOSAR.getInstance()
    pkg = document.createARPackage("Frames")
    frame = pkg.createIeee1722TpEthernetFrame("IeeeFrame")

    frame.setRelativeRepresentationTime(TimeValue().setValue(0.05))
    frame.setStreamIdentifier(PositiveInteger().setValue("42"))
    frame.setSubType(PositiveInteger().setValue("7"))
    frame.setVersion(PositiveInteger().setValue("2"))
    return document


def test_write_ieee1722_tp_ethernet_frame_xml():
    document = _build_document()
    frame = document.find("/Frames/IeeeFrame")

    parent = ET.Element("ROOT")
    ARXMLWriter().writeIeee1722TpEthernetFrame(parent, frame)

    elem = parent.find("IEEE-1722-TP-ETHERNET-FRAME")
    assert elem is not None
    assert elem.find("SHORT-NAME").text == "IeeeFrame"
    assert float(elem.find("RELATIVE-REPRESENTATION-TIME").text) == 0.05
    assert int(elem.find("STREAM-IDENTIFIER").text) == 42
    assert int(elem.find("SUB-TYPE").text) == 7
    assert int(elem.find("VERSION").text) == 2

    tags = [child.tag for child in elem]
    own_tags = [tag for tag in tags if tag in ("RELATIVE-REPRESENTATION-TIME", "STREAM-IDENTIFIER", "SUB-TYPE", "VERSION")]
    assert own_tags == ["RELATIVE-REPRESENTATION-TIME", "STREAM-IDENTIFIER", "SUB-TYPE", "VERSION"]


def test_write_ieee1722_tp_ethernet_frame_round_trip(tmp_path):
    document = _build_document()
    path = tmp_path / "ieee1722_tp_frame.arxml"
    ARXMLWriter().save(str(path), document)

    AUTOSAR.getInstance().new()
    reloaded = AUTOSAR.getInstance()
    reloaded.setARRelease("R23-11")
    ARXMLParser().load(str(path), reloaded)

    frame = reloaded.find("/Frames/IeeeFrame")
    assert isinstance(frame, Ieee1722TpEthernetFrame)
    assert isinstance(frame, AbstractEthernetFrame)
    assert frame.getShortName() == "IeeeFrame"
    assert frame.getRelativeRepresentationTime() is not None
    assert frame.getRelativeRepresentationTime().getValue() == 0.05
    assert frame.getStreamIdentifier() is not None
    assert frame.getStreamIdentifier().getValue() == 42
    assert frame.getSubType() is not None
    assert frame.getSubType().getValue() == 7
    assert frame.getVersion() is not None
    assert frame.getVersion().getValue() == 2


def test_write_ieee1722_tp_ethernet_frame_empty(tmp_path):
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Frames")
    pkg.createIeee1722TpEthernetFrame("EmptyFrame")

    path = tmp_path / "empty_ieee_frame.arxml"
    ARXMLWriter().save(str(path), document)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for tag in ("RELATIVE-REPRESENTATION-TIME", "STREAM-IDENTIFIER", "SUB-TYPE", "VERSION"):
        assert tag not in content

    AUTOSAR.getInstance().new()
    reloaded = AUTOSAR.getInstance()
    reloaded.setARRelease("R23-11")
    ARXMLParser().load(str(path), reloaded)
    frame = reloaded.find("/Frames/EmptyFrame")
    assert isinstance(frame, Ieee1722TpEthernetFrame)
    assert frame.getRelativeRepresentationTime() is None
    assert frame.getStreamIdentifier() is None
    assert frame.getSubType() is None
    assert frame.getVersion() is None
