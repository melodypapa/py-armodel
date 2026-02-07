from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ISignalMapping(ARObject):
    """
    Arranges those signals (or SignalGroups) that are transferred by the gateway
    from one channel to the other in pairs and defines the mapping between them.
    Each pair consists in a source and a target referencing to a
    ISignalTriggering.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::ISignalMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 846, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents introductory documentation about the.
        self._introduction: Optional["DocumentationBlock"] = None

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set introduction with validation.
        
        Args:
            value: The introduction to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value
        # Source destination of the referencing mapping.
        self._sourceSignal: RefType = None

    @property
    def source_signal(self) -> RefType:
        """Get sourceSignal (Pythonic accessor)."""
        return self._sourceSignal

    @source_signal.setter
    def source_signal(self, value: RefType) -> None:
        """
        Set sourceSignal with validation.
        
        Args:
            value: The sourceSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceSignal = None
            return

        self._sourceSignal = value
        # Target destination of the referencing mapping.
        self._targetSignal: RefType = None

    @property
    def target_signal(self) -> RefType:
        """Get targetSignal (Pythonic accessor)."""
        return self._targetSignal

    @target_signal.setter
    def target_signal(self, value: RefType) -> None:
        """
        Set targetSignal with validation.
        
        Args:
            value: The targetSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetSignal = None
            return

        self._targetSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.
        
        Returns:
            The introduction value
        
        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "ISignalMapping":
        """
        AUTOSAR-compliant setter for introduction with method chaining.
        
        Args:
            value: The introduction to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    def getSourceSignal(self) -> RefType:
        """
        AUTOSAR-compliant getter for sourceSignal.
        
        Returns:
            The sourceSignal value
        
        Note:
            Delegates to source_signal property (CODING_RULE_V2_00017)
        """
        return self.source_signal  # Delegates to property

    def setSourceSignal(self, value: RefType) -> "ISignalMapping":
        """
        AUTOSAR-compliant setter for sourceSignal with method chaining.
        
        Args:
            value: The sourceSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to source_signal property setter (gets validation automatically)
        """
        self.source_signal = value  # Delegates to property setter
        return self

    def getTargetSignal(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetSignal.
        
        Returns:
            The targetSignal value
        
        Note:
            Delegates to target_signal property (CODING_RULE_V2_00017)
        """
        return self.target_signal  # Delegates to property

    def setTargetSignal(self, value: RefType) -> "ISignalMapping":
        """
        AUTOSAR-compliant setter for targetSignal with method chaining.
        
        Args:
            value: The targetSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_signal property setter (gets validation automatically)
        """
        self.target_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "ISignalMapping":
        """
        Set introduction and return self for chaining.
        
        Args:
            value: The introduction to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self

    def with_source_signal(self, value: Optional[RefType]) -> "ISignalMapping":
        """
        Set sourceSignal and return self for chaining.
        
        Args:
            value: The sourceSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_source_signal("value")
        """
        self.source_signal = value  # Use property setter (gets validation)
        return self

    def with_target_signal(self, value: Optional[RefType]) -> "ISignalMapping":
        """
        Set targetSignal and return self for chaining.
        
        Args:
            value: The targetSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_signal("value")
        """
        self.target_signal = value  # Use property setter (gets validation)
        return self