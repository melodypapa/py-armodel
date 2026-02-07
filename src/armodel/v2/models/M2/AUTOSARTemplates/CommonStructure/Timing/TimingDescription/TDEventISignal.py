from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class TDEventISignal(TDEventCom):
    """
    This is used to describe timing events related to the exchange of I-Signals
    between COM and RTE.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventISignal
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 65, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._iSignal: Optional["ISignal"] = None

    @property
    def i_signal(self) -> Optional["ISignal"]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal

    @i_signal.setter
    def i_signal(self, value: Optional["ISignal"]) -> None:
        """
        Set iSignal with validation.
        
        Args:
            value: The iSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignal = None
            return

        if not isinstance(value, ISignal):
            raise TypeError(
                f"iSignal must be ISignal or None, got {type(value).__name__}"
            )
        self._iSignal = value
        # The PhysicalChannel on which the ISignal is transmitted.
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
        self._tdEventTypeEnum: Optional["TDEventISignalType"] = None

    @property
    def td_event_type_enum(self) -> Optional["TDEventISignalType"]:
        """Get tdEventTypeEnum (Pythonic accessor)."""
        return self._tdEventTypeEnum

    @td_event_type_enum.setter
    def td_event_type_enum(self, value: Optional["TDEventISignalType"]) -> None:
        """
        Set tdEventTypeEnum with validation.
        
        Args:
            value: The tdEventTypeEnum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventTypeEnum = None
            return

        if not isinstance(value, TDEventISignalType):
            raise TypeError(
                f"tdEventTypeEnum must be TDEventISignalType or None, got {type(value).__name__}"
            )
        self._tdEventTypeEnum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getISignal(self) -> "ISignal":
        """
        AUTOSAR-compliant getter for iSignal.
        
        Returns:
            The iSignal value
        
        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def setISignal(self, value: "ISignal") -> "TDEventISignal":
        """
        AUTOSAR-compliant setter for iSignal with method chaining.
        
        Args:
            value: The iSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_signal property setter (gets validation automatically)
        """
        self.i_signal = value  # Delegates to property setter
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

    def setPhysical(self, value: "PhysicalChannel") -> "TDEventISignal":
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

    def getTdEventTypeEnum(self) -> "TDEventISignalType":
        """
        AUTOSAR-compliant getter for tdEventTypeEnum.
        
        Returns:
            The tdEventTypeEnum value
        
        Note:
            Delegates to td_event_type_enum property (CODING_RULE_V2_00017)
        """
        return self.td_event_type_enum  # Delegates to property

    def setTdEventTypeEnum(self, value: "TDEventISignalType") -> "TDEventISignal":
        """
        AUTOSAR-compliant setter for tdEventTypeEnum with method chaining.
        
        Args:
            value: The tdEventTypeEnum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to td_event_type_enum property setter (gets validation automatically)
        """
        self.td_event_type_enum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_signal(self, value: Optional["ISignal"]) -> "TDEventISignal":
        """
        Set iSignal and return self for chaining.
        
        Args:
            value: The iSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_signal("value")
        """
        self.i_signal = value  # Use property setter (gets validation)
        return self

    def with_physical(self, value: Optional["PhysicalChannel"]) -> "TDEventISignal":
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

    def with_td_event_type_enum(self, value: Optional["TDEventISignalType"]) -> "TDEventISignal":
        """
        Set tdEventTypeEnum and return self for chaining.
        
        Args:
            value: The tdEventTypeEnum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_td_event_type_enum("value")
        """
        self.td_event_type_enum = value  # Use property setter (gets validation)
        return self