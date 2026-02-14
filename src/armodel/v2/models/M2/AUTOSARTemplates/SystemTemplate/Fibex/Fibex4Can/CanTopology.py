"""
AUTOSAR Package - CanTopology

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology
"""


from __future__ import annotations

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    Integer,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationConnector,
    PhysicalChannel,
)


class J1939Cluster(ARObject):
    """
    J1939 specific cluster attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::J1939Cluster

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 321, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 78, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the network ID for the J1939 cluster.
        self._networkId: Optional[PositiveInteger] = None

    @property
    def network_id(self) -> Optional[PositiveInteger]:
        """Get networkId (Pythonic accessor)."""
        return self._networkId

    @network_id.setter
    def network_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set networkId with validation.

        Args:
            value: The networkId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._networkId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"networkId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._networkId = value
        # Enables support for the Request2 PGN (RQST2).
        self._request2Support: Optional[Boolean] = None

    @property
    def request2_support(self) -> Optional[Boolean]:
        """Get request2Support (Pythonic accessor)."""
        return self._request2Support

    @request2_support.setter
    def request2_support(self, value: Optional[Boolean]) -> None:
        """
        Set request2Support with validation.

        Args:
            value: The request2Support to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._request2Support = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"request2Support must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._request2Support = value
        # Defines whether the nodes attached to this channel use initial address claim,
                # and whether they react to claims of other nodes.
        # initial address claim is sent, and the node address claims of other nodes.
        # node only sends an address claim upon does not care for contending address
                # claims.
        self._usesAddressArbitration: Optional[Boolean] = None

    @property
    def uses_address_arbitration(self) -> Optional[Boolean]:
        """Get usesAddressArbitration (Pythonic accessor)."""
        return self._usesAddressArbitration

    @uses_address_arbitration.setter
    def uses_address_arbitration(self, value: Optional[Boolean]) -> None:
        """
        Set usesAddressArbitration with validation.

        Args:
            value: The usesAddressArbitration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usesAddressArbitration = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"usesAddressArbitration must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._usesAddressArbitration = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNetworkId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for networkId.

        Returns:
            The networkId value

        Note:
            Delegates to network_id property (CODING_RULE_V2_00017)
        """
        return self.network_id  # Delegates to property

    def setNetworkId(self, value: PositiveInteger) -> J1939Cluster:
        """
        AUTOSAR-compliant setter for networkId with method chaining.

        Args:
            value: The networkId to set

        Returns:
            self for method chaining

        Note:
            Delegates to network_id property setter (gets validation automatically)
        """
        self.network_id = value  # Delegates to property setter
        return self

    def getRequest2Support(self) -> Boolean:
        """
        AUTOSAR-compliant getter for request2Support.

        Returns:
            The request2Support value

        Note:
            Delegates to request2_support property (CODING_RULE_V2_00017)
        """
        return self.request2_support  # Delegates to property

    def setRequest2Support(self, value: Boolean) -> J1939Cluster:
        """
        AUTOSAR-compliant setter for request2Support with method chaining.

        Args:
            value: The request2Support to set

        Returns:
            self for method chaining

        Note:
            Delegates to request2_support property setter (gets validation automatically)
        """
        self.request2_support = value  # Delegates to property setter
        return self

    def getUsesAddressArbitration(self) -> Boolean:
        """
        AUTOSAR-compliant getter for usesAddressArbitration.

        Returns:
            The usesAddressArbitration value

        Note:
            Delegates to uses_address_arbitration property (CODING_RULE_V2_00017)
        """
        return self.uses_address_arbitration  # Delegates to property

    def setUsesAddressArbitration(self, value: Boolean) -> J1939Cluster:
        """
        AUTOSAR-compliant setter for usesAddressArbitration with method chaining.

        Args:
            value: The usesAddressArbitration to set

        Returns:
            self for method chaining

        Note:
            Delegates to uses_address_arbitration property setter (gets validation automatically)
        """
        self.uses_address_arbitration = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_network_id(self, value: Optional[PositiveInteger]) -> J1939Cluster:
        """
        Set networkId and return self for chaining.

        Args:
            value: The networkId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network_id("value")
        """
        self.network_id = value  # Use property setter (gets validation)
        return self

    def with_request2_support(self, value: Optional[Boolean]) -> J1939Cluster:
        """
        Set request2Support and return self for chaining.

        Args:
            value: The request2Support to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request2_support("value")
        """
        self.request2_support = value  # Use property setter (gets validation)
        return self

    def with_uses_address_arbitration(self, value: Optional[Boolean]) -> J1939Cluster:
        """
        Set usesAddressArbitration and return self for chaining.

        Args:
            value: The usesAddressArbitration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uses_address_arbitration("value")
        """
        self.uses_address_arbitration = value  # Use property setter (gets validation)
        return self



