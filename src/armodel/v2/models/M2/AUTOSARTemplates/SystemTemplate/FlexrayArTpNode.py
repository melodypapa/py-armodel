from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class FlexrayArTpNode(Identifiable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to
    the Topology description.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayArTpNode
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 602, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to one or more physical connectors (max of connectors for
                # FlexRay: 2).
        # System Description this reference is mandatory.
        # In Extract this reference is optional (references to are not part of the ECU
                # Extract shall be.
        self._connector: List["FlexrayCommunication"] = []

    @property
    def connector(self) -> List["FlexrayCommunication"]:
        """Get connector (Pythonic accessor)."""
        return self._connector
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

    def getConnector(self) -> List["FlexrayCommunication"]:
        """
        AUTOSAR-compliant getter for connector.
        
        Returns:
            The connector value
        
        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def getTpAddress(self) -> "TpAddress":
        """
        AUTOSAR-compliant getter for tpAddress.
        
        Returns:
            The tpAddress value
        
        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: "TpAddress") -> "FlexrayArTpNode":
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

    def with_tp_address(self, value: Optional["TpAddress"]) -> "FlexrayArTpNode":
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