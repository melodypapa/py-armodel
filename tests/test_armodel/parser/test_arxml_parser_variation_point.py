"""Parser tests for the structural VARIATION-POINT element."""

import os

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    PostBuildVariantCriterion,
    VariationPoint,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter
from tests.test_armodel.parser._helpers import _snip

NS = "http://autosar.org/schema/r4.0"

VARIATION_POINT_ARXML = os.path.join(os.path.dirname(__file__), "data", "VariationPoint.arxml")


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
            '<SW-SYSCOND BINDING-TIME="CODE-GENERATION-TIME">'
            'defined(<SYSC-REF DEST="SW-SYSTEMCONST">/Demo/SystemConstants/SY_TURBO</SYSC-REF>)'
            ' &amp;&amp; <SYSC-STRING-REF DEST="SW-SYSTEMCONST">/Demo/SystemConstants/SY_MODE</SYSC-STRING-REF> == 0'
            "</SW-SYSCOND>"
            "<POST-BUILD-VARIANT-CONDITIONS>"
            "<POST-BUILD-VARIANT-CONDITION>"
            '<MATCHING-CRITERION-REF DEST="POST-BUILD-VARIANT-CRITERION">/Demo/Criterions/Country</MATCHING-CRITERION-REF>'
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
            '<COMPU-METHOD-REF DEST="COMPU-METHOD">/Demo/CompuMethods/CountryEnum</COMPU-METHOD-REF>'
            "<VARIATION-POINT><SHORT-LABEL>VP_Country</SHORT-LABEL></VARIATION-POINT>"
            "</POST-BUILD-VARIANT-CRITERION>"
        )
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CRITERION" % NS)

        criterion = PostBuildVariantCriterion(ARPackage(None, "Pkg"), "Country")
        parser.readIdentifiable(element, criterion)

        vp = criterion.getVariationPoint()
        assert vp is not None
        assert vp.getShortLabel().getValue() == "VP_Country"


@pytest.mark.integration
class TestVariationPointRoundTrip:
    def test_parse_write_reparse_preserves_variation_point(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.new()
        document.setARRelease("R23-11")
        parser = ARXMLParser()
        parser.load(VARIATION_POINT_ARXML, document)

        swc = document.find("/Demo/SwComponents/MySWC")
        behavior = swc.getInternalBehavior()

        vp = behavior.getVariationPoint()
        assert vp is not None
        assert vp.getShortLabel().getValue() == "VP1"
        assert vp.getSwSyscond().getBindingTime().getValue() == "codeGenerationTime"
        conditions = vp.getPostBuildVariantConditions()
        assert conditions[0].getMatchingCriterionRef().getValue() == "/Demo/Criterions/Country"

        output = str(tmp_path / "VariationPoint_roundtrip.arxml")
        writer = ARXMLWriter()
        writer.save(output, document)

        document2 = AUTOSAR.getInstance()
        document2.new()
        document2.setARRelease("R23-11")
        parser2 = ARXMLParser()
        parser2.load(output, document2)

        swc2 = document2.find("/Demo/SwComponents/MySWC")
        behavior2 = swc2.getInternalBehavior()

        vp2 = behavior2.getVariationPoint()
        assert vp2 is not None
        assert vp2.getShortLabel().getValue() == "VP1"
        assert vp2.getSwSyscond().getBindingTime().getValue() == "codeGenerationTime"
        conditions2 = vp2.getPostBuildVariantConditions()
        assert conditions2[0].getMatchingCriterionRef().getValue() == "/Demo/Criterions/Country"
        assert conditions2[0].getValue().getValue() == 1

        # Criterion element's own variation point also survives
        criterion2 = document2.find("/Demo/Criterions/Country")
        assert criterion2.getVariationPoint().getShortLabel().getValue() == "VP_Country"
