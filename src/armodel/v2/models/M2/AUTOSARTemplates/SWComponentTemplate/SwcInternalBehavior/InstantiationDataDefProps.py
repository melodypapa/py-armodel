"""
AUTOSAR Package - InstantiationDataDefProps

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::InstantiationDataDefProps
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)




class InstantiationDataDefProps(ARObject):
    """
    This is a general class allowing to apply additional SwDataDefProps to
    particular instantiations of a Data Prototype. Typically the accessibility
    and further information like alias names for a particular data is modeled on
    the level of DataPrototypes (especially VariableDataPrototypes,
    ParameterDataPrototypes). But due to the recursive structure of the
    meta-model concerning data types (a composite (data) type consists out of
    data prototypes) a part of the MCD information is described in the data type
    (in case of Application CompositeDataType). This is a strong restriction in
    the reuse of data typed because the data type should be re-used for
    different VariableDataPrototypes and ParameterDataPrototypes to guarantee
    type compatibility on C-implementation level (e.g. data of a Port is stored
    in PIM or a ParameterDataPrototype used as ROM Block and shall be typed by
    the same data type as NVRAM Block). This class overcomes such a restriction
    if applied properly.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::InstantiationDataDefProps::InstantiationDataDefProps
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 588, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the particular DataPrototype in the context of a
        # composite ParameterData which the swDataDefProps shall be.
        self._parameter: Optional["RefType"] = None

    @property
    def parameter(self) -> Optional["RefType"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: Optional["RefType"]) -> None:
        """
        Set parameter with validation.
        
        Args:
            value: The parameter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameter = None
            return

        self._parameter = value
        # These are the particular data definition properties which be applied.
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
        # This reference identifies the particular DataPrototype the context of a
        # composite VariableData which the swDataDefProps shall be.
        self._variableInstance: Optional["RefType"] = None

    @property
    def variable_instance(self) -> Optional["RefType"]:
        """Get variableInstance (Pythonic accessor)."""
        return self._variableInstance

    @variable_instance.setter
    def variable_instance(self, value: Optional["RefType"]) -> None:
        """
        Set variableInstance with validation.
        
        Args:
            value: The variableInstance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variableInstance = None
            return

        self._variableInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getParameter(self) -> "RefType":
        """
        AUTOSAR-compliant getter for parameter.
        
        Returns:
            The parameter value
        
        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def setParameter(self, value: "RefType") -> "InstantiationDataDefProps":
        """
        AUTOSAR-compliant setter for parameter with method chaining.
        
        Args:
            value: The parameter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to parameter property setter (gets validation automatically)
        """
        self.parameter = value  # Delegates to property setter
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

    def setSwDataDef(self, value: "SwDataDefProps") -> "InstantiationDataDefProps":
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

    def getVariableInstance(self) -> "RefType":
        """
        AUTOSAR-compliant getter for variableInstance.
        
        Returns:
            The variableInstance value
        
        Note:
            Delegates to variable_instance property (CODING_RULE_V2_00017)
        """
        return self.variable_instance  # Delegates to property

    def setVariableInstance(self, value: "RefType") -> "InstantiationDataDefProps":
        """
        AUTOSAR-compliant setter for variableInstance with method chaining.
        
        Args:
            value: The variableInstance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to variable_instance property setter (gets validation automatically)
        """
        self.variable_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_parameter(self, value: Optional[RefType]) -> "InstantiationDataDefProps":
        """
        Set parameter and return self for chaining.
        
        Args:
            value: The parameter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "InstantiationDataDefProps":
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

    def with_variable_instance(self, value: Optional[RefType]) -> "InstantiationDataDefProps":
        """
        Set variableInstance and return self for chaining.
        
        Args:
            value: The variableInstance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_variable_instance("value")
        """
        self.variable_instance = value  # Use property setter (gets validation)
        return self