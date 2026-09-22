"""Writer tests for Keyword (AUTOSAR_TPS_StandardizationTemplate (R4.3.1), Table 6.2, p.91).

The writer helper is exercised directly (the class has no ARPackage-level
dispatch; it nests inside KeywordSet's KEYWORDS wrapper).
XML element order per XSD group KEYWORD (AUTOSAR_00044.xsd l.52244): ABBR-NAME,
CLASSIFICATIONS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import Keyword
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


def _new_keyword():
    keyword = Keyword(_MockParent(), "Cmft")
    keyword.setAbbrName(NameToken().setValue("Cmft"))
    keyword.addClassification(NameToken().setValue("MEAN"))
    keyword.addClassification(NameToken().setValue("ACTION"))
    return keyword


class TestWriteKeyword:
    def test_write_all_fields(self):
        parent = ET.Element("ROOT")
        ARXMLWriter().writeKeyword(parent, _new_keyword())
        node = parent.find("KEYWORD")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["SHORT-NAME", "ABBR-NAME", "CLASSIFICATIONS"]
        assert node.find("ABBR-NAME").text == "Cmft"
        classifications = node.findall("CLASSIFICATIONS/CLASSIFICATION")
        assert [c.text for c in classifications] == ["MEAN", "ACTION"]

    def test_write_empty_fields_omits_optional_tags(self):
        parent = ET.Element("ROOT")
        ARXMLWriter().writeKeyword(parent, Keyword(_MockParent(), "Empty1"))
        node = parent.find("KEYWORD")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]
