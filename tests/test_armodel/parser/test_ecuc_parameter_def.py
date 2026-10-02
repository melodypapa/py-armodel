"""Parser tests for EcucParameterDef (Table 2.14, p.57, abstract — via concrete subclass).

Element order (XSD group ECUC-PARAMETER-DEF): DERIVATION, SYMBOLIC-NAME-VALUE,
WITH-AUTO (on top of the ECUC-COMMON-ATTRIBUTES group).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucIntegerParamDef

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-INTEGER-PARAM-DEF") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucParameterDef:
    def test_read_sets_all_fields(self, parser):
        param = EcucIntegerParamDef(AUTOSAR.getInstance(), "Param")
        element = _snip(
            "<SHORT-NAME>Param</SHORT-NAME>"
            "<DERIVATION><CALCULATION-FORMULA/></DERIVATION>"
            "<SYMBOLIC-NAME-VALUE>true</SYMBOLIC-NAME-VALUE>"
            "<WITH-AUTO>false</WITH-AUTO>"
        )
        parser.readEcucParameterDef(element, param)
        assert param.getDerivation() is not None
        assert param.getSymbolicNameValue().getValue() is True
        assert param.getWithAuto().getValue() is False

    def test_read_empty(self, parser):
        param = EcucIntegerParamDef(AUTOSAR.getInstance(), "Param")
        element = _snip("")
        parser.readEcucParameterDef(element, param)
        assert param.getDerivation() is None
        assert param.getSymbolicNameValue() is None
        assert param.getWithAuto() is None
