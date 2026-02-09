from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class EvaluatedVariantSet(ARElement):
    """
    that the EvaluatedVariantSet is a CollectableElement. This allows to
    establish a hierarchy of EvaluatedVariantSets.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 257, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the approval status of a predefined variant.
        # Two predefined: "APPROVED" and "REJECTED": variants are known to work.
        # variants are known NOT to work.
        # can be approved on a per-company basis; only "APPROVED" and "REJECTED"
                # recognized.
        self._approvalStatus: "NameToken" = None

    @property
    def approval_status(self) -> "NameToken":
        """Get approvalStatus (Pythonic accessor)."""
        return self._approvalStatus

    @approval_status.setter
    def approval_status(self, value: "NameToken") -> None:
        """
        Set approvalStatus with validation.

        Args:
            value: The approvalStatus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NameToken):
            raise TypeError(
                f"approvalStatus must be NameToken, got {type(value).__name__}"
            )
        self._approvalStatus = value
        # LowerMultiplicity is set to 0 to support a.
        self._evaluated: List["PredefinedVariant"] = []

    @property
    def evaluated(self) -> List["PredefinedVariant"]:
        """Get evaluated (Pythonic accessor)."""
        return self._evaluated

    def with_evaluated(self, value):
        """
        Set evaluated and return self for chaining.

        Args:
            value: The evaluated to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_evaluated("value")
        """
        self.evaluated = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApprovalStatus(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for approvalStatus.

        Returns:
            The approvalStatus value

        Note:
            Delegates to approval_status property (CODING_RULE_V2_00017)
        """
        return self.approval_status  # Delegates to property

    def setApprovalStatus(self, value: "NameToken") -> "EvaluatedVariantSet":
        """
        AUTOSAR-compliant setter for approvalStatus with method chaining.

        Args:
            value: The approvalStatus to set

        Returns:
            self for method chaining

        Note:
            Delegates to approval_status property setter (gets validation automatically)
        """
        self.approval_status = value  # Delegates to property setter
        return self

    def getEvaluated(self) -> List["PredefinedVariant"]:
        """
        AUTOSAR-compliant getter for evaluated.

        Returns:
            The evaluated value

        Note:
            Delegates to evaluated property (CODING_RULE_V2_00017)
        """
        return self.evaluated  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_approval_status(self, value: "NameToken") -> "EvaluatedVariantSet":
        """
        Set approvalStatus and return self for chaining.

        Args:
            value: The approvalStatus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_approval_status("value")
        """
        self.approval_status = value  # Use property setter (gets validation)
        return self
