"""Parser tests for HwAttributeDef (AUTOSAR_CP_TPS_ECUResourceTemplate, Table 2.13, p.26).

The reader helper is exercised directly on a HW-ATTRIBUTE-DEF fragment; XML
element order per XSD group HW-ATTRIBUTE-DEF (AUTOSAR_00052.xsd l.65571):
HW-ATTRIBUTE-LITERALS, IS-REQUIRED, UNIT-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeDef
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


def _attribute_def_fragment():
    return (
        "<HW-ATTRIBUTE-DEF xmlns='%s'>"
        "<SHORT-NAME>AttrDef1</SHORT-NAME>"
        "<HW-ATTRIBUTE-LITERALS>"
        "<HW-ATTRIBUTE-LITERAL-DEF><SHORT-NAME>LITERAL_1</SHORT-NAME></HW-ATTRIBUTE-LITERAL-DEF>"
        "<HW-ATTRIBUTE-LITERAL-DEF><SHORT-NAME>LITERAL_2</SHORT-NAME></HW-ATTRIBUTE-LITERAL-DEF>"
        "</HW-ATTRIBUTE-LITERALS>"
        "<IS-REQUIRED>true</IS-REQUIRED>"
        "<UNIT-REF DEST='UNIT'>/Units/Length</UNIT-REF>"
        "</HW-ATTRIBUTE-DEF>" % NS
    )


def test_parse_hw_attribute_def():
    attribute_def = HwAttributeDef(_MockParent(), "AttrDef1")
    root = ET.fromstring(_attribute_def_fragment())
    ARXMLParser().readHwAttributeDef(root, attribute_def)

    assert attribute_def.getShortName() == "AttrDef1"
    literals = attribute_def.getHwAttributeLiterals()
    assert [lit.getShortName() for lit in literals] == ["LITERAL_1", "LITERAL_2"]
    assert attribute_def.getIsRequired().getValue() is True
    assert attribute_def.getUnitRef().getValue() == "/Units/Length"
    assert attribute_def.getUnitRef().getDest() == "UNIT"


def test_parse_hw_attribute_def_empty():
    attribute_def = HwAttributeDef(_MockParent(), "EmptyDef")
    root = ET.fromstring("<HW-ATTRIBUTE-DEF xmlns='%s'><SHORT-NAME>EmptyDef</SHORT-NAME></HW-ATTRIBUTE-DEF>" % NS)
    ARXMLParser().readHwAttributeDef(root, attribute_def)

    assert attribute_def.getHwAttributeLiterals() == []
    assert attribute_def.getIsRequired() is None
    assert attribute_def.getUnitRef() is None
