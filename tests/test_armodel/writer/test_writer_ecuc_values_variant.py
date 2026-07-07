"""Tests for writer ECUC values and variant handling methods."""
import xml.etree.cElementTree as ET
import pytest

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucInstanceReferenceValue,
    EcucNumericalParamValue,
    EcucReferenceValue,
    EcucTextualParamValue,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwDataDefProps,
)
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import (
    SwCalprmAxisSet,
)
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (  # noqa E501
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa E501
    ARLiteral,
    ARNumerical,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (  # noqa E501
    SwSystemconstValue,
)


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
        collection.addEcucValueRef(
            _ref("/v1", "ECUC-MODULE-CONFIGURATION-VALUES")
        )
        collection.addEcucValueRef(
            _ref("/v2", "ECUC-MODULE-CONFIGURATION-VALUES")
        )
        parent = _parent()
        writer.writeEcucValueCollectionEcucValues(parent, collection)
        assert parent[0].tag == "ECUC-VALUES"
        conds = parent[0].findall(
            "ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL"
        )
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
        collection.addEcucValueRef(
            _ref("/v", "ECUC-MODULE-CONFIGURATION-VALUES")
        )
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
        param.setDefinitionRef(_ref("/d", "ECUC-PARAMETER-DEF"))
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        assert parent.find("DEFINITION-REF") is not None

    def test_with_numerical_param_value(self, writer):
        param = EcucNumericalParamValue()
        param.setDefinitionRef(_ref("/d", "ECUC-PARAMETER-DEF"))
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        assert parent.find("DEFINITION-REF") is not None

    def test_with_annotations(self, writer):
        param = EcucTextualParamValue()
        param.addAnnotation(Annotation())
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        assert parent.find("ANNOTATIONS/ANNOTATION") is not None

    def test_minimal(self, writer):
        param = EcucTextualParamValue()
        parent = _parent()
        writer.writeEcucParameterValue(parent, param)
        assert parent.find("DEFINITION-REF") is None
        assert parent.find("ANNOTATIONS") is None


class TestWriterEcucContainerValueParameterValues:
    def test_dispatches_textual_and_numerical(self, writer):
        container = _make_container()
        textual = EcucTextualParamValue()
        textual.setValue(_literal("txt"))
        textual.setDefinitionRef(_ref("/d1", "ECUC-PARAMETER-DEF"))
        container.addParameterValue(textual)
        numerical = EcucNumericalParamValue()
        numerical.setValue(_numerical(42))
        numerical.setDefinitionRef(_ref("/d2", "ECUC-PARAMETER-DEF"))
        container.addParameterValue(numerical)
        parent = _parent()
        writer.writeEcucContainerValueParameterValues(parent, container)
        assert parent[0].tag == "PARAMETER-VALUES"
        tags = {c.tag for c in parent[0]}
        assert "ECUC-TEXTUAL-PARAM-VALUE" in tags
        assert "ECUC-NUMERICAL-PARAM-VALUE" in tags

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


class TestWriterEcucContainerValueReferenceValues:
    def test_dispatches_reference_and_instance_reference(self, writer):
        container = _make_container()
        ref_val = EcucReferenceValue()
        ref_val.setValueRef(_ref("/v", "ECUC-CONTAINER-VALUE"))
        ref_val.setDefinitionRef(_ref("/d1", "ECUC-REFERENCE-DEF"))
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
        container.setDefinitionRef(
            _ref("/d", "ECUC-PARAM-CONF-CONTAINER-DEF")
        )
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
        assert parent[0].find("PARAMETER-VALUES") is not None
        assert parent[0].find("REFERENCE-VALUES") is not None
        assert parent[0].find("SUB-CONTAINERS") is not None

    def test_minimal(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainValue(parent, container)
        assert parent[0].tag == "ECUC-CONTAINER-VALUE"
        assert parent[0].find("DEFINITION-REF") is None
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
        mcv.setDefinitionRef(_ref("/d", "ECUC-MODULE-DEF"))
        mcv.setImplementationConfigVariant(_literal("variant"))
        mcv.setModuleDescriptionRef(_ref("/md", "ECUC-MODULE-DEF"))
        mcv.createContainer("c1")
        parent = _parent()
        writer.writeEcucModuleConfigurationValues(parent, mcv)
        assert parent[0].tag == "ECUC-MODULE-CONFIGURATION-VALUES"
        assert parent[0].find("SHORT-NAME").text == "mcv"
        assert parent[0].find("DEFINITION-REF") is not None
        impl = parent[0].find("IMPLEMENTATION-CONFIG-VARIANT")
        assert impl is not None
        assert impl.text == "variant"
        assert parent[0].find("MODULE-DESCRIPTION-REF") is not None
        assert parent[0].find("CONTAINERS") is not None

    def test_minimal(self, writer):
        mcv = _make_module_config()
        parent = _parent()
        writer.writeEcucModuleConfigurationValues(parent, mcv)
        assert parent[0].tag == "ECUC-MODULE-CONFIGURATION-VALUES"
        assert parent[0].find("DEFINITION-REF") is None
        assert parent[0].find("IMPLEMENTATION-CONFIG-VARIANT") is None
        assert parent[0].find("MODULE-DESCRIPTION-REF") is None
        assert parent[0].find("CONTAINERS") is None


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
        writer.writeSwSystemconstantValueSetSwSystemconstantValues(
            parent, value_set
        )
        assert parent[0].tag == "SW-SYSTEMCONSTANT-VALUES"
        values = parent[0].findall("SW-SYSTEMCONST-VALUE")
        assert len(values) == 2

    def test_empty(self, writer):
        value_set = _make_value_set()
        parent = _parent()
        writer.writeSwSystemconstantValueSetSwSystemconstantValues(
            parent, value_set
        )
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
        variant.addIncludedVariantRef(
            _ref("/v1", "PREDEFINED-VARIANT")
        )
        variant.addIncludedVariantRef(
            _ref("/v2", "PREDEFINED-VARIANT")
        )
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
        variant.addPostBuildVariantCriterionValueSetRef(
            _ref("/pb1", "POST-BUILD-VARIANT-CRITERION-VALUE-SET")
        )
        variant.addPostBuildVariantCriterionValueSetRef(
            _ref("/pb2", "POST-BUILD-VARIANT-CRITERION-VALUE-SET")
        )
        parent = _parent()
        writer.writePredefinedVariantPostBuildVariantCriterionValueSetRefs(
            parent, variant
        )
        assert parent[0].tag == (
            "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS"
        )
        refs = parent[0].findall(
            "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REF"
        )
        assert len(refs) == 2

    def test_empty(self, writer):
        variant = _make_variant()
        parent = _parent()
        writer.writePredefinedVariantPostBuildVariantCriterionValueSetRefs(
            parent, variant
        )
        assert len(parent) == 0


class TestWriterPredefinedVariantSwSystemconstantValueSetRefs:
    def test_with_refs(self, writer):
        variant = _make_variant()
        variant.addSwSystemconstantValueSetRef(
            _ref("/sv1", "SW-SYSTEMCONSTANT-VALUE-SET")
        )
        variant.addSwSystemconstantValueSetRef(
            _ref("/sv2", "SW-SYSTEMCONSTANT-VALUE-SET")
        )
        parent = _parent()
        writer.writePredefinedVariantSwSystemconstantValueSetRefs(
            parent, variant
        )
        assert parent[0].tag == "SW-SYSTEMCONSTANT-VALUE-SET-REFS"
        refs = parent[0].findall("SW-SYSTEMCONSTANT-VALUE-SET-REF")
        assert len(refs) == 2

    def test_empty(self, writer):
        variant = _make_variant()
        parent = _parent()
        writer.writePredefinedVariantSwSystemconstantValueSetRefs(
            parent, variant
        )
        assert len(parent) == 0


class TestWriterPredefinedVariant:
    def test_full(self, writer):
        variant = _make_variant()
        variant.addIncludedVariantRef(
            _ref("/iv", "PREDEFINED-VARIANT")
        )
        variant.addPostBuildVariantCriterionValueSetRef(
            _ref("/pb", "POST-BUILD-VARIANT-CRITERION-VALUE-SET")
        )
        variant.addSwSystemconstantValueSetRef(
            _ref("/sv", "SW-SYSTEMCONSTANT-VALUE-SET")
        )
        parent = _parent()
        writer.writePredefinedVariant(parent, variant)
        assert parent[0].tag == "PREDEFINED-VARIANT"
        assert parent[0].find("SHORT-NAME").text == "pv"
        assert parent[0].find("INCLUDED-VARIANT-REFS") is not None
        assert parent[0].find(
            "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS"
        ) is not None
        assert parent[0].find(
            "SW-SYSTEMCONSTANT-VALUE-SET-REFS"
        ) is not None

    def test_minimal(self, writer):
        variant = _make_variant()
        parent = _parent()
        writer.writePredefinedVariant(parent, variant)
        assert parent[0].tag == "PREDEFINED-VARIANT"
        assert parent[0].find("SHORT-NAME").text == "pv"
        assert parent[0].find("INCLUDED-VARIANT-REFS") is None
        assert parent[0].find(
            "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS"
        ) is None
        assert parent[0].find(
            "SW-SYSTEMCONSTANT-VALUE-SET-REFS"
        ) is None
