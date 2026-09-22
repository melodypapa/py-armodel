"""Writer round-trip tests for HwAttributeLiteralDef (AUTOSAR_CP_TPS_ECUResourceTemplate, Table 2.14, p.26).

Per Table 2.14 (attribute row '-') and the XSD group HW-ATTRIBUTE-LITERAL-DEF
(AUTOSAR_00052.xsd l.65637, empty sequence) only the Identifiable chain is
emitted — no VALUE element.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeLiteralDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
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


def test_write_hw_attribute_literal_def_xml():
    parent = ET.Element("ROOT")
    ARXMLWriter().writeHwAttributeLiteralDef(parent, HwAttributeLiteralDef(_MockParent(), "LITERAL_1"))

    node = parent.find("HW-ATTRIBUTE-LITERAL-DEF")
    assert node is not None
    assert node.find("SHORT-NAME").text == "LITERAL_1"
    assert [child.tag for child in node] == ["SHORT-NAME"]


def test_round_trip_preserves_short_name():
    literal_def = HwAttributeLiteralDef(_MockParent(), "LITERAL_1")
    parent = ET.Element("ROOT")
    ARXMLWriter().writeHwAttributeLiteralDef(parent, literal_def)
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

    parsed = HwAttributeLiteralDef(_MockParent(), "LITERAL_1")
    ARXMLParser().readHwAttributeLiteralDef(root[0][0], parsed)

    assert parsed.getShortName() == "LITERAL_1"
    assert not hasattr(parsed, "value")
