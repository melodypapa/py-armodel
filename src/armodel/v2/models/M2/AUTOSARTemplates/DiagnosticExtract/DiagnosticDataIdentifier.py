from typing import List, Optional


class DiagnosticDataIdentifier(DiagnosticAbstractDataIdentifier):
    """
    This meta-class represents the ability to model a diagnostic data identifier
    (DID) that is fully specified regarding the payload at configuration-time.
    (cid:53) 33 of 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate
    Diagnostic Extract Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticDataIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 33, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the dataElement associated with the Diagnostic atpVariation.
        self._dataElement: List["DiagnosticParameter"] = []

    @property
    def data_element(self) -> List["DiagnosticParameter"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement
        # This attribute indicates the size in bytes of the Diagnostic.
        self._didSize: Optional["PositiveInteger"] = None

    @property
    def did_size(self) -> Optional["PositiveInteger"]:
        """Get didSize (Pythonic accessor)."""
        return self._didSize

    @did_size.setter
    def did_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set didSize with validation.

        Args:
            value: The didSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._didSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"didSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._didSize = value
        # This attributes indicates whether the specific Diagnostic the vehicle
        # identification.
        self._representsVin: Optional["Boolean"] = None

    @property
    def represents_vin(self) -> Optional["Boolean"]:
        """Get representsVin (Pythonic accessor)."""
        return self._representsVin

    @represents_vin.setter
    def represents_vin(self, value: Optional["Boolean"]) -> None:
        """
        Set representsVin with validation.

        Args:
            value: The representsVin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._representsVin = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"representsVin must be Boolean or None, got {type(value).__name__}"
            )
        self._representsVin = value
        # This attribute represents the supported information with the
        # DiagnosticDataIdentifier.
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

    def getDidSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for didSize.

        Returns:
            The didSize value

        Note:
            Delegates to did_size property (CODING_RULE_V2_00017)
        """
        return self.did_size  # Delegates to property

    def setDidSize(self, value: "PositiveInteger") -> "DiagnosticDataIdentifier":
        """
        AUTOSAR-compliant setter for didSize with method chaining.

        Args:
            value: The didSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to did_size property setter (gets validation automatically)
        """
        self.did_size = value  # Delegates to property setter
        return self

    def getRepresentsVin(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for representsVin.

        Returns:
            The representsVin value

        Note:
            Delegates to represents_vin property (CODING_RULE_V2_00017)
        """
        return self.represents_vin  # Delegates to property

    def setRepresentsVin(self, value: "Boolean") -> "DiagnosticDataIdentifier":
        """
        AUTOSAR-compliant setter for representsVin with method chaining.

        Args:
            value: The representsVin to set

        Returns:
            self for method chaining

        Note:
            Delegates to represents_vin property setter (gets validation automatically)
        """
        self.represents_vin = value  # Delegates to property setter
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

    def setSupportInfoByte(self, value: "DiagnosticSupportInfo") -> "DiagnosticDataIdentifier":
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

    def with_did_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticDataIdentifier":
        """
        Set didSize and return self for chaining.

        Args:
            value: The didSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_did_size("value")
        """
        self.did_size = value  # Use property setter (gets validation)
        return self

    def with_represents_vin(self, value: Optional["Boolean"]) -> "DiagnosticDataIdentifier":
        """
        Set representsVin and return self for chaining.

        Args:
            value: The representsVin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_represents_vin("value")
        """
        self.represents_vin = value  # Use property setter (gets validation)
        return self

    def with_support_info_byte(self, value: Optional["DiagnosticSupportInfo"]) -> "DiagnosticDataIdentifier":
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
