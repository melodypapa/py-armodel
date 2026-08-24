"""Tests for Frame writer and round-trip (Table 6.78: Frame)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrame
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


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
    re_frame = re_pkg.getElement("MyFrame", CanFrame)
    assert re_frame is not None
    assert isinstance(re_frame.getFrameLength(), Integer)
    assert re_frame.getFrameLength().getValue() == 100
    mappings = re_frame.getPduToFrameMappings()
    assert len(mappings) == 1
    assert mappings[0].getShortName() == "Map1"
