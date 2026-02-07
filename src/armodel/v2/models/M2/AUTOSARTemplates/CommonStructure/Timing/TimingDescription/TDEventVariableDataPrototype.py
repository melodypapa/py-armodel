from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class TDEventVariableDataPrototype(TDEventVfbPort):
    """
    This is used to describe timing events related to sender-receiver
    communication at VFB level.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventVariableDataPrototype
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 53, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced VariableDataPrototype.
        self._dataElement: RefType = None

    @property
    def data_element(self) -> RefType:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: RefType) -> None:
        """
        Set dataElement with validation.
        
        Args:
            value: The dataElement to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        # The specific type of this timing event.
        self._tdEventVariableType: Optional["TDEventVariableData"] = None

    @property
    def td_event_variable_type(self) -> Optional["TDEventVariableData"]:
        """Get tdEventVariableType (Pythonic accessor)."""
        return self._tdEventVariableType

    @td_event_variable_type.setter
    def td_event_variable_type(self, value: Optional["TDEventVariableData"]) -> None:
        """
        Set tdEventVariableType with validation.
        
        Args:
            value: The tdEventVariableType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventVariableType = None
            return

        if not isinstance(value, TDEventVariableData):
            raise TypeError(
                f"tdEventVariableType must be TDEventVariableData or None, got {type(value).__name__}"
            )
        self._tdEventVariableType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElement.
        
        Returns:
            The dataElement value
        
        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: RefType) -> "TDEventVariableDataPrototype":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getTdEventVariableType(self) -> "TDEventVariableData":
        """
        AUTOSAR-compliant getter for tdEventVariableType.
        
        Returns:
            The tdEventVariableType value
        
        Note:
            Delegates to td_event_variable_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_variable_type  # Delegates to property

    def setTdEventVariableType(self, value: "TDEventVariableData") -> "TDEventVariableDataPrototype":
        """
        AUTOSAR-compliant setter for tdEventVariableType with method chaining.
        
        Args:
            value: The tdEventVariableType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to td_event_variable_type property setter (gets validation automatically)
        """
        self.td_event_variable_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional[RefType]) -> "TDEventVariableDataPrototype":
        """
        Set dataElement and return self for chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_td_event_variable_type(self, value: Optional["TDEventVariableData"]) -> "TDEventVariableDataPrototype":
        """
        Set tdEventVariableType and return self for chaining.
        
        Args:
            value: The tdEventVariableType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_td_event_variable_type("value")
        """
        self.td_event_variable_type = value  # Use property setter (gets validation)
        return self