"""
AUTOSAR Package - NetworkManagement

Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.__init__ import (
    FibexElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (    FlexrayNmSchedule,    J1939NmAddress,    NmClusterCoupling,    NmCoordinatorRole,    NmEcu,    NmPdu,)from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate import (    Communication,    CommunicationCluster,    EcuInstance,)from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet import (    EthernetPhysical,)from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (    TimeValue,)

class NmConfig(FibexElement):
    """
    Contains the all configuration elements for AUTOSAR Nm.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::NmConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 672, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of NmClusterCouplings Derived, because NmCluster can vary.
        # atpVariation.
        self._nmCluster: List[NmClusterCoupling] = []

    @property
    def nm_cluster(self) -> List[NmClusterCoupling]:
        """Get nmCluster (Pythonic accessor)."""
        return self._nmCluster
        # Collection of NM ECUs because EcuInstance can be atpVariation.
        self._nmIfEcu: List[NmEcu] = []

    @property
    def nm_if_ecu(self) -> List[NmEcu]:
        """Get nmIfEcu (Pythonic accessor)."""
        return self._nmIfEcu

    def with_nm_cluster(self, value):
        """
        Set nm_cluster and return self for chaining.

        Args:
            value: The nm_cluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_cluster("value")
        """
        self.nm_cluster = value  # Use property setter (gets validation)
        return self

    def with_bus_dependent_nm_ecu(self, value):
        """
        Set bus_dependent_nm_ecu and return self for chaining.

        Args:
            value: The bus_dependent_nm_ecu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bus_dependent_nm_ecu("value")
        """
        self.bus_dependent_nm_ecu = value  # Use property setter (gets validation)
        return self

    def with_rx_nm_pdu(self, value):
        """
        Set rx_nm_pdu and return self for chaining.

        Args:
            value: The rx_nm_pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rx_nm_pdu("value")
        """
        self.rx_nm_pdu = value  # Use property setter (gets validation)
        return self

    def with_tx_nm_pdu(self, value):
        """
        Set tx_nm_pdu and return self for chaining.

        Args:
            value: The tx_nm_pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tx_nm_pdu("value")
        """
        self.tx_nm_pdu = value  # Use property setter (gets validation)
        return self

    def with_coupled_cluster(self, value):
        """
        Set coupled_cluster and return self for chaining.

        Args:
            value: The coupled_cluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupled_cluster("value")
        """
        self.coupled_cluster = value  # Use property setter (gets validation)
        return self

    def with_coupled_cluster(self, value):
        """
        Set coupled_cluster and return self for chaining.

        Args:
            value: The coupled_cluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupled_cluster("value")
        """
        self.coupled_cluster = value  # Use property setter (gets validation)
        return self

    def with_coupled_cluster(self, value):
        """
        Set coupled_cluster and return self for chaining.

        Args:
            value: The coupled_cluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupled_cluster("value")
        """
        self.coupled_cluster = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmCluster(self) -> List[NmClusterCoupling]:
        """
        AUTOSAR-compliant getter for nmCluster.

        Returns:
            The nmCluster value

        Note:
            Delegates to nm_cluster property (CODING_RULE_V2_00017)
        """
        return self.nm_cluster  # Delegates to property

    def getNmIfEcu(self) -> List[NmEcu]:
        """
        AUTOSAR-compliant getter for nmIfEcu.

        Returns:
            The nmIfEcu value

        Note:
            Delegates to nm_if_ecu property (CODING_RULE_V2_00017)
        """
        return self.nm_if_ecu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class NmCluster(Identifiable, ABC):
    """
    Set of NM nodes coordinated with use of the NM algorithm.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::NmCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 672, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is NmCluster:
            raise TypeError("NmCluster is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to a CommunicationCluster in the topology.
        self._communication: Optional[CommunicationCluster] = None

    @property
    def communication(self) -> Optional[CommunicationCluster]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional[CommunicationCluster]) -> None:
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

        if not isinstance(value, CommunicationCluster):
            raise TypeError(
                f"communication must be CommunicationCluster or None, got {type(value).__name__}"
            )
        self._communication = value
        # absolutely decided by the local node only no other nodes can oppose that
        # decision.
        self._nmChannel: Optional[Boolean] = None

    @property
    def nm_channel(self) -> Optional[Boolean]:
        """Get nmChannel (Pythonic accessor)."""
        return self._nmChannel

    @nm_channel.setter
    def nm_channel(self, value: Optional[Boolean]) -> None:
        """
        Set nmChannel with validation.

        Args:
            value: The nmChannel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmChannel = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmChannel must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmChannel = value
        # valid if nmNodeIdEnabled is set to true.
        self._nmNode: Optional[Boolean] = None

    @property
    def nm_node(self) -> Optional[Boolean]:
        """Get nmNode (Pythonic accessor)."""
        return self._nmNode

    @nm_node.setter
    def nm_node(self, value: Optional[Boolean]) -> None:
        """
        Set nmNode with validation.

        Args:
            value: The nmNode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmNode = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmNode must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmNode = value
        self._nmNodeIdEnabled: Optional[Boolean] = None

    @property
    def nm_node_id_enabled(self) -> Optional[Boolean]:
        """Get nmNodeIdEnabled (Pythonic accessor)."""
        return self._nmNodeIdEnabled

    @nm_node_id_enabled.setter
    def nm_node_id_enabled(self, value: Optional[Boolean]) -> None:
        """
        Set nmNodeIdEnabled with validation.

        Args:
            value: The nmNodeIdEnabled to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmNodeIdEnabled = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmNodeIdEnabled must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmNodeIdEnabled = value
        self._nmPnc: Optional[Boolean] = None

    @property
    def nm_pnc(self) -> Optional[Boolean]:
        """Get nmPnc (Pythonic accessor)."""
        return self._nmPnc

    @nm_pnc.setter
    def nm_pnc(self, value: Optional[Boolean]) -> None:
        """
        Set nmPnc with validation.

        Args:
            value: The nmPnc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmPnc = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmPnc must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmPnc = value
        self._nmRepeatMsg: Optional[Boolean] = None

    @property
    def nm_repeat_msg(self) -> Optional[Boolean]:
        """Get nmRepeatMsg (Pythonic accessor)."""
        return self._nmRepeatMsg

    @nm_repeat_msg.setter
    def nm_repeat_msg(self, value: Optional[Boolean]) -> None:
        """
        Set nmRepeatMsg with validation.

        Args:
            value: The nmRepeatMsg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRepeatMsg = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmRepeatMsg must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmRepeatMsg = value
                # coordination cluster it belongs to.
        # The network is expected to call Nm_ regular intervals.
        self._nm: Optional[Boolean] = None

    @property
    def nm(self) -> Optional[Boolean]:
        """Get nm (Pythonic accessor)."""
        return self._nm

    @nm.setter
    def nm(self, value: Optional[Boolean]) -> None:
        """
        Set nm with validation.

        Args:
            value: The nm to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nm = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nm must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nm = value
                # UdpNm).
        # If then System.
        # pncVectorLength applies.
        # make the PNC Vector shorter (or same defined in System.
        # pncVectorLength).
        self._pncCluster: Optional[PositiveInteger] = None

    @property
    def pnc_cluster(self) -> Optional[PositiveInteger]:
        """Get pncCluster (Pythonic accessor)."""
        return self._pncCluster

    @pnc_cluster.setter
    def pnc_cluster(self, value: Optional[PositiveInteger]) -> None:
        """
        Set pncCluster with validation.

        Args:
            value: The pncCluster to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncCluster = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pncCluster must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pncCluster = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "CommunicationCluster":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "CommunicationCluster") -> NmCluster:
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

    def getNmChannel(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmChannel.

        Returns:
            The nmChannel value

        Note:
            Delegates to nm_channel property (CODING_RULE_V2_00017)
        """
        return self.nm_channel  # Delegates to property

    def setNmChannel(self, value: Boolean) -> NmCluster:
        """
        AUTOSAR-compliant setter for nmChannel with method chaining.

        Args:
            value: The nmChannel to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_channel property setter (gets validation automatically)
        """
        self.nm_channel = value  # Delegates to property setter
        return self

    def getNmNode(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmNode.

        Returns:
            The nmNode value

        Note:
            Delegates to nm_node property (CODING_RULE_V2_00017)
        """
        return self.nm_node  # Delegates to property

    def setNmNode(self, value: Boolean) -> NmCluster:
        """
        AUTOSAR-compliant setter for nmNode with method chaining.

        Args:
            value: The nmNode to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_node property setter (gets validation automatically)
        """
        self.nm_node = value  # Delegates to property setter
        return self

    def getNmNodeIdEnabled(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmNodeIdEnabled.

        Returns:
            The nmNodeIdEnabled value

        Note:
            Delegates to nm_node_id_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_node_id_enabled  # Delegates to property

    def setNmNodeIdEnabled(self, value: Boolean) -> NmCluster:
        """
        AUTOSAR-compliant setter for nmNodeIdEnabled with method chaining.

        Args:
            value: The nmNodeIdEnabled to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_node_id_enabled property setter (gets validation automatically)
        """
        self.nm_node_id_enabled = value  # Delegates to property setter
        return self

    def getNmPnc(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmPnc.

        Returns:
            The nmPnc value

        Note:
            Delegates to nm_pnc property (CODING_RULE_V2_00017)
        """
        return self.nm_pnc  # Delegates to property

    def setNmPnc(self, value: Boolean) -> NmCluster:
        """
        AUTOSAR-compliant setter for nmPnc with method chaining.

        Args:
            value: The nmPnc to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_pnc property setter (gets validation automatically)
        """
        self.nm_pnc = value  # Delegates to property setter
        return self

    def getNmRepeatMsg(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmRepeatMsg.

        Returns:
            The nmRepeatMsg value

        Note:
            Delegates to nm_repeat_msg property (CODING_RULE_V2_00017)
        """
        return self.nm_repeat_msg  # Delegates to property

    def setNmRepeatMsg(self, value: Boolean) -> NmCluster:
        """
        AUTOSAR-compliant setter for nmRepeatMsg with method chaining.

        Args:
            value: The nmRepeatMsg to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_repeat_msg property setter (gets validation automatically)
        """
        self.nm_repeat_msg = value  # Delegates to property setter
        return self

    def getNm(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nm.

        Returns:
            The nm value

        Note:
            Delegates to nm property (CODING_RULE_V2_00017)
        """
        return self.nm  # Delegates to property

    def setNm(self, value: Boolean) -> NmCluster:
        """
        AUTOSAR-compliant setter for nm with method chaining.

        Args:
            value: The nm to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm property setter (gets validation automatically)
        """
        self.nm = value  # Delegates to property setter
        return self

    def getPncCluster(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for pncCluster.

        Returns:
            The pncCluster value

        Note:
            Delegates to pnc_cluster property (CODING_RULE_V2_00017)
        """
        return self.pnc_cluster  # Delegates to property

    def setPncCluster(self, value: PositiveInteger) -> NmCluster:
        """
        AUTOSAR-compliant setter for pncCluster with method chaining.

        Args:
            value: The pncCluster to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_cluster property setter (gets validation automatically)
        """
        self.pnc_cluster = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional[CommunicationCluster]) -> NmCluster:
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

    def with_nm_channel(self, value: Optional[Boolean]) -> NmCluster:
        """
        Set nmChannel and return self for chaining.

        Args:
            value: The nmChannel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_channel("value")
        """
        self.nm_channel = value  # Use property setter (gets validation)
        return self

    def with_nm_node(self, value: Optional[Boolean]) -> NmCluster:
        """
        Set nmNode and return self for chaining.

        Args:
            value: The nmNode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_node("value")
        """
        self.nm_node = value  # Use property setter (gets validation)
        return self

    def with_nm_node_id_enabled(self, value: Optional[Boolean]) -> NmCluster:
        """
        Set nmNodeIdEnabled and return self for chaining.

        Args:
            value: The nmNodeIdEnabled to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_node_id_enabled("value")
        """
        self.nm_node_id_enabled = value  # Use property setter (gets validation)
        return self

    def with_nm_pnc(self, value: Optional[Boolean]) -> NmCluster:
        """
        Set nmPnc and return self for chaining.

        Args:
            value: The nmPnc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_pnc("value")
        """
        self.nm_pnc = value  # Use property setter (gets validation)
        return self

    def with_nm_repeat_msg(self, value: Optional[Boolean]) -> NmCluster:
        """
        Set nmRepeatMsg and return self for chaining.

        Args:
            value: The nmRepeatMsg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_repeat_msg("value")
        """
        self.nm_repeat_msg = value  # Use property setter (gets validation)
        return self

    def with_nm(self, value: Optional[Boolean]) -> NmCluster:
        """
        Set nm and return self for chaining.

        Args:
            value: The nm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm("value")
        """
        self.nm = value  # Use property setter (gets validation)
        return self

    def with_pnc_cluster(self, value: Optional[PositiveInteger]) -> NmCluster:
        """
        Set pncCluster and return self for chaining.

        Args:
            value: The pncCluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_cluster("value")
        """
        self.pnc_cluster = value  # Use property setter (gets validation)
        return self



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
        self._busDependentNmEcu: List[BusspecificNmEcu] = []

    @property
    def bus_dependent_nm_ecu(self) -> List[BusspecificNmEcu]:
        """Get busDependentNmEcu (Pythonic accessor)."""
        return self._busDependentNmEcu
        # Association to an ECUInstance in the topology.
        self._ecuInstance: Optional[EcuInstance] = None

    @property
    def ecu_instance(self) -> Optional[EcuInstance]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional[EcuInstance]) -> None:
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
        self._nmBusSynchronizationEnabled: Optional[Boolean] = None

    @property
    def nm_bus_synchronization_enabled(self) -> Optional[Boolean]:
        """Get nmBusSynchronizationEnabled (Pythonic accessor)."""
        return self._nmBusSynchronizationEnabled

    @nm_bus_synchronization_enabled.setter
    def nm_bus_synchronization_enabled(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmBusSynchronizationEnabled must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmBusSynchronizationEnabled = value
        self._nmComControlEnabled: Optional[Boolean] = None

    @property
    def nm_com_control_enabled(self) -> Optional[Boolean]:
        """Get nmComControlEnabled (Pythonic accessor)."""
        return self._nmComControlEnabled

    @nm_com_control_enabled.setter
    def nm_com_control_enabled(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmComControlEnabled must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmComControlEnabled = value
        self._nmCoordinator: Optional[NmCoordinator] = None

    @property
    def nm_coordinator(self) -> Optional[NmCoordinator]:
        """Get nmCoordinator (Pythonic accessor)."""
        return self._nmCoordinator

    @nm_coordinator.setter
    def nm_coordinator(self, value: Optional[NmCoordinator]) -> None:
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
        # seconds.
        self._nmCycletime: Optional[TimeValue] = None

    @property
    def nm_cycletime(self) -> Optional[TimeValue]:
        """Get nmCycletime (Pythonic accessor)."""
        return self._nmCycletime

    @nm_cycletime.setter
    def nm_cycletime(self, value: Optional[TimeValue]) -> None:
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
        self._nmPduRxIndicationEnabled: Optional[Boolean] = None

    @property
    def nm_pdu_rx_indication_enabled(self) -> Optional[Boolean]:
        """Get nmPduRxIndicationEnabled (Pythonic accessor)."""
        return self._nmPduRxIndicationEnabled

    @nm_pdu_rx_indication_enabled.setter
    def nm_pdu_rx_indication_enabled(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmPduRxIndicationEnabled must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmPduRxIndicationEnabled = value
        self._nmRemote: Optional[Boolean] = None

    @property
    def nm_remote(self) -> Optional[Boolean]:
        """Get nmRemote (Pythonic accessor)."""
        return self._nmRemote

    @nm_remote.setter
    def nm_remote(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmRemote must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmRemote = value
        self._nmStateChange: Optional[Boolean] = None

    @property
    def nm_state_change(self) -> Optional[Boolean]:
        """Get nmStateChange (Pythonic accessor)."""
        return self._nmStateChange

    @nm_state_change.setter
    def nm_state_change(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmStateChange must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmStateChange = value
        self._nmUserDataEnabled: Optional[Boolean] = None

    @property
    def nm_user_data_enabled(self) -> Optional[Boolean]:
        """Get nmUserDataEnabled (Pythonic accessor)."""
        return self._nmUserDataEnabled

    @nm_user_data_enabled.setter
    def nm_user_data_enabled(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmUserDataEnabled must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmUserDataEnabled = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBusDependentNmEcu(self) -> List[BusspecificNmEcu]:
        """
        AUTOSAR-compliant getter for busDependentNmEcu.

        Returns:
            The busDependentNmEcu value

        Note:
            Delegates to bus_dependent_nm_ecu property (CODING_RULE_V2_00017)
        """
        return self.bus_dependent_nm_ecu  # Delegates to property

    def getEcuInstance(self) -> EcuInstance:
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: EcuInstance) -> NmEcu:
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

    def getNmBusSynchronizationEnabled(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmBusSynchronizationEnabled.

        Returns:
            The nmBusSynchronizationEnabled value

        Note:
            Delegates to nm_bus_synchronization_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_bus_synchronization_enabled  # Delegates to property

    def setNmBusSynchronizationEnabled(self, value: Boolean) -> NmEcu:
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

    def getNmComControlEnabled(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmComControlEnabled.

        Returns:
            The nmComControlEnabled value

        Note:
            Delegates to nm_com_control_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_com_control_enabled  # Delegates to property

    def setNmComControlEnabled(self, value: Boolean) -> NmEcu:
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

    def getNmCoordinator(self) -> NmCoordinator:
        """
        AUTOSAR-compliant getter for nmCoordinator.

        Returns:
            The nmCoordinator value

        Note:
            Delegates to nm_coordinator property (CODING_RULE_V2_00017)
        """
        return self.nm_coordinator  # Delegates to property

    def setNmCoordinator(self, value: NmCoordinator) -> NmEcu:
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

    def getNmCycletime(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmCycletime.

        Returns:
            The nmCycletime value

        Note:
            Delegates to nm_cycletime property (CODING_RULE_V2_00017)
        """
        return self.nm_cycletime  # Delegates to property

    def setNmCycletime(self, value: TimeValue) -> NmEcu:
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

    def getNmPduRxIndicationEnabled(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmPduRxIndicationEnabled.

        Returns:
            The nmPduRxIndicationEnabled value

        Note:
            Delegates to nm_pdu_rx_indication_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_pdu_rx_indication_enabled  # Delegates to property

    def setNmPduRxIndicationEnabled(self, value: Boolean) -> NmEcu:
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

    def getNmRemote(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmRemote.

        Returns:
            The nmRemote value

        Note:
            Delegates to nm_remote property (CODING_RULE_V2_00017)
        """
        return self.nm_remote  # Delegates to property

    def setNmRemote(self, value: Boolean) -> NmEcu:
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

    def getNmStateChange(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmStateChange.

        Returns:
            The nmStateChange value

        Note:
            Delegates to nm_state_change property (CODING_RULE_V2_00017)
        """
        return self.nm_state_change  # Delegates to property

    def setNmStateChange(self, value: Boolean) -> NmEcu:
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

    def getNmUserDataEnabled(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmUserDataEnabled.

        Returns:
            The nmUserDataEnabled value

        Note:
            Delegates to nm_user_data_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_user_data_enabled  # Delegates to property

    def setNmUserDataEnabled(self, value: Boolean) -> NmEcu:
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

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> NmEcu:
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

    def with_nm_bus_synchronization_enabled(self, value: Optional[Boolean]) -> NmEcu:
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

    def with_nm_com_control_enabled(self, value: Optional[Boolean]) -> NmEcu:
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

    def with_nm_coordinator(self, value: Optional[NmCoordinator]) -> NmEcu:
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

    def with_nm_cycletime(self, value: Optional[TimeValue]) -> NmEcu:
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

    def with_nm_pdu_rx_indication_enabled(self, value: Optional[Boolean]) -> NmEcu:
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

    def with_nm_remote(self, value: Optional[Boolean]) -> NmEcu:
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

    def with_nm_state_change(self, value: Optional[Boolean]) -> NmEcu:
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

    def with_nm_user_data_enabled(self, value: Optional[Boolean]) -> NmEcu:
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



class BusspecificNmEcu(ARObject, ABC):
    """
    Busspecific NmEcu attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::BusspecificNmEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 675, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BusspecificNmEcu:
            raise TypeError("BusspecificNmEcu is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class NmCoordinator(ARObject):
    """
    A NM coordinator is an ECU, which is connected to at least two busses, and
    where the requirement exists that shutdown of NM of at least two of these
    busses (also referred to as coordinated busses) has to be performed
    synchronously.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::NmCoordinator

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 675, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Identification of the NMCoordinator.
        self._index: Optional[Integer] = None

    @property
    def index(self) -> Optional[Integer]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional[Integer]) -> None:
        """
        Set index with validation.

        Args:
            value: The index to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._index = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"index must be Integer or int or None, got {type(value).__name__}"
            )
        self._index = value
        self._nmCoordSync: Optional[Boolean] = None

    @property
    def nm_coord_sync(self) -> Optional[Boolean]:
        """Get nmCoordSync (Pythonic accessor)."""
        return self._nmCoordSync

    @nm_coord_sync.setter
    def nm_coord_sync(self, value: Optional[Boolean]) -> None:
        """
        Set nmCoordSync with validation.

        Args:
            value: The nmCoordSync to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCoordSync = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmCoordSync must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmCoordSync = value
        # coordinated NM-Cluster.
        self._nmGlobal: Optional[TimeValue] = None

    @property
    def nm_global(self) -> Optional[TimeValue]:
        """Get nmGlobal (Pythonic accessor)."""
        return self._nmGlobal

    @nm_global.setter
    def nm_global(self, value: Optional[TimeValue]) -> None:
        """
        Set nmGlobal with validation.

        Args:
            value: The nmGlobal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmGlobal = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmGlobal must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmGlobal = value
        self._nmNode: List[NmNode] = []

    @property
    def nm_node(self) -> List[NmNode]:
        """Get nmNode (Pythonic accessor)."""
        return self._nmNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIndex(self) -> Integer:
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: Integer) -> NmCoordinator:
        """
        AUTOSAR-compliant setter for index with method chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Note:
            Delegates to index property setter (gets validation automatically)
        """
        self.index = value  # Delegates to property setter
        return self

    def getNmCoordSync(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmCoordSync.

        Returns:
            The nmCoordSync value

        Note:
            Delegates to nm_coord_sync property (CODING_RULE_V2_00017)
        """
        return self.nm_coord_sync  # Delegates to property

    def setNmCoordSync(self, value: Boolean) -> NmCoordinator:
        """
        AUTOSAR-compliant setter for nmCoordSync with method chaining.

        Args:
            value: The nmCoordSync to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_coord_sync property setter (gets validation automatically)
        """
        self.nm_coord_sync = value  # Delegates to property setter
        return self

    def getNmGlobal(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmGlobal.

        Returns:
            The nmGlobal value

        Note:
            Delegates to nm_global property (CODING_RULE_V2_00017)
        """
        return self.nm_global  # Delegates to property

    def setNmGlobal(self, value: TimeValue) -> NmCoordinator:
        """
        AUTOSAR-compliant setter for nmGlobal with method chaining.

        Args:
            value: The nmGlobal to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_global property setter (gets validation automatically)
        """
        self.nm_global = value  # Delegates to property setter
        return self

    def getNmNode(self) -> List[NmNode]:
        """
        AUTOSAR-compliant getter for nmNode.

        Returns:
            The nmNode value

        Note:
            Delegates to nm_node property (CODING_RULE_V2_00017)
        """
        return self.nm_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_index(self, value: Optional[Integer]) -> NmCoordinator:
        """
        Set index and return self for chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index("value")
        """
        self.index = value  # Use property setter (gets validation)
        return self

    def with_nm_coord_sync(self, value: Optional[Boolean]) -> NmCoordinator:
        """
        Set nmCoordSync and return self for chaining.

        Args:
            value: The nmCoordSync to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_coord_sync("value")
        """
        self.nm_coord_sync = value  # Use property setter (gets validation)
        return self

    def with_nm_global(self, value: Optional[TimeValue]) -> NmCoordinator:
        """
        Set nmGlobal and return self for chaining.

        Args:
            value: The nmGlobal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_global("value")
        """
        self.nm_global = value  # Use property setter (gets validation)
        return self



class NmNode(Identifiable, ABC):
    """
    The linking of NmEcus to NmClusters is realized via the NmNodes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::NmNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 675, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is NmNode:
            raise TypeError("NmNode is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to an CommunicationController in the description.
        self._controller: Optional[Communication] = None

    @property
    def controller(self) -> Optional[Communication]:
        """Get controller (Pythonic accessor)."""
        return self._controller

    @controller.setter
    def controller(self, value: Optional[Communication]) -> None:
        """
        Set controller with validation.

        Args:
            value: The controller to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._controller = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"controller must be Communication or None, got {type(value).__name__}"
            )
        self._controller = value
        self._nmCoordCluster: Optional[PositiveInteger] = None

    @property
    def nm_coord_cluster(self) -> Optional[PositiveInteger]:
        """Get nmCoordCluster (Pythonic accessor)."""
        return self._nmCoordCluster

    @nm_coord_cluster.setter
    def nm_coord_cluster(self, value: Optional[PositiveInteger]) -> None:
        """
        Set nmCoordCluster with validation.

        Args:
            value: The nmCoordCluster to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCoordCluster = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"nmCoordCluster must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._nmCoordCluster = value
                # channel.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._nmCoordinator: Optional[NmCoordinatorRole] = None

    @property
    def nm_coordinator(self) -> Optional[NmCoordinatorRole]:
        """Get nmCoordinator (Pythonic accessor)."""
        return self._nmCoordinator

    @nm_coordinator.setter
    def nm_coordinator(self, value: Optional[NmCoordinatorRole]) -> None:
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

        if not isinstance(value, NmCoordinatorRole):
            raise TypeError(
                f"nmCoordinator must be NmCoordinatorRole or None, got {type(value).__name__}"
            )
        self._nmCoordinator = value
        # is referenced by the Nm be contained in the EcuInstance that is the NmEcu).
        self._nmIfEcu: Optional[NmEcu] = None

    @property
    def nm_if_ecu(self) -> Optional[NmEcu]:
        """Get nmIfEcu (Pythonic accessor)."""
        return self._nmIfEcu

    @nm_if_ecu.setter
    def nm_if_ecu(self, value: Optional[NmEcu]) -> None:
        """
        Set nmIfEcu with validation.

        Args:
            value: The nmIfEcu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmIfEcu = None
            return

        if not isinstance(value, NmEcu):
            raise TypeError(
                f"nmIfEcu must be NmEcu or None, got {type(value).__name__}"
            )
        self._nmIfEcu = value
        # Shall be unique in the.
        self._nmNodeId: Optional[Integer] = None

    @property
    def nm_node_id(self) -> Optional[Integer]:
        """Get nmNodeId (Pythonic accessor)."""
        return self._nmNodeId

    @nm_node_id.setter
    def nm_node_id(self, value: Optional[Integer]) -> None:
        """
        Set nmNodeId with validation.

        Args:
            value: The nmNodeId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmNodeId = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"nmNodeId must be Integer or int or None, got {type(value).__name__}"
            )
        self._nmNodeId = value
        # The passive mode configurable per channel.
        self._nmPassive: Optional[Boolean] = None

    @property
    def nm_passive(self) -> Optional[Boolean]:
        """Get nmPassive (Pythonic accessor)."""
        return self._nmPassive

    @nm_passive.setter
    def nm_passive(self, value: Optional[Boolean]) -> None:
        """
        Set nmPassive with validation.

        Args:
            value: The nmPassive to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmPassive = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmPassive must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmPassive = value
        self._rxNmPdu: List[NmPdu] = []

    @property
    def rx_nm_pdu(self) -> List[NmPdu]:
        """Get rxNmPdu (Pythonic accessor)."""
        return self._rxNmPdu
        # transmit NM Pdu.
        self._txNmPdu: List[NmPdu] = []

    @property
    def tx_nm_pdu(self) -> List[NmPdu]:
        """Get txNmPdu (Pythonic accessor)."""
        return self._txNmPdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getController(self) -> Communication:
        """
        AUTOSAR-compliant getter for controller.

        Returns:
            The controller value

        Note:
            Delegates to controller property (CODING_RULE_V2_00017)
        """
        return self.controller  # Delegates to property

    def setController(self, value: Communication) -> NmNode:
        """
        AUTOSAR-compliant setter for controller with method chaining.

        Args:
            value: The controller to set

        Returns:
            self for method chaining

        Note:
            Delegates to controller property setter (gets validation automatically)
        """
        self.controller = value  # Delegates to property setter
        return self

    def getNmCoordCluster(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for nmCoordCluster.

        Returns:
            The nmCoordCluster value

        Note:
            Delegates to nm_coord_cluster property (CODING_RULE_V2_00017)
        """
        return self.nm_coord_cluster  # Delegates to property

    def setNmCoordCluster(self, value: PositiveInteger) -> NmNode:
        """
        AUTOSAR-compliant setter for nmCoordCluster with method chaining.

        Args:
            value: The nmCoordCluster to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_coord_cluster property setter (gets validation automatically)
        """
        self.nm_coord_cluster = value  # Delegates to property setter
        return self

    def getNmCoordinator(self) -> "NmCoordinatorRole":
        """
        AUTOSAR-compliant getter for nmCoordinator.

        Returns:
            The nmCoordinator value

        Note:
            Delegates to nm_coordinator property (CODING_RULE_V2_00017)
        """
        return self.nm_coordinator  # Delegates to property

    def setNmCoordinator(self, value: "NmCoordinatorRole") -> NmNode:
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

    def getNmIfEcu(self) -> NmEcu:
        """
        AUTOSAR-compliant getter for nmIfEcu.

        Returns:
            The nmIfEcu value

        Note:
            Delegates to nm_if_ecu property (CODING_RULE_V2_00017)
        """
        return self.nm_if_ecu  # Delegates to property

    def setNmIfEcu(self, value: NmEcu) -> NmNode:
        """
        AUTOSAR-compliant setter for nmIfEcu with method chaining.

        Args:
            value: The nmIfEcu to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_if_ecu property setter (gets validation automatically)
        """
        self.nm_if_ecu = value  # Delegates to property setter
        return self

    def getNmNodeId(self) -> Integer:
        """
        AUTOSAR-compliant getter for nmNodeId.

        Returns:
            The nmNodeId value

        Note:
            Delegates to nm_node_id property (CODING_RULE_V2_00017)
        """
        return self.nm_node_id  # Delegates to property

    def setNmNodeId(self, value: Integer) -> NmNode:
        """
        AUTOSAR-compliant setter for nmNodeId with method chaining.

        Args:
            value: The nmNodeId to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_node_id property setter (gets validation automatically)
        """
        self.nm_node_id = value  # Delegates to property setter
        return self

    def getNmPassive(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmPassive.

        Returns:
            The nmPassive value

        Note:
            Delegates to nm_passive property (CODING_RULE_V2_00017)
        """
        return self.nm_passive  # Delegates to property

    def setNmPassive(self, value: Boolean) -> NmNode:
        """
        AUTOSAR-compliant setter for nmPassive with method chaining.

        Args:
            value: The nmPassive to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_passive property setter (gets validation automatically)
        """
        self.nm_passive = value  # Delegates to property setter
        return self

    def getRxNmPdu(self) -> List[NmPdu]:
        """
        AUTOSAR-compliant getter for rxNmPdu.

        Returns:
            The rxNmPdu value

        Note:
            Delegates to rx_nm_pdu property (CODING_RULE_V2_00017)
        """
        return self.rx_nm_pdu  # Delegates to property

    def getTxNmPdu(self) -> List[NmPdu]:
        """
        AUTOSAR-compliant getter for txNmPdu.

        Returns:
            The txNmPdu value

        Note:
            Delegates to tx_nm_pdu property (CODING_RULE_V2_00017)
        """
        return self.tx_nm_pdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_controller(self, value: Optional[Communication]) -> NmNode:
        """
        Set controller and return self for chaining.

        Args:
            value: The controller to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_controller("value")
        """
        self.controller = value  # Use property setter (gets validation)
        return self

    def with_nm_coord_cluster(self, value: Optional[PositiveInteger]) -> NmNode:
        """
        Set nmCoordCluster and return self for chaining.

        Args:
            value: The nmCoordCluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_coord_cluster("value")
        """
        self.nm_coord_cluster = value  # Use property setter (gets validation)
        return self

    def with_nm_coordinator(self, value: Optional[NmCoordinatorRole]) -> NmNode:
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

    def with_nm_if_ecu(self, value: Optional[NmEcu]) -> NmNode:
        """
        Set nmIfEcu and return self for chaining.

        Args:
            value: The nmIfEcu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_if_ecu("value")
        """
        self.nm_if_ecu = value  # Use property setter (gets validation)
        return self

    def with_nm_node_id(self, value: Optional[Integer]) -> NmNode:
        """
        Set nmNodeId and return self for chaining.

        Args:
            value: The nmNodeId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_node_id("value")
        """
        self.nm_node_id = value  # Use property setter (gets validation)
        return self

    def with_nm_passive(self, value: Optional[Boolean]) -> NmNode:
        """
        Set nmPassive and return self for chaining.

        Args:
            value: The nmPassive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_passive("value")
        """
        self.nm_passive = value  # Use property setter (gets validation)
        return self



class NmClusterCoupling(ARObject, ABC):
    """
    Attributes that are valid for each of the referenced (coupled) clusters.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::NmClusterCoupling

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 676, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is NmClusterCoupling:
            raise TypeError("NmClusterCoupling is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class J1939NodeName(ARObject):
    """
    This element contains attributes to configure the J1939NmNode NAME.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::J1939NodeName

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 691, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Arbitrary Address Capable field of the NAME of this node.
        self._arbitrary: Optional[Boolean] = None

    @property
    def arbitrary(self) -> Optional[Boolean]:
        """Get arbitrary (Pythonic accessor)."""
        return self._arbitrary

    @arbitrary.setter
    def arbitrary(self, value: Optional[Boolean]) -> None:
        """
        Set arbitrary with validation.

        Args:
            value: The arbitrary to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arbitrary = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"arbitrary must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._arbitrary = value
        self._ecuInstance: Optional[Integer] = None

    @property
    def ecu_instance(self) -> Optional[Integer]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"ecuInstance must be Integer or int or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
        self._function: Optional[Integer] = None

    @property
    def function(self) -> Optional[Integer]:
        """Get function (Pythonic accessor)."""
        return self._function

    @function.setter
    def function(self, value: Optional[Integer]) -> None:
        """
        Set function with validation.

        Args:
            value: The function to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._function = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"function must be Integer or int or None, got {type(value).__name__}"
            )
        self._function = value
        self._functionInstance: Optional[Integer] = None

    @property
    def function_instance(self) -> Optional[Integer]:
        """Get functionInstance (Pythonic accessor)."""
        return self._functionInstance

    @function_instance.setter
    def function_instance(self, value: Optional[Integer]) -> None:
        """
        Set functionInstance with validation.

        Args:
            value: The functionInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionInstance = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"functionInstance must be Integer or int or None, got {type(value).__name__}"
            )
        self._functionInstance = value
        self._identitiyNumber: Optional[Integer] = None

    @property
    def identitiy_number(self) -> Optional[Integer]:
        """Get identitiyNumber (Pythonic accessor)."""
        return self._identitiyNumber

    @identitiy_number.setter
    def identitiy_number(self, value: Optional[Integer]) -> None:
        """
        Set identitiyNumber with validation.

        Args:
            value: The identitiyNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._identitiyNumber = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"identitiyNumber must be Integer or int or None, got {type(value).__name__}"
            )
        self._identitiyNumber = value
        self._industryGroup: Optional[Integer] = None

    @property
    def industry_group(self) -> Optional[Integer]:
        """Get industryGroup (Pythonic accessor)."""
        return self._industryGroup

    @industry_group.setter
    def industry_group(self, value: Optional[Integer]) -> None:
        """
        Set industryGroup with validation.

        Args:
            value: The industryGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._industryGroup = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"industryGroup must be Integer or int or None, got {type(value).__name__}"
            )
        self._industryGroup = value
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._manufacturerCode: Optional[Integer] = None

    @property
    def manufacturer_code(self) -> Optional[Integer]:
        """Get manufacturerCode (Pythonic accessor)."""
        return self._manufacturerCode

    @manufacturer_code.setter
    def manufacturer_code(self, value: Optional[Integer]) -> None:
        """
        Set manufacturerCode with validation.

        Args:
            value: The manufacturerCode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._manufacturerCode = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"manufacturerCode must be Integer or int or None, got {type(value).__name__}"
            )
        self._manufacturerCode = value
        self._vehicleSystem: Optional[Integer] = None

    @property
    def vehicle_system(self) -> Optional[Integer]:
        """Get vehicleSystem (Pythonic accessor)."""
        return self._vehicleSystem

    @vehicle_system.setter
    def vehicle_system(self, value: Optional[Integer]) -> None:
        """
        Set vehicleSystem with validation.

        Args:
            value: The vehicleSystem to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vehicleSystem = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"vehicleSystem must be Integer or int or None, got {type(value).__name__}"
            )
        self._vehicleSystem = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArbitrary(self) -> Boolean:
        """
        AUTOSAR-compliant getter for arbitrary.

        Returns:
            The arbitrary value

        Note:
            Delegates to arbitrary property (CODING_RULE_V2_00017)
        """
        return self.arbitrary  # Delegates to property

    def setArbitrary(self, value: Boolean) -> J1939NodeName:
        """
        AUTOSAR-compliant setter for arbitrary with method chaining.

        Args:
            value: The arbitrary to set

        Returns:
            self for method chaining

        Note:
            Delegates to arbitrary property setter (gets validation automatically)
        """
        self.arbitrary = value  # Delegates to property setter
        return self

    def getEcuInstance(self) -> Integer:
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: Integer) -> J1939NodeName:
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

    def getFunction(self) -> Integer:
        """
        AUTOSAR-compliant getter for function.

        Returns:
            The function value

        Note:
            Delegates to function property (CODING_RULE_V2_00017)
        """
        return self.function  # Delegates to property

    def setFunction(self, value: Integer) -> J1939NodeName:
        """
        AUTOSAR-compliant setter for function with method chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Note:
            Delegates to function property setter (gets validation automatically)
        """
        self.function = value  # Delegates to property setter
        return self

    def getFunctionInstance(self) -> Integer:
        """
        AUTOSAR-compliant getter for functionInstance.

        Returns:
            The functionInstance value

        Note:
            Delegates to function_instance property (CODING_RULE_V2_00017)
        """
        return self.function_instance  # Delegates to property

    def setFunctionInstance(self, value: Integer) -> J1939NodeName:
        """
        AUTOSAR-compliant setter for functionInstance with method chaining.

        Args:
            value: The functionInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to function_instance property setter (gets validation automatically)
        """
        self.function_instance = value  # Delegates to property setter
        return self

    def getIdentitiyNumber(self) -> Integer:
        """
        AUTOSAR-compliant getter for identitiyNumber.

        Returns:
            The identitiyNumber value

        Note:
            Delegates to identitiy_number property (CODING_RULE_V2_00017)
        """
        return self.identitiy_number  # Delegates to property

    def setIdentitiyNumber(self, value: Integer) -> J1939NodeName:
        """
        AUTOSAR-compliant setter for identitiyNumber with method chaining.

        Args:
            value: The identitiyNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to identitiy_number property setter (gets validation automatically)
        """
        self.identitiy_number = value  # Delegates to property setter
        return self

    def getIndustryGroup(self) -> Integer:
        """
        AUTOSAR-compliant getter for industryGroup.

        Returns:
            The industryGroup value

        Note:
            Delegates to industry_group property (CODING_RULE_V2_00017)
        """
        return self.industry_group  # Delegates to property

    def setIndustryGroup(self, value: Integer) -> J1939NodeName:
        """
        AUTOSAR-compliant setter for industryGroup with method chaining.

        Args:
            value: The industryGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to industry_group property setter (gets validation automatically)
        """
        self.industry_group = value  # Delegates to property setter
        return self

    def getManufacturerCode(self) -> Integer:
        """
        AUTOSAR-compliant getter for manufacturerCode.

        Returns:
            The manufacturerCode value

        Note:
            Delegates to manufacturer_code property (CODING_RULE_V2_00017)
        """
        return self.manufacturer_code  # Delegates to property

    def setManufacturerCode(self, value: Integer) -> J1939NodeName:
        """
        AUTOSAR-compliant setter for manufacturerCode with method chaining.

        Args:
            value: The manufacturerCode to set

        Returns:
            self for method chaining

        Note:
            Delegates to manufacturer_code property setter (gets validation automatically)
        """
        self.manufacturer_code = value  # Delegates to property setter
        return self

    def getVehicleSystem(self) -> Integer:
        """
        AUTOSAR-compliant getter for vehicleSystem.

        Returns:
            The vehicleSystem value

        Note:
            Delegates to vehicle_system property (CODING_RULE_V2_00017)
        """
        return self.vehicle_system  # Delegates to property

    def setVehicleSystem(self, value: Integer) -> J1939NodeName:
        """
        AUTOSAR-compliant setter for vehicleSystem with method chaining.

        Args:
            value: The vehicleSystem to set

        Returns:
            self for method chaining

        Note:
            Delegates to vehicle_system property setter (gets validation automatically)
        """
        self.vehicle_system = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_arbitrary(self, value: Optional[Boolean]) -> J1939NodeName:
        """
        Set arbitrary and return self for chaining.

        Args:
            value: The arbitrary to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_arbitrary("value")
        """
        self.arbitrary = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional[Integer]) -> J1939NodeName:
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

    def with_function(self, value: Optional[Integer]) -> J1939NodeName:
        """
        Set function and return self for chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function("value")
        """
        self.function = value  # Use property setter (gets validation)
        return self

    def with_function_instance(self, value: Optional[Integer]) -> J1939NodeName:
        """
        Set functionInstance and return self for chaining.

        Args:
            value: The functionInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function_instance("value")
        """
        self.function_instance = value  # Use property setter (gets validation)
        return self

    def with_identitiy_number(self, value: Optional[Integer]) -> J1939NodeName:
        """
        Set identitiyNumber and return self for chaining.

        Args:
            value: The identitiyNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_identitiy_number("value")
        """
        self.identitiy_number = value  # Use property setter (gets validation)
        return self

    def with_industry_group(self, value: Optional[Integer]) -> J1939NodeName:
        """
        Set industryGroup and return self for chaining.

        Args:
            value: The industryGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_industry_group("value")
        """
        self.industry_group = value  # Use property setter (gets validation)
        return self

    def with_manufacturer_code(self, value: Optional[Integer]) -> J1939NodeName:
        """
        Set manufacturerCode and return self for chaining.

        Args:
            value: The manufacturerCode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_manufacturer_code("value")
        """
        self.manufacturer_code = value  # Use property setter (gets validation)
        return self

    def with_vehicle_system(self, value: Optional[Integer]) -> J1939NodeName:
        """
        Set vehicleSystem and return self for chaining.

        Args:
            value: The vehicleSystem to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vehicle_system("value")
        """
        self.vehicle_system = value  # Use property setter (gets validation)
        return self



class FlexrayNmCluster(NmCluster):
    """
    FlexRay specific NM cluster attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::FlexrayNmCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 678, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If set to true this attribute enables the support of CarWake bit evaluation
        # in received NmPdus.
        self._nmCarWakeUp: Optional[Boolean] = None

    @property
    def nm_car_wake_up(self) -> Optional[Boolean]:
        """Get nmCarWakeUp (Pythonic accessor)."""
        return self._nmCarWakeUp

    @nm_car_wake_up.setter
    def nm_car_wake_up(self, value: Optional[Boolean]) -> None:
        """
        Set nmCarWakeUp with validation.

        Args:
            value: The nmCarWakeUp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCarWakeUp = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmCarWakeUp must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmCarWakeUp = value
        # Nm Ecus of.
        self._nmDataCycle: Optional[Integer] = None

    @property
    def nm_data_cycle(self) -> Optional[Integer]:
        """Get nmDataCycle (Pythonic accessor)."""
        return self._nmDataCycle

    @nm_data_cycle.setter
    def nm_data_cycle(self, value: Optional[Integer]) -> None:
        """
        Set nmDataCycle with validation.

        Args:
            value: The nmDataCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmDataCycle = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"nmDataCycle must be Integer or int or None, got {type(value).__name__}"
            )
        self._nmDataCycle = value
        self._nmMain: Optional[TimeValue] = None

    @property
    def nm_main(self) -> Optional[TimeValue]:
        """Get nmMain (Pythonic accessor)."""
        return self._nmMain

    @nm_main.setter
    def nm_main(self, value: Optional[TimeValue]) -> None:
        """
        Set nmMain with validation.

        Args:
            value: The nmMain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMain = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMain must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMain = value
        # It the time how long it shall take to recognize that all nodes are ready to
                # sleep.
        self._nmRemote: Optional[TimeValue] = None

    @property
    def nm_remote(self) -> Optional[TimeValue]:
        """Get nmRemote (Pythonic accessor)."""
        return self._nmRemote

    @nm_remote.setter
    def nm_remote(self, value: Optional[TimeValue]) -> None:
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

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmRemote must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmRemote = value
        # Defines time how long the NM shall stay in the Repeat.
        self._nmRepeat: Optional[TimeValue] = None

    @property
    def nm_repeat(self) -> Optional[TimeValue]:
        """Get nmRepeat (Pythonic accessor)."""
        return self._nmRepeat

    @nm_repeat.setter
    def nm_repeat(self, value: Optional[TimeValue]) -> None:
        """
        Set nmRepeat with validation.

        Args:
            value: The nmRepeat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRepeat = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmRepeat must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmRepeat = value
                # vote Pdus of all Flex of this FlexRayNmCluster.
        # This value shall integral multiple of nmVotingCycle.
        self._nmRepetition: Optional[Integer] = None

    @property
    def nm_repetition(self) -> Optional[Integer]:
        """Get nmRepetition (Pythonic accessor)."""
        return self._nmRepetition

    @nm_repetition.setter
    def nm_repetition(self, value: Optional[Integer]) -> None:
        """
        Set nmRepetition with validation.

        Args:
            value: The nmRepetition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRepetition = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"nmRepetition must be Integer or int or None, got {type(value).__name__}"
            )
        self._nmRepetition = value
        # FlexRay NmEcus of.
        self._nmVotingCycle: Optional[Integer] = None

    @property
    def nm_voting_cycle(self) -> Optional[Integer]:
        """Get nmVotingCycle (Pythonic accessor)."""
        return self._nmVotingCycle

    @nm_voting_cycle.setter
    def nm_voting_cycle(self, value: Optional[Integer]) -> None:
        """
        Set nmVotingCycle with validation.

        Args:
            value: The nmVotingCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmVotingCycle = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"nmVotingCycle must be Integer or int or None, got {type(value).__name__}"
            )
        self._nmVotingCycle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmCarWakeUp(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmCarWakeUp.

        Returns:
            The nmCarWakeUp value

        Note:
            Delegates to nm_car_wake_up property (CODING_RULE_V2_00017)
        """
        return self.nm_car_wake_up  # Delegates to property

    def setNmCarWakeUp(self, value: Boolean) -> FlexrayNmCluster:
        """
        AUTOSAR-compliant setter for nmCarWakeUp with method chaining.

        Args:
            value: The nmCarWakeUp to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_car_wake_up property setter (gets validation automatically)
        """
        self.nm_car_wake_up = value  # Delegates to property setter
        return self

    def getNmDataCycle(self) -> Integer:
        """
        AUTOSAR-compliant getter for nmDataCycle.

        Returns:
            The nmDataCycle value

        Note:
            Delegates to nm_data_cycle property (CODING_RULE_V2_00017)
        """
        return self.nm_data_cycle  # Delegates to property

    def setNmDataCycle(self, value: Integer) -> FlexrayNmCluster:
        """
        AUTOSAR-compliant setter for nmDataCycle with method chaining.

        Args:
            value: The nmDataCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_data_cycle property setter (gets validation automatically)
        """
        self.nm_data_cycle = value  # Delegates to property setter
        return self

    def getNmMain(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmMain.

        Returns:
            The nmMain value

        Note:
            Delegates to nm_main property (CODING_RULE_V2_00017)
        """
        return self.nm_main  # Delegates to property

    def setNmMain(self, value: TimeValue) -> FlexrayNmCluster:
        """
        AUTOSAR-compliant setter for nmMain with method chaining.

        Args:
            value: The nmMain to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_main property setter (gets validation automatically)
        """
        self.nm_main = value  # Delegates to property setter
        return self

    def getNmRemote(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmRemote.

        Returns:
            The nmRemote value

        Note:
            Delegates to nm_remote property (CODING_RULE_V2_00017)
        """
        return self.nm_remote  # Delegates to property

    def setNmRemote(self, value: TimeValue) -> FlexrayNmCluster:
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

    def getNmRepeat(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmRepeat.

        Returns:
            The nmRepeat value

        Note:
            Delegates to nm_repeat property (CODING_RULE_V2_00017)
        """
        return self.nm_repeat  # Delegates to property

    def setNmRepeat(self, value: TimeValue) -> FlexrayNmCluster:
        """
        AUTOSAR-compliant setter for nmRepeat with method chaining.

        Args:
            value: The nmRepeat to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_repeat property setter (gets validation automatically)
        """
        self.nm_repeat = value  # Delegates to property setter
        return self

    def getNmRepetition(self) -> Integer:
        """
        AUTOSAR-compliant getter for nmRepetition.

        Returns:
            The nmRepetition value

        Note:
            Delegates to nm_repetition property (CODING_RULE_V2_00017)
        """
        return self.nm_repetition  # Delegates to property

    def setNmRepetition(self, value: Integer) -> FlexrayNmCluster:
        """
        AUTOSAR-compliant setter for nmRepetition with method chaining.

        Args:
            value: The nmRepetition to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_repetition property setter (gets validation automatically)
        """
        self.nm_repetition = value  # Delegates to property setter
        return self

    def getNmVotingCycle(self) -> Integer:
        """
        AUTOSAR-compliant getter for nmVotingCycle.

        Returns:
            The nmVotingCycle value

        Note:
            Delegates to nm_voting_cycle property (CODING_RULE_V2_00017)
        """
        return self.nm_voting_cycle  # Delegates to property

    def setNmVotingCycle(self, value: Integer) -> FlexrayNmCluster:
        """
        AUTOSAR-compliant setter for nmVotingCycle with method chaining.

        Args:
            value: The nmVotingCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_voting_cycle property setter (gets validation automatically)
        """
        self.nm_voting_cycle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_car_wake_up(self, value: Optional[Boolean]) -> FlexrayNmCluster:
        """
        Set nmCarWakeUp and return self for chaining.

        Args:
            value: The nmCarWakeUp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_car_wake_up("value")
        """
        self.nm_car_wake_up = value  # Use property setter (gets validation)
        return self

    def with_nm_data_cycle(self, value: Optional[Integer]) -> FlexrayNmCluster:
        """
        Set nmDataCycle and return self for chaining.

        Args:
            value: The nmDataCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_data_cycle("value")
        """
        self.nm_data_cycle = value  # Use property setter (gets validation)
        return self

    def with_nm_main(self, value: Optional[TimeValue]) -> FlexrayNmCluster:
        """
        Set nmMain and return self for chaining.

        Args:
            value: The nmMain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_main("value")
        """
        self.nm_main = value  # Use property setter (gets validation)
        return self

    def with_nm_remote(self, value: Optional[TimeValue]) -> FlexrayNmCluster:
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

    def with_nm_repeat(self, value: Optional[TimeValue]) -> FlexrayNmCluster:
        """
        Set nmRepeat and return self for chaining.

        Args:
            value: The nmRepeat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_repeat("value")
        """
        self.nm_repeat = value  # Use property setter (gets validation)
        return self

    def with_nm_repetition(self, value: Optional[Integer]) -> FlexrayNmCluster:
        """
        Set nmRepetition and return self for chaining.

        Args:
            value: The nmRepetition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_repetition("value")
        """
        self.nm_repetition = value  # Use property setter (gets validation)
        return self

    def with_nm_voting_cycle(self, value: Optional[Integer]) -> FlexrayNmCluster:
        """
        Set nmVotingCycle and return self for chaining.

        Args:
            value: The nmVotingCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_voting_cycle("value")
        """
        self.nm_voting_cycle = value  # Use property setter (gets validation)
        return self



class CanNmCluster(NmCluster):
    """
    Can specific NmCluster attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::CanNmCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 682, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # It determines if bus load reduction for the respective Can channel is active
        # or not.
        self._nmBusload: Optional[Boolean] = None

    @property
    def nm_busload(self) -> Optional[Boolean]:
        """Get nmBusload (Pythonic accessor)."""
        return self._nmBusload

    @nm_busload.setter
    def nm_busload(self, value: Optional[Boolean]) -> None:
        """
        Set nmBusload with validation.

        Args:
            value: The nmBusload to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmBusload = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmBusload must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmBusload = value
        self._nmCarWakeUp: Optional[PositiveInteger] = None

    @property
    def nm_car_wake_up(self) -> Optional[PositiveInteger]:
        """Get nmCarWakeUp (Pythonic accessor)."""
        return self._nmCarWakeUp

    @nm_car_wake_up.setter
    def nm_car_wake_up(self, value: Optional[PositiveInteger]) -> None:
        """
        Set nmCarWakeUp with validation.

        Args:
            value: The nmCarWakeUp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCarWakeUp = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"nmCarWakeUp must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._nmCarWakeUp = value
        self._nmCarWakeUpFilterNodeId: Optional[PositiveInteger] = None

    @property
    def nm_car_wake_up_filter_node_id(self) -> Optional[PositiveInteger]:
        """Get nmCarWakeUpFilterNodeId (Pythonic accessor)."""
        return self._nmCarWakeUpFilterNodeId

    @nm_car_wake_up_filter_node_id.setter
    def nm_car_wake_up_filter_node_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set nmCarWakeUpFilterNodeId with validation.

        Args:
            value: The nmCarWakeUpFilterNodeId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCarWakeUpFilterNodeId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"nmCarWakeUpFilterNodeId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._nmCarWakeUpFilterNodeId = value
        # If this attribute is not configured, the Vector is not used.
        self._nmCbvPosition: Optional[Integer] = None

    @property
    def nm_cbv_position(self) -> Optional[Integer]:
        """Get nmCbvPosition (Pythonic accessor)."""
        return self._nmCbvPosition

    @nm_cbv_position.setter
    def nm_cbv_position(self, value: Optional[Integer]) -> None:
        """
        Set nmCbvPosition with validation.

        Args:
            value: The nmCbvPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCbvPosition = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"nmCbvPosition must be Integer or int or None, got {type(value).__name__}"
            )
        self._nmCbvPosition = value
                # immediate NmPdus transmitted.
        # The cycle time of immediate NmPdus is nmImmediateNmCycleTime.
        self._nmImmediate: Optional[PositiveInteger] = None

    @property
    def nm_immediate(self) -> Optional[PositiveInteger]:
        """Get nmImmediate (Pythonic accessor)."""
        return self._nmImmediate

    @nm_immediate.setter
    def nm_immediate(self, value: Optional[PositiveInteger]) -> None:
        """
        Set nmImmediate with validation.

        Args:
            value: The nmImmediate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmImmediate = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"nmImmediate must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._nmImmediate = value
        # It determines how long NM shall wait with notification of transmission
                # failure errors occur on the bus.
        self._nmMessage: Optional[TimeValue] = None

    @property
    def nm_message(self) -> Optional[TimeValue]:
        """Get nmMessage (Pythonic accessor)."""
        return self._nmMessage

    @nm_message.setter
    def nm_message(self, value: Optional[TimeValue]) -> None:
        """
        Set nmMessage with validation.

        Args:
            value: The nmMessage to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMessage = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMessage must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMessage = value
        # It determines the periodic in the periodic transmission mode with bus load is
                # the basis for transmit scheduling in the mode without bus load reduction.
        self._nmMsgCycle: Optional[TimeValue] = None

    @property
    def nm_msg_cycle(self) -> Optional[TimeValue]:
        """Get nmMsgCycle (Pythonic accessor)."""
        return self._nmMsgCycle

    @nm_msg_cycle.setter
    def nm_msg_cycle(self, value: Optional[TimeValue]) -> None:
        """
        Set nmMsgCycle with validation.

        Args:
            value: The nmMsgCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMsgCycle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMsgCycle must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMsgCycle = value
        # stay in the Network Mode into Prepare Bus-Sleep Mode shall take.
        self._nmNetwork: Optional[TimeValue] = None

    @property
    def nm_network(self) -> Optional[TimeValue]:
        """Get nmNetwork (Pythonic accessor)."""
        return self._nmNetwork

    @nm_network.setter
    def nm_network(self, value: Optional[TimeValue]) -> None:
        """
        Set nmNetwork with validation.

        Args:
            value: The nmNetwork to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmNetwork = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmNetwork must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmNetwork = value
        # If this attribute is not configured, the is not used.
        self._nmNidPosition: Optional[Integer] = None

    @property
    def nm_nid_position(self) -> Optional[Integer]:
        """Get nmNidPosition (Pythonic accessor)."""
        return self._nmNidPosition

    @nm_nid_position.setter
    def nm_nid_position(self, value: Optional[Integer]) -> None:
        """
        Set nmNidPosition with validation.

        Args:
            value: The nmNidPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmNidPosition = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"nmNidPosition must be Integer or int or None, got {type(value).__name__}"
            )
        self._nmNidPosition = value
        # It the time how long it shall take to recognize that all nodes are ready to
                # sleep.
        self._nmRemote: Optional[TimeValue] = None

    @property
    def nm_remote(self) -> Optional[TimeValue]:
        """Get nmRemote (Pythonic accessor)."""
        return self._nmRemote

    @nm_remote.setter
    def nm_remote(self, value: Optional[TimeValue]) -> None:
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

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmRemote must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmRemote = value
        # Defines time how long the NM shall stay in the Repeat.
        self._nmRepeat: Optional[TimeValue] = None

    @property
    def nm_repeat(self) -> Optional[TimeValue]:
        """Get nmRepeat (Pythonic accessor)."""
        return self._nmRepeat

    @nm_repeat.setter
    def nm_repeat(self, value: Optional[TimeValue]) -> None:
        """
        Set nmRepeat with validation.

        Args:
            value: The nmRepeat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRepeat = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmRepeat must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmRepeat = value
        # It denotes time how long the CanNm shall stay in the Prepare before
                # transition into Bus-Sleep Mode place.
        self._nmWaitBus: Optional[TimeValue] = None

    @property
    def nm_wait_bus(self) -> Optional[TimeValue]:
        """Get nmWaitBus (Pythonic accessor)."""
        return self._nmWaitBus

    @nm_wait_bus.setter
    def nm_wait_bus(self, value: Optional[TimeValue]) -> None:
        """
        Set nmWaitBus with validation.

        Args:
            value: The nmWaitBus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmWaitBus = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmWaitBus must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmWaitBus = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmBusload(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmBusload.

        Returns:
            The nmBusload value

        Note:
            Delegates to nm_busload property (CODING_RULE_V2_00017)
        """
        return self.nm_busload  # Delegates to property

    def setNmBusload(self, value: Boolean) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmBusload with method chaining.

        Args:
            value: The nmBusload to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_busload property setter (gets validation automatically)
        """
        self.nm_busload = value  # Delegates to property setter
        return self

    def getNmCarWakeUp(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for nmCarWakeUp.

        Returns:
            The nmCarWakeUp value

        Note:
            Delegates to nm_car_wake_up property (CODING_RULE_V2_00017)
        """
        return self.nm_car_wake_up  # Delegates to property

    def setNmCarWakeUp(self, value: PositiveInteger) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmCarWakeUp with method chaining.

        Args:
            value: The nmCarWakeUp to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_car_wake_up property setter (gets validation automatically)
        """
        self.nm_car_wake_up = value  # Delegates to property setter
        return self

    def getNmCarWakeUpFilterNodeId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for nmCarWakeUpFilterNodeId.

        Returns:
            The nmCarWakeUpFilterNodeId value

        Note:
            Delegates to nm_car_wake_up_filter_node_id property (CODING_RULE_V2_00017)
        """
        return self.nm_car_wake_up_filter_node_id  # Delegates to property

    def setNmCarWakeUpFilterNodeId(self, value: PositiveInteger) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmCarWakeUpFilterNodeId with method chaining.

        Args:
            value: The nmCarWakeUpFilterNodeId to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_car_wake_up_filter_node_id property setter (gets validation automatically)
        """
        self.nm_car_wake_up_filter_node_id = value  # Delegates to property setter
        return self

    def getNmCbvPosition(self) -> Integer:
        """
        AUTOSAR-compliant getter for nmCbvPosition.

        Returns:
            The nmCbvPosition value

        Note:
            Delegates to nm_cbv_position property (CODING_RULE_V2_00017)
        """
        return self.nm_cbv_position  # Delegates to property

    def setNmCbvPosition(self, value: Integer) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmCbvPosition with method chaining.

        Args:
            value: The nmCbvPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_cbv_position property setter (gets validation automatically)
        """
        self.nm_cbv_position = value  # Delegates to property setter
        return self

    def getNmImmediate(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for nmImmediate.

        Returns:
            The nmImmediate value

        Note:
            Delegates to nm_immediate property (CODING_RULE_V2_00017)
        """
        return self.nm_immediate  # Delegates to property

    def setNmImmediate(self, value: PositiveInteger) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmImmediate with method chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_immediate property setter (gets validation automatically)
        """
        self.nm_immediate = value  # Delegates to property setter
        return self

    def getNmMessage(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmMessage.

        Returns:
            The nmMessage value

        Note:
            Delegates to nm_message property (CODING_RULE_V2_00017)
        """
        return self.nm_message  # Delegates to property

    def setNmMessage(self, value: TimeValue) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmMessage with method chaining.

        Args:
            value: The nmMessage to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_message property setter (gets validation automatically)
        """
        self.nm_message = value  # Delegates to property setter
        return self

    def getNmMsgCycle(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmMsgCycle.

        Returns:
            The nmMsgCycle value

        Note:
            Delegates to nm_msg_cycle property (CODING_RULE_V2_00017)
        """
        return self.nm_msg_cycle  # Delegates to property

    def setNmMsgCycle(self, value: TimeValue) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmMsgCycle with method chaining.

        Args:
            value: The nmMsgCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_msg_cycle property setter (gets validation automatically)
        """
        self.nm_msg_cycle = value  # Delegates to property setter
        return self

    def getNmNetwork(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmNetwork.

        Returns:
            The nmNetwork value

        Note:
            Delegates to nm_network property (CODING_RULE_V2_00017)
        """
        return self.nm_network  # Delegates to property

    def setNmNetwork(self, value: TimeValue) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmNetwork with method chaining.

        Args:
            value: The nmNetwork to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_network property setter (gets validation automatically)
        """
        self.nm_network = value  # Delegates to property setter
        return self

    def getNmNidPosition(self) -> Integer:
        """
        AUTOSAR-compliant getter for nmNidPosition.

        Returns:
            The nmNidPosition value

        Note:
            Delegates to nm_nid_position property (CODING_RULE_V2_00017)
        """
        return self.nm_nid_position  # Delegates to property

    def setNmNidPosition(self, value: Integer) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmNidPosition with method chaining.

        Args:
            value: The nmNidPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_nid_position property setter (gets validation automatically)
        """
        self.nm_nid_position = value  # Delegates to property setter
        return self

    def getNmRemote(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmRemote.

        Returns:
            The nmRemote value

        Note:
            Delegates to nm_remote property (CODING_RULE_V2_00017)
        """
        return self.nm_remote  # Delegates to property

    def setNmRemote(self, value: TimeValue) -> CanNmCluster:
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

    def getNmRepeat(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmRepeat.

        Returns:
            The nmRepeat value

        Note:
            Delegates to nm_repeat property (CODING_RULE_V2_00017)
        """
        return self.nm_repeat  # Delegates to property

    def setNmRepeat(self, value: TimeValue) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmRepeat with method chaining.

        Args:
            value: The nmRepeat to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_repeat property setter (gets validation automatically)
        """
        self.nm_repeat = value  # Delegates to property setter
        return self

    def getNmWaitBus(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmWaitBus.

        Returns:
            The nmWaitBus value

        Note:
            Delegates to nm_wait_bus property (CODING_RULE_V2_00017)
        """
        return self.nm_wait_bus  # Delegates to property

    def setNmWaitBus(self, value: TimeValue) -> CanNmCluster:
        """
        AUTOSAR-compliant setter for nmWaitBus with method chaining.

        Args:
            value: The nmWaitBus to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_wait_bus property setter (gets validation automatically)
        """
        self.nm_wait_bus = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_busload(self, value: Optional[Boolean]) -> CanNmCluster:
        """
        Set nmBusload and return self for chaining.

        Args:
            value: The nmBusload to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_busload("value")
        """
        self.nm_busload = value  # Use property setter (gets validation)
        return self

    def with_nm_car_wake_up(self, value: Optional[PositiveInteger]) -> CanNmCluster:
        """
        Set nmCarWakeUp and return self for chaining.

        Args:
            value: The nmCarWakeUp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_car_wake_up("value")
        """
        self.nm_car_wake_up = value  # Use property setter (gets validation)
        return self

    def with_nm_car_wake_up_filter_node_id(self, value: Optional[PositiveInteger]) -> CanNmCluster:
        """
        Set nmCarWakeUpFilterNodeId and return self for chaining.

        Args:
            value: The nmCarWakeUpFilterNodeId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_car_wake_up_filter_node_id("value")
        """
        self.nm_car_wake_up_filter_node_id = value  # Use property setter (gets validation)
        return self

    def with_nm_cbv_position(self, value: Optional[Integer]) -> CanNmCluster:
        """
        Set nmCbvPosition and return self for chaining.

        Args:
            value: The nmCbvPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_cbv_position("value")
        """
        self.nm_cbv_position = value  # Use property setter (gets validation)
        return self

    def with_nm_immediate(self, value: Optional[PositiveInteger]) -> CanNmCluster:
        """
        Set nmImmediate and return self for chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_immediate("value")
        """
        self.nm_immediate = value  # Use property setter (gets validation)
        return self

    def with_nm_message(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Set nmMessage and return self for chaining.

        Args:
            value: The nmMessage to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_message("value")
        """
        self.nm_message = value  # Use property setter (gets validation)
        return self

    def with_nm_msg_cycle(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Set nmMsgCycle and return self for chaining.

        Args:
            value: The nmMsgCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_msg_cycle("value")
        """
        self.nm_msg_cycle = value  # Use property setter (gets validation)
        return self

    def with_nm_network(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Set nmNetwork and return self for chaining.

        Args:
            value: The nmNetwork to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_network("value")
        """
        self.nm_network = value  # Use property setter (gets validation)
        return self

    def with_nm_nid_position(self, value: Optional[Integer]) -> CanNmCluster:
        """
        Set nmNidPosition and return self for chaining.

        Args:
            value: The nmNidPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_nid_position("value")
        """
        self.nm_nid_position = value  # Use property setter (gets validation)
        return self

    def with_nm_remote(self, value: Optional[TimeValue]) -> CanNmCluster:
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

    def with_nm_repeat(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Set nmRepeat and return self for chaining.

        Args:
            value: The nmRepeat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_repeat("value")
        """
        self.nm_repeat = value  # Use property setter (gets validation)
        return self

    def with_nm_wait_bus(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Set nmWaitBus and return self for chaining.

        Args:
            value: The nmWaitBus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_wait_bus("value")
        """
        self.nm_wait_bus = value  # Use property setter (gets validation)
        return self



class UdpNmCluster(NmCluster):
    """
    Udp specific NmCluster attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::UdpNmCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 687, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the position of the control bit vector within the Nm position).
        # If this attribute is not configured, the Vector is not used.
        self._nmCbvPosition: Optional[Integer] = None

    @property
    def nm_cbv_position(self) -> Optional[Integer]:
        """Get nmCbvPosition (Pythonic accessor)."""
        return self._nmCbvPosition

    @nm_cbv_position.setter
    def nm_cbv_position(self, value: Optional[Integer]) -> None:
        """
        Set nmCbvPosition with validation.

        Args:
            value: The nmCbvPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCbvPosition = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"nmCbvPosition must be Integer or int or None, got {type(value).__name__}"
            )
        self._nmCbvPosition = value
                # immediate NmPdus transmitted.
        # The cycle time of immediate NmPdus is nmImmediateNmCycleTime.
        self._nmImmediate: Optional[PositiveInteger] = None

    @property
    def nm_immediate(self) -> Optional[PositiveInteger]:
        """Get nmImmediate (Pythonic accessor)."""
        return self._nmImmediate

    @nm_immediate.setter
    def nm_immediate(self, value: Optional[PositiveInteger]) -> None:
        """
        Set nmImmediate with validation.

        Args:
            value: The nmImmediate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmImmediate = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"nmImmediate must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._nmImmediate = value
        # It determines how long NM shall wait with notification of transmission
                # failure errors occur on the bus.
        self._nmMessage: Optional[TimeValue] = None

    @property
    def nm_message(self) -> Optional[TimeValue]:
        """Get nmMessage (Pythonic accessor)."""
        return self._nmMessage

    @nm_message.setter
    def nm_message(self, value: Optional[TimeValue]) -> None:
        """
        Set nmMessage with validation.

        Args:
            value: The nmMessage to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMessage = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMessage must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMessage = value
        # It determines the periodic in the periodic transmission mode with bus load is
                # the basis for transmit scheduling in the mode without bus load reduction.
        self._nmMsgCycle: Optional[TimeValue] = None

    @property
    def nm_msg_cycle(self) -> Optional[TimeValue]:
        """Get nmMsgCycle (Pythonic accessor)."""
        return self._nmMsgCycle

    @nm_msg_cycle.setter
    def nm_msg_cycle(self, value: Optional[TimeValue]) -> None:
        """
        Set nmMsgCycle with validation.

        Args:
            value: The nmMsgCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMsgCycle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMsgCycle must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMsgCycle = value
        # It denotes the how long the UdpNm shall stay in the Network Mode into Prepare
                # Bus-Sleep Mode shall take.
        self._nmNetwork: Optional[TimeValue] = None

    @property
    def nm_network(self) -> Optional[TimeValue]:
        """Get nmNetwork (Pythonic accessor)."""
        return self._nmNetwork

    @nm_network.setter
    def nm_network(self, value: Optional[TimeValue]) -> None:
        """
        Set nmNetwork with validation.

        Args:
            value: The nmNetwork to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmNetwork = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmNetwork must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmNetwork = value
        # If this attribute is not configured, the is not used.
        self._nmNidPosition: Optional[Integer] = None

    @property
    def nm_nid_position(self) -> Optional[Integer]:
        """Get nmNidPosition (Pythonic accessor)."""
        return self._nmNidPosition

    @nm_nid_position.setter
    def nm_nid_position(self, value: Optional[Integer]) -> None:
        """
        Set nmNidPosition with validation.

        Args:
            value: The nmNidPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmNidPosition = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"nmNidPosition must be Integer or int or None, got {type(value).__name__}"
            )
        self._nmNidPosition = value
        # It the time how long it shall take to recognize that all nodes are ready to
                # sleep.
        self._nmRemote: Optional[TimeValue] = None

    @property
    def nm_remote(self) -> Optional[TimeValue]:
        """Get nmRemote (Pythonic accessor)."""
        return self._nmRemote

    @nm_remote.setter
    def nm_remote(self, value: Optional[TimeValue]) -> None:
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

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmRemote must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmRemote = value
        # Defines time how long the NM shall stay in the Repeat.
        self._nmRepeat: Optional[TimeValue] = None

    @property
    def nm_repeat(self) -> Optional[TimeValue]:
        """Get nmRepeat (Pythonic accessor)."""
        return self._nmRepeat

    @nm_repeat.setter
    def nm_repeat(self, value: Optional[TimeValue]) -> None:
        """
        Set nmRepeat with validation.

        Args:
            value: The nmRepeat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRepeat = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmRepeat must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmRepeat = value
        # It denotes time how long the CanNm shall stay in the Prepare before
                # transition into Bus-Sleep Mode place.
        self._nmWaitBus: Optional[TimeValue] = None

    @property
    def nm_wait_bus(self) -> Optional[TimeValue]:
        """Get nmWaitBus (Pythonic accessor)."""
        return self._nmWaitBus

    @nm_wait_bus.setter
    def nm_wait_bus(self, value: Optional[TimeValue]) -> None:
        """
        Set nmWaitBus with validation.

        Args:
            value: The nmWaitBus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmWaitBus = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmWaitBus must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmWaitBus = value
        # apply to.
        self._vlan: Optional[EthernetPhysical] = None

    @property
    def vlan(self) -> Optional[EthernetPhysical]:
        """Get vlan (Pythonic accessor)."""
        return self._vlan

    @vlan.setter
    def vlan(self, value: Optional[EthernetPhysical]) -> None:
        """
        Set vlan with validation.

        Args:
            value: The vlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlan = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"vlan must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._vlan = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmCbvPosition(self) -> Integer:
        """
        AUTOSAR-compliant getter for nmCbvPosition.

        Returns:
            The nmCbvPosition value

        Note:
            Delegates to nm_cbv_position property (CODING_RULE_V2_00017)
        """
        return self.nm_cbv_position  # Delegates to property

    def setNmCbvPosition(self, value: Integer) -> UdpNmCluster:
        """
        AUTOSAR-compliant setter for nmCbvPosition with method chaining.

        Args:
            value: The nmCbvPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_cbv_position property setter (gets validation automatically)
        """
        self.nm_cbv_position = value  # Delegates to property setter
        return self

    def getNmImmediate(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for nmImmediate.

        Returns:
            The nmImmediate value

        Note:
            Delegates to nm_immediate property (CODING_RULE_V2_00017)
        """
        return self.nm_immediate  # Delegates to property

    def setNmImmediate(self, value: PositiveInteger) -> UdpNmCluster:
        """
        AUTOSAR-compliant setter for nmImmediate with method chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_immediate property setter (gets validation automatically)
        """
        self.nm_immediate = value  # Delegates to property setter
        return self

    def getNmMessage(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmMessage.

        Returns:
            The nmMessage value

        Note:
            Delegates to nm_message property (CODING_RULE_V2_00017)
        """
        return self.nm_message  # Delegates to property

    def setNmMessage(self, value: TimeValue) -> UdpNmCluster:
        """
        AUTOSAR-compliant setter for nmMessage with method chaining.

        Args:
            value: The nmMessage to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_message property setter (gets validation automatically)
        """
        self.nm_message = value  # Delegates to property setter
        return self

    def getNmMsgCycle(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmMsgCycle.

        Returns:
            The nmMsgCycle value

        Note:
            Delegates to nm_msg_cycle property (CODING_RULE_V2_00017)
        """
        return self.nm_msg_cycle  # Delegates to property

    def setNmMsgCycle(self, value: TimeValue) -> UdpNmCluster:
        """
        AUTOSAR-compliant setter for nmMsgCycle with method chaining.

        Args:
            value: The nmMsgCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_msg_cycle property setter (gets validation automatically)
        """
        self.nm_msg_cycle = value  # Delegates to property setter
        return self

    def getNmNetwork(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmNetwork.

        Returns:
            The nmNetwork value

        Note:
            Delegates to nm_network property (CODING_RULE_V2_00017)
        """
        return self.nm_network  # Delegates to property

    def setNmNetwork(self, value: TimeValue) -> UdpNmCluster:
        """
        AUTOSAR-compliant setter for nmNetwork with method chaining.

        Args:
            value: The nmNetwork to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_network property setter (gets validation automatically)
        """
        self.nm_network = value  # Delegates to property setter
        return self

    def getNmNidPosition(self) -> Integer:
        """
        AUTOSAR-compliant getter for nmNidPosition.

        Returns:
            The nmNidPosition value

        Note:
            Delegates to nm_nid_position property (CODING_RULE_V2_00017)
        """
        return self.nm_nid_position  # Delegates to property

    def setNmNidPosition(self, value: Integer) -> UdpNmCluster:
        """
        AUTOSAR-compliant setter for nmNidPosition with method chaining.

        Args:
            value: The nmNidPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_nid_position property setter (gets validation automatically)
        """
        self.nm_nid_position = value  # Delegates to property setter
        return self

    def getNmRemote(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmRemote.

        Returns:
            The nmRemote value

        Note:
            Delegates to nm_remote property (CODING_RULE_V2_00017)
        """
        return self.nm_remote  # Delegates to property

    def setNmRemote(self, value: TimeValue) -> UdpNmCluster:
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

    def getNmRepeat(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmRepeat.

        Returns:
            The nmRepeat value

        Note:
            Delegates to nm_repeat property (CODING_RULE_V2_00017)
        """
        return self.nm_repeat  # Delegates to property

    def setNmRepeat(self, value: TimeValue) -> UdpNmCluster:
        """
        AUTOSAR-compliant setter for nmRepeat with method chaining.

        Args:
            value: The nmRepeat to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_repeat property setter (gets validation automatically)
        """
        self.nm_repeat = value  # Delegates to property setter
        return self

    def getNmWaitBus(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmWaitBus.

        Returns:
            The nmWaitBus value

        Note:
            Delegates to nm_wait_bus property (CODING_RULE_V2_00017)
        """
        return self.nm_wait_bus  # Delegates to property

    def setNmWaitBus(self, value: TimeValue) -> UdpNmCluster:
        """
        AUTOSAR-compliant setter for nmWaitBus with method chaining.

        Args:
            value: The nmWaitBus to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_wait_bus property setter (gets validation automatically)
        """
        self.nm_wait_bus = value  # Delegates to property setter
        return self

    def getVlan(self) -> "EthernetPhysical":
        """
        AUTOSAR-compliant getter for vlan.

        Returns:
            The vlan value

        Note:
            Delegates to vlan property (CODING_RULE_V2_00017)
        """
        return self.vlan  # Delegates to property

    def setVlan(self, value: "EthernetPhysical") -> UdpNmCluster:
        """
        AUTOSAR-compliant setter for vlan with method chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan property setter (gets validation automatically)
        """
        self.vlan = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_cbv_position(self, value: Optional[Integer]) -> UdpNmCluster:
        """
        Set nmCbvPosition and return self for chaining.

        Args:
            value: The nmCbvPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_cbv_position("value")
        """
        self.nm_cbv_position = value  # Use property setter (gets validation)
        return self

    def with_nm_immediate(self, value: Optional[PositiveInteger]) -> UdpNmCluster:
        """
        Set nmImmediate and return self for chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_immediate("value")
        """
        self.nm_immediate = value  # Use property setter (gets validation)
        return self

    def with_nm_message(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Set nmMessage and return self for chaining.

        Args:
            value: The nmMessage to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_message("value")
        """
        self.nm_message = value  # Use property setter (gets validation)
        return self

    def with_nm_msg_cycle(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Set nmMsgCycle and return self for chaining.

        Args:
            value: The nmMsgCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_msg_cycle("value")
        """
        self.nm_msg_cycle = value  # Use property setter (gets validation)
        return self

    def with_nm_network(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Set nmNetwork and return self for chaining.

        Args:
            value: The nmNetwork to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_network("value")
        """
        self.nm_network = value  # Use property setter (gets validation)
        return self

    def with_nm_nid_position(self, value: Optional[Integer]) -> UdpNmCluster:
        """
        Set nmNidPosition and return self for chaining.

        Args:
            value: The nmNidPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_nid_position("value")
        """
        self.nm_nid_position = value  # Use property setter (gets validation)
        return self

    def with_nm_remote(self, value: Optional[TimeValue]) -> UdpNmCluster:
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

    def with_nm_repeat(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Set nmRepeat and return self for chaining.

        Args:
            value: The nmRepeat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_repeat("value")
        """
        self.nm_repeat = value  # Use property setter (gets validation)
        return self

    def with_nm_wait_bus(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Set nmWaitBus and return self for chaining.

        Args:
            value: The nmWaitBus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_wait_bus("value")
        """
        self.nm_wait_bus = value  # Use property setter (gets validation)
        return self

    def with_vlan(self, value: Optional[EthernetPhysical]) -> UdpNmCluster:
        """
        Set vlan and return self for chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan("value")
        """
        self.vlan = value  # Use property setter (gets validation)
        return self



class J1939NmCluster(NmCluster):
    """
    J1939 specific NmCluster attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::J1939NmCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 691, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies whether the J1939Nm Bsw is used or not.
        # If this attribute is set to false then configuration shall not be derived
                # from the But even in this case the nmNodeId be necessary for the J1939Rm and
                # J1939Tp.
        self._addressClaim: Optional[Boolean] = None

    @property
    def address_claim(self) -> Optional[Boolean]:
        """Get addressClaim (Pythonic accessor)."""
        return self._addressClaim

    @address_claim.setter
    def address_claim(self, value: Optional[Boolean]) -> None:
        """
        Set addressClaim with validation.

        Args:
            value: The addressClaim to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._addressClaim = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"addressClaim must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._addressClaim = value
                # supported on this The dynamically allocated addresses on the bus at runtime
                # to the configured addresses.
        # The addresses on the bus resemble the.
        self._usesDynamic: Optional[Boolean] = None

    @property
    def uses_dynamic(self) -> Optional[Boolean]:
        """Get usesDynamic (Pythonic accessor)."""
        return self._usesDynamic

    @uses_dynamic.setter
    def uses_dynamic(self, value: Optional[Boolean]) -> None:
        """
        Set usesDynamic with validation.

        Args:
            value: The usesDynamic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usesDynamic = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"usesDynamic must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._usesDynamic = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddressClaim(self) -> Boolean:
        """
        AUTOSAR-compliant getter for addressClaim.

        Returns:
            The addressClaim value

        Note:
            Delegates to address_claim property (CODING_RULE_V2_00017)
        """
        return self.address_claim  # Delegates to property

    def setAddressClaim(self, value: Boolean) -> J1939NmCluster:
        """
        AUTOSAR-compliant setter for addressClaim with method chaining.

        Args:
            value: The addressClaim to set

        Returns:
            self for method chaining

        Note:
            Delegates to address_claim property setter (gets validation automatically)
        """
        self.address_claim = value  # Delegates to property setter
        return self

    def getUsesDynamic(self) -> Boolean:
        """
        AUTOSAR-compliant getter for usesDynamic.

        Returns:
            The usesDynamic value

        Note:
            Delegates to uses_dynamic property (CODING_RULE_V2_00017)
        """
        return self.uses_dynamic  # Delegates to property

    def setUsesDynamic(self, value: Boolean) -> J1939NmCluster:
        """
        AUTOSAR-compliant setter for usesDynamic with method chaining.

        Args:
            value: The usesDynamic to set

        Returns:
            self for method chaining

        Note:
            Delegates to uses_dynamic property setter (gets validation automatically)
        """
        self.uses_dynamic = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address_claim(self, value: Optional[Boolean]) -> J1939NmCluster:
        """
        Set addressClaim and return self for chaining.

        Args:
            value: The addressClaim to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address_claim("value")
        """
        self.address_claim = value  # Use property setter (gets validation)
        return self

    def with_uses_dynamic(self, value: Optional[Boolean]) -> J1939NmCluster:
        """
        Set usesDynamic and return self for chaining.

        Args:
            value: The usesDynamic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uses_dynamic("value")
        """
        self.uses_dynamic = value  # Use property setter (gets validation)
        return self



class FlexrayNmEcu(BusspecificNmEcu):
    """
    FlexRay specific attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::FlexrayNmEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 679, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Switch for enabling the processing of FlexRay Hardware NM-Votes.
        self._nmHwVote: Optional[Boolean] = None

    @property
    def nm_hw_vote(self) -> Optional[Boolean]:
        """Get nmHwVote (Pythonic accessor)."""
        return self._nmHwVote

    @nm_hw_vote.setter
    def nm_hw_vote(self, value: Optional[Boolean]) -> None:
        """
        Set nmHwVote with validation.

        Args:
            value: The nmHwVote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmHwVote = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmHwVote must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmHwVote = value
        # cycle boundary or not.
        self._nmMain: Optional[Boolean] = None

    @property
    def nm_main(self) -> Optional[Boolean]:
        """Get nmMain (Pythonic accessor)."""
        return self._nmMain

    @nm_main.setter
    def nm_main(self, value: Optional[Boolean]) -> None:
        """
        Set nmMain with validation.

        Args:
            value: The nmMain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMain = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmMain must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmMain = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmHwVote(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmHwVote.

        Returns:
            The nmHwVote value

        Note:
            Delegates to nm_hw_vote property (CODING_RULE_V2_00017)
        """
        return self.nm_hw_vote  # Delegates to property

    def setNmHwVote(self, value: Boolean) -> FlexrayNmEcu:
        """
        AUTOSAR-compliant setter for nmHwVote with method chaining.

        Args:
            value: The nmHwVote to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_hw_vote property setter (gets validation automatically)
        """
        self.nm_hw_vote = value  # Delegates to property setter
        return self

    def getNmMain(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmMain.

        Returns:
            The nmMain value

        Note:
            Delegates to nm_main property (CODING_RULE_V2_00017)
        """
        return self.nm_main  # Delegates to property

    def setNmMain(self, value: Boolean) -> FlexrayNmEcu:
        """
        AUTOSAR-compliant setter for nmMain with method chaining.

        Args:
            value: The nmMain to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_main property setter (gets validation automatically)
        """
        self.nm_main = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_hw_vote(self, value: Optional[Boolean]) -> FlexrayNmEcu:
        """
        Set nmHwVote and return self for chaining.

        Args:
            value: The nmHwVote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_hw_vote("value")
        """
        self.nm_hw_vote = value  # Use property setter (gets validation)
        return self

    def with_nm_main(self, value: Optional[Boolean]) -> FlexrayNmEcu:
        """
        Set nmMain and return self for chaining.

        Args:
            value: The nmMain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_main("value")
        """
        self.nm_main = value  # Use property setter (gets validation)
        return self



class CanNmEcu(BusspecificNmEcu):
    """
    CAN specific attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::CanNmEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 683, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class UdpNmEcu(BusspecificNmEcu):
    """
    Udp NM specific ECU attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::UdpNmEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 688, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class J1939NmEcu(BusspecificNmEcu):
    """
    J1939 NmEcu specific attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::J1939NmEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 694, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class J1939NmNode(NmNode):
    """
    J1939 specific NM Node attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::J1939NmNode

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 322, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 691, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the Address Configuration Capability of the J1939NmNode
        # (corresponding to an SAE J1939 Controller Application, CA).
        self._address: Optional[J1939NmAddress] = None

    @property
    def address(self) -> Optional[J1939NmAddress]:
        """Get address (Pythonic accessor)."""
        return self._address

    @address.setter
    def address(self, value: Optional[J1939NmAddress]) -> None:
        """
        Set address with validation.

        Args:
            value: The address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._address = None
            return

        if not isinstance(value, J1939NmAddress):
            raise TypeError(
                f"address must be J1939NmAddress or None, got {type(value).__name__}"
            )
        self._address = value
        self._nodeName: Optional[J1939NodeName] = None

    @property
    def node_name(self) -> Optional[J1939NodeName]:
        """Get nodeName (Pythonic accessor)."""
        return self._nodeName

    @node_name.setter
    def node_name(self, value: Optional[J1939NodeName]) -> None:
        """
        Set nodeName with validation.

        Args:
            value: The nodeName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nodeName = None
            return

        if not isinstance(value, J1939NodeName):
            raise TypeError(
                f"nodeName must be J1939NodeName or None, got {type(value).__name__}"
            )
        self._nodeName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddress(self) -> "J1939NmAddress":
        """
        AUTOSAR-compliant getter for address.

        Returns:
            The address value

        Note:
            Delegates to address property (CODING_RULE_V2_00017)
        """
        return self.address  # Delegates to property

    def setAddress(self, value: "J1939NmAddress") -> J1939NmNode:
        """
        AUTOSAR-compliant setter for address with method chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Note:
            Delegates to address property setter (gets validation automatically)
        """
        self.address = value  # Delegates to property setter
        return self

    def getNodeName(self) -> J1939NodeName:
        """
        AUTOSAR-compliant getter for nodeName.

        Returns:
            The nodeName value

        Note:
            Delegates to node_name property (CODING_RULE_V2_00017)
        """
        return self.node_name  # Delegates to property

    def setNodeName(self, value: J1939NodeName) -> J1939NmNode:
        """
        AUTOSAR-compliant setter for nodeName with method chaining.

        Args:
            value: The nodeName to set

        Returns:
            self for method chaining

        Note:
            Delegates to node_name property setter (gets validation automatically)
        """
        self.node_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address(self, value: Optional[J1939NmAddress]) -> J1939NmNode:
        """
        Set address and return self for chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address("value")
        """
        self.address = value  # Use property setter (gets validation)
        return self

    def with_node_name(self, value: Optional[J1939NodeName]) -> J1939NmNode:
        """
        Set nodeName and return self for chaining.

        Args:
            value: The nodeName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_node_name("value")
        """
        self.node_name = value  # Use property setter (gets validation)
        return self



class FlexrayNmNode(NmNode):
    """
    FlexRay specific NM Node attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::FlexrayNmNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 679, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CanNmNode(NmNode):
    """
    CAN specific NM Node attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::CanNmNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 684, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies if Nm drops irrelevant NM PDUs.
        # Only NM PDUs with a Partial Network Information = true and containing a
                # Partial Network request ECU trigger the standard RX indication handling keep
                # the ECU awake NM PDU triggers the standard RX indication keeps the ECU awake.
        self._allNmMessages: Optional[Boolean] = None

    @property
    def all_nm_messages(self) -> Optional[Boolean]:
        """Get allNmMessages (Pythonic accessor)."""
        return self._allNmMessages

    @all_nm_messages.setter
    def all_nm_messages(self, value: Optional[Boolean]) -> None:
        """
        Set allNmMessages with validation.

        Args:
            value: The allNmMessages to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._allNmMessages = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"allNmMessages must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._allNmMessages = value
        # in received NmPdus.
        self._nmCarWakeUp: Optional[Boolean] = None

    @property
    def nm_car_wake_up(self) -> Optional[Boolean]:
        """Get nmCarWakeUp (Pythonic accessor)."""
        return self._nmCarWakeUp

    @nm_car_wake_up.setter
    def nm_car_wake_up(self, value: Optional[Boolean]) -> None:
        """
        Set nmCarWakeUp with validation.

        Args:
            value: The nmCarWakeUp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCarWakeUp = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmCarWakeUp must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmCarWakeUp = value
                # start delay of the transmission.
        # seconds.
        self._nmMsgCycle: Optional[TimeValue] = None

    @property
    def nm_msg_cycle(self) -> Optional[TimeValue]:
        """Get nmMsgCycle (Pythonic accessor)."""
        return self._nmMsgCycle

    @nm_msg_cycle.setter
    def nm_msg_cycle(self, value: Optional[TimeValue]) -> None:
        """
        Set nmMsgCycle with validation.

        Args:
            value: The nmMsgCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMsgCycle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMsgCycle must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMsgCycle = value
                # reduction.
        # Specified in seconds.
        self._nmMsg: Optional[TimeValue] = None

    @property
    def nm_msg(self) -> Optional[TimeValue]:
        """Get nmMsg (Pythonic accessor)."""
        return self._nmMsg

    @nm_msg.setter
    def nm_msg(self, value: Optional[TimeValue]) -> None:
        """
        Set nmMsg with validation.

        Args:
            value: The nmMsg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMsg = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMsg must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMsg = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllNmMessages(self) -> Boolean:
        """
        AUTOSAR-compliant getter for allNmMessages.

        Returns:
            The allNmMessages value

        Note:
            Delegates to all_nm_messages property (CODING_RULE_V2_00017)
        """
        return self.all_nm_messages  # Delegates to property

    def setAllNmMessages(self, value: Boolean) -> CanNmNode:
        """
        AUTOSAR-compliant setter for allNmMessages with method chaining.

        Args:
            value: The allNmMessages to set

        Returns:
            self for method chaining

        Note:
            Delegates to all_nm_messages property setter (gets validation automatically)
        """
        self.all_nm_messages = value  # Delegates to property setter
        return self

    def getNmCarWakeUp(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmCarWakeUp.

        Returns:
            The nmCarWakeUp value

        Note:
            Delegates to nm_car_wake_up property (CODING_RULE_V2_00017)
        """
        return self.nm_car_wake_up  # Delegates to property

    def setNmCarWakeUp(self, value: Boolean) -> CanNmNode:
        """
        AUTOSAR-compliant setter for nmCarWakeUp with method chaining.

        Args:
            value: The nmCarWakeUp to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_car_wake_up property setter (gets validation automatically)
        """
        self.nm_car_wake_up = value  # Delegates to property setter
        return self

    def getNmMsgCycle(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmMsgCycle.

        Returns:
            The nmMsgCycle value

        Note:
            Delegates to nm_msg_cycle property (CODING_RULE_V2_00017)
        """
        return self.nm_msg_cycle  # Delegates to property

    def setNmMsgCycle(self, value: TimeValue) -> CanNmNode:
        """
        AUTOSAR-compliant setter for nmMsgCycle with method chaining.

        Args:
            value: The nmMsgCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_msg_cycle property setter (gets validation automatically)
        """
        self.nm_msg_cycle = value  # Delegates to property setter
        return self

    def getNmMsg(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmMsg.

        Returns:
            The nmMsg value

        Note:
            Delegates to nm_msg property (CODING_RULE_V2_00017)
        """
        return self.nm_msg  # Delegates to property

    def setNmMsg(self, value: TimeValue) -> CanNmNode:
        """
        AUTOSAR-compliant setter for nmMsg with method chaining.

        Args:
            value: The nmMsg to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_msg property setter (gets validation automatically)
        """
        self.nm_msg = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_all_nm_messages(self, value: Optional[Boolean]) -> CanNmNode:
        """
        Set allNmMessages and return self for chaining.

        Args:
            value: The allNmMessages to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_all_nm_messages("value")
        """
        self.all_nm_messages = value  # Use property setter (gets validation)
        return self

    def with_nm_car_wake_up(self, value: Optional[Boolean]) -> CanNmNode:
        """
        Set nmCarWakeUp and return self for chaining.

        Args:
            value: The nmCarWakeUp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_car_wake_up("value")
        """
        self.nm_car_wake_up = value  # Use property setter (gets validation)
        return self

    def with_nm_msg_cycle(self, value: Optional[TimeValue]) -> CanNmNode:
        """
        Set nmMsgCycle and return self for chaining.

        Args:
            value: The nmMsgCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_msg_cycle("value")
        """
        self.nm_msg_cycle = value  # Use property setter (gets validation)
        return self

    def with_nm_msg(self, value: Optional[TimeValue]) -> CanNmNode:
        """
        Set nmMsg and return self for chaining.

        Args:
            value: The nmMsg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_msg("value")
        """
        self.nm_msg = value  # Use property setter (gets validation)
        return self



class UdpNmNode(NmNode):
    """
    Udp specific NM Node attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::UdpNmNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 688, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies if Nm drops irrelevant NM PDUs.
        # Only NM PDUs with a Partial Network Information = true and containing a
                # Partial Network request ECU trigger the standard RX indication handling keep
                # the ECU awake NM PDU triggers the standard RX indication keeps the ECU awake.
        self._allNmMessages: Optional[Boolean] = None

    @property
    def all_nm_messages(self) -> Optional[Boolean]:
        """Get allNmMessages (Pythonic accessor)."""
        return self._allNmMessages

    @all_nm_messages.setter
    def all_nm_messages(self, value: Optional[Boolean]) -> None:
        """
        Set allNmMessages with validation.

        Args:
            value: The allNmMessages to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._allNmMessages = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"allNmMessages must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._allNmMessages = value
                # start delay of the transmission.
        # seconds.
        self._nmMsgCycle: Optional[TimeValue] = None

    @property
    def nm_msg_cycle(self) -> Optional[TimeValue]:
        """Get nmMsgCycle (Pythonic accessor)."""
        return self._nmMsgCycle

    @nm_msg_cycle.setter
    def nm_msg_cycle(self, value: Optional[TimeValue]) -> None:
        """
        Set nmMsgCycle with validation.

        Args:
            value: The nmMsgCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMsgCycle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMsgCycle must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMsgCycle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllNmMessages(self) -> Boolean:
        """
        AUTOSAR-compliant getter for allNmMessages.

        Returns:
            The allNmMessages value

        Note:
            Delegates to all_nm_messages property (CODING_RULE_V2_00017)
        """
        return self.all_nm_messages  # Delegates to property

    def setAllNmMessages(self, value: Boolean) -> UdpNmNode:
        """
        AUTOSAR-compliant setter for allNmMessages with method chaining.

        Args:
            value: The allNmMessages to set

        Returns:
            self for method chaining

        Note:
            Delegates to all_nm_messages property setter (gets validation automatically)
        """
        self.all_nm_messages = value  # Delegates to property setter
        return self

    def getNmMsgCycle(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for nmMsgCycle.

        Returns:
            The nmMsgCycle value

        Note:
            Delegates to nm_msg_cycle property (CODING_RULE_V2_00017)
        """
        return self.nm_msg_cycle  # Delegates to property

    def setNmMsgCycle(self, value: TimeValue) -> UdpNmNode:
        """
        AUTOSAR-compliant setter for nmMsgCycle with method chaining.

        Args:
            value: The nmMsgCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_msg_cycle property setter (gets validation automatically)
        """
        self.nm_msg_cycle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_all_nm_messages(self, value: Optional[Boolean]) -> UdpNmNode:
        """
        Set allNmMessages and return self for chaining.

        Args:
            value: The allNmMessages to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_all_nm_messages("value")
        """
        self.all_nm_messages = value  # Use property setter (gets validation)
        return self

    def with_nm_msg_cycle(self, value: Optional[TimeValue]) -> UdpNmNode:
        """
        Set nmMsgCycle and return self for chaining.

        Args:
            value: The nmMsgCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_msg_cycle("value")
        """
        self.nm_msg_cycle = value  # Use property setter (gets validation)
        return self



class FlexrayNmClusterCoupling(NmClusterCoupling):
    """
    FlexRay attributes that are valid for each of the referenced (coupled)
    FlexRay clusters.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::FlexrayNmClusterCoupling

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 679, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to coupled FlexRay Clusters.
        self._coupledCluster: List[FlexrayNmCluster] = []

    @property
    def coupled_cluster(self) -> List[FlexrayNmCluster]:
        """Get coupledCluster (Pythonic accessor)."""
        return self._coupledCluster
        # FrNm schedule variant according to FrNm SWS.
        self._nmSchedule: Optional[FlexrayNmSchedule] = None

    @property
    def nm_schedule(self) -> Optional[FlexrayNmSchedule]:
        """Get nmSchedule (Pythonic accessor)."""
        return self._nmSchedule

    @nm_schedule.setter
    def nm_schedule(self, value: Optional[FlexrayNmSchedule]) -> None:
        """
        Set nmSchedule with validation.

        Args:
            value: The nmSchedule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmSchedule = None
            return

        if not isinstance(value, FlexrayNmSchedule):
            raise TypeError(
                f"nmSchedule must be FlexrayNmSchedule or None, got {type(value).__name__}"
            )
        self._nmSchedule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCoupledCluster(self) -> List[FlexrayNmCluster]:
        """
        AUTOSAR-compliant getter for coupledCluster.

        Returns:
            The coupledCluster value

        Note:
            Delegates to coupled_cluster property (CODING_RULE_V2_00017)
        """
        return self.coupled_cluster  # Delegates to property

    def getNmSchedule(self) -> "FlexrayNmSchedule":
        """
        AUTOSAR-compliant getter for nmSchedule.

        Returns:
            The nmSchedule value

        Note:
            Delegates to nm_schedule property (CODING_RULE_V2_00017)
        """
        return self.nm_schedule  # Delegates to property

    def setNmSchedule(self, value: "FlexrayNmSchedule") -> FlexrayNmClusterCoupling:
        """
        AUTOSAR-compliant setter for nmSchedule with method chaining.

        Args:
            value: The nmSchedule to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_schedule property setter (gets validation automatically)
        """
        self.nm_schedule = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_schedule(self, value: Optional[FlexrayNmSchedule]) -> FlexrayNmClusterCoupling:
        """
        Set nmSchedule and return self for chaining.

        Args:
            value: The nmSchedule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_schedule("value")
        """
        self.nm_schedule = value  # Use property setter (gets validation)
        return self



class CanNmClusterCoupling(NmClusterCoupling):
    """
    CAN attributes that are valid for each of the referenced (coupled) CAN
    clusters.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::CanNmClusterCoupling

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 684, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to coupled CAN Clusters.
        self._coupledCluster: List[CanNmCluster] = []

    @property
    def coupled_cluster(self) -> List[CanNmCluster]:
        """Get coupledCluster (Pythonic accessor)."""
        return self._coupledCluster
        # Enables busload reduction support.
        self._nmBusloadReductionEnabled: Optional[Boolean] = None

    @property
    def nm_busload_reduction_enabled(self) -> Optional[Boolean]:
        """Get nmBusloadReductionEnabled (Pythonic accessor)."""
        return self._nmBusloadReductionEnabled

    @nm_busload_reduction_enabled.setter
    def nm_busload_reduction_enabled(self, value: Optional[Boolean]) -> None:
        """
        Set nmBusloadReductionEnabled with validation.

        Args:
            value: The nmBusloadReductionEnabled to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmBusloadReductionEnabled = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmBusloadReductionEnabled must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmBusloadReductionEnabled = value
        # request in.
        self._nmImmediate: Optional[Boolean] = None

    @property
    def nm_immediate(self) -> Optional[Boolean]:
        """Get nmImmediate (Pythonic accessor)."""
        return self._nmImmediate

    @nm_immediate.setter
    def nm_immediate(self, value: Optional[Boolean]) -> None:
        """
        Set nmImmediate with validation.

        Args:
            value: The nmImmediate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmImmediate = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmImmediate must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmImmediate = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCoupledCluster(self) -> List[CanNmCluster]:
        """
        AUTOSAR-compliant getter for coupledCluster.

        Returns:
            The coupledCluster value

        Note:
            Delegates to coupled_cluster property (CODING_RULE_V2_00017)
        """
        return self.coupled_cluster  # Delegates to property

    def getNmBusloadReductionEnabled(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmBusloadReductionEnabled.

        Returns:
            The nmBusloadReductionEnabled value

        Note:
            Delegates to nm_busload_reduction_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_busload_reduction_enabled  # Delegates to property

    def setNmBusloadReductionEnabled(self, value: Boolean) -> CanNmClusterCoupling:
        """
        AUTOSAR-compliant setter for nmBusloadReductionEnabled with method chaining.

        Args:
            value: The nmBusloadReductionEnabled to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_busload_reduction_enabled property setter (gets validation automatically)
        """
        self.nm_busload_reduction_enabled = value  # Delegates to property setter
        return self

    def getNmImmediate(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmImmediate.

        Returns:
            The nmImmediate value

        Note:
            Delegates to nm_immediate property (CODING_RULE_V2_00017)
        """
        return self.nm_immediate  # Delegates to property

    def setNmImmediate(self, value: Boolean) -> CanNmClusterCoupling:
        """
        AUTOSAR-compliant setter for nmImmediate with method chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_immediate property setter (gets validation automatically)
        """
        self.nm_immediate = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_busload_reduction_enabled(self, value: Optional[Boolean]) -> CanNmClusterCoupling:
        """
        Set nmBusloadReductionEnabled and return self for chaining.

        Args:
            value: The nmBusloadReductionEnabled to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_busload_reduction_enabled("value")
        """
        self.nm_busload_reduction_enabled = value  # Use property setter (gets validation)
        return self

    def with_nm_immediate(self, value: Optional[Boolean]) -> CanNmClusterCoupling:
        """
        Set nmImmediate and return self for chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_immediate("value")
        """
        self.nm_immediate = value  # Use property setter (gets validation)
        return self



class UdpNmClusterCoupling(NmClusterCoupling):
    """
    Udp attributes that are valid for each of the referenced (coupled) UdpNm
    clusters.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::UdpNmClusterCoupling

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 688, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to coupled UdpNm Clusters.
        self._coupledCluster: List[UdpNmCluster] = []

    @property
    def coupled_cluster(self) -> List[UdpNmCluster]:
        """Get coupledCluster (Pythonic accessor)."""
        return self._coupledCluster
        # Enables the asynchronous transmission of a CanNm upon bus-communication
        # request in.
        self._nmImmediate: Optional[Boolean] = None

    @property
    def nm_immediate(self) -> Optional[Boolean]:
        """Get nmImmediate (Pythonic accessor)."""
        return self._nmImmediate

    @nm_immediate.setter
    def nm_immediate(self, value: Optional[Boolean]) -> None:
        """
        Set nmImmediate with validation.

        Args:
            value: The nmImmediate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmImmediate = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmImmediate must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmImmediate = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCoupledCluster(self) -> List[UdpNmCluster]:
        """
        AUTOSAR-compliant getter for coupledCluster.

        Returns:
            The coupledCluster value

        Note:
            Delegates to coupled_cluster property (CODING_RULE_V2_00017)
        """
        return self.coupled_cluster  # Delegates to property

    def getNmImmediate(self) -> Boolean:
        """
        AUTOSAR-compliant getter for nmImmediate.

        Returns:
            The nmImmediate value

        Note:
            Delegates to nm_immediate property (CODING_RULE_V2_00017)
        """
        return self.nm_immediate  # Delegates to property

    def setNmImmediate(self, value: Boolean) -> UdpNmClusterCoupling:
        """
        AUTOSAR-compliant setter for nmImmediate with method chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_immediate property setter (gets validation automatically)
        """
        self.nm_immediate = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_immediate(self, value: Optional[Boolean]) -> UdpNmClusterCoupling:
        """
        Set nmImmediate and return self for chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_immediate("value")
        """
        self.nm_immediate = value  # Use property setter (gets validation)
        return self


class NmCoordinatorRoleEnum(AREnum):
    """
    NmCoordinatorRoleEnum enumeration

Supported NmCoordinator roles. Aggregated by NmNode.nmCoordinatorRole

Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement
    """
    # Coordinator which "actively" performs NmCoordinator functionality at this channel
    Active = "0"

    # Coordinator which "passively" performs NmCoordinator functionality at this channel - used at Nm CoordinatorSync use case.
    Passive = "1"



class FlexrayNmScheduleVariant(AREnum):
    """
    FlexrayNmScheduleVariant enumeration

FrNm schedule variant according to FrNm SWS. Aggregated by FlexrayNmClusterCoupling.nmScheduleVariant

Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement
    """
    # NM-Vote and NM Data transmitted within one PDU in static segment. The NM-Vote has to be realized as separate bit within the PDU.
    scheduleVariant1 = "0"

    # NM-Vote and NM-Data transmitted within one PDU in dynamic segment. The presence (or
    scheduleVariant2 = "1"

    # NM-Vote and NM-Data are transmitted in the static segment in separate PDUs. This alternative is not
    scheduleVariant3recommended = "2"

    # NM-Vote transmitted in static and NM-Data transmitted in dynamic segment.
    scheduleVariant4 = "3"

    # NM-Vote is transmitted in dynamic and NM-Data is transmitted in static segment. This alternative is not recommended => Variants 2 or 6 should be used instead.
    scheduleVariant5 = "4"

    # NM-Vote and NM-Data are transmitted in dynamic segment in separate PDUs.
    scheduleVariant6 = "5"

    # NM-Vote and a copy of the CBV are transmitted in the static segment (using the FlexRay NM Vector
    scheduleVariant7 = "6"



class J1939NmAddressConfigurationCapabilityEnum(AREnum):
    """
    J1939NmAddressConfigurationCapabilityEnum enumeration

Defines the Address Configuration Capability options for the J1939NmNode. Aggregated by J1939NmNode.addressConfigurationCapability

Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement
    """
    # Arbitrary Address Capable CA
    J1939NM_AAC = "4"

    # Command Configurable Address CA.
    J1939NM_CCA = "3"

    # Non-Configurable Address CA.
    J1939NM_NCA = "0"

    # Self-Configurable Address CA.
    J1939NM_SCA = "2"

    # Service Configurable Address CA.
    J1939NM_SVCA = "1"
