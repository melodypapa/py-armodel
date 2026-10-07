# This module contains AUTOSAR System Template IEEE1722TpAv classes
# (spec package M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv)

from __future__ import annotations

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpAvConnection


class IEEE1722TpCrfTypeEnum(AREnum):
    """
    Definition of the CRF stream type. Tags: atp.Status=candidate
    """

    # IEEE1722TpCrfTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.278, p.640
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on IEEE1722TpCrfConnection.crfType
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # CRF_AUDIO_SAMPLE, Audio sample timestamp Tags: atp.EnumerationLiteralIndex=0
    ENUM_AUDIO_SAMPLE = "AUDIO-SAMPLE"

    # CRF_MACHINE_CYCLE, Machine cycle timestamp Tags: atp.EnumerationLiteralIndex=3
    ENUM_MACHINE_CYCLE = "MACHINE-CYCLE"

    # CRF_USER, User specified Tags: atp.EnumerationLiteralIndex=4
    ENUM_USER = "USER"

    # CRF_VIDEO_FRAME, Video frame sync timestamp Tags: atp.EnumerationLiteralIndex=1
    ENUM_VIDEO_FRAME = "VIDEO-FRAME"

    # CRF_VIDEO_LINE, Video line sync timestamp Tags: atp.EnumerationLiteralIndex=2
    ENUM_VIDEO_LINE = "VIDEO-LINE"

    def __init__(self):
        super().__init__(
            [
                IEEE1722TpCrfTypeEnum.ENUM_AUDIO_SAMPLE,
                IEEE1722TpCrfTypeEnum.ENUM_MACHINE_CYCLE,
                IEEE1722TpCrfTypeEnum.ENUM_USER,
                IEEE1722TpCrfTypeEnum.ENUM_VIDEO_FRAME,
                IEEE1722TpCrfTypeEnum.ENUM_VIDEO_LINE,
            ]
        )


class IEEE1722TpCrfPullEnum(AREnum):
    """
    Definition of the CRF stream pull value. Tags: atp.Status=candidate
    """

    # IEEE1722TpCrfPullEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.279, p.641
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on IEEE1722TpCrfConnection.crfPull
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Multiply base_frequency field by 1.0 Tags: atp.EnumerationLiteralIndex=0 xml.name=1-0
    ENUM_1_0 = "1-0"

    # Multiply base_frequency field by 1.001 Tags: atp.EnumerationLiteralIndex=2 xml.name=1-001
    ENUM_1_001 = "1-001"

    # Multiply base_frequency field by 1/1.001 Tags: atp.EnumerationLiteralIndex=1 xml.name=1-1-001
    ENUM_1_1_001 = "1-1-001"

    # Multiply base_frequency field by 1/8 Tags: atp.EnumerationLiteralIndex=5 xml.name=1-8
    ENUM_1_8 = "1-8"

    # Multiply base_frequency field by 24/25 Tags: atp.EnumerationLiteralIndex=3 xml.name=24-25
    ENUM_24_25 = "24-25"

    # Multiply base_frequency field by 25/24 Tags: atp.EnumerationLiteralIndex=4 xml.name=25-24
    ENUM_25_24 = "25-24"

    def __init__(self):
        super().__init__(
            [
                IEEE1722TpCrfPullEnum.ENUM_1_0,
                IEEE1722TpCrfPullEnum.ENUM_1_001,
                IEEE1722TpCrfPullEnum.ENUM_1_1_001,
                IEEE1722TpCrfPullEnum.ENUM_1_8,
                IEEE1722TpCrfPullEnum.ENUM_24_25,
                IEEE1722TpCrfPullEnum.ENUM_25_24,
            ]
        )


