from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SwcBswMapping(ARElement):
    """
    Maps an SwcInternalBehavior to an BswInternalBehavior. This is required to
    coordinate the API generation and the scheduling for AUTOSAR Service
    Components, ECU Abstraction Components and Complex Driver Components by the
    RTE and the BSW scheduling mechanisms.
    
    Package: M2::AUTOSARTemplates::CommonStructure::SwcBswMapping::SwcBswMapping
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 110, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 656, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 217, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The mapped BswInternalBehavior.
        self._bswBehavior: Optional["BswInternalBehavior"] = None

    @property
    def bsw_behavior(self) -> Optional["BswInternalBehavior"]:
        """Get bswBehavior (Pythonic accessor)."""
        return self._bswBehavior

    @bsw_behavior.setter
    def bsw_behavior(self, value: Optional["BswInternalBehavior"]) -> None:
        """
        Set bswBehavior with validation.
        
        Args:
            value: The bswBehavior to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswBehavior = None
            return

        if not isinstance(value, BswInternalBehavior):
            raise TypeError(
                f"bswBehavior must be BswInternalBehavior or None, got {type(value).__name__}"
            )
        self._bswBehavior = value
        # A mapping between a pair of SWC and BSW runnables.
        # Stereotypes: atpSplitable; atpVariation.
        self._runnable: List["SwcBswRunnable"] = []

    @property
    def runnable(self) -> List["SwcBswRunnable"]:
        """Get runnable (Pythonic accessor)."""
        return self._runnable
        # The mapped SwcInternalBehavior.
        self._swcBehavior: Optional["SwcInternalBehavior"] = None

    @property
    def swc_behavior(self) -> Optional["SwcInternalBehavior"]:
        """Get swcBehavior (Pythonic accessor)."""
        return self._swcBehavior

    @swc_behavior.setter
    def swc_behavior(self, value: Optional["SwcInternalBehavior"]) -> None:
        """
        Set swcBehavior with validation.
        
        Args:
            value: The swcBehavior to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcBehavior = None
            return

        if not isinstance(value, SwcInternalBehavior):
            raise TypeError(
                f"swcBehavior must be SwcInternalBehavior or None, got {type(value).__name__}"
            )
        self._swcBehavior = value
        # A pair of SWC and BSW Triggers to be synchronized by the scheduler.
        # atpVariation.
        self._synchronized: List["SwcBswSynchronized"] = []

    @property
    def synchronized(self) -> List["SwcBswSynchronized"]:
        """Get synchronized (Pythonic accessor)."""
        return self._synchronized

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswBehavior(self) -> "BswInternalBehavior":
        """
        AUTOSAR-compliant getter for bswBehavior.
        
        Returns:
            The bswBehavior value
        
        Note:
            Delegates to bsw_behavior property (CODING_RULE_V2_00017)
        """
        return self.bsw_behavior  # Delegates to property

    def setBswBehavior(self, value: "BswInternalBehavior") -> "SwcBswMapping":
        """
        AUTOSAR-compliant setter for bswBehavior with method chaining.
        
        Args:
            value: The bswBehavior to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bsw_behavior property setter (gets validation automatically)
        """
        self.bsw_behavior = value  # Delegates to property setter
        return self

    def getRunnable(self) -> List["SwcBswRunnable"]:
        """
        AUTOSAR-compliant getter for runnable.
        
        Returns:
            The runnable value
        
        Note:
            Delegates to runnable property (CODING_RULE_V2_00017)
        """
        return self.runnable  # Delegates to property

    def getSwcBehavior(self) -> "SwcInternalBehavior":
        """
        AUTOSAR-compliant getter for swcBehavior.
        
        Returns:
            The swcBehavior value
        
        Note:
            Delegates to swc_behavior property (CODING_RULE_V2_00017)
        """
        return self.swc_behavior  # Delegates to property

    def setSwcBehavior(self, value: "SwcInternalBehavior") -> "SwcBswMapping":
        """
        AUTOSAR-compliant setter for swcBehavior with method chaining.
        
        Args:
            value: The swcBehavior to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to swc_behavior property setter (gets validation automatically)
        """
        self.swc_behavior = value  # Delegates to property setter
        return self

    def getSynchronized(self) -> List["SwcBswSynchronized"]:
        """
        AUTOSAR-compliant getter for synchronized.
        
        Returns:
            The synchronized value
        
        Note:
            Delegates to synchronized property (CODING_RULE_V2_00017)
        """
        return self.synchronized  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_behavior(self, value: Optional["BswInternalBehavior"]) -> "SwcBswMapping":
        """
        Set bswBehavior and return self for chaining.
        
        Args:
            value: The bswBehavior to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bsw_behavior("value")
        """
        self.bsw_behavior = value  # Use property setter (gets validation)
        return self

    def with_swc_behavior(self, value: Optional["SwcInternalBehavior"]) -> "SwcBswMapping":
        """
        Set swcBehavior and return self for chaining.
        
        Args:
            value: The swcBehavior to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_swc_behavior("value")
        """
        self.swc_behavior = value  # Use property setter (gets validation)
        return self