from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SwCalprmAxisTypeProps(ARObject, ABC):
    """
    Base class for the type of the calibration axis. This provides the
    particular model of the specialization. If the specialization would be the
    directly from SwCalPrmAxis, the sequence of common properties and the
    specializes ones would be different.

    Package: M2::MSR::DataDictionary::CalibrationParameter

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
        self._maxGradient: Optional["Float"] = None

    @property
    def max_gradient(self) -> Optional["Float"]:
        """Get maxGradient (Pythonic accessor)."""
        return self._maxGradient

    @max_gradient.setter
    def max_gradient(self, value: Optional["Float"]) -> None:
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

        if not isinstance(value, Float):
            raise TypeError(
                f"maxGradient must be Float or None, got {type(value).__name__}"
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

    def getMaxGradient(self) -> "Float":
        """
        AUTOSAR-compliant getter for maxGradient.

        Returns:
            The maxGradient value

        Note:
            Delegates to max_gradient property (CODING_RULE_V2_00017)
        """
        return self.max_gradient  # Delegates to property

    def setMaxGradient(self, value: "Float") -> "SwCalprmAxisTypeProps":
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

    def setMonotony(self, value: "MonotonyEnum") -> "SwCalprmAxisTypeProps":
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

    def with_max_gradient(self, value: Optional["Float"]) -> "SwCalprmAxisTypeProps":
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

    def with_monotony(self, value: Optional["MonotonyEnum"]) -> "SwCalprmAxisTypeProps":
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
