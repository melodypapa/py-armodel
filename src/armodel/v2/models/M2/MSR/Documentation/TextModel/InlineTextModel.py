"""
AUTOSAR Package - InlineTextModel

Package: M2::MSR::Documentation::TextModel::InlineTextModel
"""

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import (
    Traceable,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Br,
    EmphasisText,
    IndexEntry,
    Std,
    Superscript,
    Tt,
    Xdoc,
    Xfile,
    Xref,
    XrefTarget,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.SingleLanguageData import (
    SlOverviewParagraph,
    SlParagraph,
)


class MixedContentForLongName(ARObject, ABC):
    """
    This is the model for titles and long-names. It allows some emphasis and
    index entries but no reference target (which is provided by the identifiable
    in question). It is intended that the content model can also be rendered as
    plain text. The abstract class can be used for single language as well as
    for multi language elements.

    Package: M2::MSR::Documentation::TextModel::InlineTextModel::MixedContentForLongName

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is MixedContentForLongName:
            raise TypeError("MixedContentForLongName is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is emphasized text.
        self._e: Optional[EmphasisText] = None

    @property
    def e(self) -> Optional[EmphasisText]:
        """Get e (Pythonic accessor)."""
        return self._e

    @e.setter
    def e(self, value: Optional[EmphasisText]) -> None:
        """
        Set e with validation.

        Args:
            value: The e to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._e = None
            return
        if not isinstance(value, EmphasisText):
            raise TypeError(
                f"e must be EmphasisText, got {type(value).__name__}"
            )
        self._e = value
        self._ie: Optional[IndexEntry] = None

    @property
    def ie(self) -> Optional[IndexEntry]:
        """Get ie (Pythonic accessor)."""
        return self._ie

    @ie.setter
    def ie(self, value: Optional[IndexEntry]) -> None:
        """
        Set ie with validation.

        Args:
            value: The ie to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ie = None
            return
        if not isinstance(value, IndexEntry):
            raise TypeError(
                f"ie must be IndexEntry, got {type(value).__name__}"
            )
        self._ie = value
        self._sub: Optional[Superscript] = None

    @property
    def sub(self) -> Optional[Superscript]:
        """Get sub (Pythonic accessor)."""
        return self._sub

    @sub.setter
    def sub(self, value: Optional[Superscript]) -> None:
        """
        Set sub with validation.

        Args:
            value: The sub to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sub = None
            return
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sub must be Superscript, got {type(value).__name__}"
            )
        self._sub = value
        self._sup: Optional[Superscript] = None

    @property
    def sup(self) -> Optional[Superscript]:
        """Get sup (Pythonic accessor)."""
        return self._sup

    @sup.setter
    def sup(self, value: Optional[Superscript]) -> None:
        """
        Set sup with validation.

        Args:
            value: The sup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sup = None
            return
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sup must be Superscript, got {type(value).__name__}"
            )
        self._sup = value
        self._tt: Optional[Tt] = None

    @property
    def tt(self) -> Optional[Tt]:
        """Get tt (Pythonic accessor)."""
        return self._tt

    @tt.setter
    def tt(self, value: Optional[Tt]) -> None:
        """
        Set tt with validation.

        Args:
            value: The tt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tt = None
            return
        if not isinstance(value, Tt):
            raise TypeError(
                f"tt must be Tt, got {type(value).__name__}"
            )
        self._tt = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getE(self) -> Optional[EmphasisText]:
        """
        AUTOSAR-compliant getter for e.

        Returns:
            The e value

        Note:
            Delegates to e property (CODING_RULE_V2_00017)
        """
        return self.e  # Delegates to property

    def setE(self, value: Optional[EmphasisText]) -> "MixedContentForLongName":
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

    def getIe(self) -> Optional[IndexEntry]:
        """
        AUTOSAR-compliant getter for ie.

        Returns:
            The ie value

        Note:
            Delegates to ie property (CODING_RULE_V2_00017)
        """
        return self.ie  # Delegates to property

    def setIe(self, value: Optional[IndexEntry]) -> "MixedContentForLongName":
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

    def getSub(self) -> Optional[Superscript]:
        """
        AUTOSAR-compliant getter for sub.

        Returns:
            The sub value

        Note:
            Delegates to sub property (CODING_RULE_V2_00017)
        """
        return self.sub  # Delegates to property

    def setSub(self, value: Optional[Superscript]) -> "MixedContentForLongName":
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

    def getSup(self) -> Optional[Superscript]:
        """
        AUTOSAR-compliant getter for sup.

        Returns:
            The sup value

        Note:
            Delegates to sup property (CODING_RULE_V2_00017)
        """
        return self.sup  # Delegates to property

    def setSup(self, value: Optional[Superscript]) -> "MixedContentForLongName":
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

    def getTt(self) -> Optional[Tt]:
        """
        AUTOSAR-compliant getter for tt.

        Returns:
            The tt value

        Note:
            Delegates to tt property (CODING_RULE_V2_00017)
        """
        return self.tt  # Delegates to property

    def setTt(self, value: Optional[Tt]) -> "MixedContentForLongName":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_e(self, value: Optional[EmphasisText]) -> "MixedContentForLongName":
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

    def with_ie(self, value: Optional[IndexEntry]) -> "MixedContentForLongName":
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

    def with_sub(self, value: Optional[Superscript]) -> "MixedContentForLongName":
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

    def with_sup(self, value: Optional[Superscript]) -> "MixedContentForLongName":
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

    def with_tt(self, value: Optional[Tt]) -> "MixedContentForLongName":
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



