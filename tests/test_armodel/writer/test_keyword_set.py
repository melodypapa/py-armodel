"""Writer tests for KeywordSet (AUTOSAR_TPS_StandardizationTemplate (R4.3.1), Table 6.1, p.90).

XML element order per XSD group KEYWORD-SET (AUTOSAR_00044.xsd l.52295): the
KEYWORDS wrapper (after the emitted IDENTIFIABLE/ARElement base chain content).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import KeywordSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class _MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _new_keyword_set():
    keyword_set = KeywordSet(_MockParent(), "Set1")

    first = keyword_set.createKeyword("Cmft")
    first.setAbbrName(NameToken().setValue("Cmft"))
    second = keyword_set.createKeyword("Mngt")
    second.addClassification(NameToken().setValue("INDEX"))
    return keyword_set


class TestWriteKeywordSet:
    def test_write_all_fields(self):
        parent = ET.Element("ROOT")
        ARXMLWriter().writeKeywordSet(parent, _new_keyword_set())
        node = parent.find("KEYWORD-SET")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["SHORT-NAME", "KEYWORDS"]
        keywords = node.findall("KEYWORDS/KEYWORD")
        assert len(keywords) == 2
        assert keywords[0].find("SHORT-NAME").text == "Cmft"
        assert keywords[0].find("ABBR-NAME").text == "Cmft"
        assert [c.text for c in keywords[1].findall("CLASSIFICATIONS/CLASSIFICATION")] == ["INDEX"]

    def test_write_empty_fields_omits_optional_tags(self):
        parent = ET.Element("ROOT")
        ARXMLWriter().writeKeywordSet(parent, KeywordSet(_MockParent(), "Empty1"))
        node = parent.find("KEYWORD-SET")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]
