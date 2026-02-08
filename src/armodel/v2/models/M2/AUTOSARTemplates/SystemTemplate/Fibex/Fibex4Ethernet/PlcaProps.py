from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class PlcaProps(ARObject):
    """
    This meta-class allows to configure the PLCA (Physical Layer Collision
    Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the
    CouplingPort (PHY).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 169, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the node ID when the PLCA mode 10BASE-T1S is used.
        self._plcaLocalNode: Optional["PositiveInteger"] = None

    @property
    def plca_local_node(self) -> Optional["PositiveInteger"]:
        """Get plcaLocalNode (Pythonic accessor)."""
        return self._plcaLocalNode

    @plca_local_node.setter
    def plca_local_node(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set plcaLocalNode with validation.

        Args:
            value: The plcaLocalNode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._plcaLocalNode = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"plcaLocalNode must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._plcaLocalNode = value
        # Limits the burst frames in bit time.
        # This configuration can different from one ECU to another within the PLCA For
                # PLCA burst mode to work properly should be set greater than one IPG.
        self._plcaMaxBurst: Optional["PositiveInteger"] = None

    @property
    def plca_max_burst(self) -> Optional["PositiveInteger"]:
        """Get plcaMaxBurst (Pythonic accessor)."""
        return self._plcaMaxBurst

    @plca_max_burst.setter
    def plca_max_burst(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set plcaMaxBurst with validation.

        Args:
            value: The plcaMaxBurst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._plcaMaxBurst = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"plcaMaxBurst must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._plcaMaxBurst = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPlcaLocalNode(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for plcaLocalNode.

        Returns:
            The plcaLocalNode value

        Note:
            Delegates to plca_local_node property (CODING_RULE_V2_00017)
        """
        return self.plca_local_node  # Delegates to property

    def setPlcaLocalNode(self, value: "PositiveInteger") -> "PlcaProps":
        """
        AUTOSAR-compliant setter for plcaLocalNode with method chaining.

        Args:
            value: The plcaLocalNode to set

        Returns:
            self for method chaining

        Note:
            Delegates to plca_local_node property setter (gets validation automatically)
        """
        self.plca_local_node = value  # Delegates to property setter
        return self

    def getPlcaMaxBurst(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for plcaMaxBurst.

        Returns:
            The plcaMaxBurst value

        Note:
            Delegates to plca_max_burst property (CODING_RULE_V2_00017)
        """
        return self.plca_max_burst  # Delegates to property

    def setPlcaMaxBurst(self, value: "PositiveInteger") -> "PlcaProps":
        """
        AUTOSAR-compliant setter for plcaMaxBurst with method chaining.

        Args:
            value: The plcaMaxBurst to set

        Returns:
            self for method chaining

        Note:
            Delegates to plca_max_burst property setter (gets validation automatically)
        """
        self.plca_max_burst = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_plca_local_node(self, value: Optional["PositiveInteger"]) -> "PlcaProps":
        """
        Set plcaLocalNode and return self for chaining.

        Args:
            value: The plcaLocalNode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_plca_local_node("value")
        """
        self.plca_local_node = value  # Use property setter (gets validation)
        return self

    def with_plca_max_burst(self, value: Optional["PositiveInteger"]) -> "PlcaProps":
        """
        Set plcaMaxBurst and return self for chaining.

        Args:
            value: The plcaMaxBurst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_plca_max_burst("value")
        """
        self.plca_max_burst = value  # Use property setter (gets validation)
        return self
