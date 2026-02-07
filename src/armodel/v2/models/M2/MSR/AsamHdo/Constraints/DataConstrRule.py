from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

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
        self._constrLevel: Optional["Integer"] = None

    @property
    def constr_level(self) -> Optional["Integer"]:
        """Get constrLevel (Pythonic accessor)."""
        return self._constrLevel

    @constr_level.setter
    def constr_level(self, value: Optional["Integer"]) -> None:
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

        if not isinstance(value, Integer):
            raise TypeError(
                f"constrLevel must be Integer or None, got {type(value).__name__}"
            )
        self._constrLevel = value
        # Describes the limitations applicable on the internal opposed to the physical
        # domain).
        self._internalConstrs: Optional["InternalConstrs"] = None

    @property
    def internal_constrs(self) -> Optional["InternalConstrs"]:
        """Get internalConstrs (Pythonic accessor)."""
        return self._internalConstrs

    @internal_constrs.setter
    def internal_constrs(self, value: Optional["InternalConstrs"]) -> None:
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
        # Describes the limitations applicable on the physical opposed to the internal
        # domain).
        self._physConstrs: Optional["PhysConstrs"] = None

    @property
    def phys_constrs(self) -> Optional["PhysConstrs"]:
        """Get physConstrs (Pythonic accessor)."""
        return self._physConstrs

    @phys_constrs.setter
    def phys_constrs(self, value: Optional["PhysConstrs"]) -> None:
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

    def getConstrLevel(self) -> "Integer":
        """
        AUTOSAR-compliant getter for constrLevel.
        
        Returns:
            The constrLevel value
        
        Note:
            Delegates to constr_level property (CODING_RULE_V2_00017)
        """
        return self.constr_level  # Delegates to property

    def setConstrLevel(self, value: "Integer") -> "DataConstrRule":
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

    def getInternalConstrs(self) -> "InternalConstrs":
        """
        AUTOSAR-compliant getter for internalConstrs.
        
        Returns:
            The internalConstrs value
        
        Note:
            Delegates to internal_constrs property (CODING_RULE_V2_00017)
        """
        return self.internal_constrs  # Delegates to property

    def setInternalConstrs(self, value: "InternalConstrs") -> "DataConstrRule":
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

    def getPhysConstrs(self) -> "PhysConstrs":
        """
        AUTOSAR-compliant getter for physConstrs.
        
        Returns:
            The physConstrs value
        
        Note:
            Delegates to phys_constrs property (CODING_RULE_V2_00017)
        """
        return self.phys_constrs  # Delegates to property

    def setPhysConstrs(self, value: "PhysConstrs") -> "DataConstrRule":
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

    def with_constr_level(self, value: Optional["Integer"]) -> "DataConstrRule":
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

    def with_internal_constrs(self, value: Optional["InternalConstrs"]) -> "DataConstrRule":
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

    def with_phys_constrs(self, value: Optional["PhysConstrs"]) -> "DataConstrRule":
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