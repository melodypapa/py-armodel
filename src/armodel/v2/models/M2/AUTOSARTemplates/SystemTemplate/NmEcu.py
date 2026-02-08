from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class NmEcu(Identifiable):
    """
    ECU on which NM is running.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::NmEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 674, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Cluster specific NmEcu attributes.
        self._busDependentNmEcu: List["BusspecificNmEcu"] = []

    @property
    def bus_dependent_nm_ecu(self) -> List["BusspecificNmEcu"]:
        """Get busDependentNmEcu (Pythonic accessor)."""
        return self._busDependentNmEcu
        # Association to an ECUInstance in the topology.
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
        # Enables bus synchronization support.
        self._nmBusSynchronizationEnabled: Optional["Boolean"] = None

    @property
    def nm_bus_synchronization_enabled(self) -> Optional["Boolean"]:
        """Get nmBusSynchronizationEnabled (Pythonic accessor)."""
        return self._nmBusSynchronizationEnabled

    @nm_bus_synchronization_enabled.setter
    def nm_bus_synchronization_enabled(self, value: Optional["Boolean"]) -> None:
        """
        Set nmBusSynchronizationEnabled with validation.

        Args:
            value: The nmBusSynchronizationEnabled to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmBusSynchronizationEnabled = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmBusSynchronizationEnabled must be Boolean or None, got {type(value).__name__}"
            )
        self._nmBusSynchronizationEnabled = value
        # Enables the Communication Control support.
        self._nmComControlEnabled: Optional["Boolean"] = None

    @property
    def nm_com_control_enabled(self) -> Optional["Boolean"]:
        """Get nmComControlEnabled (Pythonic accessor)."""
        return self._nmComControlEnabled

    @nm_com_control_enabled.setter
    def nm_com_control_enabled(self, value: Optional["Boolean"]) -> None:
        """
        Set nmComControlEnabled with validation.

        Args:
            value: The nmComControlEnabled to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmComControlEnabled = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmComControlEnabled must be Boolean or None, got {type(value).__name__}"
            )
        self._nmComControlEnabled = value
        # Nm ECU may coordinate different clusters.
        self._nmCoordinator: Optional["NmCoordinator"] = None

    @property
    def nm_coordinator(self) -> Optional["NmCoordinator"]:
        """Get nmCoordinator (Pythonic accessor)."""
        return self._nmCoordinator

    @nm_coordinator.setter
    def nm_coordinator(self, value: Optional["NmCoordinator"]) -> None:
        """
        Set nmCoordinator with validation.

        Args:
            value: The nmCoordinator to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCoordinator = None
            return

        if not isinstance(value, NmCoordinator):
            raise TypeError(
                f"nmCoordinator must be NmCoordinator or None, got {type(value).__name__}"
            )
        self._nmCoordinator = value
        # The period between successive calls to the Main Function the NM Interface in
        # seconds.
        self._nmCycletime: Optional["TimeValue"] = None

    @property
    def nm_cycletime(self) -> Optional["TimeValue"]:
        """Get nmCycletime (Pythonic accessor)."""
        return self._nmCycletime

    @nm_cycletime.setter
    def nm_cycletime(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmCycletime with validation.

        Args:
            value: The nmCycletime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCycletime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmCycletime must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmCycletime = value
        # Switch for enabling the PDU Rx Indication.
        self._nmPduRxIndicationEnabled: Optional["Boolean"] = None

    @property
    def nm_pdu_rx_indication_enabled(self) -> Optional["Boolean"]:
        """Get nmPduRxIndicationEnabled (Pythonic accessor)."""
        return self._nmPduRxIndicationEnabled

    @nm_pdu_rx_indication_enabled.setter
    def nm_pdu_rx_indication_enabled(self, value: Optional["Boolean"]) -> None:
        """
        Set nmPduRxIndicationEnabled with validation.

        Args:
            value: The nmPduRxIndicationEnabled to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmPduRxIndicationEnabled = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmPduRxIndicationEnabled must be Boolean or None, got {type(value).__name__}"
            )
        self._nmPduRxIndicationEnabled = value
        # Switch for enabling remote sleep indication support.
        self._nmRemote: Optional["Boolean"] = None

    @property
    def nm_remote(self) -> Optional["Boolean"]:
        """Get nmRemote (Pythonic accessor)."""
        return self._nmRemote

    @nm_remote.setter
    def nm_remote(self, value: Optional["Boolean"]) -> None:
        """
        Set nmRemote with validation.

        Args:
            value: The nmRemote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRemote = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmRemote must be Boolean or None, got {type(value).__name__}"
            )
        self._nmRemote = value
        # Enables the CAN Network Management state change.
        self._nmStateChange: Optional["Boolean"] = None

    @property
    def nm_state_change(self) -> Optional["Boolean"]:
        """Get nmStateChange (Pythonic accessor)."""
        return self._nmStateChange

    @nm_state_change.setter
    def nm_state_change(self, value: Optional["Boolean"]) -> None:
        """
        Set nmStateChange with validation.

        Args:
            value: The nmStateChange to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmStateChange = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmStateChange must be Boolean or None, got {type(value).__name__}"
            )
        self._nmStateChange = value
        # Switch for enabling user data support.
        self._nmUserDataEnabled: Optional["Boolean"] = None

    @property
    def nm_user_data_enabled(self) -> Optional["Boolean"]:
        """Get nmUserDataEnabled (Pythonic accessor)."""
        return self._nmUserDataEnabled

    @nm_user_data_enabled.setter
    def nm_user_data_enabled(self, value: Optional["Boolean"]) -> None:
        """
        Set nmUserDataEnabled with validation.

        Args:
            value: The nmUserDataEnabled to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmUserDataEnabled = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmUserDataEnabled must be Boolean or None, got {type(value).__name__}"
            )
        self._nmUserDataEnabled = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBusDependentNmEcu(self) -> List["BusspecificNmEcu"]:
        """
        AUTOSAR-compliant getter for busDependentNmEcu.

        Returns:
            The busDependentNmEcu value

        Note:
            Delegates to bus_dependent_nm_ecu property (CODING_RULE_V2_00017)
        """
        return self.bus_dependent_nm_ecu  # Delegates to property

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> "NmEcu":
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

    def getNmBusSynchronizationEnabled(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmBusSynchronizationEnabled.

        Returns:
            The nmBusSynchronizationEnabled value

        Note:
            Delegates to nm_bus_synchronization_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_bus_synchronization_enabled  # Delegates to property

    def setNmBusSynchronizationEnabled(self, value: "Boolean") -> "NmEcu":
        """
        AUTOSAR-compliant setter for nmBusSynchronizationEnabled with method chaining.

        Args:
            value: The nmBusSynchronizationEnabled to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_bus_synchronization_enabled property setter (gets validation automatically)
        """
        self.nm_bus_synchronization_enabled = value  # Delegates to property setter
        return self

    def getNmComControlEnabled(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmComControlEnabled.

        Returns:
            The nmComControlEnabled value

        Note:
            Delegates to nm_com_control_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_com_control_enabled  # Delegates to property

    def setNmComControlEnabled(self, value: "Boolean") -> "NmEcu":
        """
        AUTOSAR-compliant setter for nmComControlEnabled with method chaining.

        Args:
            value: The nmComControlEnabled to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_com_control_enabled property setter (gets validation automatically)
        """
        self.nm_com_control_enabled = value  # Delegates to property setter
        return self

    def getNmCoordinator(self) -> "NmCoordinator":
        """
        AUTOSAR-compliant getter for nmCoordinator.

        Returns:
            The nmCoordinator value

        Note:
            Delegates to nm_coordinator property (CODING_RULE_V2_00017)
        """
        return self.nm_coordinator  # Delegates to property

    def setNmCoordinator(self, value: "NmCoordinator") -> "NmEcu":
        """
        AUTOSAR-compliant setter for nmCoordinator with method chaining.

        Args:
            value: The nmCoordinator to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_coordinator property setter (gets validation automatically)
        """
        self.nm_coordinator = value  # Delegates to property setter
        return self

    def getNmCycletime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmCycletime.

        Returns:
            The nmCycletime value

        Note:
            Delegates to nm_cycletime property (CODING_RULE_V2_00017)
        """
        return self.nm_cycletime  # Delegates to property

    def setNmCycletime(self, value: "TimeValue") -> "NmEcu":
        """
        AUTOSAR-compliant setter for nmCycletime with method chaining.

        Args:
            value: The nmCycletime to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_cycletime property setter (gets validation automatically)
        """
        self.nm_cycletime = value  # Delegates to property setter
        return self

    def getNmPduRxIndicationEnabled(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmPduRxIndicationEnabled.

        Returns:
            The nmPduRxIndicationEnabled value

        Note:
            Delegates to nm_pdu_rx_indication_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_pdu_rx_indication_enabled  # Delegates to property

    def setNmPduRxIndicationEnabled(self, value: "Boolean") -> "NmEcu":
        """
        AUTOSAR-compliant setter for nmPduRxIndicationEnabled with method chaining.

        Args:
            value: The nmPduRxIndicationEnabled to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_pdu_rx_indication_enabled property setter (gets validation automatically)
        """
        self.nm_pdu_rx_indication_enabled = value  # Delegates to property setter
        return self

    def getNmRemote(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmRemote.

        Returns:
            The nmRemote value

        Note:
            Delegates to nm_remote property (CODING_RULE_V2_00017)
        """
        return self.nm_remote  # Delegates to property

    def setNmRemote(self, value: "Boolean") -> "NmEcu":
        """
        AUTOSAR-compliant setter for nmRemote with method chaining.

        Args:
            value: The nmRemote to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_remote property setter (gets validation automatically)
        """
        self.nm_remote = value  # Delegates to property setter
        return self

    def getNmStateChange(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmStateChange.

        Returns:
            The nmStateChange value

        Note:
            Delegates to nm_state_change property (CODING_RULE_V2_00017)
        """
        return self.nm_state_change  # Delegates to property

    def setNmStateChange(self, value: "Boolean") -> "NmEcu":
        """
        AUTOSAR-compliant setter for nmStateChange with method chaining.

        Args:
            value: The nmStateChange to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_state_change property setter (gets validation automatically)
        """
        self.nm_state_change = value  # Delegates to property setter
        return self

    def getNmUserDataEnabled(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmUserDataEnabled.

        Returns:
            The nmUserDataEnabled value

        Note:
            Delegates to nm_user_data_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_user_data_enabled  # Delegates to property

    def setNmUserDataEnabled(self, value: "Boolean") -> "NmEcu":
        """
        AUTOSAR-compliant setter for nmUserDataEnabled with method chaining.

        Args:
            value: The nmUserDataEnabled to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_user_data_enabled property setter (gets validation automatically)
        """
        self.nm_user_data_enabled = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "NmEcu":
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

    def with_nm_bus_synchronization_enabled(self, value: Optional["Boolean"]) -> "NmEcu":
        """
        Set nmBusSynchronizationEnabled and return self for chaining.

        Args:
            value: The nmBusSynchronizationEnabled to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_bus_synchronization_enabled("value")
        """
        self.nm_bus_synchronization_enabled = value  # Use property setter (gets validation)
        return self

    def with_nm_com_control_enabled(self, value: Optional["Boolean"]) -> "NmEcu":
        """
        Set nmComControlEnabled and return self for chaining.

        Args:
            value: The nmComControlEnabled to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_com_control_enabled("value")
        """
        self.nm_com_control_enabled = value  # Use property setter (gets validation)
        return self

    def with_nm_coordinator(self, value: Optional["NmCoordinator"]) -> "NmEcu":
        """
        Set nmCoordinator and return self for chaining.

        Args:
            value: The nmCoordinator to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_coordinator("value")
        """
        self.nm_coordinator = value  # Use property setter (gets validation)
        return self

    def with_nm_cycletime(self, value: Optional["TimeValue"]) -> "NmEcu":
        """
        Set nmCycletime and return self for chaining.

        Args:
            value: The nmCycletime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_cycletime("value")
        """
        self.nm_cycletime = value  # Use property setter (gets validation)
        return self

    def with_nm_pdu_rx_indication_enabled(self, value: Optional["Boolean"]) -> "NmEcu":
        """
        Set nmPduRxIndicationEnabled and return self for chaining.

        Args:
            value: The nmPduRxIndicationEnabled to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_pdu_rx_indication_enabled("value")
        """
        self.nm_pdu_rx_indication_enabled = value  # Use property setter (gets validation)
        return self

    def with_nm_remote(self, value: Optional["Boolean"]) -> "NmEcu":
        """
        Set nmRemote and return self for chaining.

        Args:
            value: The nmRemote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_remote("value")
        """
        self.nm_remote = value  # Use property setter (gets validation)
        return self

    def with_nm_state_change(self, value: Optional["Boolean"]) -> "NmEcu":
        """
        Set nmStateChange and return self for chaining.

        Args:
            value: The nmStateChange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_state_change("value")
        """
        self.nm_state_change = value  # Use property setter (gets validation)
        return self

    def with_nm_user_data_enabled(self, value: Optional["Boolean"]) -> "NmEcu":
        """
        Set nmUserDataEnabled and return self for chaining.

        Args:
            value: The nmUserDataEnabled to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_user_data_enabled("value")
        """
        self.nm_user_data_enabled = value  # Use property setter (gets validation)
        return self
