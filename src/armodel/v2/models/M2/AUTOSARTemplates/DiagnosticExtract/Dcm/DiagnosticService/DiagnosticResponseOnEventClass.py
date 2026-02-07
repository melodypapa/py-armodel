from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticResponseOnEventClass(DiagnosticServiceClass):
    """
    This represents the ability to define common properties for all instances of
    the "Response on Event" diagnostic service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent::DiagnosticResponseOnEventClass
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 132, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum number of DTCs that can be stored as with change status within
        # one ResponseOnEvent interval.
        self._maxNumberOf: Optional["PositiveInteger"] = None

    @property
    def max_number_of(self) -> Optional["PositiveInteger"]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNumberOf with validation.
        
        Args:
            value: The maxNumberOf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # The maximum number of events that can be configured with sub function on.
        self._maxNum: Optional["PositiveInteger"] = None

    @property
    def max_num(self) -> Optional["PositiveInteger"]:
        """Get maxNum (Pythonic accessor)."""
        return self._maxNum

    @max_num.setter
    def max_num(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNum with validation.
        
        Args:
            value: The maxNum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNum = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxNum must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxNum = value
        # The maximum number of measurable data bytes allowed each DID that is used for
        # comparison or data change.
        self._maxSupported: Optional["PositiveInteger"] = None

    @property
    def max_supported(self) -> Optional["PositiveInteger"]:
        """Get maxSupported (Pythonic accessor)."""
        return self._maxSupported

    @max_supported.setter
    def max_supported(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxSupported with validation.
        
        Args:
            value: The maxSupported to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSupported = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxSupported must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxSupported = value
        # The call rate of the periodic scheduler to compare the of the DataIdentifier
        # (DID) or to detect DTC status.
        self._responseOn: Optional["TimeValue"] = None

    @property
    def response_on(self) -> Optional["TimeValue"]:
        """Get responseOn (Pythonic accessor)."""
        return self._responseOn

    @response_on.setter
    def response_on(self, value: Optional["TimeValue"]) -> None:
        """
        Set responseOn with validation.
        
        Args:
            value: The responseOn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._responseOn = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"responseOn must be TimeValue or None, got {type(value).__name__}"
            )
        self._responseOn = value
        # Specifies if the storeEvent functionality of the Response diagnostic service
                # shall be supported or not.
        # If true, the storeEvent functionality is available.
        # If set the storeEvent functionality is not available.
        self._storeEvent: Optional["Boolean"] = None

    @property
    def store_event(self) -> Optional["Boolean"]:
        """Get storeEvent (Pythonic accessor)."""
        return self._storeEvent

    @store_event.setter
    def store_event(self, value: Optional["Boolean"]) -> None:
        """
        Set storeEvent with validation.
        
        Args:
            value: The storeEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storeEvent = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"storeEvent must be Boolean or None, got {type(value).__name__}"
            )
        self._storeEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.
        
        Returns:
            The maxNumberOf value
        
        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> "DiagnosticResponseOnEventClass":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.
        
        Args:
            value: The maxNumberOf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getMaxNum(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNum.
        
        Returns:
            The maxNum value
        
        Note:
            Delegates to max_num property (CODING_RULE_V2_00017)
        """
        return self.max_num  # Delegates to property

    def setMaxNum(self, value: "PositiveInteger") -> "DiagnosticResponseOnEventClass":
        """
        AUTOSAR-compliant setter for maxNum with method chaining.
        
        Args:
            value: The maxNum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_num property setter (gets validation automatically)
        """
        self.max_num = value  # Delegates to property setter
        return self

    def getMaxSupported(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxSupported.
        
        Returns:
            The maxSupported value
        
        Note:
            Delegates to max_supported property (CODING_RULE_V2_00017)
        """
        return self.max_supported  # Delegates to property

    def setMaxSupported(self, value: "PositiveInteger") -> "DiagnosticResponseOnEventClass":
        """
        AUTOSAR-compliant setter for maxSupported with method chaining.
        
        Args:
            value: The maxSupported to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_supported property setter (gets validation automatically)
        """
        self.max_supported = value  # Delegates to property setter
        return self

    def getResponseOn(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for responseOn.
        
        Returns:
            The responseOn value
        
        Note:
            Delegates to response_on property (CODING_RULE_V2_00017)
        """
        return self.response_on  # Delegates to property

    def setResponseOn(self, value: "TimeValue") -> "DiagnosticResponseOnEventClass":
        """
        AUTOSAR-compliant setter for responseOn with method chaining.
        
        Args:
            value: The responseOn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to response_on property setter (gets validation automatically)
        """
        self.response_on = value  # Delegates to property setter
        return self

    def getStoreEvent(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for storeEvent.
        
        Returns:
            The storeEvent value
        
        Note:
            Delegates to store_event property (CODING_RULE_V2_00017)
        """
        return self.store_event  # Delegates to property

    def setStoreEvent(self, value: "Boolean") -> "DiagnosticResponseOnEventClass":
        """
        AUTOSAR-compliant setter for storeEvent with method chaining.
        
        Args:
            value: The storeEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to store_event property setter (gets validation automatically)
        """
        self.store_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> "DiagnosticResponseOnEventClass":
        """
        Set maxNumberOf and return self for chaining.
        
        Args:
            value: The maxNumberOf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_max_num(self, value: Optional["PositiveInteger"]) -> "DiagnosticResponseOnEventClass":
        """
        Set maxNum and return self for chaining.
        
        Args:
            value: The maxNum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_num("value")
        """
        self.max_num = value  # Use property setter (gets validation)
        return self

    def with_max_supported(self, value: Optional["PositiveInteger"]) -> "DiagnosticResponseOnEventClass":
        """
        Set maxSupported and return self for chaining.
        
        Args:
            value: The maxSupported to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_supported("value")
        """
        self.max_supported = value  # Use property setter (gets validation)
        return self

    def with_response_on(self, value: Optional["TimeValue"]) -> "DiagnosticResponseOnEventClass":
        """
        Set responseOn and return self for chaining.
        
        Args:
            value: The responseOn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_response_on("value")
        """
        self.response_on = value  # Use property setter (gets validation)
        return self

    def with_store_event(self, value: Optional["Boolean"]) -> "DiagnosticResponseOnEventClass":
        """
        Set storeEvent and return self for chaining.
        
        Args:
            value: The storeEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_store_event("value")
        """
        self.store_event = value  # Use property setter (gets validation)
        return self