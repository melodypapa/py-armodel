"""Parser tests for EcucAbstractStringParamDef (Table 2.18, p.63, abstract — via concrete subclass).

Element order (XSD group ECUC-ABSTRACT-STRING-PARAM-DEF): DEFAULT-VALUE,
MAX-LENGTH, MIN-LENGTH, REGULAR-EXPRESSION.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucStringParamDef

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-STRING-PARAM-DEF") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucAbstractStringParamDef:
    def _make_obj(self):
        return EcucStringParamDef(AUTOSAR.getInstance(), "Param")

    def test_read_sets_all_fields(self, parser):
        param = self._make_obj()
        element = _snip(
            "<SHORT-NAME>Param</SHORT-NAME>"
            "<DEFAULT-VALUE>default</DEFAULT-VALUE>"
            "<MAX-LENGTH>32</MAX-LENGTH>"
            "<MIN-LENGTH>1</MIN-LENGTH>"
            "<REGULAR-EXPRESSION>[a-z]+</REGULAR-EXPRESSION>"
        )
        parser.readEcucAbstractStringParamDef(element, param)
        assert param.getDefaultValue().getValue() == "default"
        assert param.getMaxLength().getValue() == 32
        assert param.getMinLength().getValue() == 1
        assert param.getRegularExpression().getValue() == "[a-z]+"

    def test_read_empty(self, parser):
        param = self._make_obj()
        element = _snip("")
        parser.readEcucAbstractStringParamDef(element, param)
        assert param.getDefaultValue() is None
        assert param.getMaxLength() is None
        assert param.getMinLength() is None
        assert param.getRegularExpression() is None
