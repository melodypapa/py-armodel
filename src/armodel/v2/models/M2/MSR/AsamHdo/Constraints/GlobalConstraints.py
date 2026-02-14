"""
AUTOSAR Package - GlobalConstraints

Package: M2::MSR::AsamHdo::Constraints::GlobalConstraints
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
    Limit,
    MonotonyEnum,
    Numerical,
)


class DataConstr(ARElement):
    """
    This meta-class represents the ability to specify constraints on data.

    Package: M2::MSR::AsamHdo::Constraints::GlobalConstraints::DataConstr

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 310, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 405, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 44, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 179, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular rule within the data constraints.
        self._dataConstrRule: List[DataConstrRule] = []

    @property
    def data_constr_rule(self) -> List[DataConstrRule]:
        """Get dataConstrRule (Pythonic accessor)."""
        return self._dataConstrRule

    def with_data_constr_rule(self, value):
        """
        Set data_constr_rule and return self for chaining.

        Args:
            value: The data_constr_rule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_constr_rule("value")
        """
        self.data_constr_rule = value  # Use property setter (gets validation)
        return self

    def with_scale_constr(self, value):
        """
        Set scale_constr and return self for chaining.

        Args:
            value: The scale_constr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scale_constr("value")
        """
        self.scale_constr = value  # Use property setter (gets validation)
        return self

    def with_scale_constr(self, value):
        """
        Set scale_constr and return self for chaining.

        Args:
            value: The scale_constr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scale_constr("value")
        """
        self.scale_constr = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataConstrRule(self) -> List[DataConstrRule]:
        """
        AUTOSAR-compliant getter for dataConstrRule.

        Returns:
            The dataConstrRule value

        Note:
            Delegates to data_constr_rule property (CODING_RULE_V2_00017)
        """
        return self.data_constr_rule  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DataConstrRule(ARObject):
    """
    This meta-class represents the ability to express one specific data
    constraint rule.

    Package: M2::MSR::AsamHdo::Constraints::GlobalConstraints::DataConstrRule

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 405, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 45, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute describes the category of a constraint.
        # One functions is in the area of constraint violation, where be used from a
                # certain level, to produce error the level, the more stringent the check.
        # distinguish hard or soft limits.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._constrLevel: Optional[Integer] = None

    @property
    def constr_level(self) -> Optional[Integer]:
        """Get constrLevel (Pythonic accessor)."""
        return self._constrLevel

    @constr_level.setter
    def constr_level(self, value: Optional[Integer]) -> None:
        """
        Set constrLevel with validation.

        Args:
            value: The constrLevel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._constrLevel = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"constrLevel must be Integer or int or None, got {type(value).__name__}"
            )
        self._constrLevel = value
        # domain).
        self._internalConstrs: Optional[InternalConstrs] = None

    @property
    def internal_constrs(self) -> Optional[InternalConstrs]:
        """Get internalConstrs (Pythonic accessor)."""
        return self._internalConstrs

    @internal_constrs.setter
    def internal_constrs(self, value: Optional[InternalConstrs]) -> None:
        """
        Set internalConstrs with validation.

        Args:
            value: The internalConstrs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._internalConstrs = None
            return

        if not isinstance(value, InternalConstrs):
            raise TypeError(
                f"internalConstrs must be InternalConstrs or None, got {type(value).__name__}"
            )
        self._internalConstrs = value
        # domain).
        self._physConstrs: Optional[PhysConstrs] = None

    @property
    def phys_constrs(self) -> Optional[PhysConstrs]:
        """Get physConstrs (Pythonic accessor)."""
        return self._physConstrs

    @phys_constrs.setter
    def phys_constrs(self, value: Optional[PhysConstrs]) -> None:
        """
        Set physConstrs with validation.

        Args:
            value: The physConstrs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physConstrs = None
            return

        if not isinstance(value, PhysConstrs):
            raise TypeError(
                f"physConstrs must be PhysConstrs or None, got {type(value).__name__}"
            )
        self._physConstrs = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConstrLevel(self) -> Integer:
        """
        AUTOSAR-compliant getter for constrLevel.

        Returns:
            The constrLevel value

        Note:
            Delegates to constr_level property (CODING_RULE_V2_00017)
        """
        return self.constr_level  # Delegates to property

    def setConstrLevel(self, value: Integer) -> DataConstrRule:
        """
        AUTOSAR-compliant setter for constrLevel with method chaining.

        Args:
            value: The constrLevel to set

        Returns:
            self for method chaining

        Note:
            Delegates to constr_level property setter (gets validation automatically)
        """
        self.constr_level = value  # Delegates to property setter
        return self

    def getInternalConstrs(self) -> InternalConstrs:
        """
        AUTOSAR-compliant getter for internalConstrs.

        Returns:
            The internalConstrs value

        Note:
            Delegates to internal_constrs property (CODING_RULE_V2_00017)
        """
        return self.internal_constrs  # Delegates to property

    def setInternalConstrs(self, value: InternalConstrs) -> DataConstrRule:
        """
        AUTOSAR-compliant setter for internalConstrs with method chaining.

        Args:
            value: The internalConstrs to set

        Returns:
            self for method chaining

        Note:
            Delegates to internal_constrs property setter (gets validation automatically)
        """
        self.internal_constrs = value  # Delegates to property setter
        return self

    def getPhysConstrs(self) -> PhysConstrs:
        """
        AUTOSAR-compliant getter for physConstrs.

        Returns:
            The physConstrs value

        Note:
            Delegates to phys_constrs property (CODING_RULE_V2_00017)
        """
        return self.phys_constrs  # Delegates to property

    def setPhysConstrs(self, value: PhysConstrs) -> DataConstrRule:
        """
        AUTOSAR-compliant setter for physConstrs with method chaining.

        Args:
            value: The physConstrs to set

        Returns:
            self for method chaining

        Note:
            Delegates to phys_constrs property setter (gets validation automatically)
        """
        self.phys_constrs = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_constr_level(self, value: Optional[Integer]) -> DataConstrRule:
        """
        Set constrLevel and return self for chaining.

        Args:
            value: The constrLevel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_constr_level("value")
        """
        self.constr_level = value  # Use property setter (gets validation)
        return self

    def with_internal_constrs(self, value: Optional[InternalConstrs]) -> DataConstrRule:
        """
        Set internalConstrs and return self for chaining.

        Args:
            value: The internalConstrs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_internal_constrs("value")
        """
        self.internal_constrs = value  # Use property setter (gets validation)
        return self

    def with_phys_constrs(self, value: Optional[PhysConstrs]) -> DataConstrRule:
        """
        Set physConstrs and return self for chaining.

        Args:
            value: The physConstrs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_phys_constrs("value")
        """
        self.phys_constrs = value  # Use property setter (gets validation)
        return self



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
        self._lowerLimit: Optional[Limit] = None

    @property
    def lower_limit(self) -> Optional[Limit]:
        """Get lowerLimit (Pythonic accessor)."""
        return self._lowerLimit

    @lower_limit.setter
    def lower_limit(self, value: Optional[Limit]) -> None:
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
        # to an axis.
        self._maxDiff: Optional[Numerical] = None

    @property
    def max_diff(self) -> Optional[Numerical]:
        """Get maxDiff (Pythonic accessor)."""
        return self._maxDiff

    @max_diff.setter
    def max_diff(self, value: Optional[Numerical]) -> None:
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
        self._maxGradient: Optional[Numerical] = None

    @property
    def max_gradient(self) -> Optional[Numerical]:
        """Get maxGradient (Pythonic accessor)."""
        return self._maxGradient

    @max_gradient.setter
    def max_gradient(self, value: Optional[Numerical]) -> None:
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
        # curves and maps.
        self._monotony: Optional[MonotonyEnum] = None

    @property
    def monotony(self) -> Optional[MonotonyEnum]:
        """Get monotony (Pythonic accessor)."""
        return self._monotony

    @monotony.setter
    def monotony(self, value: Optional[MonotonyEnum]) -> None:
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
        self._scaleConstr: List[ScaleConstr] = []

    @property
    def scale_constr(self) -> List[ScaleConstr]:
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
        self._upperLimit: Optional[Limit] = None

    @property
    def upper_limit(self) -> Optional[Limit]:
        """Get upperLimit (Pythonic accessor)."""
        return self._upperLimit

    @upper_limit.setter
    def upper_limit(self, value: Optional[Limit]) -> None:
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

    def getLowerLimit(self) -> Limit:
        """
        AUTOSAR-compliant getter for lowerLimit.

        Returns:
            The lowerLimit value

        Note:
            Delegates to lower_limit property (CODING_RULE_V2_00017)
        """
        return self.lower_limit  # Delegates to property

    def setLowerLimit(self, value: Limit) -> PhysConstrs:
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

    def getMaxDiff(self) -> Numerical:
        """
        AUTOSAR-compliant getter for maxDiff.

        Returns:
            The maxDiff value

        Note:
            Delegates to max_diff property (CODING_RULE_V2_00017)
        """
        return self.max_diff  # Delegates to property

    def setMaxDiff(self, value: Numerical) -> PhysConstrs:
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

    def getMaxGradient(self) -> Numerical:
        """
        AUTOSAR-compliant getter for maxGradient.

        Returns:
            The maxGradient value

        Note:
            Delegates to max_gradient property (CODING_RULE_V2_00017)
        """
        return self.max_gradient  # Delegates to property

    def setMaxGradient(self, value: Numerical) -> PhysConstrs:
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

    def getMonotony(self) -> MonotonyEnum:
        """
        AUTOSAR-compliant getter for monotony.

        Returns:
            The monotony value

        Note:
            Delegates to monotony property (CODING_RULE_V2_00017)
        """
        return self.monotony  # Delegates to property

    def setMonotony(self, value: MonotonyEnum) -> PhysConstrs:
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

    def getScaleConstr(self) -> List[ScaleConstr]:
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

    def setUnit(self, value: "Unit") -> PhysConstrs:
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

    def getUpperLimit(self) -> Limit:
        """
        AUTOSAR-compliant getter for upperLimit.

        Returns:
            The upperLimit value

        Note:
            Delegates to upper_limit property (CODING_RULE_V2_00017)
        """
        return self.upper_limit  # Delegates to property

    def setUpperLimit(self, value: Limit) -> PhysConstrs:
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

    def with_lower_limit(self, value: Optional[Limit]) -> PhysConstrs:
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

    def with_max_diff(self, value: Optional[Numerical]) -> PhysConstrs:
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

    def with_max_gradient(self, value: Optional[Numerical]) -> PhysConstrs:
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

    def with_monotony(self, value: Optional[MonotonyEnum]) -> PhysConstrs:
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

    def with_unit(self, value: Optional["Unit"]) -> PhysConstrs:
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

    def with_upper_limit(self, value: Optional[Limit]) -> PhysConstrs:
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



