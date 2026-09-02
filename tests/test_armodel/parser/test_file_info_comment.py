"""Reader/writer round-trip tests for FileInfoComment (R23-11,
AUTOSAR_FO_TPS_GenericStructureTemplate, Table 2.1, p.29).

FileInfoComment carries a single aggregation `sdgs` (List[Sdg]). The root
reader getFileInfoComment + getSdg and the root writer setFileInfoComment +
setSdg must round-trip the SDG entries including their GID attribute and
SdgCaption short name, and must tolerate an empty sdgs list (no SDGS wrapper).
"""

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import FileInfoComment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})


def _build_comment_with_sdgs():
    comment = FileInfoComment()
    sdg1 = Sdg()
    sdg1.setGID(NameToken().setValue("g1"))
    sdg1.createSdgCaption("caption_one")
    sdg2 = Sdg()
    sdg2.setGID(NameToken().setValue("g2"))
    comment.addSdg(sdg1)
    comment.addSdg(sdg2)
    return comment


def test_file_info_comment_round_trips_multiple_sdgs(parser, tmp_path):
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    document.setFileInfoComment(_build_comment_with_sdgs())

    out = tmp_path / "out.arxml"
    ARXMLWriter().save(str(out), document)

    document2 = AUTOSAR.getInstance()
    document2.new()
    parser.load(str(out), document2)

    fic = document2.getFileInfoComment()
    assert fic is not None
    sdgs = fic.getSdgs()
    assert len(sdgs) == 2
    assert sdgs[0].getGID() is not None
    assert sdgs[0].getGID().getValue() == "g1"
    assert sdgs[0].getSdgCaption() is not None
    assert sdgs[0].getSdgCaption().getShortName() == "caption_one"
    assert sdgs[1].getGID() is not None
    assert sdgs[1].getGID().getValue() == "g2"


def test_file_info_comment_round_trips_empty_sdgs(parser, tmp_path):
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    comment = FileInfoComment()
    assert comment.getSdgs() == []
    document.setFileInfoComment(comment)

    out = tmp_path / "out.arxml"
    ARXMLWriter().save(str(out), document)

    raw = out.read_text(encoding="utf-8")
    assert "<SDGS" not in raw

    document2 = AUTOSAR.getInstance()
    document2.new()
    parser.load(str(out), document2)

    fic = document2.getFileInfoComment()
    assert fic is not None
    assert fic.getSdgs() == []
