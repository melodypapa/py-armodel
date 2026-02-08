from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RuleBasedAxisCont(ARObject):
    """
    This represents the values for the axis of a compound primitive (curve,
    map). For standard and fix axes, SwAxisCont contains the values of the axis
    directly. The axis values of SwAxisCont with the category COM_AXIS, RES_AXIS
    are for display only. For editing and processing, only the values in the
    related GroupAxis are binding.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 464, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This category specifies the particular axis types: STD_AXIS (swArraysize
        # necessary).
        self._category: Optional["CalprmAxisCategory"] = None

    @property
    def category(self) -> Optional["CalprmAxisCategory"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["CalprmAxisCategory"]) -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, CalprmAxisCategory):
            raise TypeError(
                f"category must be CalprmAxisCategory or None, got {type(value).__name__}"
            )
        self._category = value
        # This represents the rule based value specification for the axis of a compound
        # primitive (curve, map).
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
        # For multidimensional compound primitives (curve, map.
        # ) necessary to know the dimensions.
        # They are specified.
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
        # This property allows to explicitly assign the axis contents particular axis.
        # It is specified by numbers where 1 the x-axis.
        # It is also possible to derive the from the sequence of the parent.
        self._swAxisIndex: Optional["AxisIndexType"] = None

    @property
    def sw_axis_index(self) -> Optional["AxisIndexType"]:
        """Get swAxisIndex (Pythonic accessor)."""
        return self._swAxisIndex

    @sw_axis_index.setter
    def sw_axis_index(self, value: Optional["AxisIndexType"]) -> None:
        """
        Set swAxisIndex with validation.

        Args:
            value: The swAxisIndex to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swAxisIndex = None
            return

        if not isinstance(value, AxisIndexType):
            raise TypeError(
                f"swAxisIndex must be AxisIndexType or None, got {type(value).__name__}"
            )
        self._swAxisIndex = value
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

    def getCategory(self) -> "CalprmAxisCategory":
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "CalprmAxisCategory") -> "RuleBasedAxisCont":
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getRuleBased(self) -> "RuleBasedValue":
        """
        AUTOSAR-compliant getter for ruleBased.

        Returns:
            The ruleBased value

        Note:
            Delegates to rule_based property (CODING_RULE_V2_00017)
        """
        return self.rule_based  # Delegates to property

    def setRuleBased(self, value: "RuleBasedValue") -> "RuleBasedAxisCont":
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

    def setSwArraysize(self, value: RefType) -> "RuleBasedAxisCont":
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

    def getSwAxisIndex(self) -> "AxisIndexType":
        """
        AUTOSAR-compliant getter for swAxisIndex.

        Returns:
            The swAxisIndex value

        Note:
            Delegates to sw_axis_index property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_index  # Delegates to property

    def setSwAxisIndex(self, value: "AxisIndexType") -> "RuleBasedAxisCont":
        """
        AUTOSAR-compliant setter for swAxisIndex with method chaining.

        Args:
            value: The swAxisIndex to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_axis_index property setter (gets validation automatically)
        """
        self.sw_axis_index = value  # Delegates to property setter
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

    def setUnit(self, value: "Unit") -> "RuleBasedAxisCont":
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

    def with_category(self, value: Optional["CalprmAxisCategory"]) -> "RuleBasedAxisCont":
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_rule_based(self, value: Optional["RuleBasedValue"]) -> "RuleBasedAxisCont":
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

    def with_sw_arraysize(self, value: Optional[RefType]) -> "RuleBasedAxisCont":
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

    def with_sw_axis_index(self, value: Optional["AxisIndexType"]) -> "RuleBasedAxisCont":
        """
        Set swAxisIndex and return self for chaining.

        Args:
            value: The swAxisIndex to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_axis_index("value")
        """
        self.sw_axis_index = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional["Unit"]) -> "RuleBasedAxisCont":
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
