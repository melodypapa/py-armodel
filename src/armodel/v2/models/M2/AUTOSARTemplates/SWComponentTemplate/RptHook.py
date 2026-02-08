from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class RptHook(ARObject):
    """
    This meta-class provide the ability to describe a rapid prototyping hook.
    This can either be described by an other AUTOSAR system with the category
    RPT_SYSTEM or as a non AUTOSAR software.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::RptHook

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 848, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute provides a code label which is used in the the hook.
        # For example this can be an C or the name of data definition.
        self._codeLabel: Optional["CIdentifier"] = None

    @property
    def code_label(self) -> Optional["CIdentifier"]:
        """Get codeLabel (Pythonic accessor)."""
        return self._codeLabel

    @code_label.setter
    def code_label(self, value: Optional["CIdentifier"]) -> None:
        """
        Set codeLabel with validation.

        Args:
            value: The codeLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._codeLabel = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"codeLabel must be CIdentifier or None, got {type(value).__name__}"
            )
        self._codeLabel = value
        # This attribute provides an identifier which shall be used in System to
        # display the Rpt Hook.
        self._mcdIdentifier: Optional["NameToken"] = None

    @property
    def mcd_identifier(self) -> Optional["NameToken"]:
        """Get mcdIdentifier (Pythonic accessor)."""
        return self._mcdIdentifier

    @mcd_identifier.setter
    def mcd_identifier(self, value: Optional["NameToken"]) -> None:
        """
        Set mcdIdentifier with validation.

        Args:
            value: The mcdIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mcdIdentifier = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"mcdIdentifier must be NameToken or None, got {type(value).__name__}"
            )
        self._mcdIdentifier = value
        # by: AnyInstanceRef.
        self._rptArHook: Optional["AtpFeature"] = None

    @property
    def rpt_ar_hook(self) -> Optional["AtpFeature"]:
        """Get rptArHook (Pythonic accessor)."""
        return self._rptArHook

    @rpt_ar_hook.setter
    def rpt_ar_hook(self, value: Optional["AtpFeature"]) -> None:
        """
        Set rptArHook with validation.

        Args:
            value: The rptArHook to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptArHook = None
            return

        if not isinstance(value, AtpFeature):
            raise TypeError(
                f"rptArHook must be AtpFeature or None, got {type(value).__name__}"
            )
        self._rptArHook = value
        # This property allows to keep special data which is not the standard model.
        # It can be utilized to tool specific data.
        self._sdg: List["Sdg"] = []

    @property
    def sdg(self) -> List["Sdg"]:
        """Get sdg (Pythonic accessor)."""
        return self._sdg

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCodeLabel(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for codeLabel.

        Returns:
            The codeLabel value

        Note:
            Delegates to code_label property (CODING_RULE_V2_00017)
        """
        return self.code_label  # Delegates to property

    def setCodeLabel(self, value: "CIdentifier") -> "RptHook":
        """
        AUTOSAR-compliant setter for codeLabel with method chaining.

        Args:
            value: The codeLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to code_label property setter (gets validation automatically)
        """
        self.code_label = value  # Delegates to property setter
        return self

    def getMcdIdentifier(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for mcdIdentifier.

        Returns:
            The mcdIdentifier value

        Note:
            Delegates to mcd_identifier property (CODING_RULE_V2_00017)
        """
        return self.mcd_identifier  # Delegates to property

    def setMcdIdentifier(self, value: "NameToken") -> "RptHook":
        """
        AUTOSAR-compliant setter for mcdIdentifier with method chaining.

        Args:
            value: The mcdIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to mcd_identifier property setter (gets validation automatically)
        """
        self.mcd_identifier = value  # Delegates to property setter
        return self

    def getRptArHook(self) -> "AtpFeature":
        """
        AUTOSAR-compliant getter for rptArHook.

        Returns:
            The rptArHook value

        Note:
            Delegates to rpt_ar_hook property (CODING_RULE_V2_00017)
        """
        return self.rpt_ar_hook  # Delegates to property

    def setRptArHook(self, value: "AtpFeature") -> "RptHook":
        """
        AUTOSAR-compliant setter for rptArHook with method chaining.

        Args:
            value: The rptArHook to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_ar_hook property setter (gets validation automatically)
        """
        self.rpt_ar_hook = value  # Delegates to property setter
        return self

    def getSdg(self) -> List["Sdg"]:
        """
        AUTOSAR-compliant getter for sdg.

        Returns:
            The sdg value

        Note:
            Delegates to sdg property (CODING_RULE_V2_00017)
        """
        return self.sdg  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_code_label(self, value: Optional["CIdentifier"]) -> "RptHook":
        """
        Set codeLabel and return self for chaining.

        Args:
            value: The codeLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_code_label("value")
        """
        self.code_label = value  # Use property setter (gets validation)
        return self

    def with_mcd_identifier(self, value: Optional["NameToken"]) -> "RptHook":
        """
        Set mcdIdentifier and return self for chaining.

        Args:
            value: The mcdIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mcd_identifier("value")
        """
        self.mcd_identifier = value  # Use property setter (gets validation)
        return self

    def with_rpt_ar_hook(self, value: Optional["AtpFeature"]) -> "RptHook":
        """
        Set rptArHook and return self for chaining.

        Args:
            value: The rptArHook to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_ar_hook("value")
        """
        self.rpt_ar_hook = value  # Use property setter (gets validation)
        return self
