"""Writer round-trip tests for UserDefinedEthernetFrame (Table 6.232, p.579)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import AbstractEthernetFrame, UserDefinedEthernetFrame
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _build_document():
    document = AUTOSAR.getInstance()
    pkg = document.createARPackage("Frames")
    frame = pkg.createUserDefinedEthernetFrame("UserFrame")

    length = Integer()
    length.setValue("64")
    frame.setFrameLength(length)
    return document


def test_write_user_defined_ethernet_frame_xml():
    document = _build_document()
    frame = document.find("/Frames/UserFrame")

    parent = ET.Element("ROOT")
    ARXMLWriter().writeUserDefinedEthernetFrame(parent, frame)

    elem = parent.find("USER-DEFINED-ETHERNET-FRAME")
    assert elem is not None
    assert elem.find("SHORT-NAME").text == "UserFrame"
    assert float(elem.find("FRAME-LENGTH").text) == 64


def test_write_user_defined_ethernet_frame_round_trip(tmp_path):
    document = _build_document()
    path = tmp_path / "user_defined_frame.arxml"
    ARXMLWriter().save(str(path), document)

    AUTOSAR.getInstance().new()
    reloaded = AUTOSAR.getInstance()
    reloaded.setARRelease("R23-11")
    ARXMLParser().load(str(path), reloaded)

    frame = reloaded.find("/Frames/UserFrame")
    assert isinstance(frame, UserDefinedEthernetFrame)
    assert isinstance(frame, AbstractEthernetFrame)
    assert frame.getShortName() == "UserFrame"
    assert frame.getFrameLength() is not None
    assert frame.getFrameLength().getValue() == 64


def test_write_user_defined_ethernet_frame_empty(tmp_path):
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Frames")
    pkg.createUserDefinedEthernetFrame("EmptyFrame")

    path = tmp_path / "empty_user_frame.arxml"
    ARXMLWriter().save(str(path), document)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "FRAME-LENGTH" not in content
    assert "PDU-TO-FRAME-MAPPINGS" not in content

    AUTOSAR.getInstance().new()
    reloaded = AUTOSAR.getInstance()
    reloaded.setARRelease("R23-11")
    ARXMLParser().load(str(path), reloaded)
    frame = reloaded.find("/Frames/EmptyFrame")
    assert isinstance(frame, UserDefinedEthernetFrame)
    assert frame.getFrameLength() is None
    assert frame.getPduToFrameMappings() == []
