from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

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