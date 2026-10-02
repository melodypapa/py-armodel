"""Parser tests for the attribute-less string-param concretes (Tables 2.19/2.20/2.22).

Each concrete class serializes under its own ECUC-*-PARAM-DEF element and
inherits the ECUC-ABSTRACT-STRING-PARAM-DEF content (round-tripped there).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucFunctionNameDef, EcucMultilineStringParamDef, EcucStringParamDef

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestReadStringParamFamily:
    @pytest.mark.parametrize("cls,tag", [
        (EcucStringParamDef, "ECUC-STRING-PARAM-DEF"),
        (EcucMultilineStringParamDef, "ECUC-MULTILINE-STRING-PARAM-DEF"),
        (EcucFunctionNameDef, "ECUC-FUNCTION-NAME-DEF"),
    ])
    def test_read_inherited_fields(self, parser, cls, tag):
        param = cls(AUTOSAR.getInstance(), "Param")
        element = ET.fromstring(
            f"<{tag} xmlns='{NS}'>"
            "<SHORT-NAME>Param</SHORT-NAME>"
            f"<{tag}-VARIANTS><{tag}-CONDITIONAL><DEFAULT-VALUE>value</DEFAULT-VALUE></{tag}-CONDITIONAL></{tag}-VARIANTS>"
            f"</{tag}>"
        )
        reader = getattr(parser, {EcucStringParamDef: "readEcucStringParamDef", EcucMultilineStringParamDef: "readEcucMultilineStringParamDef", EcucFunctionNameDef: "readEcucFunctionNameDef"}[cls])
        reader(element, param)
        assert param.getShortName() == "Param"
        assert param.getDefaultValue().getValue() == "value"
