"""
This module contains the direct members of the FibexCore package.
"""

from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    BusMirrorCanIdRangeMapping,
    BusMirrorCanIdToCanIdMapping,
    BusMirrorLinPidToCanIdMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import PackageableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannel, MirroringProtocolEnum


class FibexElement(PackageableElement, ABC):
    """
    ASAM FIBEX elements specifying Communication and Topology.
    """

    # FibexElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.64, p.2026
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is FibexElement:
            raise TypeError("FibexElement is an abstract class.")

        super().__init__(parent, short_name)


class BusMirrorChannelMapping(FibexElement, ABC):
    """
    This element defines a bus mirroring in which the traffic from one communication bus (sourceChannel) is forwarded to another one (targetChannel).
    """

    # BusMirrorChannelMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.325, p.697
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMirroringProtocol        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMirroringProtocol        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceChannel            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceChannel            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetChannel            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetChannel            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addTargetPduTriggeringRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetPduTriggeringRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is BusMirrorChannelMapping:
            raise TypeError("BusMirrorChannelMapping is an abstract class.")

        super().__init__(parent, short_name)

        # This attribute defines the bus mirroring protocol that is used in the BusMirrorChannelMapping
        self.mirroringProtocol: Optional[MirroringProtocolEnum] = None

        # Defines the sourceChannel from which frames are received. Stereotypes: atpSplitable Tags: atp.Splitkey=sourceChannel
        self.sourceChannel: Optional[BusMirrorChannel] = None

        # Defines the targetChannel to which frames are forwarded. Stereotypes: atpSplitable Tags: atp.Splitkey=targetChannel
        self.targetChannel: Optional[BusMirrorChannel] = None

        # Reference to the PduTriggering that is used for transmission of the mirrored frames on the targetChannel. Please note that on FlexRay several targetPduTriggerings may be used. For all other communication channels only a single targetPduTriggering is supported. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=targetPduTriggering.pduTriggering, target PduTriggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.targetPduTriggeringRefs: List[RefType] = []

    def getMirroringProtocol(self) -> Optional[MirroringProtocolEnum]:
        """
        This attribute defines the bus mirroring protocol that is used in the BusMirrorChannelMapping
        """
        return self.mirroringProtocol

    def setMirroringProtocol(self, value: Optional[MirroringProtocolEnum]) -> BusMirrorChannelMapping:
        """
        This attribute defines the bus mirroring protocol that is used in the BusMirrorChannelMapping

        A None value is a no-op and does not overwrite an existing mirroringProtocol.
        """
        if value is not None:
            self.mirroringProtocol = value
        return self

    def getSourceChannel(self) -> Optional[BusMirrorChannel]:
        """
        Defines the sourceChannel from which frames are received. Stereotypes: atpSplitable Tags: atp.Splitkey=sourceChannel
        """
        return self.sourceChannel

    def setSourceChannel(self, value: Optional[BusMirrorChannel]) -> BusMirrorChannelMapping:
        """
        Defines the sourceChannel from which frames are received. Stereotypes: atpSplitable Tags: atp.Splitkey=sourceChannel

        A None value is a no-op and does not overwrite an existing sourceChannel.
        """
        if value is not None:
            self.sourceChannel = value
        return self

    def getTargetChannel(self) -> Optional[BusMirrorChannel]:
        """
        Defines the targetChannel to which frames are forwarded. Stereotypes: atpSplitable Tags: atp.Splitkey=targetChannel
        """
        return self.targetChannel

    def setTargetChannel(self, value: Optional[BusMirrorChannel]) -> BusMirrorChannelMapping:
        """
        Defines the targetChannel to which frames are forwarded. Stereotypes: atpSplitable Tags: atp.Splitkey=targetChannel

        A None value is a no-op and does not overwrite an existing targetChannel.
        """
        if value is not None:
            self.targetChannel = value
        return self

    def addTargetPduTriggeringRef(self, value: Optional[RefType]) -> BusMirrorChannelMapping:
        """
        Reference to the PduTriggering that is used for transmission of the mirrored frames on the targetChannel. Please note that on FlexRay several targetPduTriggerings may be used. For all other communication channels only a single targetPduTriggering is supported. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=targetPduTriggering.pduTriggering, target PduTriggering.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not append a targetPduTriggeringRef.
        """
        if value is not None:
            self.targetPduTriggeringRefs.append(value)
        return self

    def getTargetPduTriggeringRefs(self) -> List[RefType]:
        """
        Reference to the PduTriggering that is used for transmission of the mirrored frames on the targetChannel. Please note that on FlexRay several targetPduTriggerings may be used. For all other communication channels only a single targetPduTriggering is supported. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=targetPduTriggering.pduTriggering, target PduTriggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.targetPduTriggeringRefs


class BusMirrorChannelMappingCan(BusMirrorChannelMapping):
    """
    This element defines the bus mirroring between a CAN or LIN sourceChannel and a CAN targetChannel. Tags: atp.recommendedPackage=BusMirrorChannelMappings
    """

    # BusMirrorChannelMappingCan method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.328, p.701
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addCanIdRangeMapping                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCanIdRangeMappings               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addCanIdToCanIdMapping              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCanIdToCanIdMappings             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addLinPidToCanIdMapping             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLinPidToCanIdMappings            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getMirrorSourceLinToCanRangeBaseId  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMirrorSourceLinToCanRangeBaseId  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMirrorStatusCanId                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMirrorStatusCanId                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Rules for remapping of a set of CAN IDs.
        self.canIdRangeMappings: List[BusMirrorCanIdRangeMapping] = []

        # Rules for remapping of single CanIds.
        self.canIdToCanIdMappings: List[BusMirrorCanIdToCanIdMapping] = []

        # Rules for remapping of single LIN Frames.
        self.linPidToCanIdMappings: List[BusMirrorLinPidToCanIdMapping] = []

        # Base ID merged with the LIN frame ID to form the CAN ID. Only required when a BusMirrorChannel that refers to a LinPhysicalChannel in the role channel is referenced in the role sourceChannel.
        self.mirrorSourceLinToCanRangeBaseId: Optional[PositiveInteger] = None

        # CAN ID of the CAN status frame. If configured, a status frame will be sent on the CAN destination bus that contains the state of all active source buses.
        self.mirrorStatusCanId: Optional[PositiveInteger] = None

    def addCanIdRangeMapping(self, value: Optional[BusMirrorCanIdRangeMapping]) -> BusMirrorChannelMappingCan:
        """
        Rules for remapping of a set of CAN IDs.

        A None value is a no-op and does not append a canIdRangeMapping.
        """
        if value is not None:
            self.canIdRangeMappings.append(value)
        return self

    def getCanIdRangeMappings(self) -> List[BusMirrorCanIdRangeMapping]:
        """
        Rules for remapping of a set of CAN IDs.
        """
        return self.canIdRangeMappings

    def addCanIdToCanIdMapping(self, value: Optional[BusMirrorCanIdToCanIdMapping]) -> BusMirrorChannelMappingCan:
        """
        Rules for remapping of single CanIds.

        A None value is a no-op and does not append a canIdToCanIdMapping.
        """
        if value is not None:
            self.canIdToCanIdMappings.append(value)
        return self

    def getCanIdToCanIdMappings(self) -> List[BusMirrorCanIdToCanIdMapping]:
        """
        Rules for remapping of single CanIds.
        """
        return self.canIdToCanIdMappings

    def addLinPidToCanIdMapping(self, value: Optional[BusMirrorLinPidToCanIdMapping]) -> BusMirrorChannelMappingCan:
        """
        Rules for remapping of single LIN Frames.

        A None value is a no-op and does not append a linPidToCanIdMapping.
        """
        if value is not None:
            self.linPidToCanIdMappings.append(value)
        return self

    def getLinPidToCanIdMappings(self) -> List[BusMirrorLinPidToCanIdMapping]:
        """
        Rules for remapping of single LIN Frames.
        """
        return self.linPidToCanIdMappings

    def getMirrorSourceLinToCanRangeBaseId(self) -> Optional[PositiveInteger]:
        """
        Base ID merged with the LIN frame ID to form the CAN ID. Only required when a BusMirrorChannel that refers to a LinPhysicalChannel in the role channel is referenced in the role sourceChannel.
        """
        return self.mirrorSourceLinToCanRangeBaseId

    def setMirrorSourceLinToCanRangeBaseId(self, value: Optional[PositiveInteger]) -> BusMirrorChannelMappingCan:
        """
        Base ID merged with the LIN frame ID to form the CAN ID. Only required when a BusMirrorChannel that refers to a LinPhysicalChannel in the role channel is referenced in the role sourceChannel.

        A None value is a no-op and does not overwrite an existing mirrorSourceLinToCanRangeBaseId.
        """
        if value is not None:
            self.mirrorSourceLinToCanRangeBaseId = value
        return self

    def getMirrorStatusCanId(self) -> Optional[PositiveInteger]:
        """
        CAN ID of the CAN status frame. If configured, a status frame will be sent on the CAN destination bus that contains the state of all active source buses.
        """
        return self.mirrorStatusCanId

    def setMirrorStatusCanId(self, value: Optional[PositiveInteger]) -> BusMirrorChannelMappingCan:
        """
        CAN ID of the CAN status frame. If configured, a status frame will be sent on the CAN destination bus that contains the state of all active source buses.

        A None value is a no-op and does not overwrite an existing mirrorStatusCanId.
        """
        if value is not None:
            self.mirrorStatusCanId = value
        return self


class BusMirrorChannelMappingFlexray(BusMirrorChannelMapping):
    """
    This element defines the bus mirroring between a CAN, LIN or FlexRay sourceChannel and a FlexRay targetChannel. Tags: atp.recommendedPackage=BusMirrorChannelMappings
    """

    # BusMirrorChannelMappingFlexray method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.332, p.704
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTransmissionDeadline      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransmissionDeadline      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Time in seconds after which the collection of source frames into the destination frame is stopped and the frame is sent at the latest. If omitted, destination frames are only sent when full or when the time stamp overflows.
        self.transmissionDeadline: Optional[TimeValue] = None

    def getTransmissionDeadline(self) -> Optional[TimeValue]:
        """
        Time in seconds after which the collection of source frames into the destination frame is stopped and the frame is sent at the latest. If omitted, destination frames are only sent when full or when the time stamp overflows.
        """
        return self.transmissionDeadline

    def setTransmissionDeadline(self, value: Optional[TimeValue]) -> BusMirrorChannelMappingFlexray:
        """
        Time in seconds after which the collection of source frames into the destination frame is stopped and the frame is sent at the latest. If omitted, destination frames are only sent when full or when the time stamp overflows.

        A None value is a no-op and does not overwrite an existing transmissionDeadline.
        """
        if value is not None:
            self.transmissionDeadline = value
        return self


class BusMirrorChannelMappingIp(BusMirrorChannelMapping):
    """
    This element defines the bus mirroring between a CAN, LIN or FlexRay sourceChannel and an Ethernet IP targetChannel.
    """

    # BusMirrorChannelMappingIp method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.333, p.706
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTransmissionDeadline      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransmissionDeadline      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Time in seconds after which the collection of source frames into the destination frame is stopped and the frame is sent at the latest. If omitted, destination frames are only sent when full or when the time stamp overflows.
        self.transmissionDeadline: Optional[TimeValue] = None

    def getTransmissionDeadline(self) -> Optional[TimeValue]:
        """
        Time in seconds after which the collection of source frames into the destination frame is stopped and the frame is sent at the latest. If omitted, destination frames are only sent when full or when the time stamp overflows.
        """
        return self.transmissionDeadline

    def setTransmissionDeadline(self, value: Optional[TimeValue]) -> BusMirrorChannelMappingIp:
        """
        Time in seconds after which the collection of source frames into the destination frame is stopped and the frame is sent at the latest. If omitted, destination frames are only sent when full or when the time stamp overflows.

        A None value is a no-op and does not overwrite an existing transmissionDeadline.
        """
        if value is not None:
            self.transmissionDeadline = value
        return self


class BusMirrorChannelMappingUserDefined(BusMirrorChannelMapping):
    """
    This element defines the bus mirroring between a CAN, LIN or FlexRay sourceChannel and a User Defined targetChannel. Tags: atp.recommendedPackage=BusMirrorChannelMappings
    """

    # BusMirrorChannelMappingUserDefined method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.334, p.707
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTransmissionDeadline      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransmissionDeadline      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Time in seconds after which the collection of source frames into the destination frame is stopped and the frame is sent at the latest. If omitted, destination frames are only sent when full or when the time stamp overflows.
        self.transmissionDeadline: Optional[TimeValue] = None

    def getTransmissionDeadline(self) -> Optional[TimeValue]:
        """
        Time in seconds after which the collection of source frames into the destination frame is stopped and the frame is sent at the latest. If omitted, destination frames are only sent when full or when the time stamp overflows.
        """
        return self.transmissionDeadline

    def setTransmissionDeadline(self, value: Optional[TimeValue]) -> BusMirrorChannelMappingUserDefined:
        """
        Time in seconds after which the collection of source frames into the destination frame is stopped and the frame is sent at the latest. If omitted, destination frames are only sent when full or when the time stamp overflows.

        A None value is a no-op and does not overwrite an existing transmissionDeadline.
        """
        if value is not None:
            self.transmissionDeadline = value
        return self
