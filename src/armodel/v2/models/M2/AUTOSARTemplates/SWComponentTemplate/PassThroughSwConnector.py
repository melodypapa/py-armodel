from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class PassThroughSwConnector(SwConnector):
    """
    This kind of SwConnector can be used inside a CompositionSwComponentType to
    connect two delegation PortPrototypes.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::PassThroughSwConnector
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 83, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2043, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the provided outer delegation Port Prototype of the
        # PassThroughSwConnector.
        self._providedOuter: Optional["AbstractProvidedPort"] = None

    @property
    def provided_outer(self) -> Optional["AbstractProvidedPort"]:
        """Get providedOuter (Pythonic accessor)."""
        return self._providedOuter

    @provided_outer.setter
    def provided_outer(self, value: Optional["AbstractProvidedPort"]) -> None:
        """
        Set providedOuter with validation.
        
        Args:
            value: The providedOuter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._providedOuter = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"providedOuter must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._providedOuter = value
        # This represents the required outer delegation Port Prototype of the
        # PassThroughSwConnector.
        self._requiredOuter: Optional["AbstractRequiredPort"] = None

    @property
    def required_outer(self) -> Optional["AbstractRequiredPort"]:
        """Get requiredOuter (Pythonic accessor)."""
        return self._requiredOuter

    @required_outer.setter
    def required_outer(self, value: Optional["AbstractRequiredPort"]) -> None:
        """
        Set requiredOuter with validation.
        
        Args:
            value: The requiredOuter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requiredOuter = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"requiredOuter must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._requiredOuter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvidedOuter(self) -> "AbstractProvidedPort":
        """
        AUTOSAR-compliant getter for providedOuter.
        
        Returns:
            The providedOuter value
        
        Note:
            Delegates to provided_outer property (CODING_RULE_V2_00017)
        """
        return self.provided_outer  # Delegates to property

    def setProvidedOuter(self, value: "AbstractProvidedPort") -> "PassThroughSwConnector":
        """
        AUTOSAR-compliant setter for providedOuter with method chaining.
        
        Args:
            value: The providedOuter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to provided_outer property setter (gets validation automatically)
        """
        self.provided_outer = value  # Delegates to property setter
        return self

    def getRequiredOuter(self) -> "AbstractRequiredPort":
        """
        AUTOSAR-compliant getter for requiredOuter.
        
        Returns:
            The requiredOuter value
        
        Note:
            Delegates to required_outer property (CODING_RULE_V2_00017)
        """
        return self.required_outer  # Delegates to property

    def setRequiredOuter(self, value: "AbstractRequiredPort") -> "PassThroughSwConnector":
        """
        AUTOSAR-compliant setter for requiredOuter with method chaining.
        
        Args:
            value: The requiredOuter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to required_outer property setter (gets validation automatically)
        """
        self.required_outer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provided_outer(self, value: Optional["AbstractProvidedPort"]) -> "PassThroughSwConnector":
        """
        Set providedOuter and return self for chaining.
        
        Args:
            value: The providedOuter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_provided_outer("value")
        """
        self.provided_outer = value  # Use property setter (gets validation)
        return self

    def with_required_outer(self, value: Optional["AbstractRequiredPort"]) -> "PassThroughSwConnector":
        """
        Set requiredOuter and return self for chaining.
        
        Args:
            value: The requiredOuter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_required_outer("value")
        """
        self.required_outer = value  # Use property setter (gets validation)
        return self