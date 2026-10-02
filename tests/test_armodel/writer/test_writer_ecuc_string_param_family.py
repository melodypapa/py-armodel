"""
Tests for writing the attribute-less string-param concretes (Tables
2.19/2.20/2.22, R23-11).

Each concrete class serializes under its own ECUC-*-PARAM-DEF wrapper and
delegates the inherited content to writeEcucAbstractStringParamDef.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_string_param_family.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucFunctionNameDef, EcucMultilineStringParamDef, EcucStringParamDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteStringParamFamily:
    @pytest.mark.parametrize("cls,tag", [
        (EcucStringParamDef, "ECUC-STRING-PARAM-DEF"),
        (EcucMultilineStringParamDef, "ECUC-MULTILINE-STRING-PARAM-DEF"),
        (EcucFunctionNameDef, "ECUC-FUNCTION-NAME-DEF"),
    ])
    def test_write_wrapper_and_inherited_content(self, cls, tag):
        param = cls(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Param1")
        param.setDefaultValue(VerbatimString().setValue("value"))

        parent = ET.Element("PARENT")
        writer = getattr(ARXMLWriter(), {EcucStringParamDef: "writeEcucStringParamDef", EcucMultilineStringParamDef: "writeEcucMultilineStringParamDef", EcucFunctionNameDef: "writeEcucFunctionNameDef"}[cls])
        writer(parent, param)

        child = parent.find(tag)
        assert child is not None
        assert child.find("SHORT-NAME").text == "Param1"
        conditional = child.find(f"{tag}-VARIANTS/{tag}-CONDITIONAL")
        assert conditional is not None
        assert conditional.find("DEFAULT-VALUE").text == "value"
