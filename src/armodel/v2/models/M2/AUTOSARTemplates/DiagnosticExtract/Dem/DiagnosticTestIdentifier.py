from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DiagnosticTestIdentifier(ARObject):
    """
    This meta-class represents the ability to create a diagnostic test
    identifier.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTestResult

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 205, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the numerical id associated with the identifier.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"id must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._id = value
        # This represents the unit and scaling Id of the diagnostic.
        self._uasId: Optional["PositiveInteger"] = None

    @property
    def uas_id(self) -> Optional["PositiveInteger"]:
        """Get uasId (Pythonic accessor)."""
        return self._uasId

    @uas_id.setter
    def uas_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set uasId with validation.

        Args:
            value: The uasId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._uasId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"uasId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._uasId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticTestIdentifier":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    def getUasId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for uasId.

        Returns:
            The uasId value

        Note:
            Delegates to uas_id property (CODING_RULE_V2_00017)
        """
        return self.uas_id  # Delegates to property

    def setUasId(self, value: "PositiveInteger") -> "DiagnosticTestIdentifier":
        """
        AUTOSAR-compliant setter for uasId with method chaining.

        Args:
            value: The uasId to set

        Returns:
            self for method chaining

        Note:
            Delegates to uas_id property setter (gets validation automatically)
        """
        self.uas_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticTestIdentifier":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self

    def with_uas_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticTestIdentifier":
        """
        Set uasId and return self for chaining.

        Args:
            value: The uasId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uas_id("value")
        """
        self.uas_id = value  # Use property setter (gets validation)
        return self
