from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class CanTpEcu(ARObject):
    """
    ECU specific TP configuration parameters. Each TpEcu element has a reference
    to exactly one ECUInstance in the topology.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 610, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The period between successive calls to the Main Function the AUTOSAR TP.
        # Specified in seconds.
        self._cycleTimeMain: Optional["TimeValue"] = None

    @property
    def cycle_time_main(self) -> Optional["TimeValue"]:
        """Get cycleTimeMain (Pythonic accessor)."""
        return self._cycleTimeMain

    @cycle_time_main.setter
    def cycle_time_main(self, value: Optional["TimeValue"]) -> None:
        """
        Set cycleTimeMain with validation.

        Args:
            value: The cycleTimeMain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cycleTimeMain = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"cycleTimeMain must be TimeValue or None, got {type(value).__name__}"
            )
        self._cycleTimeMain = value
        # Connection to the ECUInstance in the Topology.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCycleTimeMain(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for cycleTimeMain.

        Returns:
            The cycleTimeMain value

        Note:
            Delegates to cycle_time_main property (CODING_RULE_V2_00017)
        """
        return self.cycle_time_main  # Delegates to property

    def setCycleTimeMain(self, value: "TimeValue") -> "CanTpEcu":
        """
        AUTOSAR-compliant setter for cycleTimeMain with method chaining.

        Args:
            value: The cycleTimeMain to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_time_main property setter (gets validation automatically)
        """
        self.cycle_time_main = value  # Delegates to property setter
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

    def setEcuInstance(self, value: "EcuInstance") -> "CanTpEcu":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cycle_time_main(self, value: Optional["TimeValue"]) -> "CanTpEcu":
        """
        Set cycleTimeMain and return self for chaining.

        Args:
            value: The cycleTimeMain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_time_main("value")
        """
        self.cycle_time_main = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "CanTpEcu":
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
