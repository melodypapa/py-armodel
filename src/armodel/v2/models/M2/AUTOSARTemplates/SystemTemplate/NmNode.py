from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

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
        self._controller: Optional["Communication"] = None

    @property
    def controller(self) -> Optional["Communication"]:
        """Get controller (Pythonic accessor)."""
        return self._controller

    @controller.setter
    def controller(self, value: Optional["Communication"]) -> None:
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
        # NmCoordinationCluster identification number.
        self._nmCoordCluster: Optional["PositiveInteger"] = None

    @property
    def nm_coord_cluster(self) -> Optional["PositiveInteger"]:
        """Get nmCoordCluster (Pythonic accessor)."""
        return self._nmCoordCluster

    @nm_coord_cluster.setter
    def nm_coord_cluster(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"nmCoordCluster must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._nmCoordCluster = value
        # This attribute indicates the role the NM Coordinator will have on this
                # channel.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._nmCoordinator: Optional["NmCoordinatorRole"] = None

    @property
    def nm_coordinator(self) -> Optional["NmCoordinatorRole"]:
        """Get nmCoordinator (Pythonic accessor)."""
        return self._nmCoordinator

    @nm_coordinator.setter
    def nm_coordinator(self, value: Optional["NmCoordinatorRole"]) -> None:
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
        # Reference to the NmEcu that contains this NmNode.
        # is referenced by the Nm be contained in the EcuInstance that is the NmEcu).
        self._nmIfEcu: Optional["NmEcu"] = None

    @property
    def nm_if_ecu(self) -> Optional["NmEcu"]:
        """Get nmIfEcu (Pythonic accessor)."""
        return self._nmIfEcu

    @nm_if_ecu.setter
    def nm_if_ecu(self, value: Optional["NmEcu"]) -> None:
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
        # Node identifier of local NmNode.
        # Shall be unique in the.
        self._nmNodeId: Optional["Integer"] = None

    @property
    def nm_node_id(self) -> Optional["Integer"]:
        """Get nmNodeId (Pythonic accessor)."""
        return self._nmNodeId

    @nm_node_id.setter
    def nm_node_id(self, value: Optional["Integer"]) -> None:
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

        if not isinstance(value, Integer):
            raise TypeError(
                f"nmNodeId must be Integer or None, got {type(value).__name__}"
            )
        self._nmNodeId = value
        # Enables support of the Passive Mode.
        # The passive mode configurable per channel.
        self._nmPassive: Optional["Boolean"] = None

    @property
    def nm_passive(self) -> Optional["Boolean"]:
        """Get nmPassive (Pythonic accessor)."""
        return self._nmPassive

    @nm_passive.setter
    def nm_passive(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmPassive must be Boolean or None, got {type(value).__name__}"
            )
        self._nmPassive = value
        # receive NM Pdu.
        self._rxNmPdu: List["NmPdu"] = []

    @property
    def rx_nm_pdu(self) -> List["NmPdu"]:
        """Get rxNmPdu (Pythonic accessor)."""
        return self._rxNmPdu
        # transmit NM Pdu.
        self._txNmPdu: List["NmPdu"] = []

    @property
    def tx_nm_pdu(self) -> List["NmPdu"]:
        """Get txNmPdu (Pythonic accessor)."""
        return self._txNmPdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getController(self) -> "Communication":
        """
        AUTOSAR-compliant getter for controller.
        
        Returns:
            The controller value
        
        Note:
            Delegates to controller property (CODING_RULE_V2_00017)
        """
        return self.controller  # Delegates to property

    def setController(self, value: "Communication") -> "NmNode":
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

    def getNmCoordCluster(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for nmCoordCluster.
        
        Returns:
            The nmCoordCluster value
        
        Note:
            Delegates to nm_coord_cluster property (CODING_RULE_V2_00017)
        """
        return self.nm_coord_cluster  # Delegates to property

    def setNmCoordCluster(self, value: "PositiveInteger") -> "NmNode":
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

    def setNmCoordinator(self, value: "NmCoordinatorRole") -> "NmNode":
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

    def getNmIfEcu(self) -> "NmEcu":
        """
        AUTOSAR-compliant getter for nmIfEcu.
        
        Returns:
            The nmIfEcu value
        
        Note:
            Delegates to nm_if_ecu property (CODING_RULE_V2_00017)
        """
        return self.nm_if_ecu  # Delegates to property

    def setNmIfEcu(self, value: "NmEcu") -> "NmNode":
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

    def getNmNodeId(self) -> "Integer":
        """
        AUTOSAR-compliant getter for nmNodeId.
        
        Returns:
            The nmNodeId value
        
        Note:
            Delegates to nm_node_id property (CODING_RULE_V2_00017)
        """
        return self.nm_node_id  # Delegates to property

    def setNmNodeId(self, value: "Integer") -> "NmNode":
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

    def getNmPassive(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmPassive.
        
        Returns:
            The nmPassive value
        
        Note:
            Delegates to nm_passive property (CODING_RULE_V2_00017)
        """
        return self.nm_passive  # Delegates to property

    def setNmPassive(self, value: "Boolean") -> "NmNode":
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

    def getRxNmPdu(self) -> List["NmPdu"]:
        """
        AUTOSAR-compliant getter for rxNmPdu.
        
        Returns:
            The rxNmPdu value
        
        Note:
            Delegates to rx_nm_pdu property (CODING_RULE_V2_00017)
        """
        return self.rx_nm_pdu  # Delegates to property

    def getTxNmPdu(self) -> List["NmPdu"]:
        """
        AUTOSAR-compliant getter for txNmPdu.
        
        Returns:
            The txNmPdu value
        
        Note:
            Delegates to tx_nm_pdu property (CODING_RULE_V2_00017)
        """
        return self.tx_nm_pdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_controller(self, value: Optional["Communication"]) -> "NmNode":
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

    def with_nm_coord_cluster(self, value: Optional["PositiveInteger"]) -> "NmNode":
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

    def with_nm_coordinator(self, value: Optional["NmCoordinatorRole"]) -> "NmNode":
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

    def with_nm_if_ecu(self, value: Optional["NmEcu"]) -> "NmNode":
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

    def with_nm_node_id(self, value: Optional["Integer"]) -> "NmNode":
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

    def with_nm_passive(self, value: Optional["Boolean"]) -> "NmNode":
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