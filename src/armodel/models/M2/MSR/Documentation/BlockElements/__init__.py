from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    AlignEnum,
    Colspec,
    Entry,
    FloatEnum,
    FrameEnum,
    OrientEnum,
    PgwideEnum,
    Row,
    Table,
    TableSeparatorString,
    Tbody,
    Tgroup,
    ValignEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import MultilanguageReferrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MimeTypeString, UriString
from armodel.models.M2.MSR.Documentation.BlockElements.GerneralParameters import (
    GeneralParameter,
    PrmChar,
    PrmCharAbsTol,
    PrmCharContents,
    PrmCharMinTypMax,
    PrmCharNumericalContents,
    PrmCharNumericalValue,
    PrmCharTextualContents,
    Prms,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


class Caption(MultilanguageReferrable):
    """
    This meta-class represents the ability to express a caption which is a title, and a shortName.
    """

    # Caption method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.18, p.432
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDesc      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDesc      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! This property helps a human reader to identify the object in question. Tags: xml.sequenceOffset=10
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! This property helps a human reader to identify the object in question. Tags: xml.sequenceOffset=10

        Returns:
            The description of the object in question
        """
        return self.desc

    def setDesc(self, value: Optional[MultiLanguageOverviewParagraph]) -> Caption:
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! This property helps a human reader to identify the object in question. Tags: xml.sequenceOffset=10. A None value is a no-op and does not overwrite an existing desc.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.desc = value
        return self


class Url(ARObject):
    """
    This meta-class specifies an Uniform Resource Locator (URL).
    """

    # Url method parity checklist:
    # Spec: AUTOSAR_00052.xsd, complexType URL line 128502 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setMimeType    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMimeType    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValue       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # this denotes the mime type of the resource located by the url.
        self.mimeType: Optional[MimeTypeString] = None

        # The URL value represented by this object.
        self.value: Optional[UriString] = None

    def setMimeType(self, value: Optional[MimeTypeString]) -> Url:
        """
        this denotes the mime type of the resource located by the url. A None value is a no-op and does not overwrite an existing mimeType.
        """
        if value is not None:
            self.mimeType = value
        return self

    def getMimeType(self) -> Optional[MimeTypeString]:
        """
        this denotes the mime type of the resource located by the url.
        """
        return self.mimeType

    def setValue(self, value: Optional[UriString]) -> Url:
        """
        The URL value represented by this object. A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self

    def getValue(self) -> Optional[UriString]:
        """
        The URL value represented by this object.
        """
        return self.value


class DocumentationBlock(ARObject):
    """
    This class represents a documentation block. It is made of basic text structure elements which can be displayed in a table cell.
    """

    # DocumentationBlock method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.1, p.285
    # Spec verified: R23-11 (2026-10-17, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDefList           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefList           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addFigure            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFigures           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getFormula           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFormula           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLabeledList       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLabeledList       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addList              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLists             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getMsrQueryP2        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMsrQueryP2        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNote              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNote              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addP                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createStructuredReq  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStructuredReq     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createTrace          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTrace             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getVerbatim          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVerbatim          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents a definition list in the documentation block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=defList, defList.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=40
        self.defList: Optional[DefList] = None

        # This represents a figure in the documentation block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=figure, figure.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=70
        self.figures: List[MlFigure] = []

        # This is a formula in the definition block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=formula, formula.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=60
        self.formula: Optional[MlFormula] = None

        # This represents a labeled list. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=labeledList, labeledList.variationPoint.short Label vh.latestBindingTime=postBuild xml.sequenceOffset=50
        self.labeledList: Optional[LabeledList] = None

        # This represents numbered or unnumbered list. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=list, list.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=30
        self.lists: List[ARList] = []

        # This represents automatically contributed contents provided by an msrquery in the context of Documentation Block.
        self.msrQueryP2: Optional[MsrQueryP2] = None

        # This represents a note in the text flow. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=note, note.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=80
        self.note: Optional[Note] = None

        # This is one particular paragraph. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=p, p.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=10
        self.ps: List[MultiLanguageParagraph] = []

        # This aggregation supports structured requirements embedded in a documentation block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=structuredReq.shortName, structured Req.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=100
        self.structuredReq: Optional[StructuredReq] = None

        # This represents traceable text in the documentation block. This allows to specify requirements/constraints in any documentation block. The kind of the trace is specified in the category. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=trace.shortName, trace.variationPoint.short Label vh.latestBindingTime=postBuild xml.sequenceOffset=90
        self.trace: Optional[TraceableText] = None

        # This represents one particular verbatim text. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=verbatim, verbatim.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=20
        self.verbatim: Optional[MultiLanguageVerbatim] = None

    def getDefList(self) -> Optional[DefList]:
        """
        This represents a definition list in the documentation block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=defList, defList.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=40

        Returns:
            The definition list in the documentation block
        """
        return self.defList

    def setDefList(self, value: Optional[DefList]) -> DocumentationBlock:
        """
        This represents a definition list in the documentation block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=defList, defList.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=40. A None value is a no-op and does not overwrite an existing defList.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.defList = value
        return self

    def addFigure(self, value: Optional[MlFigure]) -> DocumentationBlock:
        """
        This represents a figure in the documentation block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=figure, figure.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=70. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.figures.append(value)
        return self

    def getFigures(self) -> List[MlFigure]:
        """
        This represents a figure in the documentation block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=figure, figure.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=70

        Returns:
            The figures in the documentation block
        """
        return self.figures

    def getFormula(self) -> Optional[MlFormula]:
        """
        This is a formula in the definition block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=formula, formula.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=60

        Returns:
            The formula in the definition block
        """
        return self.formula

    def setFormula(self, value: Optional[MlFormula]) -> DocumentationBlock:
        """
        This is a formula in the definition block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=formula, formula.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=60. A None value is a no-op and does not overwrite an existing formula.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.formula = value
        return self

    def getLabeledList(self) -> Optional[LabeledList]:
        """
        This represents a labeled list. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=labeledList, labeledList.variationPoint.short Label vh.latestBindingTime=postBuild xml.sequenceOffset=50

        Returns:
            The labeled list
        """
        return self.labeledList

    def setLabeledList(self, value: Optional[LabeledList]) -> DocumentationBlock:
        """
        This represents a labeled list. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=labeledList, labeledList.variationPoint.short Label vh.latestBindingTime=postBuild xml.sequenceOffset=50. A None value is a no-op and does not overwrite an existing labeledList.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.labeledList = value
        return self

    def addList(self, value: Optional[ARList]) -> DocumentationBlock:
        """
        This represents numbered or unnumbered list. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=list, list.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=30. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.lists.append(value)
        return self

    def getLists(self) -> List[ARList]:
        """
        This represents numbered or unnumbered list. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=list, list.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=30

        Returns:
            The lists
        """
        return self.lists

    def getMsrQueryP2(self) -> Optional[MsrQueryP2]:
        """
        This represents automatically contributed contents provided by an msrquery in the context of Documentation Block.

        Returns:
            The automatically contributed contents
        """
        return self.msrQueryP2

    def setMsrQueryP2(self, value: Optional[MsrQueryP2]) -> DocumentationBlock:
        """
        This represents automatically contributed contents provided by an msrquery in the context of Documentation Block. A None value is a no-op and does not overwrite an existing msrQueryP2.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryP2 = value
        return self

    def getNote(self) -> Optional[Note]:
        """
        This represents a note in the text flow. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=note, note.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=80

        Returns:
            The note in the text flow
        """
        return self.note

    def setNote(self, value: Optional[Note]) -> DocumentationBlock:
        """
        This represents a note in the text flow. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=note, note.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=80. A None value is a no-op and does not overwrite an existing note.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.note = value
        return self

    def addP(self, value: Optional[MultiLanguageParagraph]) -> DocumentationBlock:
        """
        This is one particular paragraph. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=p, p.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=10. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ps.append(value)
        return self

    def getPs(self) -> List[MultiLanguageParagraph]:
        """
        This is one particular paragraph. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=p, p.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=10

        Returns:
            The paragraphs
        """
        return self.ps

    def createStructuredReq(self, short_name: str) -> StructuredReq:
        """
        This aggregation supports structured requirements embedded in a documentation block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=structuredReq.shortName, structured Req.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=100

        Args:
            short_name: The short name of the structured requirements

        Returns:
            The created (or existing) structured requirements
        """
        if self.structuredReq is not None and self.structuredReq.getShortName() == short_name:
            return self.structuredReq
        self.structuredReq = StructuredReq(self, short_name)
        return self.structuredReq

    def getStructuredReq(self) -> Optional[StructuredReq]:
        """
        This aggregation supports structured requirements embedded in a documentation block. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=structuredReq.shortName, structured Req.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=100

        Returns:
            The structured requirements
        """
        return self.structuredReq

    def createTrace(self, short_name: str) -> TraceableText:
        """
        This represents traceable text in the documentation block. This allows to specify requirements/constraints in any documentation block. The kind of the trace is specified in the category. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=trace.shortName, trace.variationPoint.short Label vh.latestBindingTime=postBuild xml.sequenceOffset=90

        Args:
            short_name: The short name of the traceable text in the documentation block

        Returns:
            The created (or existing) traceable text in the documentation block
        """
        if self.trace is not None and self.trace.getShortName() == short_name:
            return self.trace
        self.trace = TraceableText(self, short_name)
        return self.trace

    def getTrace(self) -> Optional[TraceableText]:
        """
        This represents traceable text in the documentation block. This allows to specify requirements/constraints in any documentation block. The kind of the trace is specified in the category. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=trace.shortName, trace.variationPoint.short Label vh.latestBindingTime=postBuild xml.sequenceOffset=90

        Returns:
            The traceable text in the documentation block
        """
        return self.trace

    def getVerbatim(self) -> Optional[MultiLanguageVerbatim]:
        """
        This represents one particular verbatim text. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=verbatim, verbatim.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=20

        Returns:
            The verbatim text
        """
        return self.verbatim

    def setVerbatim(self, value: Optional[MultiLanguageVerbatim]) -> DocumentationBlock:
        """
        This represents one particular verbatim text. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=verbatim, verbatim.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=20. A None value is a no-op and does not overwrite an existing verbatim.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.verbatim = value
        return self


# These imports stay at the bottom: Figure/Formula/Note import Caption from this
# package __init__, and ListElements imports DocumentationBlock from it, so every
# referenced name is bound here only after the classes above are defined.
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import MlFigure as MlFigure  # noqa: E402
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import MlFormula as MlFormula  # noqa: E402
from armodel.models.M2.MSR.Documentation.BlockElements.Note import Note as Note  # noqa: E402
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import StructuredReq as StructuredReq  # noqa: E402
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import TraceableText as TraceableText  # noqa: E402
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryP2 as MsrQueryP2  # noqa: E402
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph as MultiLanguageParagraph  # noqa: E402
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageVerbatim as MultiLanguageVerbatim  # noqa: E402
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import ARList as ARList  # noqa: E402
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import DefList as DefList  # noqa: E402
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import LabeledList as LabeledList  # noqa: E402


__all__ = [
    "AlignEnum",
    "Colspec",
    "Entry",
    "FloatEnum",
    "FrameEnum",
    "OrientEnum",
    "PgwideEnum",
    "Row",
    "Table",
    "TableSeparatorString",
    "Tbody",
    "Tgroup",
    "ValignEnum",
    "Caption",
    "Url",
    "DocumentationBlock",
    "GeneralParameter",
    "PrmChar",
    "PrmCharAbsTol",
    "PrmCharContents",
    "PrmCharMinTypMax",
    "PrmCharNumericalContents",
    "PrmCharNumericalValue",
    "PrmCharTextualContents",
    "Prms",
]
