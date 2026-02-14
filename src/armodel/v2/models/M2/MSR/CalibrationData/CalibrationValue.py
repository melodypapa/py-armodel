"""
AUTOSAR Package - CalibrationValue

Package: M2::MSR::CalibrationData::CalibrationValue
"""


from __future__ import annotations

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    NumericalOrText,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    RefType,
    VerbatimString,
)
from armodel.v2.models.M2.MSR.AsamHdo.Units import (
    Unit,
)
from armodel.v2.models.M2.MSR.DataDictionary.CalibrationParameter import (
    CalprmAxisCategoryEnum,
)
from armodel.v2.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultilanguageLongName,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.SingleLanguageData import (
    SingleLanguageUnitNames,
)


class SwValueCont(ARObject):
    """
    This metaclass represents the content of one particular SwInstance.

    Package: M2::MSR::CalibrationData::CalibrationValue::SwValueCont

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
        self._swArraysize: Optional[RefType] = None

    @property
    def sw_arraysize(self) -> Optional[RefType]:
        """Get swArraysize (Pythonic accessor)."""
        return self._swArraysize

    @sw_arraysize.setter
    def sw_arraysize(self, value: Optional[RefType]) -> None:
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
        self._swValuesPhys: Optional[SwValues] = None

    @property
    def sw_values_phys(self) -> Optional[SwValues]:
        """Get swValuesPhys (Pythonic accessor)."""
        return self._swValuesPhys

    @sw_values_phys.setter
    def sw_values_phys(self, value: Optional[SwValues]) -> None:
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
        self._unit: Optional[Unit] = None

    @property
    def unit(self) -> Optional[Unit]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional[Unit]) -> None:
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
        # displayed in documents or in user interfaces.
        self._unitDisplay: Optional[SingleLanguageUnitNames] = None

    @property
    def unit_display(self) -> Optional[SingleLanguageUnitNames]:
        """Get unitDisplay (Pythonic accessor)."""
        return self._unitDisplay

    @unit_display.setter
    def unit_display(self, value: Optional[SingleLanguageUnitNames]) -> None:
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

        if not isinstance(value, SingleLanguageUnitNames):
            raise TypeError(
                f"unitDisplay must be SingleLanguageUnitNames or None, got {type(value).__name__}"
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

    def setSwArraysize(self, value: RefType) -> SwValueCont:
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

    def getSwValuesPhys(self) -> SwValues:
        """
        AUTOSAR-compliant getter for swValuesPhys.

        Returns:
            The swValuesPhys value

        Note:
            Delegates to sw_values_phys property (CODING_RULE_V2_00017)
        """
        return self.sw_values_phys  # Delegates to property

    def setSwValuesPhys(self, value: SwValues) -> SwValueCont:
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

    def getUnit(self) -> Unit:
        """
        AUTOSAR-compliant getter for unit.

        Returns:
            The unit value

        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: Unit) -> SwValueCont:
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

    def getUnitDisplay(self) -> SingleLanguageUnitNames:
        """
        AUTOSAR-compliant getter for unitDisplay.

        Returns:
            The unitDisplay value

        Note:
            Delegates to unit_display property (CODING_RULE_V2_00017)
        """
        return self.unit_display  # Delegates to property

    def setUnitDisplay(self, value: SingleLanguageUnitNames) -> SwValueCont:
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

    def with_sw_arraysize(self, value: Optional[RefType]) -> SwValueCont:
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

    def with_sw_values_phys(self, value: Optional[SwValues]) -> SwValueCont:
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

    def with_unit(self, value: Optional[Unit]) -> SwValueCont:
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

    def with_unit_display(self, value: Optional[SingleLanguageUnitNames]) -> SwValueCont:
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



