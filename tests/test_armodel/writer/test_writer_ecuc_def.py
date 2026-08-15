"""Tests for writer ECUC parameter definition handlers."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucDefinitionCollection,
    EcucDestinationUriDefRefType,
    EcucMultiplicityConfigurationClass,
    EcucValueConfigurationClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa E501
    ARBoolean,
    ARLiteral,
    CIdentifier,
    Float,
    Limit,
    PositiveInteger,
    RefType,
    RegularExpression,
    UnlimitedInteger,
    VerbatimString,
)
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


def _bool(value):
    b = ARBoolean()
    b.setValue(value)
    return b


def _posint(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _unlimited(value):
    n = UnlimitedInteger()
    n.setValue(str(value))
    return n


def _float(value):
    f = Float()
    f.setValue(str(value))
    return f


def _limit(value, interval=None):
    lim = Limit()
    lim.setValue(str(value))
    if interval is not None:
        lim.setIntervalType(interval)
    return lim


def _verbatim(value):
    v = VerbatimString()
    v.setValue(value)
    return v


def _regex(value):
    v = RegularExpression()
    v.setValue(value)
    return v


def _make_module():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createEcucModuleDef("Mod")


def _make_container():
    module = _make_module()
    return module.createEcucParamConfContainerDef("Ct")


class TestWriterEcucDefinitionElement:
    def test_full(self, writer):
        module = _make_module()
        module.setLowerMultiplicity(_posint(0))
        module.setUpperMultiplicity(_posint(1))
        module.setScope(_literal("scope"))
        parent = _parent()
        writer.writeEcucDefinitionElement(parent, module)
        assert parent.find("SHORT-NAME").text == "Mod"
        assert parent.find("LOWER-MULTIPLICITY").text == "0"
        assert parent.find("UPPER-MULTIPLICITY").text == "1"
        assert parent.find("SCOPE").text == "scope"

    def test_minimal(self, writer):
        module = _make_module()
        parent = _parent()
        writer.writeEcucDefinitionElement(parent, module)
        assert parent.find("SHORT-NAME").text == "Mod"
        assert parent.find("LOWER-MULTIPLICITY") is None
        assert parent.find("UPPER-MULTIPLICITY") is None
        assert parent.find("SCOPE") is None


class TestWriterEcucModuleDefSupportedConfigVariants:
    def test_with_variants(self, writer):
        module = _make_module()
        module.addSupportedConfigVariant(_literal("v1"))
        module.addSupportedConfigVariant(_literal("v2"))
        parent = _parent()
        writer.writeEcucModuleDefSupportedConfigVariants(parent, module)
        assert parent[0].tag == "SUPPORTED-CONFIG-VARIANTS"
        variants = parent[0].findall("SUPPORTED-CONFIG-VARIANT")
        assert len(variants) == 2
        assert variants[0].text == "v1"
        assert variants[1].text == "v2"

    def test_empty(self, writer):
        module = _make_module()
        parent = _parent()
        writer.writeEcucModuleDefSupportedConfigVariants(parent, module)
        assert len(parent) == 0


class TestWriterEcucAbstractConfigurationClass:
    def test_full(self, writer):
        cfg = EcucMultiplicityConfigurationClass()
        cfg.setConfigClass(_literal("cls"))
        cfg.setConfigVariant(_literal("var"))
        parent = _parent()
        writer.writeEcucAbstractConfigurationClass(parent, cfg)
        assert parent.find("CONFIG-CLASS").text == "cls"
        assert parent.find("CONFIG-VARIANT").text == "var"

    def test_minimal(self, writer):
        cfg = EcucMultiplicityConfigurationClass()
        parent = _parent()
        writer.writeEcucAbstractConfigurationClass(parent, cfg)
        assert parent.find("CONFIG-CLASS") is None
        assert parent.find("CONFIG-VARIANT") is None


class TestWriterEcucMultiplicityConfigurationClass:
    def test_with_value(self, writer):
        cfg = EcucMultiplicityConfigurationClass()
        cfg.setConfigClass(_literal("cls"))
        parent = _parent()
        writer.writeEcucMultiplicityConfigurationClass(parent, cfg)
        assert parent[0].tag == "ECUC-MULTIPLICITY-CONFIGURATION-CLASS"
        assert parent[0].find("CONFIG-CLASS").text == "cls"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucMultiplicityConfigurationClass(parent, None)
        assert len(parent) == 0


class TestWriterEcucValueConfigurationClass:
    def test_with_value(self, writer):
        cfg = EcucValueConfigurationClass()
        cfg.setConfigVariant(_literal("var"))
        parent = _parent()
        writer.writeEcucValueConfigurationClass(parent, cfg)
        assert parent[0].tag == "ECUC-VALUE-CONFIGURATION-CLASS"
        assert parent[0].find("CONFIG-VARIANT").text == "var"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucValueConfigurationClass(parent, None)
        assert len(parent) == 0


class TestWriterEcucCommonAttributes:
    def test_full(self, writer):
        container = _make_container()
        param = container.createEcucBooleanParamDef("P")
        param.addMultiplicityConfigClass(EcucMultiplicityConfigurationClass().setConfigClass(_literal("mc")))
        param.setOrigin(_literal("org"))
        param.setPostBuildVariantMultiplicity(_bool(True))
        param.setPostBuildVariantValue(_bool(False))
        param.setRequiresIndex(_bool(True))
        param.addValueConfigClass(EcucValueConfigurationClass().setConfigVariant(_literal("vc")))
        parent = _parent()
        writer.writeEcucCommonAttributes(parent, param)
        assert parent.find("MULTIPLICITY-CONFIG-CLASSES") is not None
        mc = parent.find("MULTIPLICITY-CONFIG-CLASSES")
        assert mc.find("ECUC-MULTIPLICITY-CONFIGURATION-CLASS") is not None
        assert parent.find("ORIGIN").text == "org"
        assert parent.find("POST-BUILD-VARIANT-MULTIPLICITY").text == "true"
        assert parent.find("POST-BUILD-VARIANT-VALUE").text == "false"
        assert parent.find("REQUIRES-INDEX").text == "true"
        assert parent.find("VALUE-CONFIG-CLASSES") is not None
        vc = parent.find("VALUE-CONFIG-CLASSES")
        assert vc.find("ECUC-VALUE-CONFIGURATION-CLASS") is not None

    def test_minimal(self, writer):
        container = _make_container()
        param = container.createEcucBooleanParamDef("P")
        parent = _parent()
        writer.writeEcucCommonAttributes(parent, param)
        assert parent.find("MULTIPLICITY-CONFIG-CLASSES") is None
        assert parent.find("ORIGIN") is None
        assert parent.find("POST-BUILD-VARIANT-MULTIPLICITY") is None
        assert parent.find("POST-BUILD-VARIANT-VALUE") is None
        assert parent.find("REQUIRES-INDEX") is None
        assert parent.find("VALUE-CONFIG-CLASSES") is None


class TestWriterEcucParameterDef:
    def test_full(self, writer):
        container = _make_container()
        param = container.createEcucBooleanParamDef("P")
        param.setOrigin(_literal("org"))
        param.setSymbolicNameValue(_bool(True))
        param.setWithAuto(_bool(False))
        parent = _parent()
        writer.writeEcucParameterDef(parent, param)
        assert parent.find("ORIGIN").text == "org"
        assert parent.find("SYMBOLIC-NAME-VALUE").text == "true"
        assert parent.find("WITH-AUTO").text == "false"
        assert parent.find("DERIVATION") is None

    def test_minimal(self, writer):
        container = _make_container()
        param = container.createEcucBooleanParamDef("P")
        parent = _parent()
        writer.writeEcucParameterDef(parent, param)
        assert parent.find("SYMBOLIC-NAME-VALUE") is None
        assert parent.find("WITH-AUTO") is None


class TestWriterEcucBooleanParamDef:
    def test_full(self, writer):
        container = _make_container()
        param = container.createEcucBooleanParamDef("P")
        param.setDefaultValue(_bool(True))
        parent = _parent()
        writer.writeEcucBooleanParamDef(parent, param)
        assert parent[0].tag == "ECUC-BOOLEAN-PARAM-DEF"
        assert parent[0].find("DEFAULT-VALUE").text == "true"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucBooleanParamDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucAbstractStringParamDef:
    def test_writes_common_attrs(self, writer):
        container = _make_container()
        param = container.createEcucStringParamDef("P")
        param.setOrigin(_literal("org"))
        parent = _parent()
        writer.writeEcucAbstractStringParamDef(parent, param)
        assert parent.find("ORIGIN").text == "org"


class TestWriterEcucStringParamDef:
    def test_full(self, writer):
        container = _make_container()
        param = container.createEcucStringParamDef("P")
        param.setDefaultValue(_verbatim("dv"))
        param.setMinLength(_posint(1))
        param.setMaxLength(_posint(64))
        param.setRegularExpression(_regex("[a-z]*"))
        parent = _parent()
        writer.writeEcucStringParamDef(parent, param)
        assert parent[0].tag == "ECUC-STRING-PARAM-DEF"
        variants = parent[0].find("ECUC-STRING-PARAM-DEF-VARIANTS")
        assert variants is not None
        cond = variants.find("ECUC-STRING-PARAM-DEF-CONDITIONAL")
        assert cond is not None
        assert cond.find("DEFAULT-VALUE").text == "dv"
        assert cond.find("MIN-LENGTH").text == "1"
        assert cond.find("MAX-LENGTH").text == "64"
        assert cond.find("REGULAR-EXPRESSION").text == "[a-z]*"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucStringParamDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucIntegerParamDef:
    def test_full(self, writer):
        container = _make_container()
        param = container.createEcucIntegerParamDef("P")
        param.setDefaultValue(_unlimited(10))
        param.setMax(_unlimited(100))
        param.setMin(_unlimited(0))
        parent = _parent()
        writer.writeEcucIntegerParamDef(parent, param)
        assert parent[0].tag == "ECUC-INTEGER-PARAM-DEF"
        assert parent[0].find("DEFAULT-VALUE").text == "10"
        assert parent[0].find("MAX").text == "100"
        assert parent[0].find("MIN").text == "0"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucIntegerParamDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucFloatParamDef:
    def test_full(self, writer):
        container = _make_container()
        param = container.createEcucFloatParamDef("P")
        param.setDefaultValue(_float(1.5))
        param.setMax(_limit(99.5, interval="CLOSED"))
        param.setMin(_limit(0.0, interval="CLOSED"))
        parent = _parent()
        writer.writeEcucFloatParamDef(parent, param)
        assert parent[0].tag == "ECUC-FLOAT-PARAM-DEF"
        assert parent[0].find("DEFAULT-VALUE").text == "1.5"
        assert parent[0].find("MAX").text == "99.5"
        assert parent[0].find("MIN").text == "0.0"
        assert parent[0].find("MAX").attrib["INTERVAL-TYPE"] == "CLOSED"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucFloatParamDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucEnumerationLiteralDef:
    def test_full(self, writer):
        container = _make_container()
        param = container.createEcucEnumerationParamDef("P")
        literal = param.createLiteral("Lit")
        literal.setOrigin(_literal("org"))
        parent = _parent()
        writer.writeEcucEnumerationLiteralDef(parent, literal)
        assert parent[0].tag == "ECUC-ENUMERATION-LITERAL-DEF"
        assert parent[0].find("SHORT-NAME").text == "Lit"
        assert parent[0].find("ORIGIN").text == "org"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucEnumerationLiteralDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucEnumerationParamDefLiterals:
    def test_with_literals(self, writer):
        container = _make_container()
        param = container.createEcucEnumerationParamDef("P")
        param.createLiteral("L1")
        param.createLiteral("L2")
        parent = _parent()
        writer.writeEcucEnumerationParamDefLiterals(parent, param)
        assert parent[0].tag == "LITERALS"
        lits = parent[0].findall("ECUC-ENUMERATION-LITERAL-DEF")
        assert len(lits) == 2

    def test_empty(self, writer):
        container = _make_container()
        param = container.createEcucEnumerationParamDef("P")
        parent = _parent()
        writer.writeEcucEnumerationParamDefLiterals(parent, param)
        assert len(parent) == 0


class TestWriterEcucEnumerationParamDef:
    def test_full(self, writer):
        container = _make_container()
        param = container.createEcucEnumerationParamDef("P")
        param.setDefaultValue(_literal("L1"))
        param.createLiteral("L1")
        parent = _parent()
        writer.writeEcucEnumerationParamDef(parent, param)
        assert parent[0].tag == "ECUC-ENUMERATION-PARAM-DEF"
        assert parent[0].find("DEFAULT-VALUE").text == "L1"
        assert parent[0].find("LITERALS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucEnumerationParamDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucFunctionNameDef:
    def test_full(self, writer):
        container = _make_container()
        param = container.createEcucFunctionNameDef("P")
        param.setDefaultValue(_verbatim("fn"))
        param.setMinLength(_posint(1))
        param.setMaxLength(_posint(64))
        param.setRegularExpression(_regex("[a-zA-Z_][a-zA-Z0-9_]*"))
        parent = _parent()
        writer.writeEcucFunctionNameDef(parent, param)
        assert parent[0].tag == "ECUC-FUNCTION-NAME-DEF"
        variants = parent[0].find("ECUC-FUNCTION-NAME-DEF-VARIANTS")
        assert variants is not None
        cond = variants.find("ECUC-FUNCTION-NAME-DEF-CONDITIONAL")
        assert cond is not None
        assert cond.find("DEFAULT-VALUE").text == "fn"
        assert cond.find("MIN-LENGTH").text == "1"
        assert cond.find("MAX-LENGTH").text == "64"
        assert cond.find("REGULAR-EXPRESSION").text == "[a-zA-Z_][a-zA-Z0-9_]*"


class TestWriterEcucMultilineStringParamDef:
    def test_full(self, writer):
        container = _make_container()
        param = container.createEcucMultilineStringParamDef("P")
        param.setDefaultValue(_verbatim("line1\nline2"))
        param.setMinLength(_posint(2))
        param.setMaxLength(_posint(200))
        parent = _parent()
        writer.writeEcucMultilineStringParamDef(parent, param)
        assert parent[0].tag == "ECUC-MULTILINE-STRING-PARAM-DEF"
        variants = parent[0].find("ECUC-MULTILINE-STRING-PARAM-DEF-VARIANTS")
        assert variants is not None
        cond = variants.find("ECUC-MULTILINE-STRING-PARAM-DEF-CONDITIONAL")
        assert cond is not None
        assert cond.find("DEFAULT-VALUE").text == "line1\nline2"
        assert cond.find("MIN-LENGTH").text == "2"
        assert cond.find("MAX-LENGTH").text == "200"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucFunctionNameDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucContainerDefParameters:
    def test_dispatches_all_param_types(self, writer):
        container = _make_container()
        container.createEcucBooleanParamDef("Bp")
        container.createEcucStringParamDef("Sp")
        container.createEcucIntegerParamDef("Ip")
        container.createEcucFloatParamDef("Fp")
        container.createEcucEnumerationParamDef("Ep")
        container.createEcucFunctionNameDef("Fn")
        container.createEcucMultilineStringParamDef("Mp")
        parent = _parent()
        writer.writeEcucContainerDefParameters(parent, container)
        assert parent[0].tag == "PARAMETERS"
        tags = {c.tag for c in parent[0]}
        assert "ECUC-BOOLEAN-PARAM-DEF" in tags
        assert "ECUC-STRING-PARAM-DEF" in tags
        assert "ECUC-INTEGER-PARAM-DEF" in tags
        assert "ECUC-FLOAT-PARAM-DEF" in tags
        assert "ECUC-ENUMERATION-PARAM-DEF" in tags
        assert "ECUC-FUNCTION-NAME-DEF" in tags
        assert "ECUC-MULTILINE-STRING-PARAM-DEF" in tags

    def test_empty(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainerDefParameters(parent, container)
        assert len(parent) == 0


class TestWriterEcucContainerDef:
    def test_full(self, writer):
        container = _make_container()
        uri_ref = EcucDestinationUriDefRefType()
        uri_ref.setValue("/Dest/Uri")
        uri_ref.setDest("ECUC-DESTINATION-URI-DEF")
        container.addDestinationUriRef(uri_ref)
        container.addMultiplicityConfigClass(EcucMultiplicityConfigurationClass().setConfigClass(_literal("mc")))
        container.setOrigin(_literal("MANUFACTURER"))
        container.setPostBuildVariantMultiplicity(_bool(True))
        container.setRequiresIndex(_bool(False))
        parent = _parent()
        writer.writeEcucContainerDef(parent, container)
        assert parent.find("DESTINATION-URI-REFS") is not None
        assert parent.find("DESTINATION-URI-REFS/DESTINATION-URI-REF").text == "/Dest/Uri"
        assert parent.find("DESTINATION-URI-REFS/DESTINATION-URI-REF").attrib["DEST"] == "ECUC-DESTINATION-URI-DEF"
        assert parent.find("MULTIPLICITY-CONFIG-CLASSES") is not None
        assert parent.find("ORIGIN").text == "MANUFACTURER"
        assert parent.find("POST-BUILD-VARIANT-MULTIPLICITY").text == "true"
        assert parent.find("REQUIRES-INDEX").text == "false"
        assert parent.find("MULTIPLE-CONFIGURATION-CONTAINER") is None

    def test_minimal(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainerDef(parent, container)
        assert parent.find("DESTINATION-URI-REFS") is None
        assert parent.find("MULTIPLICITY-CONFIG-CLASSES") is None
        assert parent.find("ORIGIN") is None
        assert parent.find("POST-BUILD-VARIANT-MULTIPLICITY") is None
        assert parent.find("REQUIRES-INDEX") is None
        assert parent.find("MULTIPLE-CONFIGURATION-CONTAINER") is None


class TestWriterEcucAbstractReferenceDef:
    def test_full(self, writer):
        container = _make_container()
        ref = container.createEcucReferenceDef("R")
        ref.setOrigin(_literal("org"))
        ref.setWithAuto(_bool(True))
        parent = _parent()
        writer.writeEcucAbstractReferenceDef(parent, ref)
        assert parent.find("ORIGIN").text == "org"
        assert parent.find("WITH-AUTO").text == "true"

    def test_omits_with_auto_when_none(self, writer):
        container = _make_container()
        ref = container.createEcucReferenceDef("R")
        parent = _parent()
        writer.writeEcucAbstractReferenceDef(parent, ref)
        assert parent.find("WITH-AUTO") is None


class TestWriterEcucAbstractInternalReferenceDef:
    def test_writes_inherited_attributes(self, writer):
        container = _make_container()
        ref = container.createEcucReferenceDef("R")
        ref.setRequiresSymbolicNameValue(_bool(True))
        parent = _parent()
        writer.writeEcucAbstractInternalReferenceDef(parent, ref)
        assert parent.find("REQUIRES-SYMBOLIC-NAME-VALUE").text == "true"

    def test_omits_requires_symbolic_name_value_when_none(self, writer):
        container = _make_container()
        ref = container.createEcucReferenceDef("R")
        parent = _parent()
        writer.writeEcucAbstractInternalReferenceDef(parent, ref)
        assert parent.find("REQUIRES-SYMBOLIC-NAME-VALUE") is None


class TestWriterEcucSymbolicNameReferenceDef:
    def test_full(self, writer):
        container = _make_container()
        ref = container.createEcucSymbolicNameReferenceDef("R")
        ref.setDestinationRef(_ref("/dst", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        parent = _parent()
        writer.writeEcucSymbolicNameReferenceDef(parent, ref)
        assert parent[0].tag == "ECUC-SYMBOLIC-NAME-REFERENCE-DEF"
        dst = parent[0].find("DESTINATION-REF")
        assert dst is not None
        assert dst.text == "/dst"
        assert dst.attrib["DEST"] == "ECUC-PARAM-CONF-CONTAINER-DEF"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucSymbolicNameReferenceDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucReferenceDef:
    def test_full(self, writer):
        container = _make_container()
        ref = container.createEcucReferenceDef("R")
        ref.setDestinationRef(_ref("/dst", "ECUC-REFERENCE-DEF"))
        parent = _parent()
        writer.writeEcucReferenceDef(parent, ref)
        assert parent[0].tag == "ECUC-REFERENCE-DEF"
        dst = parent[0].find("DESTINATION-REF")
        assert dst is not None
        assert dst.text == "/dst"
        assert dst.attrib["DEST"] == "ECUC-REFERENCE-DEF"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucReferenceDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucChoiceReferenceDef:
    def test_full(self, writer):
        container = _make_container()
        ref = container.createEcucChoiceReferenceDef("C")
        ref.addDestinationRef(_ref("/dst1", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        ref.addDestinationRef(_ref("/dst2", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        parent = _parent()
        writer.writeEcucChoiceReferenceDef(parent, ref)
        assert parent[0].tag == "ECUC-CHOICE-REFERENCE-DEF"
        dest_refs = parent[0].find("DESTINATION-REFS")
        assert dest_refs is not None
        refs = dest_refs.findall("DESTINATION-REF")
        assert len(refs) == 2
        assert refs[0].text == "/dst1"
        assert refs[0].attrib["DEST"] == "ECUC-PARAM-CONF-CONTAINER-DEF"
        assert refs[1].text == "/dst2"

    def test_omits_destination_refs_when_none(self, writer):
        container = _make_container()
        ref = container.createEcucChoiceReferenceDef("C")
        parent = _parent()
        writer.writeEcucChoiceReferenceDef(parent, ref)
        assert parent[0].find("DESTINATION-REFS") is None


class TestWriterEcucInstanceReferenceDef:
    def test_full(self, writer):
        container = _make_container()
        ref = container.createEcucInstanceReferenceDef("I")
        ref.setDestinationContext(_literal("SW-COMPONENT-PROTOTYPE R-PORT-PROTOTYPE"))
        ref.setDestinationType(_literal("VARIABLE-DATA-PROTOTYPE"))
        parent = _parent()
        writer.writeEcucInstanceReferenceDef(parent, ref)
        assert parent[0].tag == "ECUC-INSTANCE-REFERENCE-DEF"
        ctx = parent[0].find("DESTINATION-CONTEXT")
        assert ctx is not None
        assert ctx.text == "SW-COMPONENT-PROTOTYPE R-PORT-PROTOTYPE"
        typ = parent[0].find("DESTINATION-TYPE")
        assert typ is not None
        assert typ.text == "VARIABLE-DATA-PROTOTYPE"

    def test_omits_when_none(self, writer):
        container = _make_container()
        ref = container.createEcucInstanceReferenceDef("I")
        parent = _parent()
        writer.writeEcucInstanceReferenceDef(parent, ref)
        assert parent[0].find("DESTINATION-CONTEXT") is None
        assert parent[0].find("DESTINATION-TYPE") is None


class TestWriterEcucContainerDefReferences:
    def test_with_references(self, writer):
        container = _make_container()
        container.createEcucSymbolicNameReferenceDef("S")
        container.createEcucReferenceDef("R")
        parent = _parent()
        writer.writeEcucContainerDefReferences(parent, container)
        assert parent[0].tag == "REFERENCES"
        tags = {c.tag for c in parent[0]}
        assert "ECUC-SYMBOLIC-NAME-REFERENCE-DEF" in tags
        assert "ECUC-REFERENCE-DEF" in tags

    def test_empty(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainerDefReferences(parent, container)
        assert len(parent) == 0


class TestWriterEcucContainerDefSubContainers:
    def test_with_sub_containers(self, writer):
        container = _make_container()
        container.createEcucParamConfContainerDef("Sub1")
        container.createEcucChoiceContainerDef("Ch1")
        parent = _parent()
        writer.writeEcucContainerDefSubContainers(parent, container)
        assert parent[0].tag == "SUB-CONTAINERS"
        tags = {c.tag for c in parent[0]}
        assert "ECUC-PARAM-CONF-CONTAINER-DEF" in tags
        assert "ECUC-CHOICE-CONTAINER-DEF" in tags

    def test_empty(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainerDefSubContainers(parent, container)
        assert len(parent) == 0


class TestWriterEcucParamConfContainerDef:
    def test_full(self, writer):
        container = _make_container()
        container.createEcucBooleanParamDef("Bp")
        container.createEcucReferenceDef("R")
        container.createEcucParamConfContainerDef("Sub")
        parent = _parent()
        writer.writeEcucParamConfContainerDef(parent, container)
        assert parent[0].tag == "ECUC-PARAM-CONF-CONTAINER-DEF"
        assert parent[0].find("PARAMETERS") is not None
        assert parent[0].find("REFERENCES") is not None
        assert parent[0].find("SUB-CONTAINERS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucParamConfContainerDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucChoiceContainerDefChoices:
    def test_with_choices(self, writer):
        module = _make_module()
        choice = module.createEcucChoiceContainerDef("Ch")
        choice.createEcucParamConfContainerDef("Opt1")
        choice.createEcucParamConfContainerDef("Opt2")
        parent = _parent()
        writer.writeEcucChoiceContainerDefChoices(parent, choice)
        assert parent[0].tag == "CHOICES"
        opts = parent[0].findall("ECUC-PARAM-CONF-CONTAINER-DEF")
        assert len(opts) == 2

    def test_empty(self, writer):
        module = _make_module()
        choice = module.createEcucChoiceContainerDef("Ch")
        parent = _parent()
        writer.writeEcucChoiceContainerDefChoices(parent, choice)
        assert len(parent) == 0


class TestWriterEcucChoiceContainerDef:
    def test_full(self, writer):
        module = _make_module()
        choice = module.createEcucChoiceContainerDef("Ch")
        choice.createEcucParamConfContainerDef("Opt1")
        parent = _parent()
        writer.writeEcucChoiceContainerDef(parent, choice)
        assert parent[0].tag == "ECUC-CHOICE-CONTAINER-DEF"
        assert parent[0].find("CHOICES") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucChoiceContainerDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucModuleDefContainers:
    def test_with_containers(self, writer):
        module = _make_module()
        module.createEcucParamConfContainerDef("C1")
        module.createEcucChoiceContainerDef("C2")
        parent = _parent()
        writer.writeEcucModuleDefContainers(parent, module)
        assert parent[0].tag == "CONTAINERS"
        tags = {c.tag for c in parent[0]}
        assert "ECUC-PARAM-CONF-CONTAINER-DEF" in tags
        assert "ECUC-CHOICE-CONTAINER-DEF" in tags

    def test_empty(self, writer):
        module = _make_module()
        parent = _parent()
        writer.writeEcucModuleDefContainers(parent, module)
        assert len(parent) == 1
        assert parent[0].tag == "CONTAINERS"
        assert len(parent[0]) == 0


class TestWriterEcucModuleDef:
    def test_full(self, writer):
        module = _make_module()
        module.setPostBuildVariantSupport(_bool(True))
        module.addSupportedConfigVariant(_literal("v1"))
        module.createEcucParamConfContainerDef("C1")
        module.createEcucChoiceContainerDef("C2")
        parent = _parent()
        writer.writeEcucModuleDef(parent, module)
        assert parent[0].tag == "ECUC-MODULE-DEF"
        assert parent[0].find("SHORT-NAME").text == "Mod"
        assert parent[0].find("POST-BUILD-VARIANT-SUPPORT").text == "true"
        assert parent[0].find("SUPPORTED-CONFIG-VARIANTS") is not None
        assert parent[0].find("CONTAINERS") is not None

    def test_full_with_api_service_prefix_and_refined(self, writer):
        module = _make_module()
        prefix = CIdentifier()
        prefix.setValue("Cdd")
        module.setApiServicePrefix(prefix)
        module.setRefinedModuleDefRef(_ref("/Pkg/StMd", dest="ECUC-MODULE-DEF"))
        parent = _parent()
        writer.writeEcucModuleDef(parent, module)
        assert parent[0].tag == "ECUC-MODULE-DEF"
        assert parent[0].find("API-SERVICE-PREFIX").text == "Cdd"
        refined = parent[0].find("REFINED-MODULE-DEF-REF")
        assert refined is not None
        assert refined.text == "/Pkg/StMd"
        assert refined.attrib.get("DEST") == "ECUC-MODULE-DEF"

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucModuleDef(parent, None)
        assert len(parent) == 0


class TestWriterEcucDefinitionCollection:
    def test_full(self, writer):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        collection = EcucDefinitionCollection(pkg, "Coll")
        collection.addModuleRef(_ref("/Pkg/Mod", dest="ECUC-MODULE-DEF"))
        parent = _parent()
        writer.writeEcucDefinitionCollection(parent, collection)
        assert parent[0].tag == "ECUC-DEFINITION-COLLECTION"
        assert parent[0].find("SHORT-NAME").text == "Coll"
        refs = parent[0].findall("MODULE-REFS/MODULE-REF")
        assert len(refs) == 1
        assert refs[0].text == "/Pkg/Mod"
        assert refs[0].attrib.get("DEST") == "ECUC-MODULE-DEF"

    def test_empty(self, writer):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        collection = EcucDefinitionCollection(pkg, "Coll")
        parent = _parent()
        writer.writeEcucDefinitionCollection(parent, collection)
        assert parent[0].tag == "ECUC-DEFINITION-COLLECTION"
        assert parent[0].find("MODULE-REFS") is None

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucDefinitionCollection(parent, None)
        assert len(parent) == 0


# ==================== EcucDestinationUriPolicy (Table 2.36) writer round-trip ====================


class TestEcucDestinationUriPolicyWriter:
    """Writer round-trip for EcucDestinationUriDefSet -> Def -> Policy (Tables 2.34-2.36)."""

    def _round_trip(self, build):
        import os
        import tempfile

        from armodel.parser.arxml_parser import ARXMLParser

        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("UriDefSetPkg")
        build(pkg)
        with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            ARXMLWriter().save(tmp_path, autosar)
            AUTOSAR.getInstance().new()
            AUTOSAR.getInstance().setARRelease("R23-11")
            ARXMLParser().load(tmp_path, AUTOSAR.getInstance())
            reloaded_pkg = AUTOSAR.getInstance().getARPackages()[0]
            return reloaded_pkg
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

    def test_write_full_policy(self, writer):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
            EcucBooleanParamDef,
            EcucDestinationUriDefSet,
            EcucDestinationUriNestingContractEnum,
            EcucDestinationUriPolicy,
            EcucParamConfContainerDef,
            EcucReferenceDef,
        )

        def build(pkg):
            uri_def_set = pkg.createEcucDestinationUriDefSet("UriDefSet")
            uri_def = uri_def_set.createEcucDestinationUriDef("Uri1")
            policy = EcucDestinationUriPolicy()
            container = EcucParamConfContainerDef(policy, "TargetContainer")
            policy.addContainer(container)
            contract = EcucDestinationUriNestingContractEnum()
            contract.setValue(EcucDestinationUriNestingContractEnum.TARGET_CONTAINER)
            policy.setDestinationUriNestingContract(contract)
            param = EcucBooleanParamDef(policy, "InterestingParam1")
            policy.addParameter(param)
            ref = EcucReferenceDef(policy, "Ref1")
            policy.addReference(ref)
            uri_def.setDestinationUriPolicy(policy)

        reloaded_pkg = self._round_trip(build)
        uri_def_set = reloaded_pkg.getElement("UriDefSet", EcucDestinationUriDefSet)
        assert uri_def_set is not None
        uri_def = uri_def_set.getDestinationUriDefs()[0]
        assert uri_def.getShortName() == "Uri1"
        policy = uri_def.getDestinationUriPolicy()
        assert policy is not None
        assert len(policy.getContainers()) == 1
        assert policy.getContainers()[0].getShortName() == "TargetContainer"
        assert policy.getDestinationUriNestingContract().getValue() == EcucDestinationUriNestingContractEnum.TARGET_CONTAINER
        assert len(policy.getParameters()) == 1
        assert policy.getParameters()[0].getShortName() == "InterestingParam1"
        assert len(policy.getReferences()) == 1
        assert policy.getReferences()[0].getShortName() == "Ref1"

    def test_write_empty_policy(self, writer):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
            EcucDestinationUriDefSet,
            EcucDestinationUriPolicy,
        )

        def build(pkg):
            uri_def_set = pkg.createEcucDestinationUriDefSet("UriDefSet")
            uri_def = uri_def_set.createEcucDestinationUriDef("Uri2")
            policy = EcucDestinationUriPolicy()
            uri_def.setDestinationUriPolicy(policy)

        reloaded_pkg = self._round_trip(build)
        uri_def_set = reloaded_pkg.getElement("UriDefSet", EcucDestinationUriDefSet)
        uri_def = uri_def_set.getDestinationUriDefs()[0]
        policy = uri_def.getDestinationUriPolicy()
        assert policy is not None
        assert policy.getContainers() == []
        assert policy.getParameters() == []
        assert policy.getReferences() == []
        assert policy.getDestinationUriNestingContract() is None

    def test_write_no_policy(self, writer):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
            EcucDestinationUriDefSet,
        )

        def build(pkg):
            uri_def_set = pkg.createEcucDestinationUriDefSet("UriDefSet")
            uri_def_set.createEcucDestinationUriDef("Uri3")

        reloaded_pkg = self._round_trip(build)
        uri_def_set = reloaded_pkg.getElement("UriDefSet", EcucDestinationUriDefSet)
        uri_def = uri_def_set.getDestinationUriDefs()[0]
        assert uri_def.getDestinationUriPolicy() is None
