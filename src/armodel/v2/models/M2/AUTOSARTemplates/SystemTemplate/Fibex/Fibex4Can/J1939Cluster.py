from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class J1939Cluster(ARObject):
    """
    J1939 specific cluster attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::J1939Cluster

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 321, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 78, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the network ID for the J1939 cluster.
        self._networkId: Optional["PositiveInteger"] = None

    @property
    def network_id(self) -> Optional["PositiveInteger"]:
        """Get networkId (Pythonic accessor)."""
        return self._networkId

    @network_id.setter
    def network_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set networkId with validation.

        Args:
            value: The networkId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._networkId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"networkId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._networkId = value
        # Enables support for the Request2 PGN (RQST2).
        self._re-: Optional["Boolean"] = None

    @property
    def re-(self) -> Optional["Boolean"]:
        """Get re- (Pythonic accessor)."""
        return self._re-

    @re-.setter
    def re-(self, value: Optional["Boolean"]) -> None:
        """
        Set re- with validation.

        Args:
            value: The re- to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._re- = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"re- must be Boolean or None, got {type(value).__name__}"
            )
        self._re- = value
        # Defines whether the nodes attached to this channel use initial address claim,
                # and whether they react to claims of other nodes.
        # initial address claim is sent, and the node address claims of other nodes.
        # node only sends an address claim upon does not care for contending address
                # claims.
        self._usesAddress: Optional["Boolean"] = None

    @property
    def uses_address(self) -> Optional["Boolean"]:
        """Get usesAddress (Pythonic accessor)."""
        return self._usesAddress

    @uses_address.setter
    def uses_address(self, value: Optional["Boolean"]) -> None:
        """
        Set usesAddress with validation.

        Args:
            value: The usesAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usesAddress = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"usesAddress must be Boolean or None, got {type(value).__name__}"
            )
        self._usesAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNetworkId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for networkId.

        Returns:
            The networkId value

        Note:
            Delegates to network_id property (CODING_RULE_V2_00017)
        """
        return self.network_id  # Delegates to property

    def setNetworkId(self, value: "PositiveInteger") -> "J1939Cluster":
        """
        AUTOSAR-compliant setter for networkId with method chaining.

        Args:
            value: The networkId to set

        Returns:
            self for method chaining

        Note:
            Delegates to network_id property setter (gets validation automatically)
        """
        self.network_id = value  # Delegates to property setter
        return self

    def getRe-(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for re-.

        Returns:
            The re- value

        Note:
            Delegates to re- property (CODING_RULE_V2_00017)
        """
        return self.re-  # Delegates to property

    def setRe-(self, value: "Boolean") -> "J1939Cluster":
        """
        AUTOSAR-compliant setter for re- with method chaining.

        Args:
            value: The re- to set

        Returns:
            self for method chaining

        Note:
            Delegates to re- property setter (gets validation automatically)
        """
        self.re- = value  # Delegates to property setter
        return self

    def getUsesAddress(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for usesAddress.

        Returns:
            The usesAddress value

        Note:
            Delegates to uses_address property (CODING_RULE_V2_00017)
        """
        return self.uses_address  # Delegates to property

    def setUsesAddress(self, value: "Boolean") -> "J1939Cluster":
        """
        AUTOSAR-compliant setter for usesAddress with method chaining.

        Args:
            value: The usesAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to uses_address property setter (gets validation automatically)
        """
        self.uses_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_network_id(self, value: Optional["PositiveInteger"]) -> "J1939Cluster":
        """
        Set networkId and return self for chaining.

        Args:
            value: The networkId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network_id("value")
        """
        self.network_id = value  # Use property setter (gets validation)
        return self

    def with_re-(self, value: Optional["Boolean"]) -> "J1939Cluster":
        """
        Set re- and return self for chaining.

        Args:
            value: The re- to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_re-("value")
        """
        self.re- = value  # Use property setter (gets validation)
        return self

    def with_uses_address(self, value: Optional["Boolean"]) -> "J1939Cluster":
        """
        Set usesAddress and return self for chaining.

        Args:
            value: The usesAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uses_address("value")
        """
        self.uses_address = value  # Use property setter (gets validation)
        return self
