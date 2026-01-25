"""Test CommonStructureParser methods."""
import pytest
import xml.etree.ElementTree as ET
from armodel.parser.parsers.common_structure_parser import CommonStructureParser
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
    MultilanguageReferrable,
    ARElement
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ImplementationDataType
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import (
    DiagnosticConnection
)
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData, DocRevision, Modification
from armodel.models.M2.MSR.Documentation.Annotation import Annotation, GeneralAnnotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LLongName,
    LOverviewParagraph,
    LParagraph,
    LanguageSpecific
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultilanguageLongName,
    MultiLanguageOverviewParagraph,
    MultiLanguageParagraph,
    MultiLanguagePlainText
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import ARList
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import MlFigure
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg, Sd


# AUTOSAR namespace for testing
AUTOSAR_NS = "http://autosar.org/schema/r4.0"


class TestCommonStructureParser:
    """Test CommonStructureParser."""

    def setup_method(self):
        """Set up parser with namespace map for each test."""
        self.parser = CommonStructureParser()
        self.parser.nsmap = {"xmlns": AUTOSAR_NS}

    def test_read_referrable(self):
        """Test reading Referrable attributes (UUID, timestamp)."""
        xml = f'''
        <ELEMENT xmlns="{AUTOSAR_NS}" UUID="test-uuid" T="2024-01-01T00:00:00">
            <SHORT-NAME>TestName</SHORT-NAME>
        </ELEMENT>
        '''
        element = ET.fromstring(xml)

        # Object is created with short name matching XML
        obj = ImplementationDataType(None, 'TestName')
        self.parser.readReferrable(element, obj)

        # readReferrable reads UUID and timestamp, not short name
        assert obj.getShortName() == 'TestName'
        assert obj.uuid == 'test-uuid'
        assert obj.timestamp == '2024-01-01T00:00:00'

    def test_read_multilanguage_referrable(self):
        """Test reading MultilanguageReferrable attributes."""
        xml = f"""
        <ELEMENT xmlns="{AUTOSAR_NS}">
            <SHORT-NAME>TestName</SHORT-NAME>
            <LONG-NAME>
                <L-4 L="en-US">Test Long Name</L-4>
            </LONG-NAME>
        </ELEMENT>
        """
        element = ET.fromstring(xml)

        obj = ImplementationDataType(None, 'TestName')
        self.parser.readMultilanguageReferrable(element, obj)

        assert obj.getShortName() == 'TestName'
        assert obj.getLongName() is not None

    def test_read_identifiable(self):
        """Test reading Identifiable attributes."""
        xml = f"""
        <ELEMENT xmlns="{AUTOSAR_NS}" UUID="12345" T="2024-01-01T00:00:00">
            <SHORT-NAME>TestName</SHORT-NAME>
            <CATEGORY>CAT1</CATEGORY>
        </ELEMENT>
        """
        element = ET.fromstring(xml)

        obj = ImplementationDataType(None, 'TestName')
        self.parser.readIdentifiable(element, obj)

        assert obj.getShortName() == 'TestName'
        assert obj.uuid == '12345'
        assert obj.timestamp == '2024-01-01T00:00:00'
        assert obj.category.value == 'CAT1'

    def test_read_identifiable_with_desc(self):
        """Test reading Identifiable with DESC."""
        xml = f"""
        <ELEMENT xmlns="{AUTOSAR_NS}">
            <SHORT-NAME>TestName</SHORT-NAME>
            <DESC>
                <L-2 L="en-US">Description</L-2>
            </DESC>
        </ELEMENT>
        """
        element = ET.fromstring(xml)

        obj = ImplementationDataType(None, 'TestName')
        self.parser.readIdentifiable(element, obj)

        assert obj.getShortName() == 'TestName'
        assert obj.desc is not None

    def test_read_ar_element(self):
        """Test reading ARElement attributes."""
        xml = f"""
        <ELEMENT xmlns="{AUTOSAR_NS}">
            <SHORT-NAME>TestElement</SHORT-NAME>
        </ELEMENT>
        """
        element = ET.fromstring(xml)

        obj = DiagnosticConnection(None, 'TestElement')
        self.parser.readARElement(element, obj)

        assert obj.getShortName() == 'TestElement'

    def test_get_admin_data(self):
        """Test getting AdminData."""
        xml = f"""
        <ELEMENT xmlns="{AUTOSAR_NS}">
            <ADMIN-DATA>
                <SHORT-NAME>AdminData</SHORT-NAME>
                <LANGUAGE>en-US</LANGUAGE>
            </ADMIN-DATA>
        </ELEMENT>
        """
        element = ET.fromstring(xml)

        admin_data = self.parser.getAdminData(element, 'ADMIN-DATA')

        assert admin_data is not None
        # language is an ARLiteral object with a value property
        assert admin_data.language.value == 'en-US'

    def test_read_admin_data_sdgs(self):
        """Test reading SDGs in AdminData."""
        xml = f"""
        <ADMIN-DATA xmlns="{AUTOSAR_NS}">
            <SDGS>
                <SDG>
                    <SHORT-NAME>TestSDG</SHORT-NAME>
                </SDG>
            </SDGS>
        </ADMIN-DATA>
        """
        element = ET.fromstring(xml)

        admin_data = AdminData()
        self.parser.readAdminDataSdgs(element, admin_data)

        assert len(admin_data.getSdgs()) > 0

    def test_read_admin_data_doc_revisions(self):
        """Test reading DOC-REVISIONS in AdminData."""
        xml = f"""
        <ADMIN-DATA xmlns="{AUTOSAR_NS}">
            <DOC-REVISIONS>
                <DOC-REVISION>
                    <SHORT-NAME>Rev1</SHORT-NAME>
                    <STATE>DRAFT</STATE>
                </DOC-REVISION>
            </DOC-REVISIONS>
        </ADMIN-DATA>
        """
        element = ET.fromstring(xml)

        admin_data = AdminData()
        self.parser.readAdminDataDocRevisions(element, admin_data)

        assert len(admin_data.getDocRevisions()) > 0

    def test_read_doc_revision(self):
        """Test reading DocRevision."""
        xml = f"""
        <DOC-REVISION xmlns="{AUTOSAR_NS}">
            <SHORT-NAME>Rev1</SHORT-NAME>
            <DATE>2024-01-01T00:00:00</DATE>
            <ISSUED-BY>John Doe</ISSUED-BY>
            <REVISION-LABEL>1.0.0</REVISION-LABEL>
            <STATE>DRAFT</STATE>
        </DOC-REVISION>
        """
        element = ET.fromstring(xml)

        revision = DocRevision()
        self.parser.readDocRevision(element, revision)

        assert revision.date.value == '2024-01-01T00:00:00'
        assert revision.issuedBy.value == 'John Doe'
        assert revision.revisionLabel.value == '1.0.0'
        assert revision.state.value == 'DRAFT'

    def test_read_doc_revision_modifications(self):
        """Test reading modifications in DocRevision."""
        xml = f"""
        <DOC-REVISION xmlns="{AUTOSAR_NS}">
            <MODIFICATIONS>
                <MODIFICATION>
                    <CHANGE>
                        <L-2 L="en-US">Changed</L-2>
                    </CHANGE>
                    <REASON>
                        <L-2 L="en-US">Bug fix</L-2>
                    </REASON>
                </MODIFICATION>
            </MODIFICATIONS>
        </DOC-REVISION>
        """
        element = ET.fromstring(xml)

        revision = DocRevision()
        self.parser.readDocRevisionModifications(element, revision)

        assert len(revision.getModifications()) > 0

    def test_read_modification(self):
        """Test reading Modification."""
        xml = f"""
        <MODIFICATION xmlns="{AUTOSAR_NS}">
            <CHANGE>
                <L-2 L="en-US">Changed</L-2>
            </CHANGE>
            <REASON>
                <L-2 L="en-US">Bug fix</L-2>
            </REASON>
        </MODIFICATION>
        """
        element = ET.fromstring(xml)

        modification = Modification()
        self.parser.readModification(element, modification)

        assert modification.change is not None
        assert modification.reason is not None

    def test_get_multilanguage_long_name(self):
        """Test getting MultilanguageLongName."""
        xml = f"""
        <ELEMENT xmlns="{AUTOSAR_NS}">
            <LONG-NAME>
                <L-4 L="en-US">Test Long Name</L-4>
            </LONG-NAME>
        </ELEMENT>
        """
        element = ET.fromstring(xml)

        long_name = self.parser.getMultilanguageLongName(element, 'LONG-NAME')

        assert long_name is not None
        assert len(long_name.getL4s()) > 0

    def test_read_l_long_name(self):
        """Test reading LLongName elements."""
        xml = f"""
        <LONG-NAME xmlns="{AUTOSAR_NS}">
            <L-4 L="en-US">English Name</L-4>
            <L-4 L="de-DE">German Name</L-4>
        </LONG-NAME>
        """
        element = ET.fromstring(xml)

        long_name = MultilanguageLongName()
        self.parser.readLLongName(element, long_name)

        assert len(long_name.getL4s()) == 2

    def test_get_multilanguage_overview_paragraph(self):
        """Test getting MultiLanguageOverviewParagraph."""
        xml = f"""
        <ELEMENT xmlns="{AUTOSAR_NS}">
            <DESC>
                <L-2 L="en-US">Description</L-2>
            </DESC>
        </ELEMENT>
        """
        element = ET.fromstring(xml)

        paragraph = self.parser.getMultiLanguageOverviewParagraph(
            element, 'DESC'
        )

        assert paragraph is not None
        assert len(paragraph.getL2s()) > 0

    def test_read_l_overview_paragraph(self):
        """Test reading LOverviewParagraph elements."""
        xml = f"""
        <DESC xmlns="{AUTOSAR_NS}">
            <L-2 L="en-US">English Desc</L-2>
            <L-2 L="de-DE">German Desc</L-2>
        </DESC>
        """
        element = ET.fromstring(xml)

        paragraph = MultiLanguageOverviewParagraph()
        self.parser.readLOverviewParagraph(element, paragraph)

        assert len(paragraph.getL2s()) == 2

    def test_read_language_specific(self):
        """Test reading LanguageSpecific."""
        xml = f"""<L-1 xmlns="{AUTOSAR_NS}" L="en-US">Text content</L-1>"""
        element = ET.fromstring(xml)

        # LParagraph is a concrete subclass of LanguageSpecific
        specific = LParagraph()
        self.parser.readLanguageSpecific(element, specific)

        assert specific.value == 'Text content'
        assert specific.getL() == 'en-US'

    def test_get_l_paragraphs(self):
        """Test getting LParagraph list."""
        xml = f"""
        <PARAGRAPHS xmlns="{AUTOSAR_NS}">
            <L-1 L="en-US">Paragraph 1</L-1>
            <L-1 L="de-DE">Paragraph 2</L-1>
        </PARAGRAPHS>
        """
        element = ET.fromstring(xml)

        paragraphs = self.parser.getLParagraphs(element, 'L-1')

        assert len(paragraphs) == 2

    def test_get_multilanguage_paragraphs(self):
        """Test getting MultiLanguageParagraph list."""
        xml = f"""
        <PARAGRAPHS xmlns="{AUTOSAR_NS}">
            <P>
                <L-1 L="en-US">Para 1</L-1>
            </P>
            <P>
                <L-1 L="de-DE">Para 2</L-1>
            </P>
        </PARAGRAPHS>
        """
        element = ET.fromstring(xml)

        paragraphs = self.parser.getMultiLanguageParagraphs(element, 'P')

        assert len(paragraphs) == 2

    def test_get_l_plain_texts(self):
        """Test getting LPlainText list."""
        xml = f"""
        <TEXTS xmlns="{AUTOSAR_NS}">
            <L-10 L="en-US">Text 1</L-10>
            <L-10 L="de-DE">Text 2</L-10>
        </TEXTS>
        """
        element = ET.fromstring(xml)

        texts = self.parser.getLPlainTexts(element, 'L-10')

        assert len(texts) == 2

    def test_get_multilanguage_plain_text(self):
        """Test getting MultiLanguagePlainText."""
        xml = f"""
        <ELEMENT xmlns="{AUTOSAR_NS}">
            <USED-LANGUAGES>
                <L-10 L="en-US">en-US</L-10>
            </USED-LANGUAGES>
        </ELEMENT>
        """
        element = ET.fromstring(xml)

        text = self.parser.getMultiLanguagePlainText(element, 'USED-LANGUAGES')

        assert text is not None
        assert len(text.getL10s()) > 0

    def test_get_list_elements(self):
        """Test getting ARList elements."""
        xml = f"""
        <LISTS xmlns="{AUTOSAR_NS}">
            <LIST TYPE="unordered">
                <ITEM>
                    <P>
                        <L-1 L="en-US">Item 1</L-1>
                    </P>
                </ITEM>
            </LIST>
        </LISTS>
        """
        element = ET.fromstring(xml)

        lists = self.parser.getListElements(element, 'LIST')

        assert len(lists) == 1

    def test_get_graphic(self):
        """Test getting Graphic."""
        xml = f"""
        <FIGURE xmlns="{AUTOSAR_NS}">
            <GRAPHIC FILENAME="image.png"/>
        </FIGURE>
        """
        element = ET.fromstring(xml)

        graphic = self.parser.getGraphic(element, 'GRAPHIC')

        assert graphic is not None
        assert graphic.filename == 'image.png'

    def test_read_ml_figure_l_graphics(self):
        """Test reading LGraphics in MlFigure."""
        xml = f"""
        <FIGURE xmlns="{AUTOSAR_NS}">
            <L-GRAPHIC L="en-US">
                <GRAPHIC FILENAME="image_en.png"/>
            </L-GRAPHIC>
        </FIGURE>
        """
        element = ET.fromstring(xml)

        figure = MlFigure()
        self.parser.readMlFigureLGraphics(element, figure)

        assert len(figure.getLGraphics()) > 0

    def test_read_document_view_selectable(self):
        """Test reading DocumentViewSelectable."""
        # Item is a concrete subclass of DocumentViewSelectable
        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import Item

        xml = f'''<SELECTABLE xmlns="{AUTOSAR_NS}" UUID="test-uuid" T="2024-01-01T00:00:00"/>'''
        element = ET.fromstring(xml)

        selectable = Item()
        self.parser.readDocumentViewSelectable(element, selectable)

        # DocumentViewSelectable reads ARObject attributes (UUID, timestamp)
        assert selectable.uuid == 'test-uuid'
        assert selectable.timestamp == '2024-01-01T00:00:00'

    def test_read_paginateable(self):
        """Test reading Paginateable."""
        # ARList is a concrete subclass of Paginateable
        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import ARList

        xml = f'''<PAGINATEABLE xmlns="{AUTOSAR_NS}" UUID="test-uuid" T="2024-01-01T00:00:00"/>'''
        element = ET.fromstring(xml)

        paginateable = ARList()
        self.parser.readPaginateable(element, paginateable)

        # Paginateable reads DocumentViewSelectable attributes (UUID, timestamp)
        assert paginateable.uuid == 'test-uuid'
        assert paginateable.timestamp == '2024-01-01T00:00:00'

    def test_read_ml_figure(self):
        """Test reading MlFigure."""
        xml = f"""
        <FIGURE xmlns="{AUTOSAR_NS}" UUID="test-uuid" T="2024-01-01T00:00:00">
            <L-GRAPHIC L="en-US">
                <GRAPHIC FILENAME="image.png"/>
            </L-GRAPHIC>
        </FIGURE>
        """
        element = ET.fromstring(xml)

        figure = MlFigure()
        self.parser.readMlFigure(element, figure)

        # MlFigure reads ARObject attributes (UUID, timestamp) and graphics
        assert figure.uuid == 'test-uuid'
        assert figure.timestamp == '2024-01-01T00:00:00'
        assert len(figure.getLGraphics()) > 0

    def test_get_ml_figures(self):
        """Test getting MlFigure list."""
        xml = f"""
        <FIGURES xmlns="{AUTOSAR_NS}">
            <FIGURE>
                <SHORT-NAME>Figure1</SHORT-NAME>
            </FIGURE>
            <FIGURE>
                <SHORT-NAME>Figure2</SHORT-NAME>
            </FIGURE>
        </FIGURES>
        """
        element = ET.fromstring(xml)

        figures = self.parser.getMlFigures(element, 'FIGURE')

        assert len(figures) == 2

    def test_read_documentation_block(self):
        """Test reading DocumentationBlock."""
        xml = f"""
        <DOCUMENTATION xmlns="{AUTOSAR_NS}" UUID="test-uuid" T="2024-01-01T00:00:00">
            <P>
                <L-1 L="en-US">Paragraph</L-1>
            </P>
        </DOCUMENTATION>
        """
        element = ET.fromstring(xml)

        block = DocumentationBlock()
        self.parser.readDocumentationBlock(element, block)

        # DocumentationBlock reads ARObject attributes (UUID, timestamp) and paragraphs
        assert block.uuid == 'test-uuid'
        assert block.timestamp == '2024-01-01T00:00:00'
        assert len(block.getPs()) > 0

    def test_get_documentation_block(self):
        """Test getting DocumentationBlock."""
        xml = f"""
        <ELEMENT xmlns="{AUTOSAR_NS}">
            <INTRODUCTION UUID="test-uuid" T="2024-01-01T00:00:00">
                <P>
                    <L-1 L="en-US">Text</L-1>
                </P>
            </INTRODUCTION>
        </ELEMENT>
        """
        element = ET.fromstring(xml)

        block = self.parser.getDocumentationBlock(element, 'INTRODUCTION')

        assert block is not None
        assert block.uuid == 'test-uuid'

    def test_get_documentation_block_list(self):
        """Test getting DocumentationBlock list."""
        xml = f"""
        <BLOCKS xmlns="{AUTOSAR_NS}">
            <DOCUMENTATION UUID="uuid1" T="2024-01-01T00:00:00">
                <P>
                    <L-1 L="en-US">Doc1</L-1>
                </P>
            </DOCUMENTATION>
            <DOCUMENTATION UUID="uuid2" T="2024-01-01T00:00:00">
                <P>
                    <L-1 L="en-US">Doc2</L-1>
                </P>
            </DOCUMENTATION>
        </BLOCKS>
        """
        element = ET.fromstring(xml)

        blocks = self.parser.getDocumentationBlockList(element, 'DOCUMENTATION')

        assert len(blocks) == 2

    def test_read_general_annotation(self):
        """Test reading GeneralAnnotation."""
        # Annotation is a concrete subclass of GeneralAnnotation
        xml = f"""
        <ANNOTATION xmlns="{AUTOSAR_NS}">
            <SHORT-NAME>Annotation1</SHORT-NAME>
            <ANNOTATION-ORIGIN>Origin</ANNOTATION-ORIGIN>
            <ANNOTATION-TEXT>
                <P>
                    <L-1 L="en-US">Text</L-1>
                </P>
            </ANNOTATION-TEXT>
            <LABEL>
                <L-4 L="en-US">Label</L-4>
            </LABEL>
        </ANNOTATION>
        """
        element = ET.fromstring(xml)

        annotation = Annotation()
        self.parser.readGeneralAnnotation(element, annotation)

        # Attributes use camelCase naming convention
        assert annotation.getAnnotationOrigin().value == 'Origin'
        assert annotation.getAnnotationText() is not None
        assert annotation.getLabel() is not None

    def test_get_annotations(self):
        """Test getting Annotation list."""
        xml = f"""
        <ELEMENT xmlns="{AUTOSAR_NS}">
            <ANNOTATIONS>
                <ANNOTATION>
                    <SHORT-NAME>Annotation1</SHORT-NAME>
                    <ANNOTATION-ORIGIN>Origin</ANNOTATION-ORIGIN>
                </ANNOTATION>
            </ANNOTATIONS>
        </ELEMENT>
        """
        element = ET.fromstring(xml)

        annotations = self.parser.getAnnotations(element)

        assert len(annotations) == 1
        assert annotations[0].getAnnotationOrigin().value == 'Origin'

    def test_get_sdg(self):
        """Test getting Sdg."""
        xml = f"""
        <SDG xmlns="{AUTOSAR_NS}" UUID="test-uuid" T="2024-01-01T00:00:00">
            <SHORT-NAME>TestSDG</SHORT-NAME>
            <SD VALUE="value"/>
        </SDG>
        """
        element = ET.fromstring(xml)

        sdg = self.parser.getSdg(element)

        assert sdg is not None
        # Sdg reads ARObject attributes (UUID, timestamp) and short name
        assert sdg.uuid == 'test-uuid'
        assert sdg.timestamp == '2024-01-01T00:00:00'

    def test_read_sd(self):
        """Test reading Sd in Sdg."""
        xml = f"""
        <SDG xmlns="{AUTOSAR_NS}">
            <SHORT-NAME>TestSDG</SHORT-NAME>
            <SD GID="gid1">value1</SD>
            <SD GID="gid2">value2</SD>
        </SDG>
        """
        element = ET.fromstring(xml)

        sdg = Sdg()
        self.parser.readSd(element, sdg)

        assert len(sdg.getSds()) == 2

    def test_read_sdg_caption(self):
        """Test reading SDG-CAPTION."""
        xml = f"""
        <SDG xmlns="{AUTOSAR_NS}">
            <SHORT-NAME>TestSDG</SHORT-NAME>
            <SDG-CAPTION>
                <SHORT-NAME>CaptionName</SHORT-NAME>
            </SDG-CAPTION>
        </SDG>
        """
        element = ET.fromstring(xml)

        sdg = Sdg()
        self.parser.readSdgCaption(element, sdg)

        assert sdg.getSdgCaption() is not None

    def test_read_sdg_sdx_refs(self):
        """Test reading SDX-REFs."""
        xml = f"""
        <SDG xmlns="{AUTOSAR_NS}">
            <SHORT-NAME>TestSDG</SHORT-NAME>
            <SDX-REF DEST="TYPE">/path/to/ref</SDX-REF>
        </SDG>
        """
        element = ET.fromstring(xml)

        sdg = Sdg()
        self.parser.readSdgSdxRefs(element, sdg)

        assert len(sdg.getSdxRefs()) > 0
