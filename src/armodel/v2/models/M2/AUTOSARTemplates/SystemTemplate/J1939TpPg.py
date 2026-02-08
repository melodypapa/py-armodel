from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class J1939TpPg(ARObject):
    """
    A J1939TpPg represents one J1939 message (parameter group, PG) identified by
    the PGN (parameter group number) that can be received or transmitted via
    J1939Tp.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 625, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # In case of variable length IPdus (with system signals of an additional NPdu
        # (with the PGN in the is used for messages with up to 8 bytes.
        self._directPdu: Optional["NPdu"] = None

    @property
    def direct_pdu(self) -> Optional["NPdu"]:
        """Get directPdu (Pythonic accessor)."""
        return self._directPdu

    @direct_pdu.setter
    def direct_pdu(self, value: Optional["NPdu"]) -> None:
        """
        Set directPdu with validation.

        Args:
            value: The directPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._directPdu = None
            return

        if not isinstance(value, NPdu):
            raise TypeError(
                f"directPdu must be NPdu or None, got {type(value).__name__}"
            )
        self._directPdu = value
        # Parameter group number (PGN) of a J1939 message PG) that can be received or
                # J1939Tp.
        # The PGN may be omitted when directPdu is referenced and is mapped into a Can
                # an identifier.
        self._pgn: Optional["Integer"] = None

    @property
    def pgn(self) -> Optional["Integer"]:
        """Get pgn (Pythonic accessor)."""
        return self._pgn

    @pgn.setter
    def pgn(self, value: Optional["Integer"]) -> None:
        """
        Set pgn with validation.

        Args:
            value: The pgn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pgn = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"pgn must be Integer or None, got {type(value).__name__}"
            )
        self._pgn = value
        # Parameter Group can be triggered by the J1939 request 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._requestable: Optional["Boolean"] = None

    @property
    def requestable(self) -> Optional["Boolean"]:
        """Get requestable (Pythonic accessor)."""
        return self._requestable

    @requestable.setter
    def requestable(self, value: Optional["Boolean"]) -> None:
        """
        Set requestable with validation.

        Args:
            value: The requestable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestable = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"requestable must be Boolean or None, got {type(value).__name__}"
            )
        self._requestable = value
        # Reference to IPdus that are segmented by the Transport more than one IPdu is
        # referenced, the IPdus when the same PGN is received in parallel via protocols
        # (BAM, CMDT, direct) on the.
        self._sdu: List["IPdu"] = []

    @property
    def sdu(self) -> List["IPdu"]:
        """Get sdu (Pythonic accessor)."""
        return self._sdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirectPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for directPdu.

        Returns:
            The directPdu value

        Note:
            Delegates to direct_pdu property (CODING_RULE_V2_00017)
        """
        return self.direct_pdu  # Delegates to property

    def setDirectPdu(self, value: "NPdu") -> "J1939TpPg":
        """
        AUTOSAR-compliant setter for directPdu with method chaining.

        Args:
            value: The directPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to direct_pdu property setter (gets validation automatically)
        """
        self.direct_pdu = value  # Delegates to property setter
        return self

    def getPgn(self) -> "Integer":
        """
        AUTOSAR-compliant getter for pgn.

        Returns:
            The pgn value

        Note:
            Delegates to pgn property (CODING_RULE_V2_00017)
        """
        return self.pgn  # Delegates to property

    def setPgn(self, value: "Integer") -> "J1939TpPg":
        """
        AUTOSAR-compliant setter for pgn with method chaining.

        Args:
            value: The pgn to set

        Returns:
            self for method chaining

        Note:
            Delegates to pgn property setter (gets validation automatically)
        """
        self.pgn = value  # Delegates to property setter
        return self

    def getRequestable(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for requestable.

        Returns:
            The requestable value

        Note:
            Delegates to requestable property (CODING_RULE_V2_00017)
        """
        return self.requestable  # Delegates to property

    def setRequestable(self, value: "Boolean") -> "J1939TpPg":
        """
        AUTOSAR-compliant setter for requestable with method chaining.

        Args:
            value: The requestable to set

        Returns:
            self for method chaining

        Note:
            Delegates to requestable property setter (gets validation automatically)
        """
        self.requestable = value  # Delegates to property setter
        return self

    def getSdu(self) -> List["IPdu"]:
        """
        AUTOSAR-compliant getter for sdu.

        Returns:
            The sdu value

        Note:
            Delegates to sdu property (CODING_RULE_V2_00017)
        """
        return self.sdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_direct_pdu(self, value: Optional["NPdu"]) -> "J1939TpPg":
        """
        Set directPdu and return self for chaining.

        Args:
            value: The directPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direct_pdu("value")
        """
        self.direct_pdu = value  # Use property setter (gets validation)
        return self

    def with_pgn(self, value: Optional["Integer"]) -> "J1939TpPg":
        """
        Set pgn and return self for chaining.

        Args:
            value: The pgn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pgn("value")
        """
        self.pgn = value  # Use property setter (gets validation)
        return self

    def with_requestable(self, value: Optional["Boolean"]) -> "J1939TpPg":
        """
        Set requestable and return self for chaining.

        Args:
            value: The requestable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requestable("value")
        """
        self.requestable = value  # Use property setter (gets validation)
        return self
