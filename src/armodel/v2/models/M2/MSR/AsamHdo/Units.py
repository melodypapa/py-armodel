"""
AUTOSAR Package - Units

Package: M2::MSR::AsamHdo::Units
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)




class Unit(ARElement):
    """
    This is a physical measurement unit. All units that might be defined should
    stem from SI units. In order to convert one unit into another factor and
    offset are defined. For the calculation from SI-unit to the defined unit the
    factor (factorSiToUnit ) and the offset (offsetSiTo Unit ) are applied as
    follows: x [{unit}] := y * [{siUnit}] * factorSiToUnit [[unit]/{siUnit}] +
    offsetSiToUnit [{unit}] For the calculation from a unit to SI-unit the
    reciprocal of the factor (factorSiToUnit ) and the negation of the offset
    (offsetSiToUnit ) are applied. y {siUnit} := (x*{unit} - offsetSiToUnit
    [{unit}]) / (factorSiToUnit [[unit]/{siUnit}]
    
    Package: M2::MSR::AsamHdo::Units::Unit
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 333, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 64, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 400, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 479, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies how the unit shall be displayed in or in user interfaces of
                # tools.
        # The displayName the Unit.
        # Display in an ASAM MCD-2MC.
        self._displayName: Optional["SingleLanguageUnit"] = None

    @property
    def display_name(self) -> Optional["SingleLanguageUnit"]:
        """Get displayName (Pythonic accessor)."""
        return self._displayName

    @display_name.setter
    def display_name(self, value: Optional["SingleLanguageUnit"]) -> None:
        """
        Set displayName with validation.
        
        Args:
            value: The displayName to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._displayName = None
            return

        if not isinstance(value, SingleLanguageUnit):
            raise TypeError(
                f"displayName must be SingleLanguageUnit or None, got {type(value).__name__}"
            )
        self._displayName = value
        # This is the factor for the conversion from SI Units to units.
        # is used for conversion from units to SI Units.
        self._factorSiToUnit: Optional["Float"] = None

    @property
    def factor_si_to_unit(self) -> Optional["Float"]:
        """Get factorSiToUnit (Pythonic accessor)."""
        return self._factorSiToUnit

    @factor_si_to_unit.setter
    def factor_si_to_unit(self, value: Optional["Float"]) -> None:
        """
        Set factorSiToUnit with validation.
        
        Args:
            value: The factorSiToUnit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._factorSiToUnit = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"factorSiToUnit must be Float or float or None, got {type(value).__name__}"
            )
        self._factorSiToUnit = value
        # This is the offset for the conversion from and to siUnits.
        self._offsetSiToUnit: Optional["Float"] = None

    @property
    def offset_si_to_unit(self) -> Optional["Float"]:
        """Get offsetSiToUnit (Pythonic accessor)."""
        return self._offsetSiToUnit

    @offset_si_to_unit.setter
    def offset_si_to_unit(self, value: Optional["Float"]) -> None:
        """
        Set offsetSiToUnit with validation.
        
        Args:
            value: The offsetSiToUnit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offsetSiToUnit = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"offsetSiToUnit must be Float or float or None, got {type(value).__name__}"
            )
        self._offsetSiToUnit = value
        # This association represents the physical dimension to the unit belongs to.
        # Note that only values with units same physical dimensions might be converted.
        self._physical: Optional["PhysicalDimension"] = None

    @property
    def physical(self) -> Optional["PhysicalDimension"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @physical.setter
    def physical(self, value: Optional["PhysicalDimension"]) -> None:
        """
        Set physical with validation.
        
        Args:
            value: The physical to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physical = None
            return

        if not isinstance(value, PhysicalDimension):
            raise TypeError(
                f"physical must be PhysicalDimension or None, got {type(value).__name__}"
            )
        self._physical = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDisplayName(self) -> "SingleLanguageUnit":
        """
        AUTOSAR-compliant getter for displayName.
        
        Returns:
            The displayName value
        
        Note:
            Delegates to display_name property (CODING_RULE_V2_00017)
        """
        return self.display_name  # Delegates to property

    def setDisplayName(self, value: "SingleLanguageUnit") -> "Unit":
        """
        AUTOSAR-compliant setter for displayName with method chaining.
        
        Args:
            value: The displayName to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to display_name property setter (gets validation automatically)
        """
        self.display_name = value  # Delegates to property setter
        return self

    def getFactorSiToUnit(self) -> "Float":
        """
        AUTOSAR-compliant getter for factorSiToUnit.
        
        Returns:
            The factorSiToUnit value
        
        Note:
            Delegates to factor_si_to_unit property (CODING_RULE_V2_00017)
        """
        return self.factor_si_to_unit  # Delegates to property

    def setFactorSiToUnit(self, value: "Float") -> "Unit":
        """
        AUTOSAR-compliant setter for factorSiToUnit with method chaining.
        
        Args:
            value: The factorSiToUnit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to factor_si_to_unit property setter (gets validation automatically)
        """
        self.factor_si_to_unit = value  # Delegates to property setter
        return self

    def getOffsetSiToUnit(self) -> "Float":
        """
        AUTOSAR-compliant getter for offsetSiToUnit.
        
        Returns:
            The offsetSiToUnit value
        
        Note:
            Delegates to offset_si_to_unit property (CODING_RULE_V2_00017)
        """
        return self.offset_si_to_unit  # Delegates to property

    def setOffsetSiToUnit(self, value: "Float") -> "Unit":
        """
        AUTOSAR-compliant setter for offsetSiToUnit with method chaining.
        
        Args:
            value: The offsetSiToUnit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to offset_si_to_unit property setter (gets validation automatically)
        """
        self.offset_si_to_unit = value  # Delegates to property setter
        return self

    def getPhysical(self) -> "PhysicalDimension":
        """
        AUTOSAR-compliant getter for physical.
        
        Returns:
            The physical value
        
        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def setPhysical(self, value: "PhysicalDimension") -> "Unit":
        """
        AUTOSAR-compliant setter for physical with method chaining.
        
        Args:
            value: The physical to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to physical property setter (gets validation automatically)
        """
        self.physical = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_display_name(self, value: Optional["SingleLanguageUnit"]) -> "Unit":
        """
        Set displayName and return self for chaining.
        
        Args:
            value: The displayName to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_display_name("value")
        """
        self.display_name = value  # Use property setter (gets validation)
        return self

    def with_factor_si_to_unit(self, value: Optional["Float"]) -> "Unit":
        """
        Set factorSiToUnit and return self for chaining.
        
        Args:
            value: The factorSiToUnit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_factor_si_to_unit("value")
        """
        self.factor_si_to_unit = value  # Use property setter (gets validation)
        return self

    def with_offset_si_to_unit(self, value: Optional["Float"]) -> "Unit":
        """
        Set offsetSiToUnit and return self for chaining.
        
        Args:
            value: The offsetSiToUnit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_offset_si_to_unit("value")
        """
        self.offset_si_to_unit = value  # Use property setter (gets validation)
        return self

    def with_physical(self, value: Optional["PhysicalDimension"]) -> "Unit":
        """
        Set physical and return self for chaining.
        
        Args:
            value: The physical to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self



