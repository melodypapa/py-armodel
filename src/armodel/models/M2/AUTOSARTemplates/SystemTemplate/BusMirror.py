"""
This module contains AUTOSAR System Template classes of the BusMirror package.
"""

from __future__ import annotations

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger, RefType


class MirroringProtocolEnum(AREnum):
    """
    Eunumeration that defines the supported bus mirroring protocol options) with two literals.
    """

    # MirroringProtocolEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.326, p.697
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on BusMirrorChannelMapping.mirroringProtocol
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # mirroringProtocol is not used Tags: atp.EnumerationLiteralIndex=1
    NONE = "NONE"

    # version1 of the mirroringProtocol is used Tags: atp.EnumerationLiteralIndex=0
    VERSION1 = "VERSION-1"

    def __init__(self):
        super().__init__(
            [
                MirroringProtocolEnum.NONE,
                MirroringProtocolEnum.VERSION1,
            ]
        )


class BusMirrorChannel(ARObject):
    """
    This element assigns a busMirrorNetworkId to the referenced channel.
    """

    # BusMirrorChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.327, p.698
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBusMirrorNetworkId [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBusMirrorNetworkId [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getChannelRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setChannelRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute defines the networkId of the communication channel.
        self.busMirrorNetworkId: Optional[PositiveInteger] = None

        # Reference to PhysicalChannel that is used in the bus mirroring as sourceChannel or targetChannel. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=channel.physicalChannel, channel.variation Point.shortLabel vh.latestBindingTime=systemDesignTime
        self.channelRef: Optional[RefType] = None

    def getBusMirrorNetworkId(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the networkId of the communication channel.
        """
        return self.busMirrorNetworkId

    def setBusMirrorNetworkId(self, value: Optional[PositiveInteger]) -> BusMirrorChannel:
        """
        This attribute defines the networkId of the communication channel.

        A None value is a no-op and does not overwrite an existing busMirrorNetworkId.
        """
        if value is not None:
            self.busMirrorNetworkId = value
        return self

    def getChannelRef(self) -> Optional[RefType]:
        """
        Reference to PhysicalChannel that is used in the bus mirroring as sourceChannel or targetChannel. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=channel.physicalChannel, channel.variation Point.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.channelRef

    def setChannelRef(self, value: Optional[RefType]) -> BusMirrorChannel:
        """
        Reference to PhysicalChannel that is used in the bus mirroring as sourceChannel or targetChannel. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=channel.physicalChannel, channel.variation Point.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not overwrite an existing channelRef.
        """
        if value is not None:
            self.channelRef = value
        return self
