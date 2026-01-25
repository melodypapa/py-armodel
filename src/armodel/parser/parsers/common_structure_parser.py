"""
Parser for AUTOSAR CommonStructure elements.

Handles:
- ARObject (base attributes)
- Identifiable (short-name, category, desc)
- AdminData
- Documentation
- ServiceNeeds
"""
from typing import List
import xml.etree.ElementTree as ET

from ...models.M2.MSR.AsamHdo.AdminData import AdminData, DocRevision, Modification
from ...models.M2.MSR.AsamHdo.SpecialData import Sdg, Sd
from ...models.M2.MSR.Documentation.Annotation import Annotation, GeneralAnnotation
from ...models.M2.MSR.Documentation.BlockElements.Figure import (
    Graphic,
    LGraphic,
    MlFigure
)
from ...models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock
)
from ...models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import (
    ARList
)
from ...models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
    DocumentViewSelectable,
    Paginateable
)
from ...models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LLongName,
    LOverviewParagraph,
    LParagraph,
    LanguageSpecific
)
from ...models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultilanguageLongName,
    MultiLanguageOverviewParagraph,
    MultiLanguageParagraph,
    MultiLanguagePlainText
)
from ...models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Referrable,
    MultilanguageReferrable,
    Identifiable,
    ARElement
)

from ..base_arxml_parser import BaseARXMLParser


