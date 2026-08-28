"""
This module contains the SL-LET timing description event class
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventSLLET).
"""

from abc import ABC

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)


class TDEventSLLET(TimingDescriptionEvent, ABC):
    """
    Used to describe SL-LET (System-Level) timing events. Tags: atp.Status=draft
    """

    # TDEventSLLET method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.57, p.251
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent, short_name):
        if type(self) is TDEventSLLET:
            raise TypeError("TDEventSLLET is an abstract class.")
        super().__init__(parent, short_name)
