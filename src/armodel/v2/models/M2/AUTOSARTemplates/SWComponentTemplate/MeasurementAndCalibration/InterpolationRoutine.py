from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BswModuleEntry,
    Identifier,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


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
        # This attribute specifies whether the enclosing considered the default in the
        # by the System Template) of a given that owns the 1228 Document ID 62:
        # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._isDefault: Optional["Boolean"] = None

    @property
    def is_default(self) -> Optional["Boolean"]:
        """Get isDefault (Pythonic accessor)."""
        return self._isDefault

    @is_default.setter
    def is_default(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isDefault must be Boolean or None, got {type(value).__name__}"
            )
        self._isDefault = value
        # This is the name of the interpolation method which is the referenced
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

        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier or None, got {type(value).__name__}"
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

    def setInterpolation(self, value: "BswModuleEntry") -> "InterpolationRoutine":
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

    def getIsDefault(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isDefault.

        Returns:
            The isDefault value

        Note:
            Delegates to is_default property (CODING_RULE_V2_00017)
        """
        return self.is_default  # Delegates to property

    def setIsDefault(self, value: "Boolean") -> "InterpolationRoutine":
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

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> "InterpolationRoutine":
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

    def with_interpolation(self, value: Optional["BswModuleEntry"]) -> "InterpolationRoutine":
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

    def with_is_default(self, value: Optional["Boolean"]) -> "InterpolationRoutine":
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

    def with_short_label(self, value: Optional["Identifier"]) -> "InterpolationRoutine":
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
