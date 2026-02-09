from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class InterpolationRoutineMapping(ARObject):
    """
    This meta-class provides a mapping between one record layout and its
    matching interpolation routines. This allows to formally specify the
    semantics of the interpolation routines. The use case is such that the
    curves/Maps define an interpolation method. This mapping table specifies
    which interpolation routine implements methods for a particular record
    layout. Using this information, the implementer of a software-component can
    select the appropriate interpolation routine.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::InterpolationRoutine

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 430, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 46, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular interpolation routine which is to the record layout.
        self._interpolation: List["InterpolationRoutine"] = []

    @property
    def interpolation(self) -> List["InterpolationRoutine"]:
        """Get interpolation (Pythonic accessor)."""
        return self._interpolation
        # This refers to the record layout which is mapped to routines.
        self._swRecord: Optional["SwRecordLayout"] = None

    @property
    def sw_record(self) -> Optional["SwRecordLayout"]:
        """Get swRecord (Pythonic accessor)."""
        return self._swRecord

    @sw_record.setter
    def sw_record(self, value: Optional["SwRecordLayout"]) -> None:
        """
        Set swRecord with validation.

        Args:
            value: The swRecord to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swRecord = None
            return

        if not isinstance(value, SwRecordLayout):
            raise TypeError(
                f"swRecord must be SwRecordLayout or None, got {type(value).__name__}"
            )
        self._swRecord = value

    def with_interpolation(self, value):
        """
        Set interpolation and return self for chaining.

        Args:
            value: The interpolation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interpolation("value")
        """
        self.interpolation = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInterpolation(self) -> List["InterpolationRoutine"]:
        """
        AUTOSAR-compliant getter for interpolation.

        Returns:
            The interpolation value

        Note:
            Delegates to interpolation property (CODING_RULE_V2_00017)
        """
        return self.interpolation  # Delegates to property

    def getSwRecord(self) -> "SwRecordLayout":
        """
        AUTOSAR-compliant getter for swRecord.

        Returns:
            The swRecord value

        Note:
            Delegates to sw_record property (CODING_RULE_V2_00017)
        """
        return self.sw_record  # Delegates to property

    def setSwRecord(self, value: "SwRecordLayout") -> "InterpolationRoutineMapping":
        """
        AUTOSAR-compliant setter for swRecord with method chaining.

        Args:
            value: The swRecord to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_record property setter (gets validation automatically)
        """
        self.sw_record = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_record(self, value: Optional["SwRecordLayout"]) -> "InterpolationRoutineMapping":
        """
        Set swRecord and return self for chaining.

        Args:
            value: The swRecord to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_record("value")
        """
        self.sw_record = value  # Use property setter (gets validation)
        return self
