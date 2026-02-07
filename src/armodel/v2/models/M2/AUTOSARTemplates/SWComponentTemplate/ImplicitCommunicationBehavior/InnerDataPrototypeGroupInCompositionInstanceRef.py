from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class InnerDataPrototypeGroupInCompositionInstanceRef(ARObject):
    """
    This meta-class represents the ability to define an InstanceRef to a nested
    DataPrototypeGroup
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::InstanceRef::InnerDataPrototypeGroupInCompositionInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 954, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the base of the instanceRef.
        # atpDerived 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate
                # Template R23-11.
        self._base: Optional["CompositionSw"] = None

    @property
    def base(self) -> Optional["CompositionSw"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["CompositionSw"]) -> None:
        """
        Set base with validation.
        
        Args:
            value: The base to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, CompositionSw):
            raise TypeError(
                f"base must be CompositionSw or None, got {type(value).__name__}"
            )
        self._base = value
        # This represents the nested structure of SwComponent Prototypes.
        # xml.
        # sequenceOffset=20 (ordered).
        self._contextSw: List["SwComponent"] = []

    @property
    def context_sw(self) -> List["SwComponent"]:
        """Get contextSw (Pythonic accessor)."""
        return self._contextSw
        # This represents the target of the InstanceRef xml.
        # sequenceOffset=30.
        self._targetData: RefType = None

    @property
    def target_data(self) -> RefType:
        """Get targetData (Pythonic accessor)."""
        return self._targetData

    @target_data.setter
    def target_data(self, value: RefType) -> None:
        """
        Set targetData with validation.
        
        Args:
            value: The targetData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetData = None
            return

        self._targetData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "CompositionSw":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "CompositionSw") -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """
        AUTOSAR-compliant setter for base with method chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getContextSw(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for contextSw.
        
        Returns:
            The contextSw value
        
        Note:
            Delegates to context_sw property (CODING_RULE_V2_00017)
        """
        return self.context_sw  # Delegates to property

    def getTargetData(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetData.
        
        Returns:
            The targetData value
        
        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: RefType) -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """
        AUTOSAR-compliant setter for targetData with method chaining.
        
        Args:
            value: The targetData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_data property setter (gets validation automatically)
        """
        self.target_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["CompositionSw"]) -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """
        Set base and return self for chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_target_data(self, value: Optional[RefType]) -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """
        Set targetData and return self for chaining.
        
        Args:
            value: The targetData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_data("value")
        """
        self.target_data = value  # Use property setter (gets validation)
        return self