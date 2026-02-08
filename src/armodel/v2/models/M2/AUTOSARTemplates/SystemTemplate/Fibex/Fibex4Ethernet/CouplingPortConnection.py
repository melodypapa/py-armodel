from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CouplingPortConnection(ARObject):
    """
    Connection between two CouplingPorts (firstPort and secondPort) or between a
    collection of Ports that are all referenced by the portCollection reference.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 112, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the first CouplingPort that is connected via 2090 Document ID
        # 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._firstPort: Optional["CouplingPort"] = None

    @property
    def first_port(self) -> Optional["CouplingPort"]:
        """Get firstPort (Pythonic accessor)."""
        return self._firstPort

    @first_port.setter
    def first_port(self, value: Optional["CouplingPort"]) -> None:
        """
        Set firstPort with validation.

        Args:
            value: The firstPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstPort = None
            return

        if not isinstance(value, CouplingPort):
            raise TypeError(
                f"firstPort must be CouplingPort or None, got {type(value).__name__}"
            )
        self._firstPort = value
        # Reference to a number of CouplingPorts that are the CouplingPortConnection.
        # This be used to describe a 10BASE-T1S where several CouplingPorts of
                # connected via atpVariation.
        self._nodePort: List["CouplingPort"] = []

    @property
    def node_port(self) -> List["CouplingPort"]:
        """Get nodePort (Pythonic accessor)."""
        return self._nodePort
        # Defines the number of communication participants in 10BASE-T1S and the
        # nodePort reference is used.
        self._plcaLocalNode: Optional["PositiveInteger"] = None

    @property
    def plca_local_node(self) -> Optional["PositiveInteger"]:
        """Get plcaLocalNode (Pythonic accessor)."""
        return self._plcaLocalNode

    @plca_local_node.setter
    def plca_local_node(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set plcaLocalNode with validation.

        Args:
            value: The plcaLocalNode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._plcaLocalNode = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"plcaLocalNode must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._plcaLocalNode = value
        # Timer for the transmission in bit time to evaluate if a Opportunity is yield
        # or not.
        self._plcaTransmit: Optional["PositiveInteger"] = None

    @property
    def plca_transmit(self) -> Optional["PositiveInteger"]:
        """Get plcaTransmit (Pythonic accessor)."""
        return self._plcaTransmit

    @plca_transmit.setter
    def plca_transmit(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set plcaTransmit with validation.

        Args:
            value: The plcaTransmit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._plcaTransmit = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"plcaTransmit must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._plcaTransmit = value
        # Reference to the second CouplingPort that is connected
        # CouplingPortConnection.
        self._secondPort: Optional["CouplingPort"] = None

    @property
    def second_port(self) -> Optional["CouplingPort"]:
        """Get secondPort (Pythonic accessor)."""
        return self._secondPort

    @second_port.setter
    def second_port(self, value: Optional["CouplingPort"]) -> None:
        """
        Set secondPort with validation.

        Args:
            value: The secondPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondPort = None
            return

        if not isinstance(value, CouplingPort):
            raise TypeError(
                f"secondPort must be CouplingPort or None, got {type(value).__name__}"
            )
        self._secondPort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstPort(self) -> "CouplingPort":
        """
        AUTOSAR-compliant getter for firstPort.

        Returns:
            The firstPort value

        Note:
            Delegates to first_port property (CODING_RULE_V2_00017)
        """
        return self.first_port  # Delegates to property

    def setFirstPort(self, value: "CouplingPort") -> "CouplingPortConnection":
        """
        AUTOSAR-compliant setter for firstPort with method chaining.

        Args:
            value: The firstPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_port property setter (gets validation automatically)
        """
        self.first_port = value  # Delegates to property setter
        return self

    def getNodePort(self) -> List["CouplingPort"]:
        """
        AUTOSAR-compliant getter for nodePort.

        Returns:
            The nodePort value

        Note:
            Delegates to node_port property (CODING_RULE_V2_00017)
        """
        return self.node_port  # Delegates to property

    def getPlcaLocalNode(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for plcaLocalNode.

        Returns:
            The plcaLocalNode value

        Note:
            Delegates to plca_local_node property (CODING_RULE_V2_00017)
        """
        return self.plca_local_node  # Delegates to property

    def setPlcaLocalNode(self, value: "PositiveInteger") -> "CouplingPortConnection":
        """
        AUTOSAR-compliant setter for plcaLocalNode with method chaining.

        Args:
            value: The plcaLocalNode to set

        Returns:
            self for method chaining

        Note:
            Delegates to plca_local_node property setter (gets validation automatically)
        """
        self.plca_local_node = value  # Delegates to property setter
        return self

    def getPlcaTransmit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for plcaTransmit.

        Returns:
            The plcaTransmit value

        Note:
            Delegates to plca_transmit property (CODING_RULE_V2_00017)
        """
        return self.plca_transmit  # Delegates to property

    def setPlcaTransmit(self, value: "PositiveInteger") -> "CouplingPortConnection":
        """
        AUTOSAR-compliant setter for plcaTransmit with method chaining.

        Args:
            value: The plcaTransmit to set

        Returns:
            self for method chaining

        Note:
            Delegates to plca_transmit property setter (gets validation automatically)
        """
        self.plca_transmit = value  # Delegates to property setter
        return self

    def getSecondPort(self) -> "CouplingPort":
        """
        AUTOSAR-compliant getter for secondPort.

        Returns:
            The secondPort value

        Note:
            Delegates to second_port property (CODING_RULE_V2_00017)
        """
        return self.second_port  # Delegates to property

    def setSecondPort(self, value: "CouplingPort") -> "CouplingPortConnection":
        """
        AUTOSAR-compliant setter for secondPort with method chaining.

        Args:
            value: The secondPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_port property setter (gets validation automatically)
        """
        self.second_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_port(self, value: Optional["CouplingPort"]) -> "CouplingPortConnection":
        """
        Set firstPort and return self for chaining.

        Args:
            value: The firstPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_port("value")
        """
        self.first_port = value  # Use property setter (gets validation)
        return self

    def with_plca_local_node(self, value: Optional["PositiveInteger"]) -> "CouplingPortConnection":
        """
        Set plcaLocalNode and return self for chaining.

        Args:
            value: The plcaLocalNode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_plca_local_node("value")
        """
        self.plca_local_node = value  # Use property setter (gets validation)
        return self

    def with_plca_transmit(self, value: Optional["PositiveInteger"]) -> "CouplingPortConnection":
        """
        Set plcaTransmit and return self for chaining.

        Args:
            value: The plcaTransmit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_plca_transmit("value")
        """
        self.plca_transmit = value  # Use property setter (gets validation)
        return self

    def with_second_port(self, value: Optional["CouplingPort"]) -> "CouplingPortConnection":
        """
        Set secondPort and return self for chaining.

        Args:
            value: The secondPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_port("value")
        """
        self.second_port = value  # Use property setter (gets validation)
        return self
