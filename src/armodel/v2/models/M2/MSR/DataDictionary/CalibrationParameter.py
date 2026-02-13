"""
AUTOSAR Package - CalibrationParameter

Package: M2::MSR::DataDictionary::CalibrationParameter
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class SwCalprmAxisSet(ARObject):
    """
    This element specifies the input parameter axes (abscissas) of parameters
    (and variables, if these are used adaptively).

    Package: M2::MSR::DataDictionary::CalibrationParameter::SwCalprmAxisSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 351, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # One axis belonging to this SwCalprmAxisSet.
        self._swCalprmAxis: List[SwCalprmAxis] = []

    @property
    def sw_calprm_axis(self) -> List[SwCalprmAxis]:
        """Get swCalprmAxis (Pythonic accessor)."""
        return self._swCalprmAxis

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwCalprmAxis(self) -> List[SwCalprmAxis]:
        """
        AUTOSAR-compliant getter for swCalprmAxis.

        Returns:
            The swCalprmAxis value

        Note:
            Delegates to sw_calprm_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_calprm_axis  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SwCalprmAxis(ARObject):
    """
    This element specifies an individual input parameter axis (abscissa).

    Package: M2::MSR::DataDictionary::CalibrationParameter::SwCalprmAxis

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 352, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This property specifies the category of a particular axis.
        # xml.
        # sequenceOffset=30.
        self._category: Optional[CalprmAxisCategory] = None

    @property
    def category(self) -> Optional[CalprmAxisCategory]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional[CalprmAxisCategory]) -> None:
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
        # measurement and.
        self._displayFormat: Optional["DisplayFormatString"] = None

    @property
    def display_format(self) -> Optional["DisplayFormatString"]:
        """Get displayFormat (Pythonic accessor)."""
        return self._displayFormat

    @display_format.setter
    def display_format(self, value: Optional["DisplayFormatString"]) -> None:
        """
        Set displayFormat with validation.

        Args:
            value: The displayFormat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._displayFormat = None
            return

        if not isinstance(value, DisplayFormatString):
            raise TypeError(
                f"displayFormat must be DisplayFormatString or None, got {type(value).__name__}"
            )
        self._displayFormat = value
                # usually "1".
        # In a map this is "2".
        self._swAxisIndex: Optional[AxisIndexType] = None

    @property
    def sw_axis_index(self) -> Optional[AxisIndexType]:
        """Get swAxisIndex (Pythonic accessor)."""
        return self._swAxisIndex

    @sw_axis_index.setter
    def sw_axis_index(self, value: Optional[AxisIndexType]) -> None:
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
        # Tags: xml.
        # sequenceOffset=90.
        self._swCalibration: Optional["SwCalibrationAccess"] = None

    @property
    def sw_calibration(self) -> Optional["SwCalibrationAccess"]:
        """Get swCalibration (Pythonic accessor)."""
        return self._swCalibration

    @sw_calibration.setter
    def sw_calibration(self, value: Optional["SwCalibrationAccess"]) -> None:
        """
        Set swCalibration with validation.

        Args:
            value: The swCalibration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swCalibration = None
            return

        if not isinstance(value, SwCalibrationAccess):
            raise TypeError(
                f"swCalibration must be SwCalibrationAccess or None, got {type(value).__name__}"
            )
        self._swCalibration = value
        # Tags:.
        self._swCalprmAxis: Optional["SwCalprmAxisType"] = None

    @property
    def sw_calprm_axis(self) -> Optional["SwCalprmAxisType"]:
        """Get swCalprmAxis (Pythonic accessor)."""
        return self._swCalprmAxis

    @sw_calprm_axis.setter
    def sw_calprm_axis(self, value: Optional["SwCalprmAxisType"]) -> None:
        """
        Set swCalprmAxis with validation.

        Args:
            value: The swCalprmAxis to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swCalprmAxis = None
            return

        if not isinstance(value, SwCalprmAxisType):
            raise TypeError(
                f"swCalprmAxis must be SwCalprmAxisType or None, got {type(value).__name__}"
            )
        self._swCalprmAxis = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> CalprmAxisCategory:
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: CalprmAxisCategory) -> SwCalprmAxis:
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

    def getDisplayFormat(self) -> "DisplayFormatString":
        """
        AUTOSAR-compliant getter for displayFormat.

        Returns:
            The displayFormat value

        Note:
            Delegates to display_format property (CODING_RULE_V2_00017)
        """
        return self.display_format  # Delegates to property

    def setDisplayFormat(self, value: "DisplayFormatString") -> SwCalprmAxis:
        """
        AUTOSAR-compliant setter for displayFormat with method chaining.

        Args:
            value: The displayFormat to set

        Returns:
            self for method chaining

        Note:
            Delegates to display_format property setter (gets validation automatically)
        """
        self.display_format = value  # Delegates to property setter
        return self

    def getSwAxisIndex(self) -> AxisIndexType:
        """
        AUTOSAR-compliant getter for swAxisIndex.

        Returns:
            The swAxisIndex value

        Note:
            Delegates to sw_axis_index property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_index  # Delegates to property

    def setSwAxisIndex(self, value: AxisIndexType) -> SwCalprmAxis:
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

    def getSwCalibration(self) -> "SwCalibrationAccess":
        """
        AUTOSAR-compliant getter for swCalibration.

        Returns:
            The swCalibration value

        Note:
            Delegates to sw_calibration property (CODING_RULE_V2_00017)
        """
        return self.sw_calibration  # Delegates to property

    def setSwCalibration(self, value: "SwCalibrationAccess") -> SwCalprmAxis:
        """
        AUTOSAR-compliant setter for swCalibration with method chaining.

        Args:
            value: The swCalibration to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_calibration property setter (gets validation automatically)
        """
        self.sw_calibration = value  # Delegates to property setter
        return self

    def getSwCalprmAxis(self) -> "SwCalprmAxisType":
        """
        AUTOSAR-compliant getter for swCalprmAxis.

        Returns:
            The swCalprmAxis value

        Note:
            Delegates to sw_calprm_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_calprm_axis  # Delegates to property

    def setSwCalprmAxis(self, value: "SwCalprmAxisType") -> SwCalprmAxis:
        """
        AUTOSAR-compliant setter for swCalprmAxis with method chaining.

        Args:
            value: The swCalprmAxis to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_calprm_axis property setter (gets validation automatically)
        """
        self.sw_calprm_axis = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: Optional[CalprmAxisCategory]) -> SwCalprmAxis:
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

    def with_display_format(self, value: Optional["DisplayFormatString"]) -> SwCalprmAxis:
        """
        Set displayFormat and return self for chaining.

        Args:
            value: The displayFormat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_display_format("value")
        """
        self.display_format = value  # Use property setter (gets validation)
        return self

    def with_sw_axis_index(self, value: Optional[AxisIndexType]) -> SwCalprmAxis:
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

    def with_sw_calibration(self, value: Optional["SwCalibrationAccess"]) -> SwCalprmAxis:
        """
        Set swCalibration and return self for chaining.

        Args:
            value: The swCalibration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_calibration("value")
        """
        self.sw_calibration = value  # Use property setter (gets validation)
        return self

    def with_sw_calprm_axis(self, value: Optional["SwCalprmAxisType"]) -> SwCalprmAxis:
        """
        Set swCalprmAxis and return self for chaining.

        Args:
            value: The swCalprmAxis to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_calprm_axis("value")
        """
        self.sw_calprm_axis = value  # Use property setter (gets validation)
        return self



class SwCalprmAxisTypeProps(ARObject, ABC):
    """
    Base class for the type of the calibration axis. This provides the
    particular model of the specialization. If the specialization would be the
    directly from SwCalPrmAxis, the sequence of common properties and the
    specializes ones would be different.

    Package: M2::MSR::DataDictionary::CalibrationParameter::SwCalprmAxisTypeProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 353, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is SwCalprmAxisTypeProps:
            raise TypeError("SwCalprmAxisTypeProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the maximum permissible gradient adjustable object
                # (curve, map or cuboid) with a specific axis.
        # MaxGrad = maximum( - Value i-1,k)/(Axis Point i - Axis Point.
        self._maxGradient: Optional[Float] = None

    @property
    def max_gradient(self) -> Optional[Float]:
        """Get maxGradient (Pythonic accessor)."""
        return self._maxGradient

    @max_gradient.setter
    def max_gradient(self, value: Optional[Float]) -> None:
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

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"maxGradient must be Float or float or None, got {type(value).__name__}"
            )
        self._maxGradient = value
        # cuboid) with respect to a This information can be used by MCD verify whether
        # the monotony constraint is to prevent from changes violating the.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxGradient(self) -> Float:
        """
        AUTOSAR-compliant getter for maxGradient.

        Returns:
            The maxGradient value

        Note:
            Delegates to max_gradient property (CODING_RULE_V2_00017)
        """
        return self.max_gradient  # Delegates to property

    def setMaxGradient(self, value: Float) -> SwCalprmAxisTypeProps:
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

    def setMonotony(self, value: "MonotonyEnum") -> SwCalprmAxisTypeProps:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_gradient(self, value: Optional[Float]) -> SwCalprmAxisTypeProps:
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

    def with_monotony(self, value: Optional["MonotonyEnum"]) -> SwCalprmAxisTypeProps:
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


class CalprmAxisCategoryEnum(AREnum):
    """
    CalprmAxisCategoryEnum enumeration

This enum specifies the possible values of the category property within SwCalprmAxis. Aggregated by RuleBasedAxisCont.category, SwAxisCont.category, SwCalprmAxis.category

Package: M2::MSR::DataDictionary::CalibrationParameter
    """
    # Component Template
    Software = "None"

    # CP R23-11
    AUTOSAR = "None"

    # COM_AXIS is equal to an STD_AXIS, the difference is, that a COM_AXIS is an shared axis, that means this axis can be used multiple times by different CURVEs, MAPs, CUBOIDs, CUBE_4s, and
    comAxis = "0"

    # FIX_AXIS means that the input axis is not stored. The axis is calculated using parameters and so on it is also not possible to modify the axis points.
    fixAXIS = "4"

    # RES_AXIS is also an shared axis like COM_AXIS, the difference is that this kind of axis can be used for rescaling.
    resAxis = "6"

    # STD_AXIS means that input and output axis definition are stored within this CURVE, MAP, CUBOID, There is no shared or calculated axis.
    stdAxis = "8"
