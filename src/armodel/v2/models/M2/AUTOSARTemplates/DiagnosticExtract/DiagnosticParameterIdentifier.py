from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)


class DiagnosticParameterIdentifier(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a diagnostic parameter
    identifier (PID) for the purpose of executing on-board diagnostics (OBD).

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 149, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the data carried by the Diagnostic atpVariation.
        self._dataElement: List["DiagnosticParameter"] = []

    @property
    def data_element(self) -> List["DiagnosticParameter"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement
        # This is the numerical identifier used to identify the the scope of diagnostic
        # SAE J1979-DA).
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
        # The size of the entire PID can be greater than the sum of elements because
        # padding might be applied.
        self._pidSize: Optional["PositiveInteger"] = None

    @property
    def pid_size(self) -> Optional["PositiveInteger"]:
        """Get pidSize (Pythonic accessor)."""
        return self._pidSize

    @pid_size.setter
    def pid_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pidSize with validation.

        Args:
            value: The pidSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pidSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pidSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pidSize = value
        # This represents the supported information associated the
        # DiagnosticParameterIdentifier.
        self._supportInfoByte: Optional["DiagnosticSupportInfo"] = None

    @property
    def support_info_byte(self) -> Optional["DiagnosticSupportInfo"]:
        """Get supportInfoByte (Pythonic accessor)."""
        return self._supportInfoByte

    @support_info_byte.setter
    def support_info_byte(self, value: Optional["DiagnosticSupportInfo"]) -> None:
        """
        Set supportInfoByte with validation.

        Args:
            value: The supportInfoByte to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supportInfoByte = None
            return

        if not isinstance(value, DiagnosticSupportInfo):
            raise TypeError(
                f"supportInfoByte must be DiagnosticSupportInfo or None, got {type(value).__name__}"
            )
        self._supportInfoByte = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticParameterIdentifier":
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

    def getPidSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pidSize.

        Returns:
            The pidSize value

        Note:
            Delegates to pid_size property (CODING_RULE_V2_00017)
        """
        return self.pid_size  # Delegates to property

    def setPidSize(self, value: "PositiveInteger") -> "DiagnosticParameterIdentifier":
        """
        AUTOSAR-compliant setter for pidSize with method chaining.

        Args:
            value: The pidSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to pid_size property setter (gets validation automatically)
        """
        self.pid_size = value  # Delegates to property setter
        return self

    def getSupportInfoByte(self) -> "DiagnosticSupportInfo":
        """
        AUTOSAR-compliant getter for supportInfoByte.

        Returns:
            The supportInfoByte value

        Note:
            Delegates to support_info_byte property (CODING_RULE_V2_00017)
        """
        return self.support_info_byte  # Delegates to property

    def setSupportInfoByte(self, value: "DiagnosticSupportInfo") -> "DiagnosticParameterIdentifier":
        """
        AUTOSAR-compliant setter for supportInfoByte with method chaining.

        Args:
            value: The supportInfoByte to set

        Returns:
            self for method chaining

        Note:
            Delegates to support_info_byte property setter (gets validation automatically)
        """
        self.support_info_byte = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticParameterIdentifier":
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

    def with_pid_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticParameterIdentifier":
        """
        Set pidSize and return self for chaining.

        Args:
            value: The pidSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pid_size("value")
        """
        self.pid_size = value  # Use property setter (gets validation)
        return self

    def with_support_info_byte(self, value: Optional["DiagnosticSupportInfo"]) -> "DiagnosticParameterIdentifier":
        """
        Set supportInfoByte and return self for chaining.

        Args:
            value: The supportInfoByte to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_support_info_byte("value")
        """
        self.support_info_byte = value  # Use property setter (gets validation)
        return self