class InternalConstrs(ARObject):
    """
    This meta-class represents the ability to express internal constraints.

    Package: M2::MSR::AsamHdo::Constraints::GlobalConstraints::InternalConstrs

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 407, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the lower limit of the constraint.
        self._lowerLimit: Optional[Limit] = None

    @property
    def lower_limit(self) -> Optional[Limit]:
        """Get lowerLimit (Pythonic accessor)."""
        return self._lowerLimit

    @lower_limit.setter
    def lower_limit(self, value: Optional[Limit]) -> None:
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
        # to an axis.
        self._maxDiff: Optional[Numerical] = None

    @property
    def max_diff(self) -> Optional[Numerical]:
        """Get maxDiff (Pythonic accessor)."""
        return self._maxDiff

    @max_diff.setter
    def max_diff(self, value: Optional[Numerical]) -> None:
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
        self._maxGradient: Optional[Numerical] = None

    @property
    def max_gradient(self) -> Optional[Numerical]:
        """Get maxGradient (Pythonic accessor)."""
        return self._maxGradient

    @max_gradient.setter
    def max_gradient(self, value: Optional[Numerical]) -> None:
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
                # limits.
        # The following table monotony characteristics which are to be filled
                # corresponding values.
        # element has no contents or if it is omitted, "no the default content.
        self._monotony: Optional[MonotonyEnum] = None

    @property
    def monotony(self) -> Optional[MonotonyEnum]:
        """Get monotony (Pythonic accessor)."""
        return self._monotony

    @monotony.setter
    def monotony(self, value: Optional[MonotonyEnum]) -> None:
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
        self._scaleConstr: List[ScaleConstr] = []

    @property
    def scale_constr(self) -> List[ScaleConstr]:
        """Get scaleConstr (Pythonic accessor)."""
        return self._scaleConstr
        # This specifies the upper limit defined by the constraint.
        self._upperLimit: Optional[Limit] = None

    @property
    def upper_limit(self) -> Optional[Limit]:
        """Get upperLimit (Pythonic accessor)."""
        return self._upperLimit

    @upper_limit.setter
    def upper_limit(self, value: Optional[Limit]) -> None:
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

    def getLowerLimit(self) -> Limit:
        """
        AUTOSAR-compliant getter for lowerLimit.

        Returns:
            The lowerLimit value

        Note:
            Delegates to lower_limit property (CODING_RULE_V2_00017)
        """
        return self.lower_limit  # Delegates to property

    def setLowerLimit(self, value: Limit) -> InternalConstrs:
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

    def getMaxDiff(self) -> Numerical:
        """
        AUTOSAR-compliant getter for maxDiff.

        Returns:
            The maxDiff value

        Note:
            Delegates to max_diff property (CODING_RULE_V2_00017)
        """
        return self.max_diff  # Delegates to property

    def setMaxDiff(self, value: Numerical) -> InternalConstrs:
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

    def getMaxGradient(self) -> Numerical:
        """
        AUTOSAR-compliant getter for maxGradient.

        Returns:
            The maxGradient value

        Note:
            Delegates to max_gradient property (CODING_RULE_V2_00017)
        """
        return self.max_gradient  # Delegates to property

    def setMaxGradient(self, value: Numerical) -> InternalConstrs:
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

    def getMonotony(self) -> MonotonyEnum:
        """
        AUTOSAR-compliant getter for monotony.

        Returns:
            The monotony value

        Note:
            Delegates to monotony property (CODING_RULE_V2_00017)
        """
        return self.monotony  # Delegates to property

    def setMonotony(self, value: MonotonyEnum) -> InternalConstrs:
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

    def getScaleConstr(self) -> List[ScaleConstr]:
        """
        AUTOSAR-compliant getter for scaleConstr.

        Returns:
            The scaleConstr value

        Note:
            Delegates to scale_constr property (CODING_RULE_V2_00017)
        """
        return self.scale_constr  # Delegates to property

    def getUpperLimit(self) -> Limit:
        """
        AUTOSAR-compliant getter for upperLimit.

        Returns:
            The upperLimit value

        Note:
            Delegates to upper_limit property (CODING_RULE_V2_00017)
        """
        return self.upper_limit  # Delegates to property

    def setUpperLimit(self, value: Limit) -> InternalConstrs:
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

    def with_lower_limit(self, value: Optional[Limit]) -> InternalConstrs:
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

    def with_max_diff(self, value: Optional[Numerical]) -> InternalConstrs:
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

    def with_max_gradient(self, value: Optional[Numerical]) -> InternalConstrs:
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

    def with_monotony(self, value: Optional[MonotonyEnum]) -> InternalConstrs:
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

    def with_upper_limit(self, value: Optional[Limit]) -> InternalConstrs:
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



class ScaleConstr(ARObject):
    """
    This meta-class represents the ability to specify constraints as a list of
    intervals (called scales).

    Package: M2::MSR::AsamHdo::Constraints::GlobalConstraints::ScaleConstr

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1003, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # <desc> represents a general but brief description of the in question.
        self._desc: Optional["MultiLanguageOverview"] = None

    @property
    def desc(self) -> Optional["MultiLanguageOverview"]:
        """Get desc (Pythonic accessor)."""
        return self._desc

    @desc.setter
    def desc(self, value: Optional["MultiLanguageOverview"]) -> None:
        """
        Set desc with validation.

        Args:
            value: The desc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._desc = None
            return

        if not isinstance(value, MultiLanguageOverview):
            raise TypeError(
                f"desc must be MultiLanguageOverview or None, got {type(value).__name__}"
            )
        self._desc = value
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._lowerLimit: Optional[Limit] = None

    @property
    def lower_limit(self) -> Optional[Limit]:
        """Get lowerLimit (Pythonic accessor)."""
        return self._lowerLimit

    @lower_limit.setter
    def lower_limit(self, value: Optional[Limit]) -> None:
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
        # for example be used to create more specific a constraint checker.
        # The constraints cannot in the meta-model, therefore shortLabel is substitute
                # for shortName.
        self._shortLabel: Optional[Identifier] = None

    @property
    def short_label(self) -> Optional[Identifier]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional[Identifier]) -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortLabel must be Identifier or str or None, got {type(value).__name__}"
            )
        self._shortLabel = value
        self._upperLimit: Optional[Limit] = None

    @property
    def upper_limit(self) -> Optional[Limit]:
        """Get upperLimit (Pythonic accessor)."""
        return self._upperLimit

    @upper_limit.setter
    def upper_limit(self, value: Optional[Limit]) -> None:
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
        # If the attribute is missing then the is "VALID".
        self._validity: Optional["ScaleConstrValidity"] = None

    @property
    def validity(self) -> Optional["ScaleConstrValidity"]:
        """Get validity (Pythonic accessor)."""
        return self._validity

    @validity.setter
    def validity(self, value: Optional["ScaleConstrValidity"]) -> None:
        """
        Set validity with validation.

        Args:
            value: The validity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._validity = None
            return

        if not isinstance(value, ScaleConstrValidity):
            raise TypeError(
                f"validity must be ScaleConstrValidity or None, got {type(value).__name__}"
            )
        self._validity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDesc(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for desc.

        Returns:
            The desc value

        Note:
            Delegates to desc property (CODING_RULE_V2_00017)
        """
        return self.desc  # Delegates to property

    def setDesc(self, value: "MultiLanguageOverview") -> ScaleConstr:
        """
        AUTOSAR-compliant setter for desc with method chaining.

        Args:
            value: The desc to set

        Returns:
            self for method chaining

        Note:
            Delegates to desc property setter (gets validation automatically)
        """
        self.desc = value  # Delegates to property setter
        return self

    def getLowerLimit(self) -> Limit:
        """
        AUTOSAR-compliant getter for lowerLimit.

        Returns:
            The lowerLimit value

        Note:
            Delegates to lower_limit property (CODING_RULE_V2_00017)
        """
        return self.lower_limit  # Delegates to property

    def setLowerLimit(self, value: Limit) -> ScaleConstr:
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

    def getShortLabel(self) -> Identifier:
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: Identifier) -> ScaleConstr:
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    def getUpperLimit(self) -> Limit:
        """
        AUTOSAR-compliant getter for upperLimit.

        Returns:
            The upperLimit value

        Note:
            Delegates to upper_limit property (CODING_RULE_V2_00017)
        """
        return self.upper_limit  # Delegates to property

    def setUpperLimit(self, value: Limit) -> ScaleConstr:
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

    def getValidity(self) -> "ScaleConstrValidity":
        """
        AUTOSAR-compliant getter for validity.

        Returns:
            The validity value

        Note:
            Delegates to validity property (CODING_RULE_V2_00017)
        """
        return self.validity  # Delegates to property

    def setValidity(self, value: "ScaleConstrValidity") -> ScaleConstr:
        """
        AUTOSAR-compliant setter for validity with method chaining.

        Args:
            value: The validity to set

        Returns:
            self for method chaining

        Note:
            Delegates to validity property setter (gets validation automatically)
        """
        self.validity = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> ScaleConstr:
        """
        Set desc and return self for chaining.

        Args:
            value: The desc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_desc("value")
        """
        self.desc = value  # Use property setter (gets validation)
        return self

    def with_lower_limit(self, value: Optional[Limit]) -> ScaleConstr:
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

    def with_short_label(self, value: Optional[Identifier]) -> ScaleConstr:
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self

    def with_upper_limit(self, value: Optional[Limit]) -> ScaleConstr:
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

    def with_validity(self, value: Optional["ScaleConstrValidity"]) -> ScaleConstr:
        """
        Set validity and return self for chaining.

        Args:
            value: The validity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_validity("value")
        """
        self.validity = value  # Use property setter (gets validation)
        return self
