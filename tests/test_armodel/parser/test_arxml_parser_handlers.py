"""Phase E: targeted tests for uncovered handler methods in ARXMLParser.

Each test directly invokes a single handler method on `ARXMLParser` with a
minimal XML snippet, lifting coverage on specific read*/get* bodies that the
dispatch tests in test_arxml_parser_dispatch.py only route around.

Coverage focus (from term-missing report on arxml_parser.py):
    Group A — core element helpers (lines 325-424)
    Group B — SwComponentType / SwConnector (lines 2095-2384)
    Group C — DataTypes & ValueSpecs (lines 1903-1997)
    Group D — Port interfaces & CompuMethod (lines 2522-2581)
    Group E — BswBehavior orchestrators (lines 815-871)
"""

import logging
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    """Parser configured in warning mode (logs instead of raising)."""
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    """Return the AUTOSAR singleton for use as a parent in model constructors."""
    return AUTOSAR.getInstance()


# ==================== Group D: Port interfaces & CompuMethod ====================


class TestPortInterfaceAndCompuHandlers:
    """Exercise readClientServerInterface and CompuMethod helpers."""

    def test_readClientServerInterface_minimal(self, warning_parser):
        from armodel.models import ClientServerInterface

        csi = ClientServerInterface(parent=_autosar_root(), short_name="csi")
        element = _snip(
            "<SHORT-NAME>csi</SHORT-NAME>",
            root_tag="CLIENT-SERVER-INTERFACE",
        )
        warning_parser.readClientServerInterface(element, csi)
        assert csi.getShortName() == "csi"

    def test_getCompuConstContent_VF_branch(self, parser):
        from armodel.models import CompuConstFormulaContent

        element = _snip("<VF>formula</VF>", root_tag="PARENT")
        content = parser.getCompuConstContent(element)
        assert isinstance(content, CompuConstFormulaContent)
        assert content.getVf().getValue() == "formula"

    def test_getCompuConstContent_V_branch(self, parser):
        from armodel.models import CompuConstNumericContent

        element = _snip("<V>42</V>", root_tag="PARENT")
        content = parser.getCompuConstContent(element)
        assert isinstance(content, CompuConstNumericContent)
        assert content.getV().getValue() == 42

    def test_getCompuConstContent_VT_branch(self, parser):
        from armodel.models import CompuConstTextContent

        element = _snip("<VT>label</VT>", root_tag="PARENT")
        content = parser.getCompuConstContent(element)
        assert isinstance(content, CompuConstTextContent)
        assert content.getVt().getValue() == "label"

    def test_getCompuConstContent_unsupported_tag_warns(self, warning_parser, caplog):
        element = _snip("<BAD-TAG>x</BAD-TAG>", root_tag="PARENT")
        with caplog.at_level(logging.ERROR):
            content = warning_parser.getCompuConstContent(element)
        assert content is None
        assert any("Unsupported CompuConstContent" in r.getMessage() for r in caplog.records)

    def test_getCompuConstContent_empty_returns_None(self, parser):
        element = _snip("", root_tag="PARENT")
        assert parser.getCompuConstContent(element) is None

    def test_getCompuConst_wraps_content(self, parser):
        element = _snip("<CC><VT>hello</VT></CC>", root_tag="PARENT")
        compu_const = parser.getCompuConst(element, "CC")
        assert compu_const is not None
        assert compu_const.getCompuConstContentType() is not None

    def test_getCompuConst_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getCompuConst(element, "CC") is None

    def test_readCompuConst_VT_branch(self, parser):
        from armodel.models import CompuScale

        scale = CompuScale()
        element = _snip(
            "<COMPU-CONST><VT>label</VT></COMPU-CONST>",
            root_tag="SCALE",
        )
        parser.readCompuConst(element, scale)
        assert scale.compuScaleContents is not None
        contents = scale.compuScaleContents
        assert contents.compuConst is not None
        assert contents.compuConst.compuConstContentType.vt.getValue() == "label"

    def test_readCompuConst_no_VT_skips(self, parser):
        from armodel.models import CompuScale

        scale = CompuScale()
        scale.compuScaleContents = None  # ensure starting state
        element = _snip("", root_tag="SCALE")
        parser.readCompuConst(element, scale)
        # compuScaleContents should remain unset (None).
        assert scale.compuScaleContents is None

    def test_readCompuNominatorDenominator_adds_V(self, parser):
        from armodel.models import CompuNominatorDenominator

        cnd = CompuNominatorDenominator()
        element = _snip(
            "<COMPU-NUMERATOR><V>1</V><V>2</V><V>3</V></COMPU-NUMERATOR>",
            root_tag="PARENT",
        )
        parser.readCompuNominatorDenominator(
            element, "COMPU-NUMERATOR", cnd
        )
        assert len(cnd.get_vs()) == 3

    def test_readCompuNominatorDenominator_empty(self, parser):
        from armodel.models import CompuNominatorDenominator

        cnd = CompuNominatorDenominator()
        element = _snip("<COMPU-NUMERATOR/>", root_tag="PARENT")
        parser.readCompuNominatorDenominator(element, "COMPU-NUMERATOR", cnd)
        assert len(cnd.get_vs()) == 0

    def test_readCompuRationCoeffs_populates_contents(self, parser):
        from armodel.models import CompuScale, CompuScaleRationalFormula

        scale = CompuScale()
        element = _snip(
            "<COMPU-RATIONAL-COEFFS>"
            "<COMPU-DENOMINATOR><V>1</V></COMPU-DENOMINATOR>"
            "<COMPU-NUMERATOR><V>2</V><V>3</V></COMPU-NUMERATOR>"
            "</COMPU-RATIONAL-COEFFS>",
            root_tag="SCALE",
        )
        parser.readCompuRationCoeffs(element, scale)
        assert isinstance(scale.compuScaleContents, CompuScaleRationalFormula)
        coeffs = scale.compuScaleContents.compuRationalCoeffs
        assert coeffs is not None
        assert len(coeffs.compuDenominator.get_vs()) == 1
        assert len(coeffs.compuNumerator.get_vs()) == 2

    def test_readCompuRationCoeffs_missing_no_op(self, parser):
        from armodel.models import CompuScale

        scale = CompuScale()
        scale.compuScaleContents = None
        element = _snip("", root_tag="SCALE")
        parser.readCompuRationCoeffs(element, scale)
        assert scale.compuScaleContents is None


