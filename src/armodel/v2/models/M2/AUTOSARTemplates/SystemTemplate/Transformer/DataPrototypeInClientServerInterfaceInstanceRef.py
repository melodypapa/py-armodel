from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DataPrototypeInClientServerInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::InstanceRef::DataPrototypeInClientServerInterfaceInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 788, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._base: Optional["ClientServerInterface"] = None

    @property
    def base(self) -> Optional["ClientServerInterface"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["ClientServerInterface"]) -> None:
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

        if not isinstance(value, ClientServerInterface):
            raise TypeError(
                f"base must be ClientServerInterface or None, got {type(value).__name__}"
            )
        self._base = value
        # Tags: xml.
        # sequenceOffset=20.
        self._contextData: List["ApplicationComposite"] = []

    @property
    def context_data(self) -> List["ApplicationComposite"]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData
        # Tags: xml.
        # sequenceOffset=10.
        self._rootDataPrototypeInCs: RefType = None

    @property
    def root_data_prototype_in_cs(self) -> RefType:
        """Get rootDataPrototypeInCs (Pythonic accessor)."""
        return self._rootDataPrototypeInCs

    @root_data_prototype_in_cs.setter
    def root_data_prototype_in_cs(self, value: RefType) -> None:
        """
        Set rootDataPrototypeInCs with validation.
        
        Args:
            value: The rootDataPrototypeInCs to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rootDataPrototypeInCs = None
            return

        self._rootDataPrototypeInCs = value
        # Tags: xml.
        # sequenceOffset=30.
        self._targetDataPrototypeInCs: RefType = None

    @property
    def target_data_prototype_in_cs(self) -> RefType:
        """Get targetDataPrototypeInCs (Pythonic accessor)."""
        return self._targetDataPrototypeInCs

    @target_data_prototype_in_cs.setter
    def target_data_prototype_in_cs(self, value: RefType) -> None:
        """
        Set targetDataPrototypeInCs with validation.
        
        Args:
            value: The targetDataPrototypeInCs to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetDataPrototypeInCs = None
            return

        self._targetDataPrototypeInCs = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "ClientServerInterface":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "ClientServerInterface") -> "DataPrototypeInClientServerInterfaceInstanceRef":
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

    def getContextData(self) -> List["ApplicationComposite"]:
        """
        AUTOSAR-compliant getter for contextData.
        
        Returns:
            The contextData value
        
        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def getRootDataPrototypeInCs(self) -> RefType:
        """
        AUTOSAR-compliant getter for rootDataPrototypeInCs.
        
        Returns:
            The rootDataPrototypeInCs value
        
        Note:
            Delegates to root_data_prototype_in_cs property (CODING_RULE_V2_00017)
        """
        return self.root_data_prototype_in_cs  # Delegates to property

    def setRootDataPrototypeInCs(self, value: RefType) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        AUTOSAR-compliant setter for rootDataPrototypeInCs with method chaining.
        
        Args:
            value: The rootDataPrototypeInCs to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to root_data_prototype_in_cs property setter (gets validation automatically)
        """
        self.root_data_prototype_in_cs = value  # Delegates to property setter
        return self

    def getTargetDataPrototypeInCs(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetDataPrototypeInCs.
        
        Returns:
            The targetDataPrototypeInCs value
        
        Note:
            Delegates to target_data_prototype_in_cs property (CODING_RULE_V2_00017)
        """
        return self.target_data_prototype_in_cs  # Delegates to property

    def setTargetDataPrototypeInCs(self, value: RefType) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        AUTOSAR-compliant setter for targetDataPrototypeInCs with method chaining.
        
        Args:
            value: The targetDataPrototypeInCs to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_data_prototype_in_cs property setter (gets validation automatically)
        """
        self.target_data_prototype_in_cs = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["ClientServerInterface"]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
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

    def with_root_data_prototype_in_cs(self, value: Optional[RefType]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        Set rootDataPrototypeInCs and return self for chaining.
        
        Args:
            value: The rootDataPrototypeInCs to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_root_data_prototype_in_cs("value")
        """
        self.root_data_prototype_in_cs = value  # Use property setter (gets validation)
        return self

    def with_target_data_prototype_in_cs(self, value: Optional[RefType]) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """
        Set targetDataPrototypeInCs and return self for chaining.
        
        Args:
            value: The targetDataPrototypeInCs to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_data_prototype_in_cs("value")
        """
        self.target_data_prototype_in_cs = value  # Use property setter (gets validation)
        return self