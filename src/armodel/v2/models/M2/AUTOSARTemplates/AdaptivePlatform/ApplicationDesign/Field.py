from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import AutosarDataPrototype


class Field(AutosarDataPrototype):
    """
    This meta-class represents the ability to define a piece of data that can be
    accessed with read and/or write semantics. It is also possible to generate a
    notification if the value of the data changes.

    Package: M2::AUTOSARTemplates::AdaptivePlatform::ApplicationDesign::PortInterface::Field

    Sources:
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 45, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls whether read access is foreseen to.
        self._hasGetter: Optional["Boolean"] = None

    @property
    def has_getter(self) -> Optional["Boolean"]:
        """Get hasGetter (Pythonic accessor)."""
        return self._hasGetter

    @has_getter.setter
    def has_getter(self, value: Optional["Boolean"]) -> None:
        """
        Set hasGetter with validation.

        Args:
            value: The hasGetter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hasGetter = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"hasGetter must be Boolean or None, got {type(value).__name__}"
            )
        self._hasGetter = value
        # This attribute controls whether a notification semantics is this field.
        self._hasNotifier: Optional["Boolean"] = None

    @property
    def has_notifier(self) -> Optional["Boolean"]:
        """Get hasNotifier (Pythonic accessor)."""
        return self._hasNotifier

    @has_notifier.setter
    def has_notifier(self, value: Optional["Boolean"]) -> None:
        """
        Set hasNotifier with validation.

        Args:
            value: The hasNotifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hasNotifier = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"hasNotifier must be Boolean or None, got {type(value).__name__}"
            )
        self._hasNotifier = value
        # This attribute controls whether write access is foreseen to.
        self._hasSetter: Optional["Boolean"] = None

    @property
    def has_setter(self) -> Optional["Boolean"]:
        """Get hasSetter (Pythonic accessor)."""
        return self._hasSetter

    @has_setter.setter
    def has_setter(self, value: Optional["Boolean"]) -> None:
        """
        Set hasSetter with validation.

        Args:
            value: The hasSetter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hasSetter = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"hasSetter must be Boolean or None, got {type(value).__name__}"
            )
        self._hasSetter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHasGetter(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for hasGetter.

        Returns:
            The hasGetter value

        Note:
            Delegates to has_getter property (CODING_RULE_V2_00017)
        """
        return self.has_getter  # Delegates to property

    def setHasGetter(self, value: "Boolean") -> "Field":
        """
        AUTOSAR-compliant setter for hasGetter with method chaining.

        Args:
            value: The hasGetter to set

        Returns:
            self for method chaining

        Note:
            Delegates to has_getter property setter (gets validation automatically)
        """
        self.has_getter = value  # Delegates to property setter
        return self

    def getHasNotifier(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for hasNotifier.

        Returns:
            The hasNotifier value

        Note:
            Delegates to has_notifier property (CODING_RULE_V2_00017)
        """
        return self.has_notifier  # Delegates to property

    def setHasNotifier(self, value: "Boolean") -> "Field":
        """
        AUTOSAR-compliant setter for hasNotifier with method chaining.

        Args:
            value: The hasNotifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to has_notifier property setter (gets validation automatically)
        """
        self.has_notifier = value  # Delegates to property setter
        return self

    def getHasSetter(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for hasSetter.

        Returns:
            The hasSetter value

        Note:
            Delegates to has_setter property (CODING_RULE_V2_00017)
        """
        return self.has_setter  # Delegates to property

    def setHasSetter(self, value: "Boolean") -> "Field":
        """
        AUTOSAR-compliant setter for hasSetter with method chaining.

        Args:
            value: The hasSetter to set

        Returns:
            self for method chaining

        Note:
            Delegates to has_setter property setter (gets validation automatically)
        """
        self.has_setter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_has_getter(self, value: Optional["Boolean"]) -> "Field":
        """
        Set hasGetter and return self for chaining.

        Args:
            value: The hasGetter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_has_getter("value")
        """
        self.has_getter = value  # Use property setter (gets validation)
        return self

    def with_has_notifier(self, value: Optional["Boolean"]) -> "Field":
        """
        Set hasNotifier and return self for chaining.

        Args:
            value: The hasNotifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_has_notifier("value")
        """
        self.has_notifier = value  # Use property setter (gets validation)
        return self

    def with_has_setter(self, value: Optional["Boolean"]) -> "Field":
        """
        Set hasSetter and return self for chaining.

        Args:
            value: The hasSetter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_has_setter("value")
        """
        self.has_setter = value  # Use property setter (gets validation)
        return self
