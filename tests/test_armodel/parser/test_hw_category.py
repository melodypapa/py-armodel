"""Parser tests for HwCategory (AUTOSAR_CP_TPS_ECUResourceTemplate, Table 2.11, p.24).

The reader helper is exercised directly on a HW-CATEGORY fragment; the
HW-CATEGORY group holds HW-ATTRIBUTE-DEFS (AUTOSAR_00052.xsd l.65725), each
HW-ATTRIBUTE-DEF ordered per its own group (l.65571).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeDef, HwCategory
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


def _hw_category_fragment():
    return (
        "<HW-CATEGORY xmlns='%s'>"
        "<SHORT-NAME>Cat1</SHORT-NAME>"
        "<HW-ATTRIBUTE-DEFS>"
        "<HW-ATTRIBUTE-DEF>"
        "<SHORT-NAME>AttrDef1</SHORT-NAME>"
        "<HW-ATTRIBUTE-LITERALS>"
        "<HW-ATTRIBUTE-LITERAL-DEF><SHORT-NAME>LITERAL_1</SHORT-NAME></HW-ATTRIBUTE-LITERAL-DEF>"
        "</HW-ATTRIBUTE-LITERALS>"
        "<IS-REQUIRED>true</IS-REQUIRED>"
        "<UNIT-REF DEST='UNIT'>/Units/Length</UNIT-REF>"
        "</HW-ATTRIBUTE-DEF>"
        "<HW-ATTRIBUTE-DEF><SHORT-NAME>AttrDef2</SHORT-NAME></HW-ATTRIBUTE-DEF>"
        "</HW-ATTRIBUTE-DEFS>"
        "</HW-CATEGORY>" % NS
    )


def test_parse_hw_category():
    hw_category = HwCategory(_MockParent(), "Cat1")
    root = ET.fromstring(_hw_category_fragment())
    ARXMLParser().readHwCategory(root, hw_category)

    assert hw_category.getShortName() == "Cat1"
    attr_defs = hw_category.getHwAttributeDefs()
    assert len(attr_defs) == 2
    assert all(isinstance(a, HwAttributeDef) for a in attr_defs)
    assert [a.getShortName() for a in attr_defs] == ["AttrDef1", "AttrDef2"]
    assert [lit.getShortName() for lit in attr_defs[0].getHwAttributeLiterals()] == ["LITERAL_1"]
    assert attr_defs[0].getIsRequired().getValue() is True
    assert attr_defs[0].getUnitRef().getValue() == "/Units/Length"


def test_parse_hw_category_empty():
    hw_category = HwCategory(_MockParent(), "EmptyCat")
    root = ET.fromstring("<HW-CATEGORY xmlns='%s'><SHORT-NAME>EmptyCat</SHORT-NAME></HW-CATEGORY>" % NS)
    ARXMLParser().readHwCategory(root, hw_category)

    assert hw_category.getHwAttributeDefs() == []
