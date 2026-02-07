from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CpSoftwareClusterToEcuInstanceMapping(Identifiable):
    """
    This meta class maps a CpSoftwareCluster to a EcuInstance.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterToEcuInstanceMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 283, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
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
        # Unique number of the (virtual or physical) machine to Software Cluster is
        # mapped.
        self._machineId: Optional["PositiveInteger"] = None

    @property
    def machine_id(self) -> Optional["PositiveInteger"]:
        """Get machineId (Pythonic accessor)."""
        return self._machineId

    @machine_id.setter
    def machine_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set machineId with validation.

        Args:
            value: The machineId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._machineId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"machineId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._machineId = value
        # The mapped CP Software Cluster atpVariation.
        self._swCluster: List["CpSoftwareCluster"] = []

    @property
    def sw_cluster(self) -> List["CpSoftwareCluster"]:
        """Get swCluster (Pythonic accessor)."""
        return self._swCluster

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> "CpSoftwareClusterToEcuInstanceMapping":
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

    def getMachineId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for machineId.

        Returns:
            The machineId value

        Note:
            Delegates to machine_id property (CODING_RULE_V2_00017)
        """
        return self.machine_id  # Delegates to property

    def setMachineId(self, value: "PositiveInteger") -> "CpSoftwareClusterToEcuInstanceMapping":
        """
        AUTOSAR-compliant setter for machineId with method chaining.

        Args:
            value: The machineId to set

        Returns:
            self for method chaining

        Note:
            Delegates to machine_id property setter (gets validation automatically)
        """
        self.machine_id = value  # Delegates to property setter
        return self

    def getSwCluster(self) -> List["CpSoftwareCluster"]:
        """
        AUTOSAR-compliant getter for swCluster.

        Returns:
            The swCluster value

        Note:
            Delegates to sw_cluster property (CODING_RULE_V2_00017)
        """
        return self.sw_cluster  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "CpSoftwareClusterToEcuInstanceMapping":
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

    def with_machine_id(self, value: Optional["PositiveInteger"]) -> "CpSoftwareClusterToEcuInstanceMapping":
        """
        Set machineId and return self for chaining.

        Args:
            value: The machineId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_machine_id("value")
        """
        self.machine_id = value  # Use property setter (gets validation)
        return self
