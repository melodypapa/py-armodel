"""Writer tests for the structural VARIATION-POINT element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator import (
    BlueprintGenerator,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
    IntervalTypeEnum,
    PrimitiveIdentifier,
    RefType,
    String,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    VariationPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints import (
    LimitValueVariationPoint,
    NumericalValueVariationPoint,
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

        pkg = document.createARPackage("AUTOSAR")
        component = pkg.createApplicationSwComponentType("Component")
        port = component.createPRPortPrototype("Country")
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("VP_Country"))
        port.setVariationPoint(vp)

        writer = ARXMLWriter()
        element = ET.Element("PR-PORT-PROTOTYPE")
        writer.writeIdentifiable(element, port)

        vp_element = element.find("VARIATION-POINT")
        assert vp_element is not None
        assert vp_element.find("SHORT-LABEL").text == "VP_Country"


class TestWritePostBuildVariantCondition:
    """Table 7.6 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.232): the class's own
    writePostBuildVariantCondition helper (XSD 00052 group POST-BUILD-VARIANT-CONDITION,
    line 93223: MATCHING-CRITERION-REF before VALUE)."""

    def test_write_post_build_variant_condition_element_order(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        writer = ARXMLWriter()

        condition = PostBuildVariantCondition()
        condition.setMatchingCriterionRef(RefType().setValue("/Demo/Criterions/Country").setDest("POST-BUILD-VARIANT-CRITERION"))
        condition.setValue(Integer().setValue("1"))

        element = ET.Element("PARENT")
        writer.writePostBuildVariantCondition(element, condition)

        condition_element = element.find("POST-BUILD-VARIANT-CONDITION")
        assert condition_element is not None
        child_tags = [child.tag for child in condition_element]
        assert child_tags == ["MATCHING-CRITERION-REF", "VALUE"]
        ref_element = condition_element.find("MATCHING-CRITERION-REF")
        assert ref_element.text == "/Demo/Criterions/Country"
        assert ref_element.attrib["DEST"] == "POST-BUILD-VARIANT-CRITERION"
        assert condition_element.find("VALUE").text == "1"

    def test_write_empty_post_build_variant_condition_emits_bare_element(self):
        """A condition with no fields set writes a bare POST-BUILD-VARIANT-CONDITION
        without children (writer tolerates the empty form its reader must accept)."""
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        writer = ARXMLWriter()

        element = ET.Element("PARENT")
        writer.writePostBuildVariantCondition(element, PostBuildVariantCondition())

        condition_element = element.find("POST-BUILD-VARIANT-CONDITION")
        assert condition_element is not None
        assert len(condition_element) == 0


class TestWritePostBuildVariantCriterion:
    """Table 7.63 (AUTOSAR_CP_TPS_SoftwareComponentTemplate, p.614): the class's own
    writePostBuildVariantCriterion helper (XSD 00052 complexType POST-BUILD-VARIANT-CRITERION,
    line 93296: the own group's COMPU-METHOD-REF follows all base element groups)."""

    def test_write_post_build_variant_criterion_writes_compu_method_ref(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCriterion

        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        writer = ARXMLWriter()

        criterion = PostBuildVariantCriterion(ARPackage(None, "Pkg"), "Country")
        criterion.setCompuMethodRef(RefType().setValue("/Demo/CompuMethods/CountryEnum").setDest("COMPU-METHOD"))

        element = ET.Element("PARENT")
        writer.writePostBuildVariantCriterion(element, criterion)

        criterion_element = element.find("POST-BUILD-VARIANT-CRITERION")
        assert criterion_element is not None
        child_tags = [child.tag for child in criterion_element]
        assert child_tags[-1] == "COMPU-METHOD-REF"
        ref_element = criterion_element.find("COMPU-METHOD-REF")
        assert ref_element.text == "/Demo/CompuMethods/CountryEnum"
        assert ref_element.attrib["DEST"] == "COMPU-METHOD"
        assert criterion_element.find("SHORT-NAME").text == "Country"

    def test_write_post_build_variant_criterion_without_ref_omits_child(self):
        """A criterion with no compuMethodRef writes the element without a
        COMPU-METHOD-REF child (XSD minOccurs="0"; the empty form its reader accepts)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCriterion

        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        writer = ARXMLWriter()

        criterion = PostBuildVariantCriterion(ARPackage(None, "Pkg"), "Country")

        element = ET.Element("PARENT")
        writer.writePostBuildVariantCriterion(element, criterion)

        criterion_element = element.find("POST-BUILD-VARIANT-CRITERION")
        assert criterion_element is not None
        assert criterion_element.find("COMPU-METHOD-REF") is None


class TestWriteConditionByFormula:
    """Table 7.5 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.231): the
    <<atpMixedString>> content of ConditionByFormula is the formula expression."""

    def test_write_sw_syscond_writes_binding_time_and_mixed_text(self):
        vp = VariationPoint()
        syscond = ConditionByFormula()
        syscond.setBindingTime(BindingTimeEnum().setValue("preCompileTime"))
        syscond.setText("sysc == 1")
        vp.setSwSyscond(syscond)

        element = _write_vp_to_element(vp)

        syscond_element = element.find("VARIATION-POINT").find("SW-SYSCOND")
        assert syscond_element is not None
        assert syscond_element.attrib["BINDING-TIME"] == "PRE-COMPILE-TIME"
        assert syscond_element.text == "sysc == 1"

    def test_write_condition_access_writes_mixed_text(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import (
            VariationPointProxy,
        )

        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        writer = ARXMLWriter()
        element = ET.Element("PARENT")
        proxy = VariationPointProxy(None, "vpp1")
        syscond = ConditionByFormula()
        syscond.setBindingTime(BindingTimeEnum().setValue("systemDesignTime"))
        syscond.setText("sysc > 0")
        proxy.setConditionAccess(syscond)
        writer.writeVariationPointProxy(element, proxy)

        condition_access_element = element.find("VARIATION-POINT-PROXY").find("CONDITION-ACCESS")
        assert condition_access_element is not None
        assert condition_access_element.attrib["BINDING-TIME"] == "SYSTEM-DESIGN-TIME"
        assert condition_access_element.text == "sysc > 0"

    def test_write_condition_by_formula_without_text_emits_no_text(self):
        vp = VariationPoint()
        syscond = ConditionByFormula()
        syscond.setBindingTime(BindingTimeEnum().setValue("linkTime"))
        vp.setSwSyscond(syscond)

        element = _write_vp_to_element(vp)

        syscond_element = element.find("VARIATION-POINT").find("SW-SYSCOND")
        assert syscond_element is not None
        assert syscond_element.attrib["BINDING-TIME"] == "LINK-TIME"
        assert syscond_element.text is None


class TestWriteAttributeValueVariationPoint:
    def _write_avp_to_element(self, avp):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        writer = ARXMLWriter()
        element = ET.Element("PARENT")
        writer.writeAttributeValueVariationPoint(element, avp)
        return element

    def test_write_all_members(self):
        avp = LimitValueVariationPoint()
        avp.setBindingTime(BindingTimeEnum().setValue("preCompileTime"))
        avp.setSd(String().setValue("sd-x"))
        avp.setShortLabel(PrimitiveIdentifier().setValue("limit1"))
        avp.setBlueprintValue(String().setValue("derived"))
        avp.setIntervalType(IntervalTypeEnum().setValue("closed"))
        avp.setText("42")

        element = self._write_avp_to_element(avp)

        assert element.attrib["BINDING-TIME"] == "PRE-COMPILE-TIME"
        assert element.attrib["SD"] == "sd-x"
        assert element.attrib["SHORT-LABEL"] == "limit1"
        assert element.attrib["BLUEPRINT-VALUE"] == "derived"
        assert element.attrib["INTERVAL-TYPE"] == "CLOSED"
        assert element.text == "42"

    def test_write_minimal_no_attributes(self):
        avp = NumericalValueVariationPoint()

        element = self._write_avp_to_element(avp)

        assert "BINDING-TIME" not in element.attrib
        assert "INTERVAL-TYPE" not in element.attrib
        assert element.text is None


class TestWriteAttributeValueVariationPointRoundTrip:
    """Table 7.2 round-trip: parse -> write -> re-parse preserves every
    AttributeValueVariationPoint attribute value through the VALUE-ACCESS dispatch."""

    def _build_document(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy

        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")

        pkg = document.createARPackage("Demo")
        component = pkg.createApplicationSwComponentType("MyComponent")
        behavior = component.createSwcInternalBehavior("Behavior")

        proxy = VariationPointProxy(behavior, "vpp1")
        avp = NumericalValueVariationPoint()
        avp.setBindingTime(BindingTimeEnum().setValue("preCompileTime"))
        avp.setSd(String().setValue("sd-rt"))
        avp.setShortLabel(PrimitiveIdentifier().setValue("vp_rt"))
        avp.setBlueprintValue(String().setValue("bp-rt"))
        avp.setText("1234")
        proxy.setValueAccess(avp)
        behavior.addVariationPointProxy(proxy)
        return document

    def test_round_trip_value_access_fields_preserved(self, tmp_path):
        from armodel.parser.arxml_parser import ARXMLParser

        document = self._build_document()
        output = str(tmp_path / "value_access_roundtrip.arxml")
        ARXMLWriter().save(output, document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(output, document_2)

        behavior_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0].getInternalBehavior()
        proxy_2 = behavior_2.getVariationPointProxies()[0]
        value_access = proxy_2.getValueAccess()
        assert isinstance(value_access, NumericalValueVariationPoint)
        assert value_access.getBindingTime().getValue() == "preCompileTime"
        assert value_access.getSd().getValue() == "sd-rt"
        assert value_access.getShortLabel().getValue() == "vp_rt"
        assert value_access.getBlueprintValue().getValue() == "bp-rt"
        assert value_access.getText() == "1234"

    def test_no_value_access_writes_no_wrapper(self):
        import os
        import tempfile

        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy

        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")

        pkg = document.createARPackage("Demo")
        component = pkg.createApplicationSwComponentType("MyComponent")
        behavior = component.createSwcInternalBehavior("Behavior")
        behavior.addVariationPointProxy(VariationPointProxy(behavior, "vpp_empty"))

        output = tempfile.mktemp(suffix=".arxml")
        ARXMLWriter().save(output, document)
        try:
            tree = ET.parse(output)
            ns = {"ar": "http://autosar.org/schema/r4.0"}
            proxy_element = tree.getroot().find(".//ar:VARIATION-POINT-PROXY", ns)
            assert proxy_element is not None
            assert proxy_element.find("ar:VALUE-ACCESS", ns) is None
        finally:
            if os.path.exists(output):
                os.remove(output)


class TestVariationPointProxyRoundTrip:
    def _build(self, document):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy

        pkg = document.createARPackage("AUTOSAR")
        component = pkg.createApplicationSwComponentType("MyComponent")
        behavior = component.createSwcInternalBehavior("Behavior")

        proxy = VariationPointProxy(behavior, "vpp1")
        syscond = ConditionByFormula()
        syscond.setBindingTime(BindingTimeEnum().setValue("preCompileTime"))
        proxy.setConditionAccess(syscond)
        proxy.setImplementationDataTypeRef(RefType().setValue("/Demo/ImplementationDataTypes/uint8").setDest("IMPLEMENTATION-DATA-TYPE"))
        proxy.setPostBuildValueAccessRef(RefType().setValue("/Demo/Criterions/Country").setDest("POST-BUILD-VARIANT-CRITERION"))
        condition = PostBuildVariantCondition()
        condition.setMatchingCriterionRef(RefType().setValue("/Demo/Criterions/Country").setDest("POST-BUILD-VARIANT-CRITERION"))
        condition.setValue(Integer().setValue("1"))
        proxy.addPostBuildVariantCondition(condition)
        proxy.setValueAccess(NumericalValueVariationPoint())
        behavior.addVariationPointProxy(proxy)
        return behavior

    def test_round_trip_variation_point_proxy(self):
        import os
        import tempfile

        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as _AUTOSAR
        from armodel.parser.arxml_parser import ARXMLParser
        from armodel.writer.arxml_writer import ARXMLWriter

        _AUTOSAR.getInstance().setARRelease("R23-11")
        document = _AUTOSAR.getInstance()
        document.clear()
        self._build(document)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = _AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            component_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            behavior_2 = component_2.getInternalBehavior()
            proxies = behavior_2.getVariationPointProxies()
            assert len(proxies) == 1
            proxy_2 = proxies[0]
            assert proxy_2.getShortName() == "vpp1"
            assert proxy_2.getConditionAccess().getBindingTime().getValue() == "preCompileTime"
            assert proxy_2.getImplementationDataTypeRef().getDest() == "IMPLEMENTATION-DATA-TYPE"
            assert proxy_2.getImplementationDataTypeRef().getValue() == "/Demo/ImplementationDataTypes/uint8"
            assert proxy_2.getPostBuildValueAccessRef().getDest() == "POST-BUILD-VARIANT-CRITERION"
            conditions = proxy_2.getPostBuildVariantConditions()
            assert len(conditions) == 1
            assert conditions[0].getMatchingCriterionRef().getValue() == "/Demo/Criterions/Country"
            assert conditions[0].getValue().getValue() == 1
            assert isinstance(proxy_2.getValueAccess(), NumericalValueVariationPoint)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_no_variation_point_proxy(self):
        import os
        import tempfile

        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as _AUTOSAR
        from armodel.parser.arxml_parser import ARXMLParser
        from armodel.writer.arxml_writer import ARXMLWriter

        _AUTOSAR.getInstance().setARRelease("R23-11")
        document = _AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        component = pkg.createApplicationSwComponentType("MyComponent")
        component.createSwcInternalBehavior("Behavior")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = _AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            component_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            assert component_2.getInternalBehavior().getVariationPointProxies() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_limit_value_access_with_all_members(self):
        import os
        import tempfile

        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as _AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import (
            VariationPointProxy,
        )
        from armodel.parser.arxml_parser import ARXMLParser
        from armodel.writer.arxml_writer import ARXMLWriter

        _AUTOSAR.getInstance().setARRelease("R23-11")
        document = _AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        component = pkg.createApplicationSwComponentType("MyComponent")
        behavior = component.createSwcInternalBehavior("Behavior")

        proxy = VariationPointProxy(behavior, "vpp1")
        limit = LimitValueVariationPoint()
        limit.setBindingTime(BindingTimeEnum().setValue("preCompileTime"))
        limit.setSd(String().setValue("sd-x"))
        limit.setShortLabel(PrimitiveIdentifier().setValue("limit1"))
        limit.setBlueprintValue(String().setValue("derived"))
        limit.setIntervalType(IntervalTypeEnum().setValue("open"))
        limit.setText("42")
        proxy.setValueAccess(limit)
        behavior.addVariationPointProxy(proxy)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = _AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            component_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            value_access = component_2.getInternalBehavior().getVariationPointProxies()[0].getValueAccess()
            assert isinstance(value_access, LimitValueVariationPoint)
            assert value_access.getBindingTime().getValue() == "preCompileTime"
            assert value_access.getSd().getValue() == "sd-x"
            assert value_access.getShortLabel().getValue() == "limit1"
            assert value_access.getBlueprintValue().getValue() == "derived"
            assert value_access.getIntervalType().getValue() == "open"
            assert value_access.getText() == "42"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestConditionByFormulaRoundTrip:
    """Table 7.5 round-trip: parse -> write -> re-parse preserves every
    ConditionByFormula attribute plus the <<atpMixedString>> formula text
    through the VariationPoint.swSyscond aggregation."""

    def _build_document(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")

        pkg = document.createARPackage("Demo")
        criterion = pkg.createPostBuildVariantCriterion("Country")
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("VP_Country"))
        syscond = ConditionByFormula()
        syscond.setBindingTime(BindingTimeEnum().setValue("preCompileTime"))
        syscond.setText('defined(sysc) && sysc == "A"')
        vp.setSwSyscond(syscond)
        criterion.setVariationPoint(vp)
        return document

    def test_round_trip_sw_syscond_fields_preserved(self, tmp_path):
        from armodel.parser.arxml_parser import ARXMLParser

        document = self._build_document()
        output = str(tmp_path / "condition_by_formula_roundtrip.arxml")
        ARXMLWriter().save(output, document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(output, document_2)

        criterion_2 = document_2.getARPackages()[0].getPostBuildVariantCriterions()[0]
        vp_2 = criterion_2.getVariationPoint()
        assert vp_2 is not None
        assert vp_2.getShortLabel().getValue() == "VP_Country"
        sw_syscond = vp_2.getSwSyscond()
        assert isinstance(sw_syscond, ConditionByFormula)
        assert sw_syscond.getBindingTime().getValue() == "preCompileTime"
        assert sw_syscond.getText() == 'defined(sysc) && sysc == "A"'


class TestPostBuildVariantCriterionRoundTrip:
    """Table 7.63 round-trip: parse -> write -> re-parse preserves the
    PostBuildVariantCriterion element (ARPackage.element dispatch) and its
    compuMethodRef field value."""

    def test_round_trip_compu_method_ref_preserved(self, tmp_path):
        from armodel.parser.arxml_parser import ARXMLParser

        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")

        pkg = document.createARPackage("Demo")
        criterion = pkg.createPostBuildVariantCriterion("Country")
        criterion.setCompuMethodRef(RefType().setValue("/Demo/CompuMethods/CountryEnum").setDest("COMPU-METHOD"))

        file_path = str(tmp_path / "post_build_variant_criterion_roundtrip.arxml")
        ARXMLWriter().save(file_path, document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)

        criterion_2 = document_2.getARPackages()[0].getPostBuildVariantCriterions()[0]
        assert criterion_2.getShortName() == "Country"
        ref_2 = criterion_2.getCompuMethodRef()
        assert ref_2.getValue() == "/Demo/CompuMethods/CountryEnum"
        assert ref_2.getDest() == "COMPU-METHOD"
