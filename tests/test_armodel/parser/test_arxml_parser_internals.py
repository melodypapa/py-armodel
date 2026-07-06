"""Phase D: targeted tests for uncovered internal parser methods.

Each test directly invokes an internal method on ARXMLParser with a minimal
XML snippet, lifting coverage on specific handler bodies that the dispatch
tests in test_arxml_parser_dispatch.py only route around.

Focus areas (from coverage report on arxml_parser.py):
- SDG / Sd / SdgCaption / SdgSdxRefs parsing (lines 250-323)
- DocRevision / Modification parsing (lines 293-323)
- _readVariableAccesses branching (lines 426-457)
"""

import logging

import pytest
import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models import (
    AdminData,
    Annotation,
    BswModuleDescription,
    DocRevision,
    DocumentationBlock,
    Graphic,
    LGraphic,
    MlFigure,
    MultiLanguageParagraph,
    MultiLanguagePlainText,
    RunnableEntity,
    Sdg,
    SwAxisGrouped,
    SwAxisIndividual,
    SwCalprmAxis,
    SwCalprmAxisSet,
    SwDataDefProps,
    SwPointerTargetProps,
    CompositeNetworkRepresentation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    TransformationDescription,
    EndToEndTransformationDescription,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


# ==================== SDG (Service Data Group) ====================


class TestSdgParsing:
    def test_getSdg_minimal(self, parser):
        element = _snip(
            "<SD GID='MyGroup'>value1</SD>",
            root_tag="SDG",
        )
        sdg = parser.getSdg(element)
        assert isinstance(sdg, Sdg)

    def test_getSdg_with_caption(self, parser):
        element = _snip(
            "<SDG-CAPTION><SHORT-NAME>Caption1</SHORT-NAME></SDG-CAPTION>",
            root_tag="SDG",
        )
        sdg = parser.getSdg(element)
        assert sdg is not None

    def test_getSdg_with_nested_sdg(self, parser):
        element = _snip(
            "<SDG GID='Inner'><SD>x</SD></SDG>",
            root_tag="SDG",
        )
        sdg = parser.getSdg(element)
        assert sdg is not None

    def test_getSdg_with_sdx_refs(self, parser):
        element = _snip(
            "<SDX-REF DEST='SOMETHING'>/path/to/ref</SDX-REF>",
            root_tag="SDG",
        )
        sdg = parser.getSdg(element)
        assert sdg is not None

    def test_readAdminDataSdgs(self, parser):
        element = _snip(
            "<SDGS>"
            "<SDG GID='A'><SD>x</SD></SDG>"
            "<SDG GID='B'><SD>y</SD></SDG>"
            "</SDGS>"
        )
        admin = AdminData()
        parser.readAdminDataSdgs(element, admin)
        # Verify both SDGs added.
        assert len(admin.getSdgs()) == 2

    def test_readAdminDataSdgs_unsupported_tag_warns(self, caplog):
        import logging
        AUTOSAR.getInstance().new()
        p = ARXMLParser(options={"warning": True})
        element = _snip("<SDGS><UNKNOWN-SDG/></SDGS>")
        admin = AdminData()
        with caplog.at_level(logging.ERROR):
            p.readAdminDataSdgs(element, admin)
        assert any("Unsupported SDG" in r.getMessage() for r in caplog.records)


# ==================== Modification / DocRevision ====================


class TestRevisionParsing:
    def test_readDocRevision_minimal(self, parser):
        element = _snip(
            "<DATE>2024-01-01T00:00:00</DATE>"
            "<ISSUED-BY>alice</ISSUED-BY>"
            "<REVISION-LABEL>1.0.0</REVISION-LABEL>"
            "<STATE>released</STATE>",
            root_tag="DOC-REVISION",
        )
        revision = DocRevision()
        parser.readDocRevision(element, revision)
        assert revision.getIssuedBy().getValue() == "alice"
        assert revision.getState().getValue() == "released"

    def test_readDocRevision_with_modifications(self, parser):
        element = _snip(
            "<MODIFICATIONS>"
            "<MODIFICATION>"
            "<CHANGE><L-4>L-1</L-4></CHANGE>"
            "<REASON><L-4>R-1</L-4></REASON>"
            "</MODIFICATION>"
            "</MODIFICATIONS>",
            root_tag="DOC-REVISION",
        )
        revision = DocRevision()
        parser.readDocRevision(element, revision)
        # modification was added
        assert len(revision.getModifications()) == 1

    def test_readAdminDataDocRevisions(self, parser):
        element = _snip(
            "<DOC-REVISIONS>"
            "<DOC-REVISION>"
            "<ISSUED-BY>bob</ISSUED-BY>"
            "<REVISION-LABEL>2.0.0</REVISION-LABEL>"
            "</DOC-REVISION>"
            "</DOC-REVISIONS>"
        )
        admin = AdminData()
        parser.readAdminDataDocRevisions(element, admin)
        assert len(admin.getDocRevisions()) == 1

    def test_readAdminDataDocRevisions_unsupported_tag_warns(self, caplog):
        import logging
        AUTOSAR.getInstance().new()
        p = ARXMLParser(options={"warning": True})
        element = _snip("<DOC-REVISIONS><UNKNOWN/></DOC-REVISIONS>")
        admin = AdminData()
        with caplog.at_level(logging.ERROR):
            p.readAdminDataDocRevisions(element, admin)
        assert any("Unsupported DocRevision" in r.getMessage() for r in caplog.records)


# ==================== RxIdentifierRange ====================


class TestRxIdentifierRange:
    def test_getChildElementRxIdentifierRange(self, parser):
        # The method does find(element, "RX-IDENTIFIER-RANGE"), so element
        # must be the parent wrapper containing <RX-IDENTIFIER-RANGE>.
        element = _snip(
            "<RX-IDENTIFIER-RANGE>"
            "<LOWER-CAN-ID>0x100</LOWER-CAN-ID>"
            "<UPPER-CAN-ID>0x1FF</UPPER-CAN-ID>"
            "</RX-IDENTIFIER-RANGE>",
            root_tag="PARENT",
        )
        rng = parser.getChildElementRxIdentifierRange(element, "RX-IDENTIFIER-RANGE")
        assert rng is not None
        assert rng.getLowerCanId().getValue() == 256
        assert rng.getUpperCanId().getValue() == 511

    def test_getChildElementRxIdentifierRange_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getChildElementRxIdentifierRange(element, "ABSENT") is None


# ==================== _readVariableAccesses branching ====================


class TestReadVariableAccessesBranches:
    """Exercise each branch of _readVariableAccesses (arxml_parser.py:426)."""

    @pytest.fixture
    def runnable(self):
        return RunnableEntity(parent=None, short_name="R1")

    @pytest.mark.parametrize("key,creator_attr", [
        ("DATA-RECEIVE-POINT-BY-ARGUMENTS", "getDataReceivePointByArguments"),
        ("DATA-RECEIVE-POINT-BY-VALUES", "getDataReceivePointByValues"),
        ("DATA-READ-ACCESSS", "getDataReadAccesses"),
        ("DATA-WRITE-ACCESSS", "getDataWriteAccesses"),
        ("DATA-SEND-POINTS", "getDataSendPoints"),
        ("WRITTEN-LOCAL-VARIABLES", "getWrittenLocalVariables"),
        ("READ-LOCAL-VARIABLES", "getReadLocalVariables"),
    ])
    def test_branch(self, parser, runnable, key, creator_attr):
        element = _snip(
            f"<{key}>"
            f"<VARIABLE-ACCESS>"
            f"<SHORT-NAME>va1</SHORT-NAME>"
            f"</VARIABLE-ACCESS>"
            f"</{key}>",
            root_tag=key,
        )
        parser._readVariableAccesses(element, runnable, key)
        # Each branch creates one variable access on the runnable.
        created = getattr(runnable, creator_attr)()
        assert len(created) == 1, f"{key} did not produce a variable access"

    def test_unsupported_key_warns(self, runnable, caplog):
        import logging
        AUTOSAR.getInstance().new()
        p = ARXMLParser(options={"warning": True})
        # Match the double-wrap pattern from test_branch: outer ROOT contains
        # the <BAD-KEY> parent which itself wraps the VARIABLE-ACCESS.
        element = _snip(
            "<BAD-KEY><VARIABLE-ACCESS><SHORT-NAME>va</SHORT-NAME></VARIABLE-ACCESS></BAD-KEY>",
            root_tag="ROOT",
        )
        with caplog.at_level(logging.ERROR):
            p._readVariableAccesses(element, runnable, "BAD-KEY")
        assert any("Unsupported Variable Access" in r.getMessage() for r in caplog.records)


# ==================== readBswModuleDescriptionImplementedEntryRefs ====================


class TestBswModuleDescriptionImplementedEntryRefs:
    def test_reads_implemented_entry_refs(self, parser):
        bmd = BswModuleDescription(parent=None, short_name="Bmd1")
        element = _snip(
            "<PROVIDED-ENTRYS>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "<BSW-MODULE-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/pkg/Entry1</BSW-MODULE-ENTRY-REF>"
            "</BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "<BSW-MODULE-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/pkg/Entry2</BSW-MODULE-ENTRY-REF>"
            "</BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "</PROVIDED-ENTRYS>",
            root_tag="ROOT",
        )
        parser.readBswModuleDescriptionImplementedEntryRefs(element, bmd)
        assert len(bmd.getImplementedEntryRefs()) == 2

    def test_skips_entries_without_ref(self, parser):
        bmd = BswModuleDescription(parent=None, short_name="Bmd1")
        element = _snip(
            "<PROVIDED-ENTRYS>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL/>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "<BSW-MODULE-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/pkg/Entry</BSW-MODULE-ENTRY-REF>"
            "</BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "</PROVIDED-ENTRYS>",
            root_tag="ROOT",
        )
        parser.readBswModuleDescriptionImplementedEntryRefs(element, bmd)
        # Only one had a ref; the empty conditional should be skipped.
        assert len(bmd.getImplementedEntryRefs()) == 1


# ==================== Documentation Block Handlers ====================


class TestDocumentationBlockHandlers:
    def test_readDocumentationBlock_minimal(self, parser):
        element = _snip(
            "<P><L-1 L='en'>text</L-1></P>",
            root_tag="DOCUMENTATION-BLOCK",
        )
        block = DocumentationBlock()
        parser.readDocumentationBlock(element, block)
        assert len(block.getPs()) == 1

    def test_readDocumentationBlock_with_list(self, parser):
        element = _snip(
            "<LIST TYPE='number'>"
            "<ITEM><P><L-1 L='en'>item1</L-1></P></ITEM>"
            "</LIST>",
            root_tag="DOCUMENTATION-BLOCK",
        )
        block = DocumentationBlock()
        parser.readDocumentationBlock(element, block)
        assert len(block.getLists()) == 1

    def test_readDocumentationBlock_with_figure(self, parser):
        element = _snip(
            "<FIGURE>"
            "<L-GRAPHIC L='en'><GRAPHIC FILENAME='image.png'/></L-GRAPHIC>"
            "</FIGURE>",
            root_tag="DOCUMENTATION-BLOCK",
        )
        block = DocumentationBlock()
        parser.readDocumentationBlock(element, block)
        assert len(block.getFigures()) == 1

    def test_getDocumentationBlock_present(self, parser):
        element = _snip(
            "<MY-BLOCK><P><L-1 L='en'>text</L-1></P></MY-BLOCK>",
        )
        block = parser.getDocumentationBlock(element, "MY-BLOCK")
        assert block is not None
        assert isinstance(block, DocumentationBlock)

    def test_getDocumentationBlock_missing(self, parser):
        element = _snip("<X/>")
        block = parser.getDocumentationBlock(element, "MISSING")
        assert block is None

    def test_getDocumentationBlockList(self, parser):
        element = _snip(
            "<ITEM><P><L-1 L='en'>item1</L-1></P></ITEM>"
            "<ITEM><P><L-1 L='en'>item2</L-1></P></ITEM>",
        )
        blocks = parser.getDocumentationBlockList(element, "ITEM")
        assert len(blocks) == 2
        assert all(isinstance(b, DocumentationBlock) for b in blocks)

    def test_getLParagraphs(self, parser):
        element = _snip(
            "<L-1 L='en'>para1</L-1>"
            "<L-1 L='de'>para2</L-1>",
        )
        paragraphs = parser.getLParagraphs(element, "L-1")
        assert len(paragraphs) == 2

    def test_getMultiLanguageParagraphs(self, parser):
        element = _snip(
            "<P><L-1 L='en'>text1</L-1><L-1 L='de'>text2</L-1></P>",
        )
        paragraphs = parser.getMultiLanguageParagraphs(element, "P")
        assert len(paragraphs) == 1
        assert len(paragraphs[0].getL1s()) == 2

    def test_getLPlainTexts(self, parser):
        element = _snip(
            "<L-10 L='en'>plain1</L-10>"
            "<L-10 L='de'>plain2</L-10>",
        )
        texts = parser.getLPlainTexts(element, "L-10")
        assert len(texts) == 2

    def test_getMultiLanguagePlainText(self, parser):
        element = _snip(
            "<MY-TEXT>"
            "<L-10 L='en'>text1</L-10>"
            "<L-10 L='de'>text2</L-10>"
            "</MY-TEXT>",
        )
        text = parser.getMultiLanguagePlainText(element, "MY-TEXT")
        assert text is not None
        assert len(text.getL10s()) == 2

    def test_getMultiLanguagePlainText_missing(self, parser):
        element = _snip("<X/>")
        text = parser.getMultiLanguagePlainText(element, "MISSING")
        assert text is None

    def test_getListElements(self, parser):
        element = _snip(
            "<LIST TYPE='number'>"
            "<ITEM><P><L-1 L='en'>item</L-1></P></ITEM>"
            "</LIST>",
        )
        lists = parser.getListElements(element, "LIST")
        assert len(lists) == 1


# ==================== Graphic and Figure Handlers ====================


class TestGraphicAndFigureHandlers:
    def test_getGraphic_with_filename(self, parser):
        element = _snip(
            "<MY-GRAPHIC FILENAME='test.png'/>",
        )
        graphic = parser.getGraphic(element, "MY-GRAPHIC")
        assert graphic is not None
        assert graphic.getFilename() == "test.png"

    def test_getGraphic_missing(self, parser):
        element = _snip("<X/>")
        graphic = parser.getGraphic(element, "MISSING")
        assert graphic is None

    def test_getGraphic_without_filename(self, parser):
        element = _snip("<MY-GRAPHIC/>")
        graphic = parser.getGraphic(element, "MY-GRAPHIC")
        assert graphic is not None
        assert graphic.getFilename() is None

    def test_readMlFigure_with_lgraphics(self, parser):
        element = _snip(
            "<L-GRAPHIC L='en'><GRAPHIC FILENAME='fig1.png'/></L-GRAPHIC>"
            "<L-GRAPHIC L='de'><GRAPHIC FILENAME='fig2.png'/></L-GRAPHIC>",
            root_tag="ML-FIGURE",
        )
        figure = MlFigure()
        parser.readMlFigure(element, figure)
        assert len(figure.getLGraphics()) == 2

    def test_readMlFigureLGraphics(self, parser):
        element = _snip(
            "<L-GRAPHIC L='en'><GRAPHIC FILENAME='img.png'/></L-GRAPHIC>"
            "<L-GRAPHIC L='de'><GRAPHIC FILENAME='img2.png'/></L-GRAPHIC>",
            root_tag="FIGURE",
        )
        figure = MlFigure()
        parser.readMlFigureLGraphics(element, figure)
        assert len(figure.getLGraphics()) == 2

    def test_readDocumentViewSelectable(self, parser):
        element = _snip("", root_tag="SELECTABLE")
        selectable = MlFigure()
        parser.readDocumentViewSelectable(element, selectable)

    def test_readPaginateable(self, parser):
        element = _snip("", root_tag="PAGINATE")
        paginateable = MlFigure()
        parser.readPaginateable(element, paginateable)

    def test_getMlFigures(self, parser):
        element = _snip(
            "<FIGURE>"
            "<L-GRAPHIC L='en'><GRAPHIC FILENAME='f1.png'/></L-GRAPHIC>"
            "</FIGURE>"
            "<FIGURE>"
            "<L-GRAPHIC L='de'><GRAPHIC FILENAME='f2.png'/></L-GRAPHIC>"
            "</FIGURE>",
        )
        figures = parser.getMlFigures(element, "FIGURE")
        assert len(figures) == 2
        assert all(isinstance(f, MlFigure) for f in figures)


# ==================== Annotation Handlers ====================


class TestAnnotationHandlers:
    def test_readGeneralAnnotation_minimal(self, parser):
        element = _snip(
            "<ANNOTATION-ORIGIN>manual</ANNOTATION-ORIGIN>",
            root_tag="ANNOTATION",
        )
        annotation = Annotation()
        parser.readGeneralAnnotation(element, annotation)
        assert annotation.getAnnotationOrigin().getValue() == "manual"

    def test_readGeneralAnnotation_with_text(self, parser):
        element = _snip(
            "<ANNOTATION-TEXT>"
            "<P><L-1 L='en'>note</L-1></P>"
            "</ANNOTATION-TEXT>",
            root_tag="ANNOTATION",
        )
        annotation = Annotation()
        parser.readGeneralAnnotation(element, annotation)
        assert annotation.getAnnotationText() is not None

    def test_readGeneralAnnotation_with_label(self, parser):
        element = _snip(
            "<LABEL>"
            "<L-4 L='en'>LabelName</L-4>"
            "</LABEL>",
            root_tag="ANNOTATION",
        )
        annotation = Annotation()
        parser.readGeneralAnnotation(element, annotation)
        assert annotation.getLabel() is not None

    def test_getAnnotations_single(self, parser):
        element = _snip(
            "<ANNOTATIONS>"
            "<ANNOTATION><ANNOTATION-ORIGIN>tool</ANNOTATION-ORIGIN></ANNOTATION>"
            "</ANNOTATIONS>",
        )
        annotations = parser.getAnnotations(element)
        assert len(annotations) == 1
        assert isinstance(annotations[0], Annotation)

    def test_getAnnotations_multiple(self, parser):
        element = _snip(
            "<ANNOTATIONS>"
            "<ANNOTATION><ANNOTATION-ORIGIN>tool1</ANNOTATION-ORIGIN></ANNOTATION>"
            "<ANNOTATION><ANNOTATION-ORIGIN>tool2</ANNOTATION-ORIGIN></ANNOTATION>"
            "</ANNOTATIONS>",
        )
        annotations = parser.getAnnotations(element)
        assert len(annotations) == 2

    def test_getAnnotations_unsupported_tag_warns(self, caplog):
        import logging
        AUTOSAR.getInstance().new()
        p = ARXMLParser(options={"warning": True})
        element = _snip(
            "<ANNOTATIONS><UNKNOWN-ANNOTATION/></ANNOTATIONS>",
        )
        with caplog.at_level(logging.ERROR):
            annotations = p.getAnnotations(element)
        assert len(annotations) == 0
        assert any("Unsupported Annotation" in r.getMessage() for r in caplog.records)


# ==================== SwDataDefProps Handlers ====================


class TestSwDataDefPropsHandlers:
    def test_getSwDataDefProps_minimal(self, parser):
        element = _snip(
            "<SW-DATA-DEF-PROPS>"
            "<SW-DATA-DEF-PROPS-VARIANTS>"
            "<SW-DATA-DEF-PROPS-CONDITIONAL>"
            "<BASE-TYPE-REF DEST='SW-BASE-TYPE'>/types/base</BASE-TYPE-REF>"
            "</SW-DATA-DEF-PROPS-CONDITIONAL>"
            "</SW-DATA-DEF-PROPS-VARIANTS>"
            "</SW-DATA-DEF-PROPS>",
        )
        props = parser.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        assert props is not None
        assert props.getBaseTypeRef() is not None

    def test_getSwDataDefProps_missing(self, parser):
        element = _snip("<X/>")
        props = parser.getSwDataDefProps(element, "MISSING")
        assert props is None

    def test_getSwDataDefProps_with_compu_method(self, parser):
        element = _snip(
            "<SW-DATA-DEF-PROPS>"
            "<SW-DATA-DEF-PROPS-VARIANTS>"
            "<SW-DATA-DEF-PROPS-CONDITIONAL>"
            "<COMPU-METHOD-REF DEST='COMPU-METHOD'>/methods/compu</COMPU-METHOD-REF>"
            "</SW-DATA-DEF-PROPS-CONDITIONAL>"
            "</SW-DATA-DEF-PROPS-VARIANTS>"
            "</SW-DATA-DEF-PROPS>",
        )
        props = parser.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        assert props.getCompuMethodRef() is not None

    def test_getSwDataDefProps_with_annotations(self, parser):
        element = _snip(
            "<SW-DATA-DEF-PROPS>"
            "<SW-DATA-DEF-PROPS-VARIANTS>"
            "<SW-DATA-DEF-PROPS-CONDITIONAL>"
            "<ANNOTATIONS>"
            "<ANNOTATION><ANNOTATION-ORIGIN>tool</ANNOTATION-ORIGIN></ANNOTATION>"
            "</ANNOTATIONS>"
            "</SW-DATA-DEF-PROPS-CONDITIONAL>"
            "</SW-DATA-DEF-PROPS-VARIANTS>"
            "</SW-DATA-DEF-PROPS>",
        )
        props = parser.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        assert len(props.getAnnotations()) == 1

    def test_getSwPointerTargetProps(self, parser):
        element = _snip(
            "<SW-POINTER-TARGET-PROPS>"
            "<TARGET-CATEGORY>variable</TARGET-CATEGORY>"
            "</SW-POINTER-TARGET-PROPS>",
        )
        props = parser.getSwPointerTargetProps(element, "SW-POINTER-TARGET-PROPS")
        assert props is not None
        assert props.getTargetCategory().getValue() == "variable"

    def test_getSwPointerTargetProps_missing(self, parser):
        element = _snip("<X/>")
        props = parser.getSwPointerTargetProps(element, "MISSING")
        assert props is None

    def test_getSwAxisIndividual(self, parser):
        element = _snip(
            "<SW-MAX-AXIS-POINTS>100</SW-MAX-AXIS-POINTS>"
            "<SW-MIN-AXIS-POINTS>2</SW-MIN-AXIS-POINTS>",
            root_tag="SW-AXIS-INDIVIDUAL",
        )
        props = parser.getSwAxisIndividual(element)
        assert props is not None
        assert props.getSwMaxAxisPoints() is not None
        assert props.getSwMinAxisPoints() is not None

    def test_getSwAxisGrouped(self, parser):
        element = _snip(
            "<SHARED-AXIS-TYPE-REF DEST='SW-AXIS-TYPE'>/axis/type</SHARED-AXIS-TYPE-REF>",
            root_tag="SW-AXIS-GROUPED",
        )
        props = parser.getSwAxisGrouped(element)
        assert props is not None
        assert props.getSharedAxisTypeRef() is not None

    def test_getSwCalprmAxis_individual(self, parser):
        element = _snip(
            "<SW-AXIS-INDEX>0</SW-AXIS-INDEX>"
            "<CATEGORY>FIXED</CATEGORY>"
            "<SW-AXIS-INDIVIDUAL>"
            "<SW-MAX-AXIS-POINTS>10</SW-MAX-AXIS-POINTS>"
            "</SW-AXIS-INDIVIDUAL>",
            root_tag="SW-CALPRM-AXIS",
        )
        axis = parser.getSwCalprmAxis(element)
        assert axis is not None
        assert axis.sw_calprm_axis_type_props is not None

    def test_getSwCalprmAxis_grouped(self, parser):
        element = _snip(
            "<SW-AXIS-INDEX>1</SW-AXIS-INDEX>"
            "<CATEGORY>FIXED</CATEGORY>"
            "<SW-AXIS-GROUPED>"
            "<SHARED-AXIS-TYPE-REF DEST='SW-AXIS-TYPE'>/axis/shared</SHARED-AXIS-TYPE-REF>"
            "</SW-AXIS-GROUPED>",
            root_tag="SW-CALPRM-AXIS",
        )
        axis = parser.getSwCalprmAxis(element)
        assert axis is not None
        assert axis.sw_calprm_axis_type_props is not None

    def test_getSwCalprmAxisSet(self, parser):
        element = _snip(
            "<SW-CALPRM-AXIS-SET>"
            "<SW-CALPRM-AXIS>"
            "<SW-AXIS-INDEX>0</SW-AXIS-INDEX>"
            "<CATEGORY>FIXED</CATEGORY>"
            "</SW-CALPRM-AXIS>"
            "<SW-CALPRM-AXIS>"
            "<SW-AXIS-INDEX>1</SW-AXIS-INDEX>"
            "<CATEGORY>FIXED</CATEGORY>"
            "</SW-CALPRM-AXIS>"
            "</SW-CALPRM-AXIS-SET>",
        )
        set_obj = parser.getSwCalprmAxisSet(element, "SW-CALPRM-AXIS-SET")
        assert set_obj is not None
        assert len(set_obj.getSwCalprmAxises()) == 2

    def test_getCompositeNetworkRepresentation(self, parser):
        element = _snip(
            "<LEAF-ELEMENT-IREF>"
            "<ROOT-DATA-PROTOTYPE-REF DEST='DATA-PROTOTYPE'>/root</ROOT-DATA-PROTOTYPE-REF>"
            "<TARGET-DATA-PROTOTYPE-REF DEST='DATA-PROTOTYPE'>/target</TARGET-DATA-PROTOTYPE-REF>"
            "</LEAF-ELEMENT-IREF>",
            root_tag="COMPOSITE-NETWORK-REPRESENTATION",
        )
        rep = parser.getCompositeNetworkRepresentation(element)
        assert rep is not None
        assert rep.getLeafElementIRef() is not None


# ==================== SDG Deep Handlers ====================


class TestSdgDeepHandlers:
    def test_readSd_single(self, parser):
        element = _snip(
            "<SD GID='key1'>value1</SD>",
            root_tag="SDG",
        )
        sdg = Sdg()
        parser.readSd(element, sdg)
        assert len(sdg.getSds()) == 1

    def test_readSd_multiple(self, parser):
        element = _snip(
            "<SD GID='key1'>value1</SD>"
            "<SD GID='key2'>value2</SD>",
            root_tag="SDG",
        )
        sdg = Sdg()
        parser.readSd(element, sdg)
        assert len(sdg.getSds()) == 2

    def test_readSdgCaption(self, parser):
        element = _snip(
            "<SDG-CAPTION><SHORT-NAME>CaptionName</SHORT-NAME></SDG-CAPTION>",
            root_tag="SDG",
        )
        sdg = Sdg()
        parser.readSdgCaption(element, sdg)
        assert sdg.getSdgCaption() is not None

    def test_readSdgSdxRefs(self, parser):
        element = _snip(
            "<SDX-REF DEST='ELEMENT'>/path/ref1</SDX-REF>"
            "<SDX-REF DEST='ELEMENT'>/path/ref2</SDX-REF>",
            root_tag="SDG",
        )
        sdg = Sdg()
        parser.readSdgSdxRefs(element, sdg)
        assert len(sdg.getSdxRefs()) == 2

    def test_getSdg_with_gid(self, parser):
        element = _snip(
            "<SD GID='data'>value</SD>",
            root_tag="SDG",
        )
        element.attrib["GID"] = "MyGroup"
        sdg = parser.getSdg(element)
        assert sdg.getGID() == "MyGroup"

    def test_readAdminDataSdgs_nested_sdg(self, parser):
        element = _snip(
            "<SDGS>"
            "<SDG GID='Parent'>"
            "<SDG GID='Child'><SD>childValue</SD></SDG>"
            "</SDG>"
            "</SDGS>",
        )
        admin = AdminData()
        parser.readAdminDataSdgs(element, admin)
        sdgs = admin.getSdgs()
        assert len(sdgs) == 1
        assert len(sdgs[0].getSdgContentsTypes()) == 1


# ==================== Describable Handlers ====================


class TestDescribableHandlers:
    def test_readDescribable(self, parser):
        element = _snip("", root_tag="DESC")
        desc = EndToEndTransformationDescription()
        parser.readDescribable(element, desc)

    def test_readTransformationDescription(self, parser):
        element = _snip("", root_tag="TRANS-DESC")
        desc = EndToEndTransformationDescription()
        parser.readTransformationDescription(element, desc)

    def test_readEndToEndTransformationDescription(self, parser):
        element = _snip(
            "<DATA-ID-MODE>all16Bit</DATA-ID-MODE>"
            "<MAX-DELTA-COUNTER>15</MAX-DELTA-COUNTER>"
            "<MAX-ERROR-STATE-INIT>5</MAX-ERROR-STATE-INIT>"
            "<PROFILE-NAME>Profile1</PROFILE-NAME>",
            root_tag="E2E-DESC",
        )
        desc = EndToEndTransformationDescription()
        parser.readEndToEndTransformationDescription(element, desc)
        assert desc.getDataIdMode() is not None
        assert desc.getMaxDeltaCounter() is not None
        assert desc.getProfileName() is not None


# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestDocRevisionModificationGap:
    def test_unsupported_modification_tag_warns(self, warning_parser, caplog):
        from armodel.models.M2.MSR.AsamHdo.AdminData import DocRevision
        revision = DocRevision()
        element = _snip(
            "<MODIFICATIONS><UNKNOWN-MOD>"
            "<SHORT-NAME>m</SHORT-NAME>"
            "</UNKNOWN-MOD></MODIFICATIONS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readDocRevisionModifications(element, revision)
        assert any("Unsupported Modification" in r.getMessage()
                   for r in caplog.records)


# ==================== RoleBasedDataTypeAssignment / ServiceDependency (L603-615) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestSwDataDefProsInvalidValue:
    def test_readInvalidValue_sets_value(self, parser):
        from armodel.models import SwDataDefProps
        props = SwDataDefProps()
        element = _snip(
            "<INVALID-VALUE>"
            "<NUMERICAL-VALUE-SPECIFICATION>"
            "<VALUE>42</VALUE>"
            "</NUMERICAL-VALUE-SPECIFICATION>"
            "</INVALID-VALUE>"
        )
        parser.readSwDataDefProsInvalidValue(element, props)
        assert props.getInvalidValue() is not None


# ==================== CompositeNetworkRepresentation (L1943, L2122) ====================

