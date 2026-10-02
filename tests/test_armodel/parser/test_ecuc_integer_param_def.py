"""Parser tests for EcucIntegerParamDef (Table 2.16, p.60).

Element order (XSD group ECUC-INTEGER-PARAM-DEF): DEFAULT-VALUE, MAX, MIN.
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


class TestReadEcucIntegerParamDef:
    def test_read_sets_all_fields(self, parser):
        param = EcucIntegerParamDef(AUTOSAR.getInstance(), "Param")
        element = _snip("<SHORT-NAME>Param</SHORT-NAME><DEFAULT-VALUE>10</DEFAULT-VALUE><MAX>100</MAX><MIN>1</MIN>")
        parser.readEcucIntegerParamDef(element, param)
        assert param.getDefaultValue().getValue() == 10
        assert param.getMax().getValue() == 100
        assert param.getMin().getValue() == 1

    def test_read_empty(self, parser):
        param = EcucIntegerParamDef(AUTOSAR.getInstance(), "Param")
        element = _snip("")
        parser.readEcucIntegerParamDef(element, param)
        assert param.getDefaultValue() is None
        assert param.getMax() is None
        assert param.getMin() is None
