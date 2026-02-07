from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DataPrototypeInPortInterfaceInstanceRef(ARObject, ABC):
    """
    This meta-class represents the ability to: • refer to a DataPrototype in the
    context of a PortInterface. • refer to the internal structure of a
    DataPrototype which is typed by an ApplicationDatatype in the context of a
    PortInterface.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef::DataPrototypeInPortInterfaceInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1009, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DataPrototypeInPortInterfaceInstanceRef:
            raise TypeError("DataPrototypeInPortInterfaceInstanceRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpAbstract.
        self._abstractBase: Optional["PortInterface"] = None

    @property
    def abstract_base(self) -> Optional["PortInterface"]:
        """Get abstractBase (Pythonic accessor)."""
        return self._abstractBase

    @abstract_base.setter
    def abstract_base(self, value: Optional["PortInterface"]) -> None:
        """
        Set abstractBase with validation.
        
        Args:
            value: The abstractBase to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._abstractBase = None
            return

        if not isinstance(value, PortInterface):
            raise TypeError(
                f"abstractBase must be PortInterface or None, got {type(value).__name__}"
            )
        self._abstractBase = value
        # Stereotypes: atpAbstract Tags: xml.
        # sequenceOffset=20.
        self._contextData: List["ApplicationComposite"] = []

    @property
    def context_data(self) -> List["ApplicationComposite"]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # Stereotypes: atpAbstract xml.
        # sequenceOffset=10.
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
        # Stereotypes: atpAbstract xml.
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
        self._targetData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAbstractBase(self) -> "PortInterface":
        """
        AUTOSAR-compliant getter for abstractBase.
        
        Returns:
            The abstractBase value
        
        Note:
            Delegates to abstract_base property (CODING_RULE_V2_00017)
        """
        return self.abstract_base  # Delegates to property

    def setAbstractBase(self, value: "PortInterface") -> "DataPrototypeInPortInterfaceInstanceRef":
        """
        AUTOSAR-compliant setter for abstractBase with method chaining.
        
        Args:
            value: The abstractBase to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to abstract_base property setter (gets validation automatically)
        """
        self.abstract_base = value  # Delegates to property setter
        return self

    def getContextData(self) -> List["ApplicationComposite"]:
        """
        AUTOSAR-compliant getter for contextData.
        
        Returns:
            The contextData value
        
        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def getRootData(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootData.
        
        Returns:
            The rootData value
        
        Note:
            Delegates to root_data property (CODING_RULE_V2_00017)
        """
        return self.root_data  # Delegates to property

    def setRootData(self, value: RefType) -> "DataPrototypeInPortInterfaceInstanceRef":
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

    def getTargetData(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetData.
        
        Returns:
            The targetData value
        
        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: RefType) -> "DataPrototypeInPortInterfaceInstanceRef":
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

    def with_abstract_base(self, value: Optional["PortInterface"]) -> "DataPrototypeInPortInterfaceInstanceRef":
        """
        Set abstractBase and return self for chaining.
        
        Args:
            value: The abstractBase to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_abstract_base("value")
        """
        self.abstract_base = value  # Use property setter (gets validation)
        return self

    def with_root_data(self, value: Optional[RefType]) -> "DataPrototypeInPortInterfaceInstanceRef":
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

    def with_target_data(self, value: RefType) -> "DataPrototypeInPortInterfaceInstanceRef":
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