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


class TestCommonStructureParser:
    """Test CommonStructureParser."""

    def test_read_referrable(self):
        """Test reading Referrable attributes."""
        xml = """
        <ELEMENT>
            <SHORT-NAME>TestName</SHORT-NAME>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        obj = Identifiable('Dummy')
        parser.readReferrable(element, obj)

        assert obj.getShortName() == 'TestName'

    def test_read_multilanguage_referrable(self):
        """Test reading MultilanguageReferrable attributes."""
        xml = """
        <ELEMENT>
            <SHORT-NAME>TestName</SHORT-NAME>
            <LONG-NAME>
                <L-4 L="en-US">Test Long Name</L-4>
            </LONG-NAME>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        obj = MultilanguageReferrable('Dummy')
        parser.readMultilanguageReferrable(element, obj)

        assert obj.getShortName() == 'TestName'
        assert obj.getLongName() is not None

    def test_read_identifiable(self):
        """Test reading Identifiable attributes."""
        xml = """
        <ELEMENT UUID="12345" T="2024-01-01T00:00:00">
            <SHORT-NAME>TestName</SHORT-NAME>
            <CATEGORY>CAT1</CATEGORY>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        obj = Identifiable('Dummy')
        parser.readIdentifiable(element, obj)

        assert obj.getShortName() == 'TestName'
        assert obj.uuid == '12345'
        assert obj.timestamp == '2024-01-01T00:00:00'
        assert obj.category == 'CAT1'

    def test_read_identifiable_with_desc(self):
        """Test reading Identifiable with DESC."""
        xml = """
        <ELEMENT>
            <SHORT-NAME>TestName</SHORT-NAME>
            <DESC>
                <L-2 L="en-US">Description</L-2>
            </DESC>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        obj = Identifiable('Dummy')
        parser.readIdentifiable(element, obj)

        assert obj.getShortName() == 'TestName'
        assert obj.desc is not None

    def test_read_ar_element(self):
        """Test reading ARElement attributes."""
        xml = """
        <ELEMENT>
            <SHORT-NAME>TestElement</SHORT-NAME>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        obj = ARElement('Dummy')
        parser.readARElement(element, obj)

        assert obj.getShortName() == 'TestElement'

    def test_get_admin_data(self):
        """Test getting AdminData."""
        xml = """
        <ELEMENT>
            <ADMIN-DATA>
                <SHORT-NAME>AdminData</SHORT-NAME>
                <LANGUAGE>en-US</LANGUAGE>
            </ADMIN-DATA>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        admin_data = parser.getAdminData(element, 'ADMIN-DATA')

        assert admin_data is not None
        assert admin_data.language == 'en-US'

    def test_read_admin_data_sdgs(self):
        """Test reading SDGs in AdminData."""
        xml = """
        <ADMIN-DATA>
            <SDGS>
                <SDG>
                    <SHORT-NAME>TestSDG</SHORT-NAME>
                </SDG>
            </SDGS>
        </ADMIN-DATA>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        admin_data = AdminData()
        parser.readAdminDataSdgs(element, admin_data)

        assert len(admin_data.sdgs) > 0

    def test_read_admin_data_doc_revisions(self):
        """Test reading DOC-REVISIONS in AdminData."""
        xml = """
        <ADMIN-DATA>
            <DOC-REVISIONS>
                <DOC-REVISION>
                    <SHORT-NAME>Rev1</SHORT-NAME>
                    <STATE>DRAFT</STATE>
                </DOC-REVISION>
            </DOC-REVISIONS>
        </ADMIN-DATA>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        admin_data = AdminData()
        parser.readAdminDataDocRevisions(element, admin_data)

        assert len(admin_data.doc_revisions) > 0

    def test_read_doc_revision(self):
        """Test reading DocRevision."""
        xml = """
        <DOC-REVISION>
            <SHORT-NAME>Rev1</SHORT-NAME>
            <DATE>2024-01-01T00:00:00</DATE>
            <ISSUED-BY>John Doe</ISSUED-BY>
            <REVISION-LABEL>v1.0</REVISION-LABEL>
            <STATE>DRAFT</STATE>
        </DOC-REVISION>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        revision = DocRevision()
        parser.readDocRevision(element, revision)

        assert revision.date == '2024-01-01T00:00:00'
        assert revision.issued_by == 'John Doe'
        assert revision.revision_label == 'v1.0'
        assert revision.state == 'DRAFT'

    def test_read_doc_revision_modifications(self):
        """Test reading modifications in DocRevision."""
        xml = """
        <DOC-REVISION>
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
        parser = CommonStructureParser()

        revision = DocRevision()
        parser.readDocRevisionModifications(element, revision)

        assert len(revision.modifications) > 0

    def test_read_modification(self):
        """Test reading Modification."""
        xml = """
        <MODIFICATION>
            <CHANGE>
                <L-2 L="en-US">Changed</L-2>
            </CHANGE>
            <REASON>
                <L-2 L="en-US">Bug fix</L-2>
            </REASON>
        </MODIFICATION>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        modification = Modification()
        parser.readModification(element, modification)

        assert modification.change is not None
        assert modification.reason is not None

    def test_get_multilanguage_long_name(self):
        """Test getting MultilanguageLongName."""
        xml = """
        <ELEMENT>
            <LONG-NAME>
                <L-4 L="en-US">Test Long Name</L-4>
            </LONG-NAME>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        long_name = parser.getMultilanguageLongName(element, 'LONG-NAME')

        assert long_name is not None
        assert len(long_name.l4s) > 0

    def test_read_l_long_name(self):
        """Test reading LLongName elements."""
        xml = """
        <LONG-NAME>
            <L-4 L="en-US">English Name</L-4>
            <L-4 L="de-DE">German Name</L-4>
        </LONG-NAME>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        long_name = MultilanguageLongName()
        parser.readLLongName(element, long_name)

        assert len(long_name.l4s) == 2

    def test_get_multilanguage_overview_paragraph(self):
        """Test getting MultiLanguageOverviewParagraph."""
        xml = """
        <ELEMENT>
            <DESC>
                <L-2 L="en-US">Description</L-2>
            </DESC>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        paragraph = parser.getMultiLanguageOverviewParagraph(
            element, 'DESC'
        )

        assert paragraph is not None
        assert len(paragraph.l2s) > 0

    def test_read_l_overview_paragraph(self):
        """Test reading LOverviewParagraph elements."""
        xml = """
        <DESC>
            <L-2 L="en-US">English Desc</L-2>
            <L-2 L="de-DE">German Desc</L-2>
        </DESC>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        paragraph = MultiLanguageOverviewParagraph()
        parser.readLOverviewParagraph(element, paragraph)

        assert len(paragraph.l2s) == 2

    def test_read_language_specific(self):
        """Test reading LanguageSpecific."""
        xml = """<L-1 L="en-US">Text content</L-1>"""
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        specific = LanguageSpecific()
        parser.readLanguageSpecific(element, specific)

        assert specific.value == 'Text content'
        assert specific.l == 'en-US'

    def test_get_l_paragraphs(self):
        """Test getting LParagraph list."""
        xml = """
        <PARAGRAPHS>
            <L-1 L="en-US">Paragraph 1</L-1>
            <L-1 L="de-DE">Paragraph 2</L-1>
        </PARAGRAPHS>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        paragraphs = parser.getLParagraphs(element, 'L-1')

        assert len(paragraphs) == 2

    def test_get_multilanguage_paragraphs(self):
        """Test getting MultiLanguageParagraph list."""
        xml = """
        <PARAGRAPHS>
            <P>
                <L-1 L="en-US">Para 1</L-1>
            </P>
            <P>
                <L-1 L="de-DE">Para 2</L-1>
            </P>
        </PARAGRAPHS>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        paragraphs = parser.getMultiLanguageParagraphs(element, 'P')

        assert len(paragraphs) == 2

    def test_get_l_plain_texts(self):
        """Test getting LPlainText list."""
        xml = """
        <TEXTS>
            <L-10 L="en-US">Text 1</L-10>
            <L-10 L="de-DE">Text 2</L-10>
        </TEXTS>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        texts = parser.getLPlainTexts(element, 'L-10')

        assert len(texts) == 2

    def test_get_multilanguage_plain_text(self):
        """Test getting MultiLanguagePlainText."""
        xml = """
        <ELEMENT>
            <USED-LANGUAGES>
                <L-10 L="en-US">en-US</L-10>
            </USED-LANGUAGES>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        text = parser.getMultiLanguagePlainText(element, 'USED-LANGUAGES')

        assert text is not None
        assert len(text.l10s) > 0

    def test_get_list_elements(self):
        """Test getting ARList elements."""
        xml = """
        <LISTS>
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
        parser = CommonStructureParser()

        lists = parser.getListElements(element, 'LIST')

        assert len(lists) == 1

    def test_get_graphic(self):
        """Test getting Graphic."""
        xml = """
        <FIGURE>
            <GRAPHIC FILENAME="image.png"/>
        </FIGURE>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        graphic = parser.getGraphic(element, 'GRAPHIC')

        assert graphic is not None
        assert graphic.filename == 'image.png'

    def test_read_ml_figure_l_graphics(self):
        """Test reading LGraphics in MlFigure."""
        xml = """
        <FIGURE>
            <L-GRAPHIC L="en-US">
                <GRAPHIC FILENAME="image_en.png"/>
            </L-GRAPHIC>
        </FIGURE>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        figure = MlFigure()
        parser.readMlFigureLGraphics(element, figure)

        assert len(figure.l_graphics) > 0

    def test_read_document_view_selectable(self):
        """Test reading DocumentViewSelectable."""
        xml = """<SELECTABLE><SHORT-NAME>Test</SHORT-NAME></SELECTABLE>"""
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
            DocumentViewSelectable
        )
        selectable = DocumentViewSelectable()
        parser.readDocumentViewSelectable(element, selectable)

        assert selectable.getShortName() == 'Test'

    def test_read_paginateable(self):
        """Test reading Paginateable."""
        xml = """<PAGINATEABLE><SHORT-NAME>Test</SHORT-NAME></PAGINATEABLE>"""
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
            Paginateable
        )
        paginateable = Paginateable()
        parser.readPaginateable(element, paginateable)

        assert paginateable.getShortName() == 'Test'

    def test_read_ml_figure(self):
        """Test reading MlFigure."""
        xml = """
        <FIGURE>
            <SHORT-NAME>Figure1</SHORT-NAME>
            <L-GRAPHIC L="en-US">
                <GRAPHIC FILENAME="image.png"/>
            </L-GRAPHIC>
        </FIGURE>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        figure = MlFigure()
        parser.readMlFigure(element, figure)

        assert figure.getShortName() == 'Figure1'

    def test_get_ml_figures(self):
        """Test getting MlFigure list."""
        xml = """
        <FIGURES>
            <FIGURE>
                <SHORT-NAME>Figure1</SHORT-NAME>
            </FIGURE>
            <FIGURE>
                <SHORT-NAME>Figure2</SHORT-NAME>
            </FIGURE>
        </FIGURES>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        figures = parser.getMlFigures(element, 'FIGURE')

        assert len(figures) == 2

    def test_read_documentation_block(self):
        """Test reading DocumentationBlock."""
        xml = """
        <DOCUMENTATION>
            <SHORT-NAME>Doc1</SHORT-NAME>
            <P>
                <L-1 L="en-US">Paragraph</L-1>
            </P>
        </DOCUMENTATION>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        block = DocumentationBlock()
        parser.readDocumentationBlock(element, block)

        assert block.getShortName() == 'Doc1'
        assert len(block.ps) > 0

    def test_get_documentation_block(self):
        """Test getting DocumentationBlock."""
        xml = """
        <ELEMENT>
            <INTRODUCTION>
                <SHORT-NAME>Intro</SHORT-NAME>
                <P>
                    <L-1 L="en-US">Text</L-1>
                </P>
            </INTRODUCTION>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        block = parser.getDocumentationBlock(element, 'INTRODUCTION')

        assert block is not None
        assert block.getShortName() == 'Intro'

    def test_get_documentation_block_list(self):
        """Test getting DocumentationBlock list."""
        xml = """
        <BLOCKS>
            <DOCUMENTATION>
                <SHORT-NAME>Doc1</SHORT-NAME>
            </DOCUMENTATION>
            <DOCUMENTATION>
                <SHORT-NAME>Doc2</SHORT-NAME>
            </DOCUMENTATION>
        </BLOCKS>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        blocks = parser.getDocumentationBlockList(element, 'DOCUMENTATION')

        assert len(blocks) == 2

    def test_read_general_annotation(self):
        """Test reading GeneralAnnotation."""
        xml = """
        <ANNOTATION>
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
        parser = CommonStructureParser()

        annotation = GeneralAnnotation()
        parser.readGeneralAnnotation(element, annotation)

        assert annotation.annotation_origin == 'Origin'
        assert annotation.annotation_text is not None
        assert annotation.label is not None

    def test_get_annotations(self):
        """Test getting Annotation list."""
        xml = """
        <ELEMENT>
            <ANNOTATIONS>
                <ANNOTATION>
                    <SHORT-NAME>Annotation1</SHORT-NAME>
                    <ANNOTATION-ORIGIN>Origin</ANNOTATION-ORIGIN>
                </ANNOTATION>
            </ANNOTATIONS>
        </ELEMENT>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        annotations = parser.getAnnotations(element)

        assert len(annotations) == 1
        assert annotations[0].annotation_origin == 'Origin'

    def test_get_sdg(self):
        """Test getting Sdg."""
        xml = """
        <SDG>
            <SHORT-NAME>TestSDG</SHORT-NAME>
            <SDG-CAPTION>Caption</SDG-CAPTION>
            <SD VALUE="value"/>
        </SDG>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        sdg = parser.getSdg(element)

        assert sdg is not None
        assert sdg.getShortName() == 'TestSDG'

    def test_read_sd(self):
        """Test reading Sd in Sdg."""
        xml = """
        <SDG>
            <SHORT-NAME>TestSDG</SHORT-NAME>
            <SD GID="gid1">value1</SD>
            <SD GID="gid2">value2</SD>
        </SDG>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        sdg = Sdg()
        parser.readSd(element, sdg)

        assert len(sdg.sds) == 2

    def test_read_sdg_caption(self):
        """Test reading SDG-CAPTION."""
        xml = """
        <SDG>
            <SHORT-NAME>TestSDG</SHORT-NAME>
            <SDG-CAPTION>Caption</SDG-CAPTION>
        </SDG>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        sdg = Sdg()
        parser.readSdgCaption(element, sdg)

        assert sdg.sdg_caption is not None

    def test_read_sdg_sdx_refs(self):
        """Test reading SDX-REFs."""
        xml = """
        <SDG>
            <SHORT-NAME>TestSDG</SHORT-NAME>
            <SDX-REF DEST="TYPE">/path/to/ref</SDX-REF>
        </SDG>
        """
        element = ET.fromstring(xml)
        parser = CommonStructureParser()

        sdg = Sdg()
        parser.readSdgSdxRefs(element, sdg)

        assert len(sdg.sdx_refs) > 0
