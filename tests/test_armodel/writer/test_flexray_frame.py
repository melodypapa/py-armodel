"""Writer round-trip tests for FlexrayFrame (AUTOSAR_CP_TPS_SystemTemplate, Table 6.80, p.422).

Zero attribute rows — the writer emits the FLEXRAY-FRAME element with the
inherited Frame content only; element order per XSD complexType FLEXRAY-FRAME
(AR-OBJECT → REFERRABLE → ... → FIBEX-ELEMENT → FRAME → FLEXRAY-FRAME).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrame
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
    pkg.createFlexrayFrame("FrFrame")
    return document


def test_write_flexray_frame_xml():
    document = _build_document()
    frame = document.find("/Frames/FrFrame")

    parent = ET.Element("ROOT")
    ARXMLWriter().writeFlexrayFrame(parent, frame)

    elem = parent.find("FLEXRAY-FRAME")
    assert elem is not None
    assert elem.find("SHORT-NAME").text == "FrFrame"


def test_write_flexray_frame_round_trip(tmp_path):
    document = _build_document()
    path = tmp_path / "flexray_frame.arxml"
    ARXMLWriter().save(str(path), document)

    AUTOSAR.getInstance().new()
    reloaded = AUTOSAR.getInstance()
    reloaded.setARRelease("R23-11")
    ARXMLParser().load(str(path), reloaded)

    frame = reloaded.find("/Frames/FrFrame")
    assert isinstance(frame, FlexrayFrame)
    assert frame.getShortName() == "FrFrame"
