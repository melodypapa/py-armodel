from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwGenericAxisParamType(Identifiable):
    """
    This meta-class describes a generic axis parameter type, namely: •
    Plausibility checks can be specified via dataConstr. • Textual description
    (desc), as a formal description is not of any use, due to the large variety
    of possibilities. • If this parameter contains structures, these can be
    simulated through the recursive use of SwGeneric AxisParamTypes.
    
    Package: M2::MSR::DataDictionary::Axis::SwGenericAxisParamType
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 356, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference denoted data constraints applicable to the parameter.
        self._dataConstr: Optional["DataConstr"] = None

    @property
    def data_constr(self) -> Optional["DataConstr"]:
        """Get dataConstr (Pythonic accessor)."""
        return self._dataConstr

    @data_constr.setter
    def data_constr(self, value: Optional["DataConstr"]) -> None:
        """
        Set dataConstr with validation.
        
        Args:
            value: The dataConstr to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataConstr = None
            return

        if not isinstance(value, DataConstr):
            raise TypeError(
                f"dataConstr must be DataConstr or None, got {type(value).__name__}"
            )
        self._dataConstr = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataConstr(self) -> "DataConstr":
        """
        AUTOSAR-compliant getter for dataConstr.
        
        Returns:
            The dataConstr value
        
        Note:
            Delegates to data_constr property (CODING_RULE_V2_00017)
        """
        return self.data_constr  # Delegates to property

    def setDataConstr(self, value: "DataConstr") -> "SwGenericAxisParamType":
        """
        AUTOSAR-compliant setter for dataConstr with method chaining.
        
        Args:
            value: The dataConstr to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_constr property setter (gets validation automatically)
        """
        self.data_constr = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_constr(self, value: Optional["DataConstr"]) -> "SwGenericAxisParamType":
        """
        Set dataConstr and return self for chaining.
        
        Args:
            value: The dataConstr to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_constr("value")
        """
        self.data_constr = value  # Use property setter (gets validation)
        return self