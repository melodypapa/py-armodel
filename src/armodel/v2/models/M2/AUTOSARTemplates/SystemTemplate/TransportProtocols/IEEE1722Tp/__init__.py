from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    TpConfig,
)


class IEEE1722TpConfig(TpConfig):
    """
    Definition of the IEEE1722Tp protocol.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 636, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of IEEE1722Tp connections.
        # atpVariation.
        self._tpConnection: List["IEEE1722TpConnection"] = []

    @property
    def tp_connection(self) -> List["IEEE1722TpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpConnection(self) -> List["IEEE1722TpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement

    RefType,
)


class IEEE1722TpConnection(ARElement, ABC):
    """
    Definition of the IEEE1722Tp protocol.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 637, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is IEEE1722TpConnection:
            raise TypeError("IEEE1722TpConnection is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional definition of the destination MAC address for this If no given then
        # macAddressStreamId is used as address.
        self._destinationMac: Optional["MacAddressString"] = None

    @property
    def destination_mac(self) -> Optional["MacAddressString"]:
        """Get destinationMac (Pythonic accessor)."""
        return self._destinationMac

    @destination_mac.setter
    def destination_mac(self, value: Optional["MacAddressString"]) -> None:
        """
        Set destinationMac with validation.

        Args:
            value: The destinationMac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationMac = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"destinationMac must be MacAddressString or None, got {type(value).__name__}"
            )
        self._destinationMac = value
        # MAC Address part of the Stream Id.
        # atp.
        # Status=candidate.
        self._macAddress: Optional["MacAddressString"] = None

    @property
    def mac_address(self) -> Optional["MacAddressString"]:
        """Get macAddress (Pythonic accessor)."""
        return self._macAddress

    @mac_address.setter
    def mac_address(self, value: Optional["MacAddressString"]) -> None:
        """
        Set macAddress with validation.

        Args:
            value: The macAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macAddress = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"macAddress must be MacAddressString or None, got {type(value).__name__}"
            )
        self._macAddress = value
        # Reference to the lower layer Pdu used for the transport.
        self._pdu: RefType = None

    @property
    def pdu(self) -> RefType:
        """Get pdu (Pythonic accessor)."""
        return self._pdu

    @pdu.setter
    def pdu(self, value: RefType) -> None:
        """
        Set pdu with validation.

        Args:
            value: The pdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdu = None
            return

        self._pdu = value
        # Unique Id part of the Stream Id.
        self._uniqueStreamId: Optional["PositiveInteger"] = None

    @property
    def unique_stream_id(self) -> Optional["PositiveInteger"]:
        """Get uniqueStreamId (Pythonic accessor)."""
        return self._uniqueStreamId

    @unique_stream_id.setter
    def unique_stream_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set uniqueStreamId with validation.

        Args:
            value: The uniqueStreamId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._uniqueStreamId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"uniqueStreamId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._uniqueStreamId = value
        # Version of the IEEE1722TP stream.
        self._version: Optional["PositiveInteger"] = None

    @property
    def version(self) -> Optional["PositiveInteger"]:
        """Get version (Pythonic accessor)."""
        return self._version

    @version.setter
    def version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set version with validation.

        Args:
            value: The version to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._version = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"version must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._version = value
        # Optional definition of the VLAN priority for this stream.
        self._vlanPriority: Optional["PositiveInteger"] = None

    @property
    def vlan_priority(self) -> Optional["PositiveInteger"]:
        """Get vlanPriority (Pythonic accessor)."""
        return self._vlanPriority

    @vlan_priority.setter
    def vlan_priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set vlanPriority with validation.

        Args:
            value: The vlanPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanPriority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"vlanPriority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._vlanPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationMac(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for destinationMac.

        Returns:
            The destinationMac value

        Note:
            Delegates to destination_mac property (CODING_RULE_V2_00017)
        """
        return self.destination_mac  # Delegates to property

    def setDestinationMac(self, value: "MacAddressString") -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for destinationMac with method chaining.

        Args:
            value: The destinationMac to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_mac property setter (gets validation automatically)
        """
        self.destination_mac = value  # Delegates to property setter
        return self

    def getMacAddress(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for macAddress.

        Returns:
            The macAddress value

        Note:
            Delegates to mac_address property (CODING_RULE_V2_00017)
        """
        return self.mac_address  # Delegates to property

    def setMacAddress(self, value: "MacAddressString") -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for macAddress with method chaining.

        Args:
            value: The macAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_address property setter (gets validation automatically)
        """
        self.mac_address = value  # Delegates to property setter
        return self

    def getPdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for pdu.

        Returns:
            The pdu value

        Note:
            Delegates to pdu property (CODING_RULE_V2_00017)
        """
        return self.pdu  # Delegates to property

    def setPdu(self, value: RefType) -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for pdu with method chaining.

        Args:
            value: The pdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to pdu property setter (gets validation automatically)
        """
        self.pdu = value  # Delegates to property setter
        return self

    def getUniqueStreamId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for uniqueStreamId.

        Returns:
            The uniqueStreamId value

        Note:
            Delegates to unique_stream_id property (CODING_RULE_V2_00017)
        """
        return self.unique_stream_id  # Delegates to property

    def setUniqueStreamId(self, value: "PositiveInteger") -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for uniqueStreamId with method chaining.

        Args:
            value: The uniqueStreamId to set

        Returns:
            self for method chaining

        Note:
            Delegates to unique_stream_id property setter (gets validation automatically)
        """
        self.unique_stream_id = value  # Delegates to property setter
        return self

    def getVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for version.

        Returns:
            The version value

        Note:
            Delegates to version property (CODING_RULE_V2_00017)
        """
        return self.version  # Delegates to property

    def setVersion(self, value: "PositiveInteger") -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for version with method chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Note:
            Delegates to version property setter (gets validation automatically)
        """
        self.version = value  # Delegates to property setter
        return self

    def getVlanPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for vlanPriority.

        Returns:
            The vlanPriority value

        Note:
            Delegates to vlan_priority property (CODING_RULE_V2_00017)
        """
        return self.vlan_priority  # Delegates to property

    def setVlanPriority(self, value: "PositiveInteger") -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for vlanPriority with method chaining.

        Args:
            value: The vlanPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan_priority property setter (gets validation automatically)
        """
        self.vlan_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_mac(self, value: Optional["MacAddressString"]) -> "IEEE1722TpConnection":
        """
        Set destinationMac and return self for chaining.

        Args:
            value: The destinationMac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_mac("value")
        """
        self.destination_mac = value  # Use property setter (gets validation)
        return self

    def with_mac_address(self, value: Optional["MacAddressString"]) -> "IEEE1722TpConnection":
        """
        Set macAddress and return self for chaining.

        Args:
            value: The macAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_address("value")
        """
        self.mac_address = value  # Use property setter (gets validation)
        return self

    def with_pdu(self, value: Optional[RefType]) -> "IEEE1722TpConnection":
        """
        Set pdu and return self for chaining.

        Args:
            value: The pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdu("value")
        """
        self.pdu = value  # Use property setter (gets validation)
        return self

    def with_unique_stream_id(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpConnection":
        """
        Set uniqueStreamId and return self for chaining.

        Args:
            value: The uniqueStreamId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unique_stream_id("value")
        """
        self.unique_stream_id = value  # Use property setter (gets validation)
        return self

    def with_version(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpConnection":
        """
        Set version and return self for chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_version("value")
        """
        self.version = value  # Use property setter (gets validation)
        return self

    def with_vlan_priority(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpConnection":
        """
        Set vlanPriority and return self for chaining.

        Args:
            value: The vlanPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan_priority("value")
        """
        self.vlan_priority = value  # Use property setter (gets validation)
        return self

from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpConnection

    RefType,
)


class IEEE1722TpAvConnection(IEEE1722TpConnection, ABC):
    """
    AV IEEE1722Tp connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 639, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is IEEE1722TpAvConnection:
            raise TypeError("IEEE1722TpAvConnection is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the time offset that is added to the current time at in order to get
        # the "presentation time" (in content shall be presented at the.
        self._maxTransitTime: Optional["TimeValue"] = None

    @property
    def max_transit_time(self) -> Optional["TimeValue"]:
        """Get maxTransitTime (Pythonic accessor)."""
        return self._maxTransitTime

    @max_transit_time.setter
    def max_transit_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set maxTransitTime with validation.

        Args:
            value: The maxTransitTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxTransitTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"maxTransitTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._maxTransitTime = value
        # Reference to the upper layer Sdu used for the transport of of the IEEE1722Tp.
        self._sdu: List[RefType] = []

    @property
    def sdu(self) -> List[RefType]:
        """Get sdu (Pythonic accessor)."""
        return self._sdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxTransitTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for maxTransitTime.

        Returns:
            The maxTransitTime value

        Note:
            Delegates to max_transit_time property (CODING_RULE_V2_00017)
        """
        return self.max_transit_time  # Delegates to property

    def setMaxTransitTime(self, value: "TimeValue") -> "IEEE1722TpAvConnection":
        """
        AUTOSAR-compliant setter for maxTransitTime with method chaining.

        Args:
            value: The maxTransitTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_transit_time property setter (gets validation automatically)
        """
        self.max_transit_time = value  # Delegates to property setter
        return self

    def getSdu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for sdu.

        Returns:
            The sdu value

        Note:
            Delegates to sdu property (CODING_RULE_V2_00017)
        """
        return self.sdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_transit_time(self, value: Optional["TimeValue"]) -> "IEEE1722TpAvConnection":
        """
        Set maxTransitTime and return self for chaining.

        Args:
            value: The maxTransitTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_transit_time("value")
        """
        self.max_transit_time = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpConnection,
)


