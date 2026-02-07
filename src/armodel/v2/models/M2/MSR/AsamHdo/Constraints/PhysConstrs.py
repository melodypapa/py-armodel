from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class PhysConstrs(ARObject):
    """
    This meta-class represents the ability to express physical constraints.
    Therefore it has (in opposite to InternalConstrs) a reference to a Unit.
    
    Package: M2::MSR::AsamHdo::Constraints::GlobalConstraints::PhysConstrs
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 406, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2043, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the lower limit of the constraint.
        self._lowerLimit: Optional["Limit"] = None

    @property
    def lower_limit(self) -> Optional["Limit"]:
        """Get lowerLimit (Pythonic accessor)."""
        return self._lowerLimit

    @lower_limit.setter
    def lower_limit(self, value: Optional["Limit"]) -> None:
        """
        Set lowerLimit with validation.
        
        Args:
            value: The lowerLimit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerLimit = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"lowerLimit must be Limit or None, got {type(value).__name__}"
            )
        self._lowerLimit = value
        # Maximum difference that is permitted between two if the constraint is applied
        # to an axis.
        self._maxDiff: Optional["Numerical"] = None

    @property
    def max_diff(self) -> Optional["Numerical"]:
        """Get maxDiff (Pythonic accessor)."""
        return self._maxDiff

    @max_diff.setter
    def max_diff(self, value: Optional["Numerical"]) -> None:
        """
        Set maxDiff with validation.
        
        Args:
            value: The maxDiff to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDiff = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"maxDiff must be Numerical or None, got {type(value).__name__}"
            )
        self._maxDiff = value
        # This element specifies the maximum slope that may be curves and maps.
        self._maxGradient: Optional["Numerical"] = None

    @property
    def max_gradient(self) -> Optional["Numerical"]:
        """Get maxGradient (Pythonic accessor)."""
        return self._maxGradient

    @max_gradient.setter
    def max_gradient(self, value: Optional["Numerical"]) -> None:
        """
        Set maxGradient with validation.
        
        Args:
            value: The maxGradient to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxGradient = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"maxGradient must be Numerical or None, got {type(value).__name__}"
            )
        self._maxGradient = value
        # This specifies the monotony constraints on the data that this applies only to
        # curves and maps.
        self._monotony: Optional["MonotonyEnum"] = None

    @property
    def monotony(self) -> Optional["MonotonyEnum"]:
        """Get monotony (Pythonic accessor)."""
        return self._monotony

    @monotony.setter
    def monotony(self, value: Optional["MonotonyEnum"]) -> None:
        """
        Set monotony with validation.
        
        Args:
            value: The monotony to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._monotony = None
            return

        if not isinstance(value, MonotonyEnum):
            raise TypeError(
                f"monotony must be MonotonyEnum or None, got {type(value).__name__}"
            )
        self._monotony = value
        # This is one particular scale which contributes to the data.
        self._scaleConstr: List["ScaleConstr"] = []

    @property
    def scale_constr(self) -> List["ScaleConstr"]:
        """Get scaleConstr (Pythonic accessor)."""
        return self._scaleConstr
        # This is the unit to which the physical constraints relate to.
        # it is the physical unit of the specified limits.
        self._unit: Optional["Unit"] = None

    @property
    def unit(self) -> Optional["Unit"]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional["Unit"]) -> None:
        """
        Set unit with validation.
        
        Args:
            value: The unit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unit = None
            return

        if not isinstance(value, Unit):
            raise TypeError(
                f"unit must be Unit or None, got {type(value).__name__}"
            )
        self._unit = value
        # This specifies the upper limit of the constraint.
        self._upperLimit: Optional["Limit"] = None

    @property
    def upper_limit(self) -> Optional["Limit"]:
        """Get upperLimit (Pythonic accessor)."""
        return self._upperLimit

    @upper_limit.setter
    def upper_limit(self, value: Optional["Limit"]) -> None:
        """
        Set upperLimit with validation.
        
        Args:
            value: The upperLimit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperLimit = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"upperLimit must be Limit or None, got {type(value).__name__}"
            )
        self._upperLimit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLowerLimit(self) -> "Limit":
        """
        AUTOSAR-compliant getter for lowerLimit.
        
        Returns:
            The lowerLimit value
        
        Note:
            Delegates to lower_limit property (CODING_RULE_V2_00017)
        """
        return self.lower_limit  # Delegates to property

    def setLowerLimit(self, value: "Limit") -> "PhysConstrs":
        """
        AUTOSAR-compliant setter for lowerLimit with method chaining.
        
        Args:
            value: The lowerLimit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to lower_limit property setter (gets validation automatically)
        """
        self.lower_limit = value  # Delegates to property setter
        return self

    def getMaxDiff(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for maxDiff.
        
        Returns:
            The maxDiff value
        
        Note:
            Delegates to max_diff property (CODING_RULE_V2_00017)
        """
        return self.max_diff  # Delegates to property

    def setMaxDiff(self, value: "Numerical") -> "PhysConstrs":
        """
        AUTOSAR-compliant setter for maxDiff with method chaining.
        
        Args:
            value: The maxDiff to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_diff property setter (gets validation automatically)
        """
        self.max_diff = value  # Delegates to property setter
        return self

    def getMaxGradient(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for maxGradient.
        
        Returns:
            The maxGradient value
        
        Note:
            Delegates to max_gradient property (CODING_RULE_V2_00017)
        """
        return self.max_gradient  # Delegates to property

    def setMaxGradient(self, value: "Numerical") -> "PhysConstrs":
        """
        AUTOSAR-compliant setter for maxGradient with method chaining.
        
        Args:
            value: The maxGradient to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_gradient property setter (gets validation automatically)
        """
        self.max_gradient = value  # Delegates to property setter
        return self

    def getMonotony(self) -> "MonotonyEnum":
        """
        AUTOSAR-compliant getter for monotony.
        
        Returns:
            The monotony value
        
        Note:
            Delegates to monotony property (CODING_RULE_V2_00017)
        """
        return self.monotony  # Delegates to property

    def setMonotony(self, value: "MonotonyEnum") -> "PhysConstrs":
        """
        AUTOSAR-compliant setter for monotony with method chaining.
        
        Args:
            value: The monotony to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to monotony property setter (gets validation automatically)
        """
        self.monotony = value  # Delegates to property setter
        return self

    def getScaleConstr(self) -> List["ScaleConstr"]:
        """
        AUTOSAR-compliant getter for scaleConstr.
        
        Returns:
            The scaleConstr value
        
        Note:
            Delegates to scale_constr property (CODING_RULE_V2_00017)
        """
        return self.scale_constr  # Delegates to property

    def getUnit(self) -> "Unit":
        """
        AUTOSAR-compliant getter for unit.
        
        Returns:
            The unit value
        
        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: "Unit") -> "PhysConstrs":
        """
        AUTOSAR-compliant setter for unit with method chaining.
        
        Args:
            value: The unit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to unit property setter (gets validation automatically)
        """
        self.unit = value  # Delegates to property setter
        return self

    def getUpperLimit(self) -> "Limit":
        """
        AUTOSAR-compliant getter for upperLimit.
        
        Returns:
            The upperLimit value
        
        Note:
            Delegates to upper_limit property (CODING_RULE_V2_00017)
        """
        return self.upper_limit  # Delegates to property

    def setUpperLimit(self, value: "Limit") -> "PhysConstrs":
        """
        AUTOSAR-compliant setter for upperLimit with method chaining.
        
        Args:
            value: The upperLimit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to upper_limit property setter (gets validation automatically)
        """
        self.upper_limit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lower_limit(self, value: Optional["Limit"]) -> "PhysConstrs":
        """
        Set lowerLimit and return self for chaining.
        
        Args:
            value: The lowerLimit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_lower_limit("value")
        """
        self.lower_limit = value  # Use property setter (gets validation)
        return self

    def with_max_diff(self, value: Optional["Numerical"]) -> "PhysConstrs":
        """
        Set maxDiff and return self for chaining.
        
        Args:
            value: The maxDiff to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_diff("value")
        """
        self.max_diff = value  # Use property setter (gets validation)
        return self

    def with_max_gradient(self, value: Optional["Numerical"]) -> "PhysConstrs":
        """
        Set maxGradient and return self for chaining.
        
        Args:
            value: The maxGradient to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_gradient("value")
        """
        self.max_gradient = value  # Use property setter (gets validation)
        return self

    def with_monotony(self, value: Optional["MonotonyEnum"]) -> "PhysConstrs":
        """
        Set monotony and return self for chaining.
        
        Args:
            value: The monotony to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_monotony("value")
        """
        self.monotony = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional["Unit"]) -> "PhysConstrs":
        """
        Set unit and return self for chaining.
        
        Args:
            value: The unit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_unit("value")
        """
        self.unit = value  # Use property setter (gets validation)
        return self

    def with_upper_limit(self, value: Optional["Limit"]) -> "PhysConstrs":
        """
        Set upperLimit and return self for chaining.
        
        Args:
            value: The upperLimit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_upper_limit("value")
        """
        self.upper_limit = value  # Use property setter (gets validation)
        return self