class SwAxisCont(ARObject):
    """
    This represents the values for the axis of a compound primitive (curve,
    map). For standard and fix axes, SwAxisCont contains the values of the axis
    directly. The axis values of SwAxisCont with the category COM_AXIS, RES_AXIS
    are for display only. For editing and processing, only the values in the
    related GroupAxis are binding.

    Package: M2::MSR::CalibrationData::CalibrationValue::SwAxisCont

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 457, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This category specifies the particular axis types: STD_AXIS (swArraysize
        # necessary).
        self._category: Optional[CalprmAxisCategoryEnum] = None

    @property
    def category(self) -> Optional[CalprmAxisCategoryEnum]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional[CalprmAxisCategoryEnum]) -> None:
                # the dimensions.
        # They are swArraySize.
        self._swArraysize: Optional[RefType] = None

    @property
    def sw_arraysize(self) -> Optional[RefType]:
        """Get swArraysize (Pythonic accessor)."""
        return self._swArraysize

    @sw_arraysize.setter
    def sw_arraysize(self, value: Optional[RefType]) -> None:
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
        # It is specified by numbers where 1 the x-axis.
        # It is also possible to derive the from the sequence of the parent.
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
        self._swValuesPhys: Optional[SwValues] = None

    @property
    def sw_values_phys(self) -> Optional[SwValues]:
        """Get swValuesPhys (Pythonic accessor)."""
        return self._swValuesPhys

    @sw_values_phys.setter
    def sw_values_phys(self, value: Optional[SwValues]) -> None:
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
        self._unit: Optional[Unit] = None

    @property
    def unit(self) -> Optional[Unit]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional[Unit]) -> None:
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
        # axis.
        self._unitDisplay: Optional[SingleLanguageUnitNames] = None

    @property
    def unit_display(self) -> Optional[SingleLanguageUnitNames]:
        """Get unitDisplay (Pythonic accessor)."""
        return self._unitDisplay

    @unit_display.setter
    def unit_display(self, value: Optional[SingleLanguageUnitNames]) -> None:
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

        if not isinstance(value, SingleLanguageUnitNames):
            raise TypeError(
                f"unitDisplay must be SingleLanguageUnitNames or None, got {type(value).__name__}"
            )
        self._unitDisplay = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> CalprmAxisCategoryEnum:
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: CalprmAxisCategoryEnum) -> SwAxisCont:
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

    def getSwArraysize(self) -> RefType:
        """
        AUTOSAR-compliant getter for swArraysize.

        Returns:
            The swArraysize value

        Note:
            Delegates to sw_arraysize property (CODING_RULE_V2_00017)
        """
        return self.sw_arraysize  # Delegates to property

    def setSwArraysize(self, value: RefType) -> SwAxisCont:
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

    def getSwAxisIndex(self) -> AxisIndexType:
        """
        AUTOSAR-compliant getter for swAxisIndex.

        Returns:
            The swAxisIndex value

        Note:
            Delegates to sw_axis_index property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_index  # Delegates to property

    def setSwAxisIndex(self, value: AxisIndexType) -> SwAxisCont:
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

    def getSwValuesPhys(self) -> SwValues:
        """
        AUTOSAR-compliant getter for swValuesPhys.

        Returns:
            The swValuesPhys value

        Note:
            Delegates to sw_values_phys property (CODING_RULE_V2_00017)
        """
        return self.sw_values_phys  # Delegates to property

    def setSwValuesPhys(self, value: SwValues) -> SwAxisCont:
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

    def getUnit(self) -> Unit:
        """
        AUTOSAR-compliant getter for unit.

        Returns:
            The unit value

        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: Unit) -> SwAxisCont:
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

    def getUnitDisplay(self) -> SingleLanguageUnitNames:
        """
        AUTOSAR-compliant getter for unitDisplay.

        Returns:
            The unitDisplay value

        Note:
            Delegates to unit_display property (CODING_RULE_V2_00017)
        """
        return self.unit_display  # Delegates to property

    def setUnitDisplay(self, value: SingleLanguageUnitNames) -> SwAxisCont:
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

    def with_category(self, value: Optional[CalprmAxisCategoryEnum]) -> SwAxisCont:
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

    def with_sw_arraysize(self, value: Optional[RefType]) -> SwAxisCont:
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

    def with_sw_axis_index(self, value: Optional[AxisIndexType]) -> SwAxisCont:
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

    def with_sw_values_phys(self, value: Optional[SwValues]) -> SwAxisCont:
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

    def with_unit(self, value: Optional[Unit]) -> SwAxisCont:
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

    def with_unit_display(self, value: Optional[SingleLanguageUnitNames]) -> SwAxisCont:
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



class SwValues(ARObject):
    """
    that numerical values and textual values should not be mixed.

    Package: M2::MSR::CalibrationData::CalibrationValue::SwValues

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 458, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a non variant Value.
        # It is provided for sake of ASAM CDF.
        self._v: Optional[Numerical] = None

    @property
    def v(self) -> Optional[Numerical]:
        """Get v (Pythonic accessor)."""
        return self._v

    @v.setter
    def v(self, value: Optional[Numerical]) -> None:
        """
        Set v with validation.

        Args:
            value: The v to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._v = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"v must be Numerical or None, got {type(value).__name__}"
            )
        self._v = value
        # It is non variant for sake of compatibility to 2.
        # 0.
        self._vf: Optional[Numerical] = None

    @property
    def vf(self) -> Optional[Numerical]:
        """Get vf (Pythonic accessor)."""
        return self._vf

    @vf.setter
    def vf(self, value: Optional[Numerical]) -> None:
        """
        Set vf with validation.

        Args:
            value: The vf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vf = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"vf must be Numerical or None, got {type(value).__name__}"
            )
        self._vf = value
        # using stylesheets).
        # For is important that the v values are always the same (flattened) order and
                # the tool is interpret it without respecting vg.
        self._vg: Optional[RefType] = None

    @property
    def vg(self) -> Optional[RefType]:
        """Get vg (Pythonic accessor)."""
        return self._vg

    @vg.setter
    def vg(self, value: Optional[RefType]) -> None:
        """
        Set vg with validation.

        Args:
            value: The vg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vg = None
            return

        self._vg = value
        self._vt: Optional[VerbatimString] = None

    @property
    def vt(self) -> Optional[VerbatimString]:
        """Get vt (Pythonic accessor)."""
        return self._vt

    @vt.setter
    def vt(self, value: Optional[VerbatimString]) -> None:
                # or text which existence is subject formal point of view, the aggregation
                # needs to multiplicity 1 because SwValues is modelled with Nevertheless, the
                # existence of optional and subject to constraints.
        self._vtf: Optional[NumericalOrText] = None

    @property
    def vtf(self) -> Optional[NumericalOrText]:
        """Get vtf (Pythonic accessor)."""
        return self._vtf

    @vtf.setter
    def vtf(self, value: Optional[NumericalOrText]) -> None:
        """
        Set vtf with validation.

        Args:
            value: The vtf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vtf = None
            return

        if not isinstance(value, NumericalOrText):
            raise TypeError(
                f"vtf must be NumericalOrText or None, got {type(value).__name__}"
            )
        self._vtf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getV(self) -> Numerical:
        """
        AUTOSAR-compliant getter for v.

        Returns:
            The v value

        Note:
            Delegates to v property (CODING_RULE_V2_00017)
        """
        return self.v  # Delegates to property

    def setV(self, value: Numerical) -> SwValues:
        """
        AUTOSAR-compliant setter for v with method chaining.

        Args:
            value: The v to set

        Returns:
            self for method chaining

        Note:
            Delegates to v property setter (gets validation automatically)
        """
        self.v = value  # Delegates to property setter
        return self

    def getVf(self) -> Numerical:
        """
        AUTOSAR-compliant getter for vf.

        Returns:
            The vf value

        Note:
            Delegates to vf property (CODING_RULE_V2_00017)
        """
        return self.vf  # Delegates to property

    def setVf(self, value: Numerical) -> SwValues:
        """
        AUTOSAR-compliant setter for vf with method chaining.

        Args:
            value: The vf to set

        Returns:
            self for method chaining

        Note:
            Delegates to vf property setter (gets validation automatically)
        """
        self.vf = value  # Delegates to property setter
        return self

    def getVg(self) -> RefType:
        """
        AUTOSAR-compliant getter for vg.

        Returns:
            The vg value

        Note:
            Delegates to vg property (CODING_RULE_V2_00017)
        """
        return self.vg  # Delegates to property

    def setVg(self, value: RefType) -> SwValues:
        """
        AUTOSAR-compliant setter for vg with method chaining.

        Args:
            value: The vg to set

        Returns:
            self for method chaining

        Note:
            Delegates to vg property setter (gets validation automatically)
        """
        self.vg = value  # Delegates to property setter
        return self

    def getVt(self) -> VerbatimString:
        """
        AUTOSAR-compliant getter for vt.

        Returns:
            The vt value

        Note:
            Delegates to vt property (CODING_RULE_V2_00017)
        """
        return self.vt  # Delegates to property

    def setVt(self, value: VerbatimString) -> SwValues:
        """
        AUTOSAR-compliant setter for vt with method chaining.

        Args:
            value: The vt to set

        Returns:
            self for method chaining

        Note:
            Delegates to vt property setter (gets validation automatically)
        """
        self.vt = value  # Delegates to property setter
        return self

    def getVtf(self) -> NumericalOrText:
        """
        AUTOSAR-compliant getter for vtf.

        Returns:
            The vtf value

        Note:
            Delegates to vtf property (CODING_RULE_V2_00017)
        """
        return self.vtf  # Delegates to property

    def setVtf(self, value: NumericalOrText) -> SwValues:
        """
        AUTOSAR-compliant setter for vtf with method chaining.

        Args:
            value: The vtf to set

        Returns:
            self for method chaining

        Note:
            Delegates to vtf property setter (gets validation automatically)
        """
        self.vtf = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_v(self, value: Optional[Numerical]) -> SwValues:
        """
        Set v and return self for chaining.

        Args:
            value: The v to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_v("value")
        """
        self.v = value  # Use property setter (gets validation)
        return self

    def with_vf(self, value: Optional[Numerical]) -> SwValues:
        """
        Set vf and return self for chaining.

        Args:
            value: The vf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vf("value")
        """
        self.vf = value  # Use property setter (gets validation)
        return self

    def with_vg(self, value: Optional[RefType]) -> SwValues:
        """
        Set vg and return self for chaining.

        Args:
            value: The vg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vg("value")
        """
        self.vg = value  # Use property setter (gets validation)
        return self

    def with_vt(self, value: Optional[VerbatimString]) -> SwValues:
        """
        Set vt and return self for chaining.

        Args:
            value: The vt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vt("value")
        """
        self.vt = value  # Use property setter (gets validation)
        return self

    def with_vtf(self, value: Optional[NumericalOrText]) -> SwValues:
        """
        Set vtf and return self for chaining.

        Args:
            value: The vtf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vtf("value")
        """
        self.vtf = value  # Use property setter (gets validation)
        return self



