from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class LinTpNode(Identifiable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to
    the Topology description.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 614, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to a CommunicationConnector in the description.
        # System Description this reference is mandatory.
        # In Extract this reference is optional (references to are not part of the ECU
                # Extract shall be.
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
        # Configures if TP Frames of not requested LIN-Slaves are or not.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._dropNot: Optional["Boolean"] = None

    @property
    def drop_not(self) -> Optional["Boolean"]:
        """Get dropNot (Pythonic accessor)."""
        return self._dropNot

    @drop_not.setter
    def drop_not(self, value: Optional["Boolean"]) -> None:
        """
        Set dropNot with validation.

        Args:
            value: The dropNot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dropNot = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"dropNot must be Boolean or None, got {type(value).__name__}"
            )
        self._dropNot = value
        # Configures the maximum number of allowed response frames.
        self._maxNumberOf: Optional["Integer"] = None

    @property
    def max_number_of(self) -> Optional["Integer"]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional["Integer"]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxNumberOf must be Integer or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # After reception of a response pending frame the P2 is reloaded with the
        # timeout time P2max.
        self._p2Max: Optional["TimeValue"] = None

    @property
    def p2_max(self) -> Optional["TimeValue"]:
        """Get p2Max (Pythonic accessor)."""
        return self._p2Max

    @p2_max.setter
    def p2_max(self, value: Optional["TimeValue"]) -> None:
        """
        Set p2Max with validation.

        Args:
            value: The p2Max to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._p2Max = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"p2Max must be TimeValue or None, got {type(value).__name__}"
            )
        self._p2Max = value
        # P2 timeout observation parameter.
        self._p2Timing: Optional["TimeValue"] = None

    @property
    def p2_timing(self) -> Optional["TimeValue"]:
        """Get p2Timing (Pythonic accessor)."""
        return self._p2Timing

    @p2_timing.setter
    def p2_timing(self, value: Optional["TimeValue"]) -> None:
        """
        Set p2Timing with validation.

        Args:
            value: The p2Timing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._p2Timing = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"p2Timing must be TimeValue or None, got {type(value).__name__}"
            )
        self._p2Timing = value
        # Reference to the TP Address that is used by the TpNode.
        # is optional in case that the multicast TP used (reference from TpConnection).
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

    def setConnector(self, value: "Communication") -> "LinTpNode":
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

    def getDropNot(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for dropNot.

        Returns:
            The dropNot value

        Note:
            Delegates to drop_not property (CODING_RULE_V2_00017)
        """
        return self.drop_not  # Delegates to property

    def setDropNot(self, value: "Boolean") -> "LinTpNode":
        """
        AUTOSAR-compliant setter for dropNot with method chaining.

        Args:
            value: The dropNot to set

        Returns:
            self for method chaining

        Note:
            Delegates to drop_not property setter (gets validation automatically)
        """
        self.drop_not = value  # Delegates to property setter
        return self

    def getMaxNumberOf(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "Integer") -> "LinTpNode":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getP2Max(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for p2Max.

        Returns:
            The p2Max value

        Note:
            Delegates to p2_max property (CODING_RULE_V2_00017)
        """
        return self.p2_max  # Delegates to property

    def setP2Max(self, value: "TimeValue") -> "LinTpNode":
        """
        AUTOSAR-compliant setter for p2Max with method chaining.

        Args:
            value: The p2Max to set

        Returns:
            self for method chaining

        Note:
            Delegates to p2_max property setter (gets validation automatically)
        """
        self.p2_max = value  # Delegates to property setter
        return self

    def getP2Timing(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for p2Timing.

        Returns:
            The p2Timing value

        Note:
            Delegates to p2_timing property (CODING_RULE_V2_00017)
        """
        return self.p2_timing  # Delegates to property

    def setP2Timing(self, value: "TimeValue") -> "LinTpNode":
        """
        AUTOSAR-compliant setter for p2Timing with method chaining.

        Args:
            value: The p2Timing to set

        Returns:
            self for method chaining

        Note:
            Delegates to p2_timing property setter (gets validation automatically)
        """
        self.p2_timing = value  # Delegates to property setter
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

    def setTpAddress(self, value: "TpAddress") -> "LinTpNode":
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

    def with_connector(self, value: Optional["Communication"]) -> "LinTpNode":
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

    def with_drop_not(self, value: Optional["Boolean"]) -> "LinTpNode":
        """
        Set dropNot and return self for chaining.

        Args:
            value: The dropNot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_drop_not("value")
        """
        self.drop_not = value  # Use property setter (gets validation)
        return self

    def with_max_number_of(self, value: Optional["Integer"]) -> "LinTpNode":
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_p2_max(self, value: Optional["TimeValue"]) -> "LinTpNode":
        """
        Set p2Max and return self for chaining.

        Args:
            value: The p2Max to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_p2_max("value")
        """
        self.p2_max = value  # Use property setter (gets validation)
        return self

    def with_p2_timing(self, value: Optional["TimeValue"]) -> "LinTpNode":
        """
        Set p2Timing and return self for chaining.

        Args:
            value: The p2Timing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_p2_timing("value")
        """
        self.p2_timing = value  # Use property setter (gets validation)
        return self

    def with_tp_address(self, value: Optional["TpAddress"]) -> "LinTpNode":
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
