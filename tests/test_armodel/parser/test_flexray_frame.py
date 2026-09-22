"""Parser tests for FlexrayFrame (AUTOSAR_CP_TPS_SystemTemplate, Table 6.80, p.422).

Zero attribute rows — the element contributes no XML content of its own;
coverage runs through the ARPackage FLEXRAY-FRAME dispatch and the inherited
Frame content.
"""

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrame
from armodel.parser.arxml_parser import ARXMLParser


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def test_parse_flexray_frame_dispatch(tmp_path):
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Frames")
    pkg.createFlexrayFrame("FrFrame")

    from armodel.writer.arxml_writer import ARXMLWriter

    path = tmp_path / "flexray_frame.arxml"
    ARXMLWriter().save(str(path), document)

    AUTOSAR.getInstance().new()
    reloaded = AUTOSAR.getInstance()
    reloaded.setARRelease("R23-11")
    ARXMLParser().load(str(path), reloaded)

    frame = reloaded.find("/Frames/FrFrame")
    assert isinstance(frame, FlexrayFrame)
