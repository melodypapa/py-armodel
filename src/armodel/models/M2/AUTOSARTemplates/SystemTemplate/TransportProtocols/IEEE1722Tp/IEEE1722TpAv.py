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
