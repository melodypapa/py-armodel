"""
AUTOSAR Package - InterpolationRoutine

Package: M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::InterpolationRoutine
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    SwRecordLayout,
)


class InterpolationRoutineMappingSet(ARElement):
    """
    This meta-class specifies a set of interpolation routine mappings. (cid:53)
    429 of 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate
    Software Component Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::InterpolationRoutine::InterpolationRoutineMappingSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 429, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 46, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies one particular mapping of recordlayout and its matching
        # interpolationRoutines.
        self._interpolation: List[InterpolationRoutine] = []

    @property
    def interpolation(self) -> List[InterpolationRoutine]:
        """Get interpolation (Pythonic accessor)."""
        return self._interpolation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInterpolation(self) -> List[InterpolationRoutine]:
        """
        AUTOSAR-compliant getter for interpolation.

        Returns:
            The interpolation value

        Note:
            Delegates to interpolation property (CODING_RULE_V2_00017)
        """
        return self.interpolation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class InterpolationRoutineMapping(ARObject):
    """
    This meta-class provides a mapping between one record layout and its
    matching interpolation routines. This allows to formally specify the
    semantics of the interpolation routines. The use case is such that the
    curves/Maps define an interpolation method. This mapping table specifies
    which interpolation routine implements methods for a particular record
    layout. Using this information, the implementer of a software-component can
    select the appropriate interpolation routine.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::InterpolationRoutine::InterpolationRoutineMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 430, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 46, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular interpolation routine which is to the record layout.
        self._interpolation: List[InterpolationRoutine] = []

    @property
    def interpolation(self) -> List[InterpolationRoutine]:
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInterpolation(self) -> List[InterpolationRoutine]:
        """
        AUTOSAR-compliant getter for interpolation.

        Returns:
            The interpolation value

        Note:
            Delegates to interpolation property (CODING_RULE_V2_00017)
        """
        return self.interpolation  # Delegates to property

    def getSwRecord(self) -> SwRecordLayout:
        """
        AUTOSAR-compliant getter for swRecord.

        Returns:
            The swRecord value

        Note:
            Delegates to sw_record property (CODING_RULE_V2_00017)
        """
        return self.sw_record  # Delegates to property

    def setSwRecord(self, value: SwRecordLayout) -> InterpolationRoutineMapping:
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

    def with_sw_record(self, value: Optional["SwRecordLayout"]) -> InterpolationRoutineMapping:
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



class InterpolationRoutine(ARObject):
    """
    This represents an interpolation routine taken to evaluate the contents of a
    curve or map against a specific input value.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::MeasurementAndCalibration::InterpolationRoutine::InterpolationRoutine

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 430, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 46, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies a BswModuleEntry which implements the interpolation method for
        # the given record layout.
        self._interpolation: Optional["BswModuleEntry"] = None

    @property
    def interpolation(self) -> Optional["BswModuleEntry"]:
        """Get interpolation (Pythonic accessor)."""
        return self._interpolation

    @interpolation.setter
    def interpolation(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set interpolation with validation.

        Args:
            value: The interpolation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._interpolation = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"interpolation must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._interpolation = value
        # by the System Template) of a given that owns the 1228 Document ID 62:
        # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._isDefault: Optional[Boolean] = None

    @property
    def is_default(self) -> Optional[Boolean]:
        """Get isDefault (Pythonic accessor)."""
        return self._isDefault

    @is_default.setter
    def is_default(self, value: Optional[Boolean]) -> None:
        """
        Set isDefault with validation.

        Args:
            value: The isDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isDefault = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isDefault must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isDefault = value
                # bswModuleEntry.
        # It swInterpolationMethod in SwDataDef.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortLabel must be Identifier or str or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInterpolation(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for interpolation.

        Returns:
            The interpolation value

        Note:
            Delegates to interpolation property (CODING_RULE_V2_00017)
        """
        return self.interpolation  # Delegates to property

    def setInterpolation(self, value: "BswModuleEntry") -> InterpolationRoutine:
        """
        AUTOSAR-compliant setter for interpolation with method chaining.

        Args:
            value: The interpolation to set

        Returns:
            self for method chaining

        Note:
            Delegates to interpolation property setter (gets validation automatically)
        """
        self.interpolation = value  # Delegates to property setter
        return self

    def getIsDefault(self) -> Boolean:
        """
        AUTOSAR-compliant getter for isDefault.

        Returns:
            The isDefault value

        Note:
            Delegates to is_default property (CODING_RULE_V2_00017)
        """
        return self.is_default  # Delegates to property

    def setIsDefault(self, value: Boolean) -> InterpolationRoutine:
        """
        AUTOSAR-compliant setter for isDefault with method chaining.

        Args:
            value: The isDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_default property setter (gets validation automatically)
        """
        self.is_default = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> Identifier:
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: Identifier) -> InterpolationRoutine:
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_interpolation(self, value: Optional["BswModuleEntry"]) -> InterpolationRoutine:
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

    def with_is_default(self, value: Optional[Boolean]) -> InterpolationRoutine:
        """
        Set isDefault and return self for chaining.

        Args:
            value: The isDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_default("value")
        """
        self.is_default = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> InterpolationRoutine:
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self
