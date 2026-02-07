from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SecurityEventOneEveryNFilter(AbstractSecurityEventFilter):
    """
    This meta-class represents the configuration of a sampling (i.e. every n-th
    event is sampled) filter for security events.
    
    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventOneEveryNFilter
    
    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 24, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the configuration of the sampling it configures the
        # parameter "n" that controls how (n-1) shall be dropped after a sampled event
        # new sample is created.
        self._n: Optional["PositiveInteger"] = None

    @property
    def n(self) -> Optional["PositiveInteger"]:
        """Get n (Pythonic accessor)."""
        return self._n

    @n.setter
    def n(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set n with validation.
        
        Args:
            value: The n to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._n = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"n must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._n = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getN(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for n.
        
        Returns:
            The n value
        
        Note:
            Delegates to n property (CODING_RULE_V2_00017)
        """
        return self.n  # Delegates to property

    def setN(self, value: "PositiveInteger") -> "SecurityEventOneEveryNFilter":
        """
        AUTOSAR-compliant setter for n with method chaining.
        
        Args:
            value: The n to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to n property setter (gets validation automatically)
        """
        self.n = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_n(self, value: Optional["PositiveInteger"]) -> "SecurityEventOneEveryNFilter":
        """
        Set n and return self for chaining.
        
        Args:
            value: The n to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_n("value")
        """
        self.n = value  # Use property setter (gets validation)
        return self