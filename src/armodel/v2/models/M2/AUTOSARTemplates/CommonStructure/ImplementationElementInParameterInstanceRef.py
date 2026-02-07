from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ImplementationElementInParameterInstanceRef(ARObject):
    """
    that this class follows the pattern of an InstanceRef but is not implemented
    based on the abstract classes because the ImplementationDataType isn’t
    either, especially because ImplementationDataType Element isn’t derived from
    AtpPrototype.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::ImplementationElementInParameterInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 184, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The context for the referred element.
        # xml.
        # sequenceOffset=20.
        self._context: Optional["ParameterData"] = None

    @property
    def context(self) -> Optional["ParameterData"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["ParameterData"]) -> None:
        """
        Set context with validation.
        
        Args:
            value: The context to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"context must be ParameterData or None, got {type(value).__name__}"
            )
        self._context = value
        # The referred data element.
        # xml.
        # sequenceOffset=30.
        self._target: Optional["AbstractImplementation"] = None

    @property
    def target(self) -> Optional["AbstractImplementation"]:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: Optional["AbstractImplementation"]) -> None:
        """
        Set target with validation.
        
        Args:
            value: The target to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._target = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"target must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._target = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for context.
        
        Returns:
            The context value
        
        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "ParameterData") -> "ImplementationElementInParameterInstanceRef":
        """
        AUTOSAR-compliant setter for context with method chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
        return self

    def getTarget(self) -> "AbstractImplementation":
        """
        AUTOSAR-compliant getter for target.
        
        Returns:
            The target value
        
        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: "AbstractImplementation") -> "ImplementationElementInParameterInstanceRef":
        """
        AUTOSAR-compliant setter for target with method chaining.
        
        Args:
            value: The target to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target property setter (gets validation automatically)
        """
        self.target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context(self, value: Optional["ParameterData"]) -> "ImplementationElementInParameterInstanceRef":
        """
        Set context and return self for chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_target(self, value: Optional["AbstractImplementation"]) -> "ImplementationElementInParameterInstanceRef":
        """
        Set target and return self for chaining.
        
        Args:
            value: The target to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self