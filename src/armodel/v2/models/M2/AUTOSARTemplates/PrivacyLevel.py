from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class PrivacyLevel(ARObject):
    """
    This meta-class defines the Privacy Level for a Log and Trace content.

    Package: M2::AUTOSARTemplates::LogAndTraceExtract

    Sources:
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 18, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to CompuMethod of category TEXTTABLE the supported user-defined
        # privacy levels.
        self._compuMethod: Optional["CompuMethod"] = None

    @property
    def compu_method(self) -> Optional["CompuMethod"]:
        """Get compuMethod (Pythonic accessor)."""
        return self._compuMethod

    @compu_method.setter
    def compu_method(self, value: Optional["CompuMethod"]) -> None:
        """
        Set compuMethod with validation.

        Args:
            value: The compuMethod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuMethod = None
            return

        if not isinstance(value, CompuMethod):
            raise TypeError(
                f"compuMethod must be CompuMethod or None, got {type(value).__name__}"
            )
        self._compuMethod = value
        # The value that represents the privacy level and is the Extension Header.
        self._privacyLevel: Optional["PositiveInteger"] = None

    @property
    def privacy_level(self) -> Optional["PositiveInteger"]:
        """Get privacyLevel (Pythonic accessor)."""
        return self._privacyLevel

    @privacy_level.setter
    def privacy_level(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set privacyLevel with validation.

        Args:
            value: The privacyLevel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._privacyLevel = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"privacyLevel must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._privacyLevel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuMethod(self) -> "CompuMethod":
        """
        AUTOSAR-compliant getter for compuMethod.

        Returns:
            The compuMethod value

        Note:
            Delegates to compu_method property (CODING_RULE_V2_00017)
        """
        return self.compu_method  # Delegates to property

    def setCompuMethod(self, value: "CompuMethod") -> "PrivacyLevel":
        """
        AUTOSAR-compliant setter for compuMethod with method chaining.

        Args:
            value: The compuMethod to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_method property setter (gets validation automatically)
        """
        self.compu_method = value  # Delegates to property setter
        return self

    def getPrivacyLevel(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for privacyLevel.

        Returns:
            The privacyLevel value

        Note:
            Delegates to privacy_level property (CODING_RULE_V2_00017)
        """
        return self.privacy_level  # Delegates to property

    def setPrivacyLevel(self, value: "PositiveInteger") -> "PrivacyLevel":
        """
        AUTOSAR-compliant setter for privacyLevel with method chaining.

        Args:
            value: The privacyLevel to set

        Returns:
            self for method chaining

        Note:
            Delegates to privacy_level property setter (gets validation automatically)
        """
        self.privacy_level = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_method(self, value: Optional["CompuMethod"]) -> "PrivacyLevel":
        """
        Set compuMethod and return self for chaining.

        Args:
            value: The compuMethod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_method("value")
        """
        self.compu_method = value  # Use property setter (gets validation)
        return self

    def with_privacy_level(self, value: Optional["PositiveInteger"]) -> "PrivacyLevel":
        """
        Set privacyLevel and return self for chaining.

        Args:
            value: The privacyLevel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_privacy_level("value")
        """
        self.privacy_level = value  # Use property setter (gets validation)
        return self
