from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class TDEventIPdu(TDEventCom):
    """
    This is used to describe timing events related to the exchange of I-PDUs
    between the bus specific (Flex Ray / CAN / LIN) Interface BSW module and
    COM.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 66, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._iPdu: Optional["IPdu"] = None

    @property
    def i_pdu(self) -> Optional["IPdu"]:
        """Get iPdu (Pythonic accessor)."""
        return self._iPdu

    @i_pdu.setter
    def i_pdu(self, value: Optional["IPdu"]) -> None:
        """
        Set iPdu with validation.
        
        Args:
            value: The iPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"iPdu must be IPdu or None, got {type(value).__name__}"
            )
        self._iPdu = value
        # The PhysicalChannel on which the IPdu is transmitted.
        self._physical: Optional["PhysicalChannel"] = None

    @property
    def physical(self) -> Optional["PhysicalChannel"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @physical.setter
    def physical(self, value: Optional["PhysicalChannel"]) -> None:
        """
        Set physical with validation.
        
        Args:
            value: The physical to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physical = None
            return

        if not isinstance(value, PhysicalChannel):
            raise TypeError(
                f"physical must be PhysicalChannel or None, got {type(value).__name__}"
            )
        self._physical = value
        # The specific type of this timing event.
        self._tdEventType: Optional["TDEventIPduTypeEnum"] = None

    @property
    def td_event_type(self) -> Optional["TDEventIPduTypeEnum"]:
        """Get tdEventType (Pythonic accessor)."""
        return self._tdEventType

    @td_event_type.setter
    def td_event_type(self, value: Optional["TDEventIPduTypeEnum"]) -> None:
        """
        Set tdEventType with validation.
        
        Args:
            value: The tdEventType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventType = None
            return

        if not isinstance(value, TDEventIPduTypeEnum):
            raise TypeError(
                f"tdEventType must be TDEventIPduTypeEnum or None, got {type(value).__name__}"
            )
        self._tdEventType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPdu(self) -> "IPdu":
        """
        AUTOSAR-compliant getter for iPdu.
        
        Returns:
            The iPdu value
        
        Note:
            Delegates to i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_pdu  # Delegates to property

    def setIPdu(self, value: "IPdu") -> "TDEventIPdu":
        """
        AUTOSAR-compliant setter for iPdu with method chaining.
        
        Args:
            value: The iPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_pdu property setter (gets validation automatically)
        """
        self.i_pdu = value  # Delegates to property setter
        return self

    def getPhysical(self) -> "PhysicalChannel":
        """
        AUTOSAR-compliant getter for physical.
        
        Returns:
            The physical value
        
        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def setPhysical(self, value: "PhysicalChannel") -> "TDEventIPdu":
        """
        AUTOSAR-compliant setter for physical with method chaining.
        
        Args:
            value: The physical to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to physical property setter (gets validation automatically)
        """
        self.physical = value  # Delegates to property setter
        return self

    def getTdEventType(self) -> "TDEventIPduTypeEnum":
        """
        AUTOSAR-compliant getter for tdEventType.
        
        Returns:
            The tdEventType value
        
        Note:
            Delegates to td_event_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_type  # Delegates to property

    def setTdEventType(self, value: "TDEventIPduTypeEnum") -> "TDEventIPdu":
        """
        AUTOSAR-compliant setter for tdEventType with method chaining.
        
        Args:
            value: The tdEventType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to td_event_type property setter (gets validation automatically)
        """
        self.td_event_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_pdu(self, value: Optional["IPdu"]) -> "TDEventIPdu":
        """
        Set iPdu and return self for chaining.
        
        Args:
            value: The iPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_pdu("value")
        """
        self.i_pdu = value  # Use property setter (gets validation)
        return self

    def with_physical(self, value: Optional["PhysicalChannel"]) -> "TDEventIPdu":
        """
        Set physical and return self for chaining.
        
        Args:
            value: The physical to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self

    def with_td_event_type(self, value: Optional["TDEventIPduTypeEnum"]) -> "TDEventIPdu":
        """
        Set tdEventType and return self for chaining.
        
        Args:
            value: The tdEventType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_td_event_type("value")
        """
        self.td_event_type = value  # Use property setter (gets validation)
        return self