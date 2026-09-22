"""Parser tests for Keyword (AUTOSAR_TPS_StandardizationTemplate (R4.3.1), Table 6.2, p.91).

The reader helper is exercised directly on a KEYWORD fragment (the class has no
ARPackage-level dispatch; it nests inside KeywordSet's KEYWORDS wrapper).
XML element order per XSD group KEYWORD (AUTOSAR_00044.xsd l.52244): ABBR-NAME,
CLASSIFICATIONS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import Keyword
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


def _keyword_fragment():
    return (
        "<KEYWORD xmlns='%s'>"
        "<SHORT-NAME>Cmft</SHORT-NAME>"
        "<ABBR-NAME>Cmft</ABBR-NAME>"
        "<CLASSIFICATIONS>"
        "<CLASSIFICATION>MEAN</CLASSIFICATION>"
        "<CLASSIFICATION>ACTION</CLASSIFICATION>"
        "</CLASSIFICATIONS>"
        "</KEYWORD>" % NS
    )


def test_parse_keyword():
    keyword = Keyword(_MockParent(), "Cmft")
    root = ET.fromstring(_keyword_fragment())
    ARXMLParser().readKeyword(root, keyword)

    assert keyword.getShortName() == "Cmft"
    assert keyword.getAbbrName().getValue() == "Cmft"
    assert [c.getValue() for c in keyword.getClassifications()] == ["MEAN", "ACTION"]


def test_parse_keyword_empty():
    keyword = Keyword(_MockParent(), "Cmft")
    root = ET.fromstring("<KEYWORD xmlns='%s'><SHORT-NAME>Cmft</SHORT-NAME></KEYWORD>" % NS)
    ARXMLParser().readKeyword(root, keyword)

    assert keyword.getAbbrName() is None
    assert keyword.getClassifications() == []


def test_round_trip_preserves_all_values():
    keyword = Keyword(_MockParent(), "Cmft")
    root = ET.fromstring(_keyword_fragment())
    ARXMLParser().readKeyword(root, keyword)

    parent = ET.Element("ROOT")
    from armodel.writer.arxml_writer import ARXMLWriter

    ARXMLWriter().writeKeyword(parent, keyword)
    inner = ET.tostring(parent).decode("utf-8")
    reparsed_root = ET.fromstring(inner.replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))

    parsed = Keyword(_MockParent(), "Cmft")
    ARXMLParser().readKeyword(reparsed_root[0], parsed)

    assert parsed.getAbbrName().getValue() == "Cmft"
    assert [c.getValue() for c in parsed.getClassifications()] == ["MEAN", "ACTION"]
