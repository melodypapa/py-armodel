"""Tests for LinFrame writer position in the Frame chain (Table 6.87: LinFrame).

LinFrame is abstract and declares no own attribute rows; the concrete
LIN-UNCONDITIONAL-FRAME writer chains writeFrame (which chains
writeIdentifiable exactly once) and emits the inherited FRAME children
(FRAME-LENGTH, PDU-TO-FRAME-MAPPINGS) in XSD order.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinUnconditionalFrame
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


def test_write_lin_frame_frame_length(writer):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    frame = pkg.createLinUnconditionalFrame("MyLinFrame")
    frame.setFrameLength(Integer().setValue("8"))
    parent = ET.Element("LIN-UNCONDITIONAL-FRAMES")
    writer.writeLinUnconditionalFrame(parent, frame)
    lf = parent.find("LIN-UNCONDITIONAL-FRAME")
    assert lf is not None
    assert lf.find("SHORT-NAME").text == "MyLinFrame"
    assert lf.find("FRAME-LENGTH").text == "8"


def test_write_lin_frame_empty(writer):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    frame = pkg.createLinUnconditionalFrame("MyLinFrame")
    parent = ET.Element("LIN-UNCONDITIONAL-FRAMES")
    writer.writeLinUnconditionalFrame(parent, frame)
    lf = parent.find("LIN-UNCONDITIONAL-FRAME")
    assert lf is not None
    assert lf.find("FRAME-LENGTH") is None
    assert lf.find("PDU-TO-FRAME-MAPPINGS") is None


def test_round_trip_lin_frame(writer, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    frame = pkg.createLinUnconditionalFrame("MyLinFrame")
    frame.setFrameLength(Integer().setValue("8"))
    frame.setUuid(String().setValue(_UUID_VALUE))

    out_file = str(tmp_path / "lin_frame.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    AUTOSAR.getInstance().new()
    parser = ARXMLParser(options={"warning": True})
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(out_file, document)

    re_pkg = document.find("Pkg")
    re_frame = re_pkg.getReferrableElement("MyLinFrame", LinUnconditionalFrame)
    assert re_frame is not None
    assert isinstance(re_frame, LinUnconditionalFrame)
    assert re_frame.getUuid().getValue() == _UUID_VALUE
    assert isinstance(re_frame.getFrameLength(), Integer)
    assert re_frame.getFrameLength().getValue() == 8
