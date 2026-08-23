"""Tests for writer ECUC values and variant handling methods."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucAddInfoParamValue,
    EcucInstanceReferenceValue,
    EcucNumericalParamValue,
    EcucReferenceValue,
    EcucTextualParamValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (  # noqa E501
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa E501
    ARBoolean,
    ARLiteral,
    ARNumerical,
    Boolean,
    RefType,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (  # noqa E501
    SwSystemconstValue,
)
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import (
    SwCalprmAxisSet,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwDataDefProps,
)
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _literal(value):
    lit = ARLiteral()
    lit.setValue(value)
    return lit


def _numerical(value):
    n = ARNumerical()
    n.setValue(str(value))
    return n


def _make_collection():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createEcucValueCollection("Col")


def _make_module_config():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createEcucModuleConfigurationValues("mcv")


def _make_container():
    mcv = _make_module_config()
    return mcv.createContainer("cv")


def _make_value_set():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createSwSystemconstantValueSet("vss")


def _make_variant():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createPredefinedVariant("pv")


def _make_systemconst():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createSwSystemConst("sc")


class TestWriterEcucValueCollectionEcucValues:
    def test_with_refs(self, writer):
        collection = _make_collection()
        collection.addEcucValueRef(_ref("/v1", "ECUC-MODULE-CONFIGURATION-VALUES"))
        collection.addEcucValueRef(_ref("/v2", "ECUC-MODULE-CONFIGURATION-VALUES"))
        parent = _parent()
        writer.writeEcucValueCollectionEcucValues(parent, collection)
        assert parent[0].tag == "ECUC-VALUES"
        conds = parent[0].findall("ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL")
        assert len(conds) == 2
        ref_el = conds[0].find("ECUC-MODULE-CONFIGURATION-VALUES-REF")
        assert ref_el is not None

    def test_empty(self, writer):
        collection = _make_collection()
        parent = _parent()
        writer.writeEcucValueCollectionEcucValues(parent, collection)
        assert len(parent) == 0


class TestWriterEcucValueCollection:
    def test_full(self, writer):
        collection = _make_collection()
        collection.setEcuExtractRef(_ref("/ee", "ECU-EXTRACT"))
        collection.addEcucValueRef(_ref("/v", "ECUC-MODULE-CONFIGURATION-VALUES"))
        parent = _parent()
        writer.writeEcucValueCollection(parent, collection)
        assert parent[0].tag == "ECUC-VALUE-COLLECTION"
        assert parent[0].find("SHORT-NAME").text == "Col"
        assert parent[0].find("ECU-EXTRACT-REF") is not None
        assert parent[0].find("ECUC-VALUES") is not None

    def test_minimal(self, writer):
        collection = _make_collection()
        parent = _parent()
        writer.writeEcucValueCollection(parent, collection)
        assert parent[0].tag == "ECUC-VALUE-COLLECTION"
        assert parent[0].find("ECU-EXTRACT-REF") is None
        assert parent[0].find("ECUC-VALUES") is None


class TestWriterEcucContainerValueSubContainers:
    def test_with_sub_containers(self, writer):
        container = _make_container()
        container.createSubContainer("sub1")
        container.createSubContainer("sub2")
        parent = _parent()
        writer.writeEcucContainerValueSubContainers(parent, container)
        assert parent[0].tag == "SUB-CONTAINERS"
        subs = parent[0].findall("ECUC-CONTAINER-VALUE")
        assert len(subs) == 2

    def test_empty(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainerValueSubContainers(parent, container)
        assert len(parent) == 0


class TestWriterEcucParameterValue:
    def test_with_textual_param_value(self, writer):
        param = EcucTextualParamValue()
        param.setDefinition(_ref("/d", "ECUC-PARAMETER-DEF"))
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        assert parent.find("DEFINITION-REF") is not None

    def test_with_numerical_param_value(self, writer):
        param = EcucNumericalParamValue()
        param.setDefinition(_ref("/d", "ECUC-PARAMETER-DEF"))
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        assert parent.find("DEFINITION-REF") is not None

    def test_with_annotations(self, writer):
        param = EcucTextualParamValue()
        param.addAnnotation(Annotation())
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        assert parent.find("ANNOTATIONS/ANNOTATION") is not None

    def test_with_index(self, writer):
        param = EcucNumericalParamValue()
        param.setIndex(_numerical(4))
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        assert parent.find("INDEX") is not None
        assert parent.find("INDEX").text == "4"

    def test_with_is_auto_value(self, writer):
        param = EcucNumericalParamValue()
        param.setIsAutoValue(Boolean().setValue(True))
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        is_auto_value = parent.find("IS-AUTO-VALUE")
        assert is_auto_value is not None
        assert is_auto_value.text == "true"

    def test_emission_order_and_values(self, writer):
        from armodel.models.M2.MSR.Documentation.Annotation import Annotation

        param = EcucTextualParamValue()
        param.setDefinition(_ref("/d", "ECUC-PARAMETER-DEF"))
        param.setIndex(_numerical(1))
        param.addAnnotation(Annotation())
        param.setIsAutoValue(Boolean().setValue(False))
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        assert [c.tag for c in parent] == ["DEFINITION-REF", "INDEX", "ANNOTATIONS", "IS-AUTO-VALUE"]
        definition_ref = parent.find("DEFINITION-REF")
        assert definition_ref.text == "/d"
        index = parent.find("INDEX")
        assert index.text == "1"
        annotations = parent.find("ANNOTATIONS")
        assert annotations.findall("ANNOTATION") is not None
        is_auto_value = parent.find("IS-AUTO-VALUE")
        assert is_auto_value.text == "false"

    def test_minimal(self, writer):
        param = EcucTextualParamValue()
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        assert parent.find("DEFINITION-REF") is None
        assert parent.find("ANNOTATIONS") is None
        assert parent.find("INDEX") is None
        assert parent.find("IS-AUTO-VALUE") is None


class TestWriterSetEcucTextualParamValue:
    def test_writes_verbatim_string_value(self, writer):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString

        param = EcucTextualParamValue()
        param.setDefinition(_ref("/d", "ECUC-STRING-PARAM-DEF"))
        param.setValue(VerbatimString().setValue("NVM_BLOCK_NATIVE"))
        parent = _parent()
        writer.setEcucTextualParamValue(parent, param)
        child = parent.find("ECUC-TEXTUAL-PARAM-VALUE")
        assert child is not None
        assert child.find("DEFINITION-REF").text == "/d"
        assert child.find("VALUE").text == "NVM_BLOCK_NATIVE"

    def test_minimal_writes_no_value(self, writer):
        param = EcucTextualParamValue()
        parent = _parent()
        writer.setEcucTextualParamValue(parent, param)
        child = parent.find("ECUC-TEXTUAL-PARAM-VALUE")
        assert child is not None
        assert child.find("VALUE") is None


class TestWriterSetEcucNumericalParamValue:
    def test_writes_numerical_value(self, writer):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical

        param = EcucNumericalParamValue()
        param.setDefinition(_ref("/d", "ECUC-FLOAT-PARAM-DEF"))
        param.setValue(Numerical().setValue("74.8"))
        parent = _parent()
        writer.setEcucNumericalParamValue(parent, param)
        child = parent.find("ECUC-NUMERICAL-PARAM-VALUE")
        assert child is not None
        assert child.find("DEFINITION-REF").text == "/d"
        assert child.find("VALUE").text == "74.8"

    def test_minimal_writes_no_value(self, writer):
        param = EcucNumericalParamValue()
        parent = _parent()
        writer.setEcucNumericalParamValue(parent, param)
        child = parent.find("ECUC-NUMERICAL-PARAM-VALUE")
        assert child is not None
        assert child.find("VALUE") is None


class TestWriterSetEcucAddInfoParamValue:
    def test_writes_documentation_block_value(self, writer):
        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
        from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName
        from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph

        block = DocumentationBlock()
        para = MultiLanguageParagraph()
        l1 = LLongName()
        l1.l = "en"
        l1.value = "Description of the Dtc 0815."
        para.addL1(l1)
        block.addP(para)
        param = EcucAddInfoParamValue()
        param.setDefinition(_ref("/d", "ECUC-ADD-INFO-PARAM-DEF"))
        param.setValue(block)
        parent = _parent()
        writer.setEcucAddInfoParamValue(parent, param)
        child = parent.find("ECUC-ADD-INFO-PARAM-VALUE")
        assert child is not None
        assert child.find("DEFINITION-REF").text == "/d"
        p = child.find("VALUE/P")
        assert p is not None
        l_1 = p.find("L-1")
        assert l_1 is not None
        assert l_1.attrib["L"] == "en"
        assert l_1.text == "Description of the Dtc 0815."

    def test_minimal_writes_no_value(self, writer):
        param = EcucAddInfoParamValue()
        parent = _parent()
        writer.setEcucAddInfoParamValue(parent, param)
        child = parent.find("ECUC-ADD-INFO-PARAM-VALUE")
        assert child is not None
        assert child.find("VALUE") is None


class TestWriterEcucContainerValueParameterValues:
    def test_dispatches_textual_and_numerical(self, writer):
        container = _make_container()
        textual = EcucTextualParamValue()
        textual.setValue(_literal("txt"))
        textual.setDefinition(_ref("/d1", "ECUC-PARAMETER-DEF"))
        container.addParameterValue(textual)
        numerical = EcucNumericalParamValue()
        numerical.setValue(_numerical(42))
        numerical.setDefinition(_ref("/d2", "ECUC-PARAMETER-DEF"))
        container.addParameterValue(numerical)
        parent = _parent()
        writer.writeEcucContainerValueParameterValues(parent, container)
        assert parent[0].tag == "PARAMETER-VALUES"
        tags = {c.tag for c in parent[0]}
        assert "ECUC-TEXTUAL-PARAM-VALUE" in tags
        assert "ECUC-NUMERICAL-PARAM-VALUE" in tags

    def test_dispatches_add_info_param_value(self, writer):
        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock

        container = _make_container()
        add_info = EcucAddInfoParamValue()
        add_info.setValue(DocumentationBlock())
        add_info.setDefinition(_ref("/d3", "ECUC-PARAMETER-DEF"))
        container.addParameterValue(add_info)
        parent = _parent()
        writer.writeEcucContainerValueParameterValues(parent, container)
        assert parent[0].tag == "PARAMETER-VALUES"
        tags = {c.tag for c in parent[0]}
        assert "ECUC-ADD-INFO-PARAM-VALUE" in tags

    def test_empty(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainerValueParameterValues(parent, container)
        assert len(parent) == 0


class TestWriterEcucAbstractReferenceValue:
    def test_with_reference_value(self, writer):
        ref_val = EcucReferenceValue()
        ref_val.setDefinitionRef(_ref("/d", "ECUC-REFERENCE-DEF"))
        parent = _parent()
        writer.writeEcucAbstractReferenceValue(parent, ref_val)
        assert parent.find("DEFINITION-REF") is not None

    def test_with_instance_reference_value(self, writer):
        ref_val = EcucInstanceReferenceValue()
        ref_val.setDefinitionRef(_ref("/d", "ECUC-REFERENCE-DEF"))
        parent = _parent()
        writer.writeEcucAbstractReferenceValue(parent, ref_val)
        assert parent.find("DEFINITION-REF") is not None

    def test_with_annotations(self, writer):
        ref_val = EcucReferenceValue()
        ref_val.addAnnotation(Annotation())
        parent = _parent()
        writer.writeEcucAbstractReferenceValue(parent, ref_val)
        assert parent.find("ANNOTATIONS/ANNOTATION") is not None

    def test_minimal(self, writer):
        ref_val = EcucReferenceValue()
        parent = _parent()
        writer.writeEcucAbstractReferenceValue(parent, ref_val)
        assert parent.find("DEFINITION-REF") is None
        assert parent.find("ANNOTATIONS") is None

    def test_writes_all_table_2_53_fields_in_spec_order(self, writer):
        ref_val = EcucReferenceValue()
        ref_val.setDefinitionRef(_ref("/d", "ECUC-REFERENCE-DEF"))
        ref_val.setIndex(_numerical(3))
        ref_val.addAnnotation(Annotation())
        ref_val.setIsAutoValue(Boolean().setValue(True))
        parent = _parent()
        writer.writeEcucAbstractReferenceValue(parent, ref_val)
        assert [child.tag for child in parent] == ["DEFINITION-REF", "INDEX", "ANNOTATIONS", "IS-AUTO-VALUE"]
        assert parent.find("DEFINITION-REF").text == "/d"
        assert parent.find("INDEX").text == "3"
        assert parent.find("ANNOTATIONS/ANNOTATION") is not None
        assert parent.find("IS-AUTO-VALUE").text == "true"

    def test_omits_all_unset_optional_fields(self, writer):
        ref_val = EcucReferenceValue()
        parent = _parent()
        writer.writeEcucAbstractReferenceValue(parent, ref_val)
        assert len(parent) == 0


class TestWriterEcucReferenceValue:
    def test_writes_all_table_2_54_fields_in_spec_order(self, writer):
        ref_val = EcucReferenceValue()
        ref_val.setDefinitionRef(_ref("/d", "ECUC-REFERENCE-DEF"))
        ref_val.setIndex(_numerical(3))
        ref_val.addAnnotation(Annotation())
        ref_val.setIsAutoValue(Boolean().setValue(True))
        ref_val.setValueRef(_ref("/v", "ECUC-CONTAINER-VALUE"))
        parent = _parent()
        writer.setEcucReferenceValue(parent, ref_val)
        el = parent[0]
        assert el.tag == "ECUC-REFERENCE-VALUE"
        assert [child.tag for child in el] == [
            "DEFINITION-REF",
            "INDEX",
            "ANNOTATIONS",
            "IS-AUTO-VALUE",
            "VALUE-REF",
        ]
        assert el.find("DEFINITION-REF").text == "/d"
        assert el.find("INDEX").text == "3"
        assert el.find("ANNOTATIONS/ANNOTATION") is not None
        assert el.find("IS-AUTO-VALUE").text == "true"
        value_ref = el.find("VALUE-REF")
        assert value_ref.text == "/v"
        assert value_ref.attrib["DEST"] == "ECUC-CONTAINER-VALUE"

    def test_omits_all_unset_optional_fields(self, writer):
        ref_val = EcucReferenceValue()
        parent = _parent()
        writer.setEcucReferenceValue(parent, ref_val)
        assert parent.find("ECUC-REFERENCE-VALUE") is None

    def test_none_emit_nothing(self, writer):
        parent = _parent()
        writer.setEcucReferenceValue(parent, None)
        assert len(parent) == 0


class TestWriterEcucContainerValueReferenceValues:
    def test_dispatches_reference_and_instance_reference(self, writer):
        container = _make_container()
        ref_val = EcucReferenceValue()
        ref_val.setValueRef(_ref("/v", "ECUC-CONTAINER-VALUE"))
        ref_val.setDefinitionRef(_ref("/d1", "ECUC-REFERENCE-DEF"))
        ref_val.setIndex(_numerical(3))
        container.addReferenceValue(ref_val)
        iref_val = EcucInstanceReferenceValue()
        iref_val.setDefinitionRef(_ref("/d2", "ECUC-REFERENCE-DEF"))
        iref = AnyInstanceRef()
        iref.setBaseRef(_ref("/b", "ECUC-CONTAINER-VALUE"))
        iref.setTargetRef(_ref("/t", "ECUC-CONTAINER-VALUE"))
        iref_val.setValueIRef(iref)
        container.addReferenceValue(iref_val)
        parent = _parent()
        writer.writeEcucContainerValueReferenceValues(parent, container)
        assert parent[0].tag == "REFERENCE-VALUES"
        tags = {c.tag for c in parent[0]}
        assert "ECUC-REFERENCE-VALUE" in tags
        assert "ECUC-INSTANCE-REFERENCE-VALUE" in tags
        ref_el = parent[0].find("ECUC-REFERENCE-VALUE")
        assert ref_el.find("INDEX") is not None
        assert ref_el.find("INDEX").text == "3"
        iref_el = parent[0].find("ECUC-INSTANCE-REFERENCE-VALUE")
        assert iref_el.find("VALUE-IREF") is not None
        assert iref_el.find("VALUE-IREF/BASE-REF") is not None
        assert iref_el.find("VALUE-IREF/TARGET-REF") is not None

    def test_empty(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainerValueReferenceValues(parent, container)
        assert len(parent) == 0


class TestWriterEcucContainValue:
    def test_full(self, writer):
        container = _make_container()
        container.setDefinitionRef(_ref("/d", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        container.setIndex(_numerical(7))
        textual = EcucTextualParamValue()
        textual.setValue(_literal("txt"))
        container.addParameterValue(textual)
        ref_val = EcucReferenceValue()
        ref_val.setValueRef(_ref("/v", "ECUC-CONTAINER-VALUE"))
        container.addReferenceValue(ref_val)
        container.createSubContainer("sub")
        parent = _parent()
        writer.writeEcucContainValue(parent, container)
        assert parent[0].tag == "ECUC-CONTAINER-VALUE"
        assert parent[0].find("SHORT-NAME").text == "cv"
        assert parent[0].find("DEFINITION-REF") is not None
        assert parent[0].find("INDEX") is not None
        assert parent[0].find("INDEX").text == "7"
        assert parent[0].find("PARAMETER-VALUES") is not None
        assert parent[0].find("REFERENCE-VALUES") is not None
        assert parent[0].find("SUB-CONTAINERS") is not None

    def test_minimal(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainValue(parent, container)
        assert parent[0].tag == "ECUC-CONTAINER-VALUE"
        assert parent[0].find("DEFINITION-REF") is None
        assert parent[0].find("INDEX") is None
        assert parent[0].find("PARAMETER-VALUES") is None
        assert parent[0].find("REFERENCE-VALUES") is None
        assert parent[0].find("SUB-CONTAINERS") is None


class TestWriterEcucModuleConfigurationValuesContainers:
    def test_with_containers(self, writer):
        mcv = _make_module_config()
        mcv.createContainer("c1")
        mcv.createContainer("c2")
        parent = _parent()
        writer.writeEcucModuleConfigurationValuesContainers(parent, mcv)
        assert parent[0].tag == "CONTAINERS"
        containers = parent[0].findall("ECUC-CONTAINER-VALUE")
        assert len(containers) == 2

    def test_empty(self, writer):
        mcv = _make_module_config()
        parent = _parent()
        writer.writeEcucModuleConfigurationValuesContainers(parent, mcv)
        assert len(parent) == 0


class TestWriterEcucModuleConfigurationValues:
    def test_full(self, writer):
        mcv = _make_module_config()
        mcv.setDefinition(_ref("/d", "ECUC-MODULE-DEF"))
        mcv.setImplementationConfigVariant(_literal("VARIANT-PRE-COMPILE"))
        mcv.setModuleDescription(_ref("/md", "BSW-IMPLEMENTATION"))
        mcv.createContainer("c1")
        parent = _parent()
        writer.writeEcucModuleConfigurationValues(parent, mcv)
        assert parent[0].tag == "ECUC-MODULE-CONFIGURATION-VALUES"
        assert parent[0].find("SHORT-NAME").text == "mcv"
        definition_ref = parent[0].find("DEFINITION-REF")
        assert definition_ref is not None
        assert definition_ref.text == "/d"
        impl = parent[0].find("IMPLEMENTATION-CONFIG-VARIANT")
        assert impl is not None
        assert impl.text == "VARIANT-PRE-COMPILE"
        module_description_ref = parent[0].find("MODULE-DESCRIPTION-REF")
        assert module_description_ref is not None
        assert module_description_ref.text == "/md"
        assert parent[0].find("CONTAINERS") is not None

    def test_minimal(self, writer):
        mcv = _make_module_config()
        parent = _parent()
        writer.writeEcucModuleConfigurationValues(parent, mcv)
        assert parent[0].tag == "ECUC-MODULE-CONFIGURATION-VALUES"
        assert parent[0].find("DEFINITION-REF") is None
        assert parent[0].find("IMPLEMENTATION-CONFIG-VARIANT") is None
        assert parent[0].find("MODULE-DESCRIPTION-REF") is None
        assert parent[0].find("ECUC-DEF-EDITION") is None
        assert parent[0].find("POST-BUILD-VARIANT-USED") is None
        assert parent[0].find("CONTAINERS") is None

    def test_full_writes_ecuc_def_edition_and_post_build_variant_used(self, writer):
        mcv = _make_module_config()
        mcv.setEcucDefEdition(RevisionLabelString().setValue("1.0.0"))
        mcv.setPostBuildVariantUsed(Boolean().setValue(True))
        parent = _parent()
        writer.writeEcucModuleConfigurationValues(parent, mcv)
        assert parent[0].tag == "ECUC-MODULE-CONFIGURATION-VALUES"
        edition = parent[0].find("ECUC-DEF-EDITION")
        assert edition is not None
        assert edition.text == "1.0.0"
        post_build = parent[0].find("POST-BUILD-VARIANT-USED")
        assert post_build is not None
        assert post_build.text == "true"


class TestWriterSwSystemconst:
    def test_without_data_def_props(self, writer):
        const = _make_systemconst()
        parent = _parent()
        writer.writeSwSystemconst(parent, const)
        assert parent[0].tag == "SW-SYSTEMCONST"
        assert parent[0].find("SHORT-NAME").text == "sc"
        assert parent[0].find("SW-DATA-DEF-PROPS") is None

    def test_with_data_def_props(self, writer):
        const = _make_systemconst()
        props = SwDataDefProps()
        props.setSwCalprmAxisSet(SwCalprmAxisSet())
        const.setSwDataDefProps(props)
        parent = _parent()
        writer.writeSwSystemconst(parent, const)
        assert parent[0].tag == "SW-SYSTEMCONST"
        assert parent[0].find("SW-DATA-DEF-PROPS") is not None


class TestWriterSwSystemconstValue:
    def test_full(self, writer):
        value = SwSystemconstValue()
        value.setSwSystemconstRef(_ref("/sc", "SW-SYSTEMCONST"))
        value.setValue(_numerical(42))
        value.addAnnotation(Annotation())
        parent = _parent()
        writer.writeSwSystemconstValue(parent, value)
        assert parent[0].tag == "SW-SYSTEMCONST-VALUE"
        assert parent[0].find("SW-SYSTEMCONST-REF") is not None
        assert parent[0].find("VALUE") is not None
        assert parent[0].find("VALUE").text == "42"
        assert parent[0].find("ANNOTATIONS/ANNOTATION") is not None

    def test_minimal(self, writer):
        value = SwSystemconstValue()
        parent = _parent()
        writer.writeSwSystemconstValue(parent, value)
        assert parent[0].tag == "SW-SYSTEMCONST-VALUE"
        assert parent[0].find("SW-SYSTEMCONST-REF") is None
        assert parent[0].find("VALUE") is None
        assert parent[0].find("ANNOTATIONS") is None


class TestWriterSwSystemconstantValueSetSwSystemconstantValues:
    def test_with_values(self, writer):
        value_set = _make_value_set()
        v1 = SwSystemconstValue()
        v1.setSwSystemconstRef(_ref("/s1", "SW-SYSTEMCONST"))
        v1.setValue(_numerical(1))
        value_set.addSwSystemconstantValue(v1)
        v2 = SwSystemconstValue()
        v2.setSwSystemconstRef(_ref("/s2", "SW-SYSTEMCONST"))
        v2.setValue(_numerical(2))
        value_set.addSwSystemconstantValue(v2)
        parent = _parent()
        writer.writeSwSystemconstantValueSetSwSystemconstantValues(parent, value_set)
        assert parent[0].tag == "SW-SYSTEMCONSTANT-VALUES"
        values = parent[0].findall("SW-SYSTEMCONST-VALUE")
        assert len(values) == 2

    def test_empty(self, writer):
        value_set = _make_value_set()
        parent = _parent()
        writer.writeSwSystemconstantValueSetSwSystemconstantValues(parent, value_set)
        assert len(parent) == 0


class TestWriterSwSystemconstantValueSet:
    def test_full(self, writer):
        value_set = _make_value_set()
        v1 = SwSystemconstValue()
        v1.setSwSystemconstRef(_ref("/s1", "SW-SYSTEMCONST"))
        v1.setValue(_numerical(1))
        value_set.addSwSystemconstantValue(v1)
        parent = _parent()
        writer.writeSwSystemconstantValueSet(parent, value_set)
        assert parent[0].tag == "SW-SYSTEMCONSTANT-VALUE-SET"
        assert parent[0].find("SHORT-NAME").text == "vss"
        assert parent[0].find("SW-SYSTEMCONSTANT-VALUES") is not None

    def test_minimal(self, writer):
        value_set = _make_value_set()
        parent = _parent()
        writer.writeSwSystemconstantValueSet(parent, value_set)
        assert parent[0].tag == "SW-SYSTEMCONSTANT-VALUE-SET"
        assert parent[0].find("SW-SYSTEMCONSTANT-VALUES") is None


class TestWriterPredefinedVariantIncludedVariantRefs:
    def test_with_refs(self, writer):
        variant = _make_variant()
        variant.addIncludedVariantRef(_ref("/v1", "PREDEFINED-VARIANT"))
        variant.addIncludedVariantRef(_ref("/v2", "PREDEFINED-VARIANT"))
        parent = _parent()
        writer.writePredefinedVariantIncludedVariantRefs(parent, variant)
        assert parent[0].tag == "INCLUDED-VARIANT-REFS"
        refs = parent[0].findall("INCLUDED-VARIANT-REF")
        assert len(refs) == 2

    def test_empty(self, writer):
        variant = _make_variant()
        parent = _parent()
        writer.writePredefinedVariantIncludedVariantRefs(parent, variant)
        assert len(parent) == 0


class TestWriterPredefinedVariantPostBuildVariantCriterionValueSetRefs:
    def test_with_refs(self, writer):
        variant = _make_variant()
        variant.addPostBuildVariantCriterionValueSetRef(_ref("/pb1", "POST-BUILD-VARIANT-CRITERION-VALUE-SET"))
        variant.addPostBuildVariantCriterionValueSetRef(_ref("/pb2", "POST-BUILD-VARIANT-CRITERION-VALUE-SET"))
        parent = _parent()
        writer.writePredefinedVariantPostBuildVariantCriterionValueSetRefs(parent, variant)
        assert parent[0].tag == ("POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS")
        refs = parent[0].findall("POST-BUILD-VARIANT-CRITERION-VALUE-SET-REF")
        assert len(refs) == 2

    def test_empty(self, writer):
        variant = _make_variant()
        parent = _parent()
        writer.writePredefinedVariantPostBuildVariantCriterionValueSetRefs(parent, variant)
        assert len(parent) == 0


class TestWriterPredefinedVariantSwSystemconstantValueSetRefs:
    def test_with_refs(self, writer):
        variant = _make_variant()
        variant.addSwSystemconstantValueSetRef(_ref("/sv1", "SW-SYSTEMCONSTANT-VALUE-SET"))
        variant.addSwSystemconstantValueSetRef(_ref("/sv2", "SW-SYSTEMCONSTANT-VALUE-SET"))
        parent = _parent()
        writer.writePredefinedVariantSwSystemconstantValueSetRefs(parent, variant)
        assert parent[0].tag == "SW-SYSTEMCONSTANT-VALUE-SET-REFS"
        refs = parent[0].findall("SW-SYSTEMCONSTANT-VALUE-SET-REF")
        assert len(refs) == 2

    def test_empty(self, writer):
        variant = _make_variant()
        parent = _parent()
        writer.writePredefinedVariantSwSystemconstantValueSetRefs(parent, variant)
        assert len(parent) == 0


class TestWriterPredefinedVariant:
    def test_full(self, writer):
        variant = _make_variant()
        variant.addIncludedVariantRef(_ref("/iv", "PREDEFINED-VARIANT"))
        variant.addPostBuildVariantCriterionValueSetRef(_ref("/pb", "POST-BUILD-VARIANT-CRITERION-VALUE-SET"))
        variant.addSwSystemconstantValueSetRef(_ref("/sv", "SW-SYSTEMCONSTANT-VALUE-SET"))
        parent = _parent()
        writer.writePredefinedVariant(parent, variant)
        assert parent[0].tag == "PREDEFINED-VARIANT"
        assert parent[0].find("SHORT-NAME").text == "pv"
        assert parent[0].find("INCLUDED-VARIANT-REFS") is not None
        assert parent[0].find("POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS") is not None
        assert parent[0].find("SW-SYSTEMCONSTANT-VALUE-SET-REFS") is not None

    def test_minimal(self, writer):
        variant = _make_variant()
        parent = _parent()
        writer.writePredefinedVariant(parent, variant)
        assert parent[0].tag == "PREDEFINED-VARIANT"
        assert parent[0].find("SHORT-NAME").text == "pv"
        assert parent[0].find("INCLUDED-VARIANT-REFS") is None
        assert parent[0].find("POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS") is None
        assert parent[0].find("SW-SYSTEMCONSTANT-VALUE-SET-REFS") is None
