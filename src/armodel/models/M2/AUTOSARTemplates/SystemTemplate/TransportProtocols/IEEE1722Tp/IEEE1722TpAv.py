# This module contains AUTOSAR System Template IEEE1722TpAv classes
# (spec package M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAv)

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


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
