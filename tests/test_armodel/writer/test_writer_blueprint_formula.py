"""Writer tests for the BlueprintFormula element (BLUEPRINT-FORMULA).

Spec: R23-11 AUTOSAR_FO_TPS_StandardizationTemplate, Table C.16, p.163
(appendix C caption-shift: the body renders above the caption). XSD 00052 group
BLUEPRINT-FORMULA (line 9023): choice ECUC-REF / VERBATIM (+ the inherited
SW-SYSTEMCONST-DEPENDENT-FORMULA choice SYSC-STRING-REF / SYSC-REF); mixed="true".

NOTE: the sole consuming element VariationPoint.formalBlueprintCondition
(FORMAL-BLUEPRINT-CONDITION, XSD line 130040) is atp.Status="removed" in R23-11
and is deliberately not dispatched by writeVariationPoint — this helper is pinned
at element level (PostBuildVariantCriterionValue precedent).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintFormula import (
    BlueprintFormula,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LVerbatim
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageVerbatim
from armodel.writer.arxml_writer import ARXMLWriter


def _build_verbatim(text: str) -> MultiLanguageVerbatim:
    l5 = LVerbatim()
    l5.setL("EN")
    l5.setValue(text)
    return MultiLanguageVerbatim().addL5(l5)


class TestWriteBlueprintFormula:
    def test_write_full_ecuc_verbatim_sysc_and_text(self):
        formula = BlueprintFormula()
        formula.setMixedString("defined(&) informal term")
        formula.setEcucRef(RefType().setValue("/EcucDefs/MyModule").setDest("ECUC-MODULE-DEF"))
        formula.setVerbatim(_build_verbatim("max(3, x)"))
        formula.setSyscRef(RefType().setValue("/SystemConstants/MyConst").setDest("SW-SYSTEMCONST"))

        element = ET.Element("PARENT")
        ARXMLWriter().writeBlueprintFormula(element, formula)

        written = element.find("BLUEPRINT-FORMULA")
        assert written is not None
        assert written.text == "defined(&) informal term"
        ecuc_ref = written.find("ECUC-REF")
        assert ecuc_ref is not None
        assert ecuc_ref.text == "/EcucDefs/MyModule"
        assert ecuc_ref.attrib["DEST"] == "ECUC-MODULE-DEF"
        l5 = written.find("VERBATIM/L-5")
        assert l5 is not None
        assert l5.attrib["L"] == "EN"
        assert l5.text == "max(3, x)"
        sysc_ref = written.find("SYSC-REF")
        assert sysc_ref is not None
        assert sysc_ref.text == "/SystemConstants/MyConst"
        assert sysc_ref.attrib["DEST"] == "SW-SYSTEMCONST"

    def test_write_ecuc_ref_only_omits_verbatim_and_sysc(self):
        formula = BlueprintFormula()
        formula.setEcucRef(RefType().setValue("/EcucDefs/MyModule/MyParam").setDest("ECUC-PARAMETER-DEF"))

        element = ET.Element("PARENT")
        ARXMLWriter().writeBlueprintFormula(element, formula)

        written = element.find("BLUEPRINT-FORMULA")
        assert written is not None
        assert written.find("ECUC-REF").text == "/EcucDefs/MyModule/MyParam"
        assert written.find("VERBATIM") is None
        assert written.find("SYSC-REF") is None
        assert written.find("SYSC-STRING-REF") is None

    def test_write_empty_formula_emits_bare_element(self):
        element = ET.Element("PARENT")
        ARXMLWriter().writeBlueprintFormula(element, BlueprintFormula())

        written = element.find("BLUEPRINT-FORMULA")
        assert written is not None
        assert len(written) == 0
        assert written.text is None

    def test_write_none_formula_emits_no_element(self):
        element = ET.Element("PARENT")
        ARXMLWriter().writeBlueprintFormula(element, None)

        assert element.find("BLUEPRINT-FORMULA") is None
