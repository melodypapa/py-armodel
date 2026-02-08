from abc import ABC
from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import TimingDescriptionEvent


class TDEventVfb(TimingDescriptionEvent, ABC):
    """
    This is the abstract parent class to describe timing events at Virtual
    Functional Bus (VFB) level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventVfb

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 51, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TDEventVfb:
            raise TypeError("TDEventVfb is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # implemented by: ComponentIn.
        self._componentCompositionInstanceRef: Optional["SwComponent"] = None

    @property
    def component_composition_instance_ref(self) -> Optional["SwComponent"]:
        """Get componentCompositionInstanceRef (Pythonic accessor)."""
        return self._componentCompositionInstanceRef

    @component_composition_instance_ref.setter
    def component_composition_instance_ref(self, value: Optional["SwComponent"]) -> None:
        """
        Set componentCompositionInstanceRef with validation.

        Args:
            value: The componentCompositionInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._componentCompositionInstanceRef = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"componentCompositionInstanceRef must be SwComponent or None, got {type(value).__name__}"
            )
        self._componentCompositionInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponentCompositionInstanceRef(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for componentCompositionInstanceRef.

        Returns:
            The componentCompositionInstanceRef value

        Note:
            Delegates to component_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.component_composition_instance_ref  # Delegates to property

    def setComponentCompositionInstanceRef(self, value: "SwComponent") -> "TDEventVfb":
        """
        AUTOSAR-compliant setter for componentCompositionInstanceRef with method chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to component_composition_instance_ref property setter (gets validation automatically)
        """
        self.component_composition_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_component_composition_instance_ref(self, value: Optional["SwComponent"]) -> "TDEventVfb":
        """
        Set componentCompositionInstanceRef and return self for chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_component_composition_instance_ref("value")
        """
        self.component_composition_instance_ref = value  # Use property setter (gets validation)
        return self
