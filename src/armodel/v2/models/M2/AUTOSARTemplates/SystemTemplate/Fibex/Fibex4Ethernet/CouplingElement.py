from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CouplingElementEnum,
    CouplingPort,
    EcuInstance,
    EthernetCluster,
    FibexElement,
    StateDependentFirewall,
)


class CouplingElement(FibexElement):
    """
    A CouplingElement is used to connect EcuInstances to the VLAN of an
    EthernetCluster. Coupling Elements can reach from a simple hub to a complex
    managed switch or even devices with functionalities in higher layers. A
    CouplingElement that is not related to an EcuInstance occurs as a dedicated
    single device.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingElement

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 107, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This relationship defines to which cluster the Coupling belongs.
        self._communication: Optional["EthernetCluster"] = None

    @property
    def communication(self) -> Optional["EthernetCluster"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["EthernetCluster"]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, EthernetCluster):
            raise TypeError(
                f"communication must be EthernetCluster or None, got {type(value).__name__}"
            )
        self._communication = value
        # Definition of details for this specific CouplingElement.
        # Stereotypes: atpSplitable; atpVariation 2090 Document ID 63:
                # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._coupling: Optional["CouplingElement"] = None

    @property
    def coupling(self) -> Optional["CouplingElement"]:
        """Get coupling (Pythonic accessor)."""
        return self._coupling

    @coupling.setter
    def coupling(self, value: Optional["CouplingElement"]) -> None:
        """
        Set coupling with validation.

        Args:
            value: The coupling to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._coupling = None
            return

        if not isinstance(value, CouplingElement):
            raise TypeError(
                f"coupling must be CouplingElement or None, got {type(value).__name__}"
            )
        self._coupling = value
        # Hardware Port of the CouplingElement that is used to CouplingPort to
        # EcuInstances or other atpVariation.
        self._couplingPort: List["CouplingPort"] = []

    @property
    def coupling_port(self) -> List["CouplingPort"]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort
        # Describes the coupling type of this CouplingElement.
        self._couplingType: Optional["CouplingElementEnum"] = None

    @property
    def coupling_type(self) -> Optional["CouplingElementEnum"]:
        """Get couplingType (Pythonic accessor)."""
        return self._couplingType

    @coupling_type.setter
    def coupling_type(self, value: Optional["CouplingElementEnum"]) -> None:
        """
        Set couplingType with validation.

        Args:
            value: The couplingType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._couplingType = None
            return

        if not isinstance(value, CouplingElementEnum):
            raise TypeError(
                f"couplingType must be CouplingElementEnum or None, got {type(value).__name__}"
            )
        self._couplingType = value
        # Optional reference to the ECU where the Coupling located.
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
        # Firewall rules defined in the context of a Coupling.
        self._firewallRule: List["StateDependentFirewall"] = []

    @property
    def firewall_rule(self) -> List["StateDependentFirewall"]:
        """Get firewallRule (Pythonic accessor)."""
        return self._firewallRule

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "EthernetCluster":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "EthernetCluster") -> "CouplingElement":
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    def getCoupling(self) -> "CouplingElement":
        """
        AUTOSAR-compliant getter for coupling.

        Returns:
            The coupling value

        Note:
            Delegates to coupling property (CODING_RULE_V2_00017)
        """
        return self.coupling  # Delegates to property

    def setCoupling(self, value: "CouplingElement") -> "CouplingElement":
        """
        AUTOSAR-compliant setter for coupling with method chaining.

        Args:
            value: The coupling to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling property setter (gets validation automatically)
        """
        self.coupling = value  # Delegates to property setter
        return self

    def getCouplingPort(self) -> List["CouplingPort"]:
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def getCouplingType(self) -> "CouplingElementEnum":
        """
        AUTOSAR-compliant getter for couplingType.

        Returns:
            The couplingType value

        Note:
            Delegates to coupling_type property (CODING_RULE_V2_00017)
        """
        return self.coupling_type  # Delegates to property

    def setCouplingType(self, value: "CouplingElementEnum") -> "CouplingElement":
        """
        AUTOSAR-compliant setter for couplingType with method chaining.

        Args:
            value: The couplingType to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling_type property setter (gets validation automatically)
        """
        self.coupling_type = value  # Delegates to property setter
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

    def setEcuInstance(self, value: "EcuInstance") -> "CouplingElement":
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

    def getFirewallRule(self) -> List["StateDependentFirewall"]:
        """
        AUTOSAR-compliant getter for firewallRule.

        Returns:
            The firewallRule value

        Note:
            Delegates to firewall_rule property (CODING_RULE_V2_00017)
        """
        return self.firewall_rule  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["EthernetCluster"]) -> "CouplingElement":
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self

    def with_coupling(self, value: Optional["CouplingElement"]) -> "CouplingElement":
        """
        Set coupling and return self for chaining.

        Args:
            value: The coupling to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling("value")
        """
        self.coupling = value  # Use property setter (gets validation)
        return self

    def with_coupling_type(self, value: Optional["CouplingElementEnum"]) -> "CouplingElement":
        """
        Set couplingType and return self for chaining.

        Args:
            value: The couplingType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling_type("value")
        """
        self.coupling_type = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "CouplingElement":
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