class IEEE1722TpAafNominalRateEnum(AREnum):
    """
    Definition of the AAF nominal sample / frame rate. Tags: atp.Status=candidate
    """

    # IEEE1722TpAafNominalRateEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.281, p.644
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on IEEE1722TpAafConnection.aafNominalRate
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # 16 kHz Tags: atp.EnumerationLiteralIndex=2 xml.name=16-KHZ
    ENUM_16KHZ = "16-KHZ"

    # 176.4 kHz Tags: atp.EnumerationLiteralIndex=8 xml.name=176-4-KHZ
    ENUM_176_4KHZ = "176-4-KHZ"

    # 192 kHz Tags: atp.EnumerationLiteralIndex=9 xml.name=192-KHZ
    ENUM_192KHZ = "192-KHZ"

    # 24 kHz Tags: atp.EnumerationLiteralIndex=10 xml.name=24-KHZ
    ENUM_24KHZ = "24-KHZ"

    # 32 kHz Tags: atp.EnumerationLiteralIndex=3 xml.name=32-KHZ
    ENUM_32KHZ = "32-KHZ"

    # 44.1 kHz Tags: atp.EnumerationLiteralIndex=4 xml.name=44-1-KHZ
    ENUM_44_1KHZ = "44-1-KHZ"

    # 48 kHz Tags: atp.EnumerationLiteralIndex=5 xml.name=48-KHZ
    ENUM_48KHZ = "48-KHZ"

    # 88.2 kHz Tags: atp.EnumerationLiteralIndex=6 xml.name=88-2-KHZ
    ENUM_88_2KHZ = "88-2-KHZ"

    # 8 kHz Tags: atp.EnumerationLiteralIndex=1 xml.name=8-KHZ
    ENUM_8KHZ = "8-KHZ"

    # 96 kHz Tags: atp.EnumerationLiteralIndex=7 xml.name=96-KHZ
    ENUM_96KHZ = "96-KHZ"

    # User specified Tags: atp.EnumerationLiteralIndex=0
    ENUM_USER = "USER"

    def __init__(self):
        super().__init__(
            [
                IEEE1722TpAafNominalRateEnum.ENUM_16KHZ,
                IEEE1722TpAafNominalRateEnum.ENUM_176_4KHZ,
                IEEE1722TpAafNominalRateEnum.ENUM_192KHZ,
                IEEE1722TpAafNominalRateEnum.ENUM_24KHZ,
                IEEE1722TpAafNominalRateEnum.ENUM_32KHZ,
                IEEE1722TpAafNominalRateEnum.ENUM_44_1KHZ,
                IEEE1722TpAafNominalRateEnum.ENUM_48KHZ,
                IEEE1722TpAafNominalRateEnum.ENUM_8KHZ,
                IEEE1722TpAafNominalRateEnum.ENUM_88_2KHZ,
                IEEE1722TpAafNominalRateEnum.ENUM_96KHZ,
                IEEE1722TpAafNominalRateEnum.ENUM_USER,
            ]
        )


class IEEE1722TpAafFormatEnum(AREnum):
    """
    Definition of the AAF stream format. Tags: atp.Status=candidate
    """

    # IEEE1722TpAafFormatEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.282, p.644
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on IEEE1722TpAafConnection.aafFormat
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # AES3_32BIT, 32-bit AES3 format, AES3 Tags: atp.EnumerationLiteralIndex=5 xml.name=AES-3-32-BIT
    AES3_32BIT = "AES-3-32-BIT"

    # FLOAT_32BIT, 32bit floating, PCM Tags: atp.EnumerationLiteralIndex=1 xml.name=FLOAT-32-BIT
    FLOAT_32BIT = "FLOAT-32-BIT"

    # INT_16BIT, 16 bit integer, PCM Tags: atp.EnumerationLiteralIndex=4 xml.name=INT-16-BIT
    INT_16BIT = "INT-16-BIT"

    # INT_24BIT, 24 bit integer, PCM Tags: atp.EnumerationLiteralIndex=3 xml.name=INT-24-BIT
    INT_24BIT = "INT-24-BIT"

    # INT_32BIT, 32bit integer, PCM Tags: atp.EnumerationLiteralIndex=2 xml.name=INT-32-BIT
    INT_32BIT = "INT-32-BIT"

    # USER, user specific, PCM Tags: atp.EnumerationLiteralIndex=0
    USER = "USER"

    def __init__(self):
        super().__init__(
            [
                IEEE1722TpAafFormatEnum.AES3_32BIT,
                IEEE1722TpAafFormatEnum.FLOAT_32BIT,
                IEEE1722TpAafFormatEnum.INT_16BIT,
                IEEE1722TpAafFormatEnum.INT_24BIT,
                IEEE1722TpAafFormatEnum.INT_32BIT,
                IEEE1722TpAafFormatEnum.USER,
            ]
        )


