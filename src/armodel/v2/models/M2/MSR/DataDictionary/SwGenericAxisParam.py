from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwGenericAxisParam(ARObject):
    """
    This meta-class describes a specific parameter of a generic axis. The name
    of the parameter is defined through a reference to a parameter type defined
    on a corresponding axis type. The value of the parameter is given here in
    case that it is not changeable during calibration. Example is shift / offset
    in a fixed axis.
    
    Package: M2::MSR::DataDictionary::Axis::SwGenericAxisParam
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 356, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Parameter type defined on a corresponding axis type.
        # References can only be made to axis parameters types defined within the
                # referenced axis type.
        # Numerical * attr This attribute represents the value of the generic axis.
        self._swGenericAxis: Optional["SwGenericAxisParam"] = None

    @property
    def sw_generic_axis(self) -> Optional["SwGenericAxisParam"]:
        """Get swGenericAxis (Pythonic accessor)."""
        return self._swGenericAxis

    @sw_generic_axis.setter
    def sw_generic_axis(self, value: Optional["SwGenericAxisParam"]) -> None:
        """
        Set swGenericAxis with validation.
        
        Args:
            value: The swGenericAxis to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swGenericAxis = None
            return

        if not isinstance(value, SwGenericAxisParam):
            raise TypeError(
                f"swGenericAxis must be SwGenericAxisParam or None, got {type(value).__name__}"
            )
        self._swGenericAxis = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwGenericAxis(self) -> "SwGenericAxisParam":
        """
        AUTOSAR-compliant getter for swGenericAxis.
        
        Returns:
            The swGenericAxis value
        
        Note:
            Delegates to sw_generic_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_generic_axis  # Delegates to property

    def setSwGenericAxis(self, value: "SwGenericAxisParam") -> "SwGenericAxisParam":
        """
        AUTOSAR-compliant setter for swGenericAxis with method chaining.
        
        Args:
            value: The swGenericAxis to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_generic_axis property setter (gets validation automatically)
        """
        self.sw_generic_axis = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_generic_axis(self, value: Optional["SwGenericAxisParam"]) -> "SwGenericAxisParam":
        """
        Set swGenericAxis and return self for chaining.
        
        Args:
            value: The swGenericAxis to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_generic_axis("value")
        """
        self.sw_generic_axis = value  # Use property setter (gets validation)
        return self