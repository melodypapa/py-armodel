from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DiagnosticParameterSupportInfo(ARObject):
    """
    This represents a way to define which bit of the supportInfo is representing
    this part of the PID

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticParameterSupportInfo

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 149, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # defines the bit in the SupportInfo byte, which represents DataElement pidSize
                # / position / size.
        # Unit: byte.
        self._supportInfoBit: Optional["PositiveInteger"] = None

    @property
    def support_info_bit(self) -> Optional["PositiveInteger"]:
        """Get supportInfoBit (Pythonic accessor)."""
        return self._supportInfoBit

    @support_info_bit.setter
    def support_info_bit(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set supportInfoBit with validation.

        Args:
            value: The supportInfoBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supportInfoBit = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"supportInfoBit must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._supportInfoBit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSupportInfoBit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for supportInfoBit.

        Returns:
            The supportInfoBit value

        Note:
            Delegates to support_info_bit property (CODING_RULE_V2_00017)
        """
        return self.support_info_bit  # Delegates to property

    def setSupportInfoBit(self, value: "PositiveInteger") -> "DiagnosticParameterSupportInfo":
        """
        AUTOSAR-compliant setter for supportInfoBit with method chaining.

        Args:
            value: The supportInfoBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to support_info_bit property setter (gets validation automatically)
        """
        self.support_info_bit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_support_info_bit(self, value: Optional["PositiveInteger"]) -> "DiagnosticParameterSupportInfo":
        """
        Set supportInfoBit and return self for chaining.

        Args:
            value: The supportInfoBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_support_info_bit("value")
        """
        self.support_info_bit = value  # Use property setter (gets validation)
        return self
