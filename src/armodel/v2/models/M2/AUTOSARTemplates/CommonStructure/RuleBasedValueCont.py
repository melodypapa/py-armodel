from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RuleBasedValueCont(ARObject):
    """
    This represents the values of a compound primitive (CURVE, MAP, CUBOID,
    CUBE_4, CUBE_5, VAL_ BLK) or an array.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::RuleBasedValueCont

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 330, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 464, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the rule based value specification for the array or compound
        # primitive (CURVE, MAP, CUBOID, VAL_BLK).
        self._ruleBased: Optional["RuleBasedValue"] = None

    @property
    def rule_based(self) -> Optional["RuleBasedValue"]:
        """Get ruleBased (Pythonic accessor)."""
        return self._ruleBased

    @rule_based.setter
    def rule_based(self, value: Optional["RuleBasedValue"]) -> None:
        """
        Set ruleBased with validation.

        Args:
            value: The ruleBased to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ruleBased = None
            return

        if not isinstance(value, RuleBasedValue):
            raise TypeError(
                f"ruleBased must be RuleBasedValue or None, got {type(value).__name__}"
            )
        self._ruleBased = value
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRuleBased(self) -> "RuleBasedValue":
        """
        AUTOSAR-compliant getter for ruleBased.

        Returns:
            The ruleBased value

        Note:
            Delegates to rule_based property (CODING_RULE_V2_00017)
        """
        return self.rule_based  # Delegates to property

    def setRuleBased(self, value: "RuleBasedValue") -> "RuleBasedValueCont":
        """
        AUTOSAR-compliant setter for ruleBased with method chaining.

        Args:
            value: The ruleBased to set

        Returns:
            self for method chaining

        Note:
            Delegates to rule_based property setter (gets validation automatically)
        """
        self.rule_based = value  # Delegates to property setter
        return self

    def getSwArraysize(self) -> RefType:
        """
        AUTOSAR-compliant getter for swArraysize.

        Returns:
            The swArraysize value

        Note:
            Delegates to sw_arraysize property (CODING_RULE_V2_00017)
        """
        return self.sw_arraysize  # Delegates to property

    def setSwArraysize(self, value: RefType) -> "RuleBasedValueCont":
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

    def getUnit(self) -> "Unit":
        """
        AUTOSAR-compliant getter for unit.

        Returns:
            The unit value

        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: "Unit") -> "RuleBasedValueCont":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rule_based(self, value: Optional["RuleBasedValue"]) -> "RuleBasedValueCont":
        """
        Set ruleBased and return self for chaining.

        Args:
            value: The ruleBased to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rule_based("value")
        """
        self.rule_based = value  # Use property setter (gets validation)
        return self

    def with_sw_arraysize(self, value: Optional[RefType]) -> "RuleBasedValueCont":
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

    def with_unit(self, value: Optional["Unit"]) -> "RuleBasedValueCont":
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
