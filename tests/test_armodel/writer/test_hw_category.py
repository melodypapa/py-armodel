"""Writer round-trip tests for HwCategory (AUTOSAR_CP_TPS_ECUResourceTemplate, Table 2.11, p.24).

The HW-CATEGORY group (HW-ATTRIBUTE-DEFS) is emitted after the full ARElement
base chain per XSD complexType HW-CATEGORY (AUTOSAR_00052.xsd l.65746); the
nested HW-ATTRIBUTE-DEF order per XSD group HW-ATTRIBUTE-DEF (l.65571):
HW-ATTRIBUTE-LITERALS, IS-REQUIRED, UNIT-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwCategory
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.parser.arxml_parser import ARXMLParser
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


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_hw_category():
    hw_category = HwCategory(_MockParent(), "Cat1")
    attr_def = hw_category.createHwAttributeDef("AttrDef1")
    attr_def.createHwAttributeLiteral("LITERAL_1")
    attr_def.setIsRequired(_bool("true"))
    attr_def.setUnitRef(_ref("/Units/Length", "UNIT"))
    hw_category.createHwAttributeDef("AttrDef2")
    return hw_category


def test_write_hw_category_xml():
    parent = ET.Element("ROOT")
    ARXMLWriter().writeHwCategory(parent, _new_hw_category())

    node = parent.find("HW-CATEGORY")
    assert node is not None
    assert node.find("SHORT-NAME").text == "Cat1"
    assert [child.tag for child in node][-1] == "HW-ATTRIBUTE-DEFS"
    attr_defs = node.findall("HW-ATTRIBUTE-DEFS/HW-ATTRIBUTE-DEF")
    assert len(attr_defs) == 2
    assert attr_defs[0].find("SHORT-NAME").text == "AttrDef1"
    literals = attr_defs[0].findall("HW-ATTRIBUTE-LITERALS/HW-ATTRIBUTE-LITERAL-DEF")
    assert literals[0].find("SHORT-NAME").text == "LITERAL_1"
    assert attr_defs[0].find("IS-REQUIRED").text == "true"
    assert attr_defs[0].find("UNIT-REF").text == "/Units/Length"
    assert attr_defs[0].find("UNIT-REF").attrib["DEST"] == "UNIT"
    assert attr_defs[1].find("SHORT-NAME").text == "AttrDef2"


def test_round_trip_preserves_all_values():
    hw_category = _new_hw_category()
    parent = ET.Element("ROOT")
    ARXMLWriter().writeHwCategory(parent, hw_category)
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

    parsed = HwCategory(_MockParent(), "Cat1")
    ARXMLParser().readHwCategory(root[0][0], parsed)

    assert parsed.getShortName() == "Cat1"
    attr_defs = parsed.getHwAttributeDefs()
    assert [a.getShortName() for a in attr_defs] == ["AttrDef1", "AttrDef2"]
    assert [lit.getShortName() for lit in attr_defs[0].getHwAttributeLiterals()] == ["LITERAL_1"]
    assert attr_defs[0].getIsRequired().getValue() is True
    assert attr_defs[0].getUnitRef().getValue() == "/Units/Length"
    assert attr_defs[0].getUnitRef().getDest() == "UNIT"
    assert attr_defs[1].getHwAttributeLiterals() == []
