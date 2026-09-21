"""Writer round-trip tests for AbstractEthernetFrame (Table 6.229, p.578)
exercised through its concrete subclass GenericEthernetFrame (Table 6.231).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import AbstractEthernetFrame
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _build_document():
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Frames")
    frame = pkg.createGenericEthernetFrame("GenFrame")

    length = Integer()
    length.setValue("16")
    frame.setFrameLength(length)

    mapping = frame.createPduToFrameMapping("Map1")
    ref = RefType()
    ref.setDest("SECURED-I-PDU")
    ref.setValue("/Pdus/SecuredPdu")
    mapping.setPduRef(ref)
    position = Integer()
    position.setValue("0")
    mapping.setStartPosition(position)
    return document


def test_write_generic_ethernet_frame_xml():
    document = _build_document()
    frame = document.find("/Frames/GenFrame")

    parent = ET.Element("ROOT")
    ARXMLWriter().writeGenericEthernetFrame(parent, frame)

    elem = parent.find("ETHERNET-FRAME")
    assert elem is not None
    assert elem.find("SHORT-NAME").text == "GenFrame"
    assert elem.find("FRAME-LENGTH") is not None
    assert float(elem.find("FRAME-LENGTH").text) == 16
    mappings = elem.find("PDU-TO-FRAME-MAPPINGS")
    assert mappings is not None
    mapping = mappings.find("PDU-TO-FRAME-MAPPING")
    assert mapping is not None
    assert mapping.find("SHORT-NAME").text == "Map1"
    pdu_ref = mapping.find("PDU-REF")
    assert pdu_ref.text == "/Pdus/SecuredPdu"
    assert pdu_ref.attrib["DEST"] == "SECURED-I-PDU"
    assert float(mapping.find("START-POSITION").text) == 0


def test_write_generic_ethernet_frame_round_trip(tmp_path):
    document = _build_document()
    path = tmp_path / "ethernet_frame.arxml"
    ARXMLWriter().save(str(path), document)

    AUTOSAR.getInstance().new()
    reloaded = AUTOSAR.getInstance()
    reloaded.setARRelease("R23-11")
    ARXMLParser().load(str(path), reloaded)

    frame = reloaded.find("/Frames/GenFrame")
    assert isinstance(frame, AbstractEthernetFrame)
    assert frame.getFrameLength() is not None
    assert frame.getFrameLength().getValue() == 16

    mappings = frame.getPduToFrameMappings()
    assert len(mappings) == 1
    mapping = mappings[0]
    assert mapping.getShortName() == "Map1"
    assert mapping.getPduRef().getValue() == "/Pdus/SecuredPdu"
    assert mapping.getPduRef().getDest() == "SECURED-I-PDU"
    assert mapping.getStartPosition().getValue() == 0


def test_write_generic_ethernet_frame_empty_wrapper(tmp_path):
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Frames")
    pkg.createGenericEthernetFrame("EmptyFrame")

    path = tmp_path / "empty_frame.arxml"
    ARXMLWriter().save(str(path), document)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "PDU-TO-FRAME-MAPPINGS" not in content
    assert "FRAME-LENGTH" not in content

    AUTOSAR.getInstance().new()
    reloaded = AUTOSAR.getInstance()
    reloaded.setARRelease("R23-11")
    ARXMLParser().load(str(path), reloaded)
    frame = reloaded.find("/Frames/EmptyFrame")
    assert isinstance(frame, AbstractEthernetFrame)
    assert frame.getFrameLength() is None
    assert frame.getPduToFrameMappings() == []
