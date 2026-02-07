from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwitchStreamIdentification(Identifiable):
    """
    SwitchStreamIdentification
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchStreamIdentification
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 135, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the CouplingPort to be taken into account as role for this
        # SwitchStreamIdentification.
        self._egressPort: List["CouplingPort"] = []

    @property
    def egress_port(self) -> List["CouplingPort"]:
        """Get egressPort (Pythonic accessor)."""
        return self._egressPort
        # Enables Blocking all frames from the MAC address.
        # atp.
        # Status=candidate.
        self._filterActionBlock: Optional["Boolean"] = None

    @property
    def filter_action_block(self) -> Optional["Boolean"]:
        """Get filterActionBlock (Pythonic accessor)."""
        return self._filterActionBlock

    @filter_action_block.setter
    def filter_action_block(self, value: Optional["Boolean"]) -> None:
        """
        Set filterActionBlock with validation.
        
        Args:
            value: The filterActionBlock to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterActionBlock = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"filterActionBlock must be Boolean or None, got {type(value).__name__}"
            )
        self._filterActionBlock = value
        # Defines the action to modify the destination port(s) determined by the frame
        # forwarding process for an Ethernet frame.
        self._filterActionDest: Optional["SwitchStreamFilter"] = None

    @property
    def filter_action_dest(self) -> Optional["SwitchStreamFilter"]:
        """Get filterActionDest (Pythonic accessor)."""
        return self._filterActionDest

    @filter_action_dest.setter
    def filter_action_dest(self, value: Optional["SwitchStreamFilter"]) -> None:
        """
        Set filterActionDest with validation.
        
        Args:
            value: The filterActionDest to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterActionDest = None
            return

        if not isinstance(value, SwitchStreamFilter):
            raise TypeError(
                f"filterActionDest must be SwitchStreamFilter or None, got {type(value).__name__}"
            )
        self._filterActionDest = value
        # Enables Drop Frame action.
        # atp.
        # Status=candidate.
        self._filterActionDrop: Optional["Boolean"] = None

    @property
    def filter_action_drop(self) -> Optional["Boolean"]:
        """Get filterActionDrop (Pythonic accessor)."""
        return self._filterActionDrop

    @filter_action_drop.setter
    def filter_action_drop(self, value: Optional["Boolean"]) -> None:
        """
        Set filterActionDrop with validation.
        
        Args:
            value: The filterActionDrop to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterActionDrop = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"filterActionDrop must be Boolean or None, got {type(value).__name__}"
            )
        self._filterActionDrop = value
        # Defines the action to modify the VLAN-ID within a VLAN of an Ethernet frame.
        self._filterActionVlan: Optional["PositiveInteger"] = None

    @property
    def filter_action_vlan(self) -> Optional["PositiveInteger"]:
        """Get filterActionVlan (Pythonic accessor)."""
        return self._filterActionVlan

    @filter_action_vlan.setter
    def filter_action_vlan(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set filterActionVlan with validation.
        
        Args:
            value: The filterActionVlan to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterActionVlan = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"filterActionVlan must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._filterActionVlan = value
        # Reference to the CouplingPort to be taken into account as role for this
        # SwitchStreamIdentification.
        self._ingressPort: List["CouplingPort"] = []

    @property
    def ingress_port(self) -> List["CouplingPort"]:
        """Get ingressPort (Pythonic accessor)."""
        return self._ingressPort
        # Definition of a stream filter rule for this SwitchStream.
        self._streamFilter: Optional["SwitchStreamFilterRule"] = None

    @property
    def stream_filter(self) -> Optional["SwitchStreamFilterRule"]:
        """Get streamFilter (Pythonic accessor)."""
        return self._streamFilter

    @stream_filter.setter
    def stream_filter(self, value: Optional["SwitchStreamFilterRule"]) -> None:
        """
        Set streamFilter with validation.
        
        Args:
            value: The streamFilter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._streamFilter = None
            return

        if not isinstance(value, SwitchStreamFilterRule):
            raise TypeError(
                f"streamFilter must be SwitchStreamFilterRule or None, got {type(value).__name__}"
            )
        self._streamFilter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEgressPort(self) -> List["CouplingPort"]:
        """
        AUTOSAR-compliant getter for egressPort.
        
        Returns:
            The egressPort value
        
        Note:
            Delegates to egress_port property (CODING_RULE_V2_00017)
        """
        return self.egress_port  # Delegates to property

    def getFilterActionBlock(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for filterActionBlock.
        
        Returns:
            The filterActionBlock value
        
        Note:
            Delegates to filter_action_block property (CODING_RULE_V2_00017)
        """
        return self.filter_action_block  # Delegates to property

    def setFilterActionBlock(self, value: "Boolean") -> "SwitchStreamIdentification":
        """
        AUTOSAR-compliant setter for filterActionBlock with method chaining.
        
        Args:
            value: The filterActionBlock to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to filter_action_block property setter (gets validation automatically)
        """
        self.filter_action_block = value  # Delegates to property setter
        return self

    def getFilterActionDest(self) -> "SwitchStreamFilter":
        """
        AUTOSAR-compliant getter for filterActionDest.
        
        Returns:
            The filterActionDest value
        
        Note:
            Delegates to filter_action_dest property (CODING_RULE_V2_00017)
        """
        return self.filter_action_dest  # Delegates to property

    def setFilterActionDest(self, value: "SwitchStreamFilter") -> "SwitchStreamIdentification":
        """
        AUTOSAR-compliant setter for filterActionDest with method chaining.
        
        Args:
            value: The filterActionDest to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to filter_action_dest property setter (gets validation automatically)
        """
        self.filter_action_dest = value  # Delegates to property setter
        return self

    def getFilterActionDrop(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for filterActionDrop.
        
        Returns:
            The filterActionDrop value
        
        Note:
            Delegates to filter_action_drop property (CODING_RULE_V2_00017)
        """
        return self.filter_action_drop  # Delegates to property

    def setFilterActionDrop(self, value: "Boolean") -> "SwitchStreamIdentification":
        """
        AUTOSAR-compliant setter for filterActionDrop with method chaining.
        
        Args:
            value: The filterActionDrop to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to filter_action_drop property setter (gets validation automatically)
        """
        self.filter_action_drop = value  # Delegates to property setter
        return self

    def getFilterActionVlan(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for filterActionVlan.
        
        Returns:
            The filterActionVlan value
        
        Note:
            Delegates to filter_action_vlan property (CODING_RULE_V2_00017)
        """
        return self.filter_action_vlan  # Delegates to property

    def setFilterActionVlan(self, value: "PositiveInteger") -> "SwitchStreamIdentification":
        """
        AUTOSAR-compliant setter for filterActionVlan with method chaining.
        
        Args:
            value: The filterActionVlan to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to filter_action_vlan property setter (gets validation automatically)
        """
        self.filter_action_vlan = value  # Delegates to property setter
        return self

    def getIngressPort(self) -> List["CouplingPort"]:
        """
        AUTOSAR-compliant getter for ingressPort.
        
        Returns:
            The ingressPort value
        
        Note:
            Delegates to ingress_port property (CODING_RULE_V2_00017)
        """
        return self.ingress_port  # Delegates to property

    def getStreamFilter(self) -> "SwitchStreamFilterRule":
        """
        AUTOSAR-compliant getter for streamFilter.
        
        Returns:
            The streamFilter value
        
        Note:
            Delegates to stream_filter property (CODING_RULE_V2_00017)
        """
        return self.stream_filter  # Delegates to property

    def setStreamFilter(self, value: "SwitchStreamFilterRule") -> "SwitchStreamIdentification":
        """
        AUTOSAR-compliant setter for streamFilter with method chaining.
        
        Args:
            value: The streamFilter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to stream_filter property setter (gets validation automatically)
        """
        self.stream_filter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_filter_action_block(self, value: Optional["Boolean"]) -> "SwitchStreamIdentification":
        """
        Set filterActionBlock and return self for chaining.
        
        Args:
            value: The filterActionBlock to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_filter_action_block("value")
        """
        self.filter_action_block = value  # Use property setter (gets validation)
        return self

    def with_filter_action_dest(self, value: Optional["SwitchStreamFilter"]) -> "SwitchStreamIdentification":
        """
        Set filterActionDest and return self for chaining.
        
        Args:
            value: The filterActionDest to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_filter_action_dest("value")
        """
        self.filter_action_dest = value  # Use property setter (gets validation)
        return self

    def with_filter_action_drop(self, value: Optional["Boolean"]) -> "SwitchStreamIdentification":
        """
        Set filterActionDrop and return self for chaining.
        
        Args:
            value: The filterActionDrop to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_filter_action_drop("value")
        """
        self.filter_action_drop = value  # Use property setter (gets validation)
        return self

    def with_filter_action_vlan(self, value: Optional["PositiveInteger"]) -> "SwitchStreamIdentification":
        """
        Set filterActionVlan and return self for chaining.
        
        Args:
            value: The filterActionVlan to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_filter_action_vlan("value")
        """
        self.filter_action_vlan = value  # Use property setter (gets validation)
        return self

    def with_stream_filter(self, value: Optional["SwitchStreamFilterRule"]) -> "SwitchStreamIdentification":
        """
        Set streamFilter and return self for chaining.
        
        Args:
            value: The streamFilter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_stream_filter("value")
        """
        self.stream_filter = value  # Use property setter (gets validation)
        return self