# ==================== Group A: AdminData & Referrable helpers ====================


class TestAdminDataAndReferrableHandlers:
    """Exercise getAdminData, readReferrable, readIdentifiable, multilanguage
    helpers, and InstanceRef builders."""

    def test_getAdminData_full(self, parser):
        element = _snip(
            "<ADMIN-DATA>"
            "<LANGUAGE>EN</LANGUAGE>"
            "<USED-LANGUAGES><L-4>EN</L-4></USED-LANGUAGES>"
            "<SDGS><SDG GID='G'><SD>x</SD></SDG></SDGS>"
            "<DOC-REVISIONS>"
            "<DOC-REVISION>"
            "<ISSUED-BY>alice</ISSUED-BY>"
            "<REVISION-LABEL>1.0.0</REVISION-LABEL>"
            "</DOC-REVISION>"
            "</DOC-REVISIONS>"
            "</ADMIN-DATA>",
            root_tag="PARENT",
        )
        admin = parser.getAdminData(element, "ADMIN-DATA")
        assert admin is not None
        assert admin.getLanguage().getValue() == "EN"
        assert len(admin.getSdgs()) == 1
        assert len(admin.getDocRevisions()) == 1

    def test_getAdminData_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getAdminData(element, "ADMIN-DATA") is None

    def test_readReferrable_minimal(self, parser):
        from armodel.models import BswVariableAccess

        obj = BswVariableAccess(parent=_autosar_root(), short_name="va")
        element = _snip("", root_tag="ELEM")
        elem = ET.fromstring(
            f"<ELEM xmlns='{NS}' UUID='abc' T='2024-01-01T00:00:00'/>"
        )
        parser.readReferrable(elem, obj)
        assert obj.uuid == "abc"
        assert obj.timestamp == "2024-01-01T00:00:00"

    def test_readMultilanguageReferrable_sets_longName(self, parser):
        # Use a concrete MultilanguageReferrable subclass (Unit extends ARElement
        # extends Identifiable extends MultilanguageReferrable).
        from armodel.models import Unit

        obj = Unit(parent=_autosar_root(), short_name="u")
        element = _snip(
            "<LONG-NAME><L-4 L='EN'>MyLong</L-4></LONG-NAME>",
            root_tag="ELEM",
        )
        parser.readMultilanguageReferrable(element, obj)
        assert obj.getLongName() is not None

    def test_readIdentifiable_populates_category_desc_admin(self, parser):
        from armodel.models import Unit

        obj = Unit(parent=_autosar_root(), short_name="u")
        element = _snip(
            "<CATEGORY>CAT_A</CATEGORY>"
            "<DESC><L-2 L='EN'>desc</L-2></DESC>"
            "<INTRODUCTION><L-1>intro</L-1></INTRODUCTION>"
            "<ADMIN-DATA><LANGUAGE>EN</LANGUAGE></ADMIN-DATA>",
            root_tag="ELEM",
        )
        parser.readIdentifiable(element, obj)
        assert obj.getCategory().getValue() == "CAT_A"
        assert obj.getDesc() is not None
        assert obj.getAdminData() is not None
        assert obj.getAdminData().getLanguage().getValue() == "EN"

    def test_readIdentifiable_with_annotation(self, parser):
        from armodel.models import Unit

        obj = Unit(parent=_autosar_root(), short_name="u")
        element = _snip(
            "<ANNOTATIONS>"
            "<ANNOTATION>"
            "<LABEL><L-4>note</L-4></LABEL>"
            "<TEXT><L-1>body</L-1></TEXT>"
            "</ANNOTATION>"
            "</ANNOTATIONS>",
            root_tag="ELEM",
        )
        parser.readIdentifiable(element, obj)
        assert len(obj.getAnnotations()) == 1

    def test_readARElement_delegates_to_readIdentifiable(self, parser):
        from armodel.models import Unit

        obj = Unit(parent=_autosar_root(), short_name="u")
        element = _snip("<CATEGORY>CAT_A</CATEGORY>", root_tag="ELEM")
        parser.readARElement(element, obj)
        assert obj.getCategory().getValue() == "CAT_A"

    def test_getMultilanguageLongName_multiple_L4(self, parser):
        element = _snip(
            "<LONG-NAME>"
            "<L-4 L='EN'>a</L-4>"
            "<L-4 L='DE'>b</L-4>"
            "</LONG-NAME>",
            root_tag="PARENT",
        )
        long_name = parser.getMultilanguageLongName(element, "LONG-NAME")
        assert long_name is not None
        # readLLongName adds each L-4 via addL4.
        assert len(long_name.getL4s()) == 2

    def test_getMultilanguageLongName_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getMultilanguageLongName(element, "LONG-NAME") is None

    def test_getMultiLanguageOverviewParagraph_with_L2(self, parser):
        element = _snip(
            "<DESC><L-2 L='EN'>overview</L-2></DESC>",
            root_tag="PARENT",
        )
        paragraph = parser.getMultiLanguageOverviewParagraph(element, "DESC")
        assert paragraph is not None
        assert len(paragraph.getL2s()) == 1

    def test_getVariableInAtomicSWCTypeInstanceRef_full(self, parser):
        element = _snip(
            "<AUTOSAR-VARIABLE-IREF>"
            "<PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/p1</PORT-PROTOTYPE-REF>"
            "<TARGET-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/td1</TARGET-DATA-PROTOTYPE-REF>"
            "</AUTOSAR-VARIABLE-IREF>",
            root_tag="PARENT",
        )
        iref = parser.getVariableInAtomicSWCTypeInstanceRef(
            parser.find(element, "AUTOSAR-VARIABLE-IREF")
        )
        assert iref is not None
        assert iref.getPortPrototypeRef().getValue() == "/p1"
        assert iref.getTargetDataPrototypeRef().getValue() == "/td1"

    def test_getVariableInAtomicSWCTypeInstanceRef_none_element(self, parser):
        assert parser.getVariableInAtomicSWCTypeInstanceRef(None) is None

    def test_getComponentInSystemInstanceRef_full(self, parser):
        element = _snip(
            "<COMPONENT-IREF>"
            "<BASE-REF DEST='X'>/b</BASE-REF>"
            "<CONTEXT-COMPOSITION-REF DEST='COMPOSITION-SW-COMPONENT-TYPE'>/c</CONTEXT-COMPOSITION-REF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/t</TARGET-COMPONENT-REF>"
            "</COMPONENT-IREF>",
            root_tag="PARENT",
        )
        iref = parser.getComponentInSystemInstanceRef(
            parser.find(element, "COMPONENT-IREF")
        )
        assert iref is not None
        assert iref.getBaseRef().getValue() == "/b"
        assert iref.getContextCompositionRef().getValue() == "/c"
        assert iref.getTargetComponentRef().getValue() == "/t"

    def test_getAutosarVariableRef_with_iref(self, parser):
        element = _snip(
            "<ACCESSED-VARIABLE>"
            "<AUTOSAR-VARIABLE-IREF>"
            "<PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/p1</PORT-PROTOTYPE-REF>"
            "<TARGET-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/td1</TARGET-DATA-PROTOTYPE-REF>"
            "</AUTOSAR-VARIABLE-IREF>"
            "<LOCAL-VARIABLE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/lv</LOCAL-VARIABLE-REF>"
            "</ACCESSED-VARIABLE>",
            root_tag="PARENT",
        )
        ref = parser.getAutosarVariableRef(element, "ACCESSED-VARIABLE")
        assert ref is not None
        assert ref.getLocalVariableRef().getValue() == "/lv"
        assert ref.getAutosarVariableIRef() is not None


