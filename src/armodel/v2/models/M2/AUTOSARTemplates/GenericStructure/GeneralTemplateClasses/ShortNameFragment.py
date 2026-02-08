from armodel.v2.models.M2.AUTOSARTemplates import (
    Identifier,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ShortNameFragment(ARObject):
    """
    This class describes how the Referrable.shortName is composed of several
    shortNameFragments.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::ShortNameFragment

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 64, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies a single shortName (fragment) which is the composed shortName.
        self._fragment: "Identifier" = None

    @property
    def fragment(self) -> "Identifier":
        """Get fragment (Pythonic accessor)."""
        return self._fragment

    @fragment.setter
    def fragment(self, value: "Identifier") -> None:
        """
        Set fragment with validation.

        Args:
            value: The fragment to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Identifier):
            raise TypeError(
                f"fragment must be Identifier, got {type(value).__name__}"
            )
        self._fragment = value
        # This specifies the role of fragment to define e.
        # g.
        # the order fragments.
        self._role: "String" = None

    @property
    def role(self) -> "String":
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: "String") -> None:
        """
        Set role with validation.

        Args:
            value: The role to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, String):
            raise TypeError(
                f"role must be String, got {type(value).__name__}"
            )
        self._role = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFragment(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for fragment.

        Returns:
            The fragment value

        Note:
            Delegates to fragment property (CODING_RULE_V2_00017)
        """
        return self.fragment  # Delegates to property

    def setFragment(self, value: "Identifier") -> "ShortNameFragment":
        """
        AUTOSAR-compliant setter for fragment with method chaining.

        Args:
            value: The fragment to set

        Returns:
            self for method chaining

        Note:
            Delegates to fragment property setter (gets validation automatically)
        """
        self.fragment = value  # Delegates to property setter
        return self

    def getRole(self) -> "String":
        """
        AUTOSAR-compliant getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "String") -> "ShortNameFragment":
        """
        AUTOSAR-compliant setter for role with method chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_fragment(self, value: "Identifier") -> "ShortNameFragment":
        """
        Set fragment and return self for chaining.

        Args:
            value: The fragment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fragment("value")
        """
        self.fragment = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: "String") -> "ShortNameFragment":
        """
        Set role and return self for chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self
