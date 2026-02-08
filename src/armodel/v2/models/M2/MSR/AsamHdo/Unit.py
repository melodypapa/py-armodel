from typing import Optional


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

    Package: M2::MSR::AsamHdo::Units

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

        if not isinstance(value, Float):
            raise TypeError(
                f"factorSiToUnit must be Float or None, got {type(value).__name__}"
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

        if not isinstance(value, Float):
            raise TypeError(
                f"offsetSiToUnit must be Float or None, got {type(value).__name__}"
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