class CommonStructureParser(BaseARXMLParser):
    """
    Parser for AUTOSAR CommonStructure elements.

    Handles base attributes and common structures shared across all
    AUTOSAR elements including ARObject, Identifiable, and AdminData.
    """

    def __init__(self, options=None):
        """Initialize CommonStructureParser."""
        super().__init__(options)

    # ======================================================================
    # SDG (Special Data) Methods
    # ======================================================================

    def readSd(self, element: ET.Element, sdg: Sdg):
        """Read SD elements into an Sdg."""
        for child_element in self.findall(element, "./SD"):
            sd = Sd()
            self.readARObjectAttributes(child_element, sd)
            if 'GID' in child_element.attrib:
                sd.setGID(child_element.attrib['GID'])
            sd.setValue(child_element.text)
            sdg.addSd(sd)

    def readSdgCaption(self, element: ET.Element, sdg: Sdg):
        """Read SDG-CAPTION into an Sdg."""
        child_element = self.find(element, "SDG-CAPTION")
        if child_element is not None:
            sdg.createSdgCaption(self.getShortName(child_element))

    def readSdgSdxRefs(self, element: ET.Element, sdg: Sdg):
        """Read SDX-REF elements into an Sdg."""
        for ref in self.getChildElementRefTypeList(element, "SDX-REF"):
            sdg.addSdxRef(ref)

    def getSdg(self, element: ET.Element) -> Sdg:
        """Get an Sdg from an element."""
        sdg = Sdg()
        self.readARObjectAttributes(element, sdg)
        if 'GID' in element.attrib:
            sdg.setGID(element.attrib["GID"])
        self.readSdgCaption(element, sdg)
        self.readSd(element, sdg)
        for child_element in self.findall(element, "SDG"):
            sdg.addSdgContentsType(self.getSdg(child_element))
        self.readSdgSdxRefs(element, sdg)
        return sdg

    # ======================================================================
    # AdminData Methods
    # ======================================================================

    def readAdminDataSdgs(self, element: ET.Element, admin_data: AdminData):
        """Read SDGS element into AdminData."""
        for child_element in self.findall(element, "SDGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SDG":
                admin_data.addSdg(self.getSdg(child_element))
            else:
                self.notImplemented("Unsupported SDG <%s>" % tag_name)

    def readModification(self, element: ET.Element,
                        modification: Modification):
        """Read MODIFICATION element."""
        modification.setChange(
            self.getMultiLanguageOverviewParagraph(element, "CHANGE")
        ).setReason(self.getMultiLanguageOverviewParagraph(element, "REASON"))

    def readDocRevisionModifications(self, element: ET.Element,
                                     revision: DocRevision):
        """Read MODIFICATIONS element into DocRevision."""
        for child_element in self.findall(element, "MODIFICATIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODIFICATION":
                modification = Modification()
                self.readModification(child_element, modification)
                revision.addModification(modification)
            else:
                self.notImplemented(
                    "Unsupported Modification <%s>" % tag_name
                )

    def readDocRevision(self, element: ET.Element, revision: DocRevision):
        """Read DOC-REVISION element."""
        revision.setDate(
            self.getChildElementOptionalDataTime(element, "DATE")
        ).setIssuedBy(
            self.getChildElementOptionalLiteral(element, "ISSUED-BY")
        ).setRevisionLabel(
            self.getChildElementOptionalRevisionLabelString(
                element, "REVISION-LABEL"
            )
        ).setState(self.getChildElementOptionalLiteral(element, "STATE"))

        self.readDocRevisionModifications(element, revision)

    def readAdminDataDocRevisions(self, element: ET.Element,
                                   admin_data: AdminData):
        """Read DOC-REVISIONS element into AdminData."""
        for child_element in self.findall(element, "DOC-REVISIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DOC-REVISION":
                revision = DocRevision()
                self.readDocRevision(child_element, revision)
                admin_data.addDocRevision(revision)
            else:
                self.notImplemented(
                    "Unsupported DocRevision <%s>" % tag_name
                )

    def getAdminData(self, element: ET.Element, key: str) -> AdminData:
        """Get AdminData from element."""
        admin_data = None
        child_element = self.find(element, key)
        if child_element is not None:
            admin_data = AdminData()
            self.readARObjectAttributes(child_element, admin_data)
            admin_data.setLanguage(
                self.getChildElementOptionalLiteral(child_element, "LANGUAGE")
            )
            admin_data.setUsedLanguages(
                self.getMultiLanguagePlainText(child_element, "USED-LANGUAGES")
            )

            self.readAdminDataSdgs(child_element, admin_data)
            self.readAdminDataDocRevisions(child_element, admin_data)
        return admin_data

    # ======================================================================
    # Referrable / Identifiable / ARElement Methods
    # ======================================================================

    def readReferrable(self, element: ET.Element, referrable: Referrable):
        """Read Referrable attributes."""
        self.readARObjectAttributes(element, referrable)

    def readMultilanguageReferrable(self, element: ET.Element,
                                    referrable: MultilanguageReferrable):
        """Read MultilanguageReferrable attributes."""
        self.readReferrable(element, referrable)
        referrable.setLongName(
            self.getMultilanguageLongName(element, "LONG-NAME")
        )

    def readIdentifiable(self, element: ET.Element,
                        identifiable: Identifiable):
        """Read Identifiable attributes."""
        self.readMultilanguageReferrable(element, identifiable)

        for annotation in self.getAnnotations(element):
            identifiable.addAnnotation(annotation)

        identifiable.setCategory(
            self.getChildElementOptionalLiteral(element, "CATEGORY")
        ).setDesc(
            self.getMultiLanguageOverviewParagraph(element, "DESC")
        ).setIntroduction(
            self.getDocumentationBlock(element, "INTRODUCTION")
        )

        identifiable.setAdminData(self.getAdminData(element, "ADMIN-DATA"))

    def readARElement(self, element: ET.Element, ar_element: ARElement):
        """Read ARElement attributes."""
        self.readIdentifiable(element, ar_element)

    # ======================================================================
    # Multilingual Text Methods
    # ======================================================================

    def readLLongName(self, element: ET.Element,
                      long_name: MultilanguageLongName):
        """Read L-4 elements into MultilanguageLongName."""
        for child_element in self.findall(element, "L-4"):
            l4 = LLongName()
            self.readARObjectAttributes(child_element, l4)
            l4.value = child_element.text
            if 'L' in child_element.attrib:
                l4.l = child_element.attrib['L']  # noqa: E741
            long_name.addL4(l4)

    def getMultilanguageLongName(self, element: ET.Element,
                                  key: str) -> MultilanguageLongName:
        """Get MultilanguageLongName from element."""
        long_name = None
        child_element = self.find(element, "%s" % key)
        if child_element is not None:
            long_name = MultilanguageLongName()
            self.readARObjectAttributes(child_element, long_name)
            self.readLLongName(child_element, long_name)
        return long_name

    def readLOverviewParagraph(self, element: ET.Element,
                               paragraph: MultiLanguageOverviewParagraph):
        """Read L-2 elements into MultiLanguageOverviewParagraph."""
        for child_element in self.findall(element, "L-2"):
            l2 = LOverviewParagraph()
            self.readARObjectAttributes(child_element, l2)
            l2.value = child_element.text
            if 'L' in child_element.attrib:
                l2.l = child_element.attrib['L']  # noqa: E741
            paragraph.addL2(l2)

    def getMultiLanguageOverviewParagraph(
        self, element: ET.Element, key: str
    ) -> MultiLanguageOverviewParagraph:
        """Get MultiLanguageOverviewParagraph from element."""
        paragraph = None
        child_element = self.find(element, key)
        if child_element is not None:
            paragraph = MultiLanguageOverviewParagraph()
            self.readARObjectAttributes(child_element, paragraph)
            self.readLOverviewParagraph(child_element, paragraph)
        return paragraph

    def readLanguageSpecific(self, element: ET.Element,
                             specific: LanguageSpecific):
        """Read LanguageSpecific attributes."""
        self.readARObjectAttributes(element, specific)
        specific.value = element.text
        if 'L' in element.attrib:
            specific.l = element.attrib['L']  # noqa: E741

    def getLParagraphs(self, element: ET.Element,
                       key: str) -> List[LParagraph]:
        """Get list of LParagraph elements."""
        results = []
        for child_element in self.findall(element, key):
            l1 = LParagraph()
            self.readLanguageSpecific(child_element, l1)
            results.append(l1)
        return results

    def getMultiLanguageParagraphs(
        self, element: ET.Element, key: str
    ) -> List[MultiLanguageParagraph]:
        """Get list of MultiLanguageParagraph elements."""
        paragraphs = []
        for child_element in self.findall(element, key):
            paragraph = MultiLanguageParagraph()
            self.readARObjectAttributes(child_element, paragraph)
            for l1 in self.getLParagraphs(child_element, "L-1"):
                paragraph.addL1(l1)
            paragraphs.append(paragraph)
        return paragraphs

    def getLPlainTexts(self, element: ET.Element,
                       key: str) -> List[LParagraph]:
        """Get list of LPlainText elements."""
        results = []
        for child_element in self.findall(element, key):
            l1 = LParagraph()
            self.readLanguageSpecific(child_element, l1)
            results.append(l1)
        return results

    def getMultiLanguagePlainText(
        self, element: ET.Element, key: str
    ) -> MultiLanguagePlainText:
        """Get MultiLanguagePlainText from element."""
        paragraph = None
        child_element = self.find(element, key)
        if child_element is not None:
            paragraph = MultiLanguagePlainText()
            self.readARObjectAttributes(child_element, paragraph)
            for l10 in self.getLPlainTexts(child_element, "L-10"):
                paragraph.addL10(l10)
        return paragraph

    # ======================================================================
    # Documentation Block Methods
    # ======================================================================

    def getListElements(self, element: ET.Element,
                        key: str) -> List[ARList]:
        """
        Read the DocumentationBlock List.
        """
        result = []
        for child_element in self.findall(element, key):
            list_obj = ARList()
            if 'TYPE' in child_element.attrib:
                list_obj.setType(child_element.attrib['TYPE'])
            for block in self.getDocumentationBlockList(child_element, "ITEM"):
                list_obj.addItem(block)
            result.append(list_obj)
        return result

    def getGraphic(self, element: ET.Element, key: str) -> Graphic:
        """Get Graphic from element."""
        graphic = None
        child_element = self.find(element, key)
        if child_element is not None:
            graphic = Graphic()
            if "FILENAME" in child_element.attrib:
                graphic.setFilename(child_element.attrib["FILENAME"])
        return graphic

    def readMlFigureLGraphics(self, element: ET.Element, figure: MlFigure):
        """Read L-GRAPHIC elements into MlFigure."""
        for child_element in self.findall(element, "L-GRAPHIC"):
            graphic = LGraphic()
            if "L" in child_element.attrib:
                graphic.setL(child_element.attrib["L"])
            graphic.setGraphic(self.getGraphic(child_element, "GRAPHIC"))
            figure.addLGraphics(graphic)

    def readDocumentViewSelectable(self, element: ET.Element,
                                   selectable: DocumentViewSelectable):
        """Read DocumentViewSelectable attributes."""
        self.readARObjectAttributes(element, selectable)

    def readPaginateable(self, element: ET.Element,
                         paginateable: Paginateable):
        """Read Paginateable attributes."""
        self.readDocumentViewSelectable(element, paginateable)

    def readMlFigure(self, element: ET.Element, figure: MlFigure):
        """Read MlFigure element."""
        self.readPaginateable(element, figure)
        self.readMlFigureLGraphics(element, figure)

    def getMlFigures(self, element: ET.Element,
                     key: str) -> List[MlFigure]:
        """Get list of MlFigure elements."""
        result = []
        for child_element in self.findall(element, key):
            figure = MlFigure()
            self.readMlFigure(child_element, figure)
            result.append(figure)
        return result

    def readDocumentationBlock(self, element: ET.Element,
                               block: DocumentationBlock):
        """Read DocumentationBlock element."""
        self.readARObjectAttributes(element, block)
        for paragraph in self.getMultiLanguageParagraphs(element, "P"):
            block.addP(paragraph)
        for list_obj in self.getListElements(element, "LIST"):
            block.addList(list_obj)
        for figure in self.getMlFigures(element, "FIGURE"):
            block.addFigure(figure)

    def getDocumentationBlock(self, element: ET.Element,
                               key: str) -> DocumentationBlock:
        """Get DocumentationBlock from element."""
        block = None
        child_element = self.find(element, key)
        if child_element is not None:
            block = DocumentationBlock()
            self.readDocumentationBlock(child_element, block)
        return block

    def getDocumentationBlockList(
        self, element: ET.Element, key: str
    ) -> List[DocumentationBlock]:
        """Get list of DocumentationBlock elements."""
        blocks = []
        for child_element in self.findall(element, key):
            block = DocumentationBlock()
            self.readDocumentationBlock(child_element, block)
            blocks.append(block)
        return blocks

    # ======================================================================
    # Annotation Methods
    # ======================================================================

    def readGeneralAnnotation(self, element: ET.Element,
                              annotation: GeneralAnnotation):
        """Read GeneralAnnotation element."""
        annotation.setAnnotationOrigin(
            self.getChildElementOptionalLiteral(element, 'ANNOTATION-ORIGIN')
        ).setAnnotationText(
            self.getDocumentationBlock(element, "ANNOTATION-TEXT")
        ).setLabel(
            self.getMultilanguageLongName(element, "LABEL")
        )

    def getAnnotations(self, element: ET.Element) -> List[Annotation]:
        """Get list of Annotation elements."""
        annotations = []
        for child_element in self.findall(element, "ANNOTATIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ANNOTATION":
                annotation = Annotation()
                self.readGeneralAnnotation(child_element, annotation)
                annotations.append(annotation)
            else:
                self.notImplemented(
                    "Unsupported Annotation <%s>" % tag_name
                )
        return annotations