class IEEE1722TpCrfConnection(IEEE1722TpAvConnection):
    """
    AV IEEE1722Tp CRF connection. Tags: atp.Status=candidate atp.recommendedPackage=IEEE1722TpConnections
    """

    # IEEE1722TpCrfConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.277, p.640
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseFrequency         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBaseFrequency         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCrfPull               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCrfPull               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCrfType               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCrfType               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFrameSyncEnabled      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFrameSyncEnabled      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimestampInterval     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimestampInterval     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Base row: ARElement, ARObject, CollectableElement, IEEE1722TpAvConnection, IEEE1722TpConnection, Identifiable, MultilanguageReferrable, PackageableElement, Referrable)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # CRF base frequency in Hz. Tags: atp.Status=candidate
        self.baseFrequency: Optional[PositiveInteger] = None

        # Definition of the CRF stream pull value.
        self.crfPull: Optional[IEEE1722TpCrfPullEnum] = None

        # Definition of the CRF stream type.
        self.crfType: Optional[IEEE1722TpCrfTypeEnum] = None

        # Defines whether the "fs" (frame sync) shall be enabled. Tags: atp.Status=candidate
        self.frameSyncEnabled: Optional[Boolean] = None

        # CRF timestamp interval as multiple of the baseFrequency. Tags: atp.Status=candidate
        self.timestampInterval: Optional[PositiveInteger] = None

    def getBaseFrequency(self) -> Optional[PositiveInteger]:
        """
        CRF base frequency in Hz. Tags: atp.Status=candidate
        """
        return self.baseFrequency

    def setBaseFrequency(self, value: Optional[PositiveInteger]) -> IEEE1722TpCrfConnection:
        """
        CRF base frequency in Hz. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing baseFrequency.
        """
        if value is not None:
            self.baseFrequency = value
        return self

    def getCrfPull(self) -> Optional[IEEE1722TpCrfPullEnum]:
        """
        Definition of the CRF stream pull value.
        """
        return self.crfPull

    def setCrfPull(self, value: Optional[IEEE1722TpCrfPullEnum]) -> IEEE1722TpCrfConnection:
        """
        Definition of the CRF stream pull value.
        A None value is a no-op and does not overwrite an existing crfPull.
        """
        if value is not None:
            self.crfPull = value
        return self

    def getCrfType(self) -> Optional[IEEE1722TpCrfTypeEnum]:
        """
        Definition of the CRF stream type.
        """
        return self.crfType

    def setCrfType(self, value: Optional[IEEE1722TpCrfTypeEnum]) -> IEEE1722TpCrfConnection:
        """
        Definition of the CRF stream type.
        A None value is a no-op and does not overwrite an existing crfType.
        """
        if value is not None:
            self.crfType = value
        return self

    def getFrameSyncEnabled(self) -> Optional[Boolean]:
        """
        Defines whether the "fs" (frame sync) shall be enabled. Tags: atp.Status=candidate
        """
        return self.frameSyncEnabled

    def setFrameSyncEnabled(self, value: Optional[Boolean]) -> IEEE1722TpCrfConnection:
        """
        Defines whether the "fs" (frame sync) shall be enabled. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing frameSyncEnabled.
        """
        if value is not None:
            self.frameSyncEnabled = value
        return self

    def getTimestampInterval(self) -> Optional[PositiveInteger]:
        """
        CRF timestamp interval as multiple of the baseFrequency. Tags: atp.Status=candidate
        """
        return self.timestampInterval

    def setTimestampInterval(self, value: Optional[PositiveInteger]) -> IEEE1722TpCrfConnection:
        """
        CRF timestamp interval as multiple of the baseFrequency. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing timestampInterval.
        """
        if value is not None:
            self.timestampInterval = value
        return self
