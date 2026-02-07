from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class J1939TpNode(Identifiable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to
    the Topology description.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::J1939TpNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 626, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to a CommunicationConnector in the description.
        # In a System Description this mandatory.
        # In an ECU Extract this reference (references to ECUs that are not part of the
                # shall be avoided).
        self._connector: Optional["Communication"] = None

    @property
    def connector(self) -> Optional["Communication"]:
        """Get connector (Pythonic accessor)."""
        return self._connector

    @connector.setter
    def connector(self, value: Optional["Communication"]) -> None:
        """
        Set connector with validation.

        Args:
            value: The connector to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connector = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"connector must be Communication or None, got {type(value).__name__}"
            )
        self._connector = value
        # Reference to the TP Address that is used by the TpNode.
        # is optional only when no TP is sent and is received.
        self._tpAddress: Optional["TpAddress"] = None

    @property
    def tp_address(self) -> Optional["TpAddress"]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional["TpAddress"]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, TpAddress):
            raise TypeError(
                f"tpAddress must be TpAddress or None, got {type(value).__name__}"
            )
        self._tpAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnector(self) -> "Communication":
        """
        AUTOSAR-compliant getter for connector.

        Returns:
            The connector value

        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def setConnector(self, value: "Communication") -> "J1939TpNode":
        """
        AUTOSAR-compliant setter for connector with method chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Note:
            Delegates to connector property setter (gets validation automatically)
        """
        self.connector = value  # Delegates to property setter
        return self

    def getTpAddress(self) -> "TpAddress":
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: "TpAddress") -> "J1939TpNode":
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connector(self, value: Optional["Communication"]) -> "J1939TpNode":
        """
        Set connector and return self for chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connector("value")
        """
        self.connector = value  # Use property setter (gets validation)
        return self

    def with_tp_address(self, value: Optional["TpAddress"]) -> "J1939TpNode":
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self
