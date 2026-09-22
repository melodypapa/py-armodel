"""Parser tests for KeywordSet (AUTOSAR_TPS_StandardizationTemplate (R4.3.1), Table 6.1, p.90).

XML element order per XSD group KEYWORD-SET (AUTOSAR_00044.xsd l.52295): the
KEYWORDS wrapper (after the emitted IDENTIFIABLE/ARElement base chain content).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import KeywordSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class _MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _keyword_set_fragment():
    return (
        "<KEYWORD-SET xmlns='%s'>"
        "<SHORT-NAME>Set1</SHORT-NAME>"
        "<KEYWORDS>"
        "<KEYWORD><SHORT-NAME>Cmft</SHORT-NAME><ABBR-NAME>Cmft</ABBR-NAME></KEYWORD>"
        "<KEYWORD><SHORT-NAME>Mngt</SHORT-NAME><CLASSIFICATIONS><CLASSIFICATION>INDEX</CLASSIFICATION></CLASSIFICATIONS></KEYWORD>"
        "</KEYWORDS>"
        "</KEYWORD-SET>" % NS
    )


def test_parse_keyword_set():
    keyword_set = KeywordSet(_MockParent(), "Set1")
    root = ET.fromstring(_keyword_set_fragment())
    ARXMLParser().readKeywordSet(root, keyword_set)

    assert isinstance(keyword_set, AtpBlueprintable)
    keywords = keyword_set.getKeywords()
    assert [k.getShortName() for k in keywords] == ["Cmft", "Mngt"]
    assert keywords[0].getAbbrName().getValue() == "Cmft"
    assert [c.getValue() for c in keywords[1].getClassifications()] == ["INDEX"]


def test_parse_keyword_set_empty():
    keyword_set = KeywordSet(_MockParent(), "Set1")
    root = ET.fromstring("<KEYWORD-SET xmlns='%s'><SHORT-NAME>Set1</SHORT-NAME></KEYWORD-SET>" % NS)
    ARXMLParser().readKeywordSet(root, keyword_set)

    assert keyword_set.getKeywords() == []


def test_round_trip_preserves_all_values():
    keyword_set = KeywordSet(_MockParent(), "Set1")
    root = ET.fromstring(_keyword_set_fragment())
    ARXMLParser().readKeywordSet(root, keyword_set)

    parent = ET.Element("ROOT")
    from armodel.writer.arxml_writer import ARXMLWriter

    ARXMLWriter().writeKeywordSet(parent, keyword_set)
    inner = ET.tostring(parent).decode("utf-8")
    reparsed_root = ET.fromstring(inner.replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))

    parsed = KeywordSet(_MockParent(), "Set1")
    ARXMLParser().readKeywordSet(reparsed_root[0], parsed)

    keywords = parsed.getKeywords()
    assert [k.getShortName() for k in keywords] == ["Cmft", "Mngt"]
    assert keywords[0].getAbbrName().getValue() == "Cmft"
    assert [c.getValue() for c in keywords[1].getClassifications()] == ["INDEX"]
