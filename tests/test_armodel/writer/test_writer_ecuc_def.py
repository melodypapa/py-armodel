"""Tests for writer ECUC parameter definition handlers."""
import xml.etree.cElementTree as ET
import pytest

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucBooleanParamDef,
    EcucChoiceContainerDef,
    EcucEnumerationLiteralDef,
    EcucEnumerationParamDef,
    EcucFloatParamDef,
    EcucFunctionNameDef,
    EcucIntegerParamDef,
    EcucModuleDef,
    EcucMultiplicityConfigurationClass,
    EcucParamConfContainerDef,
    EcucReferenceDef,
    EcucStringParamDef,
    EcucSymbolicNameReferenceDef,
    EcucValueConfigurationClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa E501
    ARBoolean,
    ARLiteral,
    Float,
    Limit,
    PositiveInteger,
    RefType,
    UnlimitedInteger,
    VerbatimString,
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
        param.addMultiplicityConfigClass(
            EcucMultiplicityConfigurationClass().setConfigClass(
                _literal("mc")
            )
        )
        param.setOrigin(_literal("org"))
        param.setPostBuildVariantMultiplicity(_bool(True))
        param.setPostBuildVariantValue(_bool(False))
        param.setRequiresIndex(_bool(True))
        param.addValueConfigClass(
            EcucValueConfigurationClass().setConfigVariant(_literal("vc"))
        )
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
        parent = _parent()
        writer.writeEcucStringParamDef(parent, param)
        assert parent[0].tag == "ECUC-STRING-PARAM-DEF"

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

    def test_empty(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainerDefParameters(parent, container)
        assert len(parent) == 0


class TestWriterEcucContainerDef:
    def test_full(self, writer):
        container = _make_container()
        container.addMultiplicityConfigClass(
            EcucMultiplicityConfigurationClass().setConfigClass(
                _literal("mc")
            )
        )
        container.setPostBuildVariantMultiplicity(_bool(True))
        container.setRequiresIndex(_bool(False))
        container.setMultipleConfigurationContainer(_bool(True))
        parent = _parent()
        writer.writeEcucContainerDef(parent, container)
        assert parent.find("MULTIPLICITY-CONFIG-CLASSES") is not None
        assert parent.find("POST-BUILD-VARIANT-MULTIPLICITY").text == "true"
        assert parent.find("REQUIRES-INDEX").text == "false"
        assert (
            parent.find("MULTIPLE-CONFIGURATION-CONTAINER").text == "true"
        )

    def test_minimal(self, writer):
        container = _make_container()
        parent = _parent()
        writer.writeEcucContainerDef(parent, container)
        assert parent.find("MULTIPLICITY-CONFIG-CLASSES") is None
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


class TestWriterEcucAbstractInternalReferenceDef:
    def test_writes_inherited_attributes(self, writer):
        container = _make_container()
        ref = container.createEcucReferenceDef("R")
        ref.setWithAuto(_bool(True))
        parent = _parent()
        writer.writeEcucAbstractInternalReferenceDef(parent, ref)
        assert parent.find("WITH-AUTO").text == "true"


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
        assert len(parent) == 0


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
        assert (
            parent[0].find("POST-BUILD-VARIANT-SUPPORT").text == "true"
        )
        assert parent[0].find("SUPPORTED-CONFIG-VARIANTS") is not None
        assert parent[0].find("CONTAINERS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeEcucModuleDef(parent, None)
        assert len(parent) == 0