# ==================== Group C: DataTypes & ValueSpecs ====================


class TestDataTypeAndValueSpecHandlers:
    """Exercise readImplementationDataType, readSwBaseType, SwValues,
    ValueList, SwValueCont, ApplicationValueSpecification, and
    getChildValueSpecification."""

    def test_readSwBaseType_full(self, parser):
        from armodel.models import SwBaseType

        bt = SwBaseType(parent=_autosar_root(), short_name="bt")
        # Per AUTOSAR schema, BASE-TYPE-* children live directly under SW-BASE-TYPE
        # (no BASE-TYPE-DEFINITION wrapper). See tests/integration_tests/test_files.
        element = _snip(
            "<SHORT-NAME>bt</SHORT-NAME>"
            "<BASE-TYPE-SIZE>32</BASE-TYPE-SIZE>"
            "<BASE-TYPE-ENCODING>IEEE754</BASE-TYPE-ENCODING>"
            "<BYTE-ORDER>BIG-ENDIAN</BYTE-ORDER>"
            "<MEM-ALIGNMENT>4</MEM-ALIGNMENT>"
            "<NATIVE-DECLARATION>float</NATIVE-DECLARATION>",
            root_tag="SW-BASE-TYPE",
        )
        parser.readSwBaseType(element, bt)
        definition = bt.getBaseTypeDefinition()
        assert definition.getBaseTypeSize().getValue() == 32
        assert definition.getNativeDeclaration().getValue() == "float"
        assert definition.getByteOrder().getValue() == "BIG-ENDIAN"

    def test_readBaseTypeDirectDefinition_empty(self, parser):
        from armodel.models import BaseTypeDirectDefinition

        definition = BaseTypeDirectDefinition()
        element = _snip("<X/>")
        parser.readBaseTypeDirectDefinition(element, definition)
        assert definition.getBaseTypeSize() is None
        assert definition.getBaseTypeEncoding() is None
        assert definition.getByteOrder() is None
        assert definition.getMemAlignment() is None
        assert definition.getNativeDeclaration() is None

    def test_readImplementationDataType_minimal(self, parser):
        from armodel.models import ImplementationDataType

        idt = ImplementationDataType(parent=_autosar_root(), short_name="idt")
        element = _snip(
            "<SHORT-NAME>idt</SHORT-NAME>", root_tag="IMPLEMENTATION-DATA-TYPE"
        )
        parser.readImplementationDataType(element, idt)
        assert idt.getDynamicArraySizeProfile() is None
        assert idt.getTypeEmitter() is None

    def test_readImplementationDataType_with_typeEmitter_and_profile(self, parser):
        from armodel.models import ImplementationDataType

        idt = ImplementationDataType(parent=_autosar_root(), short_name="idt")
        element = _snip(
            "<SHORT-NAME>idt</SHORT-NAME>"
            "<DYNAMIC-ARRAY-SIZE-PROFILE>VAR</DYNAMIC-ARRAY-SIZE-PROFILE>"
            "<TYPE-EMITTER>HAL</TYPE-EMITTER>",
            root_tag="IMPLEMENTATION-DATA-TYPE",
        )
        parser.readImplementationDataType(element, idt)
        assert idt.getDynamicArraySizeProfile().getValue() == "VAR"
        assert idt.getTypeEmitter().getValue() == "HAL"

    def test_readImplementationDataType_with_symbol_props(self, parser):
        from armodel.models import ImplementationDataType

        idt = ImplementationDataType(parent=_autosar_root(), short_name="idt")
        element = _snip(
            "<SHORT-NAME>idt</SHORT-NAME>"
            "<SYMBOL-PROPS>"
            "<SHORT-NAME>sp</SHORT-NAME>"
            "</SYMBOL-PROPS>",
            root_tag="IMPLEMENTATION-DATA-TYPE",
        )
        parser.readImplementationDataType(element, idt)
        # Symbol props are stored on the data type; verify at least no exception.
        assert idt.getShortName() == "idt"

    def test_readImplementationDataTypeSubElements_unsupported_tag_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ImplementationDataType

        idt = ImplementationDataType(parent=_autosar_root(), short_name="idt")
        element = _snip(
            "<SUB-ELEMENTS><BAD-ELEMENT/></SUB-ELEMENTS>",
            root_tag="IMPLEMENTATION-DATA-TYPE",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readImplementationDataTypeSubElements(element, idt)
        assert any(
            "Unsupported ImplementationDataType SubElement" in r.getMessage()
            for r in caplog.records
        )

    def test_getSwValues_with_V_and_VT(self, parser):
        element = _snip(
            "<SW-VALUES-PHYS>"
            "<V>1.0</V>"
            "<V>2.0</V>"
            "<VT>label</VT>"
            "</SW-VALUES-PHYS>",
            root_tag="PARENT",
        )
        sw_values = parser.getSwValues(element, "SW-VALUES-PHYS")
        assert sw_values is not None
        assert len(sw_values.getVs()) == 2
        assert sw_values.vt.getValue() == "label"

    def test_getSwValues_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getSwValues(element, "SW-VALUES-PHYS") is None

    def test_getValueList_present(self, parser):
        element = _snip(
            "<SW-ARRAYSIZE><V>4</V></SW-ARRAYSIZE>", root_tag="PARENT"
        )
        value_list = parser.getValueList(element, "SW-ARRAYSIZE")
        assert value_list is not None
        # ValueList stores a single V (ARFloat).
        assert value_list.getV() is not None
        assert float(value_list.getV().getValue()) == 4.0

    def test_getValueList_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getValueList(element, "SW-ARRAYSIZE") is None

    def test_getSwValueCont_full(self, parser):
        element = _snip(
            "<SW-VALUE-CONT>"
            "<UNIT-REF DEST='UNIT'>/u</UNIT-REF>"
            "<SW-ARRAYSIZE><V>2</V></SW-ARRAYSIZE>"
            "<SW-VALUES-PHYS><V>1.0</V></SW-VALUES-PHYS>"
            "</SW-VALUE-CONT>",
            root_tag="PARENT",
        )
        cont = parser.getSwValueCont(element)
        assert cont is not None
        assert cont.getUnitRef().getValue() == "/u"
        assert cont.getSwArraysize() is not None
        assert cont.getSwValuesPhys() is not None
        assert len(cont.getSwValuesPhys().getVs()) == 1

    def test_getSwValueCont_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getSwValueCont(element) is None

    def test_readApplicationValueSpecification_populates_fields(self, parser):
        from armodel.models import ApplicationValueSpecification

        value_spec = ApplicationValueSpecification()
        value_spec.short_name = "vs"  # required by readValueSpecification path
        element = _snip(
            "<SHORT-NAME>vs</SHORT-NAME>"
            "<CATEGORY>CAT</CATEGORY>"
            "<SW-VALUE-CONT>"
            "<UNIT-REF DEST='UNIT'>/u</UNIT-REF>"
            "</SW-VALUE-CONT>",
            root_tag="APPLICATION-VALUE-SPECIFICATION",
        )
        parser.readApplicationValueSpecification(element, value_spec)
        assert value_spec.getCategory().getValue() == "CAT"
        assert value_spec.getSwValueCont() is not None
        assert value_spec.getSwValueCont().getUnitRef().getValue() == "/u"

    def test_getChildValueSpecification_present(self, parser):
        from armodel.models import NumericalValueSpecification

        element = _snip(
            "<INIT-VALUE>"
            "<NUMERICAL-VALUE-SPECIFICATION>"
            "<SHORT-NAME>n</SHORT-NAME>"
            "<VALUE>42</VALUE>"
            "</NUMERICAL-VALUE-SPECIFICATION>"
            "</INIT-VALUE>",
            root_tag="PARENT",
        )
        value_spec = parser.getChildValueSpecification(element, "INIT-VALUE")
        assert value_spec is not None
        assert isinstance(value_spec, NumericalValueSpecification)

    def test_getChildValueSpecification_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getChildValueSpecification(element, "INIT-VALUE") is None


# ==================== Group B: SwComponentType & Connectors ====================


class TestSwComponentAndConnectorHandlers:
    """Exercise readSwComponentTypePorts, readSwComponentPrototype,
    readSwConnector family, readCompositionSwComponentTypeDataTypeMappingSet,
    and readDataTypeMaps."""

    @pytest.fixture
    def composition(self):
        from armodel.models import CompositionSwComponentType

        return CompositionSwComponentType(parent=_autosar_root(), short_name="Comp")

    def test_readSwComponentTypePorts_creates_PPort(self, parser, composition):
        element = _snip(
            "<PORTS>"
            "<P-PORT-PROTOTYPE><SHORT-NAME>pp1</SHORT-NAME></P-PORT-PROTOTYPE>"
            "</PORTS>",
            root_tag="COMP",
        )
        parser.readSwComponentTypePorts(element, composition)
        assert len(composition.getPPortPrototypes()) == 1

    def test_readSwComponentTypePorts_creates_RPort(self, parser, composition):
        element = _snip(
            "<PORTS>"
            "<R-PORT-PROTOTYPE><SHORT-NAME>rp1</SHORT-NAME></R-PORT-PROTOTYPE>"
            "</PORTS>",
            root_tag="COMP",
        )
        parser.readSwComponentTypePorts(element, composition)
        assert len(composition.getRPortPrototypes()) == 1

    def test_readSwComponentTypePorts_creates_PRPort(self, parser, composition):
        element = _snip(
            "<PORTS>"
            "<PR-PORT-PROTOTYPE><SHORT-NAME>prp1</SHORT-NAME></PR-PORT-PROTOTYPE>"
            "</PORTS>",
            root_tag="COMP",
        )
        parser.readSwComponentTypePorts(element, composition)
        assert len(composition.getPRPortPrototypes()) == 1

    def test_readSwComponentTypePorts_unsupported_tag_warns(
        self, warning_parser, composition, caplog
    ):
        element = _snip(
            "<PORTS><BAD-PORT/></PORTS>", root_tag="COMP"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwComponentTypePorts(element, composition)
        assert any(
            "Unsupported Port Prototype" in r.getMessage()
            for r in caplog.records
        )

    def test_readSwComponentPrototype_sets_typeTRef(self, parser, composition):
        prototype = composition.createSwComponentPrototype("cp1")
        element = _snip(
            "<SHORT-NAME>cp1</SHORT-NAME>"
            "<TYPE-TREF DEST='COMPOSITION-SW-COMPONENT-TYPE'>/t</TYPE-TREF>",
            root_tag="SW-COMPONENT-PROTOTYPE",
        )
        parser.readSwComponentPrototype(element, prototype)
        assert prototype.getTypeTRef().getValue() == "/t"

    def test_readAssemblySwConnector_with_provider_and_requester(
        self, parser, composition
    ):
        connector = composition.createAssemblySwConnector("a1")
        element = _snip(
            "<SHORT-NAME>a1</SHORT-NAME>"
            "<PROVIDER-IREF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/c1</CONTEXT-COMPONENT-REF>"
            "<TARGET-P-PORT-REF DEST='P-PORT-PROTOTYPE'>/pp1</TARGET-P-PORT-REF>"
            "</PROVIDER-IREF>"
            "<REQUESTER-IREF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/c2</CONTEXT-COMPONENT-REF>"
            "<TARGET-R-PORT-REF DEST='R-PORT-PROTOTYPE'>/rp1</TARGET-R-PORT-REF>"
            "</REQUESTER-IREF>",
            root_tag="ASSEMBLY-SW-CONNECTOR",
        )
        parser.readAssemblySwConnector(element, connector)
        assert connector.getProviderIRef() is not None
        assert connector.getProviderIRef().getTargetPPortRef().getValue() == "/pp1"
        assert connector.getRequesterIRef() is not None
        assert connector.getRequesterIRef().getTargetRPortRef().getValue() == "/rp1"

    def test_readAssemblySwConnector_without_IRefs(self, parser, composition):
        connector = composition.createAssemblySwConnector("a2")
        element = _snip(
            "<SHORT-NAME>a2</SHORT-NAME>", root_tag="ASSEMBLY-SW-CONNECTOR"
        )
        parser.readAssemblySwConnector(element, connector)
        assert connector.getProviderIRef() is None
        assert connector.getRequesterIRef() is None

    def test_readSwConnector_sets_mappingRef(self, parser, composition):
        connector = composition.createAssemblySwConnector("a3")
        element = _snip(
            "<SHORT-NAME>a3</SHORT-NAME>"
            "<MAPPING-REF DEST='X'>/m</MAPPING-REF>",
            root_tag="ASSEMBLY-SW-CONNECTOR",
        )
        parser.readAssemblySwConnector(element, connector)
        assert connector.getMappingRef().getValue() == "/m"

    def test_readDelegationSwConnector_inner_RPort_IRef(
        self, parser, composition
    ):
        connector = composition.createDelegationSwConnector("d1")
        element = _snip(
            "<SHORT-NAME>d1</SHORT-NAME>"
            "<INNER-PORT-IREF>"
            "<R-PORT-IN-COMPOSITION-INSTANCE-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/c</CONTEXT-COMPONENT-REF>"
            "<TARGET-R-PORT-REF DEST='R-PORT-PROTOTYPE'>/rp</TARGET-R-PORT-REF>"
            "</R-PORT-IN-COMPOSITION-INSTANCE-REF>"
            "</INNER-PORT-IREF>"
            "<OUTER-PORT-REF DEST='PORT-PROTOTYPE'>/op</OUTER-PORT-REF>",
            root_tag="DELEGATION-SW-CONNECTOR",
        )
        parser.readDelegationSwConnector(element, connector)
        assert connector.getInnerPortIRref() is not None
        assert connector.getOuterPortRef().getValue() == "/op"

    def test_readDelegationSwConnector_inner_PPort_IRef(
        self, parser, composition
    ):
        connector = composition.createDelegationSwConnector("d2")
        element = _snip(
            "<SHORT-NAME>d2</SHORT-NAME>"
            "<INNER-PORT-IREF>"
            "<P-PORT-IN-COMPOSITION-INSTANCE-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/c</CONTEXT-COMPONENT-REF>"
            "<TARGET-P-PORT-REF DEST='P-PORT-PROTOTYPE'>/pp</TARGET-P-PORT-REF>"
            "</P-PORT-IN-COMPOSITION-INSTANCE-REF>"
            "</INNER-PORT-IREF>"
            "<OUTER-PORT-REF DEST='PORT-PROTOTYPE'>/op</OUTER-PORT-REF>",
            root_tag="DELEGATION-SW-CONNECTOR",
        )
        parser.readDelegationSwConnector(element, connector)
        assert connector.getInnerPortIRref() is not None
        assert connector.getOuterPortRef().getValue() == "/op"

    def test_readDelegationSwConnector_only_inner_ref(self, parser, composition):
        # Note: readDelegationSwConnector checks getInnerPortIRref() AND
        # getOuterPortRef() for None *before* OUTER-PORT-REF is parsed, so the
        # only way to avoid the raise is to supply an INNER-PORT-IREF.
        connector = composition.createDelegationSwConnector("d3")
        element = _snip(
            "<SHORT-NAME>d3</SHORT-NAME>"
            "<INNER-PORT-IREF>"
            "<R-PORT-IN-COMPOSITION-INSTANCE-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/c</CONTEXT-COMPONENT-REF>"
            "<TARGET-R-PORT-REF DEST='R-PORT-PROTOTYPE'>/rp</TARGET-R-PORT-REF>"
            "</R-PORT-IN-COMPOSITION-INSTANCE-REF>"
            "</INNER-PORT-IREF>",
            root_tag="DELEGATION-SW-CONNECTOR",
        )
        parser.readDelegationSwConnector(element, connector)
        assert connector.getInnerPortIRref() is not None
        # OUTER-PORT-REF was absent; should remain None.
        assert connector.getOuterPortRef() is None

    def test_readDelegationSwConnector_both_missing_warns(
        self, warning_parser, composition, caplog
    ):
        connector = composition.createDelegationSwConnector("d4")
        element = _snip(
            "<SHORT-NAME>d4</SHORT-NAME>", root_tag="DELEGATION-SW-CONNECTOR"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readDelegationSwConnector(element, connector)
        assert any(
            "Invalid PortPrototype of DELEGATION-SW-CONNECTOR" in r.getMessage()
            for r in caplog.records
        )

    def test_readCompositionSwComponentTypeDataTypeMappingSet_adds_refs(
        self, parser, composition
    ):
        element = _snip(
            "<DATA-TYPE-MAPPING-REFS>"
            "<DATA-TYPE-MAPPING-REF DEST='DATA-TYPE-MAPPING-SET'>/dtm1</DATA-TYPE-MAPPING-REF>"
            "<DATA-TYPE-MAPPING-REF DEST='DATA-TYPE-MAPPING-SET'>/dtm2</DATA-TYPE-MAPPING-REF>"
            "</DATA-TYPE-MAPPING-REFS>",
            root_tag="COMP",
        )
        parser.readCompositionSwComponentTypeDataTypeMappingSet(element, composition)
        assert len(composition.getDataTypeMappings()) == 2

    def test_readCompositionSwComponentTypeDataTypeMappingSet_missing_no_op(
        self, parser, composition
    ):
        element = _snip("<X/>")
        parser.readCompositionSwComponentTypeDataTypeMappingSet(element, composition)
        assert len(composition.getDataTypeMappings()) == 0

    def test_readDataTypeMaps_adds_to_parent_and_global(self, parser):
        from armodel.models import DataTypeMappingSet

        dtms = DataTypeMappingSet(parent=_autosar_root(), short_name="DTMS")
        element = _snip(
            "<DATA-TYPE-MAPS>"
            "<DATA-TYPE-MAP>"
            "<APPLICATION-DATA-TYPE-REF DEST='APPLICATION-DATA-TYPE'>/adt</APPLICATION-DATA-TYPE-REF>"
            "<IMPLEMENTATION-DATA-TYPE-REF DEST='IMPLEMENTATION-DATA-TYPE'>/idt</IMPLEMENTATION-DATA-TYPE-REF>"
            "</DATA-TYPE-MAP>"
            "</DATA-TYPE-MAPS>",
            root_tag="DATA-TYPE-MAPPING-SET",
        )
        parser.readDataTypeMaps(element, dtms)
        assert len(dtms.getDataTypeMaps()) == 1


# ==================== Group E: BswBehavior orchestrators ====================


class TestBswBehaviorOrchestratorHandlers:
    """Exercise readSwcInternalBehavior (top-level cascade), readBswVariableAccess,
    and the readBswModuleEntityDataSendPoints/DataReceiverPoints dispatchers."""

    def test_readSwcInternalBehavior_minimal(self, warning_parser):
        from armodel.models import ApplicationSwComponentType

        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="a")
        behavior = app.createSwcInternalBehavior("ib")
        element = _snip(
            "<SHORT-NAME>ib</SHORT-NAME>", root_tag="SWC-INTERNAL-BEHAVIOR"
        )
        warning_parser.readSwcInternalBehavior(element, behavior)
        # The two end-of-method optional fields should be None with empty body.
        assert behavior.getHandleTerminationAndRestart() is None
        assert behavior.getSupportsMultipleInstantiation() is None

    def test_readSwcInternalBehavior_with_optional_literals(self, warning_parser):
        from armodel.models import ApplicationSwComponentType

        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="a")
        behavior = app.createSwcInternalBehavior("ib")
        element = _snip(
            "<SHORT-NAME>ib</SHORT-NAME>"
            "<HANDLE-TERMINATION-AND-RESTART>YES</HANDLE-TERMINATION-AND-RESTART>"
            "<SUPPORTS-MULTIPLE-INSTANTIATION>true</SUPPORTS-MULTIPLE-INSTANTIATION>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        warning_parser.readSwcInternalBehavior(element, behavior)
        assert behavior.getHandleTerminationAndRestart().getValue() == "YES"
        assert behavior.getSupportsMultipleInstantiation() is not None

    def test_readBswVariableAccess_sets_ref(self, parser):
        from armodel.models import BswVariableAccess

        access = BswVariableAccess(parent=_autosar_root(), short_name="va")
        element = _snip(
            "<SHORT-NAME>va</SHORT-NAME>"
            "<ACCESSED-VARIABLE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/v</ACCESSED-VARIABLE-REF>",
            root_tag="BSW-VARIABLE-ACCESS",
        )
        parser.readBswVariableAccess(element, access)
        assert access.getAccessedVariableRef().getValue() == "/v"

    def test_readBswVariableAccess_missing_ref_is_None(self, parser):
        from armodel.models import BswVariableAccess

        access = BswVariableAccess(parent=_autosar_root(), short_name="va")
        element = _snip(
            "<SHORT-NAME>va</SHORT-NAME>", root_tag="BSW-VARIABLE-ACCESS"
        )
        parser.readBswVariableAccess(element, access)
        assert access.getAccessedVariableRef() is None

    def test_readBswModuleEntityDataSendPoints_creates_point(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bib")
        entity = behavior.createBswSchedulableEntity("e1")
        element = _snip(
            "<DATA-SEND-POINTS>"
            "<BSW-VARIABLE-ACCESS><SHORT-NAME>s1</SHORT-NAME></BSW-VARIABLE-ACCESS>"
            "</DATA-SEND-POINTS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntityDataSendPoints(element, entity)
        assert len(entity.getDataSendPoints()) == 1

    def test_readBswModuleEntityDataSendPoints_unsupported_tag_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bib")
        entity = behavior.createBswSchedulableEntity("e1")
        element = _snip(
            "<DATA-SEND-POINTS><BAD/></DATA-SEND-POINTS>", root_tag="ENTITY"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleEntityDataSendPoints(element, entity)
        assert any(
            "Unsupported Data Send Point" in r.getMessage()
            for r in caplog.records
        )

    def test_readBswModuleEntityDataReceiverPoints_creates_point(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bib")
        entity = behavior.createBswSchedulableEntity("e1")
        element = _snip(
            "<DATA-RECEIVE-POINTS>"
            "<BSW-VARIABLE-ACCESS><SHORT-NAME>r1</SHORT-NAME></BSW-VARIABLE-ACCESS>"
            "</DATA-RECEIVE-POINTS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntityDataReceiverPoints(element, entity)
        assert len(entity.getDataReceivePoints()) == 1

    def test_readBswModuleEntityDataReceiverPoints_unsupported_tag_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bib")
        entity = behavior.createBswSchedulableEntity("e1")
        element = _snip(
            "<DATA-RECEIVE-POINTS><BAD/></DATA-RECEIVE-POINTS>", root_tag="ENTITY"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleEntityDataReceiverPoints(element, entity)
        assert any(
            "Unsupported Data Receive Point" in r.getMessage()
            for r in caplog.records
        )
