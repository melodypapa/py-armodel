"""Parser tests for the structural VARIATION-POINT element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    PostBuildVariantCriterion,
    VariationPoint,
)
from tests.test_armodel.parser._helpers import _snip

NS = "http://autosar.org/schema/r4.0"


class TestReadVariationPoint:
    def test_read_variation_point_minimal(self, parser):
        element = _snip("<VARIATION-POINT><SHORT-LABEL>VP1</SHORT-LABEL></VARIATION-POINT>")
        vp_element = element.find("{%s}VARIATION-POINT" % NS)

        vp = parser.readVariationPoint(vp_element, VariationPoint())

        assert vp is not None
        assert vp.getShortLabel().getValue() == "VP1"
        assert vp.getSwSyscond() is None
        assert vp.getPostBuildVariantConditions() == []

    def test_read_variation_point_full(self, parser):
        inner = (
            "<VARIATION-POINT>"
            "<SHORT-LABEL>VP_Turbo</SHORT-LABEL>"
            "<SW-SYSCOND BINDING-TIME=\"CODE-GENERATION-TIME\">"
            "defined(<SYSC-REF DEST=\"SW-SYSTEMCONST\">/Demo/SystemConstants/SY_TURBO</SYSC-REF>)"
            " &amp;&amp; <SYSC-STRING-REF DEST=\"SW-SYSTEMCONST\">/Demo/SystemConstants/SY_MODE</SYSC-STRING-REF> == 0"
            "</SW-SYSCOND>"
            "<POST-BUILD-VARIANT-CONDITIONS>"
            "<POST-BUILD-VARIANT-CONDITION>"
            "<MATCHING-CRITERION-REF DEST=\"POST-BUILD-VARIANT-CRITERION\">/Demo/Criterions/Country</MATCHING-CRITERION-REF>"
            "<VALUE>1</VALUE>"
            "</POST-BUILD-VARIANT-CONDITION>"
            "</POST-BUILD-VARIANT-CONDITIONS>"
            "</VARIATION-POINT>"
        )
        vp_element = _snip(inner).find("{%s}VARIATION-POINT" % NS)

        vp = parser.readVariationPoint(vp_element, VariationPoint())

        sw_syscond = vp.getSwSyscond()
        assert isinstance(sw_syscond, ConditionByFormula)
        assert sw_syscond.getBindingTime().getValue() == "codeGenerationTime"
        items = sw_syscond.getFormulaItems()
        assert items[0] == "defined("
        assert items[1][0] == "SYSC-REF"
        assert items[1][1].getValue() == "/Demo/SystemConstants/SY_TURBO"
        assert items[1][1].getDest() == "SW-SYSTEMCONST"
        assert items[2] == ") && "
        assert items[3][0] == "SYSC-STRING-REF"
        assert items[3][1].getValue() == "/Demo/SystemConstants/SY_MODE"
        assert items[4] == " == 0"

        conditions = vp.getPostBuildVariantConditions()
        assert len(conditions) == 1
        assert isinstance(conditions[0], PostBuildVariantCondition)
        assert conditions[0].getMatchingCriterionRef().getValue() == "/Demo/Criterions/Country"
        assert conditions[0].getMatchingCriterionRef().getDest() == "POST-BUILD-VARIANT-CRITERION"
        assert conditions[0].getValue().getValue() == 1

    def test_read_identifiable_picks_up_variation_point(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage

        inner = (
            "<POST-BUILD-VARIANT-CRITERION>"
            "<SHORT-NAME>Country</SHORT-NAME>"
            "<COMPU-METHOD-REF DEST=\"COMPU-METHOD\">/Demo/CompuMethods/CountryEnum</COMPU-METHOD-REF>"
            "<VARIATION-POINT><SHORT-LABEL>VP_Country</SHORT-LABEL></VARIATION-POINT>"
            "</POST-BUILD-VARIANT-CRITERION>"
        )
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CRITERION" % NS)

        criterion = PostBuildVariantCriterion(ARPackage(None, "Pkg"), "Country")
        parser.readIdentifiable(element, criterion)

        vp = criterion.getVariationPoint()
        assert vp is not None
        assert vp.getShortLabel().getValue() == "VP_Country"
