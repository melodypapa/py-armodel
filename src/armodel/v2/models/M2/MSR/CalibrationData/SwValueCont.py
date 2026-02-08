from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SwValueCont(ARObject):
    """
    This metaclass represents the content of one particular SwInstance.

    Package: M2::MSR::CalibrationData::CalibrationValue

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 449, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the size of each dimension for CURVE, MAP, CUBOID,
                # CUBE_4, RES_AXIS, VAL_BLK.
        # dimension one value has to be defined, e.
        # g.
        # one of COM_AXIS and two or more in case of MAP.
        self._swArraysize: RefType = None

    @property
    def sw_arraysize(self) -> RefType:
        """Get swArraysize (Pythonic accessor)."""
        return self._swArraysize

    @sw_arraysize.setter
    def sw_arraysize(self, value: RefType) -> None:
        """
        Set swArraysize with validation.

        Args:
            value: The swArraysize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swArraysize = None
            return

        self._swArraysize = value
        # swValuesPhys represents the values in the physical.
        self._swValuesPhys: Optional["SwValues"] = None

    @property
    def sw_values_phys(self) -> Optional["SwValues"]:
        """Get swValuesPhys (Pythonic accessor)."""
        return self._swValuesPhys

    @sw_values_phys.setter
    def sw_values_phys(self, value: Optional["SwValues"]) -> None:
        """
        Set swValuesPhys with validation.

        Args:
            value: The swValuesPhys to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swValuesPhys = None
            return

        if not isinstance(value, SwValues):
            raise TypeError(
                f"swValuesPhys must be SwValues or None, got {type(value).__name__}"
            )
        self._swValuesPhys = value
        # This represents the physical unit of the provided values.
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
        # This specifies how the physical units of the current value set shall be
        # displayed in documents or in user interfaces.
        self._unitDisplay: Optional["SingleLanguageUnit"] = None

    @property
    def unit_display(self) -> Optional["SingleLanguageUnit"]:
        """Get unitDisplay (Pythonic accessor)."""
        return self._unitDisplay

    @unit_display.setter
    def unit_display(self, value: Optional["SingleLanguageUnit"]) -> None:
        """
        Set unitDisplay with validation.

        Args:
            value: The unitDisplay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unitDisplay = None
            return

        if not isinstance(value, SingleLanguageUnit):
            raise TypeError(
                f"unitDisplay must be SingleLanguageUnit or None, got {type(value).__name__}"
            )
        self._unitDisplay = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwArraysize(self) -> RefType:
        """
        AUTOSAR-compliant getter for swArraysize.

        Returns:
            The swArraysize value

        Note:
            Delegates to sw_arraysize property (CODING_RULE_V2_00017)
        """
        return self.sw_arraysize  # Delegates to property

    def setSwArraysize(self, value: RefType) -> "SwValueCont":
        """
        AUTOSAR-compliant setter for swArraysize with method chaining.

        Args:
            value: The swArraysize to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_arraysize property setter (gets validation automatically)
        """
        self.sw_arraysize = value  # Delegates to property setter
        return self

    def getSwValuesPhys(self) -> "SwValues":
        """
        AUTOSAR-compliant getter for swValuesPhys.

        Returns:
            The swValuesPhys value

        Note:
            Delegates to sw_values_phys property (CODING_RULE_V2_00017)
        """
        return self.sw_values_phys  # Delegates to property

    def setSwValuesPhys(self, value: "SwValues") -> "SwValueCont":
        """
        AUTOSAR-compliant setter for swValuesPhys with method chaining.

        Args:
            value: The swValuesPhys to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_values_phys property setter (gets validation automatically)
        """
        self.sw_values_phys = value  # Delegates to property setter
        return self

    def getUnit(self) -> "Unit":
        """
        AUTOSAR-compliant getter for unit.

        Returns:
            The unit value

        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: "Unit") -> "SwValueCont":
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

    def getUnitDisplay(self) -> "SingleLanguageUnit":
        """
        AUTOSAR-compliant getter for unitDisplay.

        Returns:
            The unitDisplay value

        Note:
            Delegates to unit_display property (CODING_RULE_V2_00017)
        """
        return self.unit_display  # Delegates to property

    def setUnitDisplay(self, value: "SingleLanguageUnit") -> "SwValueCont":
        """
        AUTOSAR-compliant setter for unitDisplay with method chaining.

        Args:
            value: The unitDisplay to set

        Returns:
            self for method chaining

        Note:
            Delegates to unit_display property setter (gets validation automatically)
        """
        self.unit_display = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_arraysize(self, value: Optional[RefType]) -> "SwValueCont":
        """
        Set swArraysize and return self for chaining.

        Args:
            value: The swArraysize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_arraysize("value")
        """
        self.sw_arraysize = value  # Use property setter (gets validation)
        return self

    def with_sw_values_phys(self, value: Optional["SwValues"]) -> "SwValueCont":
        """
        Set swValuesPhys and return self for chaining.

        Args:
            value: The swValuesPhys to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_values_phys("value")
        """
        self.sw_values_phys = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional["Unit"]) -> "SwValueCont":
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

    def with_unit_display(self, value: Optional["SingleLanguageUnit"]) -> "SwValueCont":
        """
        Set unitDisplay and return self for chaining.

        Args:
            value: The unitDisplay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unit_display("value")
        """
        self.unit_display = value  # Use property setter (gets validation)
        return self
