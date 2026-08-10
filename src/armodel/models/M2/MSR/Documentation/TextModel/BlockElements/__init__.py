from __future__ import annotations

from typing import List, Optional

from armodel.models.M2.MSR.Documentation.BlockElements.Figure import MlFigure as MlFigure
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import MlFormula as MlFormula
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import ARList as ARList
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import DefList as DefList
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import LabeledList as LabeledList
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.Note import Note as Note
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.RequirementsTracing import StructuredReq as StructuredReq
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.RequirementsTracing import TraceableText as TraceableText
from armodel.models.M2.MSR.Documentation.TextModel.MsrQuery import MsrQueryP2 as MsrQueryP2
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageVerbatim as MultiLanguageVerbatim
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class DocumentationBlock(ARObject):
    """
    This class represents a documentation block. It is made of basic text structure elements which can be displayed in a table cell.
    """

    # DocumentationBlock method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.1, p.285
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDefList           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefList           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addFigure            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFigures           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getFormula           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFormula           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLabeledList       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLabeledList       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addList              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLists             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getMsrQueryP2        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMsrQueryP2        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNote              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNote              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addP                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getStructuredReq     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setStructuredReq     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTrace             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTrace             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVerbatim          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVerbatim          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents a definition list in the documentation block.
        self.defList: Optional[DefList] = None

        # This represents a figure in the documentation block.
        self.figures: List[MlFigure] = []

        # This is a formula in the definition block.
        self.formula: Optional[MlFormula] = None

        # This represents a labeled list.
        self.labeledList: Optional[LabeledList] = None

        # This represents numbered or unnumbered list.
        self.lists: List[ARList] = []

        # This represents automatically contributed contents provided by an msrquery in the context of Documentation Block.
        self.msrQueryP2: Optional[MsrQueryP2] = None

        # This represents a note in the text flow.
        self.note: Optional[Note] = None

        # This is one particular paragraph.
        self.ps: List[MultiLanguageParagraph] = []

        # This aggregation supports structured requirements embedded in a documentation block.
        self.structuredReq: Optional[StructuredReq] = None

        # This represents traceable text in the documentation block. This allows to specify requirements/constraints in any documentation block. The kind of the trace is specified in the category.
        self.trace: Optional[TraceableText] = None

        # This represents one particular verbatim text.
        self.verbatim: Optional[MultiLanguageVerbatim] = None

    def getDefList(self) -> Optional[DefList]:
        """
        This represents a definition list in the documentation block.

        Returns:
            The definition list in the documentation block
        """
        return self.defList

    def setDefList(self, value: Optional[DefList]) -> "DocumentationBlock":
        """
        This represents a definition list in the documentation block. A None value is a no-op and does not overwrite an existing defList.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.defList = value
        return self

    def addFigure(self, value: Optional[MlFigure]) -> "DocumentationBlock":
        """
        This represents a figure in the documentation block. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.figures.append(value)
        return self

    def getFigures(self) -> List[MlFigure]:
        """
        This represents a figure in the documentation block.

        Returns:
            The figures in the documentation block
        """
        return self.figures

    def getFormula(self) -> Optional[MlFormula]:
        """
        This is a formula in the definition block.

        Returns:
            The formula in the definition block
        """
        return self.formula

    def setFormula(self, value: Optional[MlFormula]) -> "DocumentationBlock":
        """
        This is a formula in the definition block. A None value is a no-op and does not overwrite an existing formula.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.formula = value
        return self

    def getLabeledList(self) -> Optional[LabeledList]:
        """
        This represents a labeled list.

        Returns:
            The labeled list
        """
        return self.labeledList

    def setLabeledList(self, value: Optional[LabeledList]) -> "DocumentationBlock":
        """
        This represents a labeled list. A None value is a no-op and does not overwrite an existing labeledList.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.labeledList = value
        return self

    def addList(self, value: Optional[ARList]) -> "DocumentationBlock":
        """
        This represents numbered or unnumbered list. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.lists.append(value)
        return self

    def getLists(self) -> List[ARList]:
        """
        This represents numbered or unnumbered list.

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

    def setMsrQueryP2(self, value: Optional[MsrQueryP2]) -> "DocumentationBlock":
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
        This represents a note in the text flow.

        Returns:
            The note in the text flow
        """
        return self.note

    def setNote(self, value: Optional[Note]) -> "DocumentationBlock":
        """
        This represents a note in the text flow. A None value is a no-op and does not overwrite an existing note.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.note = value
        return self

    def addP(self, value: Optional[MultiLanguageParagraph]) -> "DocumentationBlock":
        """
        This is one particular paragraph. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ps.append(value)
        return self

    def getPs(self) -> List[MultiLanguageParagraph]:
        """
        This is one particular paragraph.

        Returns:
            The paragraphs
        """
        return self.ps

    def getStructuredReq(self) -> Optional[StructuredReq]:
        """
        This aggregation supports structured requirements embedded in a documentation block.

        Returns:
            The structured requirements
        """
        return self.structuredReq

    def setStructuredReq(self, value: Optional[StructuredReq]) -> "DocumentationBlock":
        """
        This aggregation supports structured requirements embedded in a documentation block. A None value is a no-op and does not overwrite an existing structuredReq.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.structuredReq = value
        return self

    def getTrace(self) -> Optional[TraceableText]:
        """
        This represents traceable text in the documentation block. This allows to specify requirements/constraints in any documentation block. The kind of the trace is specified in the category.

        Returns:
            The traceable text in the documentation block
        """
        return self.trace

    def setTrace(self, value: Optional[TraceableText]) -> "DocumentationBlock":
        """
        This represents traceable text in the documentation block. This allows to specify requirements/constraints in any documentation block. The kind of the trace is specified in the category. A None value is a no-op and does not overwrite an existing trace.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.trace = value
        return self

    def getVerbatim(self) -> Optional[MultiLanguageVerbatim]:
        """
        This represents one particular verbatim text.

        Returns:
            The verbatim text
        """
        return self.verbatim

    def setVerbatim(self, value: Optional[MultiLanguageVerbatim]) -> "DocumentationBlock":
        """
        This represents one particular verbatim text. A None value is a no-op and does not overwrite an existing verbatim.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.verbatim = value
        return self
