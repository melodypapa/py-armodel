"""Writer round-trip tests for HwAttributeDef (AUTOSAR_CP_TPS_ECUResourceTemplate, Table 2.13, p.26).

Child order per XSD group HW-ATTRIBUTE-DEF (AUTOSAR_00052.xsd l.65571):
HW-ATTRIBUTE-LITERALS, IS-REQUIRED, UNIT-REF (after the Identifiable groups).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeDef
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


def _new_attribute_def():
    attribute_def = HwAttributeDef(_MockParent(), "AttrDef1")
    attribute_def.createHwAttributeLiteral("LITERAL_1")
    attribute_def.createHwAttributeLiteral("LITERAL_2")
    attribute_def.setIsRequired(_bool("true"))
    attribute_def.setUnitRef(_ref("/Units/Length", "UNIT"))
    return attribute_def


def test_write_hw_attribute_def_xml():
    parent = ET.Element("ROOT")
    ARXMLWriter().writeHwAttributeDef(parent, _new_attribute_def())

    node = parent.find("HW-ATTRIBUTE-DEF")
    assert node is not None
    assert node.find("SHORT-NAME").text == "AttrDef1"
    literals = node.findall("HW-ATTRIBUTE-LITERALS/HW-ATTRIBUTE-LITERAL-DEF")
    assert [lit.find("SHORT-NAME").text for lit in literals] == ["LITERAL_1", "LITERAL_2"]
    assert node.find("IS-REQUIRED").text == "true"
    unit_ref = node.find("UNIT-REF")
    assert unit_ref.text == "/Units/Length"
    assert unit_ref.attrib["DEST"] == "UNIT"
    assert [child.tag for child in node] == [
        "SHORT-NAME",
        "HW-ATTRIBUTE-LITERALS",
        "IS-REQUIRED",
        "UNIT-REF",
    ]


def test_write_empty_hw_attribute_def_omits_optional_tags():
    parent = ET.Element("ROOT")
    ARXMLWriter().writeHwAttributeDef(parent, HwAttributeDef(_MockParent(), "EmptyDef"))

    node = parent.find("HW-ATTRIBUTE-DEF")
    assert node is not None
    assert [child.tag for child in node] == ["SHORT-NAME"]


def test_round_trip_preserves_all_values():
    attribute_def = _new_attribute_def()
    parent = ET.Element("ROOT")
    ARXMLWriter().writeHwAttributeDef(parent, attribute_def)
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

    parsed = HwAttributeDef(_MockParent(), "AttrDef1")
    ARXMLParser().readHwAttributeDef(root[0][0], parsed)

    assert parsed.getShortName() == "AttrDef1"
    literals = parsed.getHwAttributeLiterals()
    assert [lit.getShortName() for lit in literals] == ["LITERAL_1", "LITERAL_2"]
    assert parsed.getIsRequired().getValue() is True
    assert parsed.getUnitRef().getValue() == "/Units/Length"
    assert parsed.getUnitRef().getDest() == "UNIT"
