from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    AtomicSwComponentType,
)


class SensorActuatorSwComponentType(AtomicSwComponentType):
    """
    The SensorActuatorSwComponentType introduces the possibility to link from
    the software representation of a sensor/actuator to its hardware description
    provided by the ECU Resource Template.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 646, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2055, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 244, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference from the Sensor Actuator Software Component the description of the
        # actual hardware.
        self._sensorActuator: Optional["HwDescriptionEntity"] = None

    @property
    def sensor_actuator(self) -> Optional["HwDescriptionEntity"]:
        """Get sensorActuator (Pythonic accessor)."""
        return self._sensorActuator

    @sensor_actuator.setter
    def sensor_actuator(self, value: Optional["HwDescriptionEntity"]) -> None:
        """
        Set sensorActuator with validation.

        Args:
            value: The sensorActuator to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sensorActuator = None
            return

        if not isinstance(value, HwDescriptionEntity):
            raise TypeError(
                f"sensorActuator must be HwDescriptionEntity or None, got {type(value).__name__}"
            )
        self._sensorActuator = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSensorActuator(self) -> "HwDescriptionEntity":
        """
        AUTOSAR-compliant getter for sensorActuator.

        Returns:
            The sensorActuator value

        Note:
            Delegates to sensor_actuator property (CODING_RULE_V2_00017)
        """
        return self.sensor_actuator  # Delegates to property

    def setSensorActuator(self, value: "HwDescriptionEntity") -> "SensorActuatorSwComponentType":
        """
        AUTOSAR-compliant setter for sensorActuator with method chaining.

        Args:
            value: The sensorActuator to set

        Returns:
            self for method chaining

        Note:
            Delegates to sensor_actuator property setter (gets validation automatically)
        """
        self.sensor_actuator = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sensor_actuator(self, value: Optional["HwDescriptionEntity"]) -> "SensorActuatorSwComponentType":
        """
        Set sensorActuator and return self for chaining.

        Args:
            value: The sensorActuator to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sensor_actuator("value")
        """
        self.sensor_actuator = value  # Use property setter (gets validation)
        return self
