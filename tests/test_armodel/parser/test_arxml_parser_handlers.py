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
from unittest.mock import MagicMock

import pytest

from armodel.models import (
    AUTOSAR,
    ApplicationSwComponentType,
    CompositionSwComponentType,
    InstanceEventInCompositionInstanceRef,
    InstantiationTimingEventProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthTcpIpIcmpProps, EthTcpIpProps, TcpIpIcmpv4Props, TcpIpIcmpv6Props, TcpProps, UdpProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import OsTaskPreemptabilityEnum, OsTaskProxy
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

        element = _snip("<VF>42</VF>", root_tag="PARENT")
        content = parser.getCompuConstContent(element)
        assert isinstance(content, CompuConstFormulaContent)
        from armodel.models import ARNumerical

        assert isinstance(content.getVf(), ARNumerical)
        assert content.getVf().getValue() == 42

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
        from armodel.models import VerbatimString

        assert isinstance(content.getVt(), VerbatimString)
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

    def test_readCompuScale_reads_a2l_and_inverse_value(self, parser):
        from armodel.models import CompuScale

        scale = CompuScale()
        element = _snip(
            "<A2L-DISPLAY-TEXT>display</A2L-DISPLAY-TEXT>" "<COMPU-INVERSE-VALUE><VT>inverse</VT></COMPU-INVERSE-VALUE>",
            root_tag="SCALE",
        )
        parser.readCompuScale(element, scale)
        assert scale.getA2lDisplayText().getValue() == "display"
        assert scale.getCompuInverseValue().getCompuConstContentType().getVt().getValue() == "inverse"

    def test_readCompuNominatorDenominator_adds_V(self, parser):
        from armodel.models import CompuNominatorDenominator

        cnd = CompuNominatorDenominator()
        element = _snip(
            "<COMPU-NUMERATOR><V>1</V><V>2</V><V>3</V></COMPU-NUMERATOR>",
            root_tag="PARENT",
        )
        parser.readCompuNominatorDenominator(element, "COMPU-NUMERATOR", cnd)
        assert [str(v) for v in cnd.getVs()] == ["1", "2", "3"]

    def test_readCompuNominatorDenominator_empty(self, parser):
        from armodel.models import CompuNominatorDenominator

        cnd = CompuNominatorDenominator()
        element = _snip("<COMPU-NUMERATOR/>", root_tag="PARENT")
        parser.readCompuNominatorDenominator(element, "COMPU-NUMERATOR", cnd)
        assert cnd.getVs() == []

    def test_readCompuRationCoeffs_populates_contents(self, parser):
        from armodel.models import CompuScale, CompuScaleRationalFormula

        scale = CompuScale()
        element = _snip(
            "<COMPU-RATIONAL-COEFFS>" "<COMPU-DENOMINATOR><V>1</V></COMPU-DENOMINATOR>" "<COMPU-NUMERATOR><V>2</V><V>3</V></COMPU-NUMERATOR>" "</COMPU-RATIONAL-COEFFS>",
            root_tag="SCALE",
        )
        parser.readCompuRationCoeffs(element, scale)
        assert isinstance(scale.compuScaleContents, CompuScaleRationalFormula)
        coeffs = scale.compuScaleContents.compuRationalCoeffs
        assert coeffs is not None
        assert [str(v) for v in coeffs.compuDenominator.getVs()] == ["1"]
        assert [str(v) for v in coeffs.compuNumerator.getVs()] == ["2", "3"]

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

    def test_readDocRevision_sets_revision_label_predecessors(self, parser):
        from armodel.models.M2.MSR.AsamHdo.AdminData import DocRevision

        element = _snip(
            "<DOC-REVISION>" "<REVISION-LABEL>1.0.0</REVISION-LABEL>" "<REVISION-LABEL-P-1>0.9.0</REVISION-LABEL-P-1>" "<REVISION-LABEL-P-2>0.8.0</REVISION-LABEL-P-2>" "</DOC-REVISION>",
            root_tag="PARENT",
        )
        revision = DocRevision()
        child = parser.find(element, "DOC-REVISION")
        parser.readDocRevision(child, revision)
        assert revision.getRevisionLabel().getValue() == "1.0.0"
        assert revision.getRevisionLabelP1().getValue() == "0.9.0"
        assert revision.getRevisionLabelP2().getValue() == "0.8.0"

    def test_readEcucEnumerationLiteral_sets_ecucCond(self, parser):
        from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucEnumerationLiteralDef

        element = _snip(
            "<ECUC-ENUMERATION-LITERAL-DEF>"
            "<SHORT-NAME>Lit</SHORT-NAME>"
            "<ECUC-COND><INFORMAL-FORMULA><L-1>cond</L-1></INFORMAL-FORMULA></ECUC-COND>"
            "<ORIGIN>AUTOSAR_ECUC</ORIGIN>"
            "</ECUC-ENUMERATION-LITERAL-DEF>",
            root_tag="PARENT",
        )
        literal = EcucEnumerationLiteralDef(parent=None, short_name="Lit")
        child = parser.find(element, "ECUC-ENUMERATION-LITERAL-DEF")
        parser.readEcucEnumerationLiteral(child, literal)
        assert literal.getOrigin().getValue() == "AUTOSAR_ECUC"
        # Spec Table 2.24: ecucCond aggr must be read from ECUC-COND
        assert literal.getEcucCond() is not None
        assert literal.getEcucCond().getInformalFormula() is not None

    def test_readReferrable_minimal(self, parser):
        from armodel.models import BswVariableAccess

        obj = BswVariableAccess(parent=_autosar_root(), short_name="va")
        _element = _snip("", root_tag="ELEM")
        elem = ET.fromstring(f"<ELEM xmlns='{NS}' UUID='abc' T='2024-01-01T00:00:00'/>")
        parser.readReferrable(elem, obj)
        # Since the uuid move (Group1.md work order), uuid is owned by Identifiable;
        # BswVariableAccess is a Referrable (not Identifiable) so the UUID attribute
        # is not stored, while T still round-trips.
        assert not hasattr(obj, "uuid")
        assert obj.getTimestamp().getValue() == "2024-01-01T00:00:00"

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

    def test_readSingleLanguageReferrable_sets_longName1(self, parser):
        from armodel.models import SingleLanguageReferrable

        class ConcreteSingleLanguageReferrable(SingleLanguageReferrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteSingleLanguageReferrable(_autosar_root(), "sl")
        element = _snip(
            "<LONG-NAME-1>MyLong</LONG-NAME-1>",
            root_tag="ELEM",
        )
        parser.readSingleLanguageReferrable(element, obj)
        assert obj.getLongName1() is not None
        assert obj.getLongName1().getValue().getValue() == "MyLong"

    def test_readSingleLanguageReferrable_parses_long_name1_inline(self, parser):
        from armodel.models import SingleLanguageReferrable

        class ConcreteSingleLanguageReferrable(SingleLanguageReferrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteSingleLanguageReferrable(_autosar_root(), "sl")
        element = _snip(
            "<LONG-NAME-1 SUP='2'>H2O</LONG-NAME-1>",
            root_tag="ELEM",
        )
        parser.readSingleLanguageReferrable(element, obj)
        assert obj.getLongName1().getValue().getValue() == "H2O"
        assert obj.getLongName1().getSup().getValue() == "2"

    def test_readSingleLanguageReferrable_without_long_name1(self, parser):
        from armodel.models import SingleLanguageReferrable

        class ConcreteSingleLanguageReferrable(SingleLanguageReferrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteSingleLanguageReferrable(_autosar_root(), "sl")
        element = _snip("<SHORT-NAME>sl</SHORT-NAME>", root_tag="ELEM")
        parser.readSingleLanguageReferrable(element, obj)
        assert obj.getLongName1() is None

    def test_readIdentifiable_populates_category_desc_admin(self, parser):
        from armodel.models import Unit

        obj = Unit(parent=_autosar_root(), short_name="u")
        element = _snip(
            "<CATEGORY>CAT_A</CATEGORY>" "<DESC><L-2 L='EN'>desc</L-2></DESC>" "<INTRODUCTION><L-1>intro</L-1></INTRODUCTION>" "<ADMIN-DATA><LANGUAGE>EN</LANGUAGE></ADMIN-DATA>",
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
            "<ANNOTATIONS>" "<ANNOTATION>" "<LABEL><L-4>note</L-4></LABEL>" "<TEXT><L-1>body</L-1></TEXT>" "</ANNOTATION>" "</ANNOTATIONS>",
            root_tag="ELEM",
        )
        parser.readIdentifiable(element, obj)
        assert len(obj.getAnnotations()) == 1

    def test_readIdentifiable_empty_annotations_wrapper(self, parser):
        from armodel.models import Unit

        obj = Unit(parent=_autosar_root(), short_name="u")
        element = _snip("<ANNOTATIONS/>", root_tag="ELEM")
        parser.readIdentifiable(element, obj)
        assert obj.getAnnotations() == []

    def test_readARElement_delegates_to_readIdentifiable(self, parser):
        from armodel.models import Unit

        obj = Unit(parent=_autosar_root(), short_name="u")
        element = _snip("<CATEGORY>CAT_A</CATEGORY>", root_tag="ELEM")
        parser.readARElement(element, obj)
        assert obj.getCategory().getValue() == "CAT_A"

    def test_getMultilanguageLongName_multiple_L4(self, parser):
        element = _snip(
            "<LONG-NAME>" "<L-4 L='EN'>a</L-4>" "<L-4 L='DE'>b</L-4>" "</LONG-NAME>",
            root_tag="PARENT",
        )
        long_name = parser.getMultilanguageLongName(element, "LONG-NAME")
        assert long_name is not None
        # readLLongName adds each L-4 via addL4.
        assert len(long_name.getL4s()) == 2

    def test_getMultilanguageLongName_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getMultilanguageLongName(element, "LONG-NAME") is None

    def test_getMultilanguageLongName_parses_l4_fields(self, parser):
        element = _snip(
            "<LONG-NAME>" "<L-4 L='EN'>Engine</L-4>" "<L-4 L='DE'>Motor</L-4>" "</LONG-NAME>",
            root_tag="PARENT",
        )
        long_name = parser.getMultilanguageLongName(element, "LONG-NAME")
        assert long_name is not None
        l4s = long_name.getL4s()
        assert len(l4s) == 2
        assert l4s[0].getValue() == "Engine"
        assert l4s[0].getL() == "EN"
        assert l4s[1].getValue() == "Motor"
        assert l4s[1].getL() == "DE"

    def test_getSingleLanguageLongName_parses_value_and_inline(self, parser):
        element = _snip(
            "<LONG-NAME-1>Engine<TT TYPE='VARIABLE'>term</TT></LONG-NAME-1>",
            root_tag="PARENT",
        )
        long_name = parser.getSingleLanguageLongName(element, "LONG-NAME-1")
        assert long_name is not None
        assert long_name.getValue().getValue() == "Engine"
        assert long_name.getTt() is not None
        assert long_name.getTt().getValue().getValue() == "term"

    def test_getSingleLanguageLongName_parses_sup_sub(self, parser):
        element = _snip(
            "<LONG-NAME-1 SUP='2' SUB='3'>H2O</LONG-NAME-1>",
            root_tag="PARENT",
        )
        long_name = parser.getSingleLanguageLongName(element, "LONG-NAME-1")
        assert long_name.getValue().getValue() == "H2O"
        assert long_name.getSup().getValue() == "2"
        assert long_name.getSub().getValue() == "3"

    def test_getSingleLanguageLongName_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getSingleLanguageLongName(element, "LONG-NAME-1") is None

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
        iref = parser.getVariableInAtomicSWCTypeInstanceRef(parser.find(element, "AUTOSAR-VARIABLE-IREF"))
        assert iref is not None
        assert iref.getPortPrototypeRef().getValue() == "/p1"
        assert iref.getTargetDataPrototypeRef().getValue() == "/td1"
        assert iref.getTargetDataPrototypeRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

    def test_getVariableInAtomicSWCTypeInstanceRef_none_element(self, parser):
        assert parser.getVariableInAtomicSWCTypeInstanceRef(None) is None

    def test_getParameterInAtomicSWCTypeInstanceRef_full(self, parser):
        element = _snip(
            "<AUTOSAR-PARAMETER-IREF>"
            "<BASE-REF DEST='ATOMIC-SW-COMPONENT-TYPE'>/b</BASE-REF>"
            "<PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/p1</PORT-PROTOTYPE-REF>"
            "<ROOT-PARAMETER-DATA-PROTOTYPE-REF DEST='DATA-PROTOTYPE'>/r1</ROOT-PARAMETER-DATA-PROTOTYPE-REF>"
            "<CONTEXT-DATA-PROTOTYPE-REF DEST='APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE'>/c1</CONTEXT-DATA-PROTOTYPE-REF>"
            "<TARGET-DATA-PROTOTYPE-REF DEST='DATA-PROTOTYPE'>/t1</TARGET-DATA-PROTOTYPE-REF>"
            "</AUTOSAR-PARAMETER-IREF>",
            root_tag="PARENT",
        )
        iref = parser.getParameterInAtomicSWCTypeInstanceRef(element, "AUTOSAR-PARAMETER-IREF")
        assert iref is not None
        # base is <<atpDerived>> and must NOT be read from BASE-REF
        assert iref.getBaseRef() is None
        assert iref.getPortPrototypeRef().getValue() == "/p1"
        assert iref.getRootParameterDataPrototypeRef().getValue() == "/r1"
        ctx = iref.getContextDataPrototypeRefs()
        assert len(ctx) == 1 and ctx[0].getValue() == "/c1"
        assert iref.getTargetDataPrototypeRef().getValue() == "/t1"

    def test_getParameterInAtomicSWCTypeInstanceRef_none_element(self, parser):
        assert parser.getParameterInAtomicSWCTypeInstanceRef(_snip(""), "AUTOSAR-PARAMETER-IREF") is None

    def test_getComponentInSystemInstanceRef_full(self, parser):
        element = _snip(
            "<COMPONENT-IREF>"
            "<BASE-REF DEST='X'>/b</BASE-REF>"
            "<CONTEXT-COMPOSITION-REF DEST='COMPOSITION-SW-COMPONENT-TYPE'>/c</CONTEXT-COMPOSITION-REF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/t</TARGET-COMPONENT-REF>"
            "</COMPONENT-IREF>",
            root_tag="PARENT",
        )
        iref = parser.getComponentInSystemInstanceRef(parser.find(element, "COMPONENT-IREF"))
        assert iref is not None
        assert iref.getBaseRef().getValue() == "/b"
        assert iref.getContextCompositionRef().getValue() == "/c"
        assert iref.getTargetComponentRef().getValue() == "/t"

    def test_getOperationInSystemInstanceRef_full(self, parser):
        element = _snip(
            "<OPERATION-IREF>"
            "<BASE-REF DEST='COMPOSITION-SW-COMPONENT-TYPE'>/b</BASE-REF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/comp</CONTEXT-COMPOSITION-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/c1</CONTEXT-COMPONENT-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/c2</CONTEXT-COMPONENT-REF>"
            "<CONTEXT-PORT-REF DEST='PORT-PROTOTYPE'>/port</CONTEXT-PORT-REF>"
            "<TARGET-OPERATION-REF DEST='CLIENT-SERVER-OPERATION'>/op</TARGET-OPERATION-REF>"
            "</OPERATION-IREF>",
            root_tag="PARENT",
        )
        iref = parser.getOperationInSystemInstanceRef(parser.find(element, "OPERATION-IREF"))
        assert iref is not None
        assert iref.getBaseRef().getValue() == "/b"
        assert iref.getBaseRef().getDest() == "COMPOSITION-SW-COMPONENT-TYPE"
        assert iref.getContextCompositionRef().getValue() == "/comp"
        assert iref.getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
        ctx = iref.getContextComponentRefs()
        assert len(ctx) == 2
        assert [r.getValue() for r in ctx] == ["/c1", "/c2"]
        assert all(r.getDest() == "SW-COMPONENT-PROTOTYPE" for r in ctx)
        assert iref.getContextPortRef().getValue() == "/port"
        assert iref.getTargetOperationRef().getValue() == "/op"
        assert iref.getTargetOperationRef().getDest() == "CLIENT-SERVER-OPERATION"

    def test_getOperationInSystemInstanceRef_empty(self, parser):
        element = _snip(
            "<OPERATION-IREF>" "<TARGET-OPERATION-REF DEST='CLIENT-SERVER-OPERATION'>/op</TARGET-OPERATION-REF>" "</OPERATION-IREF>",
            root_tag="PARENT",
        )
        iref = parser.getOperationInSystemInstanceRef(parser.find(element, "OPERATION-IREF"))
        assert iref is not None
        assert iref.getBaseRef() is None
        assert iref.getContextCompositionRef() is None
        assert iref.getContextComponentRefs() == []
        assert iref.getContextPortRef() is None
        assert iref.getTargetOperationRef().getValue() == "/op"

    def test_getOperationInSystemInstanceRef_none_element(self, parser):
        assert parser.getOperationInSystemInstanceRef(None) is None

    def test_readClientIdDefinition_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinition

        id_definition = ClientIdDefinition(parent=_autosar_root(), short_name="CID1")
        element = _snip(
            "<CLIENT-ID>5</CLIENT-ID>"
            "<CLIENT-SERVER-OPERATION-IREF>"
            "<CONTEXT-PORT-REF DEST='R-PORT-PROTOTYPE'>/port</CONTEXT-PORT-REF>"
            "<TARGET-OPERATION-REF DEST='CLIENT-SERVER-OPERATION'>/op</TARGET-OPERATION-REF>"
            "</CLIENT-SERVER-OPERATION-IREF>",
            root_tag="CLIENT-ID-DEFINITION",
        )
        parser.readClientIdDefinition(element, id_definition)
        assert id_definition.getClientId().getValue() == "5"
        iref = id_definition.getClientServerOperationIRef()
        assert iref is not None
        assert iref.getContextPortRef().getValue() == "/port"
        assert iref.getTargetOperationRef().getValue() == "/op"
        assert iref.getTargetOperationRef().getDest() == "CLIENT-SERVER-OPERATION"

    def test_readClientIdDefinition_client_id_only(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinition

        id_definition = ClientIdDefinition(parent=_autosar_root(), short_name="CID1")
        element = _snip("<CLIENT-ID>7</CLIENT-ID>", root_tag="CLIENT-ID-DEFINITION")
        parser.readClientIdDefinition(element, id_definition)
        assert id_definition.getClientId().getValue() == "7"
        assert id_definition.getClientServerOperationIRef() is None

    def test_readClientIdDefinition_empty(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinition

        id_definition = ClientIdDefinition(parent=_autosar_root(), short_name="CID1")
        element = _snip("", root_tag="CLIENT-ID-DEFINITION")
        parser.readClientIdDefinition(element, id_definition)
        assert id_definition.getClientId() is None
        assert id_definition.getClientServerOperationIRef() is None

    def test_readClientIdDefinitionSet_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinitionSet

        id_definition_set = ClientIdDefinitionSet(parent=_autosar_root(), short_name="IDS1")
        element = _snip(
            "<CLIENT-ID-DEFINITIONS>"
            "<CLIENT-ID-DEFINITION><SHORT-NAME>CID1</SHORT-NAME><CLIENT-ID>5</CLIENT-ID></CLIENT-ID-DEFINITION>"
            "<CLIENT-ID-DEFINITION><SHORT-NAME>CID2</SHORT-NAME><CLIENT-ID>7</CLIENT-ID></CLIENT-ID-DEFINITION>"
            "</CLIENT-ID-DEFINITIONS>",
            root_tag="CLIENT-ID-DEFINITION-SET",
        )
        parser.readClientIdDefinitionSet(element, id_definition_set)
        definitions = id_definition_set.getClientIdDefinitions()
        assert len(definitions) == 2
        assert definitions[0].getShortName() == "CID1"
        assert definitions[0].getClientId().getValue() == "5"
        assert definitions[1].getShortName() == "CID2"
        assert definitions[1].getClientId().getValue() == "7"

    def test_readClientIdDefinitionSet_empty_wrapper(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinitionSet

        id_definition_set = ClientIdDefinitionSet(parent=_autosar_root(), short_name="IDS1")
        element = _snip("<CLIENT-ID-DEFINITIONS/>", root_tag="CLIENT-ID-DEFINITION-SET")
        parser.readClientIdDefinitionSet(element, id_definition_set)
        assert id_definition_set.getClientIdDefinitions() == []

    def test_readClientIdDefinitionSet_no_wrapper(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ClientIdDefinitionSet

        id_definition_set = ClientIdDefinitionSet(parent=_autosar_root(), short_name="IDS1")
        element = _snip("", root_tag="CLIENT-ID-DEFINITION-SET")
        parser.readClientIdDefinitionSet(element, id_definition_set)
        assert id_definition_set.getClientIdDefinitions() == []

    def test_readInterpolationRoutine_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration import InterpolationRoutine

        routine = InterpolationRoutine()
        element = _snip(
            "<SHORT-LABEL>LinearInterpolation</SHORT-LABEL>"
            "<IS-DEFAULT>true</IS-DEFAULT>"
            '<INTERPOLATION-ROUTINE-REF DEST="BSW-MODULE-ENTRY">/BswM/BswEntries/InterpolationEntry</INTERPOLATION-ROUTINE-REF>',
            root_tag="INTERPOLATION-ROUTINE",
        )
        parser.readInterpolationRoutine(element, routine)
        assert routine.getShortLabel().getValue() == "LinearInterpolation"
        assert routine.getIsDefault().getValue() is True
        assert routine.getInterpolationRoutineRef().getDest() == "BSW-MODULE-ENTRY"
        assert routine.getInterpolationRoutineRef().getValue() == "/BswM/BswEntries/InterpolationEntry"

    def test_readInterpolationRoutine_empty(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration import InterpolationRoutine

        routine = InterpolationRoutine()
        element = _snip("", root_tag="INTERPOLATION-ROUTINE")
        parser.readInterpolationRoutine(element, routine)
        assert routine.getShortLabel() is None
        assert routine.getIsDefault() is None
        assert routine.getInterpolationRoutineRef() is None

    def test_readInterpolationRoutineMapping_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration import InterpolationRoutineMapping

        mapping = InterpolationRoutineMapping()
        element = _snip(
            "<INTERPOLATION-ROUTINES>"
            "<INTERPOLATION-ROUTINE>"
            "<SHORT-LABEL>LinearInterpolation</SHORT-LABEL>"
            '<INTERPOLATION-ROUTINE-REF DEST="BSW-MODULE-ENTRY">/BswM/BswEntries/InterpolationEntry</INTERPOLATION-ROUTINE-REF>'
            "</INTERPOLATION-ROUTINE>"
            "<INTERPOLATION-ROUTINE>"
            "<SHORT-LABEL>TableLookup</SHORT-LABEL>"
            "</INTERPOLATION-ROUTINE>"
            "</INTERPOLATION-ROUTINES>"
            '<SW-RECORD-LAYOUT-REF DEST="SW-RECORD-LAYOUT">/Package/SwRecordLayouts/Layout1</SW-RECORD-LAYOUT-REF>',
            root_tag="INTERPOLATION-ROUTINE-MAPPING",
        )
        parser.readInterpolationRoutineMapping(element, mapping)
        routines = mapping.getInterpolationRoutines()
        assert len(routines) == 2
        assert routines[0].getShortLabel().getValue() == "LinearInterpolation"
        assert routines[0].getInterpolationRoutineRef().getValue() == "/BswM/BswEntries/InterpolationEntry"
        assert routines[1].getShortLabel().getValue() == "TableLookup"
        assert mapping.getSwRecordLayoutRef().getDest() == "SW-RECORD-LAYOUT"
        assert mapping.getSwRecordLayoutRef().getValue() == "/Package/SwRecordLayouts/Layout1"

    def test_readInterpolationRoutineMapping_empty(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration import InterpolationRoutineMapping

        mapping = InterpolationRoutineMapping()
        element = _snip("", root_tag="INTERPOLATION-ROUTINE-MAPPING")
        parser.readInterpolationRoutineMapping(element, mapping)
        assert mapping.getInterpolationRoutines() == []
        assert mapping.getSwRecordLayoutRef() is None

    def test_readInterpolationRoutineMappingSet_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration import InterpolationRoutineMappingSet

        mapping_set = InterpolationRoutineMappingSet(parent=_autosar_root(), short_name="IRS1")
        element = _snip(
            "<INTERPOLATION-ROUTINE-MAPPINGS>"
            "<INTERPOLATION-ROUTINE-MAPPING>"
            "<INTERPOLATION-ROUTINES>"
            "<INTERPOLATION-ROUTINE><SHORT-LABEL>LinearInterpolation</SHORT-LABEL></INTERPOLATION-ROUTINE>"
            "</INTERPOLATION-ROUTINES>"
            '<SW-RECORD-LAYOUT-REF DEST="SW-RECORD-LAYOUT">/Package/SwRecordLayouts/Layout1</SW-RECORD-LAYOUT-REF>'
            "</INTERPOLATION-ROUTINE-MAPPING>"
            "<INTERPOLATION-ROUTINE-MAPPING>"
            '<SW-RECORD-LAYOUT-REF DEST="SW-RECORD-LAYOUT">/Package/SwRecordLayouts/Layout2</SW-RECORD-LAYOUT-REF>'
            "</INTERPOLATION-ROUTINE-MAPPING>"
            "</INTERPOLATION-ROUTINE-MAPPINGS>",
            root_tag="INTERPOLATION-ROUTINE-MAPPING-SET",
        )
        parser.readInterpolationRoutineMappingSet(element, mapping_set)
        mappings = mapping_set.getInterpolationRoutineMappings()
        assert len(mappings) == 2
        assert mappings[0].getInterpolationRoutines()[0].getShortLabel().getValue() == "LinearInterpolation"
        assert mappings[0].getSwRecordLayoutRef().getDest() == "SW-RECORD-LAYOUT"
        assert mappings[0].getSwRecordLayoutRef().getValue() == "/Package/SwRecordLayouts/Layout1"
        assert mappings[1].getInterpolationRoutines() == []
        assert mappings[1].getSwRecordLayoutRef().getValue() == "/Package/SwRecordLayouts/Layout2"

    def test_readInterpolationRoutineMappingSet_empty(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration import InterpolationRoutineMappingSet

        mapping_set = InterpolationRoutineMappingSet(parent=_autosar_root(), short_name="IRS1")
        element = _snip("", root_tag="INTERPOLATION-ROUTINE-MAPPING-SET")
        parser.readInterpolationRoutineMappingSet(element, mapping_set)
        assert mapping_set.getInterpolationRoutineMappings() == []

    def test_readSwComponentPrototypeAssignment_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SwComponentPrototypeAssignment

        assignment = SwComponentPrototypeAssignment()
        element = _snip(
            "<SW-COMPONENT-IREF>"
            "<CONTEXT-COMPOSITION-REF DEST='COMPOSITION-SW-COMPONENT-PROTOTYPE'>/comp</CONTEXT-COMPOSITION-REF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/swc</TARGET-COMPONENT-REF>"
            "</SW-COMPONENT-IREF>"
            "<VARIATION-POINT><SHORT-LABEL>VP_SWCA</SHORT-LABEL></VARIATION-POINT>",
            root_tag="SW-COMPONENT-PROTOTYPE-ASSIGNMENT",
        )
        parser.readSwComponentPrototypeAssignment(element, assignment)
        iref = assignment.getSwComponentIRef()
        assert iref is not None
        assert iref.getContextCompositionRef().getValue() == "/comp"
        assert iref.getContextCompositionRef().getDest() == "COMPOSITION-SW-COMPONENT-PROTOTYPE"
        assert iref.getTargetComponentRef().getValue() == "/swc"
        assert iref.getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert assignment.getVariationPoint().getShortLabel().getValue() == "VP_SWCA"

    def test_readSwComponentPrototypeAssignment_empty(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SwComponentPrototypeAssignment

        assignment = SwComponentPrototypeAssignment()
        element = _snip("", root_tag="SW-COMPONENT-PROTOTYPE-ASSIGNMENT")
        parser.readSwComponentPrototypeAssignment(element, assignment)
        assert assignment.getSwComponentIRef() is None
        assert assignment.getVariationPoint() is None

    def test_readCpSoftwareCluster_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import CpSoftwareCluster

        cluster = CpSoftwareCluster(parent=_autosar_root(), short_name="Cluster1")
        element = _snip(
            "<SOFTWARE-CLUSTER-ID>42</SOFTWARE-CLUSTER-ID>"
            "<SW-COMPONENT-ASSIGNMENTS>"
            "<SW-COMPONENT-PROTOTYPE-ASSIGNMENT>"
            "<SW-COMPONENT-IREF>"
            "<CONTEXT-COMPOSITION-REF DEST='COMPOSITION-SW-COMPONENT-PROTOTYPE'>/comp</CONTEXT-COMPOSITION-REF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/swc</TARGET-COMPONENT-REF>"
            "</SW-COMPONENT-IREF>"
            "</SW-COMPONENT-PROTOTYPE-ASSIGNMENT>"
            "<SW-COMPONENT-PROTOTYPE-ASSIGNMENT/>"
            "</SW-COMPONENT-ASSIGNMENTS>"
            "<SW-COMPOSITIONS>"
            "<COMPOSITION-SW-COMPONENT-TYPE-REF-CONDITIONAL>"
            '<COMPOSITION-SW-COMPONENT-TYPE-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/Composition/Comp1</COMPOSITION-SW-COMPONENT-TYPE-REF>'
            "</COMPOSITION-SW-COMPONENT-TYPE-REF-CONDITIONAL>"
            "</SW-COMPOSITIONS>",
            root_tag="CP-SOFTWARE-CLUSTER",
        )
        parser.readCpSoftwareCluster(element, cluster)
        assert cluster.getSoftwareClusterId().getValue() == 42
        assignments = cluster.getSwComponentAssignments()
        assert len(assignments) == 2
        assert assignments[0].getSwComponentIRef().getContextCompositionRef().getValue() == "/comp"
        assert assignments[0].getSwComponentIRef().getTargetComponentRef().getValue() == "/swc"
        assert assignments[1].getSwComponentIRef() is None
        refs = cluster.getSwCompositionRefs()
        assert len(refs) == 1
        assert refs[0].getDest() == "COMPOSITION-SW-COMPONENT-TYPE"
        assert refs[0].getValue() == "/Composition/Comp1"

    def test_readCpSoftwareCluster_empty(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import CpSoftwareCluster

        cluster = CpSoftwareCluster(parent=_autosar_root(), short_name="Cluster1")
        element = _snip("", root_tag="CP-SOFTWARE-CLUSTER")
        parser.readCpSoftwareCluster(element, cluster)
        assert cluster.getSoftwareClusterId() is None
        assert cluster.getSwComponentAssignments() == []
        assert cluster.getSwCompositionRefs() == []

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
        assert definition.getBaseTypeEncoding().getValue() == "IEEE754"
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
        element = _snip("<SHORT-NAME>idt</SHORT-NAME>", root_tag="IMPLEMENTATION-DATA-TYPE")
        parser.readImplementationDataType(element, idt)
        assert idt.getDynamicArraySizeProfile() is None
        assert idt.getTypeEmitter() is None

    def test_readImplementationDataType_with_typeEmitter_and_profile(self, parser):
        from armodel.models import ImplementationDataType

        idt = ImplementationDataType(parent=_autosar_root(), short_name="idt")
        element = _snip(
            "<SHORT-NAME>idt</SHORT-NAME>" "<DYNAMIC-ARRAY-SIZE-PROFILE>VAR</DYNAMIC-ARRAY-SIZE-PROFILE>" "<TYPE-EMITTER>HAL</TYPE-EMITTER>",
            root_tag="IMPLEMENTATION-DATA-TYPE",
        )
        parser.readImplementationDataType(element, idt)
        assert idt.getDynamicArraySizeProfile().getValue() == "VAR"
        assert idt.getTypeEmitter().getValue() == "HAL"

    def test_readImplementationDataType_with_symbol_props(self, parser):
        from armodel.models import ImplementationDataType

        idt = ImplementationDataType(parent=_autosar_root(), short_name="idt")
        element = _snip(
            "<SHORT-NAME>idt</SHORT-NAME>" "<SYMBOL-PROPS>" "<SHORT-NAME>sp</SHORT-NAME>" "</SYMBOL-PROPS>",
            root_tag="IMPLEMENTATION-DATA-TYPE",
        )
        parser.readImplementationDataType(element, idt)
        # Symbol props are stored on the data type; verify at least no exception.
        assert idt.getShortName() == "idt"

    def test_readImplementationDataTypeSubElements_unsupported_tag_warns(self, warning_parser, caplog):
        from armodel.models import ImplementationDataType

        idt = ImplementationDataType(parent=_autosar_root(), short_name="idt")
        element = _snip(
            "<SUB-ELEMENTS><BAD-ELEMENT/></SUB-ELEMENTS>",
            root_tag="IMPLEMENTATION-DATA-TYPE",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readImplementationDataTypeSubElements(element, idt)
        assert any("Unsupported ImplementationDataType SubElement" in r.getMessage() for r in caplog.records)

    def test_getSwValues_with_V_and_VT(self, parser):
        element = _snip(
            "<SW-VALUES-PHYS>" "<V>1.0</V>" "<V>2.0</V>" "<VT>label</VT>" "</SW-VALUES-PHYS>",
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
        element = _snip("<SW-ARRAYSIZE><V>4</V></SW-ARRAYSIZE>", root_tag="PARENT")
        value_list = parser.getValueList(element, "SW-ARRAYSIZE")
        assert value_list is not None
        # ValueList stores a single V (Float).
        assert value_list.getV() is not None
        assert float(value_list.getV().getValue()) == 4.0

    def test_getValueList_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getValueList(element, "SW-ARRAYSIZE") is None

    def test_getValueList_with_vf_list(self, parser):
        element = _snip(
            "<SW-ARRAYSIZE>" "<VF><V>1.5</V></VF>" "<VF><V>2.5</V></VF>" "<V>4</V>" "</SW-ARRAYSIZE>",
            root_tag="PARENT",
        )
        value_list = parser.getValueList(element, "SW-ARRAYSIZE")
        assert value_list is not None
        assert float(value_list.getV().getValue()) == 4.0
        vfs = value_list.getVfs()
        assert len(vfs) == 2
        assert float(vfs[0].getValue()) == 1.5
        assert float(vfs[1].getValue()) == 2.5

    def test_getSwValueCont_full(self, parser):
        element = _snip(
            "<SW-VALUE-CONT>"
            "<UNIT-REF DEST='UNIT'>/u</UNIT-REF>"
            "<SW-ARRAYSIZE><V>2</V></SW-ARRAYSIZE>"
            "<SW-VALUES-PHYS><V>1.0</V></SW-VALUES-PHYS>"
            "<UNIT-DISPLAY-NAME>display</UNIT-DISPLAY-NAME>"
            "</SW-VALUE-CONT>",
            root_tag="PARENT",
        )
        cont = parser.getSwValueCont(element)
        assert cont is not None
        assert cont.getUnitRef().getValue() == "/u"
        assert cont.getSwArraysize() is not None
        assert cont.getSwArraysize().getV().getValue() == "2"
        assert cont.getSwValuesPhys() is not None
        assert len(cont.getSwValuesPhys().getVs()) == 1
        assert cont.getSwValuesPhys().getVs()[0].getValue() == "1.0"
        assert cont.getUnitDisplayName().getValue().getValue() == "display"

    def test_getSwValueCont_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getSwValueCont(element) is None

    def test_getValueGroup_with_label_and_contents(self, parser):
        element = _snip(
            "<VG>" "<LABEL><L-4 L='FOR-ALL'>group label</L-4></LABEL>" "<V>1.5</V>" "<V>2.5</V>" "</VG>",
            root_tag="PARENT",
        )
        vg = parser.getValueGroup(element, "VG")
        assert vg is not None
        assert vg.getLabel() is not None
        l4s = vg.getLabel().getL4s()
        assert len(l4s) == 1
        assert l4s[0].getValue() == "group label"
        contents = vg.getVgContents()
        assert contents is not None
        assert len(contents.getVs()) == 2

    def test_getValueGroup_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getValueGroup(element, "VG") is None

    def test_getSwValues_with_nested_VG(self, parser):
        element = _snip(
            "<SW-VALUES-PHYS>" "<V>0.0</V>" "<VG><V>1.5</V></VG>" "</SW-VALUES-PHYS>",
            root_tag="PARENT",
        )
        sw_values = parser.getSwValues(element, "SW-VALUES-PHYS")
        assert sw_values is not None
        assert len(sw_values.getVs()) == 1
        assert sw_values.getVg() is not None
        assert len(sw_values.getVg().getVgContents().getVs()) == 1

    def test_getSwValues_with_vf_and_verbatim_vt(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString

        element = _snip(
            "<SW-VALUES-PHYS>" "<VF>0.5</VF>" "<VF>1.5</VF>" "<VT>a|b</VT>" "</SW-VALUES-PHYS>",
            root_tag="PARENT",
        )
        sw_values = parser.getSwValues(element, "SW-VALUES-PHYS")
        assert sw_values is not None
        assert len(sw_values.getVfs()) == 2
        assert float(sw_values.getVfs()[0].getValue()) == 0.5
        assert float(sw_values.getVfs()[1].getValue()) == 1.5
        assert isinstance(sw_values.getVt(), VerbatimString)
        assert sw_values.getVt().getValue() == "a|b"

    def test_getSwValues_with_vtf(self, parser):
        element = _snip(
            "<SW-VALUES-PHYS>" "<VTF><VF>7</VF></VTF>" "<VTF><VT>text</VT></VTF>" "</SW-VALUES-PHYS>",
            root_tag="PARENT",
        )
        sw_values = parser.getSwValues(element, "SW-VALUES-PHYS")
        assert sw_values is not None
        vtfs = sw_values.getVtfs()
        assert len(vtfs) == 2
        assert float(vtfs[0].getVf().getValue()) == 7
        assert vtfs[1].getVt().getValue() == "text"

    def test_getNotAvailableValueSpecification_with_default_pattern(self, parser):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NotAvailableValueSpecification

        root = _snip(
            "<NOT-AVAILABLE-VALUE-SPECIFICATION>" "<DEFAULT-PATTERN>4</DEFAULT-PATTERN>" "</NOT-AVAILABLE-VALUE-SPECIFICATION>",
            root_tag="PARENT",
        )
        spec = parser.getValueSpecification(root[0], "NOT-AVAILABLE-VALUE-SPECIFICATION")
        assert isinstance(spec, NotAvailableValueSpecification)
        assert spec.getDefaultPattern().getValue() == 4

    def test_getNotAvailableValueSpecification_without_default_pattern(self, parser):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NotAvailableValueSpecification

        root = _snip("<NOT-AVAILABLE-VALUE-SPECIFICATION/>", root_tag="PARENT")
        spec = parser.getValueSpecification(root[0], "NOT-AVAILABLE-VALUE-SPECIFICATION")
        assert isinstance(spec, NotAvailableValueSpecification)
        assert spec.getDefaultPattern() is None

    def test_getConstantSpecificationMapping_with_refs(self, parser):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ConstantSpecificationMapping

        root = _snip(
            "<CONSTANT-SPECIFICATION-MAPPING>"
            "<APPL-CONSTANT-REF DEST='CONSTANT-SPECIFICATION'>/Appl/Const</APPL-CONSTANT-REF>"
            "<IMPL-CONSTANT-REF DEST='CONSTANT-SPECIFICATION'>/Impl/Const</IMPL-CONSTANT-REF>"
            "</CONSTANT-SPECIFICATION-MAPPING>",
            root_tag="PARENT",
        )
        mapping = parser.getConstantSpecificationMapping(root[0])
        assert isinstance(mapping, ConstantSpecificationMapping)
        assert mapping.getApplConstantRef().getValue() == "/Appl/Const"
        assert mapping.getImplConstantRef().getValue() == "/Impl/Const"

    def test_getConstantSpecificationMapping_without_refs(self, parser):
        root = _snip("<CONSTANT-SPECIFICATION-MAPPING/>", root_tag="PARENT")
        mapping = parser.getConstantSpecificationMapping(root[0])
        assert mapping is not None
        assert mapping.getApplConstantRef() is None
        assert mapping.getImplConstantRef() is None

    def test_readApplicationValueSpecification_populates_fields(self, parser):
        from armodel.models import ApplicationValueSpecification

        value_spec = ApplicationValueSpecification()
        value_spec.short_name = "vs"  # required by readValueSpecification path
        element = _snip(
            "<SHORT-NAME>vs</SHORT-NAME>" "<CATEGORY>CAT</CATEGORY>" "<SW-VALUE-CONT>" "<UNIT-REF DEST='UNIT'>/u</UNIT-REF>" "</SW-VALUE-CONT>",
            root_tag="APPLICATION-VALUE-SPECIFICATION",
        )
        parser.readApplicationValueSpecification(element, value_spec)
        assert value_spec.getCategory().getValue() == "CAT"
        assert value_spec.getSwValueCont() is not None
        assert value_spec.getSwValueCont().getUnitRef().getValue() == "/u"

    def test_getChildValueSpecification_present(self, parser):
        from armodel.models import NumericalValueSpecification

        element = _snip(
            "<INIT-VALUE>" "<NUMERICAL-VALUE-SPECIFICATION>" "<SHORT-NAME>n</SHORT-NAME>" "<VALUE>42</VALUE>" "</NUMERICAL-VALUE-SPECIFICATION>" "</INIT-VALUE>",
            root_tag="PARENT",
        )
        value_spec = parser.getChildValueSpecification(element, "INIT-VALUE")
        assert value_spec is not None
        assert isinstance(value_spec, NumericalValueSpecification)

    def test_getChildValueSpecification_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getChildValueSpecification(element, "INIT-VALUE") is None


# ==================== RuleBasedValueSpecification family ====================


class TestRuleBasedValueSpecHandlers:
    """Exercise getApplicationRuleBasedValueSpecification and its inner
    readers (getRuleBasedAxisCont, getRuleBasedValueCont,
    getRuleBasedValueSpecification, getRuleArguments, getNumericalOrText)."""

    def test_getNumericalOrText(self, parser):
        element = _snip("<VF>1.5</VF><VT>label</VT>", root_tag="VTF")
        not_text = parser.getNumericalOrText(element)
        assert not_text is not None
        assert not_text.getVf().getValue() == 1.5
        assert not_text.getVt().getValue() == "label"

    def test_getNumericalOrText_missing_returns_None_fields(self, parser):
        element = _snip("<VTF/>", root_tag="VTF")
        not_text = parser.getNumericalOrText(element)
        assert not_text is not None
        assert not_text.getVf() is None
        assert not_text.getVt() is None

    def test_getRuleArguments_full(self, parser):
        element = _snip(
            "<V>1</V><VF>2</VF><VT>label</VT><VTF><VF>1.5</VF><VT>alt</VT></VTF>",
            root_tag="RULE-ARGUMENTS",
        )
        arguments = parser.getRuleArguments(element)
        assert arguments is not None
        assert arguments.getV().getValue() == 1
        assert arguments.getVf().getValue() == 2
        assert arguments.getVt().getValue() == "label"
        assert arguments.getVtf() is not None
        assert arguments.getVtf().getVf().getValue() == 1.5

    def test_getRuleBasedValueSpecification_full(self, parser):
        element = _snip(
            "<RULE>FILL_UNTIL_END</RULE>" "<ARGUMENTSS><RULE-ARGUMENTS><V>1</V></RULE-ARGUMENTS></ARGUMENTSS>" "<MAX-SIZE-TO-FILL>8</MAX-SIZE-TO-FILL>",
            root_tag="RULE-BASED-VALUES",
        )
        value_spec = parser.getRuleBasedValueSpecification(element)
        assert value_spec is not None
        assert value_spec.getRule().getValue() == "FILL_UNTIL_END"
        assert len(value_spec.getArguments()) == 1
        assert value_spec.getMaxSizeToFill() is not None
        assert float(value_spec.getMaxSizeToFill().getValue()) == 8.0

    def test_getRuleBasedValueSpecification_missing_returns_None(self, parser):
        _element = _snip("<X/>")
        assert parser.getRuleBasedValueSpecification(None) is None

    def test_getRuleBasedValueSpecification_empty_arguments(self, parser):
        element = _snip("<RULE>FILL_UNTIL_END</RULE>", root_tag="RULE-BASED-VALUES")
        value_spec = parser.getRuleBasedValueSpecification(element)
        assert value_spec is not None
        assert value_spec.getArguments() == []
        assert value_spec.getRule().getValue() == "FILL_UNTIL_END"

    def test_getRuleBasedAxisCont_full(self, parser):
        element = _snip(
            "<CATEGORY>STD_AXIS</CATEGORY>"
            "<UNIT-REF DEST='UNIT'>/p/u</UNIT-REF>"
            "<SW-ARRAYSIZE><V>3</V></SW-ARRAYSIZE>"
            "<SW-AXIS-INDEX>1</SW-AXIS-INDEX>"
            "<RULE-BASED-VALUES><RULE>FILL_UNTIL_END</RULE></RULE-BASED-VALUES>",
            root_tag="RULE-BASED-AXIS-CONT",
        )
        cont = parser.getRuleBasedAxisCont(element)
        assert cont is not None
        assert cont.getCategory().getValue() == "STD_AXIS"
        assert cont.getUnitRef().getValue() == "/p/u"
        assert cont.getSwArraysize() is not None
        assert cont.getSwAxisIndex().getValue() == "1"
        assert cont.getRuleBasedValues() is not None

    def test_getRuleBasedValueCont_full(self, parser):
        element = _snip(
            "<SW-VALUE-CONT>" "<UNIT-REF DEST='UNIT'>/p/u</UNIT-REF>" "<SW-ARRAYSIZE><V>10</V></SW-ARRAYSIZE>" "<RULE-BASED-VALUES><RULE>FILL_UNTIL_END</RULE></RULE-BASED-VALUES>" "</SW-VALUE-CONT>",
            root_tag="PARENT",
        )
        cont = parser.getRuleBasedValueCont(element)
        assert cont is not None
        assert cont.getUnitRef().getValue() == "/p/u"
        assert cont.getSwArraysize() is not None
        assert cont.getRuleBasedValues() is not None

    def test_getRuleBasedValueCont_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getRuleBasedValueCont(element) is None

    def test_getApplicationRuleBasedValueSpecification_full(self, parser):
        from armodel.models import ApplicationRuleBasedValueSpecification

        element = _snip(
            "<CATEGORY>ARRAY</CATEGORY>"
            "<SW-AXIS-CONTS>"
            "<RULE-BASED-AXIS-CONT>"
            "<CATEGORY>STD_AXIS</CATEGORY>"
            "<RULE-BASED-VALUES><RULE>FILL_UNTIL_END</RULE></RULE-BASED-VALUES>"
            "</RULE-BASED-AXIS-CONT>"
            "</SW-AXIS-CONTS>"
            "<SW-VALUE-CONT>"
            "<RULE-BASED-VALUES><RULE>FILL_UNTIL_END</RULE></RULE-BASED-VALUES>"
            "</SW-VALUE-CONT>",
            root_tag="APPLICATION-RULE-BASED-VALUE-SPECIFICATION",
        )
        value_spec = parser.getApplicationRuleBasedValueSpecification(element)
        assert isinstance(value_spec, ApplicationRuleBasedValueSpecification)
        assert value_spec.getCategory().getValue() == "ARRAY"
        assert len(value_spec.getSwAxisConts()) == 1
        assert value_spec.getSwAxisConts()[0].getCategory().getValue() == "STD_AXIS"
        assert value_spec.getSwValueCont() is not None

    def test_getValueSpecification_dispatch_application_rule_based(self, parser):
        element = _snip(
            "<CATEGORY>ARRAY</CATEGORY>",
            root_tag="APPLICATION-RULE-BASED-VALUE-SPECIFICATION",
        )
        value_spec = parser.getValueSpecification(element, "APPLICATION-RULE-BASED-VALUE-SPECIFICATION")
        from armodel.models import ApplicationRuleBasedValueSpecification

        assert isinstance(value_spec, ApplicationRuleBasedValueSpecification)

    def test_getCompositeRuleBasedValueSpecification_full(self, parser):
        from armodel.models import ApplicationRuleBasedValueSpecification, ArrayValueSpecification

        element = _snip(
            "<RULE>FILL_UNTIL_END</RULE>"
            "<ARGUMENTS>"
            "<ARRAY-VALUE-SPECIFICATION>"
            "<ELEMENTS>"
            "<NUMERICAL-VALUE-SPECIFICATION><VALUE>1</VALUE></NUMERICAL-VALUE-SPECIFICATION>"
            "</ELEMENTS>"
            "</ARRAY-VALUE-SPECIFICATION>"
            "</ARGUMENTS>"
            "<COMPOUND-PRIMITIVE-ARGUMENTS>"
            "<APPLICATION-RULE-BASED-VALUE-SPECIFICATION><CATEGORY>ARRAY</CATEGORY></APPLICATION-RULE-BASED-VALUE-SPECIFICATION>"
            "</COMPOUND-PRIMITIVE-ARGUMENTS>"
            "<MAX-SIZE-TO-FILL>16</MAX-SIZE-TO-FILL>",
            root_tag="COMPOSITE-RULE-BASED-VALUE-SPECIFICATION",
        )
        value_spec = parser.getCompositeRuleBasedValueSpecification(element)
        assert value_spec.getRule().getValue() == "FILL_UNTIL_END"
        assert len(value_spec.getArguments()) == 1
        assert isinstance(value_spec.getArguments()[0], ArrayValueSpecification)
        assert len(value_spec.getArguments()[0].getElements()) == 1
        assert len(value_spec.getCompoundPrimitiveArguments()) == 1
        assert isinstance(value_spec.getCompoundPrimitiveArguments()[0], ApplicationRuleBasedValueSpecification)
        assert value_spec.getMaxSizeToFill().__class__.__name__ == "PositiveInteger"
        assert value_spec.getMaxSizeToFill().getValue() == 16

    def test_getCompositeRuleBasedValueSpecification_empty_lists(self, parser):
        element = _snip("<RULE>FILL_UNTIL_END</RULE>", root_tag="COMPOSITE-RULE-BASED-VALUE-SPECIFICATION")
        value_spec = parser.getCompositeRuleBasedValueSpecification(element)
        assert value_spec.getRule().getValue() == "FILL_UNTIL_END"
        assert value_spec.getArguments() == []
        assert value_spec.getCompoundPrimitiveArguments() == []
        assert value_spec.getMaxSizeToFill() is None

    def test_getValueSpecification_dispatch_composite_rule_based(self, parser):
        from armodel.models import CompositeRuleBasedValueSpecification

        element = _snip(
            "<RULE>FILL_UNTIL_END</RULE>",
            root_tag="COMPOSITE-RULE-BASED-VALUE-SPECIFICATION",
        )
        value_spec = parser.getValueSpecification(element, "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION")
        assert isinstance(value_spec, CompositeRuleBasedValueSpecification)

    def test_readConstantSpecification_nested_composite_rule_based(self, parser):
        from armodel.models import (
            ApplicationRuleBasedValueSpecification,
            CompositeRuleBasedValueSpecification,
            ConstantSpecification,
            NumericalValueSpecification,
            RecordValueSpecification,
        )

        element = _snip(
            "<SHORT-NAME>c</SHORT-NAME>"
            "<VALUE-SPEC>"
            "<COMPOSITE-RULE-BASED-VALUE-SPECIFICATION>"
            "<RULE>FILL_UNTIL_END</RULE>"
            "<ARGUMENTS>"
            "<RECORD-VALUE-SPECIFICATION>"
            "<FIELDS><NUMERICAL-VALUE-SPECIFICATION><VALUE>1</VALUE></NUMERICAL-VALUE-SPECIFICATION></FIELDS>"
            "</RECORD-VALUE-SPECIFICATION>"
            "</ARGUMENTS>"
            "<COMPOUND-PRIMITIVE-ARGUMENTS>"
            "<APPLICATION-RULE-BASED-VALUE-SPECIFICATION><CATEGORY>ARRAY</CATEGORY></APPLICATION-RULE-BASED-VALUE-SPECIFICATION>"
            "</COMPOUND-PRIMITIVE-ARGUMENTS>"
            "<MAX-SIZE-TO-FILL>16</MAX-SIZE-TO-FILL>"
            "</COMPOSITE-RULE-BASED-VALUE-SPECIFICATION>"
            "</VALUE-SPEC>",
            root_tag="CONSTANT-SPECIFICATION",
        )
        spec = ConstantSpecification(_autosar_root(), "c")
        parser.readConstantSpecification(element, spec)

        value_spec = spec.getValueSpec()
        assert isinstance(value_spec, CompositeRuleBasedValueSpecification)
        assert value_spec.getRule().getValue() == "FILL_UNTIL_END"
        assert value_spec.getMaxSizeToFill() is not None
        assert float(value_spec.getMaxSizeToFill().getValue()) == 16.0
        assert len(value_spec.getArguments()) == 1
        assert isinstance(value_spec.getArguments()[0], RecordValueSpecification)
        fields = value_spec.getArguments()[0].getFields()
        assert len(fields) == 1
        assert isinstance(fields[0], NumericalValueSpecification)
        assert float(fields[0].getValue().getValue()) == 1.0
        assert len(value_spec.getCompoundPrimitiveArguments()) == 1
        assert isinstance(value_spec.getCompoundPrimitiveArguments()[0], ApplicationRuleBasedValueSpecification)


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
            "<PORTS>" "<P-PORT-PROTOTYPE><SHORT-NAME>pp1</SHORT-NAME></P-PORT-PROTOTYPE>" "</PORTS>",
            root_tag="COMP",
        )
        parser.readSwComponentTypePorts(element, composition)
        assert len(composition.getPPortPrototypes()) == 1

    def test_readSwComponentTypePorts_creates_RPort(self, parser, composition):
        element = _snip(
            "<PORTS>" "<R-PORT-PROTOTYPE><SHORT-NAME>rp1</SHORT-NAME></R-PORT-PROTOTYPE>" "</PORTS>",
            root_tag="COMP",
        )
        parser.readSwComponentTypePorts(element, composition)
        assert len(composition.getRPortPrototypes()) == 1

    def test_readSwComponentTypePorts_creates_PRPort(self, parser, composition):
        element = _snip(
            "<PORTS>" "<PR-PORT-PROTOTYPE><SHORT-NAME>prp1</SHORT-NAME></PR-PORT-PROTOTYPE>" "</PORTS>",
            root_tag="COMP",
        )
        parser.readSwComponentTypePorts(element, composition)
        assert len(composition.getPRPortPrototypes()) == 1

    def test_readSwComponentTypePorts_unsupported_tag_warns(self, warning_parser, composition, caplog):
        element = _snip("<PORTS><BAD-PORT/></PORTS>", root_tag="COMP")
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwComponentTypePorts(element, composition)
        assert any("Unsupported Port Prototype" in r.getMessage() for r in caplog.records)

    def test_readSwComponentTypeSwcMappingConstraints(self, parser, composition):
        element = _snip(
            "<SWC-MAPPING-CONSTRAINT-REFS>"
            "<SWC-MAPPING-CONSTRAINT-REF DEST='SWC-MAPPING-CONSTRAINTS'>/Mapping/Const1</SWC-MAPPING-CONSTRAINT-REF>"
            "<SWC-MAPPING-CONSTRAINT-REF DEST='SWC-MAPPING-CONSTRAINTS'>/Mapping/Const2</SWC-MAPPING-CONSTRAINT-REF>"
            "</SWC-MAPPING-CONSTRAINT-REFS>",
            root_tag="COMP",
        )
        parser.readSwComponentTypeSwcMappingConstraints(element, composition)
        refs = composition.getSwcMappingConstraintsRefs()
        assert [ref.getValue() for ref in refs] == ["/Mapping/Const1", "/Mapping/Const2"]
        assert refs[0].getDest() == "SWC-MAPPING-CONSTRAINTS"

    def test_readSwComponentTypeUnitGroups(self, parser, composition):
        element = _snip(
            "<UNIT-GROUP-REFS>" "<UNIT-GROUP-REF DEST='UNIT-GROUP'>/Units/Group1</UNIT-GROUP-REF>" "</UNIT-GROUP-REFS>",
            root_tag="COMP",
        )
        parser.readSwComponentTypeUnitGroups(element, composition)
        refs = composition.getUnitGroupRefs()
        assert [ref.getValue() for ref in refs] == ["/Units/Group1"]
        assert refs[0].getDest() == "UNIT-GROUP"

    def test_readSwComponentPrototype_sets_typeTRef(self, parser, composition):
        prototype = composition.createSwComponentPrototype("cp1")
        element = _snip(
            "<SHORT-NAME>cp1</SHORT-NAME>" "<TYPE-TREF DEST='COMPOSITION-SW-COMPONENT-TYPE'>/t</TYPE-TREF>",
            root_tag="SW-COMPONENT-PROTOTYPE",
        )
        parser.readSwComponentPrototype(element, prototype)
        assert prototype.getTypeTRef().getValue() == "/t"

    def test_readAssemblySwConnector_with_provider_and_requester(self, parser, composition):
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
        assert connector.getProviderIRef().getContextComponentRef().getValue() == "/c1"
        assert connector.getProviderIRef().getContextComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert connector.getProviderIRef().getTargetPPortRef().getDest() == "P-PORT-PROTOTYPE"
        assert connector.getRequesterIRef().getContextComponentRef().getValue() == "/c2"
        assert connector.getRequesterIRef().getContextComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert connector.getRequesterIRef().getTargetRPortRef().getDest() == "R-PORT-PROTOTYPE"

    def test_readAssemblySwConnector_without_IRefs(self, parser, composition):
        connector = composition.createAssemblySwConnector("a2")
        element = _snip("<SHORT-NAME>a2</SHORT-NAME>", root_tag="ASSEMBLY-SW-CONNECTOR")
        parser.readAssemblySwConnector(element, connector)
        assert connector.getProviderIRef() is None
        assert connector.getRequesterIRef() is None

    def test_readAssemblySwConnector_preserves_mapping_and_iref_values(self, parser, composition):
        connector = composition.createAssemblySwConnector("a4")
        element = _snip(
            "<SHORT-NAME>a4</SHORT-NAME>"
            "<MAPPING-REF DEST='PORT-INTERFACE-MAPPING'>/mapping</MAPPING-REF>"
            "<PROVIDER-IREF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/provider/component</CONTEXT-COMPONENT-REF>"
            "<TARGET-P-PORT-REF DEST='P-PORT-PROTOTYPE'>/provider/port</TARGET-P-PORT-REF>"
            "</PROVIDER-IREF>"
            "<REQUESTER-IREF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/requester/component</CONTEXT-COMPONENT-REF>"
            "<TARGET-R-PORT-REF DEST='R-PORT-PROTOTYPE'>/requester/port</TARGET-R-PORT-REF>"
            "</REQUESTER-IREF>",
            root_tag="ASSEMBLY-SW-CONNECTOR",
        )

        parser.readAssemblySwConnector(element, connector)

        assert connector.getMappingRef().getValue() == "/mapping"
        assert connector.getMappingRef().getDest() == "PORT-INTERFACE-MAPPING"
        assert connector.getProviderIRef().getContextComponentRef().getValue() == "/provider/component"
        assert connector.getProviderIRef().getTargetPPortRef().getValue() == "/provider/port"
        assert connector.getRequesterIRef().getContextComponentRef().getValue() == "/requester/component"
        assert connector.getRequesterIRef().getTargetRPortRef().getValue() == "/requester/port"

    def test_readSwConnector_sets_mappingRef(self, parser, composition):
        connector = composition.createAssemblySwConnector("a3")
        element = _snip(
            "<SHORT-NAME>a3</SHORT-NAME>" "<MAPPING-REF DEST='X'>/m</MAPPING-REF>",
            root_tag="ASSEMBLY-SW-CONNECTOR",
        )
        parser.readAssemblySwConnector(element, connector)
        assert connector.getMappingRef().getValue() == "/m"

    def test_readDelegationSwConnector_inner_RPort_IRef(self, parser, composition):
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
        assert connector.getInnerPortIRef() is not None
        assert connector.getOuterPortRef().getValue() == "/op"
        assert connector.getInnerPortIRef().getContextComponentRef().getValue() == "/c"
        assert connector.getInnerPortIRef().getContextComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert connector.getInnerPortIRef().getTargetRPortRef().getValue() == "/rp"
        assert connector.getInnerPortIRef().getTargetRPortRef().getDest() == "R-PORT-PROTOTYPE"

    def test_readDelegationSwConnector_inner_PPort_IRef(self, parser, composition):
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
        assert connector.getInnerPortIRef() is not None
        assert connector.getOuterPortRef().getValue() == "/op"
        assert connector.getInnerPortIRef().getContextComponentRef().getValue() == "/c"
        assert connector.getInnerPortIRef().getContextComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert connector.getInnerPortIRef().getTargetPPortRef().getValue() == "/pp"
        assert connector.getInnerPortIRef().getTargetPPortRef().getDest() == "P-PORT-PROTOTYPE"

    def test_readDelegationSwConnector_only_inner_ref(self, parser, composition):
        # Note: readDelegationSwConnector checks getInnerPortIRef() AND
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
        assert connector.getInnerPortIRef() is not None
        # OUTER-PORT-REF was absent; should remain None.
        assert connector.getOuterPortRef() is None

    def test_readDelegationSwConnector_both_missing_warns(self, warning_parser, composition, caplog):
        connector = composition.createDelegationSwConnector("d4")
        element = _snip("<SHORT-NAME>d4</SHORT-NAME>", root_tag="DELEGATION-SW-CONNECTOR")
        with caplog.at_level(logging.ERROR):
            warning_parser.readDelegationSwConnector(element, connector)
        assert any("Invalid PortPrototype of DELEGATION-SW-CONNECTOR" in r.getMessage() for r in caplog.records)

    def test_readCompositionSwComponentTypeDataTypeMappingSet_adds_refs(self, parser, composition):
        element = _snip(
            "<DATA-TYPE-MAPPING-REFS>"
            "<DATA-TYPE-MAPPING-REF DEST='DATA-TYPE-MAPPING-SET'>/dtm1</DATA-TYPE-MAPPING-REF>"
            "<DATA-TYPE-MAPPING-REF DEST='DATA-TYPE-MAPPING-SET'>/dtm2</DATA-TYPE-MAPPING-REF>"
            "</DATA-TYPE-MAPPING-REFS>",
            root_tag="COMP",
        )
        parser.readCompositionSwComponentTypeDataTypeMappingSet(element, composition)
        assert len(composition.getDataTypeMappingRefs()) == 2

    def test_readCompositionSwComponentTypeDataTypeMappingSet_missing_no_op(self, parser, composition):
        element = _snip("<X/>")
        parser.readCompositionSwComponentTypeDataTypeMappingSet(element, composition)
        assert len(composition.getDataTypeMappingRefs()) == 0

    def test_readCompositionSwComponentTypeConstantValueMappingSet_adds_refs(self, parser, composition):
        element = _snip(
            "<CONSTANT-VALUE-MAPPING-REFS>"
            "<CONSTANT-VALUE-MAPPING-REF DEST='CONSTANT-SPECIFICATION-MAPPING-SET'>/cvm1</CONSTANT-VALUE-MAPPING-REF>"
            "<CONSTANT-VALUE-MAPPING-REF DEST='CONSTANT-SPECIFICATION-MAPPING-SET'>/cvm2</CONSTANT-VALUE-MAPPING-REF>"
            "</CONSTANT-VALUE-MAPPING-REFS>",
            root_tag="COMP",
        )
        parser.readCompositionSwComponentTypeConstantValueMappingSet(element, composition)
        assert len(composition.getConstantValueMappingRefs()) == 2
        assert composition.getConstantValueMappingRefs()[0].getValue() == "/cvm1"

    def test_readCompositionSwComponentTypeConstantValueMappingSet_missing_no_op(self, parser, composition):
        element = _snip("<X/>")
        parser.readCompositionSwComponentTypeConstantValueMappingSet(element, composition)
        assert len(composition.getConstantValueMappingRefs()) == 0

    def test_readPassThroughSwConnector(self, parser, composition):
        connector = composition.createPassThroughSwConnector("p1")
        element = _snip(
            "<SHORT-NAME>p1</SHORT-NAME>"
            "<PROVIDED-OUTER-PORT-REF DEST='P-PORT-PROTOTYPE'>/pop</PROVIDED-OUTER-PORT-REF>"
            "<REQUIRED-OUTER-PORT-REF DEST='R-PORT-PROTOTYPE'>/rop</REQUIRED-OUTER-PORT-REF>",
            root_tag="PASS-THROUGH-SW-CONNECTOR",
        )
        parser.readPassThroughSwConnector(element, connector)
        assert connector.getProvidedOuterPortRef().getValue() == "/pop"
        assert connector.getRequiredOuterPortRef().getValue() == "/rop"

    def test_readPassThroughSwConnector_without_outer_refs(self, parser, composition):
        connector = composition.createPassThroughSwConnector("p2")
        element = _snip("<SHORT-NAME>p2</SHORT-NAME>", root_tag="PASS-THROUGH-SW-CONNECTOR")
        parser.readPassThroughSwConnector(element, connector)
        assert connector.getProvidedOuterPortRef() is None
        assert connector.getRequiredOuterPortRef() is None

    def test_readInstanceEventInCompositionInstanceRef(self, parser):
        instance_ref = InstanceEventInCompositionInstanceRef()
        element = _snip(
            "<CONTEXT-COMPONENT-PROTOTYPE-REF DEST='SW-COMPONENT-PROTOTYPE'>/inner1</CONTEXT-COMPONENT-PROTOTYPE-REF>"
            "<CONTEXT-COMPONENT-PROTOTYPE-REF DEST='SW-COMPONENT-PROTOTYPE'>/inner2</CONTEXT-COMPONENT-PROTOTYPE-REF>"
            "<TARGET-EVENT-REF DEST='TIMING-EVENT'>/evt</TARGET-EVENT-REF>",
            root_tag="REFINED-EVENT-IREF",
        )
        parser.readInstanceEventInCompositionInstanceRef(element, instance_ref)
        assert len(instance_ref.getContextComponentPrototypeRefs()) == 2
        assert instance_ref.getContextComponentPrototypeRefs()[0].getValue() == "/inner1"
        assert instance_ref.getTargetEventRef().getValue() == "/evt"

    def test_readInstantiationTimingEventProps(self, parser):
        props = InstantiationTimingEventProps()
        element = _snip(
            "<REFINED-EVENT-IREF>"
            "<CONTEXT-COMPONENT-PROTOTYPE-REF DEST='SW-COMPONENT-PROTOTYPE'>/inner</CONTEXT-COMPONENT-PROTOTYPE-REF>"
            "<TARGET-EVENT-REF DEST='TIMING-EVENT'>/evt</TARGET-EVENT-REF>"
            "</REFINED-EVENT-IREF>"
            "<SHORT-LABEL>Label</SHORT-LABEL>"
            "<PERIOD>0.01</PERIOD>",
            root_tag="INSTANTIATION-TIMING-EVENT-PROPS",
        )
        parser.readInstantiationTimingEventProps(element, props)
        assert props.getRefinedEventIRef() is not None
        assert props.getRefinedEventIRef().getTargetEventRef().getValue() == "/evt"
        assert props.getShortLabel().getValue() == "Label"
        assert props.getPeriod().getValue() == 0.01

    def test_readCompositionSwComponentTypeInstantiationRTEEventProps(self, parser, composition):
        element = _snip(
            "<INSTANTIATION-RTE-EVENT-PROPSS>"
            "<INSTANTIATION-TIMING-EVENT-PROPS>"
            "<REFINED-EVENT-IREF>"
            "<CONTEXT-COMPONENT-PROTOTYPE-REF DEST='SW-COMPONENT-PROTOTYPE'>/inner</CONTEXT-COMPONENT-PROTOTYPE-REF>"
            "<TARGET-EVENT-REF DEST='TIMING-EVENT'>/evt</TARGET-EVENT-REF>"
            "</REFINED-EVENT-IREF>"
            "<SHORT-LABEL>Label</SHORT-LABEL>"
            "<PERIOD>0.01</PERIOD>"
            "</INSTANTIATION-TIMING-EVENT-PROPS>"
            "</INSTANTIATION-RTE-EVENT-PROPSS>",
            root_tag="COMP",
        )
        parser.readCompositionSwComponentTypeInstantiationRTEEventProps(element, composition)
        assert len(composition.getInstantiationRTEEventProps()) == 1
        props = composition.getInstantiationRTEEventProps()[0]
        assert isinstance(props, InstantiationTimingEventProps)
        assert props.getShortLabel().getValue() == "Label"
        assert props.getPeriod().getValue() == 0.01

    def test_readCompositionSwComponentTypeInstantiationRTEEventProps_missing_no_op(self, parser, composition):
        element = _snip("<X/>")
        parser.readCompositionSwComponentTypeInstantiationRTEEventProps(element, composition)
        assert len(composition.getInstantiationRTEEventProps()) == 0

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

    def test_readDataTypeMappingSet_preserves_both_mapping_lists(self, parser):
        from armodel.models import DataTypeMappingSet

        dtms = DataTypeMappingSet(parent=_autosar_root(), short_name="DTMS")
        element = _snip(
            "<SHORT-NAME>DTMS</SHORT-NAME>"
            "<DATA-TYPE-MAPS>"
            "<DATA-TYPE-MAP>"
            "<APPLICATION-DATA-TYPE-REF DEST='APPLICATION-DATA-TYPE'>/adt</APPLICATION-DATA-TYPE-REF>"
            "<IMPLEMENTATION-DATA-TYPE-REF DEST='IMPLEMENTATION-DATA-TYPE'>/idt</IMPLEMENTATION-DATA-TYPE-REF>"
            "</DATA-TYPE-MAP>"
            "</DATA-TYPE-MAPS>"
            "<MODE-REQUEST-TYPE-MAPS>"
            "<MODE-REQUEST-TYPE-MAP>"
            "<IMPLEMENTATION-DATA-TYPE-REF DEST='IMPLEMENTATION-DATA-TYPE'>/mode-idt</IMPLEMENTATION-DATA-TYPE-REF>"
            "<MODE-GROUP-REF DEST='MODE-DECLARATION-GROUP'>/mode-group</MODE-GROUP-REF>"
            "</MODE-REQUEST-TYPE-MAP>"
            "</MODE-REQUEST-TYPE-MAPS>",
            root_tag="DATA-TYPE-MAPPING-SET",
        )

        parser.readDataTypeMappingSet(element, dtms)

        assert dtms.getShortName() == "DTMS"
        assert len(dtms.getDataTypeMaps()) == 1
        assert dtms.getDataTypeMaps()[0].getApplicationDataTypeRef().getValue() == "/adt"
        assert dtms.getDataTypeMaps()[0].getImplementationDataTypeRef().getValue() == "/idt"
        assert len(dtms.getModeRequestTypeMaps()) == 1
        assert dtms.getModeRequestTypeMaps()[0].getImplementationDataTypeRef().getValue() == "/mode-idt"
        assert dtms.getModeRequestTypeMaps()[0].getModeGroupRef().getValue() == "/mode-group"

    def test_readDataTypeMappingSet_empty(self, parser):
        from armodel.models import DataTypeMappingSet

        dtms = DataTypeMappingSet(parent=_autosar_root(), short_name="DTMS")
        parser.readDataTypeMappingSet(_snip("<SHORT-NAME>DTMS</SHORT-NAME>", root_tag="DATA-TYPE-MAPPING-SET"), dtms)
        assert dtms.getDataTypeMaps() == []
        assert dtms.getModeRequestTypeMaps() == []


# ==================== Group E: BswBehavior orchestrators ====================


class TestBswBehaviorOrchestratorHandlers:
    """Exercise readSwcInternalBehavior (top-level cascade), readBswVariableAccess,
    and the readBswModuleEntityDataSendPoints/DataReceiverPoints dispatchers."""

    def test_readSwcInternalBehavior_minimal(self, warning_parser):
        from armodel.models import ApplicationSwComponentType

        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="a")
        behavior = app.createSwcInternalBehavior("ib")
        element = _snip("<SHORT-NAME>ib</SHORT-NAME>", root_tag="SWC-INTERNAL-BEHAVIOR")
        warning_parser.readSwcInternalBehavior(element, behavior)
        # The two end-of-method optional fields should be None with empty body.
        assert behavior.getHandleTerminationAndRestart() is None
        assert behavior.getSupportsMultipleInstantiation() is None

    def test_readSwcInternalBehavior_exclusiveAreaPolicies(self, warning_parser):
        from armodel.models import ApplicationSwComponentType

        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="a")
        behavior = app.createSwcInternalBehavior("ib")
        element = _snip(
            "<SHORT-NAME>ib</SHORT-NAME>"
            "<EXCLUSIVE-AREA-POLICYS>"
            "<SWC-EXCLUSIVE-AREA-POLICY>"
            "<API-PRINCIPLE>perExecutable</API-PRINCIPLE>"
            '<EXCLUSIVE-AREA-REF DEST="EXCLUSIVE-AREA">/ea1</EXCLUSIVE-AREA-REF>'
            "</SWC-EXCLUSIVE-AREA-POLICY>"
            "</EXCLUSIVE-AREA-POLICYS>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        warning_parser.readSwcInternalBehavior(element, behavior)
        policies = behavior.getExclusiveAreaPolicies()
        assert len(policies) == 1
        assert policies[0].getApiPrinciple().getValue() == "perExecutable"
        assert policies[0].getExclusiveAreaRef().getValue() == "/ea1"

    def test_readSwcInternalBehavior_with_optional_literals(self, warning_parser):
        from armodel.models import ApplicationSwComponentType

        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="a")
        behavior = app.createSwcInternalBehavior("ib")
        element = _snip(
            "<SHORT-NAME>ib</SHORT-NAME>" "<HANDLE-TERMINATION-AND-RESTART>YES</HANDLE-TERMINATION-AND-RESTART>" "<SUPPORTS-MULTIPLE-INSTANTIATION>true</SUPPORTS-MULTIPLE-INSTANTIATION>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        warning_parser.readSwcInternalBehavior(element, behavior)
        assert behavior.getHandleTerminationAndRestart().getValue() == "YES"
        assert behavior.getSupportsMultipleInstantiation() is not None

    def test_readBswVariableAccess_sets_ref(self, parser):
        from armodel.models import BswVariableAccess

        access = BswVariableAccess(parent=_autosar_root(), short_name="va")
        element = _snip(
            "<SHORT-NAME>va</SHORT-NAME>" "<ACCESSED-VARIABLE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/v</ACCESSED-VARIABLE-REF>",
            root_tag="BSW-VARIABLE-ACCESS",
        )
        parser.readBswVariableAccess(element, access)
        assert access.getAccessedVariableRef().getValue() == "/v"

    def test_readBswVariableAccess_missing_ref_is_None(self, parser):
        from armodel.models import BswVariableAccess

        access = BswVariableAccess(parent=_autosar_root(), short_name="va")
        element = _snip("<SHORT-NAME>va</SHORT-NAME>", root_tag="BSW-VARIABLE-ACCESS")
        parser.readBswVariableAccess(element, access)
        assert access.getAccessedVariableRef() is None

    def test_readBswModuleEntityDataSendPoints_creates_point(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bib")
        entity = behavior.createBswSchedulableEntity("e1")
        element = _snip(
            "<DATA-SEND-POINTS>" "<BSW-VARIABLE-ACCESS><SHORT-NAME>s1</SHORT-NAME></BSW-VARIABLE-ACCESS>" "</DATA-SEND-POINTS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntityDataSendPoints(element, entity)
        assert len(entity.getDataSendPoints()) == 1

    def test_readBswModuleEntityDataSendPoints_unsupported_tag_warns(self, warning_parser, caplog):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bib")
        entity = behavior.createBswSchedulableEntity("e1")
        element = _snip("<DATA-SEND-POINTS><BAD/></DATA-SEND-POINTS>", root_tag="ENTITY")
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleEntityDataSendPoints(element, entity)
        assert any("Unsupported Data Send Point" in r.getMessage() for r in caplog.records)

    def test_readBswModuleEntityDataReceiverPoints_creates_point(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bib")
        entity = behavior.createBswSchedulableEntity("e1")
        element = _snip(
            "<DATA-RECEIVE-POINTS>" "<BSW-VARIABLE-ACCESS><SHORT-NAME>r1</SHORT-NAME></BSW-VARIABLE-ACCESS>" "</DATA-RECEIVE-POINTS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntityDataReceiverPoints(element, entity)
        assert len(entity.getDataReceivePoints()) == 1

    def test_readBswModuleEntityDataReceiverPoints_unsupported_tag_warns(self, warning_parser, caplog):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bib")
        entity = behavior.createBswSchedulableEntity("e1")
        element = _snip("<DATA-RECEIVE-POINTS><BAD/></DATA-RECEIVE-POINTS>", root_tag="ENTITY")
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleEntityDataReceiverPoints(element, entity)
        assert any("Unsupported Data Receive Point" in r.getMessage() for r in caplog.records)


# ==================== Group F: Misc Handlers (DataTransformation, Keyword, ModeDeclaration) ====================


class TestDataTransformationHandlers:
    """Exercise readDataTransformationSet, transformation technologies,
    transformation descriptions, data transformations, and buffer properties."""

    def test_readDataTransformationSet_minimal(self, parser):
        from armodel.models import DataTransformationSet

        dtf_set = DataTransformationSet(parent=_autosar_root(), short_name="dtf_set")
        element = _snip(
            "<SHORT-NAME>dtf_set</SHORT-NAME>",
            root_tag="DATA-TRANSFORMATION-SET",
        )
        parser.readDataTransformationSet(element, dtf_set)
        assert dtf_set.getShortName() == "dtf_set"
        assert len(dtf_set.getDataTransformations()) == 0
        assert len(dtf_set.getTransformationTechnologies()) == 0

    def test_readDataTransformationSet_with_transformation(self, parser):
        from armodel.models import DataTransformationSet

        dtf_set = DataTransformationSet(parent=_autosar_root(), short_name="dtf_set")
        element = _snip(
            "<SHORT-NAME>dtf_set</SHORT-NAME>"
            "<DATA-TRANSFORMATIONS>"
            "<DATA-TRANSFORMATION>"
            "<SHORT-NAME>dt1</SHORT-NAME>"
            "<EXECUTE-DESPITE-DATA-UNAVAILABILITY>true</EXECUTE-DESPITE-DATA-UNAVAILABILITY>"
            "</DATA-TRANSFORMATION>"
            "</DATA-TRANSFORMATIONS>",
            root_tag="DATA-TRANSFORMATION-SET",
        )
        parser.readDataTransformationSet(element, dtf_set)
        assert len(dtf_set.getDataTransformations()) == 1
        dt1 = dtf_set.getDataTransformations()[0]
        assert dt1.getShortName() == "dt1"
        assert dt1.getExecuteDespiteDataUnavailability() is not None

    def test_readDataTransformation_with_transformer_chain_refs(self, parser):
        from armodel.models import DataTransformationSet

        dtf_set = DataTransformationSet(parent=_autosar_root(), short_name="dtf_set")
        element = _snip(
            "<SHORT-NAME>dtf_set</SHORT-NAME>"
            "<DATA-TRANSFORMATIONS>"
            "<DATA-TRANSFORMATION>"
            "<SHORT-NAME>dt1</SHORT-NAME>"
            "<DATA-TRANSFORMATION-KIND>SYMMETRIC</DATA-TRANSFORMATION-KIND>"
            "<TRANSFORMER-CHAIN-REFS>"
            "<TRANSFORMER-CHAIN-REF DEST='TRANSFORMER-CHAIN'>/tc1</TRANSFORMER-CHAIN-REF>"
            "<TRANSFORMER-CHAIN-REF DEST='TRANSFORMER-CHAIN'>/tc2</TRANSFORMER-CHAIN-REF>"
            "</TRANSFORMER-CHAIN-REFS>"
            "</DATA-TRANSFORMATION>"
            "</DATA-TRANSFORMATIONS>",
            root_tag="DATA-TRANSFORMATION-SET",
        )
        parser.readDataTransformationSet(element, dtf_set)
        dt1 = dtf_set.getDataTransformations()[0]
        assert dt1.getDataTransformationKind() is not None
        assert dt1.getDataTransformationKind().getValue() == "SYMMETRIC"
        assert len(dt1.getTransformerChainRefs()) == 2
        assert dt1.getTransformerChainRefs()[0].getValue() == "/tc1"
        assert dt1.getTransformerChainRefs()[1].getValue() == "/tc2"

    def test_readDataTransformationSet_unsupported_tag_warns(self, warning_parser, caplog):
        from armodel.models import DataTransformationSet

        dtf_set = DataTransformationSet(parent=_autosar_root(), short_name="dtf_set")
        element = _snip(
            "<SHORT-NAME>dtf_set</SHORT-NAME>" "<DATA-TRANSFORMATIONS><BAD-ELEMENT/></DATA-TRANSFORMATIONS>",
            root_tag="DATA-TRANSFORMATION-SET",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readDataTransformationSet(element, dtf_set)
        assert any("Unsupported DataTransformation" in r.getMessage() for r in caplog.records)

    def test_readTransformationTechnology_minimal(self, parser):
        from armodel.models import DataTransformationSet

        dtf_set = DataTransformationSet(parent=_autosar_root(), short_name="dtf_set")
        element = _snip(
            "<SHORT-NAME>dtf_set</SHORT-NAME>"
            "<TRANSFORMATION-TECHNOLOGYS>"
            "<TRANSFORMATION-TECHNOLOGY>"
            "<SHORT-NAME>tech1</SHORT-NAME>"
            "</TRANSFORMATION-TECHNOLOGY>"
            "</TRANSFORMATION-TECHNOLOGYS>",
            root_tag="DATA-TRANSFORMATION-SET",
        )
        parser.readDataTransformationSet(element, dtf_set)
        assert len(dtf_set.getTransformationTechnologies()) == 1
        tech = dtf_set.getTransformationTechnologies()[0]
        assert tech.getShortName() == "tech1"

    def test_readTransformationTechnology_with_properties(self, parser):
        from armodel.models import DataTransformationSet

        dtf_set = DataTransformationSet(parent=_autosar_root(), short_name="dtf_set")
        element = _snip(
            "<SHORT-NAME>dtf_set</SHORT-NAME>"
            "<TRANSFORMATION-TECHNOLOGYS>"
            "<TRANSFORMATION-TECHNOLOGY>"
            "<SHORT-NAME>tech1</SHORT-NAME>"
            "<HAS-INTERNAL-STATE>true</HAS-INTERNAL-STATE>"
            "<NEEDS-ORIGINAL-DATA>true</NEEDS-ORIGINAL-DATA>"
            "<PROTOCOL>E2E</PROTOCOL>"
            "<TRANSFORMER-CLASS>safety</TRANSFORMER-CLASS>"
            "<VERSION>1.0</VERSION>"
            "</TRANSFORMATION-TECHNOLOGY>"
            "</TRANSFORMATION-TECHNOLOGYS>",
            root_tag="DATA-TRANSFORMATION-SET",
        )
        parser.readDataTransformationSet(element, dtf_set)
        tech = dtf_set.getTransformationTechnologies()[0]
        assert tech.getHasInternalState() is not None
        assert tech.getHasInternalState().getValue() is True
        assert tech.getNeedsOriginalData() is not None
        assert tech.getProtocol().getValue() == "E2E"
        assert tech.getTransformerClass().getValue() == "safety"
        assert tech.getVersion().getValue() == "1.0"

    def test_readTransformationTechnology_with_buffer_properties(self, parser):
        from armodel.models import DataTransformationSet

        dtf_set = DataTransformationSet(parent=_autosar_root(), short_name="dtf_set")
        element = _snip(
            "<SHORT-NAME>dtf_set</SHORT-NAME>"
            "<TRANSFORMATION-TECHNOLOGYS>"
            "<TRANSFORMATION-TECHNOLOGY>"
            "<SHORT-NAME>tech1</SHORT-NAME>"
            "<BUFFER-PROPERTIES>"
            "<HEADER-LENGTH>8</HEADER-LENGTH>"
            "<IN-PLACE>true</IN-PLACE>"
            "</BUFFER-PROPERTIES>"
            "</TRANSFORMATION-TECHNOLOGY>"
            "</TRANSFORMATION-TECHNOLOGYS>",
            root_tag="DATA-TRANSFORMATION-SET",
        )
        parser.readDataTransformationSet(element, dtf_set)
        tech = dtf_set.getTransformationTechnologies()[0]
        assert tech.getBufferProperties() is not None
        assert tech.getBufferProperties().getHeaderLength().getValue() == 8
        assert tech.getBufferProperties().getInPlace() is not None

    def test_readTransformationTechnology_unsupported_tag_warns(self, warning_parser, caplog):
        from armodel.models import DataTransformationSet

        dtf_set = DataTransformationSet(parent=_autosar_root(), short_name="dtf_set")
        element = _snip(
            "<SHORT-NAME>dtf_set</SHORT-NAME>" "<TRANSFORMATION-TECHNOLOGYS><BAD-ELEMENT/></TRANSFORMATION-TECHNOLOGYS>",
            root_tag="DATA-TRANSFORMATION-SET",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readDataTransformationSet(element, dtf_set)
        assert any("Unsupported TransformationTechnology" in r.getMessage() for r in caplog.records)

    def test_readEndToEndTransformationDescription_full(self, parser):
        from armodel.models import DataTransformationSet

        dtf_set = DataTransformationSet(parent=_autosar_root(), short_name="dtf_set")
        element = _snip(
            "<SHORT-NAME>dtf_set</SHORT-NAME>"
            "<TRANSFORMATION-TECHNOLOGYS>"
            "<TRANSFORMATION-TECHNOLOGY>"
            "<SHORT-NAME>tech1</SHORT-NAME>"
            "<TRANSFORMATION-DESCRIPTIONS>"
            "<END-TO-END-TRANSFORMATION-DESCRIPTION>"
            "<DATA-ID-MODE>all16Bit</DATA-ID-MODE>"
            "<MAX-DELTA-COUNTER>2</MAX-DELTA-COUNTER>"
            "<MAX-ERROR-STATE-INIT>1</MAX-ERROR-STATE-INIT>"
            "<MAX-ERROR-STATE-INVALID>2</MAX-ERROR-STATE-INVALID>"
            "<MAX-ERROR-STATE-VALID>3</MAX-ERROR-STATE-VALID>"
            "<MAX-NO-NEW-OR-REPEATED-DATA>2</MAX-NO-NEW-OR-REPEATED-DATA>"
            "<MIN-OK-STATE-INIT>1</MIN-OK-STATE-INIT>"
            "<MIN-OK-STATE-INVALID>1</MIN-OK-STATE-INVALID>"
            "<MIN-OK-STATE-VALID>1</MIN-OK-STATE-VALID>"
            "<PROFILE-BEHAVIOR>R-4-2</PROFILE-BEHAVIOR>"
            "<PROFILE-NAME>Profile1</PROFILE-NAME>"
            "<SYNC-COUNTER-INIT>0</SYNC-COUNTER-INIT>"
            "<UPPER-HEADER-BITS-TO-SHIFT>4</UPPER-HEADER-BITS-TO-SHIFT>"
            "<WINDOW-SIZE-INIT>1</WINDOW-SIZE-INIT>"
            "<WINDOW-SIZE-INVALID>2</WINDOW-SIZE-INVALID>"
            "<WINDOW-SIZE-VALID>3</WINDOW-SIZE-VALID>"
            "</END-TO-END-TRANSFORMATION-DESCRIPTION>"
            "</TRANSFORMATION-DESCRIPTIONS>"
            "</TRANSFORMATION-TECHNOLOGY>"
            "</TRANSFORMATION-TECHNOLOGYS>",
            root_tag="DATA-TRANSFORMATION-SET",
        )
        parser.readDataTransformationSet(element, dtf_set)
        tech = dtf_set.getTransformationTechnologies()[0]
        assert tech.getTransformationDescription() is not None
        desc = tech.getTransformationDescription()
        assert desc.getDataIdMode().getValue() == "all16Bit"
        assert desc.getMaxDeltaCounter().getValue() == 2
        assert desc.getProfileName().getValue() == "Profile1"

    def test_readTransformationTechnology_unsupported_desc_tag_warns(self, warning_parser, caplog):
        from armodel.models import DataTransformationSet

        dtf_set = DataTransformationSet(parent=_autosar_root(), short_name="dtf_set")
        element = _snip(
            "<SHORT-NAME>dtf_set</SHORT-NAME>"
            "<TRANSFORMATION-TECHNOLOGYS>"
            "<TRANSFORMATION-TECHNOLOGY>"
            "<SHORT-NAME>tech1</SHORT-NAME>"
            "<TRANSFORMATION-DESCRIPTIONS><BAD-DESC/></TRANSFORMATION-DESCRIPTIONS>"
            "</TRANSFORMATION-TECHNOLOGY>"
            "</TRANSFORMATION-TECHNOLOGYS>",
            root_tag="DATA-TRANSFORMATION-SET",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readDataTransformationSet(element, dtf_set)
        assert any("Unsupported TransformationDescription" in r.getMessage() for r in caplog.records)


class TestKeywordAndCollectionHandlers:
    """Exercise readKeywordSet/Keywords, readKeyword/Classifications,
    readCollection + element refs."""

    def test_readKeywordSet_minimal(self, parser):
        from armodel.models import KeywordSet

        ks = KeywordSet(parent=_autosar_root(), short_name="ks")
        element = _snip(
            "<SHORT-NAME>ks</SHORT-NAME>",
            root_tag="KEYWORD-SET",
        )
        parser.readKeywordSet(element, ks)
        assert ks.getShortName() == "ks"
        assert len(ks.getKeywords()) == 0

    def test_readKeywordSet_with_keywords(self, parser):
        from armodel.models import KeywordSet

        ks = KeywordSet(parent=_autosar_root(), short_name="ks")
        element = _snip(
            "<SHORT-NAME>ks</SHORT-NAME>" "<KEYWORDS>" "<KEYWORD>" "<SHORT-NAME>kw1</SHORT-NAME>" "</KEYWORD>" "<KEYWORD>" "<SHORT-NAME>kw2</SHORT-NAME>" "</KEYWORD>" "</KEYWORDS>",
            root_tag="KEYWORD-SET",
        )
        parser.readKeywordSet(element, ks)
        assert len(ks.getKeywords()) == 2
        assert ks.getKeywords()[0].getShortName() == "kw1"
        assert ks.getKeywords()[1].getShortName() == "kw2"

    def test_readKeyword_with_abbr_name_and_classifications(self, parser):
        from armodel.models import KeywordSet

        ks = KeywordSet(parent=_autosar_root(), short_name="ks")
        element = _snip(
            "<SHORT-NAME>ks</SHORT-NAME>"
            "<KEYWORDS>"
            "<KEYWORD>"
            "<SHORT-NAME>kw1</SHORT-NAME>"
            "<ABBR-NAME>abbr1</ABBR-NAME>"
            "<CLASSIFICATIONS>"
            "<CLASSIFICATION>class1</CLASSIFICATION>"
            "<CLASSIFICATION>class2</CLASSIFICATION>"
            "</CLASSIFICATIONS>"
            "</KEYWORD>"
            "</KEYWORDS>",
            root_tag="KEYWORD-SET",
        )
        parser.readKeywordSet(element, ks)
        kw = ks.getKeywords()[0]
        assert kw.getAbbrName().getValue() == "abbr1"
        assert len(kw.getClassifications()) == 2
        assert kw.getClassifications()[0].getValue() == "class1"
        assert kw.getClassifications()[1].getValue() == "class2"

    def test_readKeywordSet_unsupported_tag_warns(self, warning_parser, caplog):
        from armodel.models import KeywordSet

        ks = KeywordSet(parent=_autosar_root(), short_name="ks")
        element = _snip(
            "<SHORT-NAME>ks</SHORT-NAME>" "<KEYWORDS><BAD-KEYWORD/></KEYWORDS>",
            root_tag="KEYWORD-SET",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readKeywordSet(element, ks)
        assert any("Unsupported Keyword" in r.getMessage() for r in caplog.records)

    def test_readCollection_minimal(self, parser):
        from armodel.models import Collection

        coll = Collection(parent=_autosar_root(), short_name="coll")
        element = _snip(
            "<SHORT-NAME>coll</SHORT-NAME>",
            root_tag="COLLECTION",
        )
        parser.readCollection(element, coll)
        assert coll.getShortName() == "coll"
        assert coll.getAutoCollect() is None
        assert coll.getElementRole() is None

    def test_readCollection_with_properties_and_refs(self, parser):
        from armodel.models import Collection

        coll = Collection(parent=_autosar_root(), short_name="coll")
        element = _snip(
            "<SHORT-NAME>coll</SHORT-NAME>"
            "<AUTO-COLLECT>REF-ALL</AUTO-COLLECT>"
            "<ELEMENT-ROLE>role1</ELEMENT-ROLE>"
            "<ELEMENT-REFS>"
            "<ELEMENT-REF DEST='ELEMENT'>/e1</ELEMENT-REF>"
            "<ELEMENT-REF DEST='ELEMENT'>/e2</ELEMENT-REF>"
            "</ELEMENT-REFS>"
            "<SOURCE-ELEMENT-REFS>"
            "<SOURCE-ELEMENT-REF DEST='ELEMENT'>/s1</SOURCE-ELEMENT-REF>"
            "</SOURCE-ELEMENT-REFS>",
            root_tag="COLLECTION",
        )
        parser.readCollection(element, coll)
        assert coll.getAutoCollect().getValue() == "refAll"
        assert coll.getElementRole().getValue() == "role1"
        assert len(coll.getElementRefs()) == 2
        assert coll.getElementRefs()[0].getValue() == "/e1"
        assert coll.getElementRefs()[1].getValue() == "/e2"
        assert len(coll.getSourceElementRefs()) == 1
        assert coll.getSourceElementRefs()[0].getValue() == "/s1"


class TestModeDeclarationMappingHandlers:
    """Exercise readModeDeclarationMappingSet/Mappings,
    readModeDeclarationMapping, first mode refs, port prototype blueprint."""

    def test_readModeDeclarationMappingSet_minimal(self, parser):
        from armodel.models import ModeDeclarationMappingSet

        mms = ModeDeclarationMappingSet(parent=_autosar_root(), short_name="mms")
        element = _snip(
            "<SHORT-NAME>mms</SHORT-NAME>",
            root_tag="MODE-DECLARATION-MAPPING-SET",
        )
        parser.readModeDeclarationMappingSet(element, mms)
        assert mms.getShortName() == "mms"
        assert len(mms.getModeDeclarationMappings()) == 0

    def test_readModeDeclarationMappingSet_with_mapping(self, parser):
        from armodel.models import ModeDeclarationMappingSet

        mms = ModeDeclarationMappingSet(parent=_autosar_root(), short_name="mms")
        element = _snip(
            "<SHORT-NAME>mms</SHORT-NAME>" "<MODE-DECLARATION-MAPPINGS>" "<MODE-DECLARATION-MAPPING>" "<SHORT-NAME>mapping1</SHORT-NAME>" "</MODE-DECLARATION-MAPPING>" "</MODE-DECLARATION-MAPPINGS>",
            root_tag="MODE-DECLARATION-MAPPING-SET",
        )
        parser.readModeDeclarationMappingSet(element, mms)
        assert len(mms.getModeDeclarationMappings()) == 1
        mapping = mms.getModeDeclarationMappings()[0]
        assert mapping.getShortName() == "mapping1"

    def test_readModeDeclarationMappingSet_round_trip(self, parser):
        from armodel.models import ModeDeclarationMappingSet
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.writer.arxml_writer import ARXMLWriter

        mms = ModeDeclarationMappingSet(parent=_autosar_root(), short_name="mms")
        mapping = mms.createModeDeclarationMapping("mapping1")
        first_ref = RefType()
        first_ref.setValue("/mode1")
        mapping.addFirstModeRef(first_ref)
        second_ref = RefType()
        second_ref.setValue("/mode2")
        second_ref.dest = "MODE-DECLARATION"
        mapping.setSecondModeRef(second_ref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeModeDeclarationMappingSet(parent, mms)
        inner = ET.tostring(parent[0], encoding="unicode")
        container = ET.fromstring(f"<MODE-DECLARATION-MAPPING-SETS xmlns='{NS}'>{inner}</MODE-DECLARATION-MAPPING-SETS>")
        element = container[0]

        recovered = ModeDeclarationMappingSet(parent=_autosar_root(), short_name="recovered")
        parser.readModeDeclarationMappingSet(element, recovered)
        mappings = recovered.getModeDeclarationMappings()
        assert len(mappings) == 1
        assert mappings[0].getShortName() == "mapping1"
        first_refs = mappings[0].getFirstModeRefs()
        assert len(first_refs) == 1
        assert first_refs[0].getValue() == "/mode1"
        second_ref_recovered = mappings[0].getSecondModeRef()
        assert second_ref_recovered is not None
        assert second_ref_recovered.getValue() == "/mode2"
        assert second_ref_recovered.dest == "MODE-DECLARATION"

    def test_readModeDeclarationMapping_with_refs(self, parser):
        from armodel.models import ModeDeclarationMappingSet

        mms = ModeDeclarationMappingSet(parent=_autosar_root(), short_name="mms")
        element = _snip(
            "<SHORT-NAME>mms</SHORT-NAME>"
            "<MODE-DECLARATION-MAPPINGS>"
            "<MODE-DECLARATION-MAPPING>"
            "<SHORT-NAME>mapping1</SHORT-NAME>"
            "<FIRST-MODE-REFS>"
            "<FIRST-MODE-REF DEST='MODE-DECLARATION'>/mode1</FIRST-MODE-REF>"
            "<FIRST-MODE-REF DEST='MODE-DECLARATION'>/mode2</FIRST-MODE-REF>"
            "</FIRST-MODE-REFS>"
            "<SECOND-MODE-REF DEST='MODE-DECLARATION'>/mode3</SECOND-MODE-REF>"
            "</MODE-DECLARATION-MAPPING>"
            "</MODE-DECLARATION-MAPPINGS>",
            root_tag="MODE-DECLARATION-MAPPING-SET",
        )
        parser.readModeDeclarationMappingSet(element, mms)
        mapping = mms.getModeDeclarationMappings()[0]
        assert len(mapping.getFirstModeRefs()) == 2
        assert mapping.getFirstModeRefs()[0].getValue() == "/mode1"
        assert mapping.getFirstModeRefs()[1].getValue() == "/mode2"
        assert mapping.getSecondModeRef().getValue() == "/mode3"

    def test_readModeDeclarationMappingSet_unsupported_tag_warns(self, warning_parser, caplog):
        from armodel.models import ModeDeclarationMappingSet

        mms = ModeDeclarationMappingSet(parent=_autosar_root(), short_name="mms")
        element = _snip(
            "<SHORT-NAME>mms</SHORT-NAME>" "<MODE-DECLARATION-MAPPINGS><BAD-MAPPING/></MODE-DECLARATION-MAPPINGS>",
            root_tag="MODE-DECLARATION-MAPPING-SET",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readModeDeclarationMappingSet(element, mms)
        assert any("Unsupported ModeDeclarationMapping" in r.getMessage() for r in caplog.records)


class TestModeDeclarationGroupPrototypeHandlers:
    """Exercise readModeDeclarationGroupPrototype."""

    def test_readModeDeclarationGroupPrototype_minimal(self, parser):
        from armodel.models import ModeDeclarationGroupPrototype

        proto = ModeDeclarationGroupPrototype(parent=_autosar_root(), short_name="proto")
        element = _snip(
            "<SHORT-NAME>proto</SHORT-NAME>",
            root_tag="MODE-DECLARATION-GROUP-PROTOTYPE",
        )
        parser.readModeDeclarationGroupPrototype(element, proto)
        assert proto.getShortName() == "proto"
        assert proto.getTypeTRef() is None

    def test_readModeDeclarationGroupPrototype_with_type_ref(self, parser):
        from armodel.models import ModeDeclarationGroupPrototype

        proto = ModeDeclarationGroupPrototype(parent=_autosar_root(), short_name="proto")
        element = _snip(
            "<SHORT-NAME>proto</SHORT-NAME>" "<TYPE-TREF DEST='MODE-DECLARATION-GROUP'>/mdg1</TYPE-TREF>",
            root_tag="MODE-DECLARATION-GROUP-PROTOTYPE",
        )
        parser.readModeDeclarationGroupPrototype(element, proto)
        assert proto.getTypeTRef() is not None
        assert proto.getTypeTRef().getValue() == "/mdg1"


class TestModeDeclarationGroupHandlers:
    """Exercise readModeDeclarationGroup."""

    def test_readModeDeclarationGroup_with_modes(self, parser):
        from armodel.models import ModeDeclarationGroup
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

        group = ModeDeclarationGroup(parent=_autosar_root(), short_name="Group")
        element = _snip(
            "<SHORT-NAME>Group</SHORT-NAME>"
            "<MODE-DECLARATIONS>"
            "<MODE-DECLARATION><SHORT-NAME>Mode1</SHORT-NAME><VALUE>4</VALUE></MODE-DECLARATION>"
            "</MODE-DECLARATIONS>"
            "<INITIAL-MODE-REF DEST='MODE-DECLARATION'>/Group/Mode1</INITIAL-MODE-REF>"
            "<ON-TRANSITION-VALUE>7</ON-TRANSITION-VALUE>",
            root_tag="MODE-DECLARATION-GROUP",
        )
        parser.readModeDeclarationGroup(element, group)
        assert group.getShortName() == "Group"
        decls = group.getModeDeclarations()
        assert len(decls) == 1
        assert decls[0].getShortName() == "Mode1"
        assert isinstance(decls[0].getValue(), PositiveInteger)
        assert decls[0].getValue().getValue() == 4
        assert group.getInitialModeRef().getValue() == "/Group/Mode1"
        assert group.getOnTransitionValue().getValue() == 7

    def test_readModeDeclarationGroup_empty_modes(self, parser):
        from armodel.models import ModeDeclarationGroup

        group = ModeDeclarationGroup(parent=_autosar_root(), short_name="Group")
        element = _snip(
            "<SHORT-NAME>Group</SHORT-NAME>",
            root_tag="MODE-DECLARATION-GROUP",
        )
        parser.readModeDeclarationGroup(element, group)
        assert group.getModeDeclarations() == []
        assert group.getInitialModeRef() is None
        assert group.getOnTransitionValue() is None

    def test_readModeDeclarationGroup_mode_manager_error_behavior(self, parser):
        from armodel.models import ModeDeclarationGroup, ModeErrorReactionPolicyEnum

        group = ModeDeclarationGroup(parent=_autosar_root(), short_name="Group")
        element = _snip(
            "<SHORT-NAME>Group</SHORT-NAME>"
            "<MODE-MANAGER-ERROR-BEHAVIOR>"
            "<DEFAULT-MODE-REF DEST='MODE-DECLARATION'>/Group/ErrorMode</DEFAULT-MODE-REF>"
            "<ERROR-REACTION-POLICY>defaultMode</ERROR-REACTION-POLICY>"
            "</MODE-MANAGER-ERROR-BEHAVIOR>",
            root_tag="MODE-DECLARATION-GROUP",
        )
        parser.readModeDeclarationGroup(element, group)
        behavior = group.getModeManagerErrorBehavior()
        assert behavior is not None
        assert behavior.getDefaultModeRef().getValue() == "/Group/ErrorMode"
        assert isinstance(behavior.getErrorReactionPolicy(), ModeErrorReactionPolicyEnum)
        assert behavior.getErrorReactionPolicy().getValue() == ModeErrorReactionPolicyEnum.DEFAULT_MODE

    def test_readModeDeclarationGroup_mode_user_error_behavior(self, parser):
        from armodel.models import ModeDeclarationGroup, ModeErrorReactionPolicyEnum

        group = ModeDeclarationGroup(parent=_autosar_root(), short_name="Group")
        element = _snip(
            "<SHORT-NAME>Group</SHORT-NAME>"
            "<MODE-USER-ERROR-BEHAVIOR>"
            "<DEFAULT-MODE-REF DEST='MODE-DECLARATION'>/Group/ErrorMode</DEFAULT-MODE-REF>"
            "<ERROR-REACTION-POLICY>lastMode</ERROR-REACTION-POLICY>"
            "</MODE-USER-ERROR-BEHAVIOR>",
            root_tag="MODE-DECLARATION-GROUP",
        )
        parser.readModeDeclarationGroup(element, group)
        behavior = group.getModeUserErrorBehavior()
        assert behavior is not None
        assert behavior.getDefaultModeRef().getValue() == "/Group/ErrorMode"
        assert isinstance(behavior.getErrorReactionPolicy(), ModeErrorReactionPolicyEnum)
        assert behavior.getErrorReactionPolicy().getValue() == ModeErrorReactionPolicyEnum.LAST_MODE

    def test_readModeDeclarationGroup_mode_transitions(self, parser):
        from armodel.models import ModeDeclarationGroup

        group = ModeDeclarationGroup(parent=_autosar_root(), short_name="Group")
        element = _snip(
            "<SHORT-NAME>Group</SHORT-NAME>"
            "<MODE-TRANSITIONS>"
            "<MODE-TRANSITION>"
            "<SHORT-NAME>Transition1</SHORT-NAME>"
            "<ENTERED-MODE-REF DEST='MODE-DECLARATION'>/Group/Mode2</ENTERED-MODE-REF>"
            "<EXITED-MODE-REF DEST='MODE-DECLARATION'>/Group/Mode1</EXITED-MODE-REF>"
            "</MODE-TRANSITION>"
            "</MODE-TRANSITIONS>",
            root_tag="MODE-DECLARATION-GROUP",
        )
        parser.readModeDeclarationGroup(element, group)
        transitions = group.getModeTransitions()
        assert len(transitions) == 1
        assert transitions[0].getShortName() == "Transition1"
        assert transitions[0].getEnteredModeRef().getValue() == "/Group/Mode2"
        assert transitions[0].getExitedModeRef().getValue() == "/Group/Mode1"

    def test_readPortPrototypeBlueprint_minimal(self, parser):
        from armodel.models import PortPrototypeBlueprint

        blueprint = PortPrototypeBlueprint(parent=_autosar_root(), short_name="blueprint")
        element = _snip(
            "<SHORT-NAME>blueprint</SHORT-NAME>",
            root_tag="PORT-PROTOTYPE-BLUEPRINT",
        )
        parser.readPortPrototypeBlueprint(element, blueprint)
        assert blueprint.getShortName() == "blueprint"
        assert blueprint.getInterfaceRef() is None

    def test_readPortPrototypeBlueprint_with_interface_ref(self, parser):
        from armodel.models import PortPrototypeBlueprint

        blueprint = PortPrototypeBlueprint(parent=_autosar_root(), short_name="blueprint")
        element = _snip(
            "<SHORT-NAME>blueprint</SHORT-NAME>" "<INTERFACE-REF DEST='SENDER-RECEIVER-INTERFACE'>/sri1</INTERFACE-REF>",
            root_tag="PORT-PROTOTYPE-BLUEPRINT",
        )
        parser.readPortPrototypeBlueprint(element, blueprint)
        assert blueprint.getInterfaceRef() is not None
        assert blueprint.getInterfaceRef().getValue() == "/sri1"


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestPortGroupAndComposition:
    def test_readSwComponentTypePortGroups_unsupported_raises(self, warning_parser, caplog):
        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
        element = _snip("<PORT-GROUPS><BAD/></PORT-GROUPS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwComponentTypePortGroups(element, app)
        assert any("Unsupported Port Group type" in r.getMessage() for r in caplog.records)

    def test_readDelegationSwConnectorInnerPortIRef_unsupported_raises(self, warning_parser, caplog):
        from armodel.models import DelegationSwConnector

        connector = DelegationSwConnector(parent=MagicMock(), short_name="Dc")
        element = _snip("<INNER-PORT-IREF><BAD/></INNER-PORT-IREF>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readDelegationSwConnectorInnerPortIRef(element, connector)
        assert any("Unsupported child element of INNER-PORT-IREF" in r.getMessage() for r in caplog.records)

    def test_readCompositionSwComponentTypeComponents_unsupported_warns(self, warning_parser, caplog):
        comp = CompositionSwComponentType(parent=_autosar_root(), short_name="Comp")
        element = _snip("<COMPONENTS><BAD/></COMPONENTS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readCompositionSwComponentTypeComponents(element, comp)
        assert any("Unsupported Component" in r.getMessage() for r in caplog.records)


# ==================== InvalidationPolicies (L2423-2426, L2455) ====================
# readInvalidationPolicys was removed: it was an unreachable duplicate of
# readSenderReceiverInterfaceInvalidationPolicies that referenced nonexistent
# snake_case attributes (data_element_ref / handle_invalid) on InvalidationPolicy.


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestTimingGaps:
    def test_readExecutionOrderConstraint_order_unsupported_raises(self, warning_parser, caplog):
        from armodel.models import SwcTiming

        swc_timing = SwcTiming(parent=_autosar_root(), short_name="T")
        element = _snip(
            "<TIMING-REQUIREMENTS>"
            "<EXECUTION-ORDER-CONSTRAINT>"
            "<SHORT-NAME>eoc</SHORT-NAME>"
            "<ORDERED-ELEMENTS>"
            "<BAD/>"
            "</ORDERED-ELEMENTS>"
            "</EXECUTION-ORDER-CONSTRAINT>"
            "</TIMING-REQUIREMENTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readTimingExtension(element, swc_timing)
        assert any("Unsupported order element" in r.getMessage() for r in caplog.records)

    def test_readTimingExtension_unsupported_requirement_raises(self, warning_parser, caplog):
        from armodel.models import SwcTiming

        swc_timing = SwcTiming(parent=_autosar_root(), short_name="T")
        element = _snip("<TIMING-REQUIREMENTS>" "<BAD-REQ/>" "</TIMING-REQUIREMENTS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readTimingExtension(element, swc_timing)
        assert any("Unsupported timing requirement" in r.getMessage() for r in caplog.records)


# ==================== FrameTriggering / Flexray (L3010, L3038-3044, L3059) ====================


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestSwSystemconstantValueSet:
    def test_readSwSystemconstantValueSetSwSystemconstantValues_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import SwSystemconstantValueSet

        value_set = SwSystemconstantValueSet(parent=MagicMock(), short_name="Vs")
        element = _snip("<SW-SYSTEMCONSTANT-VALUES><BAD/></SW-SYSTEMCONSTANT-VALUES>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwSystemconstantValueSetSwSystemconstantValues(element, value_set)
        assert any("Unsupported SwSystemconstValue" in r.getMessage() for r in caplog.records)


# ==================== CouplingPort (L4873) ====================


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestLifeCycleInfoSet:
    def test_readLifeCycleInfoSetLifeCycleInfos_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import LifeCycleInfoSet

        info_set = LifeCycleInfoSet(parent=MagicMock(), short_name="Lcs")
        element = _snip("<LIFE-CYCLE-INFOS><BAD/></LIFE-CYCLE-INFOS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readLifeCycleInfoSetLifeCycleInfos(element, info_set)
        assert any("Unsupported Life Cycle Info" in r.getMessage() for r in caplog.records)


# ==================== FlatMap (L5567) ====================


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestFlatMap:
    def test_readFlatMapInstances_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import FlatMap

        flat_map = FlatMap(parent=MagicMock(), short_name="Fm")
        element = _snip("<INSTANCES><BAD/></INSTANCES>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readFlatMapInstances(element, flat_map)
        assert any("Unsupported Flat Map Instances" in r.getMessage() for r in caplog.records)


# ==================== ClientServerInterfaceMapping (L5601) ====================


# ==================== J1939Cluster (Table 3.28, R23-11) ====================


class TestReadJ1939Cluster:
    def test_readJ1939Cluster_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import J1939Cluster

        cluster = J1939Cluster(parent=_autosar_root(), short_name="JCluster1")
        element = _snip(
            "<J-1939-CLUSTER-VARIANTS>"
            "<J-1939-CLUSTER-CONDITIONAL>"
            "<PROTOCOL-NAME>JAUS</PROTOCOL-NAME>"
            "<NETWORK-ID>2</NETWORK-ID>"
            "<REQUEST-2-SUPPORT>true</REQUEST-2-SUPPORT>"
            "<USES-ADDRESS-ARBITRATION>false</USES-ADDRESS-ARBITRATION>"
            "</J-1939-CLUSTER-CONDITIONAL>"
            "</J-1939-CLUSTER-VARIANTS>",
            root_tag="J-1939-CLUSTER",
        )
        parser.readJ1939Cluster(element, cluster)
        assert cluster.getProtocolName().getValue() == "JAUS"
        assert cluster.getNetworkId().getValue() == 2
        assert cluster.getRequest2Support().getValue() is True
        assert cluster.getUsesAddressArbitration().getValue() is False

    def test_readJ1939Cluster_empty(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import J1939Cluster

        cluster = J1939Cluster(parent=_autosar_root(), short_name="JCluster1")
        element = _snip("", root_tag="J-1939-CLUSTER")
        parser.readJ1939Cluster(element, cluster)
        assert cluster.getNetworkId() is None
        assert cluster.getRequest2Support() is None
        assert cluster.getUsesAddressArbitration() is None


class TestReadTcpProps:
    """Tests for readTcpProps handler (R23-11 TcpProps, Table 3.111, p.155)."""

    def test_read_tcp_props_full(self, parser):
        element = _snip(
            """
                <TCP-CONGESTION-AVOIDANCE-ENABLED>true</TCP-CONGESTION-AVOIDANCE-ENABLED>
                <TCP-DELAYED-ACK-TIMEOUT>0.1</TCP-DELAYED-ACK-TIMEOUT>
                <TCP-KEEP-ALIVE-PROBES-MAX>5</TCP-KEEP-ALIVE-PROBES-MAX>
                <TCP-MAX-RTX>4</TCP-MAX-RTX>
                <TCP-NAGLE-ENABLED>false</TCP-NAGLE-ENABLED>
                <TCP-RETRANSMISSION-TIMEOUT>0.5</TCP-RETRANSMISSION-TIMEOUT>
                <TCP-TTL>64</TCP-TTL>
            """,
            root_tag="TCP-PROPS",
        )
        props = TcpProps()
        parser.readTcpProps(element, props)
        assert props.getTcpCongestionAvoidanceEnabled().getValue() is True
        assert props.getTcpDelayedAckTimeout().getValue() == 0.1
        assert props.getTcpKeepAliveProbesMax().getValue() == 5
        assert props.getTcpMaxRtx().getValue() == 4
        assert props.getTcpNagleEnabled().getValue() is False
        assert props.getTcpRetransmissionTimeout().getValue() == 0.5
        assert props.getTcpTtl().getValue() == 64

    def test_read_tcp_props_empty(self, parser):
        element = _snip("", root_tag="TCP-PROPS")
        props = TcpProps()
        parser.readTcpProps(element, props)
        assert props.getTcpTtl() is None
        assert props.getTcpNagleEnabled() is None
        assert props.getTcpRetransmissionTimeout() is None


class TestReadUdpProps:
    """Tests for readUdpProps handler (R23-11 UdpProps, Table 3.110, p.154)."""

    def test_read_udp_props_full(self, parser):
        element = _snip("<UDP-TTL>64</UDP-TTL>", root_tag="UDP-PROPS")
        props = UdpProps()
        parser.readUdpProps(element, props)
        assert props.getUdpTtl().getValue() == 64

    def test_read_udp_props_empty(self, parser):
        element = _snip("", root_tag="UDP-PROPS")
        props = UdpProps()
        parser.readUdpProps(element, props)
        assert props.getUdpTtl() is None


class TestReadEthTcpIpProps:
    """Tests for readEthTcpIpProps handler (R23-11 EthTcpIpProps, Table 3.109, p.153)."""

    def test_read_eth_tcp_ip_props_full(self, parser):

        element = _snip(
            """
                <SHORT-NAME>Props1</SHORT-NAME>
                <TCP-PROPS>
                    <TCP-TTL>64</TCP-TTL>
                </TCP-PROPS>
                <UDP-PROPS>
                    <UDP-TTL>32</UDP-TTL>
                </UDP-PROPS>
            """,
            root_tag="ETH-TCP-IP-PROPS",
        )
        props = EthTcpIpProps(parent=_autosar_root(), short_name="Props1")
        parser.readEthTcpIpProps(element, props)
        assert props.getTcpProps() is not None
        assert props.getTcpProps().getTcpTtl().getValue() == 64
        assert props.getUdpProps() is not None
        assert props.getUdpProps().getUdpTtl().getValue() == 32

    def test_read_eth_tcp_ip_props_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Props1</SHORT-NAME>
            """,
            root_tag="ETH-TCP-IP-PROPS",
        )
        props = EthTcpIpProps(parent=_autosar_root(), short_name="Props1")
        parser.readEthTcpIpProps(element, props)
        assert props.getTcpProps() is None
        assert props.getUdpProps() is None


class TestReadTcpIpIcmpv4Props:
    """Tests for readTcpIpIcmpv4Props handler (R23-11 TcpIpIcmpv4Props, Table 3.113, p.156)."""

    def test_read_tcp_ip_icmpv4_props_full(self, parser):
        element = _snip(
            """
                <TCP-IP-ICMP-V-4-ECHO-REPLY-ENABLED>true</TCP-IP-ICMP-V-4-ECHO-REPLY-ENABLED>
                <TCP-IP-ICMP-V-4-TTL>64</TCP-IP-ICMP-V-4-TTL>
            """,
            root_tag="ICMP-V-4-PROPS",
        )
        props = TcpIpIcmpv4Props()
        parser.readTcpIpIcmpv4Props(element, props)
        assert props.getTcpIpIcmpV4EchoReplyEnabled().getValue() is True
        assert props.getTcpIpIcmpV4Ttl().getValue() == 64

    def test_read_tcp_ip_icmpv4_props_empty(self, parser):
        element = _snip("", root_tag="ICMP-V-4-PROPS")
        props = TcpIpIcmpv4Props()
        parser.readTcpIpIcmpv4Props(element, props)
        assert props.getTcpIpIcmpV4EchoReplyEnabled() is None
        assert props.getTcpIpIcmpV4Ttl() is None


class TestReadTcpIpIcmpv6Props:
    """Tests for readTcpIpIcmpv6Props handler (R23-11 TcpIpIcmpv6Props, Table 3.114, p.157)."""

    def test_read_tcp_ip_icmpv6_props_full(self, parser):
        element = _snip(
            """
                <TCP-IP-ICMP-V-6-ECHO-REPLY-AVOID-FRAGMENTATION>true</TCP-IP-ICMP-V-6-ECHO-REPLY-AVOID-FRAGMENTATION>
                <TCP-IP-ICMP-V-6-ECHO-REPLY-ENABLED>false</TCP-IP-ICMP-V-6-ECHO-REPLY-ENABLED>
                <TCP-IP-ICMP-V-6-HOP-LIMIT>255</TCP-IP-ICMP-V-6-HOP-LIMIT>
                <TCP-IP-ICMP-V-6-MSG-DESTINATION-UNREACHABLE-ENABLED>true</TCP-IP-ICMP-V-6-MSG-DESTINATION-UNREACHABLE-ENABLED>
                <TCP-IP-ICMP-V-6-MSG-PARAMETER-PROBLEM-ENABLED>false</TCP-IP-ICMP-V-6-MSG-PARAMETER-PROBLEM-ENABLED>
            """,
            root_tag="ICMP-V-6-PROPS",
        )
        props = TcpIpIcmpv6Props()
        parser.readTcpIpIcmpv6Props(element, props)
        assert props.getTcpIpIcmpV6EchoReplyAvoidFragmentation().getValue() is True
        assert props.getTcpIpIcmpV6EchoReplyEnabled().getValue() is False
        assert props.getTcpIpIcmpV6HopLimit().getValue() == 255
        assert props.getTcpIpIcmpV6MsgDestinationUnreachableEnabled().getValue() is True
        assert props.getTcpIpIcmpV6MsgParameterProblemEnabled().getValue() is False

    def test_read_tcp_ip_icmpv6_props_empty(self, parser):
        element = _snip("", root_tag="ICMP-V-6-PROPS")
        props = TcpIpIcmpv6Props()
        parser.readTcpIpIcmpv6Props(element, props)
        assert props.getTcpIpIcmpV6EchoReplyAvoidFragmentation() is None
        assert props.getTcpIpIcmpV6EchoReplyEnabled() is None
        assert props.getTcpIpIcmpV6HopLimit() is None
        assert props.getTcpIpIcmpV6MsgDestinationUnreachableEnabled() is None
        assert props.getTcpIpIcmpV6MsgParameterProblemEnabled() is None


class TestReadEthTcpIpIcmpProps:
    """Tests for readEthTcpIpIcmpProps handler (R23-11 EthTcpIpIcmpProps, Table 3.112, p.156)."""

    def test_read_eth_tcp_ip_icmp_props_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Props1</SHORT-NAME>
                <ICMP-V-4-PROPS>
                    <TCP-IP-ICMP-V-4-ECHO-REPLY-ENABLED>true</TCP-IP-ICMP-V-4-ECHO-REPLY-ENABLED>
                    <TCP-IP-ICMP-V-4-TTL>64</TCP-IP-ICMP-V-4-TTL>
                </ICMP-V-4-PROPS>
                <ICMP-V-6-PROPS>
                    <TCP-IP-ICMP-V-6-ECHO-REPLY-ENABLED>false</TCP-IP-ICMP-V-6-ECHO-REPLY-ENABLED>
                    <TCP-IP-ICMP-V-6-HOP-LIMIT>255</TCP-IP-ICMP-V-6-HOP-LIMIT>
                </ICMP-V-6-PROPS>
            """,
            root_tag="ETH-TCP-IP-ICMP-PROPS",
        )
        props = EthTcpIpIcmpProps(parent=_autosar_root(), short_name="Props1")
        parser.readEthTcpIpIcmpProps(element, props)
        assert props.getIcmpV4Props() is not None
        assert props.getIcmpV4Props().getTcpIpIcmpV4EchoReplyEnabled().getValue() is True
        assert props.getIcmpV4Props().getTcpIpIcmpV4Ttl().getValue() == 64
        assert props.getIcmpV6Props() is not None
        assert props.getIcmpV6Props().getTcpIpIcmpV6EchoReplyEnabled().getValue() is False
        assert props.getIcmpV6Props().getTcpIpIcmpV6HopLimit().getValue() == 255

    def test_read_eth_tcp_ip_icmp_props_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Props1</SHORT-NAME>
            """,
            root_tag="ETH-TCP-IP-ICMP-PROPS",
        )
        props = EthTcpIpIcmpProps(parent=_autosar_root(), short_name="Props1")
        parser.readEthTcpIpIcmpProps(element, props)
        assert props.getIcmpV4Props() is None
        assert props.getIcmpV6Props() is None


class TestReadOsTaskProxy:
    """Tests for readOsTaskProxy handler (R23-11 OsTaskProxy, Table 5.15, p.208)."""

    def test_read_os_task_proxy_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>TaskProxy1</SHORT-NAME>
                <PERIOD>0.01</PERIOD>
                <PREEMPTABILITY>FULL</PREEMPTABILITY>
                <PRIORITY>4</PRIORITY>
            """,
            root_tag="OS-TASK-PROXY",
        )
        proxy = OsTaskProxy(parent=_autosar_root(), short_name="TaskProxy1")
        parser.readOsTaskProxy(element, proxy)
        assert proxy.getPeriod() is not None
        assert proxy.getPeriod().getValue() == 0.01
        assert proxy.getPreemptability() is not None
        assert isinstance(proxy.getPreemptability(), OsTaskPreemptabilityEnum)
        assert proxy.getPreemptability().getValue() == "FULL"
        assert proxy.getPriority() is not None
        assert proxy.getPriority().getValue() == 4

    def test_read_os_task_proxy_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>TaskProxy1</SHORT-NAME>
            """,
            root_tag="OS-TASK-PROXY",
        )
        proxy = OsTaskProxy(parent=_autosar_root(), short_name="TaskProxy1")
        parser.readOsTaskProxy(element, proxy)
        assert proxy.getPeriod() is None
        assert proxy.getPreemptability() is None
        assert proxy.getPriority() is None
