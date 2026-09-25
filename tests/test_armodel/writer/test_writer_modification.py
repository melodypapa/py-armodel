"""Reader/writer round-trip tests for Modification (Table 4.18)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.MSR.AsamHdo.AdminData import DocRevision, Modification
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _overview_paragraph(text: str) -> MultiLanguageOverviewParagraph:
    paragraph = MultiLanguageOverviewParagraph()
    paragraph.addL2(LOverviewParagraph().setValue(text))
    return paragraph


def _full_modification() -> Modification:
    modification = Modification()
    modification.setChange(_overview_paragraph("changed the timing condition"))
    modification.setReason(_overview_paragraph("fix the startup delay"))
    return modification


def test_write_modification(writer):
    parent = _parent()
    writer.writeModification(parent, _full_modification())

    tag = parent.find("MODIFICATION")
    assert tag is not None
    children = list(tag)
    assert [child.tag for child in children] == ["CHANGE", "REASON"]
    assert children[0].find("L-2").text == "changed the timing condition"
    assert children[1].find("L-2").text == "fix the startup delay"


def test_write_modification_empty(writer):
    parent = _parent()
    writer.writeModification(parent, Modification())

    tag = parent.find("MODIFICATION")
    assert tag is not None
    assert len(list(tag)) == 0


def test_write_doc_revision_empty_modifications(writer):
    parent = _parent()
    writer.writeDocRevisionModifications(parent, DocRevision())

    assert parent.find("MODIFICATIONS") is None


def test_modification_round_trip(writer):
    revision = DocRevision()
    revision.addModification(_full_modification())

    parent = _parent()
    writer.writeDocRevisionModifications(parent, revision)

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded_revision = DocRevision()
    parser.readDocRevisionModifications(reparsed, reloaded_revision)

    modifications = reloaded_revision.getModifications()
    assert len(modifications) == 1
    reloaded = modifications[0]
    assert isinstance(reloaded, Modification)
    assert isinstance(reloaded.getChange(), MultiLanguageOverviewParagraph)
    assert reloaded.getChange().getL2s()[0].getValue() == "changed the timing condition"
    assert isinstance(reloaded.getReason(), MultiLanguageOverviewParagraph)
    assert reloaded.getReason().getL2s()[0].getValue() == "fix the startup delay"
