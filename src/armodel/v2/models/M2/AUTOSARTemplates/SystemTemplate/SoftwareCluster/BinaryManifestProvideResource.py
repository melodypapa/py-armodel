from typing import Optional


class BinaryManifestProvideResource(BinaryManifestResource):
    """
    This meta-class represents a provided resource in the binary manifest.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest::BinaryManifestProvideResource

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 914, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute provides an upper limit for the number of for this resource.
        self._numberOf: Optional["PositiveInteger"] = None

    @property
    def number_of(self) -> Optional["PositiveInteger"]:
        """Get numberOf (Pythonic accessor)."""
        return self._numberOf

    @number_of.setter
    def number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set numberOf with validation.

        Args:
            value: The numberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._numberOf = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"numberOf must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._numberOf = value
        # This attribute indicates whether the enclosing Binary supports multiple
        # notifiers sets.
        self._supports: Optional["Boolean"] = None

    @property
    def supports(self) -> Optional["Boolean"]:
        """Get supports (Pythonic accessor)."""
        return self._supports

    @supports.setter
    def supports(self, value: Optional["Boolean"]) -> None:
        """
        Set supports with validation.

        Args:
            value: The supports to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supports = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"supports must be Boolean or None, got {type(value).__name__}"
            )
        self._supports = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for numberOf.

        Returns:
            The numberOf value

        Note:
            Delegates to number_of property (CODING_RULE_V2_00017)
        """
        return self.number_of  # Delegates to property

    def setNumberOf(self, value: "PositiveInteger") -> "BinaryManifestProvideResource":
        """
        AUTOSAR-compliant setter for numberOf with method chaining.

        Args:
            value: The numberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to number_of property setter (gets validation automatically)
        """
        self.number_of = value  # Delegates to property setter
        return self

    def getSupports(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for supports.

        Returns:
            The supports value

        Note:
            Delegates to supports property (CODING_RULE_V2_00017)
        """
        return self.supports  # Delegates to property

    def setSupports(self, value: "Boolean") -> "BinaryManifestProvideResource":
        """
        AUTOSAR-compliant setter for supports with method chaining.

        Args:
            value: The supports to set

        Returns:
            self for method chaining

        Note:
            Delegates to supports property setter (gets validation automatically)
        """
        self.supports = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_number_of(self, value: Optional["PositiveInteger"]) -> "BinaryManifestProvideResource":
        """
        Set numberOf and return self for chaining.

        Args:
            value: The numberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_number_of("value")
        """
        self.number_of = value  # Use property setter (gets validation)
        return self

    def with_supports(self, value: Optional["Boolean"]) -> "BinaryManifestProvideResource":
        """
        Set supports and return self for chaining.

        Args:
            value: The supports to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supports("value")
        """
        self.supports = value  # Use property setter (gets validation)
        return self
