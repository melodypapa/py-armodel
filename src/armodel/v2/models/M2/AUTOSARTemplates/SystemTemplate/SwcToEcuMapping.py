from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    EcuInstance,
    HwElement,
    SwComponent,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class SwcToEcuMapping(Identifiable):
    """
    This meta-class is used: • to map SwComponentPrototypes to a specific ECU
    Instance unit, • optionally to map SwComponentPrototypes to a HwElement with
    category ProcessingUnit, • optionally to map SwComponentPrototypes typed by
    SensorActuatorSwComponentType to a Hw Element with category SensorActuator.
    For each combination of ECUInstance and the optional ProcessingUnit and the
    optional SensorActuator only one SwcToEcuMapping shall be used.

    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::SwcToEcuMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 197, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # to the referenced ECUInstance.
        # If the referenced is a composition, this all atomic software components
                # within the mapped to the ECU.
        # is aditionally a mapping of some SwComponent the Composition to another ECU
                # inner mapping overrides the outer mapping.
        # by: ComponentInSystem.
        self._component: List["SwComponent"] = []

    @property
    def component(self) -> List["SwComponent"]:
        """Get component (Pythonic accessor)."""
        return self._component
        # Optional mapping of SwComponentPrototypes that are by
        # SensorActuatorSwComponentType to a Hw category SensorActuator.
        self._controlledHw: Optional["HwElement"] = None

    @property
    def controlled_hw(self) -> Optional["HwElement"]:
        """Get controlledHw (Pythonic accessor)."""
        return self._controlledHw

    @controlled_hw.setter
    def controlled_hw(self, value: Optional["HwElement"]) -> None:
        """
        Set controlledHw with validation.

        Args:
            value: The controlledHw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._controlledHw = None
            return

        if not isinstance(value, HwElement):
            raise TypeError(
                f"controlledHw must be HwElement or None, got {type(value).__name__}"
            )
        self._controlledHw = value
        # Reference to a specific ECU Instance description.
        self._ecuInstance: Optional["EcuInstance"] = None

    @property
    def ecu_instance(self) -> Optional["EcuInstance"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional["EcuInstance"]) -> None:
        """
        Set ecuInstance with validation.

        Args:
            value: The ecuInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecuInstance must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
        # Optional mapping of software components to individual residing in one ECU.
        # A is described in the ECU Resource the HwElement of HwCategory Processing.
        self._processingUnit: Optional["HwElement"] = None

    @property
    def processing_unit(self) -> Optional["HwElement"]:
        """Get processingUnit (Pythonic accessor)."""
        return self._processingUnit

    @processing_unit.setter
    def processing_unit(self, value: Optional["HwElement"]) -> None:
        """
        Set processingUnit with validation.

        Args:
            value: The processingUnit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._processingUnit = None
            return

        if not isinstance(value, HwElement):
            raise TypeError(
                f"processingUnit must be HwElement or None, got {type(value).__name__}"
            )
        self._processingUnit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponent(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for component.

        Returns:
            The component value

        Note:
            Delegates to component property (CODING_RULE_V2_00017)
        """
        return self.component  # Delegates to property

    def getControlledHw(self) -> "HwElement":
        """
        AUTOSAR-compliant getter for controlledHw.

        Returns:
            The controlledHw value

        Note:
            Delegates to controlled_hw property (CODING_RULE_V2_00017)
        """
        return self.controlled_hw  # Delegates to property

    def setControlledHw(self, value: "HwElement") -> "SwcToEcuMapping":
        """
        AUTOSAR-compliant setter for controlledHw with method chaining.

        Args:
            value: The controlledHw to set

        Returns:
            self for method chaining

        Note:
            Delegates to controlled_hw property setter (gets validation automatically)
        """
        self.controlled_hw = value  # Delegates to property setter
        return self

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> "SwcToEcuMapping":
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
        return self

    def getProcessingUnit(self) -> "HwElement":
        """
        AUTOSAR-compliant getter for processingUnit.

        Returns:
            The processingUnit value

        Note:
            Delegates to processing_unit property (CODING_RULE_V2_00017)
        """
        return self.processing_unit  # Delegates to property

    def setProcessingUnit(self, value: "HwElement") -> "SwcToEcuMapping":
        """
        AUTOSAR-compliant setter for processingUnit with method chaining.

        Args:
            value: The processingUnit to set

        Returns:
            self for method chaining

        Note:
            Delegates to processing_unit property setter (gets validation automatically)
        """
        self.processing_unit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_controlled_hw(self, value: Optional["HwElement"]) -> "SwcToEcuMapping":
        """
        Set controlledHw and return self for chaining.

        Args:
            value: The controlledHw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_controlled_hw("value")
        """
        self.controlled_hw = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "SwcToEcuMapping":
        """
        Set ecuInstance and return self for chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self

    def with_processing_unit(self, value: Optional["HwElement"]) -> "SwcToEcuMapping":
        """
        Set processingUnit and return self for chaining.

        Args:
            value: The processingUnit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_processing_unit("value")
        """
        self.processing_unit = value  # Use property setter (gets validation)
        return self
