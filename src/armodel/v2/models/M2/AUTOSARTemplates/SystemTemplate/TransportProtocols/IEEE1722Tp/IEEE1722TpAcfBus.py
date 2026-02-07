from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class IEEE1722TpAcfBus(Identifiable, ABC):
    """
    Abstract class to define various busses to be transported over a IEEE1722TP
    ACF connection.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfBus
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 657, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is IEEE1722TpAcfBus:
            raise TypeError("IEEE1722TpAcfBus is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # One part transported over IEEE1722Tp channel.
        # atpVariation.
        self._acfPart: List["IEEE1722TpAcfBusPart"] = []

    @property
    def acf_part(self) -> List["IEEE1722TpAcfBusPart"]:
        """Get acfPart (Pythonic accessor)."""
        return self._acfPart
        # Id of the transported bus over the ACF connection.
        self._busId: Optional["PositiveInteger"] = None

    @property
    def bus_id(self) -> Optional["PositiveInteger"]:
        """Get busId (Pythonic accessor)."""
        return self._busId

    @bus_id.setter
    def bus_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set busId with validation.
        
        Args:
            value: The busId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._busId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"busId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._busId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAcfPart(self) -> List["IEEE1722TpAcfBusPart"]:
        """
        AUTOSAR-compliant getter for acfPart.
        
        Returns:
            The acfPart value
        
        Note:
            Delegates to acf_part property (CODING_RULE_V2_00017)
        """
        return self.acf_part  # Delegates to property

    def getBusId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for busId.
        
        Returns:
            The busId value
        
        Note:
            Delegates to bus_id property (CODING_RULE_V2_00017)
        """
        return self.bus_id  # Delegates to property

    def setBusId(self, value: "PositiveInteger") -> "IEEE1722TpAcfBus":
        """
        AUTOSAR-compliant setter for busId with method chaining.
        
        Args:
            value: The busId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bus_id property setter (gets validation automatically)
        """
        self.bus_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bus_id(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAcfBus":
        """
        Set busId and return self for chaining.
        
        Args:
            value: The busId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bus_id("value")
        """
        self.bus_id = value  # Use property setter (gets validation)
        return self