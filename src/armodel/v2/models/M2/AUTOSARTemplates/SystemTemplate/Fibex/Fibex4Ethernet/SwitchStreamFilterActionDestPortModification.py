from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwitchStreamFilterActionDestPortModification(Identifiable):
    """
    Defines the action to modify the destination port(s) determined by the frame
    forwarding process for an particular Ethernet frame. Either the egress
    destination of an Ethernet frame is extended or overwritten.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchStreamFilterActionDestPortModification
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 140, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the egress ports used as the target of the to modify the egress
        # port.
        self._egressPort: List["CouplingPort"] = []

    @property
    def egress_port(self) -> List["CouplingPort"]:
        """Get egressPort (Pythonic accessor)."""
        return self._egressPort
        # Defines the method to modify the egress destination.
        # overwrite or extend the egress destination.
        # atp.
        # Status=candidate.
        self._modification: Optional["SwitchStreamFilter"] = None

    @property
    def modification(self) -> Optional["SwitchStreamFilter"]:
        """Get modification (Pythonic accessor)."""
        return self._modification

    @modification.setter
    def modification(self, value: Optional["SwitchStreamFilter"]) -> None:
        """
        Set modification with validation.
        
        Args:
            value: The modification to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modification = None
            return

        if not isinstance(value, SwitchStreamFilter):
            raise TypeError(
                f"modification must be SwitchStreamFilter or None, got {type(value).__name__}"
            )
        self._modification = value

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

    def getModification(self) -> "SwitchStreamFilter":
        """
        AUTOSAR-compliant getter for modification.
        
        Returns:
            The modification value
        
        Note:
            Delegates to modification property (CODING_RULE_V2_00017)
        """
        return self.modification  # Delegates to property

    def setModification(self, value: "SwitchStreamFilter") -> "SwitchStreamFilterActionDestPortModification":
        """
        AUTOSAR-compliant setter for modification with method chaining.
        
        Args:
            value: The modification to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to modification property setter (gets validation automatically)
        """
        self.modification = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_modification(self, value: Optional["SwitchStreamFilter"]) -> "SwitchStreamFilterActionDestPortModification":
        """
        Set modification and return self for chaining.
        
        Args:
            value: The modification to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_modification("value")
        """
        self.modification = value  # Use property setter (gets validation)
        return self