"""Tests for Frame writer and round-trip (Table 6.78: Frame)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
    DateTime,
    Integer,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrame
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

_UUID_VALUE = "7c3a5b6c-7d8e-49a0-b1c2-3d4e5f6a7b8e"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def test_write_frame_frame_length(writer):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    frame = pkg.createCanFrame("MyFrame")
    frame.setFrameLength(Integer().setValue("100"))
    parent = ET.Element("CAN-FRAMES")
    writer.writeCanFrame(parent, frame)
    cf = parent.find("CAN-FRAME")
    assert cf.find("FRAME-LENGTH").text == "100"


def test_round_trip_frame(writer, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    frame = pkg.createCanFrame("MyFrame")
    frame.setFrameLength(Integer().setValue("100"))
    frame.createPduToFrameMapping("Map1")

    out_file = str(tmp_path / "frame.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    AUTOSAR.getInstance().new()
    parser = ARXMLParser(options={"warning": True})
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(out_file, document)

    re_pkg = document.find("Pkg")
    re_frame = re_pkg.getReferrableElement("MyFrame", CanFrame)
    assert re_frame is not None
    assert isinstance(re_frame.getFrameLength(), Integer)
    assert re_frame.getFrameLength().getValue() == 100
    mappings = re_frame.getPduToFrameMappings()
    assert len(mappings) == 1
    assert mappings[0].getShortName() == "Map1"


def test_write_frame_empty_wrapper_list(writer):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    frame = pkg.createCanFrame("MyFrame")
    parent = ET.Element("CAN-FRAMES")
    writer.writeCanFrame(parent, frame)
    cf = parent.find("CAN-FRAME")
    assert cf.find("FRAME-LENGTH") is None
    assert cf.find("PDU-TO-FRAME-MAPPINGS") is None


def test_round_trip_frame_mapping_values(writer, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    frame = pkg.createCanFrame("MyFrame")
    mapping = frame.createPduToFrameMapping("Map1")
    mapping.setPackingByteOrder(ByteOrderEnum().setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST))
    pdu_ref = RefType()
    pdu_ref.setValue("/pdus/NmPdu1")
    pdu_ref.setDest("NM-PDU")
    mapping.setPduRef(pdu_ref)
    mapping.setStartPosition(Integer().setValue("8"))
    mapping.setUpdateIndicationBitPosition(Integer().setValue("7"))

    out_file = str(tmp_path / "frame_mappings.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    AUTOSAR.getInstance().new()
    parser = ARXMLParser(options={"warning": True})
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(out_file, document)

    re_frame = document.find("Pkg").getReferrableElement("MyFrame", CanFrame)
    mappings = re_frame.getPduToFrameMappings()
    assert len(mappings) == 1
    re_mapping = mappings[0]
    assert re_mapping.getShortName() == "Map1"
    assert re_mapping.getPackingByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-FIRST"
    assert re_mapping.getPduRef().getValue() == "/pdus/NmPdu1"
    assert re_mapping.getPduRef().getDest() == "NM-PDU"
    assert re_mapping.getStartPosition().getValue() == 8
    assert re_mapping.getUpdateIndicationBitPosition().getValue() == 7


def test_round_trip_frame_base_level(writer, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    frame = pkg.createCanFrame("MyFrame")
    frame.setUuid(String().setValue(_UUID_VALUE))
    frame.setCategory("someCategory")
    frame.setChecksum(String().setValue("5"))
    frame.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))

    out_file = str(tmp_path / "frame_base.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    AUTOSAR.getInstance().new()
    parser = ARXMLParser(options={"warning": True})
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(out_file, document)

    re_frame = document.find("Pkg").getReferrableElement("MyFrame", CanFrame)
    assert re_frame.getUuid().getValue() == _UUID_VALUE
    assert re_frame.getCategory().getValue() == "someCategory"
    assert re_frame.getChecksum().getValue() == "5"
    assert re_frame.getTimestamp().getValue() == "2025-04-04T00:00:00Z"


def test_round_trip_frame_mapping_document_order(writer, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    frame = pkg.createCanFrame("MyFrame")
    frame.createPduToFrameMapping("Bravo")
    frame.createPduToFrameMapping("Alpha")

    out_file = str(tmp_path / "frame_order.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    AUTOSAR.getInstance().new()
    parser = ARXMLParser(options={"warning": True})
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(out_file, document)

    re_frame = document.find("Pkg").getReferrableElement("MyFrame", CanFrame)
    mappings = re_frame.getPduToFrameMappings()
    assert [m.getShortName() for m in mappings] == ["Bravo", "Alpha"]
