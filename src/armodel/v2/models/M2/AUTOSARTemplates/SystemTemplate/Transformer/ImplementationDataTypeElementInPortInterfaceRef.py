from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class ImplementationDataTypeElementInPortInterfaceRef(DataPrototypeReference):
    """
    This meta-class represents the ability to refer to the internal structure of
    an AutosarDataPrototype which is typed by an ImplementationDatatype in the
    context of a PortInterface. In other words, this meta-class shall not be
    used to model a reference to the AutosarDataPrototype as a target itself,
    even if the AutosarDataPrototype is typed by an ImplementationDataType and
    even if that ImplementationDataType represents a composite data type.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef::ImplementationDataTypeElementInPortInterfaceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 789, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a context in case there are subelements with explicit types.
        # The reference has to be ordered to reflect the nested structure.
        # xml.
        # sequenceOffset=20.
        self._context: List["AbstractImplementation"] = []

    @property
    def context(self) -> List["AbstractImplementation"]:
        """Get context (Pythonic accessor)."""
        return self._context
        # This refers to the AutosarDataPrototype which is typed by
                # ImplementationDatatype.
        # The targetDataPrototype defined contextDataPrototypes can be found
                # rootDataPrototype.
        self._rootData: RefType = None

    @property
    def root_data(self) -> RefType:
        """Get rootData (Pythonic accessor)."""
        return self._rootData

    @root_data.setter
    def root_data(self, value: RefType) -> None:
        """
        Set rootData with validation.
        
        Args:
            value: The rootData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootData = None
            return

        self._rootData = value
        # This is a target ImplementationDataTypeElement in case that the
                # rootDataPrototype is composite and the target is subElement of the
                # rootDataPrototype.
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

    def getContext(self) -> List["AbstractImplementation"]:
        """
        AUTOSAR-compliant getter for context.
        
        Returns:
            The context value
        
        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def getRootData(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootData.
        
        Returns:
            The rootData value
        
        Note:
            Delegates to root_data property (CODING_RULE_V2_00017)
        """
        return self.root_data  # Delegates to property

    def setRootData(self, value: RefType) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """
        AUTOSAR-compliant setter for rootData with method chaining.
        
        Args:
            value: The rootData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to root_data property setter (gets validation automatically)
        """
        self.root_data = value  # Delegates to property setter
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

    def setTarget(self, value: "AbstractImplementation") -> "ImplementationDataTypeElementInPortInterfaceRef":
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

    def with_root_data(self, value: Optional[RefType]) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """
        Set rootData and return self for chaining.
        
        Args:
            value: The rootData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_root_data("value")
        """
        self.root_data = value  # Use property setter (gets validation)
        return self

    def with_target(self, value: Optional["AbstractImplementation"]) -> "ImplementationDataTypeElementInPortInterfaceRef":
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