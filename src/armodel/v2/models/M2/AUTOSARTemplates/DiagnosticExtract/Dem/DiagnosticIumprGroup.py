from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DiagnosticIumprGroup(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a IUMPR groups.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticIumprGroup

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 210, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference collects DiagnosticIumpr to a Diagnostic.
        self._iumpr: List["DiagnosticIumpr"] = []

    @property
    def iumpr(self) -> List["DiagnosticIumpr"]:
        """Get iumpr (Pythonic accessor)."""
        return self._iumpr
        # This aggregation allows for the variant modeling of the groupIdentifier.
        # atpVariation.
        self._iumprGroup: RefType = None

    @property
    def iumpr_group(self) -> RefType:
        """Get iumprGroup (Pythonic accessor)."""
        return self._iumprGroup

    @iumpr_group.setter
    def iumpr_group(self, value: RefType) -> None:
        """
        Set iumprGroup with validation.

        Args:
            value: The iumprGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iumprGroup = None
            return

        self._iumprGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIumpr(self) -> List["DiagnosticIumpr"]:
        """
        AUTOSAR-compliant getter for iumpr.

        Returns:
            The iumpr value

        Note:
            Delegates to iumpr property (CODING_RULE_V2_00017)
        """
        return self.iumpr  # Delegates to property

    def getIumprGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for iumprGroup.

        Returns:
            The iumprGroup value

        Note:
            Delegates to iumpr_group property (CODING_RULE_V2_00017)
        """
        return self.iumpr_group  # Delegates to property

    def setIumprGroup(self, value: RefType) -> "DiagnosticIumprGroup":
        """
        AUTOSAR-compliant setter for iumprGroup with method chaining.

        Args:
            value: The iumprGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to iumpr_group property setter (gets validation automatically)
        """
        self.iumpr_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_iumpr_group(self, value: Optional[RefType]) -> "DiagnosticIumprGroup":
        """
        Set iumprGroup and return self for chaining.

        Args:
            value: The iumprGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iumpr_group("value")
        """
        self.iumpr_group = value  # Use property setter (gets validation)
        return self
