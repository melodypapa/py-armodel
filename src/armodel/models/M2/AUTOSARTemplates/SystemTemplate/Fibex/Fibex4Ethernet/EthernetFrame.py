# This module contains AUTOSAR System Template classes for Ethernet frames
# It defines Ethernet frame structures for network communication

from __future__ import annotations

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering


class AbstractEthernetFrame(Frame, ABC):
    """
    Ethernet specific attributes to the Frame.
    """

    # AbstractEthernetFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.229, p.578
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractEthernetFrame:
            raise TypeError("AbstractEthernetFrame is an abstract class.")

        super().__init__(parent, short_name)


class GenericEthernetFrame(AbstractEthernetFrame):
    """
    This element is used for EthernetFrames without additional attributes that are routed by the EthIf. Tags: atp.recommendedPackage=Frames
    """

    # GenericEthernetFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.231, p.579
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class Ieee1722TpEthernetFrame(AbstractEthernetFrame):
    """
    Ieee1722Tp Ethernet Frame Tags: atp.Status=obsolete atp.recommendedPackage=Frames
    """

    # Ieee1722TpEthernetFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.233, p.579
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRelativeRepresentationTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRelativeRepresentationTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStreamIdentifier            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStreamIdentifier            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubType                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSubType                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVersion                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVersion                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the time when content shall be presented (in seconds). The actual absolute time is creation time plus relative presentation time Tags: atp.Status=obsolete
        self.relativeRepresentationTime: Optional[TimeValue] = None

        # IEEE 1722 stream identifier. Tags: atp.Status=obsolete
        self.streamIdentifier: Optional[PositiveInteger] = None

        # Protocol type. Tags: atp.Status=obsolete
        self.subType: Optional[PositiveInteger] = None

        # Revision of Ieee1722 standard. Tags: atp.Status=obsolete
        self.version: Optional[PositiveInteger] = None

    def getRelativeRepresentationTime(self) -> Optional[TimeValue]:
        """
        Defines the time when content shall be presented (in seconds). The actual absolute time is creation time plus relative presentation time Tags: atp.Status=obsolete
        """

        return self.relativeRepresentationTime

    def setRelativeRepresentationTime(self, value: Optional[TimeValue]) -> Ieee1722TpEthernetFrame:
        """
        Defines the time when content shall be presented (in seconds). The actual absolute time is creation time plus relative presentation time Tags: atp.Status=obsolete

        A None value is a no-op and does not overwrite an existing relativeRepresentationTime.
        """

        if value is not None:
            self.relativeRepresentationTime = value
        return self

    def getStreamIdentifier(self) -> Optional[PositiveInteger]:
        """
        IEEE 1722 stream identifier. Tags: atp.Status=obsolete
        """

        return self.streamIdentifier

    def setStreamIdentifier(self, value: Optional[PositiveInteger]) -> Ieee1722TpEthernetFrame:
        """
        IEEE 1722 stream identifier. Tags: atp.Status=obsolete

        A None value is a no-op and does not overwrite an existing streamIdentifier.
        """

        if value is not None:
            self.streamIdentifier = value
        return self

    def getSubType(self) -> Optional[PositiveInteger]:
        """
        Protocol type. Tags: atp.Status=obsolete
        """

        return self.subType

    def setSubType(self, value: Optional[PositiveInteger]) -> Ieee1722TpEthernetFrame:
        """
        Protocol type. Tags: atp.Status=obsolete

        A None value is a no-op and does not overwrite an existing subType.
        """

        if value is not None:
            self.subType = value
        return self

    def getVersion(self) -> Optional[PositiveInteger]:
        """
        Revision of Ieee1722 standard. Tags: atp.Status=obsolete
        """

        return self.version

    def setVersion(self, value: Optional[PositiveInteger]) -> Ieee1722TpEthernetFrame:
        """
        Revision of Ieee1722 standard. Tags: atp.Status=obsolete

        A None value is a no-op and does not overwrite an existing version.
        """

        if value is not None:
            self.version = value
        return self


class UserDefinedEthernetFrame(AbstractEthernetFrame):
    """
    UserDefinedEthernetFrame allows the description of a frame-based communication to Complex Drivers that are located above the EthDrv. Tags: atp.recommendedPackage=Frames
    """

    # UserDefinedEthernetFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.232, p.579
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EthernetFrameTriggering(FrameTriggering):
    """
    Ethernet specific Frame element.
    """

    # EthernetFrameTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.230, p.578
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