class ValueGroup(ARObject):
    """
    This element enables values to be grouped. It can be used to perform row and
    column-orientated groupings, so that these can be rendered properly e.g. as
    a table.

    Package: M2::MSR::CalibrationData::CalibrationValue::ValueGroup

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 458, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This label allows to give the valueGroup a particular It can be used if the
        # Values are rendered as a.
        self._label: Optional[MultilanguageLongName] = None

    @property
    def label(self) -> Optional[MultilanguageLongName]:
        """Get label (Pythonic accessor)."""
        return self._label

    @label.setter
    def label(self, value: Optional[MultilanguageLongName]) -> None:
        """
        Set label with validation.

        Args:
            value: The label to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._label = None
            return

        if not isinstance(value, MultilanguageLongName):
            raise TypeError(
                f"label must be MultilanguageLongName or None, got {type(value).__name__}"
            )
        self._label = value
        self._vgContents: Optional[SwValues] = None

    @property
    def vg_contents(self) -> Optional[SwValues]:
        """Get vgContents (Pythonic accessor)."""
        return self._vgContents

    @vg_contents.setter
    def vg_contents(self, value: Optional[SwValues]) -> None:
        """
        Set vgContents with validation.

        Args:
            value: The vgContents to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vgContents = None
            return

        if not isinstance(value, SwValues):
            raise TypeError(
                f"vgContents must be SwValues or None, got {type(value).__name__}"
            )
        self._vgContents = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLabel(self) -> MultilanguageLongName:
        """
        AUTOSAR-compliant getter for label.

        Returns:
            The label value

        Note:
            Delegates to label property (CODING_RULE_V2_00017)
        """
        return self.label  # Delegates to property

    def setLabel(self, value: MultilanguageLongName) -> ValueGroup:
        """
        AUTOSAR-compliant setter for label with method chaining.

        Args:
            value: The label to set

        Returns:
            self for method chaining

        Note:
            Delegates to label property setter (gets validation automatically)
        """
        self.label = value  # Delegates to property setter
        return self

    def getVgContents(self) -> SwValues:
        """
        AUTOSAR-compliant getter for vgContents.

        Returns:
            The vgContents value

        Note:
            Delegates to vg_contents property (CODING_RULE_V2_00017)
        """
        return self.vg_contents  # Delegates to property

    def setVgContents(self, value: SwValues) -> ValueGroup:
        """
        AUTOSAR-compliant setter for vgContents with method chaining.

        Args:
            value: The vgContents to set

        Returns:
            self for method chaining

        Note:
            Delegates to vg_contents property setter (gets validation automatically)
        """
        self.vg_contents = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_label(self, value: Optional[MultilanguageLongName]) -> ValueGroup:
        """
        Set label and return self for chaining.

        Args:
            value: The label to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_label("value")
        """
        self.label = value  # Use property setter (gets validation)
        return self

    def with_vg_contents(self, value: Optional[SwValues]) -> ValueGroup:
        """
        Set vgContents and return self for chaining.

        Args:
            value: The vgContents to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vg_contents("value")
        """
        self.vg_contents = value  # Use property setter (gets validation)
        return self
