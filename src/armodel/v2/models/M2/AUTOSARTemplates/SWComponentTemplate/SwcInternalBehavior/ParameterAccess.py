from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class ParameterAccess(AbstractAccessPoint):
    """
    The presence of a ParameterAccess implies that a RunnableEntity needs access
    to a ParameterData Prototype.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::ParameterAccess
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 325, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 586, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the accessed calibration parameter.
        self._accessedParameter: RefType = None

    @property
    def accessed_parameter(self) -> RefType:
        """Get accessedParameter (Pythonic accessor)."""
        return self._accessedParameter

    @accessed_parameter.setter
    def accessed_parameter(self, value: RefType) -> None:
        """
        Set accessedParameter with validation.
        
        Args:
            value: The accessedParameter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessedParameter = None
            return

        self._accessedParameter = value
        # This allows denote instance and access specific mainly input values and
        # common axis.
        self._swDataDef: Optional["SwDataDefProps"] = None

    @property
    def sw_data_def(self) -> Optional["SwDataDefProps"]:
        """Get swDataDef (Pythonic accessor)."""
        return self._swDataDef

    @sw_data_def.setter
    def sw_data_def(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set swDataDef with validation.
        
        Args:
            value: The swDataDef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swDataDef = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"swDataDef must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._swDataDef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessedParameter(self) -> RefType:
        """
        AUTOSAR-compliant getter for accessedParameter.
        
        Returns:
            The accessedParameter value
        
        Note:
            Delegates to accessed_parameter property (CODING_RULE_V2_00017)
        """
        return self.accessed_parameter  # Delegates to property

    def setAccessedParameter(self, value: RefType) -> "ParameterAccess":
        """
        AUTOSAR-compliant setter for accessedParameter with method chaining.
        
        Args:
            value: The accessedParameter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to accessed_parameter property setter (gets validation automatically)
        """
        self.accessed_parameter = value  # Delegates to property setter
        return self

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.
        
        Returns:
            The swDataDef value
        
        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> "ParameterAccess":
        """
        AUTOSAR-compliant setter for swDataDef with method chaining.
        
        Args:
            value: The swDataDef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_data_def property setter (gets validation automatically)
        """
        self.sw_data_def = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_accessed_parameter(self, value: Optional[RefType]) -> "ParameterAccess":
        """
        Set accessedParameter and return self for chaining.
        
        Args:
            value: The accessedParameter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_accessed_parameter("value")
        """
        self.accessed_parameter = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "ParameterAccess":
        """
        Set swDataDef and return self for chaining.
        
        Args:
            value: The swDataDef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_data_def("value")
        """
        self.sw_data_def = value  # Use property setter (gets validation)
        return self