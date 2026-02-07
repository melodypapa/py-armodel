from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class RootSwCompositionPrototype(Identifiable):
    """
    The RootSwCompositionPrototype represents the top-level-composition of
    software components within a given System. According to the use case of the
    System, this may for example be a more or less complete VFB description, the
    software of a System Extract or the software of a flat ECU Extract with only
    atomic SWCs. Therefore the RootSwComposition will only occasionally contain
    all atomic software components that are used in a complete VFB System. The
    OEM is primarily interested in the required functionality and the interfaces
    defining the integration of the Software Component into the System. The
    internal structure of such a component contains often substantial
    intellectual property of a supplier. Therefore a top-level software
    composition will often contain empty compositions which represent
    subsystems. The contained SwComponentPrototypes are fully specified by their
    SwComponentTypes (including Port Prototypes, PortInterfaces,
    VariableDataPrototypes, SwcInternalBehavior etc.), and their ports are
    interconnected using SwConnectorPrototypes.

    Package: M2::AUTOSARTemplates::SystemTemplate::RootSwCompositionPrototype

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1003, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 186, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 240, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 18, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Used CalibrationParameterValueSet for instance specific initialization of
                # calibration parameters.
        # atpSplitable.
        self._calibration: List["CalibrationParameter"] = []

    @property
    def calibration(self) -> List["CalibrationParameter"]:
        """Get calibration (Pythonic accessor)."""
        return self._calibration
        # The FlatMap used in the scope of this RootSw.
        self._flatMap: Optional["FlatMap"] = None

    @property
    def flat_map(self) -> Optional["FlatMap"]:
        """Get flatMap (Pythonic accessor)."""
        return self._flatMap

    @flat_map.setter
    def flat_map(self, value: Optional["FlatMap"]) -> None:
        """
        Set flatMap with validation.

        Args:
            value: The flatMap to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flatMap = None
            return

        if not isinstance(value, FlatMap):
            raise TypeError(
                f"flatMap must be FlatMap or None, got {type(value).__name__}"
            )
        self._flatMap = value
        # that includes all Component instances of the system.
        self._software: Optional["CompositionSw"] = None

    @property
    def software(self) -> Optional["CompositionSw"]:
        """Get software (Pythonic accessor)."""
        return self._software

    @software.setter
    def software(self, value: Optional["CompositionSw"]) -> None:
        """
        Set software with validation.

        Args:
            value: The software to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._software = None
            return

        if not isinstance(value, CompositionSw):
            raise TypeError(
                f"software must be CompositionSw or None, got {type(value).__name__}"
            )
        self._software = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalibration(self) -> List["CalibrationParameter"]:
        """
        AUTOSAR-compliant getter for calibration.

        Returns:
            The calibration value

        Note:
            Delegates to calibration property (CODING_RULE_V2_00017)
        """
        return self.calibration  # Delegates to property

    def getFlatMap(self) -> "FlatMap":
        """
        AUTOSAR-compliant getter for flatMap.

        Returns:
            The flatMap value

        Note:
            Delegates to flat_map property (CODING_RULE_V2_00017)
        """
        return self.flat_map  # Delegates to property

    def setFlatMap(self, value: "FlatMap") -> "RootSwCompositionPrototype":
        """
        AUTOSAR-compliant setter for flatMap with method chaining.

        Args:
            value: The flatMap to set

        Returns:
            self for method chaining

        Note:
            Delegates to flat_map property setter (gets validation automatically)
        """
        self.flat_map = value  # Delegates to property setter
        return self

    def getSoftware(self) -> "CompositionSw":
        """
        AUTOSAR-compliant getter for software.

        Returns:
            The software value

        Note:
            Delegates to software property (CODING_RULE_V2_00017)
        """
        return self.software  # Delegates to property

    def setSoftware(self, value: "CompositionSw") -> "RootSwCompositionPrototype":
        """
        AUTOSAR-compliant setter for software with method chaining.

        Args:
            value: The software to set

        Returns:
            self for method chaining

        Note:
            Delegates to software property setter (gets validation automatically)
        """
        self.software = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_flat_map(self, value: Optional["FlatMap"]) -> "RootSwCompositionPrototype":
        """
        Set flatMap and return self for chaining.

        Args:
            value: The flatMap to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flat_map("value")
        """
        self.flat_map = value  # Use property setter (gets validation)
        return self

    def with_software(self, value: Optional["CompositionSw"]) -> "RootSwCompositionPrototype":
        """
        Set software and return self for chaining.

        Args:
            value: The software to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_software("value")
        """
        self.software = value  # Use property setter (gets validation)
        return self
