from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SignalPathConstraint(ARObject, ABC):
    """
    Additional guidelines for the System Generator, which specific way a signal
    between two Software Components should take in the network without defining
    in which frame and with which timing it is transmitted.

    Package: M2::AUTOSARTemplates::SystemTemplate::SignalPaths::SignalPathConstraint

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2057, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is SignalPathConstraint:
            raise TypeError("SignalPathConstraint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents introductory documentation about the constraint.
        self._introduction: "DocumentationBlock" = None

    @property
    def introduction(self) -> "DocumentationBlock":
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: "DocumentationBlock") -> None:
        """
        Set introduction with validation.

        Args:
            value: The introduction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock, got {type(value).__name__}"
            )
        self._introduction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "SignalPathConstraint":
        """
        AUTOSAR-compliant setter for introduction with method chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_introduction(self, value: "DocumentationBlock") -> "SignalPathConstraint":
        """
        Set introduction and return self for chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self
