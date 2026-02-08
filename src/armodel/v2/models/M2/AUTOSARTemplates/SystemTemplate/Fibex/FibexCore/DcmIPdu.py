from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    IPdu,
)


class DcmIPdu(IPdu):
    """
    Represents the IPdus handled by Dcm.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 343, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Attribute is used to distinguish a request from a response.
        self._diagPduType: Optional["DiagPduType"] = None

    @property
    def diag_pdu_type(self) -> Optional["DiagPduType"]:
        """Get diagPduType (Pythonic accessor)."""
        return self._diagPduType

    @diag_pdu_type.setter
    def diag_pdu_type(self, value: Optional["DiagPduType"]) -> None:
        """
        Set diagPduType with validation.

        Args:
            value: The diagPduType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagPduType = None
            return

        if not isinstance(value, DiagPduType):
            raise TypeError(
                f"diagPduType must be DiagPduType or None, got {type(value).__name__}"
            )
        self._diagPduType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagPduType(self) -> "DiagPduType":
        """
        AUTOSAR-compliant getter for diagPduType.

        Returns:
            The diagPduType value

        Note:
            Delegates to diag_pdu_type property (CODING_RULE_V2_00017)
        """
        return self.diag_pdu_type  # Delegates to property

    def setDiagPduType(self, value: "DiagPduType") -> "DcmIPdu":
        """
        AUTOSAR-compliant setter for diagPduType with method chaining.

        Args:
            value: The diagPduType to set

        Returns:
            self for method chaining

        Note:
            Delegates to diag_pdu_type property setter (gets validation automatically)
        """
        self.diag_pdu_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diag_pdu_type(self, value: Optional["DiagPduType"]) -> "DcmIPdu":
        """
        Set diagPduType and return self for chaining.

        Args:
            value: The diagPduType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diag_pdu_type("value")
        """
        self.diag_pdu_type = value  # Use property setter (gets validation)
        return self
