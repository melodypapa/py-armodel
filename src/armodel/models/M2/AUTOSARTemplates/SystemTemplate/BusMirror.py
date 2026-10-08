"""
This module contains AUTOSAR System Template classes of the BusMirror package.
"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


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
