from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SwAxisGrouped(SwCalprmAxisTypeProps):
    """
    An SwAxisGrouped is an axis which is shared between multiple calibration
    parameters.

    Package: M2::MSR::DataDictionary::Axis::SwAxisGrouped

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 357, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the datatype of the calibration parameter providing shared axis.
        self._sharedAxisType: Optional["ApplicationPrimitive"] = None

    @property
    def shared_axis_type(self) -> Optional["ApplicationPrimitive"]:
        """Get sharedAxisType (Pythonic accessor)."""
        return self._sharedAxisType

    @shared_axis_type.setter
    def shared_axis_type(self, value: Optional["ApplicationPrimitive"]) -> None:
        """
        Set sharedAxisType with validation.

        Args:
            value: The sharedAxisType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sharedAxisType = None
            return

        if not isinstance(value, ApplicationPrimitive):
            raise TypeError(
                f"sharedAxisType must be ApplicationPrimitive or None, got {type(value).__name__}"
            )
        self._sharedAxisType = value
        # Describes which axis of the referenced calibration the values for the group
                # axis.
        # The the following convention: = value axis.
        # in this case, the interpolation result of parameter is used as a base point
                # index should only be specified if the parameter contains more than one axis.
        # It is for the axis index of parameters with one axis, to be set to 1, if data
                # has not been swAxisIndex.
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
        # This property specifies the calibration parameter which the input axis.
        # In AUTOSAR, the type of the parameter shall be compatible to specified by
                # sharedAxisType.
        # that the multiplicity of this aggregation cannot to 0.
        # 1 based on the non-mainstream schema defined at the aggregation.
        # multiplicity has to be factually considered a SwAxisGrouped that does not
                # aggregate the is still valid according to the XML on the use case documented
                # in.
        self._swCalprmRef: RefType = None

    @property
    def sw_calprm_ref(self) -> RefType:
        """Get swCalprmRef (Pythonic accessor)."""
        return self._swCalprmRef

    @sw_calprm_ref.setter
    def sw_calprm_ref(self, value: RefType) -> None:
        """
        Set swCalprmRef with validation.

        Args:
            value: The swCalprmRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._swCalprmRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSharedAxisType(self) -> "ApplicationPrimitive":
        """
        AUTOSAR-compliant getter for sharedAxisType.

        Returns:
            The sharedAxisType value

        Note:
            Delegates to shared_axis_type property (CODING_RULE_V2_00017)
        """
        return self.shared_axis_type  # Delegates to property

    def setSharedAxisType(self, value: "ApplicationPrimitive") -> "SwAxisGrouped":
        """
        AUTOSAR-compliant setter for sharedAxisType with method chaining.

        Args:
            value: The sharedAxisType to set

        Returns:
            self for method chaining

        Note:
            Delegates to shared_axis_type property setter (gets validation automatically)
        """
        self.shared_axis_type = value  # Delegates to property setter
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

    def setSwAxisIndex(self, value: "AxisIndexType") -> "SwAxisGrouped":
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

    def getSwCalprmRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for swCalprmRef.

        Returns:
            The swCalprmRef value

        Note:
            Delegates to sw_calprm_ref property (CODING_RULE_V2_00017)
        """
        return self.sw_calprm_ref  # Delegates to property

    def setSwCalprmRef(self, value: RefType) -> "SwAxisGrouped":
        """
        AUTOSAR-compliant setter for swCalprmRef with method chaining.

        Args:
            value: The swCalprmRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_calprm_ref property setter (gets validation automatically)
        """
        self.sw_calprm_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_shared_axis_type(self, value: Optional["ApplicationPrimitive"]) -> "SwAxisGrouped":
        """
        Set sharedAxisType and return self for chaining.

        Args:
            value: The sharedAxisType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_shared_axis_type("value")
        """
        self.shared_axis_type = value  # Use property setter (gets validation)
        return self

    def with_sw_axis_index(self, value: Optional["AxisIndexType"]) -> "SwAxisGrouped":
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

    def with_sw_calprm_ref(self, value: RefType) -> "SwAxisGrouped":
        """
        Set swCalprmRef and return self for chaining.

        Args:
            value: The swCalprmRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_calprm_ref("value")
        """
        self.sw_calprm_ref = value  # Use property setter (gets validation)
        return self
