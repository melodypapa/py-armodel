"""Parser tests for the structural VARIATION-POINT element."""

import os

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator import (
    BlueprintGenerator,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    PostBuildVariantCriterion,
    PostBuildVariantCriterionValue,
    VariationPoint,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
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

    def test_read_identifiable_ignores_variation_point_on_non_capable(self, parser, caplog):
        """The parser gate ignores VARIATION-POINT on non-capable classes.

        A plain Identifiable (IDENTIFIABLE group carries no VARIATION-POINT and
        this probe adds no anchor) must not be populated; a warning is logged
        (constr_2638: no variation points in non-variant roles).
        """
        import logging

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        class Probe(Identifiable):
            pass

        inner = "<IDENTIFIABLE>" "<SHORT-NAME>Plain</SHORT-NAME>" "<VARIATION-POINT><SHORT-LABEL>VP_Plain</SHORT-LABEL></VARIATION-POINT>" "</IDENTIFIABLE>"
        element = _snip(inner).find("{%s}IDENTIFIABLE" % NS)

        probe = Probe(None, "Plain")
        with caplog.at_level(logging.WARNING, logger=parser.logger.name):
            parser.readIdentifiable(element, probe)

        assert getattr(probe, "variationPoint", None) is None
        assert not hasattr(probe, "setVariationPoint")
        assert any("VARIATION-POINT" in record.message for record in caplog.records)


class TestReadConditionByFormula:
    """Table 7.5 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.231): the
    <<atpMixedString>> content of ConditionByFormula is the formula expression."""

    def test_read_sw_syscond_reads_binding_time_and_mixed_text(self, parser):
        inner = "<VARIATION-POINT>" '<SW-SYSCOND BINDING-TIME="PRE-COMPILE-TIME">sysc == 1</SW-SYSCOND>' "</VARIATION-POINT>"
        vp_element = _snip(inner).find("{%s}VARIATION-POINT" % NS)

        vp = parser.readVariationPoint(vp_element, VariationPoint())

        sw_syscond = vp.getSwSyscond()
        assert isinstance(sw_syscond, ConditionByFormula)
        assert sw_syscond.getBindingTime().getValue() == "preCompileTime"
        assert sw_syscond.getMixedString() == "sysc == 1"

    def test_read_sw_syscond_without_text_leaves_text_none(self, parser):
        inner = "<VARIATION-POINT>" '<SW-SYSCOND BINDING-TIME="LINK-TIME"/>' "</VARIATION-POINT>"
        vp_element = _snip(inner).find("{%s}VARIATION-POINT" % NS)

        vp = parser.readVariationPoint(vp_element, VariationPoint())

        sw_syscond = vp.getSwSyscond()
        assert sw_syscond.getBindingTime().getValue() == "linkTime"
        assert sw_syscond.getMixedString() is None

    def test_read_condition_access_reads_mixed_text(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import (
            VariationPointProxy,
        )

        inner = "<VARIATION-POINT-PROXY>" '<CONDITION-ACCESS BINDING-TIME="SYSTEM-DESIGN-TIME">sysc &gt; 0</CONDITION-ACCESS>' "</VARIATION-POINT-PROXY>"
        element = _snip(inner).find("{%s}VARIATION-POINT-PROXY" % NS)

        proxy = VariationPointProxy(None, "vpp1")
        parser.readVariationPointProxy(element, proxy)

        condition_access = proxy.getConditionAccess()
        assert isinstance(condition_access, ConditionByFormula)
        assert condition_access.getBindingTime().getValue() == "systemDesignTime"
        assert condition_access.getMixedString() == "sysc > 0"


class TestReadPostBuildVariantCondition:
    """Table 7.6 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.232): the class's own
    readPostBuildVariantCondition helper (XSD group order MATCHING-CRITERION-REF,
    VALUE)."""

    def test_read_post_build_variant_condition_reads_fields(self, parser):
        inner = (
            "<POST-BUILD-VARIANT-CONDITION>"
            '<MATCHING-CRITERION-REF DEST="POST-BUILD-VARIANT-CRITERION">/Demo/Criterions/Country</MATCHING-CRITERION-REF>'
            "<VALUE>1</VALUE>"
            "</POST-BUILD-VARIANT-CONDITION>"
        )
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CONDITION" % NS)

        condition = parser.readPostBuildVariantCondition(element, PostBuildVariantCondition())

        ref = condition.getMatchingCriterionRef()
        assert ref.getValue() == "/Demo/Criterions/Country"
        assert ref.getDest() == "POST-BUILD-VARIANT-CRITERION"
        assert condition.getValue().getValue() == 1

    def test_read_empty_post_build_variant_condition_leaves_fields_none(self, parser):
        """An empty POST-BUILD-VARIANT-CONDITION (XSD minOccurs="0" for both children)
        parses to a condition with both fields left None."""
        inner = "<POST-BUILD-VARIANT-CONDITION/>"
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CONDITION" % NS)

        condition = parser.readPostBuildVariantCondition(element, PostBuildVariantCondition())

        assert condition.getMatchingCriterionRef() is None
        assert condition.getValue() is None

    def test_read_post_build_variant_condition_value_only(self, parser):
        """A condition carrying only VALUE (criterion ref absent) keeps both fields
        faithful: ref None, value read."""
        inner = "<POST-BUILD-VARIANT-CONDITION>" "<VALUE>7</VALUE>" "</POST-BUILD-VARIANT-CONDITION>"
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CONDITION" % NS)

        condition = parser.readPostBuildVariantCondition(element, PostBuildVariantCondition())

        assert condition.getMatchingCriterionRef() is None
        assert condition.getValue().getValue() == 7


class TestReadPostBuildVariantCriterion:
    """Table 7.63 (AUTOSAR_CP_TPS_SoftwareComponentTemplate, p.614): the class's own
    readPostBuildVariantCriterion helper plus the ARPackage.element dispatch
    (XSD 00052 group POST-BUILD-VARIANT-CRITERION: single COMPU-METHOD-REF,
    minOccurs="0")."""

    def test_read_post_build_variant_criterion_reads_compu_method_ref(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage

        inner = (
            "<POST-BUILD-VARIANT-CRITERION>"
            "<SHORT-NAME>Country</SHORT-NAME>"
            '<COMPU-METHOD-REF DEST="COMPU-METHOD">/Demo/CompuMethods/CountryEnum</COMPU-METHOD-REF>'
            "</POST-BUILD-VARIANT-CRITERION>"
        )
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CRITERION" % NS)

        criterion = PostBuildVariantCriterion(ARPackage(None, "Pkg"), "Country")
        parser.readPostBuildVariantCriterion(element, criterion)

        ref = criterion.getCompuMethodRef()
        assert ref.getValue() == "/Demo/CompuMethods/CountryEnum"
        assert ref.getDest() == "COMPU-METHOD"

    def test_read_empty_post_build_variant_criterion_leaves_ref_none(self, parser):
        """An empty POST-BUILD-VARIANT-CRITERION (XSD COMPU-METHOD-REF minOccurs="0")
        parses with the ref left None."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage

        inner = "<POST-BUILD-VARIANT-CRITERION>" "<SHORT-NAME>Country</SHORT-NAME>" "</POST-BUILD-VARIANT-CRITERION>"
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CRITERION" % NS)

        criterion = PostBuildVariantCriterion(ARPackage(None, "Pkg"), "Country")
        parser.readPostBuildVariantCriterion(element, criterion)

        assert criterion.getCompuMethodRef() is None

    def test_read_ar_package_dispatches_post_build_variant_criterion(self, parser):
        """readARPackageElements dispatches POST-BUILD-VARIANT-CRITERION through
        ARPackage.createPostBuildVariantCriterion and populates compuMethodRef."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage

        inner = (
            "<AR-PACKAGE>"
            "<SHORT-NAME>Criterions</SHORT-NAME>"
            "<ELEMENTS>"
            "<POST-BUILD-VARIANT-CRITERION>"
            "<SHORT-NAME>Country</SHORT-NAME>"
            '<COMPU-METHOD-REF DEST="COMPU-METHOD">/Demo/CompuMethods/CountryEnum</COMPU-METHOD-REF>'
            "</POST-BUILD-VARIANT-CRITERION>"
            "</ELEMENTS>"
            "</AR-PACKAGE>"
        )
        element = _snip(inner).find("{%s}AR-PACKAGE" % NS)

        pkg = ARPackage(None, "Criterions")
        parser.readARPackageElements(element, pkg)

        criterions = pkg.getPostBuildVariantCriterions()
        assert len(criterions) == 1
        assert criterions[0].getShortName() == "Country"
        assert criterions[0].getCompuMethodRef().getValue() == "/Demo/CompuMethods/CountryEnum"
        assert criterions[0].getCompuMethodRef().getDest() == "COMPU-METHOD"


class TestReadPostBuildVariantCriterionValue:
    """Table 7.27 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.259): the class's own
    readPostBuildVariantCriterionValue helper (XSD 00052 group POST-BUILD-VARIANT-CRITERION-VALUE,
    line 93322: VARIANT-CRITERION-REF, VALUE, ANNOTATIONS)."""

    def test_read_post_build_variant_criterion_value_reads_fields(self, parser):
        inner = (
            "<POST-BUILD-VARIANT-CRITERION-VALUE>"
            '<VARIANT-CRITERION-REF DEST="POST-BUILD-VARIANT-CRITERION">/Demo/Criterions/Country</VARIANT-CRITERION-REF>'
            "<VALUE>42</VALUE>"
            "<ANNOTATIONS>"
            "<ANNOTATION>"
            "<LABEL>"
            '<L-4 L="EN">Country is Germany</L-4>'
            "</LABEL>"
            "</ANNOTATION>"
            "</ANNOTATIONS>"
            "</POST-BUILD-VARIANT-CRITERION-VALUE>"
        )
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CRITERION-VALUE" % NS)

        value = parser.readPostBuildVariantCriterionValue(element, PostBuildVariantCriterionValue())

        ref = value.getVariantCriterionRef()
        assert ref.getValue() == "/Demo/Criterions/Country"
        assert ref.getDest() == "POST-BUILD-VARIANT-CRITERION"
        assert value.getValue().getValue() == 42
        annotations = value.getAnnotations()
        assert len(annotations) == 1
        assert isinstance(annotations[0], Annotation)
        assert annotations[0].getLabel().getL4s()[0].getValue() == "Country is Germany"

    def test_read_empty_post_build_variant_criterion_value_leaves_fields_empty(self, parser):
        """An empty POST-BUILD-VARIANT-CRITERION-VALUE (XSD minOccurs="0" for all three
        children) parses to a value object with all fields left empty."""
        inner = "<POST-BUILD-VARIANT-CRITERION-VALUE/>"
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CRITERION-VALUE" % NS)

        value = parser.readPostBuildVariantCriterionValue(element, PostBuildVariantCriterionValue())

        assert value.getVariantCriterionRef() is None
        assert value.getValue() is None
        assert value.getAnnotations() == []

    def test_read_post_build_variant_criterion_value_value_only(self, parser):
        """A criterion value carrying only VALUE (ref and annotations absent) keeps all
        fields faithful: ref None, value read, no annotations."""
        inner = "<POST-BUILD-VARIANT-CRITERION-VALUE>" "<VALUE>7</VALUE>" "</POST-BUILD-VARIANT-CRITERION-VALUE>"
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CRITERION-VALUE" % NS)

        value = parser.readPostBuildVariantCriterionValue(element, PostBuildVariantCriterionValue())

        assert value.getVariantCriterionRef() is None
        assert value.getValue().getValue() == 7
        assert value.getAnnotations() == []


class TestReadVariationPointProxy:
    def test_read_value_access(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints import (
            NumericalValueVariationPoint,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import (
            VariationPointProxy,
        )

        inner = "<VARIATION-POINT-PROXY>" "<SHORT-NAME>vpp1</SHORT-NAME>" "<VALUE-ACCESS>" "<NUMERICAL-VALUE-VARIATION-POINT/>" "</VALUE-ACCESS>" "</VARIATION-POINT-PROXY>"
        element = _snip(inner).find("{%s}VARIATION-POINT-PROXY" % NS)

        proxy = VariationPointProxy(None, "vpp1")
        parser.readVariationPointProxy(element, proxy)

        value_access = proxy.getValueAccess()
        assert isinstance(value_access, NumericalValueVariationPoint)

    def test_read_value_access_attributes_and_text(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints import (
            NumericalValueVariationPoint,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import (
            VariationPointProxy,
        )

        inner = (
            "<VARIATION-POINT-PROXY>"
            "<SHORT-NAME>vpp1</SHORT-NAME>"
            "<VALUE-ACCESS>"
            '<NUMERICAL-VALUE-VARIATION-POINT BINDING-TIME="PRE-COMPILE-TIME" SD="sd-1" SHORT-LABEL="vp1" BLUEPRINT-VALUE="bp">123</NUMERICAL-VALUE-VARIATION-POINT>'
            "</VALUE-ACCESS>"
            "</VARIATION-POINT-PROXY>"
        )
        element = _snip(inner).find("{%s}VARIATION-POINT-PROXY" % NS)

        proxy = VariationPointProxy(None, "vpp1")
        parser.readVariationPointProxy(element, proxy)

        value_access = proxy.getValueAccess()
        assert isinstance(value_access, NumericalValueVariationPoint)
        assert value_access.getBindingTime().getValue() == "preCompileTime"
        assert value_access.getSd().getValue() == "sd-1"
        assert value_access.getShortLabel().getValue() == "vp1"
        assert value_access.getBlueprintValue().getValue() == "bp"
        assert value_access.getText() == "123"

    def test_read_value_access_empty_wrapper(self, parser):
        """An empty VALUE-ACCESS wrapper leaves valueAccess unset (None)."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import (
            VariationPointProxy,
        )

        inner = "<VARIATION-POINT-PROXY>" "<SHORT-NAME>vpp3</SHORT-NAME>" "<VALUE-ACCESS/>" "</VARIATION-POINT-PROXY>"
        element = _snip(inner).find("{%s}VARIATION-POINT-PROXY" % NS)

        proxy = VariationPointProxy(None, "vpp3")
        parser.readVariationPointProxy(element, proxy)

        assert proxy.getValueAccess() is None

    def test_read_limit_value_access_with_interval_type(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints import (
            LimitValueVariationPoint,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import (
            VariationPointProxy,
        )

        inner = "<VARIATION-POINT-PROXY>" "<SHORT-NAME>vpp2</SHORT-NAME>" "<VALUE-ACCESS>" '<LIMIT INTERVAL-TYPE="CLOSED">42</LIMIT>' "</VALUE-ACCESS>" "</VARIATION-POINT-PROXY>"
        element = _snip(inner).find("{%s}VARIATION-POINT-PROXY" % NS)

        proxy = VariationPointProxy(None, "vpp2")
        parser.readVariationPointProxy(element, proxy)

        value_access = proxy.getValueAccess()
        assert isinstance(value_access, LimitValueVariationPoint)
        assert value_access.getIntervalType().getValue() == "closed"
        assert value_access.getText() == "42"


class TestReadVariationPointSpecAttributes:
    """Table 7.4 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.226): readVariationPoint
    populates all seven spec attributes (XSD 00052 group VARIATION-POINT, line 130012:
    SHORT-LABEL, DESC, BLUEPRINT-CONDITION, [FORMAL-BLUEPRINT-CONDITION removed],
    FORMAL-BLUEPRINT-GENERATOR, SW-SYSCOND, POST-BUILD-VARIANT-CONDITIONS, SDG)."""

    def test_read_all_seven_spec_attributes(self, parser):
        inner = (
            "<VARIATION-POINT>"
            "<SHORT-LABEL>VP_All</SHORT-LABEL>"
            "<DESC>"
            '<L-2 L="EN">Short purpose text</L-2>'
            "</DESC>"
            "<BLUEPRINT-CONDITION>"
            "<P>"
            '<L-1 L="EN">Resolve the derivation manually.</L-1>'
            "</P>"
            "</BLUEPRINT-CONDITION>"
            '<FORMAL-BLUEPRINT-GENERATOR><EXPRESSION>LET Name = "Example";</EXPRESSION></FORMAL-BLUEPRINT-GENERATOR>'
            '<SW-SYSCOND BINDING-TIME="PRE-COMPILE-TIME">sysc == 1</SW-SYSCOND>'
            "<POST-BUILD-VARIANT-CONDITIONS>"
            "<POST-BUILD-VARIANT-CONDITION>"
            '<MATCHING-CRITERION-REF DEST="POST-BUILD-VARIANT-CRITERION">/Demo/Criterions/Country</MATCHING-CRITERION-REF>'
            "<VALUE>1</VALUE>"
            "</POST-BUILD-VARIANT-CONDITION>"
            "</POST-BUILD-VARIANT-CONDITIONS>"
            '<SDG GID="SDG_TOOL">'
            '<SD GID="TOOL-ID">Tool X</SD>'
            "</SDG>"
            "</VARIATION-POINT>"
        )
        vp_element = _snip(inner).find("{%s}VARIATION-POINT" % NS)

        vp = parser.readVariationPoint(vp_element, VariationPoint())

        assert vp.getShortLabel().getValue() == "VP_All"

        desc = vp.getDesc()
        assert isinstance(desc, MultiLanguageOverviewParagraph)
        assert desc.getL2s()[0].getValue() == "Short purpose text"
        assert desc.getL2s()[0].getL() == "EN"

        blueprint_condition = vp.getBlueprintCondition()
        assert isinstance(blueprint_condition, DocumentationBlock)
        assert blueprint_condition.getPs()[0].getL1s()[0].getValue() == "Resolve the derivation manually."

        generator = vp.getFormalBlueprintGenerator()
        assert isinstance(generator, BlueprintGenerator)
        assert generator.getExpression().getValue() == 'LET Name = "Example";'

        sw_syscond = vp.getSwSyscond()
        assert isinstance(sw_syscond, ConditionByFormula)
        assert sw_syscond.getBindingTime().getValue() == "preCompileTime"
        assert sw_syscond.getMixedString() == "sysc == 1"

        conditions = vp.getPostBuildVariantConditions()
        assert len(conditions) == 1
        assert conditions[0].getMatchingCriterionRef().getValue() == "/Demo/Criterions/Country"
        assert conditions[0].getValue().getValue() == 1

        sdg = vp.getSdg()
        assert isinstance(sdg, Sdg)
        assert sdg.getGID().getValue() == "SDG_TOOL"

    def test_read_empty_post_build_variant_conditions_wrapper(self, parser):
        """An empty POST-BUILD-VARIANT-CONDITIONS wrapper (XSD choice
        minOccurs="0") parses to no conditions."""
        inner = "<VARIATION-POINT>" "<POST-BUILD-VARIANT-CONDITIONS/>" "</VARIATION-POINT>"
        vp_element = _snip(inner).find("{%s}VARIATION-POINT" % NS)

        vp = parser.readVariationPoint(vp_element, VariationPoint())

        assert vp.getPostBuildVariantConditions() == []


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

        # Criterion element's own variation point also survives: the criterion is
        # an ARElement in the ARPackage.element role (atpVariation, GST Table 4.1),
        # so its VARIATION-POINT is schema-conformant via the PACKAGEABLE-ELEMENT
        # group anchor.
        criterion2 = document2.find("/Demo/Criterions/Country")
        assert criterion2.getVariationPoint().getShortLabel().getValue() == "VP_Country"
