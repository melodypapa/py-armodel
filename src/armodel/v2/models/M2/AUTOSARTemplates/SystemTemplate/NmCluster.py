from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


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
        self._communication: Optional["CommunicationCluster"] = None

    @property
    def communication(self) -> Optional["CommunicationCluster"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["CommunicationCluster"]) -> None:
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
        # This parameter shall be set to indicate if the sleep of this can be
        # absolutely decided by the local node only no other nodes can oppose that
        # decision.
        self._nmChannel: Optional["Boolean"] = None

    @property
    def nm_channel(self) -> Optional["Boolean"]:
        """Get nmChannel (Pythonic accessor)."""
        return self._nmChannel

    @nm_channel.setter
    def nm_channel(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmChannel must be Boolean or None, got {type(value).__name__}"
            )
        self._nmChannel = value
        # Enables the Request Repeat Message Request support.
        # valid if nmNodeIdEnabled is set to true.
        self._nmNode: Optional["Boolean"] = None

    @property
    def nm_node(self) -> Optional["Boolean"]:
        """Get nmNode (Pythonic accessor)."""
        return self._nmNode

    @nm_node.setter
    def nm_node(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmNode must be Boolean or None, got {type(value).__name__}"
            )
        self._nmNode = value
        # Enables the source node identifier.
        self._nmNodeIdEnabled: Optional["Boolean"] = None

    @property
    def nm_node_id_enabled(self) -> Optional["Boolean"]:
        """Get nmNodeIdEnabled (Pythonic accessor)."""
        return self._nmNodeIdEnabled

    @nm_node_id_enabled.setter
    def nm_node_id_enabled(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmNodeIdEnabled must be Boolean or None, got {type(value).__name__}"
            )
        self._nmNodeIdEnabled = value
        # Defines whether this NmCluster contributes to the partial mechanism.
        self._nmPnc: Optional["Boolean"] = None

    @property
    def nm_pnc(self) -> Optional["Boolean"]:
        """Get nmPnc (Pythonic accessor)."""
        return self._nmPnc

    @nm_pnc.setter
    def nm_pnc(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmPnc must be Boolean or None, got {type(value).__name__}"
            )
        self._nmPnc = value
        # Switch for enabling the Repeat Message Bit Indication.
        self._nmRepeatMsg: Optional["Boolean"] = None

    @property
    def nm_repeat_msg(self) -> Optional["Boolean"]:
        """Get nmRepeatMsg (Pythonic accessor)."""
        return self._nmRepeatMsg

    @nm_repeat_msg.setter
    def nm_repeat_msg(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmRepeatMsg must be Boolean or None, got {type(value).__name__}"
            )
        self._nmRepeatMsg = value
        # If this parameter is true, then this network is a network for the NM
                # coordination cluster it belongs to.
        # The network is expected to call Nm_ regular intervals.
        self._nm: Optional["Boolean"] = None

    @property
    def nm(self) -> Optional["Boolean"]:
        """Get nm (Pythonic accessor)."""
        return self._nm

    @nm.setter
    def nm(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nm must be Boolean or None, got {type(value).__name__}"
            )
        self._nm = value
        # Optionally defines the length of the PNC Vector per (and VLAN in case of
                # UdpNm).
        # If then System.
        # pncVectorLength applies.
        # make the PNC Vector shorter (or same defined in System.
        # pncVectorLength).
        self._pncCluster: Optional["PositiveInteger"] = None

    @property
    def pnc_cluster(self) -> Optional["PositiveInteger"]:
        """Get pncCluster (Pythonic accessor)."""
        return self._pncCluster

    @pnc_cluster.setter
    def pnc_cluster(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pncCluster must be PositiveInteger or None, got {type(value).__name__}"
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

    def setCommunication(self, value: "CommunicationCluster") -> "NmCluster":
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

    def getNmChannel(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmChannel.

        Returns:
            The nmChannel value

        Note:
            Delegates to nm_channel property (CODING_RULE_V2_00017)
        """
        return self.nm_channel  # Delegates to property

    def setNmChannel(self, value: "Boolean") -> "NmCluster":
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

    def getNmNode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmNode.

        Returns:
            The nmNode value

        Note:
            Delegates to nm_node property (CODING_RULE_V2_00017)
        """
        return self.nm_node  # Delegates to property

    def setNmNode(self, value: "Boolean") -> "NmCluster":
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

    def getNmNodeIdEnabled(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmNodeIdEnabled.

        Returns:
            The nmNodeIdEnabled value

        Note:
            Delegates to nm_node_id_enabled property (CODING_RULE_V2_00017)
        """
        return self.nm_node_id_enabled  # Delegates to property

    def setNmNodeIdEnabled(self, value: "Boolean") -> "NmCluster":
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

    def getNmPnc(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmPnc.

        Returns:
            The nmPnc value

        Note:
            Delegates to nm_pnc property (CODING_RULE_V2_00017)
        """
        return self.nm_pnc  # Delegates to property

    def setNmPnc(self, value: "Boolean") -> "NmCluster":
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

    def getNmRepeatMsg(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmRepeatMsg.

        Returns:
            The nmRepeatMsg value

        Note:
            Delegates to nm_repeat_msg property (CODING_RULE_V2_00017)
        """
        return self.nm_repeat_msg  # Delegates to property

    def setNmRepeatMsg(self, value: "Boolean") -> "NmCluster":
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

    def getNm(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nm.

        Returns:
            The nm value

        Note:
            Delegates to nm property (CODING_RULE_V2_00017)
        """
        return self.nm  # Delegates to property

    def setNm(self, value: "Boolean") -> "NmCluster":
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

    def getPncCluster(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pncCluster.

        Returns:
            The pncCluster value

        Note:
            Delegates to pnc_cluster property (CODING_RULE_V2_00017)
        """
        return self.pnc_cluster  # Delegates to property

    def setPncCluster(self, value: "PositiveInteger") -> "NmCluster":
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

    def with_communication(self, value: Optional["CommunicationCluster"]) -> "NmCluster":
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

    def with_nm_channel(self, value: Optional["Boolean"]) -> "NmCluster":
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

    def with_nm_node(self, value: Optional["Boolean"]) -> "NmCluster":
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

    def with_nm_node_id_enabled(self, value: Optional["Boolean"]) -> "NmCluster":
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

    def with_nm_pnc(self, value: Optional["Boolean"]) -> "NmCluster":
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

    def with_nm_repeat_msg(self, value: Optional["Boolean"]) -> "NmCluster":
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

    def with_nm(self, value: Optional["Boolean"]) -> "NmCluster":
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

    def with_pnc_cluster(self, value: Optional["PositiveInteger"]) -> "NmCluster":
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