class MixedContentForParagraph(ARObject, ABC):
    """
    This mainly represents the text model of a full blown paragraph within a
    documentation.

    Package: M2::MSR::Documentation::TextModel::InlineTextModel::MixedContentForParagraph

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 289, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is MixedContentForParagraph:
            raise TypeError("MixedContentForParagraph is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element is the same as function here as in a HTML it forces a line
        # break.
        self._br: Optional[Br] = None

    @property
    def br(self) -> Optional[Br]:
        """Get br (Pythonic accessor)."""
        return self._br

    @br.setter
    def br(self, value: Optional[Br]) -> None:
        """
        Set br with validation.

        Args:
            value: The br to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._br = None
            return
        if not isinstance(value, Br):
            raise TypeError(
                f"br must be Br, got {type(value).__name__}"
            )
        self._br = value
        self._e: Optional[EmphasisText] = None

    @property
    def e(self) -> Optional[EmphasisText]:
        """Get e (Pythonic accessor)."""
        return self._e

    @e.setter
    def e(self, value: Optional[EmphasisText]) -> None:
        """
        Set e with validation.

        Args:
            value: The e to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._e = None
            return
        if not isinstance(value, EmphasisText):
            raise TypeError(
                f"e must be EmphasisText, got {type(value).__name__}"
            )
        self._e = value
        self._ft: Optional[SlParagraph] = None

    @property
    def ft(self) -> Optional[SlParagraph]:
        """Get ft (Pythonic accessor)."""
        return self._ft

    @ft.setter
    def ft(self, value: Optional[SlParagraph]) -> None:
        """
        Set ft with validation.

        Args:
            value: The ft to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ft = None
            return
        if not isinstance(value, SlParagraph):
            raise TypeError(
                f"ft must be SlParagraph, got {type(value).__name__}"
            )
        self._ft = value
        self._ie: Optional[IndexEntry] = None

    @property
    def ie(self) -> Optional[IndexEntry]:
        """Get ie (Pythonic accessor)."""
        return self._ie

    @ie.setter
    def ie(self, value: Optional[IndexEntry]) -> None:
        """
        Set ie with validation.

        Args:
            value: The ie to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ie = None
            return
        if not isinstance(value, IndexEntry):
            raise TypeError(
                f"ie must be IndexEntry, got {type(value).__name__}"
            )
        self._ie = value
        self._std: Optional[Std] = None

    @property
    def std(self) -> Optional[Std]:
        """Get std (Pythonic accessor)."""
        return self._std

    @std.setter
    def std(self, value: Optional[Std]) -> None:
        """
        Set std with validation.

        Args:
            value: The std to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._std = None
            return
        if not isinstance(value, Std):
            raise TypeError(
                f"std must be Std, got {type(value).__name__}"
            )
        self._std = value
        self._sub: Optional[Superscript] = None

    @property
    def sub(self) -> Optional[Superscript]:
        """Get sub (Pythonic accessor)."""
        return self._sub

    @sub.setter
    def sub(self, value: Optional[Superscript]) -> None:
        """
        Set sub with validation.

        Args:
            value: The sub to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sub = None
            return
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sub must be Superscript, got {type(value).__name__}"
            )
        self._sub = value
        self._sup: Optional[Superscript] = None

    @property
    def sup(self) -> Optional[Superscript]:
        """Get sup (Pythonic accessor)."""
        return self._sup

    @sup.setter
    def sup(self, value: Optional[Superscript]) -> None:
        """
        Set sup with validation.

        Args:
            value: The sup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sup = None
            return
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sup must be Superscript, got {type(value).__name__}"
            )
        self._sup = value
        self._trace: Optional[Traceable] = None

    @property
    def trace(self) -> Optional[Traceable]:
        """Get trace (Pythonic accessor)."""
        return self._trace

    @trace.setter
    def trace(self, value: Optional[Traceable]) -> None:
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
        if not isinstance(value, Traceable):
            raise TypeError(
                f"trace must be Traceable, got {type(value).__name__}"
            )
        self._trace = value
        self._tt: Optional[Tt] = None

    @property
    def tt(self) -> Optional[Tt]:
        """Get tt (Pythonic accessor)."""
        return self._tt

    @tt.setter
    def tt(self, value: Optional[Tt]) -> None:
        """
        Set tt with validation.

        Args:
            value: The tt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tt = None
            return
        if not isinstance(value, Tt):
            raise TypeError(
                f"tt must be Tt, got {type(value).__name__}"
            )
        self._tt = value
        self._xdoc: Optional[Xdoc] = None

    @property
    def xdoc(self) -> Optional[Xdoc]:
        """Get xdoc (Pythonic accessor)."""
        return self._xdoc

    @xdoc.setter
    def xdoc(self, value: Optional[Xdoc]) -> None:
        """
        Set xdoc with validation.

        Args:
            value: The xdoc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._xdoc = None
            return
        if not isinstance(value, Xdoc):
            raise TypeError(
                f"xdoc must be Xdoc, got {type(value).__name__}"
            )
        self._xdoc = value
        self._xfile: Optional[Xfile] = None

    @property
    def xfile(self) -> Optional[Xfile]:
        """Get xfile (Pythonic accessor)."""
        return self._xfile

    @xfile.setter
    def xfile(self, value: Optional[Xfile]) -> None:
        """
        Set xfile with validation.

        Args:
            value: The xfile to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._xfile = None
            return
        if not isinstance(value, Xfile):
            raise TypeError(
                f"xfile must be Xfile, got {type(value).__name__}"
            )
        self._xfile = value
        self._xref: Optional[Xref] = None

    @property
    def xref(self) -> Optional[Xref]:
        """Get xref (Pythonic accessor)."""
        return self._xref

    @xref.setter
    def xref(self, value: Optional[Xref]) -> None:
        """
        Set xref with validation.

        Args:
            value: The xref to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._xref = None
            return
        if not isinstance(value, Xref):
            raise TypeError(
                f"xref must be Xref, got {type(value).__name__}"
            )
        self._xref = value
        self._xrefTarget: Optional[XrefTarget] = None

    @property
    def xref_target(self) -> Optional[XrefTarget]:
        """Get xrefTarget (Pythonic accessor)."""
        return self._xrefTarget

    @xref_target.setter
    def xref_target(self, value: Optional[XrefTarget]) -> None:
        """
        Set xrefTarget with validation.

        Args:
            value: The xrefTarget to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._xrefTarget = None
            return
        if not isinstance(value, XrefTarget):
            raise TypeError(
                f"xrefTarget must be XrefTarget, got {type(value).__name__}"
            )
        self._xrefTarget = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBr(self) -> Optional[Br]:
        """
        AUTOSAR-compliant getter for br.

        Returns:
            The br value

        Note:
            Delegates to br property (CODING_RULE_V2_00017)
        """
        return self.br  # Delegates to property

    def setBr(self, value: Optional[Br]) -> "MixedContentForParagraph":
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

    def getE(self) -> Optional[EmphasisText]:
        """
        AUTOSAR-compliant getter for e.

        Returns:
            The e value

        Note:
            Delegates to e property (CODING_RULE_V2_00017)
        """
        return self.e  # Delegates to property

    def setE(self, value: Optional[EmphasisText]) -> "MixedContentForParagraph":
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

    def getFt(self) -> Optional[SlParagraph]:
        """
        AUTOSAR-compliant getter for ft.

        Returns:
            The ft value

        Note:
            Delegates to ft property (CODING_RULE_V2_00017)
        """
        return self.ft  # Delegates to property

    def setFt(self, value: Optional[SlParagraph]) -> "MixedContentForParagraph":
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

    def getIe(self) -> Optional[IndexEntry]:
        """
        AUTOSAR-compliant getter for ie.

        Returns:
            The ie value

        Note:
            Delegates to ie property (CODING_RULE_V2_00017)
        """
        return self.ie  # Delegates to property

    def setIe(self, value: Optional[IndexEntry]) -> "MixedContentForParagraph":
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

    def getStd(self) -> Optional[Std]:
        """
        AUTOSAR-compliant getter for std.

        Returns:
            The std value

        Note:
            Delegates to std property (CODING_RULE_V2_00017)
        """
        return self.std  # Delegates to property

    def setStd(self, value: Optional[Std]) -> "MixedContentForParagraph":
        """
        AUTOSAR-compliant setter for std with method chaining.

        Args:
            value: The std to set

        Returns:
            self for method chaining

        Note:
            Delegates to std property setter (gets validation automatically)
        """
        self.std = value  # Delegates to property setter
        return self

    def getSub(self) -> Optional[Superscript]:
        """
        AUTOSAR-compliant getter for sub.

        Returns:
            The sub value

        Note:
            Delegates to sub property (CODING_RULE_V2_00017)
        """
        return self.sub  # Delegates to property

    def setSub(self, value: Optional[Superscript]) -> "MixedContentForParagraph":
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

    def getSup(self) -> Optional[Superscript]:
        """
        AUTOSAR-compliant getter for sup.

        Returns:
            The sup value

        Note:
            Delegates to sup property (CODING_RULE_V2_00017)
        """
        return self.sup  # Delegates to property

    def setSup(self, value: Optional[Superscript]) -> "MixedContentForParagraph":
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

    def getTrace(self) -> Optional[Traceable]:
        """
        AUTOSAR-compliant getter for trace.

        Returns:
            The trace value

        Note:
            Delegates to trace property (CODING_RULE_V2_00017)
        """
        return self.trace  # Delegates to property

    def setTrace(self, value: Optional[Traceable]) -> "MixedContentForParagraph":
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

    def getTt(self) -> Optional[Tt]:
        """
        AUTOSAR-compliant getter for tt.

        Returns:
            The tt value

        Note:
            Delegates to tt property (CODING_RULE_V2_00017)
        """
        return self.tt  # Delegates to property

    def setTt(self, value: Optional[Tt]) -> "MixedContentForParagraph":
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

    def getXdoc(self) -> Optional[Xdoc]:
        """
        AUTOSAR-compliant getter for xdoc.

        Returns:
            The xdoc value

        Note:
            Delegates to xdoc property (CODING_RULE_V2_00017)
        """
        return self.xdoc  # Delegates to property

    def setXdoc(self, value: Optional[Xdoc]) -> "MixedContentForParagraph":
        """
        AUTOSAR-compliant setter for xdoc with method chaining.

        Args:
            value: The xdoc to set

        Returns:
            self for method chaining

        Note:
            Delegates to xdoc property setter (gets validation automatically)
        """
        self.xdoc = value  # Delegates to property setter
        return self

    def getXfile(self) -> Optional[Xfile]:
        """
        AUTOSAR-compliant getter for xfile.

        Returns:
            The xfile value

        Note:
            Delegates to xfile property (CODING_RULE_V2_00017)
        """
        return self.xfile  # Delegates to property

    def setXfile(self, value: Optional[Xfile]) -> "MixedContentForParagraph":
        """
        AUTOSAR-compliant setter for xfile with method chaining.

        Args:
            value: The xfile to set

        Returns:
            self for method chaining

        Note:
            Delegates to xfile property setter (gets validation automatically)
        """
        self.xfile = value  # Delegates to property setter
        return self

    def getXref(self) -> Optional[Xref]:
        """
        AUTOSAR-compliant getter for xref.

        Returns:
            The xref value

        Note:
            Delegates to xref property (CODING_RULE_V2_00017)
        """
        return self.xref  # Delegates to property

    def setXref(self, value: Optional[Xref]) -> "MixedContentForParagraph":
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

    def getXrefTarget(self) -> Optional[XrefTarget]:
        """
        AUTOSAR-compliant getter for xrefTarget.

        Returns:
            The xrefTarget value

        Note:
            Delegates to xref_target property (CODING_RULE_V2_00017)
        """
        return self.xref_target  # Delegates to property

    def setXrefTarget(self, value: Optional[XrefTarget]) -> "MixedContentForParagraph":
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

    def with_br(self, value: Optional[Br]) -> "MixedContentForParagraph":
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

    def with_e(self, value: Optional[EmphasisText]) -> "MixedContentForParagraph":
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

    def with_ft(self, value: Optional[SlParagraph]) -> "MixedContentForParagraph":
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

    def with_ie(self, value: Optional[IndexEntry]) -> "MixedContentForParagraph":
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

    def with_std(self, value: Optional[Std]) -> "MixedContentForParagraph":
        """
        Set std and return self for chaining.

        Args:
            value: The std to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_std("value")
        """
        self.std = value  # Use property setter (gets validation)
        return self

    def with_sub(self, value: Optional[Superscript]) -> "MixedContentForParagraph":
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

    def with_sup(self, value: Optional[Superscript]) -> "MixedContentForParagraph":
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

    def with_trace(self, value: Optional[Traceable]) -> "MixedContentForParagraph":
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

    def with_tt(self, value: Optional[Tt]) -> "MixedContentForParagraph":
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

    def with_xdoc(self, value: Optional[Xdoc]) -> "MixedContentForParagraph":
        """
        Set xdoc and return self for chaining.

        Args:
            value: The xdoc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_xdoc("value")
        """
        self.xdoc = value  # Use property setter (gets validation)
        return self

    def with_xfile(self, value: Optional[Xfile]) -> "MixedContentForParagraph":
        """
        Set xfile and return self for chaining.

        Args:
            value: The xfile to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_xfile("value")
        """
        self.xfile = value  # Use property setter (gets validation)
        return self

    def with_xref(self, value: Optional[Xref]) -> "MixedContentForParagraph":
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

    def with_xref_target(self, value: Optional[XrefTarget]) -> "MixedContentForParagraph":
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



class MixedContentForOverviewParagraph(ARObject, ABC):
    """
    This is the text model of a restricted paragraph item within a
    documentation. Such restricted paragraphs are used mainly for overview
    items, e.g. desc.

    Package: M2::MSR::Documentation::TextModel::InlineTextModel::MixedContentForOverviewParagraph

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
        self._br: Optional[Br] = None

    @property
    def br(self) -> Optional[Br]:
        """Get br (Pythonic accessor)."""
        return self._br

    @br.setter
    def br(self, value: Optional[Br]) -> None:
        """
        Set br with validation.

        Args:
            value: The br to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._br = None
            return
        if not isinstance(value, Br):
            raise TypeError(
                f"br must be Br, got {type(value).__name__}"
            )
        self._br = value
        self._e: Optional[EmphasisText] = None

    @property
    def e(self) -> Optional[EmphasisText]:
        """Get e (Pythonic accessor)."""
        return self._e

    @e.setter
    def e(self, value: Optional[EmphasisText]) -> None:
        """
        Set e with validation.

        Args:
            value: The e to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._e = None
            return
        if not isinstance(value, EmphasisText):
            raise TypeError(
                f"e must be EmphasisText, got {type(value).__name__}"
            )
        self._e = value
        self._ft: Optional[SlOverviewParagraph] = None

    @property
    def ft(self) -> Optional[SlOverviewParagraph]:
        """Get ft (Pythonic accessor)."""
        return self._ft

    @ft.setter
    def ft(self, value: Optional[SlOverviewParagraph]) -> None:
        """
        Set ft with validation.

        Args:
            value: The ft to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ft = None
            return
        if not isinstance(value, SlOverviewParagraph):
            raise TypeError(
                f"ft must be SlOverviewParagraph, got {type(value).__name__}"
            )
        self._ft = value
        self._ie: Optional[IndexEntry] = None

    @property
    def ie(self) -> Optional[IndexEntry]:
        """Get ie (Pythonic accessor)."""
        return self._ie

    @ie.setter
    def ie(self, value: Optional[IndexEntry]) -> None:
        """
        Set ie with validation.

        Args:
            value: The ie to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ie = None
            return
        if not isinstance(value, IndexEntry):
            raise TypeError(
                f"ie must be IndexEntry, got {type(value).__name__}"
            )
        self._ie = value
        self._sub: Optional[Superscript] = None

    @property
    def sub(self) -> Optional[Superscript]:
        """Get sub (Pythonic accessor)."""
        return self._sub

    @sub.setter
    def sub(self, value: Optional[Superscript]) -> None:
        """
        Set sub with validation.

        Args:
            value: The sub to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sub = None
            return
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sub must be Superscript, got {type(value).__name__}"
            )
        self._sub = value
        self._sup: Optional[Superscript] = None

    @property
    def sup(self) -> Optional[Superscript]:
        """Get sup (Pythonic accessor)."""
        return self._sup

    @sup.setter
    def sup(self, value: Optional[Superscript]) -> None:
        """
        Set sup with validation.

        Args:
            value: The sup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sup = None
            return
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sup must be Superscript, got {type(value).__name__}"
            )
        self._sup = value
        self._trace: Optional[Traceable] = None

    @property
    def trace(self) -> Optional[Traceable]:
        """Get trace (Pythonic accessor)."""
        return self._trace

    @trace.setter
    def trace(self, value: Optional[Traceable]) -> None:
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
        if not isinstance(value, Traceable):
            raise TypeError(
                f"trace must be Traceable, got {type(value).__name__}"
            )
        self._trace = value
        self._tt: Optional[Tt] = None

    @property
    def tt(self) -> Optional[Tt]:
        """Get tt (Pythonic accessor)."""
        return self._tt

    @tt.setter
    def tt(self, value: Optional[Tt]) -> None:
        """
        Set tt with validation.

        Args:
            value: The tt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tt = None
            return
        if not isinstance(value, Tt):
            raise TypeError(
                f"tt must be Tt, got {type(value).__name__}"
            )
        self._tt = value
        self._xref: Optional[Xref] = None

    @property
    def xref(self) -> Optional[Xref]:
        """Get xref (Pythonic accessor)."""
        return self._xref

    @xref.setter
    def xref(self, value: Optional[Xref]) -> None:
        """
        Set xref with validation.

        Args:
            value: The xref to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._xref = None
            return
        if not isinstance(value, Xref):
            raise TypeError(
                f"xref must be Xref, got {type(value).__name__}"
            )
        self._xref = value
        self._xrefTarget: Optional[XrefTarget] = None

    @property
    def xref_target(self) -> Optional[XrefTarget]:
        """Get xrefTarget (Pythonic accessor)."""
        return self._xrefTarget

    @xref_target.setter
    def xref_target(self, value: Optional[XrefTarget]) -> None:
        """
        Set xrefTarget with validation.

        Args:
            value: The xrefTarget to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._xrefTarget = None
            return
        if not isinstance(value, XrefTarget):
            raise TypeError(
                f"xrefTarget must be XrefTarget, got {type(value).__name__}"
            )
        self._xrefTarget = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBr(self) -> Optional[Br]:
        """
        AUTOSAR-compliant getter for br.

        Returns:
            The br value

        Note:
            Delegates to br property (CODING_RULE_V2_00017)
        """
        return self.br  # Delegates to property

    def setBr(self, value: Optional[Br]) -> "MixedContentForOverviewParagraph":
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

    def getE(self) -> Optional[EmphasisText]:
        """
        AUTOSAR-compliant getter for e.

        Returns:
            The e value

        Note:
            Delegates to e property (CODING_RULE_V2_00017)
        """
        return self.e  # Delegates to property

    def setE(self, value: Optional[EmphasisText]) -> "MixedContentForOverviewParagraph":
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

    def getFt(self) -> Optional[SlOverviewParagraph]:
        """
        AUTOSAR-compliant getter for ft.

        Returns:
            The ft value

        Note:
            Delegates to ft property (CODING_RULE_V2_00017)
        """
        return self.ft  # Delegates to property

    def setFt(self, value: Optional[SlOverviewParagraph]) -> "MixedContentForOverviewParagraph":
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

    def getIe(self) -> Optional[IndexEntry]:
        """
        AUTOSAR-compliant getter for ie.

        Returns:
            The ie value

        Note:
            Delegates to ie property (CODING_RULE_V2_00017)
        """
        return self.ie  # Delegates to property

    def setIe(self, value: Optional[IndexEntry]) -> "MixedContentForOverviewParagraph":
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

    def getSub(self) -> Optional[Superscript]:
        """
        AUTOSAR-compliant getter for sub.

        Returns:
            The sub value

        Note:
            Delegates to sub property (CODING_RULE_V2_00017)
        """
        return self.sub  # Delegates to property

    def setSub(self, value: Optional[Superscript]) -> "MixedContentForOverviewParagraph":
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

    def getSup(self) -> Optional[Superscript]:
        """
        AUTOSAR-compliant getter for sup.

        Returns:
            The sup value

        Note:
            Delegates to sup property (CODING_RULE_V2_00017)
        """
        return self.sup  # Delegates to property

    def setSup(self, value: Optional[Superscript]) -> "MixedContentForOverviewParagraph":
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

    def getTrace(self) -> Optional[Traceable]:
        """
        AUTOSAR-compliant getter for trace.

        Returns:
            The trace value

        Note:
            Delegates to trace property (CODING_RULE_V2_00017)
        """
        return self.trace  # Delegates to property

    def setTrace(self, value: Optional[Traceable]) -> "MixedContentForOverviewParagraph":
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

    def getTt(self) -> Optional[Tt]:
        """
        AUTOSAR-compliant getter for tt.

        Returns:
            The tt value

        Note:
            Delegates to tt property (CODING_RULE_V2_00017)
        """
        return self.tt  # Delegates to property

    def setTt(self, value: Optional[Tt]) -> "MixedContentForOverviewParagraph":
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

    def getXref(self) -> Optional[Xref]:
        """
        AUTOSAR-compliant getter for xref.

        Returns:
            The xref value

        Note:
            Delegates to xref property (CODING_RULE_V2_00017)
        """
        return self.xref  # Delegates to property

    def setXref(self, value: Optional[Xref]) -> "MixedContentForOverviewParagraph":
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

    def getXrefTarget(self) -> Optional[XrefTarget]:
        """
        AUTOSAR-compliant getter for xrefTarget.

        Returns:
            The xrefTarget value

        Note:
            Delegates to xref_target property (CODING_RULE_V2_00017)
        """
        return self.xref_target  # Delegates to property

    def setXrefTarget(self, value: Optional[XrefTarget]) -> "MixedContentForOverviewParagraph":
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

    def with_br(self, value: Optional[Br]) -> "MixedContentForOverviewParagraph":
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

    def with_e(self, value: Optional[EmphasisText]) -> "MixedContentForOverviewParagraph":
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

    def with_ft(self, value: Optional[SlOverviewParagraph]) -> "MixedContentForOverviewParagraph":
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

    def with_ie(self, value: Optional[IndexEntry]) -> "MixedContentForOverviewParagraph":
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

    def with_sub(self, value: Optional[Superscript]) -> "MixedContentForOverviewParagraph":
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

    def with_sup(self, value: Optional[Superscript]) -> "MixedContentForOverviewParagraph":
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

    def with_trace(self, value: Optional[Traceable]) -> "MixedContentForOverviewParagraph":
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

    def with_tt(self, value: Optional[Tt]) -> "MixedContentForOverviewParagraph":
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

    def with_xref(self, value: Optional[Xref]) -> "MixedContentForOverviewParagraph":
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

    def with_xref_target(self, value: Optional[XrefTarget]) -> "MixedContentForOverviewParagraph":
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



class MixedContentForVerbatim(ARObject, ABC):
    """
    This is the text model for preformatted (verbatim) text. It mainly consists
    of attributes which do not change the length on rendering. This class
    represents multilingual verbatim. Verbatim, sometimes called preformatted
    text, means that white-space is maintained. When verbatim is rendered in PDF
    or Online media, it is rendered using a monospaced font while white-space is
    obeyed. Blanks are rendered as well as newline characters. Even if there are
    inline elements, the length of the data shall not be influenced by
    formatting.

    Package: M2::MSR::Documentation::TextModel::InlineTextModel::MixedContentForVerbatim

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 292, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is MixedContentForVerbatim:
            raise TypeError("MixedContentForVerbatim is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element is the same as function here as in a HTML it forces a line
        # break.
        self._br: Optional[Br] = None

    @property
    def br(self) -> Optional[Br]:
        """Get br (Pythonic accessor)."""
        return self._br

    @br.setter
    def br(self, value: Optional[Br]) -> None:
        """
        Set br with validation.

        Args:
            value: The br to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._br = None
            return
        if not isinstance(value, Br):
            raise TypeError(
                f"br must be Br, got {type(value).__name__}"
            )
        self._br = value
        # Note that in verbatim, the attribute not be considered since verbatim is
                # always monospace font.
        self._e: Optional[EmphasisText] = None

    @property
    def e(self) -> Optional[EmphasisText]:
        """Get e (Pythonic accessor)."""
        return self._e

    @e.setter
    def e(self, value: Optional[EmphasisText]) -> None:
        """
        Set e with validation.

        Args:
            value: The e to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._e = None
            return
        if not isinstance(value, EmphasisText):
            raise TypeError(
                f"e must be EmphasisText, got {type(value).__name__}"
            )
        self._e = value
        # Note that it’s of the user not to take a tt that would add to the text (such
                # as SgmlElement).
        self._tt: Optional[Tt] = None

    @property
    def tt(self) -> Optional[Tt]:
        """Get tt (Pythonic accessor)."""
        return self._tt

    @tt.setter
    def tt(self, value: Optional[Tt]) -> None:
        """
        Set tt with validation.

        Args:
            value: The tt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tt = None
            return
        if not isinstance(value, Tt):
            raise TypeError(
                f"tt must be Tt, got {type(value).__name__}"
            )
        self._tt = value
        # The disturb the arrangement of the text.
        # It is the author to keep this under control.
        self._xref: Optional[Xref] = None

    @property
    def xref(self) -> Optional[Xref]:
        """Get xref (Pythonic accessor)."""
        return self._xref

    @xref.setter
    def xref(self, value: Optional[Xref]) -> None:
        """
        Set xref with validation.

        Args:
            value: The xref to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._xref = None
            return
        if not isinstance(value, Xref):
            raise TypeError(
                f"xref must be Xref, got {type(value).__name__}"
            )
        self._xref = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBr(self) -> Optional[Br]:
        """
        AUTOSAR-compliant getter for br.

        Returns:
            The br value

        Note:
            Delegates to br property (CODING_RULE_V2_00017)
        """
        return self.br  # Delegates to property

    def setBr(self, value: Optional[Br]) -> "MixedContentForVerbatim":
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

    def getE(self) -> Optional[EmphasisText]:
        """
        AUTOSAR-compliant getter for e.

        Returns:
            The e value

        Note:
            Delegates to e property (CODING_RULE_V2_00017)
        """
        return self.e  # Delegates to property

    def setE(self, value: Optional[EmphasisText]) -> "MixedContentForVerbatim":
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

    def getTt(self) -> Optional[Tt]:
        """
        AUTOSAR-compliant getter for tt.

        Returns:
            The tt value

        Note:
            Delegates to tt property (CODING_RULE_V2_00017)
        """
        return self.tt  # Delegates to property

    def setTt(self, value: Optional[Tt]) -> "MixedContentForVerbatim":
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

    def getXref(self) -> Optional[Xref]:
        """
        AUTOSAR-compliant getter for xref.

        Returns:
            The xref value

        Note:
            Delegates to xref property (CODING_RULE_V2_00017)
        """
        return self.xref  # Delegates to property

    def setXref(self, value: Optional[Xref]) -> "MixedContentForVerbatim":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_br(self, value: Optional[Br]) -> "MixedContentForVerbatim":
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

    def with_e(self, value: Optional[EmphasisText]) -> "MixedContentForVerbatim":
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

    def with_tt(self, value: Optional[Tt]) -> "MixedContentForVerbatim":
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

    def with_xref(self, value: Optional[Xref]) -> "MixedContentForVerbatim":
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



class MixedContentForPlainText(ARObject, ABC):
    """
    This represents a plain text which conceptually is handled as mixed
    contents. It is modeled as such for symmetry reasons.

    Package: M2::MSR::Documentation::TextModel::InlineTextModel::MixedContentForPlainText

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 349, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is MixedContentForPlainText:
            raise TypeError("MixedContentForPlainText is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class MixedContentForUnitNames(ARObject, ABC):
    """
    This is the text model for items with subscript and superscripts such as
    measurement unit designations. It is intended, that such models can easily
    be transcribed to a plain text model either by using appropriate characters
    or by transcribing like mˆ2.

    Package: M2::MSR::Documentation::TextModel::InlineTextModel::MixedContentForUnitNames

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 456, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is MixedContentForUnitNames:
            raise TypeError("MixedContentForUnitNames is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is subscript text.
        self._sub: Optional[Superscript] = None

    @property
    def sub(self) -> Optional[Superscript]:
        """Get sub (Pythonic accessor)."""
        return self._sub

    @sub.setter
    def sub(self, value: Optional[Superscript]) -> None:
        """
        Set sub with validation.

        Args:
            value: The sub to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sub = None
            return
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sub must be Superscript, got {type(value).__name__}"
            )
        self._sub = value
        self._sup: Optional[Superscript] = None

    @property
    def sup(self) -> Optional[Superscript]:
        """Get sup (Pythonic accessor)."""
        return self._sup

    @sup.setter
    def sup(self, value: Optional[Superscript]) -> None:
        """
        Set sup with validation.

        Args:
            value: The sup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sup = None
            return
        if not isinstance(value, Superscript):
            raise TypeError(
                f"sup must be Superscript, got {type(value).__name__}"
            )
        self._sup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSub(self) -> Optional[Superscript]:
        """
        AUTOSAR-compliant getter for sub.

        Returns:
            The sub value

        Note:
            Delegates to sub property (CODING_RULE_V2_00017)
        """
        return self.sub  # Delegates to property

    def setSub(self, value: Optional[Superscript]) -> "MixedContentForUnitNames":
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

    def getSup(self) -> Optional[Superscript]:
        """
        AUTOSAR-compliant getter for sup.

        Returns:
            The sup value

        Note:
            Delegates to sup property (CODING_RULE_V2_00017)
        """
        return self.sup  # Delegates to property

    def setSup(self, value: Optional[Superscript]) -> "MixedContentForUnitNames":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sub(self, value: Optional[Superscript]) -> "MixedContentForUnitNames":
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

    def with_sup(self, value: Optional[Superscript]) -> "MixedContentForUnitNames":
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