class IEEE1722TpAcfConnection(IEEE1722TpConnection):
    """
    ACF IEEE1722Tp connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 656, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the transported busses over this ACF atpVariation.
        self._acfTransported: List["IEEE1722TpAcfBus"] = []

    @property
    def acf_transported(self) -> List["IEEE1722TpAcfBus"]:
        """Get acfTransported (Pythonic accessor)."""
        return self._acfTransported
        # When this timeout expires the IEEE1722Tp ACF is triggered for sending.
        # The respective timer is the first Pdu is put into the IEEE1722Tp seconds.
        self._collection: Optional["TimeValue"] = None

    @property
    def collection(self) -> Optional["TimeValue"]:
        """Get collection (Pythonic accessor)."""
        return self._collection

    @collection.setter
    def collection(self, value: Optional["TimeValue"]) -> None:
        """
        Set collection with validation.

        Args:
            value: The collection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._collection = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"collection must be TimeValue or None, got {type(value).__name__}"
            )
        self._collection = value
        # Defines if this ACF-stream is allowed to collect of different bus kinds (i.
        # e.
        # whether it is collect CAN and LIN ACF-messages in one.
        self._mixedBusType: Optional["Boolean"] = None

    @property
    def mixed_bus_type(self) -> Optional["Boolean"]:
        """Get mixedBusType (Pythonic accessor)."""
        return self._mixedBusType

    @mixed_bus_type.setter
    def mixed_bus_type(self, value: Optional["Boolean"]) -> None:
        """
        Set mixedBusType with validation.

        Args:
            value: The mixedBusType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mixedBusType = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"mixedBusType must be Boolean or None, got {type(value).__name__}"
            )
        self._mixedBusType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAcfTransported(self) -> List["IEEE1722TpAcfBus"]:
        """
        AUTOSAR-compliant getter for acfTransported.

        Returns:
            The acfTransported value

        Note:
            Delegates to acf_transported property (CODING_RULE_V2_00017)
        """
        return self.acf_transported  # Delegates to property

    def getCollection(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for collection.

        Returns:
            The collection value

        Note:
            Delegates to collection property (CODING_RULE_V2_00017)
        """
        return self.collection  # Delegates to property

    def setCollection(self, value: "TimeValue") -> "IEEE1722TpAcfConnection":
        """
        AUTOSAR-compliant setter for collection with method chaining.

        Args:
            value: The collection to set

        Returns:
            self for method chaining

        Note:
            Delegates to collection property setter (gets validation automatically)
        """
        self.collection = value  # Delegates to property setter
        return self

    def getMixedBusType(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for mixedBusType.

        Returns:
            The mixedBusType value

        Note:
            Delegates to mixed_bus_type property (CODING_RULE_V2_00017)
        """
        return self.mixed_bus_type  # Delegates to property

    def setMixedBusType(self, value: "Boolean") -> "IEEE1722TpAcfConnection":
        """
        AUTOSAR-compliant setter for mixedBusType with method chaining.

        Args:
            value: The mixedBusType to set

        Returns:
            self for method chaining

        Note:
            Delegates to mixed_bus_type property setter (gets validation automatically)
        """
        self.mixed_bus_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_collection(self, value: Optional["TimeValue"]) -> "IEEE1722TpAcfConnection":
        """
        Set collection and return self for chaining.

        Args:
            value: The collection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_collection("value")
        """
        self.collection = value  # Use property setter (gets validation)
        return self

    def with_mixed_bus_type(self, value: Optional["Boolean"]) -> "IEEE1722TpAcfConnection":
        """
        Set mixedBusType and return self for chaining.

        Args:
            value: The mixedBusType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mixed_bus_type("value")
        """
        self.mixed_bus_type = value  # Use property setter (gets validation)
        return self
