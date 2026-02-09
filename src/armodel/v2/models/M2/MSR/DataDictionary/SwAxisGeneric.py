from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SwAxisGeneric(ARObject):
    """
    This meta-class defines a generic axis. In a generic axis the axispoints
    points are calculated in the ECU. The ECU is equipped with a fixed
    calculation algorithm. Parameters for the algorithm can be stored in the
    data component of the ECU. Therefore these parameters are specified in the
    data declaration, not in the calibration data.

    Package: M2::MSR::DataDictionary::Axis

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 355, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Associated axis calculation strategy.
        self._swAxisType: Optional["SwAxisType"] = None

    @property
    def sw_axis_type(self) -> Optional["SwAxisType"]:
        """Get swAxisType (Pythonic accessor)."""
        return self._swAxisType

    @sw_axis_type.setter
    def sw_axis_type(self, value: Optional["SwAxisType"]) -> None:
        """
        Set swAxisType with validation.

        Args:
            value: The swAxisType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swAxisType = None
            return

        if not isinstance(value, SwAxisType):
            raise TypeError(
                f"swAxisType must be SwAxisType or None, got {type(value).__name__}"
            )
        self._swAxisType = value
        # Specific parameter of a generic axis.
        self._swGenericAxis: List["SwGenericAxisParam"] = []

    @property
    def sw_generic_axis(self) -> List["SwGenericAxisParam"]:
        """Get swGenericAxis (Pythonic accessor)."""
        return self._swGenericAxis

    def with_sw_generic_axis(self, value):
        """
        Set sw_generic_axis and return self for chaining.

        Args:
            value: The sw_generic_axis to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_generic_axis("value")
        """
        self.sw_generic_axis = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwAxisType(self) -> "SwAxisType":
        """
        AUTOSAR-compliant getter for swAxisType.

        Returns:
            The swAxisType value

        Note:
            Delegates to sw_axis_type property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_type  # Delegates to property

    def setSwAxisType(self, value: "SwAxisType") -> "SwAxisGeneric":
        """
        AUTOSAR-compliant setter for swAxisType with method chaining.

        Args:
            value: The swAxisType to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_axis_type property setter (gets validation automatically)
        """
        self.sw_axis_type = value  # Delegates to property setter
        return self

    def getSwGenericAxis(self) -> List["SwGenericAxisParam"]:
        """
        AUTOSAR-compliant getter for swGenericAxis.

        Returns:
            The swGenericAxis value

        Note:
            Delegates to sw_generic_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_generic_axis  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_axis_type(self, value: Optional["SwAxisType"]) -> "SwAxisGeneric":
        """
        Set swAxisType and return self for chaining.

        Args:
            value: The swAxisType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_axis_type("value")
        """
        self.sw_axis_type = value  # Use property setter (gets validation)
        return self
