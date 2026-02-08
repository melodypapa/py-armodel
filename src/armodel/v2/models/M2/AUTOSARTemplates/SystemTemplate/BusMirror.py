from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import (
    FibexElement,
)


class BusMirrorChannelMapping(FibexElement, ABC):
    """
    This element defines a bus mirroring in which the traffic from one
    communication bus (sourceChannel) is forwarded to another one
    (targetChannel).

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 697, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BusMirrorChannelMapping:
            raise TypeError("BusMirrorChannelMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the bus mirroring protocol that is in the
        # BusMirrorChannelMapping.
        self._mirroring: Optional["MirroringProtocolEnum"] = None

    @property
    def mirroring(self) -> Optional["MirroringProtocolEnum"]:
        """Get mirroring (Pythonic accessor)."""
        return self._mirroring

    @mirroring.setter
    def mirroring(self, value: Optional["MirroringProtocolEnum"]) -> None:
        """
        Set mirroring with validation.

        Args:
            value: The mirroring to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mirroring = None
            return

        if not isinstance(value, MirroringProtocolEnum):
            raise TypeError(
                f"mirroring must be MirroringProtocolEnum or None, got {type(value).__name__}"
            )
        self._mirroring = value
        # Defines the sourceChannel from which frames are.
        self._sourceChannel: Optional["BusMirrorChannel"] = None

    @property
    def source_channel(self) -> Optional["BusMirrorChannel"]:
        """Get sourceChannel (Pythonic accessor)."""
        return self._sourceChannel

    @source_channel.setter
    def source_channel(self, value: Optional["BusMirrorChannel"]) -> None:
        """
        Set sourceChannel with validation.

        Args:
            value: The sourceChannel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceChannel = None
            return

        if not isinstance(value, BusMirrorChannel):
            raise TypeError(
                f"sourceChannel must be BusMirrorChannel or None, got {type(value).__name__}"
            )
        self._sourceChannel = value
        # Defines the targetChannel to which frames are forwarded.
        self._targetChannel: Optional["BusMirrorChannel"] = None

    @property
    def target_channel(self) -> Optional["BusMirrorChannel"]:
        """Get targetChannel (Pythonic accessor)."""
        return self._targetChannel

    @target_channel.setter
    def target_channel(self, value: Optional["BusMirrorChannel"]) -> None:
        """
        Set targetChannel with validation.

        Args:
            value: The targetChannel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetChannel = None
            return

        if not isinstance(value, BusMirrorChannel):
            raise TypeError(
                f"targetChannel must be BusMirrorChannel or None, got {type(value).__name__}"
            )
        self._targetChannel = value
        # Reference to the PduTriggering that is used for of the mirrored frames on the
                # targetChannel.
        # that on FlexRay several targetPduTriggerings used.
        # For all other communication channels only targetPduTriggering is supported.
        # atpVariation.
        self._targetPdu: List[RefType] = []

    @property
    def target_pdu(self) -> List[RefType]:
        """Get targetPdu (Pythonic accessor)."""
        return self._targetPdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMirroring(self) -> "MirroringProtocolEnum":
        """
        AUTOSAR-compliant getter for mirroring.

        Returns:
            The mirroring value

        Note:
            Delegates to mirroring property (CODING_RULE_V2_00017)
        """
        return self.mirroring  # Delegates to property

    def setMirroring(self, value: "MirroringProtocolEnum") -> "BusMirrorChannelMapping":
        """
        AUTOSAR-compliant setter for mirroring with method chaining.

        Args:
            value: The mirroring to set

        Returns:
            self for method chaining

        Note:
            Delegates to mirroring property setter (gets validation automatically)
        """
        self.mirroring = value  # Delegates to property setter
        return self

    def getSourceChannel(self) -> "BusMirrorChannel":
        """
        AUTOSAR-compliant getter for sourceChannel.

        Returns:
            The sourceChannel value

        Note:
            Delegates to source_channel property (CODING_RULE_V2_00017)
        """
        return self.source_channel  # Delegates to property

    def setSourceChannel(self, value: "BusMirrorChannel") -> "BusMirrorChannelMapping":
        """
        AUTOSAR-compliant setter for sourceChannel with method chaining.

        Args:
            value: The sourceChannel to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_channel property setter (gets validation automatically)
        """
        self.source_channel = value  # Delegates to property setter
        return self

    def getTargetChannel(self) -> "BusMirrorChannel":
        """
        AUTOSAR-compliant getter for targetChannel.

        Returns:
            The targetChannel value

        Note:
            Delegates to target_channel property (CODING_RULE_V2_00017)
        """
        return self.target_channel  # Delegates to property

    def setTargetChannel(self, value: "BusMirrorChannel") -> "BusMirrorChannelMapping":
        """
        AUTOSAR-compliant setter for targetChannel with method chaining.

        Args:
            value: The targetChannel to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_channel property setter (gets validation automatically)
        """
        self.target_channel = value  # Delegates to property setter
        return self

    def getTargetPdu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for targetPdu.

        Returns:
            The targetPdu value

        Note:
            Delegates to target_pdu property (CODING_RULE_V2_00017)
        """
        return self.target_pdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mirroring(self, value: Optional["MirroringProtocolEnum"]) -> "BusMirrorChannelMapping":
        """
        Set mirroring and return self for chaining.

        Args:
            value: The mirroring to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mirroring("value")
        """
        self.mirroring = value  # Use property setter (gets validation)
        return self

    def with_source_channel(self, value: Optional["BusMirrorChannel"]) -> "BusMirrorChannelMapping":
        """
        Set sourceChannel and return self for chaining.

        Args:
            value: The sourceChannel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_channel("value")
        """
        self.source_channel = value  # Use property setter (gets validation)
        return self

    def with_target_channel(self, value: Optional["BusMirrorChannel"]) -> "BusMirrorChannelMapping":
        """
        Set targetChannel and return self for chaining.

        Args:
            value: The targetChannel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_channel("value")
        """
        self.target_channel = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class BusMirrorChannel(ARObject):
    """
    This element assigns a busMirrorNetworkId to the referenced channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 698, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the networkId of the communication.
        self._busMirror: Optional["PositiveInteger"] = None

    @property
    def bus_mirror(self) -> Optional["PositiveInteger"]:
        """Get busMirror (Pythonic accessor)."""
        return self._busMirror

    @bus_mirror.setter
    def bus_mirror(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set busMirror with validation.

        Args:
            value: The busMirror to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._busMirror = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"busMirror must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._busMirror = value
        # Reference to PhysicalChannel that is used in the bus sourceChannel or
                # targetChannel.
        # atpVariation.
        self._channel: Optional["PhysicalChannel"] = None

    @property
    def channel(self) -> Optional["PhysicalChannel"]:
        """Get channel (Pythonic accessor)."""
        return self._channel

    @channel.setter
    def channel(self, value: Optional["PhysicalChannel"]) -> None:
        """
        Set channel with validation.

        Args:
            value: The channel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._channel = None
            return

        if not isinstance(value, PhysicalChannel):
            raise TypeError(
                f"channel must be PhysicalChannel or None, got {type(value).__name__}"
            )
        self._channel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBusMirror(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for busMirror.

        Returns:
            The busMirror value

        Note:
            Delegates to bus_mirror property (CODING_RULE_V2_00017)
        """
        return self.bus_mirror  # Delegates to property

    def setBusMirror(self, value: "PositiveInteger") -> "BusMirrorChannel":
        """
        AUTOSAR-compliant setter for busMirror with method chaining.

        Args:
            value: The busMirror to set

        Returns:
            self for method chaining

        Note:
            Delegates to bus_mirror property setter (gets validation automatically)
        """
        self.bus_mirror = value  # Delegates to property setter
        return self

    def getChannel(self) -> "PhysicalChannel":
        """
        AUTOSAR-compliant getter for channel.

        Returns:
            The channel value

        Note:
            Delegates to channel property (CODING_RULE_V2_00017)
        """
        return self.channel  # Delegates to property

    def setChannel(self, value: "PhysicalChannel") -> "BusMirrorChannel":
        """
        AUTOSAR-compliant setter for channel with method chaining.

        Args:
            value: The channel to set

        Returns:
            self for method chaining

        Note:
            Delegates to channel property setter (gets validation automatically)
        """
        self.channel = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bus_mirror(self, value: Optional["PositiveInteger"]) -> "BusMirrorChannel":
        """
        Set busMirror and return self for chaining.

        Args:
            value: The busMirror to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bus_mirror("value")
        """
        self.bus_mirror = value  # Use property setter (gets validation)
        return self

    def with_channel(self, value: Optional["PhysicalChannel"]) -> "BusMirrorChannel":
        """
        Set channel and return self for chaining.

        Args:
            value: The channel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_channel("value")
        """
        self.channel = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import (
    BusMirrorChannelMapping,
)


class BusMirrorChannelMappingCan(BusMirrorChannelMapping):
    """
    This element defines the bus mirroring between a CAN or LIN sourceChannel
    and a CAN targetChannel.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 700, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Rules for remapping of a set of CAN IDs.
        self._canIdRange: List["BusMirrorCanIdRange"] = []

    @property
    def can_id_range(self) -> List["BusMirrorCanIdRange"]:
        """Get canIdRange (Pythonic accessor)."""
        return self._canIdRange
        # Rules for remapping of single CanIds.
        self._canIdToCanId: List["BusMirrorCanIdToCanId"] = []

    @property
    def can_id_to_can_id(self) -> List["BusMirrorCanIdToCanId"]:
        """Get canIdToCanId (Pythonic accessor)."""
        return self._canIdToCanId
        # Rules for remapping of single LIN Frames.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._linPidToCanId: List["BusMirrorLinPidToCan"] = []

    @property
    def lin_pid_to_can_id(self) -> List["BusMirrorLinPidToCan"]:
        """Get linPidToCanId (Pythonic accessor)."""
        return self._linPidToCanId
        # Base ID merged with the LIN frame ID to form the CAN required when a
        # BusMirrorChannel that refers to a the role channel is referenced in
        # sourceChannel.
        self._mirrorSourceLin: Optional["PositiveInteger"] = None

    @property
    def mirror_source_lin(self) -> Optional["PositiveInteger"]:
        """Get mirrorSourceLin (Pythonic accessor)."""
        return self._mirrorSourceLin

    @mirror_source_lin.setter
    def mirror_source_lin(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set mirrorSourceLin with validation.

        Args:
            value: The mirrorSourceLin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mirrorSourceLin = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"mirrorSourceLin must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._mirrorSourceLin = value
        # CAN ID of the CAN status frame.
        # configured, a status frame will be sent on the CAN that contains the state of
                # all active source.
        self._mirrorStatus: Optional["PositiveInteger"] = None

    @property
    def mirror_status(self) -> Optional["PositiveInteger"]:
        """Get mirrorStatus (Pythonic accessor)."""
        return self._mirrorStatus

    @mirror_status.setter
    def mirror_status(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set mirrorStatus with validation.

        Args:
            value: The mirrorStatus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mirrorStatus = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"mirrorStatus must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._mirrorStatus = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCanIdRange(self) -> List["BusMirrorCanIdRange"]:
        """
        AUTOSAR-compliant getter for canIdRange.

        Returns:
            The canIdRange value

        Note:
            Delegates to can_id_range property (CODING_RULE_V2_00017)
        """
        return self.can_id_range  # Delegates to property

    def getCanIdToCanId(self) -> List["BusMirrorCanIdToCanId"]:
        """
        AUTOSAR-compliant getter for canIdToCanId.

        Returns:
            The canIdToCanId value

        Note:
            Delegates to can_id_to_can_id property (CODING_RULE_V2_00017)
        """
        return self.can_id_to_can_id  # Delegates to property

    def getLinPidToCanId(self) -> List["BusMirrorLinPidToCan"]:
        """
        AUTOSAR-compliant getter for linPidToCanId.

        Returns:
            The linPidToCanId value

        Note:
            Delegates to lin_pid_to_can_id property (CODING_RULE_V2_00017)
        """
        return self.lin_pid_to_can_id  # Delegates to property

    def getMirrorSourceLin(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for mirrorSourceLin.

        Returns:
            The mirrorSourceLin value

        Note:
            Delegates to mirror_source_lin property (CODING_RULE_V2_00017)
        """
        return self.mirror_source_lin  # Delegates to property

    def setMirrorSourceLin(self, value: "PositiveInteger") -> "BusMirrorChannelMappingCan":
        """
        AUTOSAR-compliant setter for mirrorSourceLin with method chaining.

        Args:
            value: The mirrorSourceLin to set

        Returns:
            self for method chaining

        Note:
            Delegates to mirror_source_lin property setter (gets validation automatically)
        """
        self.mirror_source_lin = value  # Delegates to property setter
        return self

    def getMirrorStatus(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for mirrorStatus.

        Returns:
            The mirrorStatus value

        Note:
            Delegates to mirror_status property (CODING_RULE_V2_00017)
        """
        return self.mirror_status  # Delegates to property

    def setMirrorStatus(self, value: "PositiveInteger") -> "BusMirrorChannelMappingCan":
        """
        AUTOSAR-compliant setter for mirrorStatus with method chaining.

        Args:
            value: The mirrorStatus to set

        Returns:
            self for method chaining

        Note:
            Delegates to mirror_status property setter (gets validation automatically)
        """
        self.mirror_status = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mirror_source_lin(self, value: Optional["PositiveInteger"]) -> "BusMirrorChannelMappingCan":
        """
        Set mirrorSourceLin and return self for chaining.

        Args:
            value: The mirrorSourceLin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mirror_source_lin("value")
        """
        self.mirror_source_lin = value  # Use property setter (gets validation)
        return self

    def with_mirror_status(self, value: Optional["PositiveInteger"]) -> "BusMirrorChannelMappingCan":
        """
        Set mirrorStatus and return self for chaining.

        Args:
            value: The mirrorStatus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mirror_status("value")
        """
        self.mirror_status = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class BusMirrorCanIdRangeMapping(ARObject):
    """
    This element defines a rule for remapping a set of CAN IDs.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 702, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Base ID merged with the masked parts of the original ID to form the mapped
        # CAN ID.
        self._destinationBase: Optional["PositiveInteger"] = None

    @property
    def destination_base(self) -> Optional["PositiveInteger"]:
        """Get destinationBase (Pythonic accessor)."""
        return self._destinationBase

    @destination_base.setter
    def destination_base(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set destinationBase with validation.

        Args:
            value: The destinationBase to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationBase = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"destinationBase must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._destinationBase = value
        # Value to match masked original CAN IDs.
        self._sourceCanIdCode: Optional["PositiveInteger"] = None

    @property
    def source_can_id_code(self) -> Optional["PositiveInteger"]:
        """Get sourceCanIdCode (Pythonic accessor)."""
        return self._sourceCanIdCode

    @source_can_id_code.setter
    def source_can_id_code(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sourceCanIdCode with validation.

        Args:
            value: The sourceCanIdCode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceCanIdCode = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sourceCanIdCode must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sourceCanIdCode = value
        # Mask applied to original CAN IDs before comparison.
        self._sourceCanId: Optional["PositiveInteger"] = None

    @property
    def source_can_id(self) -> Optional["PositiveInteger"]:
        """Get sourceCanId (Pythonic accessor)."""
        return self._sourceCanId

    @source_can_id.setter
    def source_can_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sourceCanId with validation.

        Args:
            value: The sourceCanId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceCanId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sourceCanId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sourceCanId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationBase(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for destinationBase.

        Returns:
            The destinationBase value

        Note:
            Delegates to destination_base property (CODING_RULE_V2_00017)
        """
        return self.destination_base  # Delegates to property

    def setDestinationBase(self, value: "PositiveInteger") -> "BusMirrorCanIdRangeMapping":
        """
        AUTOSAR-compliant setter for destinationBase with method chaining.

        Args:
            value: The destinationBase to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_base property setter (gets validation automatically)
        """
        self.destination_base = value  # Delegates to property setter
        return self

    def getSourceCanIdCode(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sourceCanIdCode.

        Returns:
            The sourceCanIdCode value

        Note:
            Delegates to source_can_id_code property (CODING_RULE_V2_00017)
        """
        return self.source_can_id_code  # Delegates to property

    def setSourceCanIdCode(self, value: "PositiveInteger") -> "BusMirrorCanIdRangeMapping":
        """
        AUTOSAR-compliant setter for sourceCanIdCode with method chaining.

        Args:
            value: The sourceCanIdCode to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_can_id_code property setter (gets validation automatically)
        """
        self.source_can_id_code = value  # Delegates to property setter
        return self

    def getSourceCanId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sourceCanId.

        Returns:
            The sourceCanId value

        Note:
            Delegates to source_can_id property (CODING_RULE_V2_00017)
        """
        return self.source_can_id  # Delegates to property

    def setSourceCanId(self, value: "PositiveInteger") -> "BusMirrorCanIdRangeMapping":
        """
        AUTOSAR-compliant setter for sourceCanId with method chaining.

        Args:
            value: The sourceCanId to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_can_id property setter (gets validation automatically)
        """
        self.source_can_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_base(self, value: Optional["PositiveInteger"]) -> "BusMirrorCanIdRangeMapping":
        """
        Set destinationBase and return self for chaining.

        Args:
            value: The destinationBase to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_base("value")
        """
        self.destination_base = value  # Use property setter (gets validation)
        return self

    def with_source_can_id_code(self, value: Optional["PositiveInteger"]) -> "BusMirrorCanIdRangeMapping":
        """
        Set sourceCanIdCode and return self for chaining.

        Args:
            value: The sourceCanIdCode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_can_id_code("value")
        """
        self.source_can_id_code = value  # Use property setter (gets validation)
        return self

    def with_source_can_id(self, value: Optional["PositiveInteger"]) -> "BusMirrorCanIdRangeMapping":
        """
        Set sourceCanId and return self for chaining.

        Args:
            value: The sourceCanId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_can_id("value")
        """
        self.source_can_id = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class BusMirrorCanIdToCanIdMapping(ARObject):
    """
    This element defines a rule for remapping a single CAN ID.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 702, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the CanId on the targetChannel.
        self._remappedCanId: Optional["PositiveInteger"] = None

    @property
    def remapped_can_id(self) -> Optional["PositiveInteger"]:
        """Get remappedCanId (Pythonic accessor)."""
        return self._remappedCanId

    @remapped_can_id.setter
    def remapped_can_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set remappedCanId with validation.

        Args:
            value: The remappedCanId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remappedCanId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"remappedCanId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._remappedCanId = value
        # This reference points to the sourceFrame with sourceCan the sourceChannel.
        self._souceCanId: RefType = None

    @property
    def souce_can_id(self) -> RefType:
        """Get souceCanId (Pythonic accessor)."""
        return self._souceCanId

    @souce_can_id.setter
    def souce_can_id(self, value: RefType) -> None:
        """
        Set souceCanId with validation.

        Args:
            value: The souceCanId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._souceCanId = None
            return

        self._souceCanId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRemappedCanId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for remappedCanId.

        Returns:
            The remappedCanId value

        Note:
            Delegates to remapped_can_id property (CODING_RULE_V2_00017)
        """
        return self.remapped_can_id  # Delegates to property

    def setRemappedCanId(self, value: "PositiveInteger") -> "BusMirrorCanIdToCanIdMapping":
        """
        AUTOSAR-compliant setter for remappedCanId with method chaining.

        Args:
            value: The remappedCanId to set

        Returns:
            self for method chaining

        Note:
            Delegates to remapped_can_id property setter (gets validation automatically)
        """
        self.remapped_can_id = value  # Delegates to property setter
        return self

    def getSouceCanId(self) -> RefType:
        """
        AUTOSAR-compliant getter for souceCanId.

        Returns:
            The souceCanId value

        Note:
            Delegates to souce_can_id property (CODING_RULE_V2_00017)
        """
        return self.souce_can_id  # Delegates to property

    def setSouceCanId(self, value: RefType) -> "BusMirrorCanIdToCanIdMapping":
        """
        AUTOSAR-compliant setter for souceCanId with method chaining.

        Args:
            value: The souceCanId to set

        Returns:
            self for method chaining

        Note:
            Delegates to souce_can_id property setter (gets validation automatically)
        """
        self.souce_can_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_remapped_can_id(self, value: Optional["PositiveInteger"]) -> "BusMirrorCanIdToCanIdMapping":
        """
        Set remappedCanId and return self for chaining.

        Args:
            value: The remappedCanId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remapped_can_id("value")
        """
        self.remapped_can_id = value  # Use property setter (gets validation)
        return self

    def with_souce_can_id(self, value: Optional[RefType]) -> "BusMirrorCanIdToCanIdMapping":
        """
        Set souceCanId and return self for chaining.

        Args:
            value: The souceCanId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_souce_can_id("value")
        """
        self.souce_can_id = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class BusMirrorLinPidToCanIdMapping(ARObject):
    """
    This element defines a rule for remapping a single LIN Frame.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 702, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the CanId on the targetChannel.
        self._remappedCanId: Optional["PositiveInteger"] = None

    @property
    def remapped_can_id(self) -> Optional["PositiveInteger"]:
        """Get remappedCanId (Pythonic accessor)."""
        return self._remappedCanId

    @remapped_can_id.setter
    def remapped_can_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set remappedCanId with validation.

        Args:
            value: The remappedCanId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remappedCanId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"remappedCanId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._remappedCanId = value
        # This reference points to the sourceFrame with sourceCan the sourceChannel.
        self._sourceLinPid: RefType = None

    @property
    def source_lin_pid(self) -> RefType:
        """Get sourceLinPid (Pythonic accessor)."""
        return self._sourceLinPid

    @source_lin_pid.setter
    def source_lin_pid(self, value: RefType) -> None:
        """
        Set sourceLinPid with validation.

        Args:
            value: The sourceLinPid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceLinPid = None
            return

        self._sourceLinPid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRemappedCanId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for remappedCanId.

        Returns:
            The remappedCanId value

        Note:
            Delegates to remapped_can_id property (CODING_RULE_V2_00017)
        """
        return self.remapped_can_id  # Delegates to property

    def setRemappedCanId(self, value: "PositiveInteger") -> "BusMirrorLinPidToCanIdMapping":
        """
        AUTOSAR-compliant setter for remappedCanId with method chaining.

        Args:
            value: The remappedCanId to set

        Returns:
            self for method chaining

        Note:
            Delegates to remapped_can_id property setter (gets validation automatically)
        """
        self.remapped_can_id = value  # Delegates to property setter
        return self

    def getSourceLinPid(self) -> RefType:
        """
        AUTOSAR-compliant getter for sourceLinPid.

        Returns:
            The sourceLinPid value

        Note:
            Delegates to source_lin_pid property (CODING_RULE_V2_00017)
        """
        return self.source_lin_pid  # Delegates to property

    def setSourceLinPid(self, value: RefType) -> "BusMirrorLinPidToCanIdMapping":
        """
        AUTOSAR-compliant setter for sourceLinPid with method chaining.

        Args:
            value: The sourceLinPid to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_lin_pid property setter (gets validation automatically)
        """
        self.source_lin_pid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_remapped_can_id(self, value: Optional["PositiveInteger"]) -> "BusMirrorLinPidToCanIdMapping":
        """
        Set remappedCanId and return self for chaining.

        Args:
            value: The remappedCanId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remapped_can_id("value")
        """
        self.remapped_can_id = value  # Use property setter (gets validation)
        return self

    def with_source_lin_pid(self, value: Optional[RefType]) -> "BusMirrorLinPidToCanIdMapping":
        """
        Set sourceLinPid and return self for chaining.

        Args:
            value: The sourceLinPid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_lin_pid("value")
        """
        self.source_lin_pid = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import (
    BusMirrorChannelMapping,
)


class BusMirrorChannelMappingFlexray(BusMirrorChannelMapping):
    """
    This element defines the bus mirroring between a CAN, LIN or FlexRay
    sourceChannel and a FlexRay targetChannel.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 704, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Time in seconds after which the collection of source into the destination
                # frame is stopped and the sent at the latest.
        # destination frames are only sent when full or time stamp overflows.
        self._transmission: Optional["TimeValue"] = None

    @property
    def transmission(self) -> Optional["TimeValue"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["TimeValue"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"transmission must be TimeValue or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTransmission(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TimeValue") -> "BusMirrorChannelMappingFlexray":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transmission(self, value: Optional["TimeValue"]) -> "BusMirrorChannelMappingFlexray":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import (
    BusMirrorChannelMapping,
)


class BusMirrorChannelMappingIp(BusMirrorChannelMapping):
    """
    This element defines the bus mirroring between a CAN, LIN or FlexRay
    sourceChannel and an Ethernet IP targetChannel.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 705, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Time in seconds after which the collection of source into the destination
                # frame is stopped and the sent at the latest.
        # destination frames are only sent when full or time stamp overflows.
        self._transmission: Optional["TimeValue"] = None

    @property
    def transmission(self) -> Optional["TimeValue"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["TimeValue"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"transmission must be TimeValue or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTransmission(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TimeValue") -> "BusMirrorChannelMappingIp":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transmission(self, value: Optional["TimeValue"]) -> "BusMirrorChannelMappingIp":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import (
    BusMirrorChannelMapping,
)


class BusMirrorChannelMappingUserDefined(BusMirrorChannelMapping):
    """
    This element defines the bus mirroring between a CAN, LIN or FlexRay
    sourceChannel and a User Defined targetChannel.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 707, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Time in seconds after which the collection of source into the destination
                # frame is stopped and the sent at the latest.
        # destination frames are only sent when full or time stamp overflows.
        self._transmission: Optional["TimeValue"] = None

    @property
    def transmission(self) -> Optional["TimeValue"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["TimeValue"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"transmission must be TimeValue or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTransmission(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TimeValue") -> "BusMirrorChannelMappingUserDefined":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transmission(self, value: Optional["TimeValue"]) -> "BusMirrorChannelMappingUserDefined":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self
