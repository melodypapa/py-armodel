from typing import List, Optional


class DiagnosticSecureCodingMapping(DiagnosticMapping):
    """
    This meta-class acts a mapping element to select diagnostic service
    instances that are used in the secure coding procedure. Besides, there are
    already defined diagnostic capabilities they furthermore have a additional
    semantics that is used during the secure coding process. In particular, this
    class references write data by identifier instances that mandatory require a
    secure coding and this class references a diagnostic routine control that is
    used to provide the signature and to persist the data in non-volatile
    memory.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticSecureCodingMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 312, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refer to write data by identifier instances that have the to be a secure
        # coding DID.
        self._dataIdentifier: List["DiagnosticWriteDataBy"] = []

    @property
    def data_identifier(self) -> List["DiagnosticWriteDataBy"]:
        """Get dataIdentifier (Pythonic accessor)."""
        return self._dataIdentifier
        # Refer to a routine control that is used to authenticate and secure coding
        # data.
        self._validation: Optional["DiagnosticStartRoutine"] = None

    @property
    def validation(self) -> Optional["DiagnosticStartRoutine"]:
        """Get validation (Pythonic accessor)."""
        return self._validation

    @validation.setter
    def validation(self, value: Optional["DiagnosticStartRoutine"]) -> None:
        """
        Set validation with validation.

        Args:
            value: The validation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._validation = None
            return

        if not isinstance(value, DiagnosticStartRoutine):
            raise TypeError(
                f"validation must be DiagnosticStartRoutine or None, got {type(value).__name__}"
            )
        self._validation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataIdentifier(self) -> List["DiagnosticWriteDataBy"]:
        """
        AUTOSAR-compliant getter for dataIdentifier.

        Returns:
            The dataIdentifier value

        Note:
            Delegates to data_identifier property (CODING_RULE_V2_00017)
        """
        return self.data_identifier  # Delegates to property

    def getValidation(self) -> "DiagnosticStartRoutine":
        """
        AUTOSAR-compliant getter for validation.

        Returns:
            The validation value

        Note:
            Delegates to validation property (CODING_RULE_V2_00017)
        """
        return self.validation  # Delegates to property

    def setValidation(self, value: "DiagnosticStartRoutine") -> "DiagnosticSecureCodingMapping":
        """
        AUTOSAR-compliant setter for validation with method chaining.

        Args:
            value: The validation to set

        Returns:
            self for method chaining

        Note:
            Delegates to validation property setter (gets validation automatically)
        """
        self.validation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_validation(self, value: Optional["DiagnosticStartRoutine"]) -> "DiagnosticSecureCodingMapping":
        """
        Set validation and return self for chaining.

        Args:
            value: The validation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_validation("value")
        """
        self.validation = value  # Use property setter (gets validation)
        return self
