"""Writer tests for the structural VARIATION-POINT element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator.BlueprintGenerator import (
    BlueprintGenerator,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
    RefType,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    PostBuildVariantCriterion,
    VariationPoint,
)
from armodel.writer.arxml_writer import ARXMLWriter


def _write_vp_to_element(vp: VariationPoint) -> ET.Element:
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    writer = ARXMLWriter()
    element = ET.Element("PARENT")
    writer.writeVariationPoint(element, vp)
    return element


class TestWriteVariationPoint:
    def test_write_minimal(self):
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("VP1"))

        element = _write_vp_to_element(vp)

        vp_element = element.find("VARIATION-POINT")
        assert vp_element is not None
        assert vp_element.find("SHORT-LABEL").text == "VP1"

    def test_write_full_roundtrip_content(self):
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("VP_Turbo"))

        syscond = ConditionByFormula()
        syscond.setBindingTime(BindingTimeEnum().setValue("codeGenerationTime"))
        syscond.addFormulaText("defined(")
        syscond.addFormulaRef(RefType().setValue("/Demo/SystemConstants/SY_TURBO").setDest("SW-SYSTEMCONST"))
        syscond.addFormulaText(")")
        vp.setSwSyscond(syscond)

        condition = PostBuildVariantCondition()
        condition.setMatchingCriterionRef(RefType().setValue("/Demo/Criterions/Country").setDest("POST-BUILD-VARIANT-CRITERION"))
        condition.setValue(Integer().setValue("1"))
        vp.addPostBuildVariantCondition(condition)

        generator = BlueprintGenerator()
        generator.setExpression(VerbatimString().setValue('LET Name = "Example";'))
        vp.setFormalBlueprintGenerator(generator)

        element = _write_vp_to_element(vp)

        vp_element = element.find("VARIATION-POINT")

        # XSD sequence order: SHORT-LABEL, DESC, BLUEPRINT-CONDITION,
        # FORMAL-BLUEPRINT-GENERATOR, SW-SYSCOND, POST-BUILD-VARIANT-CONDITIONS, SDG
        child_tags = [child.tag for child in vp_element]
        assert child_tags.index("SHORT-LABEL") < child_tags.index("SW-SYSCOND")
        assert child_tags.index("SW-SYSCOND") < child_tags.index("POST-BUILD-VARIANT-CONDITIONS")
        assert child_tags.index("FORMAL-BLUEPRINT-GENERATOR") < child_tags.index("SW-SYSCOND")
        assert vp_element.find("SHORT-LABEL").text == "VP_Turbo"

        syscond_element = vp_element.find("SW-SYSCOND")
        assert syscond_element is not None
        assert syscond_element.attrib["BINDING-TIME"] == "CODE-GENERATION-TIME"
        assert syscond_element.text == "defined("
        refs = syscond_element.findall("SYSC-REF")
        assert len(refs) == 1
        assert refs[0].attrib["DEST"] == "SW-SYSTEMCONST"
        assert refs[0].text == "/Demo/SystemConstants/SY_TURBO"
        assert refs[0].tail == ")"

        conditions_wrapper = vp_element.find("POST-BUILD-VARIANT-CONDITIONS")
        condition_element = conditions_wrapper.find("POST-BUILD-VARIANT-CONDITION")
        ref_element = condition_element.find("MATCHING-CRITERION-REF")
        assert ref_element.text == "/Demo/Criterions/Country"
        assert ref_element.attrib["DEST"] == "POST-BUILD-VARIANT-CRITERION"
        assert condition_element.find("VALUE").text == "1"

        # XSD BLUEPRINT-GENERATOR sequence: INTRODUCTION before EXPRESSION
        formal = vp_element.find("FORMAL-BLUEPRINT-GENERATOR")
        formal_tags = [child.tag for child in formal]
        assert formal_tags == ["EXPRESSION"]
        assert formal.find("EXPRESSION").text == 'LET Name = "Example";'

    def test_write_none_creates_no_element(self):
        vp = None

        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        writer = ARXMLWriter()
        element = ET.Element("PARENT")
        writer.writeVariationPoint(element, vp)

        assert element.find("VARIATION-POINT") is None

    def test_write_identifiable_emits_variation_point(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")

        criterion = PostBuildVariantCriterion(document, "Country")
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("VP_Country"))
        criterion.setVariationPoint(vp)

        writer = ARXMLWriter()
        element = ET.Element("POST-BUILD-VARIANT-CRITERION")
        writer.writeIdentifiable(element, criterion)

        vp_element = element.find("VARIATION-POINT")
        assert vp_element is not None
        assert vp_element.find("SHORT-LABEL").text == "VP_Country"
