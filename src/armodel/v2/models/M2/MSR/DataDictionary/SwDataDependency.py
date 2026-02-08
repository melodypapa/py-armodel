from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SwDataDependency(ARObject):
    """
    This element describes the interdependencies of data objects, e.g. variables
    and parameters. Use cases: • Calculate the value of a calibration parameter
    (by the MCD system) from the value(s) of other calibration parameters. •
    Virtual data - that means the data object is not directly in the ecu and
    this property describes how the "virtual variable" can be computed from the
    real ones (by the MCD system).

    Package: M2::MSR::DataDictionary::DataDefProperties::SwDataDependency

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 373, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element describes the formula with which the between the participating
        # objects are.
        self._swData: Optional["CompuGenericMath"] = None

    @property
    def sw_data(self) -> Optional["CompuGenericMath"]:
        """Get swData (Pythonic accessor)."""
        return self._swData

    @sw_data.setter
    def sw_data(self, value: Optional["CompuGenericMath"]) -> None:
        """
        Set swData with validation.

        Args:
            value: The swData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swData = None
            return

        if not isinstance(value, CompuGenericMath):
            raise TypeError(
                f"swData must be CompuGenericMath or None, got {type(value).__name__}"
            )
        self._swData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwData(self) -> "CompuGenericMath":
        """
        AUTOSAR-compliant getter for swData.

        Returns:
            The swData value

        Note:
            Delegates to sw_data property (CODING_RULE_V2_00017)
        """
        return self.sw_data  # Delegates to property

    def setSwData(self, value: "CompuGenericMath") -> "SwDataDependency":
        """
        AUTOSAR-compliant setter for swData with method chaining.

        Args:
            value: The swData to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_data property setter (gets validation automatically)
        """
        self.sw_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_data(self, value: Optional["CompuGenericMath"]) -> "SwDataDependency":
        """
        Set swData and return self for chaining.

        Args:
            value: The swData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_data("value")
        """
        self.sw_data = value  # Use property setter (gets validation)
        return self