class AbstractCanCluster(ARObject, ABC):
    """
    Abstract class that is used to collect the common TtCAN, J1939 and CAN
    Cluster attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::AbstractCanCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 62, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCanCluster:
            raise TypeError("AbstractCanCluster is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CAN bus off monitoring / recovery at system level.
        self._busOffRecovery: Optional["CanClusterBusOff"] = None

    @property
    def bus_off_recovery(self) -> Optional["CanClusterBusOff"]:
        """Get busOffRecovery (Pythonic accessor)."""
        return self._busOffRecovery

    @bus_off_recovery.setter
    def bus_off_recovery(self, value: Optional["CanClusterBusOff"]) -> None:
        """
        Set busOffRecovery with validation.

        Args:
            value: The busOffRecovery to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._busOffRecovery = None
            return

        if not isinstance(value, CanClusterBusOff):
            raise TypeError(
                f"busOffRecovery must be CanClusterBusOff or None, got {type(value).__name__}"
            )
        self._busOffRecovery = value
        self._canFdBaudrate: Optional["PositiveUnlimitedInteger"] = None

    @property
    def can_fd_baudrate(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get canFdBaudrate (Pythonic accessor)."""
        return self._canFdBaudrate

    @can_fd_baudrate.setter
    def can_fd_baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set canFdBaudrate with validation.

        Args:
            value: The canFdBaudrate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canFdBaudrate = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"canFdBaudrate must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._canFdBaudrate = value
        self._canXlBaudrate: Optional["PositiveUnlimitedInteger"] = None

    @property
    def can_xl_baudrate(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get canXlBaudrate (Pythonic accessor)."""
        return self._canXlBaudrate

    @can_xl_baudrate.setter
    def can_xl_baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set canXlBaudrate with validation.

        Args:
            value: The canXlBaudrate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canXlBaudrate = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"canXlBaudrate must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._canXlBaudrate = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBusOffRecovery(self) -> "CanClusterBusOff":
        """
        AUTOSAR-compliant getter for busOffRecovery.

        Returns:
            The busOffRecovery value

        Note:
            Delegates to bus_off_recovery property (CODING_RULE_V2_00017)
        """
        return self.bus_off_recovery  # Delegates to property

    def setBusOffRecovery(self, value: "CanClusterBusOff") -> AbstractCanCluster:
        """
        AUTOSAR-compliant setter for busOffRecovery with method chaining.

        Args:
            value: The busOffRecovery to set

        Returns:
            self for method chaining

        Note:
            Delegates to bus_off_recovery property setter (gets validation automatically)
        """
        self.bus_off_recovery = value  # Delegates to property setter
        return self

    def getCanFdBaudrate(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for canFdBaudrate.

        Returns:
            The canFdBaudrate value

        Note:
            Delegates to can_fd_baudrate property (CODING_RULE_V2_00017)
        """
        return self.can_fd_baudrate  # Delegates to property

    def setCanFdBaudrate(self, value: "PositiveUnlimitedInteger") -> AbstractCanCluster:
        """
        AUTOSAR-compliant setter for canFdBaudrate with method chaining.

        Args:
            value: The canFdBaudrate to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_fd_baudrate property setter (gets validation automatically)
        """
        self.can_fd_baudrate = value  # Delegates to property setter
        return self

    def getCanXlBaudrate(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for canXlBaudrate.

        Returns:
            The canXlBaudrate value

        Note:
            Delegates to can_xl_baudrate property (CODING_RULE_V2_00017)
        """
        return self.can_xl_baudrate  # Delegates to property

    def setCanXlBaudrate(self, value: "PositiveUnlimitedInteger") -> AbstractCanCluster:
        """
        AUTOSAR-compliant setter for canXlBaudrate with method chaining.

        Args:
            value: The canXlBaudrate to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_xl_baudrate property setter (gets validation automatically)
        """
        self.can_xl_baudrate = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bus_off_recovery(self, value: Optional["CanClusterBusOff"]) -> AbstractCanCluster:
        """
        Set busOffRecovery and return self for chaining.

        Args:
            value: The busOffRecovery to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bus_off_recovery("value")
        """
        self.bus_off_recovery = value  # Use property setter (gets validation)
        return self

    def with_can_fd_baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> AbstractCanCluster:
        """
        Set canFdBaudrate and return self for chaining.

        Args:
            value: The canFdBaudrate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_fd_baudrate("value")
        """
        self.can_fd_baudrate = value  # Use property setter (gets validation)
        return self

    def with_can_xl_baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> AbstractCanCluster:
        """
        Set canXlBaudrate and return self for chaining.

        Args:
            value: The canXlBaudrate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_xl_baudrate("value")
        """
        self.can_xl_baudrate = value  # Use property setter (gets validation)
        return self



class CanCluster(ARObject):
    """
    CAN bus specific cluster attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 62, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CanClusterBusOffRecovery(ARObject):
    """
    This element contains the attributes that are used to configure the CAN bus
    off monitoring / recovery at system level.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanClusterBusOffRecovery

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 62, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This threshold defines the count of bus-offs until the recovery switches from
        # level 1 (short recovery level 2 (long recovery time).
        self._borCounterL1To: Optional[PositiveInteger] = None

    @property
    def bor_counter_l1_to(self) -> Optional[PositiveInteger]:
        """Get borCounterL1To (Pythonic accessor)."""
        return self._borCounterL1To

    @bor_counter_l1_to.setter
    def bor_counter_l1_to(self, value: Optional[PositiveInteger]) -> None:
        """
        Set borCounterL1To with validation.

        Args:
            value: The borCounterL1To to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._borCounterL1To = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"borCounterL1To must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._borCounterL1To = value
        # This attribute defines the duration of the bus-off recovery level 1 (short
                # recovery time) in seconds.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._borTimeL1: Optional["TimeValue"] = None

    @property
    def bor_time_l1(self) -> Optional["TimeValue"]:
        """Get borTimeL1 (Pythonic accessor)."""
        return self._borTimeL1

    @bor_time_l1.setter
    def bor_time_l1(self, value: Optional["TimeValue"]) -> None:
        """
        Set borTimeL1 with validation.

        Args:
            value: The borTimeL1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._borTimeL1 = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"borTimeL1 must be TimeValue or None, got {type(value).__name__}"
            )
        self._borTimeL1 = value
        # This attribute defines the duration of the bus-off recovery level 2 (long
        # recovery time) in seconds.
        self._borTimeL2: Optional["TimeValue"] = None

    @property
    def bor_time_l2(self) -> Optional["TimeValue"]:
        """Get borTimeL2 (Pythonic accessor)."""
        return self._borTimeL2

    @bor_time_l2.setter
    def bor_time_l2(self, value: Optional["TimeValue"]) -> None:
        """
        Set borTimeL2 with validation.

        Args:
            value: The borTimeL2 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._borTimeL2 = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"borTimeL2 must be TimeValue or None, got {type(value).__name__}"
            )
        self._borTimeL2 = value
        # This attribute defines the duration of the bus-off event in seconds.
        self._borTimeTx: Optional["TimeValue"] = None

    @property
    def bor_time_tx(self) -> Optional["TimeValue"]:
        """Get borTimeTx (Pythonic accessor)."""
        return self._borTimeTx

    @bor_time_tx.setter
    def bor_time_tx(self, value: Optional["TimeValue"]) -> None:
        """
        Set borTimeTx with validation.

        Args:
            value: The borTimeTx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._borTimeTx = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"borTimeTx must be TimeValue or None, got {type(value).__name__}"
            )
        self._borTimeTx = value
        self._mainFunction: Optional["TimeValue"] = None

    @property
    def main_function(self) -> Optional["TimeValue"]:
        """Get mainFunction (Pythonic accessor)."""
        return self._mainFunction

    @main_function.setter
    def main_function(self, value: Optional["TimeValue"]) -> None:
        """
        Set mainFunction with validation.

        Args:
            value: The mainFunction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mainFunction = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"mainFunction must be TimeValue or None, got {type(value).__name__}"
            )
        self._mainFunction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBorCounterL1To(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for borCounterL1To.

        Returns:
            The borCounterL1To value

        Note:
            Delegates to bor_counter_l1_to property (CODING_RULE_V2_00017)
        """
        return self.bor_counter_l1_to  # Delegates to property

    def setBorCounterL1To(self, value: PositiveInteger) -> CanClusterBusOffRecovery:
        """
        AUTOSAR-compliant setter for borCounterL1To with method chaining.

        Args:
            value: The borCounterL1To to set

        Returns:
            self for method chaining

        Note:
            Delegates to bor_counter_l1_to property setter (gets validation automatically)
        """
        self.bor_counter_l1_to = value  # Delegates to property setter
        return self

    def getBorTimeL1(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for borTimeL1.

        Returns:
            The borTimeL1 value

        Note:
            Delegates to bor_time_l1 property (CODING_RULE_V2_00017)
        """
        return self.bor_time_l1  # Delegates to property

    def setBorTimeL1(self, value: "TimeValue") -> CanClusterBusOffRecovery:
        """
        AUTOSAR-compliant setter for borTimeL1 with method chaining.

        Args:
            value: The borTimeL1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to bor_time_l1 property setter (gets validation automatically)
        """
        self.bor_time_l1 = value  # Delegates to property setter
        return self

    def getBorTimeL2(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for borTimeL2.

        Returns:
            The borTimeL2 value

        Note:
            Delegates to bor_time_l2 property (CODING_RULE_V2_00017)
        """
        return self.bor_time_l2  # Delegates to property

    def setBorTimeL2(self, value: "TimeValue") -> CanClusterBusOffRecovery:
        """
        AUTOSAR-compliant setter for borTimeL2 with method chaining.

        Args:
            value: The borTimeL2 to set

        Returns:
            self for method chaining

        Note:
            Delegates to bor_time_l2 property setter (gets validation automatically)
        """
        self.bor_time_l2 = value  # Delegates to property setter
        return self

    def getBorTimeTx(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for borTimeTx.

        Returns:
            The borTimeTx value

        Note:
            Delegates to bor_time_tx property (CODING_RULE_V2_00017)
        """
        return self.bor_time_tx  # Delegates to property

    def setBorTimeTx(self, value: "TimeValue") -> CanClusterBusOffRecovery:
        """
        AUTOSAR-compliant setter for borTimeTx with method chaining.

        Args:
            value: The borTimeTx to set

        Returns:
            self for method chaining

        Note:
            Delegates to bor_time_tx property setter (gets validation automatically)
        """
        self.bor_time_tx = value  # Delegates to property setter
        return self

    def getMainFunction(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for mainFunction.

        Returns:
            The mainFunction value

        Note:
            Delegates to main_function property (CODING_RULE_V2_00017)
        """
        return self.main_function  # Delegates to property

    def setMainFunction(self, value: "TimeValue") -> CanClusterBusOffRecovery:
        """
        AUTOSAR-compliant setter for mainFunction with method chaining.

        Args:
            value: The mainFunction to set

        Returns:
            self for method chaining

        Note:
            Delegates to main_function property setter (gets validation automatically)
        """
        self.main_function = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bor_counter_l1_to(self, value: Optional[PositiveInteger]) -> CanClusterBusOffRecovery:
        """
        Set borCounterL1To and return self for chaining.

        Args:
            value: The borCounterL1To to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bor_counter_l1_to("value")
        """
        self.bor_counter_l1_to = value  # Use property setter (gets validation)
        return self

    def with_bor_time_l1(self, value: Optional["TimeValue"]) -> CanClusterBusOffRecovery:
        """
        Set borTimeL1 and return self for chaining.

        Args:
            value: The borTimeL1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bor_time_l1("value")
        """
        self.bor_time_l1 = value  # Use property setter (gets validation)
        return self

    def with_bor_time_l2(self, value: Optional["TimeValue"]) -> CanClusterBusOffRecovery:
        """
        Set borTimeL2 and return self for chaining.

        Args:
            value: The borTimeL2 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bor_time_l2("value")
        """
        self.bor_time_l2 = value  # Use property setter (gets validation)
        return self

    def with_bor_time_tx(self, value: Optional["TimeValue"]) -> CanClusterBusOffRecovery:
        """
        Set borTimeTx and return self for chaining.

        Args:
            value: The borTimeTx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bor_time_tx("value")
        """
        self.bor_time_tx = value  # Use property setter (gets validation)
        return self

    def with_main_function(self, value: Optional["TimeValue"]) -> CanClusterBusOffRecovery:
        """
        Set mainFunction and return self for chaining.

        Args:
            value: The mainFunction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_main_function("value")
        """
        self.main_function = value  # Use property setter (gets validation)
        return self



class CanCommunicationController(ARObject):
    """
    CAN bus specific communication port attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanCommunicationController

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 63, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AbstractCanCommunicationController(ARObject, ABC):
    """
    Abstract class that is used to collect the common TtCAN and CAN Controller
    attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::AbstractCanCommunicationController

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 63, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCanCommunicationController:
            raise TypeError("AbstractCanCommunicationController is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CAN Bit Timing configuration.
        self._canControllerControllerAttributes: Optional[AbstractCanPhysicalChannel] = None

    @property
    def can_controller_controller_attributes(self) -> Optional[AbstractCanPhysicalChannel]:
        """Get canControllerControllerAttributes (Pythonic accessor)."""
        return self._canControllerControllerAttributes

    @can_controller_controller_attributes.setter
    def can_controller_controller_attributes(self, value: Optional[AbstractCanPhysicalChannel]) -> None:
        """
        Set canControllerControllerAttributes with validation.

        Args:
            value: The canControllerControllerAttributes to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canControllerControllerAttributes = None
            return

        if not isinstance(value, AbstractCan):
            raise TypeError(
                f"canControllerControllerAttributes must be AbstractCan or None, got {type(value).__name__}"
            )
        self._canControllerControllerAttributes = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCanControllerControllerAttributes(self) -> AbstractCanPhysicalChannel:
        """
        AUTOSAR-compliant getter for canControllerControllerAttributes.

        Returns:
            The canControllerControllerAttributes value

        Note:
            Delegates to can_controller_controller_attributes property (CODING_RULE_V2_00017)
        """
        return self.can_controller_controller_attributes  # Delegates to property

    def setCanControllerControllerAttributes(self, value: AbstractCanPhysicalChannel) -> AbstractCanCommunicationController:
        """
        AUTOSAR-compliant setter for canControllerControllerAttributes with method chaining.

        Args:
            value: The canControllerControllerAttributes to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_controller_controller_attributes property setter (gets validation automatically)
        """
        self.can_controller_controller_attributes = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_can_controller_controller_attributes(self, value: Optional[AbstractCanPhysicalChannel]) -> AbstractCanCommunicationController:
        """
        Set canControllerControllerAttributes and return self for chaining.

        Args:
            value: The canControllerControllerAttributes to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_controller_controller_attributes("value")
        """
        self.can_controller_controller_attributes = value  # Use property setter (gets validation)
        return self



class AbstractCanCommunicationControllerAttributes(ARObject, ABC):
    """
    For the configuration of the CanController parameters two different
    approaches can be used: 1. Providing exact values which are taken by the ECU
    developer (CanControllerConfiguration). 2. Providing ranges of values which
    are taken as requirements and have to be respected by the ECU developer
    (CanControllerConfigurationRequirements).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::AbstractCanCommunicationControllerAttributes

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 64, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCanCommunicationControllerAttributes:
            raise TypeError("AbstractCanCommunicationControllerAttributes is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Additional CanFD ranges of the bit timing related configuration of a CanFD
                # controller.
        # If this element exists controller supports CanFD frames and the ECU take
                # these ranges as requirements for the the CanFD controller.
        self._canControllerFd: Optional["CanControllerFd"] = None

    @property
    def can_controller_fd(self) -> Optional["CanControllerFd"]:
        """Get canControllerFd (Pythonic accessor)."""
        return self._canControllerFd

    @can_controller_fd.setter
    def can_controller_fd(self, value: Optional["CanControllerFd"]) -> None:
        """
        Set canControllerFd with validation.

        Args:
            value: The canControllerFd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canControllerFd = None
            return

        if not isinstance(value, CanControllerFd):
            raise TypeError(
                f"canControllerFd must be CanControllerFd or None, got {type(value).__name__}"
            )
        self._canControllerFd = value
                # controller.
        # If this element exists controller supports CanXL frames and the ECU take
                # these ranges as requirements for the the CanXL controller.
        self._canControllerXl: Optional["CanControllerXl"] = None

    @property
    def can_controller_xl(self) -> Optional["CanControllerXl"]:
        """Get canControllerXl (Pythonic accessor)."""
        return self._canControllerXl

    @can_controller_xl.setter
    def can_controller_xl(self, value: Optional["CanControllerXl"]) -> None:
        """
        Set canControllerXl with validation.

        Args:
            value: The canControllerXl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canControllerXl = None
            return

        if not isinstance(value, CanControllerXl):
            raise TypeError(
                f"canControllerXl must be CanControllerXl or None, got {type(value).__name__}"
            )
        self._canControllerXl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCanControllerFd(self) -> "CanControllerFd":
        """
        AUTOSAR-compliant getter for canControllerFd.

        Returns:
            The canControllerFd value

        Note:
            Delegates to can_controller_fd property (CODING_RULE_V2_00017)
        """
        return self.can_controller_fd  # Delegates to property

    def setCanControllerFd(self, value: "CanControllerFd") -> AbstractCanCommunicationControllerAttributes:
        """
        AUTOSAR-compliant setter for canControllerFd with method chaining.

        Args:
            value: The canControllerFd to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_controller_fd property setter (gets validation automatically)
        """
        self.can_controller_fd = value  # Delegates to property setter
        return self

    def getCanControllerXl(self) -> "CanControllerXl":
        """
        AUTOSAR-compliant getter for canControllerXl.

        Returns:
            The canControllerXl value

        Note:
            Delegates to can_controller_xl property (CODING_RULE_V2_00017)
        """
        return self.can_controller_xl  # Delegates to property

    def setCanControllerXl(self, value: "CanControllerXl") -> AbstractCanCommunicationControllerAttributes:
        """
        AUTOSAR-compliant setter for canControllerXl with method chaining.

        Args:
            value: The canControllerXl to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_controller_xl property setter (gets validation automatically)
        """
        self.can_controller_xl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_can_controller_fd(self, value: Optional["CanControllerFd"]) -> AbstractCanCommunicationControllerAttributes:
        """
        Set canControllerFd and return self for chaining.

        Args:
            value: The canControllerFd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_controller_fd("value")
        """
        self.can_controller_fd = value  # Use property setter (gets validation)
        return self

    def with_can_controller_xl(self, value: Optional["CanControllerXl"]) -> AbstractCanCommunicationControllerAttributes:
        """
        Set canControllerXl and return self for chaining.

        Args:
            value: The canControllerXl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_controller_xl("value")
        """
        self.can_controller_xl = value  # Use property setter (gets validation)
        return self



class CanControllerFdConfiguration(ARObject):
    """
    Bit timing related configuration of a CAN controller for payload and CRC of
    a CAN FD frame.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanControllerFdConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 66, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the value which is used to pad unused data in frames which are
        # bigger than 8 byte if the length Pdu which was requested to be sent does not
        # match DLC values of CAN FD.
        self._paddingValue: Optional[PositiveInteger] = None

    @property
    def padding_value(self) -> Optional[PositiveInteger]:
        """Get paddingValue (Pythonic accessor)."""
        return self._paddingValue

    @padding_value.setter
    def padding_value(self, value: Optional[PositiveInteger]) -> None:
        """
        Set paddingValue with validation.

        Args:
            value: The paddingValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._paddingValue = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"paddingValue must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._paddingValue = value
        self._propSeg: Optional[PositiveInteger] = None

    @property
    def prop_seg(self) -> Optional[PositiveInteger]:
        """Get propSeg (Pythonic accessor)."""
        return self._propSeg

    @prop_seg.setter
    def prop_seg(self, value: Optional[PositiveInteger]) -> None:
        """
        Set propSeg with validation.

        Args:
            value: The propSeg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._propSeg = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"propSeg must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._propSeg = value
        # Transmitter Delay Compensation used to adjust the position of the Secondary
                # (SSP), relative to the beginning of the If this parameter is configured, the
                # Compensation is done by the CAN controller.
        # If not specified Compensation is disabled.
        self._sspOffset: Optional[PositiveInteger] = None

    @property
    def ssp_offset(self) -> Optional[PositiveInteger]:
        """Get sspOffset (Pythonic accessor)."""
        return self._sspOffset

    @ssp_offset.setter
    def ssp_offset(self, value: Optional[PositiveInteger]) -> None:
        """
        Set sspOffset with validation.

        Args:
            value: The sspOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sspOffset = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sspOffset must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sspOffset = value
        self._syncJumpWidth: Optional[PositiveInteger] = None

    @property
    def sync_jump_width(self) -> Optional[PositiveInteger]:
        """Get syncJumpWidth (Pythonic accessor)."""
        return self._syncJumpWidth

    @sync_jump_width.setter
    def sync_jump_width(self, value: Optional[PositiveInteger]) -> None:
        """
        Set syncJumpWidth with validation.

        Args:
            value: The syncJumpWidth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncJumpWidth = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"syncJumpWidth must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._syncJumpWidth = value
        self._timeSeg1: Optional[PositiveInteger] = None

    @property
    def time_seg1(self) -> Optional[PositiveInteger]:
        """Get timeSeg1 (Pythonic accessor)."""
        return self._timeSeg1

    @time_seg1.setter
    def time_seg1(self, value: Optional[PositiveInteger]) -> None:
        """
        Set timeSeg1 with validation.

        Args:
            value: The timeSeg1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSeg1 = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"timeSeg1 must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._timeSeg1 = value
        # Specifies phase segment 2 in time quantas.
        self._timeSeg2: Optional[PositiveInteger] = None

    @property
    def time_seg2(self) -> Optional[PositiveInteger]:
        """Get timeSeg2 (Pythonic accessor)."""
        return self._timeSeg2

    @time_seg2.setter
    def time_seg2(self, value: Optional[PositiveInteger]) -> None:
        """
        Set timeSeg2 with validation.

        Args:
            value: The timeSeg2 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSeg2 = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"timeSeg2 must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._timeSeg2 = value
        # Specifies if the bit rate switching shall be used for FD frames shall be sent
        # with bit rate FD frames shall be sent without bit rate.
        self._txBitRateSwitch: Optional[Boolean] = None

    @property
    def tx_bit_rate_switch(self) -> Optional[Boolean]:
        """Get txBitRateSwitch (Pythonic accessor)."""
        return self._txBitRateSwitch

    @tx_bit_rate_switch.setter
    def tx_bit_rate_switch(self, value: Optional[Boolean]) -> None:
        """
        Set txBitRateSwitch with validation.

        Args:
            value: The txBitRateSwitch to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._txBitRateSwitch = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"txBitRateSwitch must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._txBitRateSwitch = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPaddingValue(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for paddingValue.

        Returns:
            The paddingValue value

        Note:
            Delegates to padding_value property (CODING_RULE_V2_00017)
        """
        return self.padding_value  # Delegates to property

    def setPaddingValue(self, value: PositiveInteger) -> CanControllerFdConfiguration:
        """
        AUTOSAR-compliant setter for paddingValue with method chaining.

        Args:
            value: The paddingValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to padding_value property setter (gets validation automatically)
        """
        self.padding_value = value  # Delegates to property setter
        return self

    def getPropSeg(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for propSeg.

        Returns:
            The propSeg value

        Note:
            Delegates to prop_seg property (CODING_RULE_V2_00017)
        """
        return self.prop_seg  # Delegates to property

    def setPropSeg(self, value: PositiveInteger) -> CanControllerFdConfiguration:
        """
        AUTOSAR-compliant setter for propSeg with method chaining.

        Args:
            value: The propSeg to set

        Returns:
            self for method chaining

        Note:
            Delegates to prop_seg property setter (gets validation automatically)
        """
        self.prop_seg = value  # Delegates to property setter
        return self

    def getSspOffset(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for sspOffset.

        Returns:
            The sspOffset value

        Note:
            Delegates to ssp_offset property (CODING_RULE_V2_00017)
        """
        return self.ssp_offset  # Delegates to property

    def setSspOffset(self, value: PositiveInteger) -> CanControllerFdConfiguration:
        """
        AUTOSAR-compliant setter for sspOffset with method chaining.

        Args:
            value: The sspOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to ssp_offset property setter (gets validation automatically)
        """
        self.ssp_offset = value  # Delegates to property setter
        return self

    def getSyncJumpWidth(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for syncJumpWidth.

        Returns:
            The syncJumpWidth value

        Note:
            Delegates to sync_jump_width property (CODING_RULE_V2_00017)
        """
        return self.sync_jump_width  # Delegates to property

    def setSyncJumpWidth(self, value: PositiveInteger) -> CanControllerFdConfiguration:
        """
        AUTOSAR-compliant setter for syncJumpWidth with method chaining.

        Args:
            value: The syncJumpWidth to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_jump_width property setter (gets validation automatically)
        """
        self.sync_jump_width = value  # Delegates to property setter
        return self

    def getTimeSeg1(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for timeSeg1.

        Returns:
            The timeSeg1 value

        Note:
            Delegates to time_seg1 property (CODING_RULE_V2_00017)
        """
        return self.time_seg1  # Delegates to property

    def setTimeSeg1(self, value: PositiveInteger) -> CanControllerFdConfiguration:
        """
        AUTOSAR-compliant setter for timeSeg1 with method chaining.

        Args:
            value: The timeSeg1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_seg1 property setter (gets validation automatically)
        """
        self.time_seg1 = value  # Delegates to property setter
        return self

    def getTimeSeg2(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for timeSeg2.

        Returns:
            The timeSeg2 value

        Note:
            Delegates to time_seg2 property (CODING_RULE_V2_00017)
        """
        return self.time_seg2  # Delegates to property

    def setTimeSeg2(self, value: PositiveInteger) -> CanControllerFdConfiguration:
        """
        AUTOSAR-compliant setter for timeSeg2 with method chaining.

        Args:
            value: The timeSeg2 to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_seg2 property setter (gets validation automatically)
        """
        self.time_seg2 = value  # Delegates to property setter
        return self

    def getTxBitRateSwitch(self) -> Boolean:
        """
        AUTOSAR-compliant getter for txBitRateSwitch.

        Returns:
            The txBitRateSwitch value

        Note:
            Delegates to tx_bit_rate_switch property (CODING_RULE_V2_00017)
        """
        return self.tx_bit_rate_switch  # Delegates to property

    def setTxBitRateSwitch(self, value: Boolean) -> CanControllerFdConfiguration:
        """
        AUTOSAR-compliant setter for txBitRateSwitch with method chaining.

        Args:
            value: The txBitRateSwitch to set

        Returns:
            self for method chaining

        Note:
            Delegates to tx_bit_rate_switch property setter (gets validation automatically)
        """
        self.tx_bit_rate_switch = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_padding_value(self, value: Optional[PositiveInteger]) -> CanControllerFdConfiguration:
        """
        Set paddingValue and return self for chaining.

        Args:
            value: The paddingValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_padding_value("value")
        """
        self.padding_value = value  # Use property setter (gets validation)
        return self

    def with_prop_seg(self, value: Optional[PositiveInteger]) -> CanControllerFdConfiguration:
        """
        Set propSeg and return self for chaining.

        Args:
            value: The propSeg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prop_seg("value")
        """
        self.prop_seg = value  # Use property setter (gets validation)
        return self

    def with_ssp_offset(self, value: Optional[PositiveInteger]) -> CanControllerFdConfiguration:
        """
        Set sspOffset and return self for chaining.

        Args:
            value: The sspOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ssp_offset("value")
        """
        self.ssp_offset = value  # Use property setter (gets validation)
        return self

    def with_sync_jump_width(self, value: Optional[PositiveInteger]) -> CanControllerFdConfiguration:
        """
        Set syncJumpWidth and return self for chaining.

        Args:
            value: The syncJumpWidth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_jump_width("value")
        """
        self.sync_jump_width = value  # Use property setter (gets validation)
        return self

    def with_time_seg1(self, value: Optional[PositiveInteger]) -> CanControllerFdConfiguration:
        """
        Set timeSeg1 and return self for chaining.

        Args:
            value: The timeSeg1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_seg1("value")
        """
        self.time_seg1 = value  # Use property setter (gets validation)
        return self

    def with_time_seg2(self, value: Optional[PositiveInteger]) -> CanControllerFdConfiguration:
        """
        Set timeSeg2 and return self for chaining.

        Args:
            value: The timeSeg2 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_seg2("value")
        """
        self.time_seg2 = value  # Use property setter (gets validation)
        return self

    def with_tx_bit_rate_switch(self, value: Optional[Boolean]) -> CanControllerFdConfiguration:
        """
        Set txBitRateSwitch and return self for chaining.

        Args:
            value: The txBitRateSwitch to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tx_bit_rate_switch("value")
        """
        self.tx_bit_rate_switch = value  # Use property setter (gets validation)
        return self



class CanControllerFdConfigurationRequirements(ARObject):
    """
    This element allows the specification of ranges for the CanFD bit timing
    configuration parameters. These ranges are taken as requirements and shall
    be respected by the ECU developer.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanControllerFdConfigurationRequirements

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 66, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum number of time quanta in the bit time.
        self._maxNumberOfTimeQuantaPerBit: Optional[Integer] = None

    @property
    def max_number_of_time_quanta_per_bit(self) -> Optional[Integer]:
        """Get maxNumberOfTimeQuantaPerBit (Pythonic accessor)."""
        return self._maxNumberOfTimeQuantaPerBit

    @max_number_of_time_quanta_per_bit.setter
    def max_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> None:
        """
        Set maxNumberOfTimeQuantaPerBit with validation.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOfTimeQuantaPerBit = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxNumberOfTimeQuantaPerBit must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxNumberOfTimeQuantaPerBit = value
        # value of the sample point as a percentage of total bit time.
        self._maxSample: Optional[Float] = None

    @property
    def max_sample(self) -> Optional[Float]:
        """Get maxSample (Pythonic accessor)."""
        return self._maxSample

    @max_sample.setter
    def max_sample(self, value: Optional[Float]) -> None:
        """
        Set maxSample with validation.

        Args:
            value: The maxSample to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSample = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"maxSample must be Float or float or None, got {type(value).__name__}"
            )
        self._maxSample = value
        # Synchronization Jump Width value as a of the total bit time.
        # The (Re-)Synchronization (SJW) defines how far a resynchronization the Sample
                # Point inside the limits defined by Buffer Segments to compensate for edge.
        self._maxSyncJump: Optional[Float] = None

    @property
    def max_sync_jump(self) -> Optional[Float]:
        """Get maxSyncJump (Pythonic accessor)."""
        return self._maxSyncJump

    @max_sync_jump.setter
    def max_sync_jump(self, value: Optional[Float]) -> None:
        """
        Set maxSyncJump with validation.

        Args:
            value: The maxSyncJump to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSyncJump = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"maxSyncJump must be Float or float or None, got {type(value).__name__}"
            )
        self._maxSyncJump = value
        # If not specified Transceiver Delay is disabled.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maxTrcvDelay: Optional["TimeValue"] = None

    @property
    def max_trcv_delay(self) -> Optional["TimeValue"]:
        """Get maxTrcvDelay (Pythonic accessor)."""
        return self._maxTrcvDelay

    @max_trcv_delay.setter
    def max_trcv_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set maxTrcvDelay with validation.

        Args:
            value: The maxTrcvDelay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxTrcvDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"maxTrcvDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._maxTrcvDelay = value
        self._minNumberOfTimeQuantaPerBit: Optional[Integer] = None

    @property
    def min_number_of_time_quanta_per_bit(self) -> Optional[Integer]:
        """Get minNumberOfTimeQuantaPerBit (Pythonic accessor)."""
        return self._minNumberOfTimeQuantaPerBit

    @min_number_of_time_quanta_per_bit.setter
    def min_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> None:
        """
        Set minNumberOfTimeQuantaPerBit with validation.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minNumberOfTimeQuantaPerBit = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"minNumberOfTimeQuantaPerBit must be Integer or int or None, got {type(value).__name__}"
            )
        self._minNumberOfTimeQuantaPerBit = value
        # value of the sample point as a percentage of the time.
        self._minSamplePoint: Optional[Float] = None

    @property
    def min_sample_point(self) -> Optional[Float]:
        """Get minSamplePoint (Pythonic accessor)."""
        return self._minSamplePoint

    @min_sample_point.setter
    def min_sample_point(self, value: Optional[Float]) -> None:
        """
        Set minSamplePoint with validation.

        Args:
            value: The minSamplePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minSamplePoint = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"minSamplePoint must be Float or float or None, got {type(value).__name__}"
            )
        self._minSamplePoint = value
        # Synchronization Jump Width value as a of the total bit time.
        # The (Re-)Synchronization (SJW) defines how far a resynchronization the Sample
                # Point inside the limits defined by Buffer Segments to compensate for edge.
        self._minSyncJump: Optional[Float] = None

    @property
    def min_sync_jump(self) -> Optional[Float]:
        """Get minSyncJump (Pythonic accessor)."""
        return self._minSyncJump

    @min_sync_jump.setter
    def min_sync_jump(self, value: Optional[Float]) -> None:
        """
        Set minSyncJump with validation.

        Args:
            value: The minSyncJump to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minSyncJump = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"minSyncJump must be Float or float or None, got {type(value).__name__}"
            )
        self._minSyncJump = value
        # If not specified Transceiver Delay is disabled.
        self._minTrcvDelay: Optional["TimeValue"] = None

    @property
    def min_trcv_delay(self) -> Optional["TimeValue"]:
        """Get minTrcvDelay (Pythonic accessor)."""
        return self._minTrcvDelay

    @min_trcv_delay.setter
    def min_trcv_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set minTrcvDelay with validation.

        Args:
            value: The minTrcvDelay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minTrcvDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minTrcvDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._minTrcvDelay = value
        # bigger than 8 byte if the length Pdu which was requested to be sent does not
        # match DLC values of CAN FD.
        self._paddingValue: Optional[PositiveInteger] = None

    @property
    def padding_value(self) -> Optional[PositiveInteger]:
        """Get paddingValue (Pythonic accessor)."""
        return self._paddingValue

    @padding_value.setter
    def padding_value(self, value: Optional[PositiveInteger]) -> None:
        """
        Set paddingValue with validation.

        Args:
            value: The paddingValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._paddingValue = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"paddingValue must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._paddingValue = value
        # with bit rate FD frames shall be sent without bit rate.
        self._txBitRateSwitch: Optional[Boolean] = None

    @property
    def tx_bit_rate_switch(self) -> Optional[Boolean]:
        """Get txBitRateSwitch (Pythonic accessor)."""
        return self._txBitRateSwitch

    @tx_bit_rate_switch.setter
    def tx_bit_rate_switch(self, value: Optional[Boolean]) -> None:
        """
        Set txBitRateSwitch with validation.

        Args:
            value: The txBitRateSwitch to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._txBitRateSwitch = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"txBitRateSwitch must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._txBitRateSwitch = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxNumberOfTimeQuantaPerBit(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxNumberOfTimeQuantaPerBit.

        Returns:
            The maxNumberOfTimeQuantaPerBit value

        Note:
            Delegates to max_number_of_time_quanta_per_bit property (CODING_RULE_V2_00017)
        """
        return self.max_number_of_time_quanta_per_bit  # Delegates to property

    def setMaxNumberOfTimeQuantaPerBit(self, value: Integer) -> CanControllerFdConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxNumberOfTimeQuantaPerBit with method chaining.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of_time_quanta_per_bit property setter (gets validation automatically)
        """
        self.max_number_of_time_quanta_per_bit = value  # Delegates to property setter
        return self

    def getMaxSample(self) -> Float:
        """
        AUTOSAR-compliant getter for maxSample.

        Returns:
            The maxSample value

        Note:
            Delegates to max_sample property (CODING_RULE_V2_00017)
        """
        return self.max_sample  # Delegates to property

    def setMaxSample(self, value: Float) -> CanControllerFdConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxSample with method chaining.

        Args:
            value: The maxSample to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_sample property setter (gets validation automatically)
        """
        self.max_sample = value  # Delegates to property setter
        return self

    def getMaxSyncJump(self) -> Float:
        """
        AUTOSAR-compliant getter for maxSyncJump.

        Returns:
            The maxSyncJump value

        Note:
            Delegates to max_sync_jump property (CODING_RULE_V2_00017)
        """
        return self.max_sync_jump  # Delegates to property

    def setMaxSyncJump(self, value: Float) -> CanControllerFdConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxSyncJump with method chaining.

        Args:
            value: The maxSyncJump to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_sync_jump property setter (gets validation automatically)
        """
        self.max_sync_jump = value  # Delegates to property setter
        return self

    def getMaxTrcvDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for maxTrcvDelay.

        Returns:
            The maxTrcvDelay value

        Note:
            Delegates to max_trcv_delay property (CODING_RULE_V2_00017)
        """
        return self.max_trcv_delay  # Delegates to property

    def setMaxTrcvDelay(self, value: "TimeValue") -> CanControllerFdConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxTrcvDelay with method chaining.

        Args:
            value: The maxTrcvDelay to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_trcv_delay property setter (gets validation automatically)
        """
        self.max_trcv_delay = value  # Delegates to property setter
        return self

    def getMinNumberOfTimeQuantaPerBit(self) -> Integer:
        """
        AUTOSAR-compliant getter for minNumberOfTimeQuantaPerBit.

        Returns:
            The minNumberOfTimeQuantaPerBit value

        Note:
            Delegates to min_number_of_time_quanta_per_bit property (CODING_RULE_V2_00017)
        """
        return self.min_number_of_time_quanta_per_bit  # Delegates to property

    def setMinNumberOfTimeQuantaPerBit(self, value: Integer) -> CanControllerFdConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minNumberOfTimeQuantaPerBit with method chaining.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_number_of_time_quanta_per_bit property setter (gets validation automatically)
        """
        self.min_number_of_time_quanta_per_bit = value  # Delegates to property setter
        return self

    def getMinSamplePoint(self) -> Float:
        """
        AUTOSAR-compliant getter for minSamplePoint.

        Returns:
            The minSamplePoint value

        Note:
            Delegates to min_sample_point property (CODING_RULE_V2_00017)
        """
        return self.min_sample_point  # Delegates to property

    def setMinSamplePoint(self, value: Float) -> CanControllerFdConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minSamplePoint with method chaining.

        Args:
            value: The minSamplePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_sample_point property setter (gets validation automatically)
        """
        self.min_sample_point = value  # Delegates to property setter
        return self

    def getMinSyncJump(self) -> Float:
        """
        AUTOSAR-compliant getter for minSyncJump.

        Returns:
            The minSyncJump value

        Note:
            Delegates to min_sync_jump property (CODING_RULE_V2_00017)
        """
        return self.min_sync_jump  # Delegates to property

    def setMinSyncJump(self, value: Float) -> CanControllerFdConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minSyncJump with method chaining.

        Args:
            value: The minSyncJump to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_sync_jump property setter (gets validation automatically)
        """
        self.min_sync_jump = value  # Delegates to property setter
        return self

    def getMinTrcvDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minTrcvDelay.

        Returns:
            The minTrcvDelay value

        Note:
            Delegates to min_trcv_delay property (CODING_RULE_V2_00017)
        """
        return self.min_trcv_delay  # Delegates to property

    def setMinTrcvDelay(self, value: "TimeValue") -> CanControllerFdConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minTrcvDelay with method chaining.

        Args:
            value: The minTrcvDelay to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_trcv_delay property setter (gets validation automatically)
        """
        self.min_trcv_delay = value  # Delegates to property setter
        return self

    def getPaddingValue(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for paddingValue.

        Returns:
            The paddingValue value

        Note:
            Delegates to padding_value property (CODING_RULE_V2_00017)
        """
        return self.padding_value  # Delegates to property

    def setPaddingValue(self, value: PositiveInteger) -> CanControllerFdConfigurationRequirements:
        """
        AUTOSAR-compliant setter for paddingValue with method chaining.

        Args:
            value: The paddingValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to padding_value property setter (gets validation automatically)
        """
        self.padding_value = value  # Delegates to property setter
        return self

    def getTxBitRateSwitch(self) -> Boolean:
        """
        AUTOSAR-compliant getter for txBitRateSwitch.

        Returns:
            The txBitRateSwitch value

        Note:
            Delegates to tx_bit_rate_switch property (CODING_RULE_V2_00017)
        """
        return self.tx_bit_rate_switch  # Delegates to property

    def setTxBitRateSwitch(self, value: Boolean) -> CanControllerFdConfigurationRequirements:
        """
        AUTOSAR-compliant setter for txBitRateSwitch with method chaining.

        Args:
            value: The txBitRateSwitch to set

        Returns:
            self for method chaining

        Note:
            Delegates to tx_bit_rate_switch property setter (gets validation automatically)
        """
        self.tx_bit_rate_switch = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> CanControllerFdConfigurationRequirements:
        """
        Set maxNumberOfTimeQuantaPerBit and return self for chaining.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of_time_quanta_per_bit("value")
        """
        self.max_number_of_time_quanta_per_bit = value  # Use property setter (gets validation)
        return self

    def with_max_sample(self, value: Optional[Float]) -> CanControllerFdConfigurationRequirements:
        """
        Set maxSample and return self for chaining.

        Args:
            value: The maxSample to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_sample("value")
        """
        self.max_sample = value  # Use property setter (gets validation)
        return self

    def with_max_sync_jump(self, value: Optional[Float]) -> CanControllerFdConfigurationRequirements:
        """
        Set maxSyncJump and return self for chaining.

        Args:
            value: The maxSyncJump to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_sync_jump("value")
        """
        self.max_sync_jump = value  # Use property setter (gets validation)
        return self

    def with_max_trcv_delay(self, value: Optional["TimeValue"]) -> CanControllerFdConfigurationRequirements:
        """
        Set maxTrcvDelay and return self for chaining.

        Args:
            value: The maxTrcvDelay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_trcv_delay("value")
        """
        self.max_trcv_delay = value  # Use property setter (gets validation)
        return self

    def with_min_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> CanControllerFdConfigurationRequirements:
        """
        Set minNumberOfTimeQuantaPerBit and return self for chaining.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_number_of_time_quanta_per_bit("value")
        """
        self.min_number_of_time_quanta_per_bit = value  # Use property setter (gets validation)
        return self

    def with_min_sample_point(self, value: Optional[Float]) -> CanControllerFdConfigurationRequirements:
        """
        Set minSamplePoint and return self for chaining.

        Args:
            value: The minSamplePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_sample_point("value")
        """
        self.min_sample_point = value  # Use property setter (gets validation)
        return self

    def with_min_sync_jump(self, value: Optional[Float]) -> CanControllerFdConfigurationRequirements:
        """
        Set minSyncJump and return self for chaining.

        Args:
            value: The minSyncJump to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_sync_jump("value")
        """
        self.min_sync_jump = value  # Use property setter (gets validation)
        return self

    def with_min_trcv_delay(self, value: Optional["TimeValue"]) -> CanControllerFdConfigurationRequirements:
        """
        Set minTrcvDelay and return self for chaining.

        Args:
            value: The minTrcvDelay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_trcv_delay("value")
        """
        self.min_trcv_delay = value  # Use property setter (gets validation)
        return self

    def with_padding_value(self, value: Optional[PositiveInteger]) -> CanControllerFdConfigurationRequirements:
        """
        Set paddingValue and return self for chaining.

        Args:
            value: The paddingValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_padding_value("value")
        """
        self.padding_value = value  # Use property setter (gets validation)
        return self

    def with_tx_bit_rate_switch(self, value: Optional[Boolean]) -> CanControllerFdConfigurationRequirements:
        """
        Set txBitRateSwitch and return self for chaining.

        Args:
            value: The txBitRateSwitch to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tx_bit_rate_switch("value")
        """
        self.tx_bit_rate_switch = value  # Use property setter (gets validation)
        return self



class CanControllerXlConfiguration(ARObject):
    """
    This meta-class represents the CAN XL-specific controller attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanControllerXlConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 70, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies if error signaling shall be enabled.
        # This is not when the transceiver is switched to PWM mode to TRUE).
        # signaling shall be enabled.
        # signaling shall be disabled.
        self._errorSignaling: Optional[Boolean] = None

    @property
    def error_signaling(self) -> Optional[Boolean]:
        """Get errorSignaling (Pythonic accessor)."""
        return self._errorSignaling

    @error_signaling.setter
    def error_signaling(self, value: Optional[Boolean]) -> None:
        """
        Set errorSignaling with validation.

        Args:
            value: The errorSignaling to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._errorSignaling = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"errorSignaling must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._errorSignaling = value
        self._propSeg: Optional[PositiveInteger] = None

    @property
    def prop_seg(self) -> Optional[PositiveInteger]:
        """Get propSeg (Pythonic accessor)."""
        return self._propSeg

    @prop_seg.setter
    def prop_seg(self, value: Optional[PositiveInteger]) -> None:
        """
        Set propSeg with validation.

        Args:
            value: The propSeg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._propSeg = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"propSeg must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._propSeg = value
        self._pwmL: Optional[PositiveInteger] = None

    @property
    def pwm_l(self) -> Optional[PositiveInteger]:
        """Get pwmL (Pythonic accessor)."""
        return self._pwmL

    @pwm_l.setter
    def pwm_l(self, value: Optional[PositiveInteger]) -> None:
        """
        Set pwmL with validation.

        Args:
            value: The pwmL to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pwmL = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pwmL must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pwmL = value
        self._pwmO: Optional[PositiveInteger] = None

    @property
    def pwm_o(self) -> Optional[PositiveInteger]:
        """Get pwmO (Pythonic accessor)."""
        return self._pwmO

    @pwm_o.setter
    def pwm_o(self, value: Optional[PositiveInteger]) -> None:
        """
        Set pwmO with validation.

        Args:
            value: The pwmO to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pwmO = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pwmO must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pwmO = value
        self._pwmS: Optional[PositiveInteger] = None

    @property
    def pwm_s(self) -> Optional[PositiveInteger]:
        """Get pwmS (Pythonic accessor)."""
        return self._pwmS

    @pwm_s.setter
    def pwm_s(self, value: Optional[PositiveInteger]) -> None:
        """
        Set pwmS with validation.

        Args:
            value: The pwmS to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pwmS = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pwmS must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pwmS = value
        # Transmitter Delay Compensation used to adjust the position of the Secondary
                # (SSP), relative to the beginning of the If this parameter is configured, the
                # Compensation is done by the CAN controller.
        # If not specified Compensation is disabled.
        self._sspOffset: Optional[PositiveInteger] = None

    @property
    def ssp_offset(self) -> Optional[PositiveInteger]:
        """Get sspOffset (Pythonic accessor)."""
        return self._sspOffset

    @ssp_offset.setter
    def ssp_offset(self, value: Optional[PositiveInteger]) -> None:
        """
        Set sspOffset with validation.

        Args:
            value: The sspOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sspOffset = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sspOffset must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sspOffset = value
        self._syncJumpWidth: Optional[PositiveInteger] = None

    @property
    def sync_jump_width(self) -> Optional[PositiveInteger]:
        """Get syncJumpWidth (Pythonic accessor)."""
        return self._syncJumpWidth

    @sync_jump_width.setter
    def sync_jump_width(self, value: Optional[PositiveInteger]) -> None:
        """
        Set syncJumpWidth with validation.

        Args:
            value: The syncJumpWidth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncJumpWidth = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"syncJumpWidth must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._syncJumpWidth = value
        self._timeSeg1: Optional[PositiveInteger] = None

    @property
    def time_seg1(self) -> Optional[PositiveInteger]:
        """Get timeSeg1 (Pythonic accessor)."""
        return self._timeSeg1

    @time_seg1.setter
    def time_seg1(self, value: Optional[PositiveInteger]) -> None:
        """
        Set timeSeg1 with validation.

        Args:
            value: The timeSeg1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSeg1 = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"timeSeg1 must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._timeSeg1 = value
        # Specifies phase segment 2 in time quantas.
        self._timeSeg2: Optional[PositiveInteger] = None

    @property
    def time_seg2(self) -> Optional[PositiveInteger]:
        """Get timeSeg2 (Pythonic accessor)."""
        return self._timeSeg2

    @time_seg2.setter
    def time_seg2(self, value: Optional[PositiveInteger]) -> None:
        """
        Set timeSeg2 with validation.

        Args:
            value: The timeSeg2 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSeg2 = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"timeSeg2 must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._timeSeg2 = value
        # Specifies if the transceiver shall be set to the PWM mode.
        # The transceiver shall be switched to PWM mode.
        # transceiver shall work in classic CAN mode.
        self._trcvPwmMode: Optional[Boolean] = None

    @property
    def trcv_pwm_mode(self) -> Optional[Boolean]:
        """Get trcvPwmMode (Pythonic accessor)."""
        return self._trcvPwmMode

    @trcv_pwm_mode.setter
    def trcv_pwm_mode(self, value: Optional[Boolean]) -> None:
        """
        Set trcvPwmMode with validation.

        Args:
            value: The trcvPwmMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trcvPwmMode = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"trcvPwmMode must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._trcvPwmMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getErrorSignaling(self) -> Boolean:
        """
        AUTOSAR-compliant getter for errorSignaling.

        Returns:
            The errorSignaling value

        Note:
            Delegates to error_signaling property (CODING_RULE_V2_00017)
        """
        return self.error_signaling  # Delegates to property

    def setErrorSignaling(self, value: Boolean) -> CanControllerXlConfiguration:
        """
        AUTOSAR-compliant setter for errorSignaling with method chaining.

        Args:
            value: The errorSignaling to set

        Returns:
            self for method chaining

        Note:
            Delegates to error_signaling property setter (gets validation automatically)
        """
        self.error_signaling = value  # Delegates to property setter
        return self

    def getPropSeg(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for propSeg.

        Returns:
            The propSeg value

        Note:
            Delegates to prop_seg property (CODING_RULE_V2_00017)
        """
        return self.prop_seg  # Delegates to property

    def setPropSeg(self, value: PositiveInteger) -> CanControllerXlConfiguration:
        """
        AUTOSAR-compliant setter for propSeg with method chaining.

        Args:
            value: The propSeg to set

        Returns:
            self for method chaining

        Note:
            Delegates to prop_seg property setter (gets validation automatically)
        """
        self.prop_seg = value  # Delegates to property setter
        return self

    def getPwmL(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for pwmL.

        Returns:
            The pwmL value

        Note:
            Delegates to pwm_l property (CODING_RULE_V2_00017)
        """
        return self.pwm_l  # Delegates to property

    def setPwmL(self, value: PositiveInteger) -> CanControllerXlConfiguration:
        """
        AUTOSAR-compliant setter for pwmL with method chaining.

        Args:
            value: The pwmL to set

        Returns:
            self for method chaining

        Note:
            Delegates to pwm_l property setter (gets validation automatically)
        """
        self.pwm_l = value  # Delegates to property setter
        return self

    def getPwmO(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for pwmO.

        Returns:
            The pwmO value

        Note:
            Delegates to pwm_o property (CODING_RULE_V2_00017)
        """
        return self.pwm_o  # Delegates to property

    def setPwmO(self, value: PositiveInteger) -> CanControllerXlConfiguration:
        """
        AUTOSAR-compliant setter for pwmO with method chaining.

        Args:
            value: The pwmO to set

        Returns:
            self for method chaining

        Note:
            Delegates to pwm_o property setter (gets validation automatically)
        """
        self.pwm_o = value  # Delegates to property setter
        return self

    def getPwmS(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for pwmS.

        Returns:
            The pwmS value

        Note:
            Delegates to pwm_s property (CODING_RULE_V2_00017)
        """
        return self.pwm_s  # Delegates to property

    def setPwmS(self, value: PositiveInteger) -> CanControllerXlConfiguration:
        """
        AUTOSAR-compliant setter for pwmS with method chaining.

        Args:
            value: The pwmS to set

        Returns:
            self for method chaining

        Note:
            Delegates to pwm_s property setter (gets validation automatically)
        """
        self.pwm_s = value  # Delegates to property setter
        return self

    def getSspOffset(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for sspOffset.

        Returns:
            The sspOffset value

        Note:
            Delegates to ssp_offset property (CODING_RULE_V2_00017)
        """
        return self.ssp_offset  # Delegates to property

    def setSspOffset(self, value: PositiveInteger) -> CanControllerXlConfiguration:
        """
        AUTOSAR-compliant setter for sspOffset with method chaining.

        Args:
            value: The sspOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to ssp_offset property setter (gets validation automatically)
        """
        self.ssp_offset = value  # Delegates to property setter
        return self

    def getSyncJumpWidth(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for syncJumpWidth.

        Returns:
            The syncJumpWidth value

        Note:
            Delegates to sync_jump_width property (CODING_RULE_V2_00017)
        """
        return self.sync_jump_width  # Delegates to property

    def setSyncJumpWidth(self, value: PositiveInteger) -> CanControllerXlConfiguration:
        """
        AUTOSAR-compliant setter for syncJumpWidth with method chaining.

        Args:
            value: The syncJumpWidth to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_jump_width property setter (gets validation automatically)
        """
        self.sync_jump_width = value  # Delegates to property setter
        return self

    def getTimeSeg1(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for timeSeg1.

        Returns:
            The timeSeg1 value

        Note:
            Delegates to time_seg1 property (CODING_RULE_V2_00017)
        """
        return self.time_seg1  # Delegates to property

    def setTimeSeg1(self, value: PositiveInteger) -> CanControllerXlConfiguration:
        """
        AUTOSAR-compliant setter for timeSeg1 with method chaining.

        Args:
            value: The timeSeg1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_seg1 property setter (gets validation automatically)
        """
        self.time_seg1 = value  # Delegates to property setter
        return self

    def getTimeSeg2(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for timeSeg2.

        Returns:
            The timeSeg2 value

        Note:
            Delegates to time_seg2 property (CODING_RULE_V2_00017)
        """
        return self.time_seg2  # Delegates to property

    def setTimeSeg2(self, value: PositiveInteger) -> CanControllerXlConfiguration:
        """
        AUTOSAR-compliant setter for timeSeg2 with method chaining.

        Args:
            value: The timeSeg2 to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_seg2 property setter (gets validation automatically)
        """
        self.time_seg2 = value  # Delegates to property setter
        return self

    def getTrcvPwmMode(self) -> Boolean:
        """
        AUTOSAR-compliant getter for trcvPwmMode.

        Returns:
            The trcvPwmMode value

        Note:
            Delegates to trcv_pwm_mode property (CODING_RULE_V2_00017)
        """
        return self.trcv_pwm_mode  # Delegates to property

    def setTrcvPwmMode(self, value: Boolean) -> CanControllerXlConfiguration:
        """
        AUTOSAR-compliant setter for trcvPwmMode with method chaining.

        Args:
            value: The trcvPwmMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to trcv_pwm_mode property setter (gets validation automatically)
        """
        self.trcv_pwm_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_error_signaling(self, value: Optional[Boolean]) -> CanControllerXlConfiguration:
        """
        Set errorSignaling and return self for chaining.

        Args:
            value: The errorSignaling to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_error_signaling("value")
        """
        self.error_signaling = value  # Use property setter (gets validation)
        return self

    def with_prop_seg(self, value: Optional[PositiveInteger]) -> CanControllerXlConfiguration:
        """
        Set propSeg and return self for chaining.

        Args:
            value: The propSeg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prop_seg("value")
        """
        self.prop_seg = value  # Use property setter (gets validation)
        return self

    def with_pwm_l(self, value: Optional[PositiveInteger]) -> CanControllerXlConfiguration:
        """
        Set pwmL and return self for chaining.

        Args:
            value: The pwmL to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pwm_l("value")
        """
        self.pwm_l = value  # Use property setter (gets validation)
        return self

    def with_pwm_o(self, value: Optional[PositiveInteger]) -> CanControllerXlConfiguration:
        """
        Set pwmO and return self for chaining.

        Args:
            value: The pwmO to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pwm_o("value")
        """
        self.pwm_o = value  # Use property setter (gets validation)
        return self

    def with_pwm_s(self, value: Optional[PositiveInteger]) -> CanControllerXlConfiguration:
        """
        Set pwmS and return self for chaining.

        Args:
            value: The pwmS to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pwm_s("value")
        """
        self.pwm_s = value  # Use property setter (gets validation)
        return self

    def with_ssp_offset(self, value: Optional[PositiveInteger]) -> CanControllerXlConfiguration:
        """
        Set sspOffset and return self for chaining.

        Args:
            value: The sspOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ssp_offset("value")
        """
        self.ssp_offset = value  # Use property setter (gets validation)
        return self

    def with_sync_jump_width(self, value: Optional[PositiveInteger]) -> CanControllerXlConfiguration:
        """
        Set syncJumpWidth and return self for chaining.

        Args:
            value: The syncJumpWidth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_jump_width("value")
        """
        self.sync_jump_width = value  # Use property setter (gets validation)
        return self

    def with_time_seg1(self, value: Optional[PositiveInteger]) -> CanControllerXlConfiguration:
        """
        Set timeSeg1 and return self for chaining.

        Args:
            value: The timeSeg1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_seg1("value")
        """
        self.time_seg1 = value  # Use property setter (gets validation)
        return self

    def with_time_seg2(self, value: Optional[PositiveInteger]) -> CanControllerXlConfiguration:
        """
        Set timeSeg2 and return self for chaining.

        Args:
            value: The timeSeg2 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_seg2("value")
        """
        self.time_seg2 = value  # Use property setter (gets validation)
        return self

    def with_trcv_pwm_mode(self, value: Optional[Boolean]) -> CanControllerXlConfiguration:
        """
        Set trcvPwmMode and return self for chaining.

        Args:
            value: The trcvPwmMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trcv_pwm_mode("value")
        """
        self.trcv_pwm_mode = value  # Use property setter (gets validation)
        return self



class CanControllerXlConfigurationRequirements(ARObject):
    """
    This element allows the specification of ranges for the CAN XL configuration
    parameters. These ranges are taken as requirements and have to be respected
    by the ECU developer.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanControllerXlConfigurationRequirements

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 71, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies if error signaling shall be enabled.
        # This is not when the transceiver is switched to PWM mode to TRUE).
        # signaling shall be enabled.
        # signaling shall be disabled.
        self._errorSignaling: Optional[Boolean] = None

    @property
    def error_signaling(self) -> Optional[Boolean]:
        """Get errorSignaling (Pythonic accessor)."""
        return self._errorSignaling

    @error_signaling.setter
    def error_signaling(self, value: Optional[Boolean]) -> None:
        """
        Set errorSignaling with validation.

        Args:
            value: The errorSignaling to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._errorSignaling = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"errorSignaling must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._errorSignaling = value
        self._maxNumberOfTimeQuantaPerBit: Optional[Integer] = None

    @property
    def max_number_of_time_quanta_per_bit(self) -> Optional[Integer]:
        """Get maxNumberOfTimeQuantaPerBit (Pythonic accessor)."""
        return self._maxNumberOfTimeQuantaPerBit

    @max_number_of_time_quanta_per_bit.setter
    def max_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> None:
        """
        Set maxNumberOfTimeQuantaPerBit with validation.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOfTimeQuantaPerBit = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxNumberOfTimeQuantaPerBit must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxNumberOfTimeQuantaPerBit = value
        self._maxPwmL: Optional[PositiveInteger] = None

    @property
    def max_pwm_l(self) -> Optional[PositiveInteger]:
        """Get maxPwmL (Pythonic accessor)."""
        return self._maxPwmL

    @max_pwm_l.setter
    def max_pwm_l(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxPwmL with validation.

        Args:
            value: The maxPwmL to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxPwmL = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxPwmL must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxPwmL = value
        self._maxPwmO: Optional[PositiveInteger] = None

    @property
    def max_pwm_o(self) -> Optional[PositiveInteger]:
        """Get maxPwmO (Pythonic accessor)."""
        return self._maxPwmO

    @max_pwm_o.setter
    def max_pwm_o(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxPwmO with validation.

        Args:
            value: The maxPwmO to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxPwmO = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxPwmO must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxPwmO = value
        self._maxPwmS: Optional[PositiveInteger] = None

    @property
    def max_pwm_s(self) -> Optional[PositiveInteger]:
        """Get maxPwmS (Pythonic accessor)."""
        return self._maxPwmS

    @max_pwm_s.setter
    def max_pwm_s(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxPwmS with validation.

        Args:
            value: The maxPwmS to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxPwmS = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxPwmS must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxPwmS = value
        # value of the sample point as a percentage of total bit time.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maxSample: Optional[Float] = None

    @property
    def max_sample(self) -> Optional[Float]:
        """Get maxSample (Pythonic accessor)."""
        return self._maxSample

    @max_sample.setter
    def max_sample(self, value: Optional[Float]) -> None:
        """
        Set maxSample with validation.

        Args:
            value: The maxSample to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSample = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"maxSample must be Float or float or None, got {type(value).__name__}"
            )
        self._maxSample = value
        # Synchronization Jump Width value as a of the total bit time.
        # The (Re-)Synchronization (SJW) defines how far a resynchronization the Sample
                # Point inside the limits defined by Buffer Segments to compensate for edge.
        self._maxSyncJump: Optional[Float] = None

    @property
    def max_sync_jump(self) -> Optional[Float]:
        """Get maxSyncJump (Pythonic accessor)."""
        return self._maxSyncJump

    @max_sync_jump.setter
    def max_sync_jump(self, value: Optional[Float]) -> None:
        """
        Set maxSyncJump with validation.

        Args:
            value: The maxSyncJump to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSyncJump = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"maxSyncJump must be Float or float or None, got {type(value).__name__}"
            )
        self._maxSyncJump = value
        # If not specified Transceiver Delay is disabled.
        self._maxTrcvDelay: Optional["TimeValue"] = None

    @property
    def max_trcv_delay(self) -> Optional["TimeValue"]:
        """Get maxTrcvDelay (Pythonic accessor)."""
        return self._maxTrcvDelay

    @max_trcv_delay.setter
    def max_trcv_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set maxTrcvDelay with validation.

        Args:
            value: The maxTrcvDelay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxTrcvDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"maxTrcvDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._maxTrcvDelay = value
        self._minNumberOfTimeQuantaPerBit: Optional[Integer] = None

    @property
    def min_number_of_time_quanta_per_bit(self) -> Optional[Integer]:
        """Get minNumberOfTimeQuantaPerBit (Pythonic accessor)."""
        return self._minNumberOfTimeQuantaPerBit

    @min_number_of_time_quanta_per_bit.setter
    def min_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> None:
        """
        Set minNumberOfTimeQuantaPerBit with validation.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minNumberOfTimeQuantaPerBit = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"minNumberOfTimeQuantaPerBit must be Integer or int or None, got {type(value).__name__}"
            )
        self._minNumberOfTimeQuantaPerBit = value
        self._minPwmL: Optional[PositiveInteger] = None

    @property
    def min_pwm_l(self) -> Optional[PositiveInteger]:
        """Get minPwmL (Pythonic accessor)."""
        return self._minPwmL

    @min_pwm_l.setter
    def min_pwm_l(self, value: Optional[PositiveInteger]) -> None:
        """
        Set minPwmL with validation.

        Args:
            value: The minPwmL to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minPwmL = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minPwmL must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minPwmL = value
        self._minPwmO: Optional[PositiveInteger] = None

    @property
    def min_pwm_o(self) -> Optional[PositiveInteger]:
        """Get minPwmO (Pythonic accessor)."""
        return self._minPwmO

    @min_pwm_o.setter
    def min_pwm_o(self, value: Optional[PositiveInteger]) -> None:
        """
        Set minPwmO with validation.

        Args:
            value: The minPwmO to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minPwmO = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minPwmO must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minPwmO = value
        self._minPwmS: Optional[PositiveInteger] = None

    @property
    def min_pwm_s(self) -> Optional[PositiveInteger]:
        """Get minPwmS (Pythonic accessor)."""
        return self._minPwmS

    @min_pwm_s.setter
    def min_pwm_s(self, value: Optional[PositiveInteger]) -> None:
        """
        Set minPwmS with validation.

        Args:
            value: The minPwmS to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minPwmS = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minPwmS must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minPwmS = value
        # value of the sample point as a percentage of the time.
        self._minSamplePoint: Optional[Float] = None

    @property
    def min_sample_point(self) -> Optional[Float]:
        """Get minSamplePoint (Pythonic accessor)."""
        return self._minSamplePoint

    @min_sample_point.setter
    def min_sample_point(self, value: Optional[Float]) -> None:
        """
        Set minSamplePoint with validation.

        Args:
            value: The minSamplePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minSamplePoint = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"minSamplePoint must be Float or float or None, got {type(value).__name__}"
            )
        self._minSamplePoint = value
        # Synchronization Jump Width value as a of the total bit time.
        # The (Re-)Synchronization (SJW) defines how far a resynchronization the Sample
                # Point inside the limits defined by Buffer Segments to compensate for edge.
        self._minSyncJump: Optional[Float] = None

    @property
    def min_sync_jump(self) -> Optional[Float]:
        """Get minSyncJump (Pythonic accessor)."""
        return self._minSyncJump

    @min_sync_jump.setter
    def min_sync_jump(self, value: Optional[Float]) -> None:
        """
        Set minSyncJump with validation.

        Args:
            value: The minSyncJump to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minSyncJump = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"minSyncJump must be Float or float or None, got {type(value).__name__}"
            )
        self._minSyncJump = value
        # If not specified Transceiver Delay is disabled.
        self._minTrcvDelay: Optional["TimeValue"] = None

    @property
    def min_trcv_delay(self) -> Optional["TimeValue"]:
        """Get minTrcvDelay (Pythonic accessor)."""
        return self._minTrcvDelay

    @min_trcv_delay.setter
    def min_trcv_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set minTrcvDelay with validation.

        Args:
            value: The minTrcvDelay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minTrcvDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minTrcvDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._minTrcvDelay = value
        # The transceiver shall be switched to PWM mode.
        # transceiver shall work in classic CAN mode.
        self._trcvPwmMode: Optional[Boolean] = None

    @property
    def trcv_pwm_mode(self) -> Optional[Boolean]:
        """Get trcvPwmMode (Pythonic accessor)."""
        return self._trcvPwmMode

    @trcv_pwm_mode.setter
    def trcv_pwm_mode(self, value: Optional[Boolean]) -> None:
        """
        Set trcvPwmMode with validation.

        Args:
            value: The trcvPwmMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trcvPwmMode = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"trcvPwmMode must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._trcvPwmMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getErrorSignaling(self) -> Boolean:
        """
        AUTOSAR-compliant getter for errorSignaling.

        Returns:
            The errorSignaling value

        Note:
            Delegates to error_signaling property (CODING_RULE_V2_00017)
        """
        return self.error_signaling  # Delegates to property

    def setErrorSignaling(self, value: Boolean) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for errorSignaling with method chaining.

        Args:
            value: The errorSignaling to set

        Returns:
            self for method chaining

        Note:
            Delegates to error_signaling property setter (gets validation automatically)
        """
        self.error_signaling = value  # Delegates to property setter
        return self

    def getMaxNumberOfTimeQuantaPerBit(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxNumberOfTimeQuantaPerBit.

        Returns:
            The maxNumberOfTimeQuantaPerBit value

        Note:
            Delegates to max_number_of_time_quanta_per_bit property (CODING_RULE_V2_00017)
        """
        return self.max_number_of_time_quanta_per_bit  # Delegates to property

    def setMaxNumberOfTimeQuantaPerBit(self, value: Integer) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxNumberOfTimeQuantaPerBit with method chaining.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of_time_quanta_per_bit property setter (gets validation automatically)
        """
        self.max_number_of_time_quanta_per_bit = value  # Delegates to property setter
        return self

    def getMaxPwmL(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxPwmL.

        Returns:
            The maxPwmL value

        Note:
            Delegates to max_pwm_l property (CODING_RULE_V2_00017)
        """
        return self.max_pwm_l  # Delegates to property

    def setMaxPwmL(self, value: PositiveInteger) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxPwmL with method chaining.

        Args:
            value: The maxPwmL to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_pwm_l property setter (gets validation automatically)
        """
        self.max_pwm_l = value  # Delegates to property setter
        return self

    def getMaxPwmO(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxPwmO.

        Returns:
            The maxPwmO value

        Note:
            Delegates to max_pwm_o property (CODING_RULE_V2_00017)
        """
        return self.max_pwm_o  # Delegates to property

    def setMaxPwmO(self, value: PositiveInteger) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxPwmO with method chaining.

        Args:
            value: The maxPwmO to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_pwm_o property setter (gets validation automatically)
        """
        self.max_pwm_o = value  # Delegates to property setter
        return self

    def getMaxPwmS(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxPwmS.

        Returns:
            The maxPwmS value

        Note:
            Delegates to max_pwm_s property (CODING_RULE_V2_00017)
        """
        return self.max_pwm_s  # Delegates to property

    def setMaxPwmS(self, value: PositiveInteger) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxPwmS with method chaining.

        Args:
            value: The maxPwmS to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_pwm_s property setter (gets validation automatically)
        """
        self.max_pwm_s = value  # Delegates to property setter
        return self

    def getMaxSample(self) -> Float:
        """
        AUTOSAR-compliant getter for maxSample.

        Returns:
            The maxSample value

        Note:
            Delegates to max_sample property (CODING_RULE_V2_00017)
        """
        return self.max_sample  # Delegates to property

    def setMaxSample(self, value: Float) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxSample with method chaining.

        Args:
            value: The maxSample to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_sample property setter (gets validation automatically)
        """
        self.max_sample = value  # Delegates to property setter
        return self

    def getMaxSyncJump(self) -> Float:
        """
        AUTOSAR-compliant getter for maxSyncJump.

        Returns:
            The maxSyncJump value

        Note:
            Delegates to max_sync_jump property (CODING_RULE_V2_00017)
        """
        return self.max_sync_jump  # Delegates to property

    def setMaxSyncJump(self, value: Float) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxSyncJump with method chaining.

        Args:
            value: The maxSyncJump to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_sync_jump property setter (gets validation automatically)
        """
        self.max_sync_jump = value  # Delegates to property setter
        return self

    def getMaxTrcvDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for maxTrcvDelay.

        Returns:
            The maxTrcvDelay value

        Note:
            Delegates to max_trcv_delay property (CODING_RULE_V2_00017)
        """
        return self.max_trcv_delay  # Delegates to property

    def setMaxTrcvDelay(self, value: "TimeValue") -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxTrcvDelay with method chaining.

        Args:
            value: The maxTrcvDelay to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_trcv_delay property setter (gets validation automatically)
        """
        self.max_trcv_delay = value  # Delegates to property setter
        return self

    def getMinNumberOfTimeQuantaPerBit(self) -> Integer:
        """
        AUTOSAR-compliant getter for minNumberOfTimeQuantaPerBit.

        Returns:
            The minNumberOfTimeQuantaPerBit value

        Note:
            Delegates to min_number_of_time_quanta_per_bit property (CODING_RULE_V2_00017)
        """
        return self.min_number_of_time_quanta_per_bit  # Delegates to property

    def setMinNumberOfTimeQuantaPerBit(self, value: Integer) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minNumberOfTimeQuantaPerBit with method chaining.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_number_of_time_quanta_per_bit property setter (gets validation automatically)
        """
        self.min_number_of_time_quanta_per_bit = value  # Delegates to property setter
        return self

    def getMinPwmL(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for minPwmL.

        Returns:
            The minPwmL value

        Note:
            Delegates to min_pwm_l property (CODING_RULE_V2_00017)
        """
        return self.min_pwm_l  # Delegates to property

    def setMinPwmL(self, value: PositiveInteger) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minPwmL with method chaining.

        Args:
            value: The minPwmL to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_pwm_l property setter (gets validation automatically)
        """
        self.min_pwm_l = value  # Delegates to property setter
        return self

    def getMinPwmO(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for minPwmO.

        Returns:
            The minPwmO value

        Note:
            Delegates to min_pwm_o property (CODING_RULE_V2_00017)
        """
        return self.min_pwm_o  # Delegates to property

    def setMinPwmO(self, value: PositiveInteger) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minPwmO with method chaining.

        Args:
            value: The minPwmO to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_pwm_o property setter (gets validation automatically)
        """
        self.min_pwm_o = value  # Delegates to property setter
        return self

    def getMinPwmS(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for minPwmS.

        Returns:
            The minPwmS value

        Note:
            Delegates to min_pwm_s property (CODING_RULE_V2_00017)
        """
        return self.min_pwm_s  # Delegates to property

    def setMinPwmS(self, value: PositiveInteger) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minPwmS with method chaining.

        Args:
            value: The minPwmS to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_pwm_s property setter (gets validation automatically)
        """
        self.min_pwm_s = value  # Delegates to property setter
        return self

    def getMinSamplePoint(self) -> Float:
        """
        AUTOSAR-compliant getter for minSamplePoint.

        Returns:
            The minSamplePoint value

        Note:
            Delegates to min_sample_point property (CODING_RULE_V2_00017)
        """
        return self.min_sample_point  # Delegates to property

    def setMinSamplePoint(self, value: Float) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minSamplePoint with method chaining.

        Args:
            value: The minSamplePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_sample_point property setter (gets validation automatically)
        """
        self.min_sample_point = value  # Delegates to property setter
        return self

    def getMinSyncJump(self) -> Float:
        """
        AUTOSAR-compliant getter for minSyncJump.

        Returns:
            The minSyncJump value

        Note:
            Delegates to min_sync_jump property (CODING_RULE_V2_00017)
        """
        return self.min_sync_jump  # Delegates to property

    def setMinSyncJump(self, value: Float) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minSyncJump with method chaining.

        Args:
            value: The minSyncJump to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_sync_jump property setter (gets validation automatically)
        """
        self.min_sync_jump = value  # Delegates to property setter
        return self

    def getMinTrcvDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minTrcvDelay.

        Returns:
            The minTrcvDelay value

        Note:
            Delegates to min_trcv_delay property (CODING_RULE_V2_00017)
        """
        return self.min_trcv_delay  # Delegates to property

    def setMinTrcvDelay(self, value: "TimeValue") -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minTrcvDelay with method chaining.

        Args:
            value: The minTrcvDelay to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_trcv_delay property setter (gets validation automatically)
        """
        self.min_trcv_delay = value  # Delegates to property setter
        return self

    def getTrcvPwmMode(self) -> Boolean:
        """
        AUTOSAR-compliant getter for trcvPwmMode.

        Returns:
            The trcvPwmMode value

        Note:
            Delegates to trcv_pwm_mode property (CODING_RULE_V2_00017)
        """
        return self.trcv_pwm_mode  # Delegates to property

    def setTrcvPwmMode(self, value: Boolean) -> CanControllerXlConfigurationRequirements:
        """
        AUTOSAR-compliant setter for trcvPwmMode with method chaining.

        Args:
            value: The trcvPwmMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to trcv_pwm_mode property setter (gets validation automatically)
        """
        self.trcv_pwm_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_error_signaling(self, value: Optional[Boolean]) -> CanControllerXlConfigurationRequirements:
        """
        Set errorSignaling and return self for chaining.

        Args:
            value: The errorSignaling to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_error_signaling("value")
        """
        self.error_signaling = value  # Use property setter (gets validation)
        return self

    def with_max_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> CanControllerXlConfigurationRequirements:
        """
        Set maxNumberOfTimeQuantaPerBit and return self for chaining.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of_time_quanta_per_bit("value")
        """
        self.max_number_of_time_quanta_per_bit = value  # Use property setter (gets validation)
        return self

    def with_max_pwm_l(self, value: Optional[PositiveInteger]) -> CanControllerXlConfigurationRequirements:
        """
        Set maxPwmL and return self for chaining.

        Args:
            value: The maxPwmL to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_pwm_l("value")
        """
        self.max_pwm_l = value  # Use property setter (gets validation)
        return self

    def with_max_pwm_o(self, value: Optional[PositiveInteger]) -> CanControllerXlConfigurationRequirements:
        """
        Set maxPwmO and return self for chaining.

        Args:
            value: The maxPwmO to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_pwm_o("value")
        """
        self.max_pwm_o = value  # Use property setter (gets validation)
        return self

    def with_max_pwm_s(self, value: Optional[PositiveInteger]) -> CanControllerXlConfigurationRequirements:
        """
        Set maxPwmS and return self for chaining.

        Args:
            value: The maxPwmS to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_pwm_s("value")
        """
        self.max_pwm_s = value  # Use property setter (gets validation)
        return self

    def with_max_sample(self, value: Optional[Float]) -> CanControllerXlConfigurationRequirements:
        """
        Set maxSample and return self for chaining.

        Args:
            value: The maxSample to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_sample("value")
        """
        self.max_sample = value  # Use property setter (gets validation)
        return self

    def with_max_sync_jump(self, value: Optional[Float]) -> CanControllerXlConfigurationRequirements:
        """
        Set maxSyncJump and return self for chaining.

        Args:
            value: The maxSyncJump to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_sync_jump("value")
        """
        self.max_sync_jump = value  # Use property setter (gets validation)
        return self

    def with_max_trcv_delay(self, value: Optional["TimeValue"]) -> CanControllerXlConfigurationRequirements:
        """
        Set maxTrcvDelay and return self for chaining.

        Args:
            value: The maxTrcvDelay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_trcv_delay("value")
        """
        self.max_trcv_delay = value  # Use property setter (gets validation)
        return self

    def with_min_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> CanControllerXlConfigurationRequirements:
        """
        Set minNumberOfTimeQuantaPerBit and return self for chaining.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_number_of_time_quanta_per_bit("value")
        """
        self.min_number_of_time_quanta_per_bit = value  # Use property setter (gets validation)
        return self

    def with_min_pwm_l(self, value: Optional[PositiveInteger]) -> CanControllerXlConfigurationRequirements:
        """
        Set minPwmL and return self for chaining.

        Args:
            value: The minPwmL to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_pwm_l("value")
        """
        self.min_pwm_l = value  # Use property setter (gets validation)
        return self

    def with_min_pwm_o(self, value: Optional[PositiveInteger]) -> CanControllerXlConfigurationRequirements:
        """
        Set minPwmO and return self for chaining.

        Args:
            value: The minPwmO to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_pwm_o("value")
        """
        self.min_pwm_o = value  # Use property setter (gets validation)
        return self

    def with_min_pwm_s(self, value: Optional[PositiveInteger]) -> CanControllerXlConfigurationRequirements:
        """
        Set minPwmS and return self for chaining.

        Args:
            value: The minPwmS to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_pwm_s("value")
        """
        self.min_pwm_s = value  # Use property setter (gets validation)
        return self

    def with_min_sample_point(self, value: Optional[Float]) -> CanControllerXlConfigurationRequirements:
        """
        Set minSamplePoint and return self for chaining.

        Args:
            value: The minSamplePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_sample_point("value")
        """
        self.min_sample_point = value  # Use property setter (gets validation)
        return self

    def with_min_sync_jump(self, value: Optional[Float]) -> CanControllerXlConfigurationRequirements:
        """
        Set minSyncJump and return self for chaining.

        Args:
            value: The minSyncJump to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_sync_jump("value")
        """
        self.min_sync_jump = value  # Use property setter (gets validation)
        return self

    def with_min_trcv_delay(self, value: Optional["TimeValue"]) -> CanControllerXlConfigurationRequirements:
        """
        Set minTrcvDelay and return self for chaining.

        Args:
            value: The minTrcvDelay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_trcv_delay("value")
        """
        self.min_trcv_delay = value  # Use property setter (gets validation)
        return self

    def with_trcv_pwm_mode(self, value: Optional[Boolean]) -> CanControllerXlConfigurationRequirements:
        """
        Set trcvPwmMode and return self for chaining.

        Args:
            value: The trcvPwmMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trcv_pwm_mode("value")
        """
        self.trcv_pwm_mode = value  # Use property setter (gets validation)
        return self



class AbstractCanPhysicalChannel(PhysicalChannel, ABC):
    """
    Abstract class that is used to collect the common TtCAN and CAN
    PhysicalChannel attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::AbstractCanPhysicalChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 73, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCanPhysicalChannel:
            raise TypeError("AbstractCanPhysicalChannel is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AbstractCanCommunicationConnector(CommunicationConnector, ABC):
    """
    Abstract class that is used to collect the common TtCAN and CAN
    CommunicationConnector attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::AbstractCanCommunicationConnector

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 73, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCanCommunicationConnector:
            raise TypeError("AbstractCanCommunicationConnector is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CanControllerConfiguration(AbstractCanCommunicationControllerAttributes):
    """
    This element is used for the specification of the exact CAN Bit Timing
    configuration parameter values.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanControllerConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 64, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies propagation delay in time quantas.
        self._propSeg: Optional[Integer] = None

    @property
    def prop_seg(self) -> Optional[Integer]:
        """Get propSeg (Pythonic accessor)."""
        return self._propSeg

    @prop_seg.setter
    def prop_seg(self, value: Optional[Integer]) -> None:
        """
        Set propSeg with validation.

        Args:
            value: The propSeg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._propSeg = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"propSeg must be Integer or int or None, got {type(value).__name__}"
            )
        self._propSeg = value
        # Jump Width how far a resynchronization may move the inside the limits defined
        # by the Phase Buffer compensate for edge phase errors.
        self._syncJumpWidth: Optional[Integer] = None

    @property
    def sync_jump_width(self) -> Optional[Integer]:
        """Get syncJumpWidth (Pythonic accessor)."""
        return self._syncJumpWidth

    @sync_jump_width.setter
    def sync_jump_width(self, value: Optional[Integer]) -> None:
        """
        Set syncJumpWidth with validation.

        Args:
            value: The syncJumpWidth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncJumpWidth = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"syncJumpWidth must be Integer or int or None, got {type(value).__name__}"
            )
        self._syncJumpWidth = value
        # Phase_Seg1.
        self._timeSeg1: Optional[Integer] = None

    @property
    def time_seg1(self) -> Optional[Integer]:
        """Get timeSeg1 (Pythonic accessor)."""
        return self._timeSeg1

    @time_seg1.setter
    def time_seg1(self, value: Optional[Integer]) -> None:
        """
        Set timeSeg1 with validation.

        Args:
            value: The timeSeg1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSeg1 = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"timeSeg1 must be Integer or int or None, got {type(value).__name__}"
            )
        self._timeSeg1 = value
        # Specifies phase segment 2 in time quantas.
        # Phase_Seg2.
        self._timeSeg2: Optional[Integer] = None

    @property
    def time_seg2(self) -> Optional[Integer]:
        """Get timeSeg2 (Pythonic accessor)."""
        return self._timeSeg2

    @time_seg2.setter
    def time_seg2(self, value: Optional[Integer]) -> None:
        """
        Set timeSeg2 with validation.

        Args:
            value: The timeSeg2 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSeg2 = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"timeSeg2 must be Integer or int or None, got {type(value).__name__}"
            )
        self._timeSeg2 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPropSeg(self) -> Integer:
        """
        AUTOSAR-compliant getter for propSeg.

        Returns:
            The propSeg value

        Note:
            Delegates to prop_seg property (CODING_RULE_V2_00017)
        """
        return self.prop_seg  # Delegates to property

    def setPropSeg(self, value: Integer) -> CanControllerConfiguration:
        """
        AUTOSAR-compliant setter for propSeg with method chaining.

        Args:
            value: The propSeg to set

        Returns:
            self for method chaining

        Note:
            Delegates to prop_seg property setter (gets validation automatically)
        """
        self.prop_seg = value  # Delegates to property setter
        return self

    def getSyncJumpWidth(self) -> Integer:
        """
        AUTOSAR-compliant getter for syncJumpWidth.

        Returns:
            The syncJumpWidth value

        Note:
            Delegates to sync_jump_width property (CODING_RULE_V2_00017)
        """
        return self.sync_jump_width  # Delegates to property

    def setSyncJumpWidth(self, value: Integer) -> CanControllerConfiguration:
        """
        AUTOSAR-compliant setter for syncJumpWidth with method chaining.

        Args:
            value: The syncJumpWidth to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_jump_width property setter (gets validation automatically)
        """
        self.sync_jump_width = value  # Delegates to property setter
        return self

    def getTimeSeg1(self) -> Integer:
        """
        AUTOSAR-compliant getter for timeSeg1.

        Returns:
            The timeSeg1 value

        Note:
            Delegates to time_seg1 property (CODING_RULE_V2_00017)
        """
        return self.time_seg1  # Delegates to property

    def setTimeSeg1(self, value: Integer) -> CanControllerConfiguration:
        """
        AUTOSAR-compliant setter for timeSeg1 with method chaining.

        Args:
            value: The timeSeg1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_seg1 property setter (gets validation automatically)
        """
        self.time_seg1 = value  # Delegates to property setter
        return self

    def getTimeSeg2(self) -> Integer:
        """
        AUTOSAR-compliant getter for timeSeg2.

        Returns:
            The timeSeg2 value

        Note:
            Delegates to time_seg2 property (CODING_RULE_V2_00017)
        """
        return self.time_seg2  # Delegates to property

    def setTimeSeg2(self, value: Integer) -> CanControllerConfiguration:
        """
        AUTOSAR-compliant setter for timeSeg2 with method chaining.

        Args:
            value: The timeSeg2 to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_seg2 property setter (gets validation automatically)
        """
        self.time_seg2 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_prop_seg(self, value: Optional[Integer]) -> CanControllerConfiguration:
        """
        Set propSeg and return self for chaining.

        Args:
            value: The propSeg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prop_seg("value")
        """
        self.prop_seg = value  # Use property setter (gets validation)
        return self

    def with_sync_jump_width(self, value: Optional[Integer]) -> CanControllerConfiguration:
        """
        Set syncJumpWidth and return self for chaining.

        Args:
            value: The syncJumpWidth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_jump_width("value")
        """
        self.sync_jump_width = value  # Use property setter (gets validation)
        return self

    def with_time_seg1(self, value: Optional[Integer]) -> CanControllerConfiguration:
        """
        Set timeSeg1 and return self for chaining.

        Args:
            value: The timeSeg1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_seg1("value")
        """
        self.time_seg1 = value  # Use property setter (gets validation)
        return self

    def with_time_seg2(self, value: Optional[Integer]) -> CanControllerConfiguration:
        """
        Set timeSeg2 and return self for chaining.

        Args:
            value: The timeSeg2 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_seg2("value")
        """
        self.time_seg2 = value  # Use property setter (gets validation)
        return self



class CanControllerConfigurationRequirements(AbstractCanCommunicationControllerAttributes):
    """
    This element allows the specification of ranges for the CAN Bit Timing
    configuration parameters. These ranges are taken as requirements and have to
    be respected by the ECU developer.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanControllerConfigurationRequirements

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 65, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum number of time quanta in the bit time.
        self._maxNumberOfTimeQuantaPerBit: Optional[Integer] = None

    @property
    def max_number_of_time_quanta_per_bit(self) -> Optional[Integer]:
        """Get maxNumberOfTimeQuantaPerBit (Pythonic accessor)."""
        return self._maxNumberOfTimeQuantaPerBit

    @max_number_of_time_quanta_per_bit.setter
    def max_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> None:
        """
        Set maxNumberOfTimeQuantaPerBit with validation.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOfTimeQuantaPerBit = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxNumberOfTimeQuantaPerBit must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxNumberOfTimeQuantaPerBit = value
        # value of the sample point as a percentage of total bit time.
        self._maxSample: Optional[Float] = None

    @property
    def max_sample(self) -> Optional[Float]:
        """Get maxSample (Pythonic accessor)."""
        return self._maxSample

    @max_sample.setter
    def max_sample(self, value: Optional[Float]) -> None:
        """
        Set maxSample with validation.

        Args:
            value: The maxSample to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSample = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"maxSample must be Float or float or None, got {type(value).__name__}"
            )
        self._maxSample = value
        # Synchronization Jump Width value as a of the total bit time.
        # The (Re-)Synchronization (SJW) defines how far a resynchronization the Sample
                # Point inside the limits defined by Buffer Segments to compensate for edge.
        self._maxSyncJump: Optional[Float] = None

    @property
    def max_sync_jump(self) -> Optional[Float]:
        """Get maxSyncJump (Pythonic accessor)."""
        return self._maxSyncJump

    @max_sync_jump.setter
    def max_sync_jump(self, value: Optional[Float]) -> None:
        """
        Set maxSyncJump with validation.

        Args:
            value: The maxSyncJump to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSyncJump = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"maxSyncJump must be Float or float or None, got {type(value).__name__}"
            )
        self._maxSyncJump = value
        self._minNumberOfTimeQuantaPerBit: Optional[Integer] = None

    @property
    def min_number_of_time_quanta_per_bit(self) -> Optional[Integer]:
        """Get minNumberOfTimeQuantaPerBit (Pythonic accessor)."""
        return self._minNumberOfTimeQuantaPerBit

    @min_number_of_time_quanta_per_bit.setter
    def min_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> None:
        """
        Set minNumberOfTimeQuantaPerBit with validation.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minNumberOfTimeQuantaPerBit = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"minNumberOfTimeQuantaPerBit must be Integer or int or None, got {type(value).__name__}"
            )
        self._minNumberOfTimeQuantaPerBit = value
        # value of the sample point as a percentage of the time.
        self._minSamplePoint: Optional[Float] = None

    @property
    def min_sample_point(self) -> Optional[Float]:
        """Get minSamplePoint (Pythonic accessor)."""
        return self._minSamplePoint

    @min_sample_point.setter
    def min_sample_point(self, value: Optional[Float]) -> None:
        """
        Set minSamplePoint with validation.

        Args:
            value: The minSamplePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minSamplePoint = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"minSamplePoint must be Float or float or None, got {type(value).__name__}"
            )
        self._minSamplePoint = value
        # Synchronization Jump Width value as a of the total bit time.
        # The (Re-)Synchronization (SJW) defines how far a resynchronization the Sample
                # Point inside the limits defined by Buffer Segments to compensate for edge.
        self._minSyncJump: Optional[Float] = None

    @property
    def min_sync_jump(self) -> Optional[Float]:
        """Get minSyncJump (Pythonic accessor)."""
        return self._minSyncJump

    @min_sync_jump.setter
    def min_sync_jump(self, value: Optional[Float]) -> None:
        """
        Set minSyncJump with validation.

        Args:
            value: The minSyncJump to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minSyncJump = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"minSyncJump must be Float or float or None, got {type(value).__name__}"
            )
        self._minSyncJump = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxNumberOfTimeQuantaPerBit(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxNumberOfTimeQuantaPerBit.

        Returns:
            The maxNumberOfTimeQuantaPerBit value

        Note:
            Delegates to max_number_of_time_quanta_per_bit property (CODING_RULE_V2_00017)
        """
        return self.max_number_of_time_quanta_per_bit  # Delegates to property

    def setMaxNumberOfTimeQuantaPerBit(self, value: Integer) -> CanControllerConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxNumberOfTimeQuantaPerBit with method chaining.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of_time_quanta_per_bit property setter (gets validation automatically)
        """
        self.max_number_of_time_quanta_per_bit = value  # Delegates to property setter
        return self

    def getMaxSample(self) -> Float:
        """
        AUTOSAR-compliant getter for maxSample.

        Returns:
            The maxSample value

        Note:
            Delegates to max_sample property (CODING_RULE_V2_00017)
        """
        return self.max_sample  # Delegates to property

    def setMaxSample(self, value: Float) -> CanControllerConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxSample with method chaining.

        Args:
            value: The maxSample to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_sample property setter (gets validation automatically)
        """
        self.max_sample = value  # Delegates to property setter
        return self

    def getMaxSyncJump(self) -> Float:
        """
        AUTOSAR-compliant getter for maxSyncJump.

        Returns:
            The maxSyncJump value

        Note:
            Delegates to max_sync_jump property (CODING_RULE_V2_00017)
        """
        return self.max_sync_jump  # Delegates to property

    def setMaxSyncJump(self, value: Float) -> CanControllerConfigurationRequirements:
        """
        AUTOSAR-compliant setter for maxSyncJump with method chaining.

        Args:
            value: The maxSyncJump to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_sync_jump property setter (gets validation automatically)
        """
        self.max_sync_jump = value  # Delegates to property setter
        return self

    def getMinNumberOfTimeQuantaPerBit(self) -> Integer:
        """
        AUTOSAR-compliant getter for minNumberOfTimeQuantaPerBit.

        Returns:
            The minNumberOfTimeQuantaPerBit value

        Note:
            Delegates to min_number_of_time_quanta_per_bit property (CODING_RULE_V2_00017)
        """
        return self.min_number_of_time_quanta_per_bit  # Delegates to property

    def setMinNumberOfTimeQuantaPerBit(self, value: Integer) -> CanControllerConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minNumberOfTimeQuantaPerBit with method chaining.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_number_of_time_quanta_per_bit property setter (gets validation automatically)
        """
        self.min_number_of_time_quanta_per_bit = value  # Delegates to property setter
        return self

    def getMinSamplePoint(self) -> Float:
        """
        AUTOSAR-compliant getter for minSamplePoint.

        Returns:
            The minSamplePoint value

        Note:
            Delegates to min_sample_point property (CODING_RULE_V2_00017)
        """
        return self.min_sample_point  # Delegates to property

    def setMinSamplePoint(self, value: Float) -> CanControllerConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minSamplePoint with method chaining.

        Args:
            value: The minSamplePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_sample_point property setter (gets validation automatically)
        """
        self.min_sample_point = value  # Delegates to property setter
        return self

    def getMinSyncJump(self) -> Float:
        """
        AUTOSAR-compliant getter for minSyncJump.

        Returns:
            The minSyncJump value

        Note:
            Delegates to min_sync_jump property (CODING_RULE_V2_00017)
        """
        return self.min_sync_jump  # Delegates to property

    def setMinSyncJump(self, value: Float) -> CanControllerConfigurationRequirements:
        """
        AUTOSAR-compliant setter for minSyncJump with method chaining.

        Args:
            value: The minSyncJump to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_sync_jump property setter (gets validation automatically)
        """
        self.min_sync_jump = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> CanControllerConfigurationRequirements:
        """
        Set maxNumberOfTimeQuantaPerBit and return self for chaining.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of_time_quanta_per_bit("value")
        """
        self.max_number_of_time_quanta_per_bit = value  # Use property setter (gets validation)
        return self

    def with_max_sample(self, value: Optional[Float]) -> CanControllerConfigurationRequirements:
        """
        Set maxSample and return self for chaining.

        Args:
            value: The maxSample to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_sample("value")
        """
        self.max_sample = value  # Use property setter (gets validation)
        return self

    def with_max_sync_jump(self, value: Optional[Float]) -> CanControllerConfigurationRequirements:
        """
        Set maxSyncJump and return self for chaining.

        Args:
            value: The maxSyncJump to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_sync_jump("value")
        """
        self.max_sync_jump = value  # Use property setter (gets validation)
        return self

    def with_min_number_of_time_quanta_per_bit(self, value: Optional[Integer]) -> CanControllerConfigurationRequirements:
        """
        Set minNumberOfTimeQuantaPerBit and return self for chaining.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_number_of_time_quanta_per_bit("value")
        """
        self.min_number_of_time_quanta_per_bit = value  # Use property setter (gets validation)
        return self

    def with_min_sample_point(self, value: Optional[Float]) -> CanControllerConfigurationRequirements:
        """
        Set minSamplePoint and return self for chaining.

        Args:
            value: The minSamplePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_sample_point("value")
        """
        self.min_sample_point = value  # Use property setter (gets validation)
        return self

    def with_min_sync_jump(self, value: Optional[Float]) -> CanControllerConfigurationRequirements:
        """
        Set minSyncJump and return self for chaining.

        Args:
            value: The minSyncJump to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_sync_jump("value")
        """
        self.min_sync_jump = value  # Use property setter (gets validation)
        return self



class CanPhysicalChannel(AbstractCanPhysicalChannel):
    """
    CAN bus specific physical channel attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanPhysicalChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 73, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CanCommunicationConnector(AbstractCanCommunicationConnector):
    """
    CAN bus specific communication connector attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanCommunicationConnector

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 74, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Bit mask for CAN Identifier used to configure the CAN for partial network
        # wakeup.
        self._pncWakeupCan: Optional[PositiveInteger] = None

    @property
    def pnc_wakeup_can(self) -> Optional[PositiveInteger]:
        """Get pncWakeupCan (Pythonic accessor)."""
        return self._pncWakeupCan

    @pnc_wakeup_can.setter
    def pnc_wakeup_can(self, value: Optional[PositiveInteger]) -> None:
        """
        Set pncWakeupCan with validation.

        Args:
            value: The pncWakeupCan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncWakeupCan = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pncWakeupCan must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pncWakeupCan = value
        # wakeup.
        self._pncWakeup: Optional["PositiveUnlimitedInteger"] = None

    @property
    def pnc_wakeup(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get pncWakeup (Pythonic accessor)."""
        return self._pncWakeup

    @pnc_wakeup.setter
    def pnc_wakeup(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set pncWakeup with validation.

        Args:
            value: The pncWakeup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncWakeup = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"pncWakeup must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._pncWakeup = value
        # partial network wakeup in Bytes.
        self._pncWakeupDlc: Optional[PositiveInteger] = None

    @property
    def pnc_wakeup_dlc(self) -> Optional[PositiveInteger]:
        """Get pncWakeupDlc (Pythonic accessor)."""
        return self._pncWakeupDlc

    @pnc_wakeup_dlc.setter
    def pnc_wakeup_dlc(self, value: Optional[PositiveInteger]) -> None:
        """
        Set pncWakeupDlc with validation.

        Args:
            value: The pncWakeupDlc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncWakeupDlc = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pncWakeupDlc must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pncWakeupDlc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPncWakeupCan(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for pncWakeupCan.

        Returns:
            The pncWakeupCan value

        Note:
            Delegates to pnc_wakeup_can property (CODING_RULE_V2_00017)
        """
        return self.pnc_wakeup_can  # Delegates to property

    def setPncWakeupCan(self, value: PositiveInteger) -> CanCommunicationConnector:
        """
        AUTOSAR-compliant setter for pncWakeupCan with method chaining.

        Args:
            value: The pncWakeupCan to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_wakeup_can property setter (gets validation automatically)
        """
        self.pnc_wakeup_can = value  # Delegates to property setter
        return self

    def getPncWakeup(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for pncWakeup.

        Returns:
            The pncWakeup value

        Note:
            Delegates to pnc_wakeup property (CODING_RULE_V2_00017)
        """
        return self.pnc_wakeup  # Delegates to property

    def setPncWakeup(self, value: "PositiveUnlimitedInteger") -> CanCommunicationConnector:
        """
        AUTOSAR-compliant setter for pncWakeup with method chaining.

        Args:
            value: The pncWakeup to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_wakeup property setter (gets validation automatically)
        """
        self.pnc_wakeup = value  # Delegates to property setter
        return self

    def getPncWakeupDlc(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for pncWakeupDlc.

        Returns:
            The pncWakeupDlc value

        Note:
            Delegates to pnc_wakeup_dlc property (CODING_RULE_V2_00017)
        """
        return self.pnc_wakeup_dlc  # Delegates to property

    def setPncWakeupDlc(self, value: PositiveInteger) -> CanCommunicationConnector:
        """
        AUTOSAR-compliant setter for pncWakeupDlc with method chaining.

        Args:
            value: The pncWakeupDlc to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_wakeup_dlc property setter (gets validation automatically)
        """
        self.pnc_wakeup_dlc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_pnc_wakeup_can(self, value: Optional[PositiveInteger]) -> CanCommunicationConnector:
        """
        Set pncWakeupCan and return self for chaining.

        Args:
            value: The pncWakeupCan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_wakeup_can("value")
        """
        self.pnc_wakeup_can = value  # Use property setter (gets validation)
        return self

    def with_pnc_wakeup(self, value: Optional["PositiveUnlimitedInteger"]) -> CanCommunicationConnector:
        """
        Set pncWakeup and return self for chaining.

        Args:
            value: The pncWakeup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_wakeup("value")
        """
        self.pnc_wakeup = value  # Use property setter (gets validation)
        return self

    def with_pnc_wakeup_dlc(self, value: Optional[PositiveInteger]) -> CanCommunicationConnector:
        """
        Set pncWakeupDlc and return self for chaining.

        Args:
            value: The pncWakeupDlc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_wakeup_dlc("value")
        """
        self.pnc_wakeup_dlc = value  # Use property setter (gets validation)
        return self
