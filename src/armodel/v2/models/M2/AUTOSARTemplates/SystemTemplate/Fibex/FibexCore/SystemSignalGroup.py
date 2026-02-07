from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SystemSignalGroup(ARElement):
    """
    A signal group refers to a set of signals that shall always be kept
    together. A signal group is used to guarantee the atomic transfer of AUTOSAR
    composite data types. The SystemSignalGroup defines a signal grouping on VFB
    level. On cluster level the Signal grouping is described by the ISignalGroup
    element.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SystemSignalGroup
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 324, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a set of SystemSignals that shall always be.
        self._systemSignal: List["SystemSignal"] = []

    @property
    def system_signal(self) -> List["SystemSignal"]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal
        # Optional reference to the SystemSignal which shall the transformed (linear)
        # data.
        self._transforming: Optional["SystemSignal"] = None

    @property
    def transforming(self) -> Optional["SystemSignal"]:
        """Get transforming (Pythonic accessor)."""
        return self._transforming

    @transforming.setter
    def transforming(self, value: Optional["SystemSignal"]) -> None:
        """
        Set transforming with validation.
        
        Args:
            value: The transforming to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transforming = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"transforming must be SystemSignal or None, got {type(value).__name__}"
            )
        self._transforming = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSystemSignal(self) -> List["SystemSignal"]:
        """
        AUTOSAR-compliant getter for systemSignal.
        
        Returns:
            The systemSignal value
        
        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def getTransforming(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for transforming.
        
        Returns:
            The transforming value
        
        Note:
            Delegates to transforming property (CODING_RULE_V2_00017)
        """
        return self.transforming  # Delegates to property

    def setTransforming(self, value: "SystemSignal") -> "SystemSignalGroup":
        """
        AUTOSAR-compliant setter for transforming with method chaining.
        
        Args:
            value: The transforming to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transforming property setter (gets validation automatically)
        """
        self.transforming = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transforming(self, value: Optional["SystemSignal"]) -> "SystemSignalGroup":
        """
        Set transforming and return self for chaining.
        
        Args:
            value: The transforming to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_transforming("value")
        """
        self.transforming = value  # Use property setter (gets validation)
        return self