class UnitGroup(ARElement):
    """
    that the UnitGroup does not ensure the physical compliance of the units.
    This is maintained by the physical dimension.
    
    Package: M2::MSR::AsamHdo::Units::UnitGroup
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 314, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 402, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents one particular unit in the UnitGroup.
        self._unit: List["Unit"] = []

    @property
    def unit(self) -> List["Unit"]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getUnit(self) -> List["Unit"]:
        """
        AUTOSAR-compliant getter for unit.
        
        Returns:
            The unit value
        
        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class PhysicalDimension(ARElement):
    """
    that the equivalence of the exponents does not per se define the
    convertibility. For example Energy and Torque share the same exponents (Nm).
    Please note further the value of an exponent does not necessarily have to be
    an integer number. It is also possible that the value yields a rational
    number, e.g. to compute the square root of a given physical quantity. In
    this case the exponent value would be a rational number where the numerator
    value is 1 and the denominator value is 2.
    
    Package: M2::MSR::AsamHdo::Units::PhysicalDimension
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 398, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the exponent of the physical current".
        self._currentExp: Optional["Numerical"] = None

    @property
    def current_exp(self) -> Optional["Numerical"]:
        """Get currentExp (Pythonic accessor)."""
        return self._currentExp

    @current_exp.setter
    def current_exp(self, value: Optional["Numerical"]) -> None:
        """
        Set currentExp with validation.
        
        Args:
            value: The currentExp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._currentExp = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"currentExp must be Numerical or None, got {type(value).__name__}"
            )
        self._currentExp = value
        # The exponent of the physical dimension "length".
        self._lengthExp: Optional["Numerical"] = None

    @property
    def length_exp(self) -> Optional["Numerical"]:
        """Get lengthExp (Pythonic accessor)."""
        return self._lengthExp

    @length_exp.setter
    def length_exp(self, value: Optional["Numerical"]) -> None:
        """
        Set lengthExp with validation.
        
        Args:
            value: The lengthExp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lengthExp = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"lengthExp must be Numerical or None, got {type(value).__name__}"
            )
        self._lengthExp = value
        # The exponent of the physical dimension "luminous.
        self._luminous: Optional["Numerical"] = None

    @property
    def luminous(self) -> Optional["Numerical"]:
        """Get luminous (Pythonic accessor)."""
        return self._luminous

    @luminous.setter
    def luminous(self, value: Optional["Numerical"]) -> None:
        """
        Set luminous with validation.
        
        Args:
            value: The luminous to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._luminous = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"luminous must be Numerical or None, got {type(value).__name__}"
            )
        self._luminous = value
        # The exponent of the physical dimension "mass".
        self._massExp: Optional["Numerical"] = None

    @property
    def mass_exp(self) -> Optional["Numerical"]:
        """Get massExp (Pythonic accessor)."""
        return self._massExp

    @mass_exp.setter
    def mass_exp(self, value: Optional["Numerical"]) -> None:
        """
        Set massExp with validation.
        
        Args:
            value: The massExp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._massExp = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"massExp must be Numerical or None, got {type(value).__name__}"
            )
        self._massExp = value
        # The exponent of the physical dimension "quantity of.
        self._molarAmount: Optional["Numerical"] = None

    @property
    def molar_amount(self) -> Optional["Numerical"]:
        """Get molarAmount (Pythonic accessor)."""
        return self._molarAmount

    @molar_amount.setter
    def molar_amount(self, value: Optional["Numerical"]) -> None:
        """
        Set molarAmount with validation.
        
        Args:
            value: The molarAmount to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._molarAmount = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"molarAmount must be Numerical or None, got {type(value).__name__}"
            )
        self._molarAmount = value
        # The exponent of the physical dimension "temperature".
        self._temperatureExp: Optional["Numerical"] = None

    @property
    def temperature_exp(self) -> Optional["Numerical"]:
        """Get temperatureExp (Pythonic accessor)."""
        return self._temperatureExp

    @temperature_exp.setter
    def temperature_exp(self, value: Optional["Numerical"]) -> None:
        """
        Set temperatureExp with validation.
        
        Args:
            value: The temperatureExp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._temperatureExp = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"temperatureExp must be Numerical or None, got {type(value).__name__}"
            )
        self._temperatureExp = value
        # The exponent of the physical dimension "time".
        self._timeExp: Optional["Numerical"] = None

    @property
    def time_exp(self) -> Optional["Numerical"]:
        """Get timeExp (Pythonic accessor)."""
        return self._timeExp

    @time_exp.setter
    def time_exp(self, value: Optional["Numerical"]) -> None:
        """
        Set timeExp with validation.
        
        Args:
            value: The timeExp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeExp = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"timeExp must be Numerical or None, got {type(value).__name__}"
            )
        self._timeExp = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCurrentExp(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for currentExp.
        
        Returns:
            The currentExp value
        
        Note:
            Delegates to current_exp property (CODING_RULE_V2_00017)
        """
        return self.current_exp  # Delegates to property

    def setCurrentExp(self, value: "Numerical") -> "PhysicalDimension":
        """
        AUTOSAR-compliant setter for currentExp with method chaining.
        
        Args:
            value: The currentExp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to current_exp property setter (gets validation automatically)
        """
        self.current_exp = value  # Delegates to property setter
        return self

    def getLengthExp(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for lengthExp.
        
        Returns:
            The lengthExp value
        
        Note:
            Delegates to length_exp property (CODING_RULE_V2_00017)
        """
        return self.length_exp  # Delegates to property

    def setLengthExp(self, value: "Numerical") -> "PhysicalDimension":
        """
        AUTOSAR-compliant setter for lengthExp with method chaining.
        
        Args:
            value: The lengthExp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to length_exp property setter (gets validation automatically)
        """
        self.length_exp = value  # Delegates to property setter
        return self

    def getLuminous(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for luminous.
        
        Returns:
            The luminous value
        
        Note:
            Delegates to luminous property (CODING_RULE_V2_00017)
        """
        return self.luminous  # Delegates to property

    def setLuminous(self, value: "Numerical") -> "PhysicalDimension":
        """
        AUTOSAR-compliant setter for luminous with method chaining.
        
        Args:
            value: The luminous to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to luminous property setter (gets validation automatically)
        """
        self.luminous = value  # Delegates to property setter
        return self

    def getMassExp(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for massExp.
        
        Returns:
            The massExp value
        
        Note:
            Delegates to mass_exp property (CODING_RULE_V2_00017)
        """
        return self.mass_exp  # Delegates to property

    def setMassExp(self, value: "Numerical") -> "PhysicalDimension":
        """
        AUTOSAR-compliant setter for massExp with method chaining.
        
        Args:
            value: The massExp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mass_exp property setter (gets validation automatically)
        """
        self.mass_exp = value  # Delegates to property setter
        return self

    def getMolarAmount(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for molarAmount.
        
        Returns:
            The molarAmount value
        
        Note:
            Delegates to molar_amount property (CODING_RULE_V2_00017)
        """
        return self.molar_amount  # Delegates to property

    def setMolarAmount(self, value: "Numerical") -> "PhysicalDimension":
        """
        AUTOSAR-compliant setter for molarAmount with method chaining.
        
        Args:
            value: The molarAmount to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to molar_amount property setter (gets validation automatically)
        """
        self.molar_amount = value  # Delegates to property setter
        return self

    def getTemperatureExp(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for temperatureExp.
        
        Returns:
            The temperatureExp value
        
        Note:
            Delegates to temperature_exp property (CODING_RULE_V2_00017)
        """
        return self.temperature_exp  # Delegates to property

    def setTemperatureExp(self, value: "Numerical") -> "PhysicalDimension":
        """
        AUTOSAR-compliant setter for temperatureExp with method chaining.
        
        Args:
            value: The temperatureExp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to temperature_exp property setter (gets validation automatically)
        """
        self.temperature_exp = value  # Delegates to property setter
        return self

    def getTimeExp(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for timeExp.
        
        Returns:
            The timeExp value
        
        Note:
            Delegates to time_exp property (CODING_RULE_V2_00017)
        """
        return self.time_exp  # Delegates to property

    def setTimeExp(self, value: "Numerical") -> "PhysicalDimension":
        """
        AUTOSAR-compliant setter for timeExp with method chaining.
        
        Args:
            value: The timeExp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_exp property setter (gets validation automatically)
        """
        self.time_exp = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_current_exp(self, value: Optional["Numerical"]) -> "PhysicalDimension":
        """
        Set currentExp and return self for chaining.
        
        Args:
            value: The currentExp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_current_exp("value")
        """
        self.current_exp = value  # Use property setter (gets validation)
        return self

    def with_length_exp(self, value: Optional["Numerical"]) -> "PhysicalDimension":
        """
        Set lengthExp and return self for chaining.
        
        Args:
            value: The lengthExp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_length_exp("value")
        """
        self.length_exp = value  # Use property setter (gets validation)
        return self

    def with_luminous(self, value: Optional["Numerical"]) -> "PhysicalDimension":
        """
        Set luminous and return self for chaining.
        
        Args:
            value: The luminous to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_luminous("value")
        """
        self.luminous = value  # Use property setter (gets validation)
        return self

    def with_mass_exp(self, value: Optional["Numerical"]) -> "PhysicalDimension":
        """
        Set massExp and return self for chaining.
        
        Args:
            value: The massExp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mass_exp("value")
        """
        self.mass_exp = value  # Use property setter (gets validation)
        return self

    def with_molar_amount(self, value: Optional["Numerical"]) -> "PhysicalDimension":
        """
        Set molarAmount and return self for chaining.
        
        Args:
            value: The molarAmount to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_molar_amount("value")
        """
        self.molar_amount = value  # Use property setter (gets validation)
        return self

    def with_temperature_exp(self, value: Optional["Numerical"]) -> "PhysicalDimension":
        """
        Set temperatureExp and return self for chaining.
        
        Args:
            value: The temperatureExp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_temperature_exp("value")
        """
        self.temperature_exp = value  # Use property setter (gets validation)
        return self

    def with_time_exp(self, value: Optional["Numerical"]) -> "PhysicalDimension":
        """
        Set timeExp and return self for chaining.
        
        Args:
            value: The timeExp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_exp("value")
        """
        self.time_exp = value  # Use property setter (gets validation)
        return self



class PhysicalDimensionMapping(ARObject):
    """
    This class represents a specific mapping between two PhysicalDimensions.
    
    Package: M2::MSR::AsamHdo::Units::PhysicalDimensionMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 399, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the first PhysicalDimension of the PhysicalDimensionMapping.
        self._firstPhysical: Optional["PhysicalDimension"] = None

    @property
    def first_physical(self) -> Optional["PhysicalDimension"]:
        """Get firstPhysical (Pythonic accessor)."""
        return self._firstPhysical

    @first_physical.setter
    def first_physical(self, value: Optional["PhysicalDimension"]) -> None:
        """
        Set firstPhysical with validation.
        
        Args:
            value: The firstPhysical to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstPhysical = None
            return

        if not isinstance(value, PhysicalDimension):
            raise TypeError(
                f"firstPhysical must be PhysicalDimension or None, got {type(value).__name__}"
            )
        self._firstPhysical = value
        # This represents the first PhysicalDimension of the PhysicalDimensionMapping.
        self._secondPhysical: Optional["PhysicalDimension"] = None

    @property
    def second_physical(self) -> Optional["PhysicalDimension"]:
        """Get secondPhysical (Pythonic accessor)."""
        return self._secondPhysical

    @second_physical.setter
    def second_physical(self, value: Optional["PhysicalDimension"]) -> None:
        """
        Set secondPhysical with validation.
        
        Args:
            value: The secondPhysical to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondPhysical = None
            return

        if not isinstance(value, PhysicalDimension):
            raise TypeError(
                f"secondPhysical must be PhysicalDimension or None, got {type(value).__name__}"
            )
        self._secondPhysical = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstPhysical(self) -> "PhysicalDimension":
        """
        AUTOSAR-compliant getter for firstPhysical.
        
        Returns:
            The firstPhysical value
        
        Note:
            Delegates to first_physical property (CODING_RULE_V2_00017)
        """
        return self.first_physical  # Delegates to property

    def setFirstPhysical(self, value: "PhysicalDimension") -> "PhysicalDimensionMapping":
        """
        AUTOSAR-compliant setter for firstPhysical with method chaining.
        
        Args:
            value: The firstPhysical to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to first_physical property setter (gets validation automatically)
        """
        self.first_physical = value  # Delegates to property setter
        return self

    def getSecondPhysical(self) -> "PhysicalDimension":
        """
        AUTOSAR-compliant getter for secondPhysical.
        
        Returns:
            The secondPhysical value
        
        Note:
            Delegates to second_physical property (CODING_RULE_V2_00017)
        """
        return self.second_physical  # Delegates to property

    def setSecondPhysical(self, value: "PhysicalDimension") -> "PhysicalDimensionMapping":
        """
        AUTOSAR-compliant setter for secondPhysical with method chaining.
        
        Args:
            value: The secondPhysical to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to second_physical property setter (gets validation automatically)
        """
        self.second_physical = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_physical(self, value: Optional["PhysicalDimension"]) -> "PhysicalDimensionMapping":
        """
        Set firstPhysical and return self for chaining.
        
        Args:
            value: The firstPhysical to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_first_physical("value")
        """
        self.first_physical = value  # Use property setter (gets validation)
        return self

    def with_second_physical(self, value: Optional["PhysicalDimension"]) -> "PhysicalDimensionMapping":
        """
        Set secondPhysical and return self for chaining.
        
        Args:
            value: The secondPhysical to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_second_physical("value")
        """
        self.second_physical = value  # Use property setter (gets validation)
        return self



class PhysicalDimensionMappingSet(ARElement):
    """
    This class represents a container for a list of mappings between
    PhysicalDimensions.
    
    Package: M2::MSR::AsamHdo::Units::PhysicalDimensionMappingSet
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 399, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents a concrete collections of
        # PhysicalDimensionMappings in the context of one.
        self._physical: List["PhysicalDimension"] = []

    @property
    def physical(self) -> List["PhysicalDimension"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPhysical(self) -> List["PhysicalDimension"]:
        """
        AUTOSAR-compliant getter for physical.
        
        Returns:
            The physical value
        
        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====