from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class GlobalTimeGateway(Identifiable):
    """
    This represents the ability to define a time gateway for establishing a
    global time domain over several communication clusters.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 861, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The GlobalTimeGateway is hosted by the referenced Ecu.
        self._host: Optional["EcuInstance"] = None

    @property
    def host(self) -> Optional["EcuInstance"]:
        """Get host (Pythonic accessor)."""
        return self._host

    @host.setter
    def host(self, value: Optional["EcuInstance"]) -> None:
        """
        Set host with validation.

        Args:
            value: The host to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._host = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"host must be EcuInstance or None, got {type(value).__name__}"
            )
        self._host = value
        # This represents the master of the global time gateway.
        self._master: Optional["GlobalTimeMaster"] = None

    @property
    def master(self) -> Optional["GlobalTimeMaster"]:
        """Get master (Pythonic accessor)."""
        return self._master

    @master.setter
    def master(self, value: Optional["GlobalTimeMaster"]) -> None:
        """
        Set master with validation.

        Args:
            value: The master to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._master = None
            return

        if not isinstance(value, GlobalTimeMaster):
            raise TypeError(
                f"master must be GlobalTimeMaster or None, got {type(value).__name__}"
            )
        self._master = value
        # This represents the slave of the GlobalTimeGateway.
        self._slave: Optional["GlobalTimeSlave"] = None

    @property
    def slave(self) -> Optional["GlobalTimeSlave"]:
        """Get slave (Pythonic accessor)."""
        return self._slave

    @slave.setter
    def slave(self, value: Optional["GlobalTimeSlave"]) -> None:
        """
        Set slave with validation.

        Args:
            value: The slave to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slave = None
            return

        if not isinstance(value, GlobalTimeSlave):
            raise TypeError(
                f"slave must be GlobalTimeSlave or None, got {type(value).__name__}"
            )
        self._slave = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHost(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for host.

        Returns:
            The host value

        Note:
            Delegates to host property (CODING_RULE_V2_00017)
        """
        return self.host  # Delegates to property

    def setHost(self, value: "EcuInstance") -> "GlobalTimeGateway":
        """
        AUTOSAR-compliant setter for host with method chaining.

        Args:
            value: The host to set

        Returns:
            self for method chaining

        Note:
            Delegates to host property setter (gets validation automatically)
        """
        self.host = value  # Delegates to property setter
        return self

    def getMaster(self) -> "GlobalTimeMaster":
        """
        AUTOSAR-compliant getter for master.

        Returns:
            The master value

        Note:
            Delegates to master property (CODING_RULE_V2_00017)
        """
        return self.master  # Delegates to property

    def setMaster(self, value: "GlobalTimeMaster") -> "GlobalTimeGateway":
        """
        AUTOSAR-compliant setter for master with method chaining.

        Args:
            value: The master to set

        Returns:
            self for method chaining

        Note:
            Delegates to master property setter (gets validation automatically)
        """
        self.master = value  # Delegates to property setter
        return self

    def getSlave(self) -> "GlobalTimeSlave":
        """
        AUTOSAR-compliant getter for slave.

        Returns:
            The slave value

        Note:
            Delegates to slave property (CODING_RULE_V2_00017)
        """
        return self.slave  # Delegates to property

    def setSlave(self, value: "GlobalTimeSlave") -> "GlobalTimeGateway":
        """
        AUTOSAR-compliant setter for slave with method chaining.

        Args:
            value: The slave to set

        Returns:
            self for method chaining

        Note:
            Delegates to slave property setter (gets validation automatically)
        """
        self.slave = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_host(self, value: Optional["EcuInstance"]) -> "GlobalTimeGateway":
        """
        Set host and return self for chaining.

        Args:
            value: The host to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_host("value")
        """
        self.host = value  # Use property setter (gets validation)
        return self

    def with_master(self, value: Optional["GlobalTimeMaster"]) -> "GlobalTimeGateway":
        """
        Set master and return self for chaining.

        Args:
            value: The master to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_master("value")
        """
        self.master = value  # Use property setter (gets validation)
        return self

    def with_slave(self, value: Optional["GlobalTimeSlave"]) -> "GlobalTimeGateway":
        """
        Set slave and return self for chaining.

        Args:
            value: The slave to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_slave("value")
        """
        self.slave = value  # Use property setter (gets validation)
        return self
