"""
AUTOSAR Package - BlockElements

Package: M2::MSR::Documentation::BlockElements
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    MultilanguageReferrable,
)


class DocumentationBlock(ARObject):
    """
    This class represents a documentation block. It is made of basic text
    structure elements which can be displayed in a table cell.

    Package: M2::MSR::Documentation::BlockElements::DocumentationBlock

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 52, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 983, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 285, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 181, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a definition list in the documentation atpVariation.
        self._defList: Optional["RefType"] = None

    @property
    def def_list(self) -> Optional["RefType"]:
        """Get defList (Pythonic accessor)."""
        return self._defList

    @def_list.setter
    def def_list(self, value: Optional["RefType"]) -> None:
        """
        Set defList with validation.

        Args:
            value: The defList to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defList = None
            return

        self._defList = value
        # This represents a figure in the documentation block.
        # atpVariation.
        self._figure: Optional["MlFigure"] = None

    @property
    def figure(self) -> Optional["MlFigure"]:
        """Get figure (Pythonic accessor)."""
        return self._figure

    @figure.setter
    def figure(self, value: Optional["MlFigure"]) -> None:
        """
        Set figure with validation.

        Args:
            value: The figure to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._figure = None
            return

        if not isinstance(value, MlFigure):
            raise TypeError(
                f"figure must be MlFigure or None, got {type(value).__name__}"
            )
        self._figure = value
        # This is a formula in the definition block.
        # atpVariation.
        self._formula: Optional["MlFormula"] = None

    @property
    def formula(self) -> Optional["MlFormula"]:
        """Get formula (Pythonic accessor)."""
        return self._formula

    @formula.setter
    def formula(self, value: Optional["MlFormula"]) -> None:
        """
        Set formula with validation.

        Args:
            value: The formula to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._formula = None
            return

        if not isinstance(value, MlFormula):
            raise TypeError(
                f"formula must be MlFormula or None, got {type(value).__name__}"
            )
        self._formula = value
        # This represents a labeled list.
        # atpVariation.
        self._labeledListLabel: Optional["RefType"] = None

    @property
    def labeled_list_label(self) -> Optional["RefType"]:
        """Get labeledListLabel (Pythonic accessor)."""
        return self._labeledListLabel

    @labeled_list_label.setter
    def labeled_list_label(self, value: Optional["RefType"]) -> None:
        """
        Set labeledListLabel with validation.

        Args:
            value: The labeledListLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._labeledListLabel = None
            return

        self._labeledListLabel = value
        # This represents numbered or unnumbered list.
        # atpVariation.
        self._list: Optional["RefType"] = None

    @property
    def list(self) -> Optional["RefType"]:
        """Get list (Pythonic accessor)."""
        return self._list

    @list.setter
    def list(self, value: Optional["RefType"]) -> None:
        """
        Set list with validation.

        Args:
            value: The list to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._list = None
            return

        self._list = value
        # This represents automatically contributed contents an msrquery in the context
        # of Documentation 719 Document ID 673:
        # AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template R23-11.
        self._msrQueryP2: Optional["MsrQueryP2"] = None

    @property
    def msr_query_p2(self) -> Optional["MsrQueryP2"]:
        """Get msrQueryP2 (Pythonic accessor)."""
        return self._msrQueryP2

    @msr_query_p2.setter
    def msr_query_p2(self, value: Optional["MsrQueryP2"]) -> None:
        """
        Set msrQueryP2 with validation.

        Args:
            value: The msrQueryP2 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._msrQueryP2 = None
            return

        if not isinstance(value, MsrQueryP2):
            raise TypeError(
                f"msrQueryP2 must be MsrQueryP2 or None, got {type(value).__name__}"
            )
        self._msrQueryP2 = value
        # This represents a note in the text flow.
        # atpVariation.
        self._note: Optional["Note"] = None

    @property
    def note(self) -> Optional["Note"]:
        """Get note (Pythonic accessor)."""
        return self._note

    @note.setter
    def note(self, value: Optional["Note"]) -> None:
        """
        Set note with validation.

        Args:
            value: The note to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._note = None
            return

        if not isinstance(value, Note):
            raise TypeError(
                f"note must be Note or None, got {type(value).__name__}"
            )
        self._note = value
        # This is one particular paragraph.
        # atpSplitable; atpVariation.
        self._p: Optional["MultiLanguage"] = None

    @property
    def p(self) -> Optional["MultiLanguage"]:
        """Get p (Pythonic accessor)."""
        return self._p

    @p.setter
    def p(self, value: Optional["MultiLanguage"]) -> None:
        """
        Set p with validation.

        Args:
            value: The p to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._p = None
            return

        if not isinstance(value, MultiLanguage):
            raise TypeError(
                f"p must be MultiLanguage or None, got {type(value).__name__}"
            )
        self._p = value
        # This aggregation supports structured requirements a documentation block.
        # atpVariation.
        self._structuredReq: Optional["StructuredReq"] = None

    @property
    def structured_req(self) -> Optional["StructuredReq"]:
        """Get structuredReq (Pythonic accessor)."""
        return self._structuredReq

    @structured_req.setter
    def structured_req(self, value: Optional["StructuredReq"]) -> None:
        """
        Set structuredReq with validation.

        Args:
            value: The structuredReq to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._structuredReq = None
            return

        if not isinstance(value, StructuredReq):
            raise TypeError(
                f"structuredReq must be StructuredReq or None, got {type(value).__name__}"
            )
        self._structuredReq = value
        # This represents traceable text in the documentation block.
        # to specify requirements/constraints in any of the trace is specified in the
                # category.
        # atpVariation.
        self._trace: Optional["TraceableText"] = None

    @property
    def trace(self) -> Optional["TraceableText"]:
        """Get trace (Pythonic accessor)."""
        return self._trace

    @trace.setter
    def trace(self, value: Optional["TraceableText"]) -> None:
        """
        Set trace with validation.

        Args:
            value: The trace to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trace = None
            return

        if not isinstance(value, TraceableText):
            raise TypeError(
                f"trace must be TraceableText or None, got {type(value).__name__}"
            )
        self._trace = value
        # This represents one particular verbatim text.
        # atpVariation.
        self._verbatim: Optional["MultiLanguageVerbatim"] = None

    @property
    def verbatim(self) -> Optional["MultiLanguageVerbatim"]:
        """Get verbatim (Pythonic accessor)."""
        return self._verbatim

    @verbatim.setter
    def verbatim(self, value: Optional["MultiLanguageVerbatim"]) -> None:
        """
        Set verbatim with validation.

        Args:
            value: The verbatim to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._verbatim = None
            return

        if not isinstance(value, MultiLanguageVerbatim):
            raise TypeError(
                f"verbatim must be MultiLanguageVerbatim or None, got {type(value).__name__}"
            )
        self._verbatim = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefList(self) -> "RefType":
        """
        AUTOSAR-compliant getter for defList.

        Returns:
            The defList value

        Note:
            Delegates to def_list property (CODING_RULE_V2_00017)
        """
        return self.def_list  # Delegates to property

    def setDefList(self, value: "RefType") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for defList with method chaining.

        Args:
            value: The defList to set

        Returns:
            self for method chaining

        Note:
            Delegates to def_list property setter (gets validation automatically)
        """
        self.def_list = value  # Delegates to property setter
        return self

    def getFigure(self) -> "MlFigure":
        """
        AUTOSAR-compliant getter for figure.

        Returns:
            The figure value

        Note:
            Delegates to figure property (CODING_RULE_V2_00017)
        """
        return self.figure  # Delegates to property

    def setFigure(self, value: "MlFigure") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for figure with method chaining.

        Args:
            value: The figure to set

        Returns:
            self for method chaining

        Note:
            Delegates to figure property setter (gets validation automatically)
        """
        self.figure = value  # Delegates to property setter
        return self

    def getFormula(self) -> "MlFormula":
        """
        AUTOSAR-compliant getter for formula.

        Returns:
            The formula value

        Note:
            Delegates to formula property (CODING_RULE_V2_00017)
        """
        return self.formula  # Delegates to property

    def setFormula(self, value: "MlFormula") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for formula with method chaining.

        Args:
            value: The formula to set

        Returns:
            self for method chaining

        Note:
            Delegates to formula property setter (gets validation automatically)
        """
        self.formula = value  # Delegates to property setter
        return self

    def getLabeledListLabel(self) -> "RefType":
        """
        AUTOSAR-compliant getter for labeledListLabel.

        Returns:
            The labeledListLabel value

        Note:
            Delegates to labeled_list_label property (CODING_RULE_V2_00017)
        """
        return self.labeled_list_label  # Delegates to property

    def setLabeledListLabel(self, value: "RefType") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for labeledListLabel with method chaining.

        Args:
            value: The labeledListLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to labeled_list_label property setter (gets validation automatically)
        """
        self.labeled_list_label = value  # Delegates to property setter
        return self

    def getList(self) -> "RefType":
        """
        AUTOSAR-compliant getter for list.

        Returns:
            The list value

        Note:
            Delegates to list property (CODING_RULE_V2_00017)
        """
        return self.list  # Delegates to property

    def setList(self, value: "RefType") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for list with method chaining.

        Args:
            value: The list to set

        Returns:
            self for method chaining

        Note:
            Delegates to list property setter (gets validation automatically)
        """
        self.list = value  # Delegates to property setter
        return self

    def getMsrQueryP2(self) -> "MsrQueryP2":
        """
        AUTOSAR-compliant getter for msrQueryP2.

        Returns:
            The msrQueryP2 value

        Note:
            Delegates to msr_query_p2 property (CODING_RULE_V2_00017)
        """
        return self.msr_query_p2  # Delegates to property

    def setMsrQueryP2(self, value: "MsrQueryP2") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for msrQueryP2 with method chaining.

        Args:
            value: The msrQueryP2 to set

        Returns:
            self for method chaining

        Note:
            Delegates to msr_query_p2 property setter (gets validation automatically)
        """
        self.msr_query_p2 = value  # Delegates to property setter
        return self

    def getNote(self) -> "Note":
        """
        AUTOSAR-compliant getter for note.

        Returns:
            The note value

        Note:
            Delegates to note property (CODING_RULE_V2_00017)
        """
        return self.note  # Delegates to property

    def setNote(self, value: "Note") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for note with method chaining.

        Args:
            value: The note to set

        Returns:
            self for method chaining

        Note:
            Delegates to note property setter (gets validation automatically)
        """
        self.note = value  # Delegates to property setter
        return self

    def getP(self) -> "MultiLanguage":
        """
        AUTOSAR-compliant getter for p.

        Returns:
            The p value

        Note:
            Delegates to p property (CODING_RULE_V2_00017)
        """
        return self.p  # Delegates to property

    def setP(self, value: "MultiLanguage") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for p with method chaining.

        Args:
            value: The p to set

        Returns:
            self for method chaining

        Note:
            Delegates to p property setter (gets validation automatically)
        """
        self.p = value  # Delegates to property setter
        return self

    def getStructuredReq(self) -> "StructuredReq":
        """
        AUTOSAR-compliant getter for structuredReq.

        Returns:
            The structuredReq value

        Note:
            Delegates to structured_req property (CODING_RULE_V2_00017)
        """
        return self.structured_req  # Delegates to property

    def setStructuredReq(self, value: "StructuredReq") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for structuredReq with method chaining.

        Args:
            value: The structuredReq to set

        Returns:
            self for method chaining

        Note:
            Delegates to structured_req property setter (gets validation automatically)
        """
        self.structured_req = value  # Delegates to property setter
        return self

    def getTrace(self) -> "TraceableText":
        """
        AUTOSAR-compliant getter for trace.

        Returns:
            The trace value

        Note:
            Delegates to trace property (CODING_RULE_V2_00017)
        """
        return self.trace  # Delegates to property

    def setTrace(self, value: "TraceableText") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for trace with method chaining.

        Args:
            value: The trace to set

        Returns:
            self for method chaining

        Note:
            Delegates to trace property setter (gets validation automatically)
        """
        self.trace = value  # Delegates to property setter
        return self

    def getVerbatim(self) -> "MultiLanguageVerbatim":
        """
        AUTOSAR-compliant getter for verbatim.

        Returns:
            The verbatim value

        Note:
            Delegates to verbatim property (CODING_RULE_V2_00017)
        """
        return self.verbatim  # Delegates to property

    def setVerbatim(self, value: "MultiLanguageVerbatim") -> "DocumentationBlock":
        """
        AUTOSAR-compliant setter for verbatim with method chaining.

        Args:
            value: The verbatim to set

        Returns:
            self for method chaining

        Note:
            Delegates to verbatim property setter (gets validation automatically)
        """
        self.verbatim = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_def_list(self, value: Optional[RefType]) -> "DocumentationBlock":
        """
        Set defList and return self for chaining.

        Args:
            value: The defList to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_def_list("value")
        """
        self.def_list = value  # Use property setter (gets validation)
        return self

    def with_figure(self, value: Optional["MlFigure"]) -> "DocumentationBlock":
        """
        Set figure and return self for chaining.

        Args:
            value: The figure to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_figure("value")
        """
        self.figure = value  # Use property setter (gets validation)
        return self

    def with_formula(self, value: Optional["MlFormula"]) -> "DocumentationBlock":
        """
        Set formula and return self for chaining.

        Args:
            value: The formula to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_formula("value")
        """
        self.formula = value  # Use property setter (gets validation)
        return self

    def with_labeled_list_label(self, value: Optional[RefType]) -> "DocumentationBlock":
        """
        Set labeledListLabel and return self for chaining.

        Args:
            value: The labeledListLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_labeled_list_label("value")
        """
        self.labeled_list_label = value  # Use property setter (gets validation)
        return self

    def with_list(self, value: Optional[RefType]) -> "DocumentationBlock":
        """
        Set list and return self for chaining.

        Args:
            value: The list to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_list("value")
        """
        self.list = value  # Use property setter (gets validation)
        return self

    def with_msr_query_p2(self, value: Optional["MsrQueryP2"]) -> "DocumentationBlock":
        """
        Set msrQueryP2 and return self for chaining.

        Args:
            value: The msrQueryP2 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_msr_query_p2("value")
        """
        self.msr_query_p2 = value  # Use property setter (gets validation)
        return self

    def with_note(self, value: Optional["Note"]) -> "DocumentationBlock":
        """
        Set note and return self for chaining.

        Args:
            value: The note to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_note("value")
        """
        self.note = value  # Use property setter (gets validation)
        return self

    def with_p(self, value: Optional["MultiLanguage"]) -> "DocumentationBlock":
        """
        Set p and return self for chaining.

        Args:
            value: The p to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_p("value")
        """
        self.p = value  # Use property setter (gets validation)
        return self

    def with_structured_req(self, value: Optional["StructuredReq"]) -> "DocumentationBlock":
        """
        Set structuredReq and return self for chaining.

        Args:
            value: The structuredReq to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_structured_req("value")
        """
        self.structured_req = value  # Use property setter (gets validation)
        return self

    def with_trace(self, value: Optional["TraceableText"]) -> "DocumentationBlock":
        """
        Set trace and return self for chaining.

        Args:
            value: The trace to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trace("value")
        """
        self.trace = value  # Use property setter (gets validation)
        return self

    def with_verbatim(self, value: Optional["MultiLanguageVerbatim"]) -> "DocumentationBlock":
        """
        Set verbatim and return self for chaining.

        Args:
            value: The verbatim to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_verbatim("value")
        """
        self.verbatim = value  # Use property setter (gets validation)
        return self



class Caption(MultilanguageReferrable):
    """
    This meta-class represents the ability to express a caption which is a
    title, and a shortName.

    Package: M2::MSR::Documentation::BlockElements::Caption

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 432, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a general but brief (one paragraph) what the object in
                # question is about.
        # It is only This property helps a human reader to object in question.
        self._desc: Optional["MultiLanguageOverview"] = None

    @property
    def desc(self) -> Optional["MultiLanguageOverview"]:
        """Get desc (Pythonic accessor)."""
        return self._desc

    @desc.setter
    def desc(self, value: Optional["MultiLanguageOverview"]) -> None:
        """
        Set desc with validation.

        Args:
            value: The desc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._desc = None
            return

        if not isinstance(value, MultiLanguageOverview):
            raise TypeError(
                f"desc must be MultiLanguageOverview or None, got {type(value).__name__}"
            )
        self._desc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDesc(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for desc.

        Returns:
            The desc value

        Note:
            Delegates to desc property (CODING_RULE_V2_00017)
        """
        return self.desc  # Delegates to property

    def setDesc(self, value: "MultiLanguageOverview") -> "Caption":
        """
        AUTOSAR-compliant setter for desc with method chaining.

        Args:
            value: The desc to set

        Returns:
            self for method chaining

        Note:
            Delegates to desc property setter (gets validation automatically)
        """
        self.desc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> "Caption":
        """
        Set desc and return self for chaining.

        Args:
            value: The desc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_desc("value")
        """
        self.desc = value  # Use property setter (gets validation)
        return self


__all__ = [
    "DocumentationBlock",
    "Caption",
]
