"""Parser tests for HwAttributeLiteralDef (AUTOSAR_CP_TPS_ECUResourceTemplate, Table 2.14, p.26).

The reader helper is exercised directly on a HW-ATTRIBUTE-LITERAL-DEF fragment;
per Table 2.14 (attribute row '-') and the XSD group HW-ATTRIBUTE-LITERAL-DEF
(AUTOSAR_00052.xsd l.65637, empty sequence) the class carries no own attributes
beyond the Identifiable chain.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeLiteralDef
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


def _literal_def_fragment():
    return "<HW-ATTRIBUTE-LITERAL-DEF xmlns='%s'>" "<SHORT-NAME>LITERAL_1</SHORT-NAME>" "<CATEGORY>STD</CATEGORY>" "</HW-ATTRIBUTE-LITERAL-DEF>" % NS


def test_parse_hw_attribute_literal_def():
    literal_def = HwAttributeLiteralDef(_MockParent(), "LITERAL_1")
    root = ET.fromstring(_literal_def_fragment())
    ARXMLParser().readHwAttributeLiteralDef(root, literal_def)

    assert literal_def.getShortName() == "LITERAL_1"
    assert literal_def.getCategory().getValue() == "STD"


def test_parse_hw_attribute_literal_def_ignores_legacy_value_element():
    """VALUE is not part of the HW-ATTRIBUTE-LITERAL-DEF group (Table 2.14 row '-') — no own attribute absorbs it."""
    literal_def = HwAttributeLiteralDef(_MockParent(), "LITERAL_1")
    root = ET.fromstring("<HW-ATTRIBUTE-LITERAL-DEF xmlns='%s'><SHORT-NAME>LITERAL_1</SHORT-NAME><VALUE>1</VALUE></HW-ATTRIBUTE-LITERAL-DEF>" % NS)
    ARXMLParser().readHwAttributeLiteralDef(root, literal_def)

    assert literal_def.getShortName() == "LITERAL_1"
    assert not hasattr(literal_def, "value")
