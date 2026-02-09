from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class MixedContentForOverviewParagraph(ARObject, ABC):
    """
    This is the text model of a restricted paragraph item within a
    documentation. Such restricted paragraphs are used mainly for overview
    items, e.g. desc.

    Package: M2::MSR::Documentation::TextModel::InlineTextModel

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 289, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is MixedContentForOverviewParagraph:
            raise TypeError("MixedContentForOverviewParagraph is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element is the same as function here as in a HTML it forces a line
        # break.
        self._br: "Br" = None

    @property
    def br(self) -> "Br":
        """Get br (Pythonic accessor)."""
        return self._br

    @br.setter
    def br(self, value: "Br") -> None:
        """
        Set br with validation.

        Args:
            value: The br to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Br):
            raise TypeError(
                f"br must be Br, got {type(value).__name__}"
            )
        self._br = value
        self._e: "EmphasisText" = None

    @property
    def e(self) -> "EmphasisText":
        """Get e (Pythonic accessor)."""
        return self._e

    @e.setter
    def e(self, value: "EmphasisText") -> None:
        """
        Set e with validation.

        Args:
            value: The e to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, EmphasisText):
            raise TypeError(
                f"e must be EmphasisText, got {type(value).__name__}"
            )
        self._e = value
        self._ft: "SlOverviewParagraph" = None

    @property
    def ft(self) -> "SlOverviewParagraph":
        """Get ft (Pythonic accessor)."""
        return self._ft

    @ft.setter
    def ft(self, value: "SlOverviewParagraph") -> None:
        """
        Set ft with validation.

        Args:
            value: The ft to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, SlOverviewParagraph):
            raise TypeError(
                f"ft must be SlOverviewParagraph, got {type(value).__name__}"
            )
        self._ft = value
        self._ie: "IndexEntry" = None

    @property
    def ie(self) -> "IndexEntry":
        """Get ie (Pythonic accessor)."""
        return self._ie

    @ie.setter
    def ie(self, value: "IndexEntry") -> None:
        """
        Set ie with validation.

        Args:
            value: The ie to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, IndexEntry):
            raise TypeError(
                f"ie must be IndexEntry, got {type(value).__name__}"
            )
        self._ie = value
        self._sub: "Superscript" = None

    @property
    def sub(self) -> "Superscript":
        """Get sub (Pythonic accessor)."""
        return self._sub

    @sub.setter
    def sub(self, value: "Superscript") -> None:
        """
        Set sub with validation.

        Args:
            value: The sub to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sub must be Superscript, got {type(value).__name__}"
            )
        self._sub = value
        self._sup: "Superscript" = None

    @property
    def sup(self) -> "Superscript":
        """Get sup (Pythonic accessor)."""
        return self._sup

    @sup.setter
    def sup(self, value: "Superscript") -> None:
        """
        Set sup with validation.

        Args:
            value: The sup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sup must be Superscript, got {type(value).__name__}"
            )
        self._sup = value
        self._trace: "Traceable" = None

    @property
    def trace(self) -> "Traceable":
        """Get trace (Pythonic accessor)."""
        return self._trace

    @trace.setter
    def trace(self, value: "Traceable") -> None:
        """
        Set trace with validation.

        Args:
            value: The trace to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Traceable):
            raise TypeError(
                f"trace must be Traceable, got {type(value).__name__}"
            )
        self._trace = value
        self._tt: "Tt" = None

    @property
    def tt(self) -> "Tt":
        """Get tt (Pythonic accessor)."""
        return self._tt

    @tt.setter
    def tt(self, value: "Tt") -> None:
        """
        Set tt with validation.

        Args:
            value: The tt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Tt):
            raise TypeError(
                f"tt must be Tt, got {type(value).__name__}"
            )
        self._tt = value
        self._xref: "Xref" = None

    @property
    def xref(self) -> "Xref":
        """Get xref (Pythonic accessor)."""
        return self._xref

    @xref.setter
    def xref(self, value: "Xref") -> None:
        """
        Set xref with validation.

        Args:
            value: The xref to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Xref):
            raise TypeError(
                f"xref must be Xref, got {type(value).__name__}"
            )
        self._xref = value
        self._xrefTarget: "XrefTarget" = None

    @property
    def xref_target(self) -> "XrefTarget":
        """Get xrefTarget (Pythonic accessor)."""
        return self._xrefTarget

    @xref_target.setter
    def xref_target(self, value: "XrefTarget") -> None:
        """
        Set xrefTarget with validation.

        Args:
            value: The xrefTarget to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, XrefTarget):
            raise TypeError(
                f"xrefTarget must be XrefTarget, got {type(value).__name__}"
            )
        self._xrefTarget = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBr(self) -> "Br":
        """
        AUTOSAR-compliant getter for br.

        Returns:
            The br value

        Note:
            Delegates to br property (CODING_RULE_V2_00017)
        """
        return self.br  # Delegates to property

    def setBr(self, value: "Br") -> "MixedContentForOverviewParagraph":
        """
        AUTOSAR-compliant setter for br with method chaining.

        Args:
            value: The br to set

        Returns:
            self for method chaining

        Note:
            Delegates to br property setter (gets validation automatically)
        """
        self.br = value  # Delegates to property setter
        return self

    def getE(self) -> "EmphasisText":
        """
        AUTOSAR-compliant getter for e.

        Returns:
            The e value

        Note:
            Delegates to e property (CODING_RULE_V2_00017)
        """
        return self.e  # Delegates to property

    def setE(self, value: "EmphasisText") -> "MixedContentForOverviewParagraph":
        """
        AUTOSAR-compliant setter for e with method chaining.

        Args:
            value: The e to set

        Returns:
            self for method chaining

        Note:
            Delegates to e property setter (gets validation automatically)
        """
        self.e = value  # Delegates to property setter
        return self

    def getFt(self) -> "SlOverviewParagraph":
        """
        AUTOSAR-compliant getter for ft.

        Returns:
            The ft value

        Note:
            Delegates to ft property (CODING_RULE_V2_00017)
        """
        return self.ft  # Delegates to property

    def setFt(self, value: "SlOverviewParagraph") -> "MixedContentForOverviewParagraph":
        """
        AUTOSAR-compliant setter for ft with method chaining.

        Args:
            value: The ft to set

        Returns:
            self for method chaining

        Note:
            Delegates to ft property setter (gets validation automatically)
        """
        self.ft = value  # Delegates to property setter
        return self

    def getIe(self) -> "IndexEntry":
        """
        AUTOSAR-compliant getter for ie.

        Returns:
            The ie value

        Note:
            Delegates to ie property (CODING_RULE_V2_00017)
        """
        return self.ie  # Delegates to property

    def setIe(self, value: "IndexEntry") -> "MixedContentForOverviewParagraph":
        """
        AUTOSAR-compliant setter for ie with method chaining.

        Args:
            value: The ie to set

        Returns:
            self for method chaining

        Note:
            Delegates to ie property setter (gets validation automatically)
        """
        self.ie = value  # Delegates to property setter
        return self

    def getSub(self) -> "Superscript":
        """
        AUTOSAR-compliant getter for sub.

        Returns:
            The sub value

        Note:
            Delegates to sub property (CODING_RULE_V2_00017)
        """
        return self.sub  # Delegates to property

    def setSub(self, value: "Superscript") -> "MixedContentForOverviewParagraph":
        """
        AUTOSAR-compliant setter for sub with method chaining.

        Args:
            value: The sub to set

        Returns:
            self for method chaining

        Note:
            Delegates to sub property setter (gets validation automatically)
        """
        self.sub = value  # Delegates to property setter
        return self

    def getSup(self) -> "Superscript":
        """
        AUTOSAR-compliant getter for sup.

        Returns:
            The sup value

        Note:
            Delegates to sup property (CODING_RULE_V2_00017)
        """
        return self.sup  # Delegates to property

    def setSup(self, value: "Superscript") -> "MixedContentForOverviewParagraph":
        """
        AUTOSAR-compliant setter for sup with method chaining.

        Args:
            value: The sup to set

        Returns:
            self for method chaining

        Note:
            Delegates to sup property setter (gets validation automatically)
        """
        self.sup = value  # Delegates to property setter
        return self

    def getTrace(self) -> "Traceable":
        """
        AUTOSAR-compliant getter for trace.

        Returns:
            The trace value

        Note:
            Delegates to trace property (CODING_RULE_V2_00017)
        """
        return self.trace  # Delegates to property

    def setTrace(self, value: "Traceable") -> "MixedContentForOverviewParagraph":
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

    def getTt(self) -> "Tt":
        """
        AUTOSAR-compliant getter for tt.

        Returns:
            The tt value

        Note:
            Delegates to tt property (CODING_RULE_V2_00017)
        """
        return self.tt  # Delegates to property

    def setTt(self, value: "Tt") -> "MixedContentForOverviewParagraph":
        """
        AUTOSAR-compliant setter for tt with method chaining.

        Args:
            value: The tt to set

        Returns:
            self for method chaining

        Note:
            Delegates to tt property setter (gets validation automatically)
        """
        self.tt = value  # Delegates to property setter
        return self

    def getXref(self) -> "Xref":
        """
        AUTOSAR-compliant getter for xref.

        Returns:
            The xref value

        Note:
            Delegates to xref property (CODING_RULE_V2_00017)
        """
        return self.xref  # Delegates to property

    def setXref(self, value: "Xref") -> "MixedContentForOverviewParagraph":
        """
        AUTOSAR-compliant setter for xref with method chaining.

        Args:
            value: The xref to set

        Returns:
            self for method chaining

        Note:
            Delegates to xref property setter (gets validation automatically)
        """
        self.xref = value  # Delegates to property setter
        return self

    def getXrefTarget(self) -> "XrefTarget":
        """
        AUTOSAR-compliant getter for xrefTarget.

        Returns:
            The xrefTarget value

        Note:
            Delegates to xref_target property (CODING_RULE_V2_00017)
        """
        return self.xref_target  # Delegates to property

    def setXrefTarget(self, value: "XrefTarget") -> "MixedContentForOverviewParagraph":
        """
        AUTOSAR-compliant setter for xrefTarget with method chaining.

        Args:
            value: The xrefTarget to set

        Returns:
            self for method chaining

        Note:
            Delegates to xref_target property setter (gets validation automatically)
        """
        self.xref_target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_br(self, value: "Br") -> "MixedContentForOverviewParagraph":
        """
        Set br and return self for chaining.

        Args:
            value: The br to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_br("value")
        """
        self.br = value  # Use property setter (gets validation)
        return self

    def with_e(self, value: "EmphasisText") -> "MixedContentForOverviewParagraph":
        """
        Set e and return self for chaining.

        Args:
            value: The e to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_e("value")
        """
        self.e = value  # Use property setter (gets validation)
        return self

    def with_ft(self, value: "SlOverviewParagraph") -> "MixedContentForOverviewParagraph":
        """
        Set ft and return self for chaining.

        Args:
            value: The ft to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ft("value")
        """
        self.ft = value  # Use property setter (gets validation)
        return self

    def with_ie(self, value: "IndexEntry") -> "MixedContentForOverviewParagraph":
        """
        Set ie and return self for chaining.

        Args:
            value: The ie to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ie("value")
        """
        self.ie = value  # Use property setter (gets validation)
        return self

    def with_sub(self, value: "Superscript") -> "MixedContentForOverviewParagraph":
        """
        Set sub and return self for chaining.

        Args:
            value: The sub to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub("value")
        """
        self.sub = value  # Use property setter (gets validation)
        return self

    def with_sup(self, value: "Superscript") -> "MixedContentForOverviewParagraph":
        """
        Set sup and return self for chaining.

        Args:
            value: The sup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sup("value")
        """
        self.sup = value  # Use property setter (gets validation)
        return self

    def with_trace(self, value: "Traceable") -> "MixedContentForOverviewParagraph":
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

    def with_tt(self, value: "Tt") -> "MixedContentForOverviewParagraph":
        """
        Set tt and return self for chaining.

        Args:
            value: The tt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tt("value")
        """
        self.tt = value  # Use property setter (gets validation)
        return self

    def with_xref(self, value: "Xref") -> "MixedContentForOverviewParagraph":
        """
        Set xref and return self for chaining.

        Args:
            value: The xref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_xref("value")
        """
        self.xref = value  # Use property setter (gets validation)
        return self

    def with_xref_target(self, value: "XrefTarget") -> "MixedContentForOverviewParagraph":
        """
        Set xrefTarget and return self for chaining.

        Args:
            value: The xrefTarget to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_xref_target("value")
        """
        self.xref_target = value  # Use property setter (gets validation)
        return self
