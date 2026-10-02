"""Parser tests for EcucEnumerationParamDef (2.23), EcucEnumerationLiteralDef (2.24)
and EcucAddInfoParamDef (2.25).

Element orders (XSD groups): ECUC-ENUMERATION-PARAM-DEF → DEFAULT-VALUE,
LITERALS; ECUC-ENUMERATION-LITERAL-DEF → ECUC-COND, ORIGIN;
ECUC-ADD-INFO-PARAM-DEF → parameter-def content only (no own attrs).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAddInfoParamDef, EcucEnumerationLiteralDef, EcucEnumerationParamDef

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str) -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucEnumerationParamDef:
    def test_read_sets_all_fields(self, parser):
        param = EcucEnumerationParamDef(AUTOSAR.getInstance(), "Param")
        element = _snip(
            "<SHORT-NAME>Param</SHORT-NAME>"
            "<DEFAULT-VALUE>LITERAL_1</DEFAULT-VALUE>"
            "<LITERALS>"
            "<ECUC-ENUMERATION-LITERAL-DEF><SHORT-NAME>Literal1</SHORT-NAME></ECUC-ENUMERATION-LITERAL-DEF>"
            "</LITERALS>",
            "ECUC-ENUMERATION-PARAM-DEF",
        )
        parser.readEcucEnumerationParamDef(element, param)
        assert param.getDefaultValue().getValue() == "LITERAL_1"
        literals = param.getLiterals()
        assert len(literals) == 1
        assert isinstance(literals[0], EcucEnumerationLiteralDef)
        assert literals[0].getShortName() == "Literal1"

    def test_read_empty(self, parser):
        param = EcucEnumerationParamDef(AUTOSAR.getInstance(), "Param")
        element = _snip("", "ECUC-ENUMERATION-PARAM-DEF")
        parser.readEcucEnumerationParamDef(element, param)
        assert param.getDefaultValue() is None
        assert param.getLiterals() == []


class TestReadEcucEnumerationLiteralDef:
    def test_read_sets_all_fields(self, parser):
        literal = EcucEnumerationLiteralDef(AUTOSAR.getInstance(), "Literal")
        element = _snip(
            "<SHORT-NAME>Literal</SHORT-NAME>"
            "<ORIGIN>AUTOSAR Ecuc Definition Collection</ORIGIN>",
            "ECUC-ENUMERATION-LITERAL-DEF",
        )
        parser.readEcucEnumerationLiteral(element, literal)
        assert literal.getShortName() == "Literal"
        assert literal.getOrigin().getValue() == "AUTOSAR Ecuc Definition Collection"

    def test_read_empty(self, parser):
        literal = EcucEnumerationLiteralDef(AUTOSAR.getInstance(), "Literal")
        element = _snip("", "ECUC-ENUMERATION-LITERAL-DEF")
        parser.readEcucEnumerationLiteral(element, literal)
        assert literal.getEcucCond() is None
        assert literal.getOrigin() is None


class TestReadEcucAddInfoParamDef:
    def test_read(self, parser):
        param = EcucAddInfoParamDef(AUTOSAR.getInstance(), "Param")
        element = _snip("<SHORT-NAME>Param</SHORT-NAME>", "ECUC-ADD-INFO-PARAM-DEF")
        parser.readEcucAddInfoParamDef(element, param)
        assert param.getShortName() == "Param"
        assert param.getSymbolicNameValue() is None
