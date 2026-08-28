"""
This module contains the Complex timing description event class
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventComplex).
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)


class TDEventComplex(TimingDescriptionEvent):
    """
    This is used to describe complex timing events. The context of a complex timing event either is described informally, e.g. using the documentation block, or is described formally by the associated TDEventOccurrenceExpression.
    """

    # TDEventComplex method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.48, p.78
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)
