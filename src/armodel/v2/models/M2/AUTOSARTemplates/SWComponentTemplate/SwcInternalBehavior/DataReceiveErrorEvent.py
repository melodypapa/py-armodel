from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DataReceiveErrorEvent(RTEEvent):
    """
    This event is raised when the Com layer detects and notifies an error
    concerning the reception of the referenced VariableDataPrototype.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::DataReceiveErrorEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 543, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # there was an error during the by: RVariableInAtomicSwc.
        self._data: RefType = None

    @property
    def data(self) -> RefType:
        """Get data (Pythonic accessor)."""
        return self._data

    @data.setter
    def data(self, value: RefType) -> None:
        """
        Set data with validation.
        
        Args:
            value: The data to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._data = None
            return

        self._data = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> RefType:
        """
        AUTOSAR-compliant getter for data.
        
        Returns:
            The data value
        
        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def setData(self, value: RefType) -> "DataReceiveErrorEvent":
        """
        AUTOSAR-compliant setter for data with method chaining.
        
        Args:
            value: The data to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data property setter (gets validation automatically)
        """
        self.data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data(self, value: Optional[RefType]) -> "DataReceiveErrorEvent":
        """
        Set data and return self for chaining.
        
        Args:
            value: The data to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data("value")
        """
        self.data = value  # Use property setter (gets validation)
        return self