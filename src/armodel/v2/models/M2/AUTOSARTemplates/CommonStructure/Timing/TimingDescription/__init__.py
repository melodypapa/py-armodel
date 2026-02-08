"""
V2 M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription package.
"""

from .TimingDescription import *

# Classes:
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import TimingDescription
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescriptionEvent import TimingDescriptionEvent
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescriptionEventChain import TimingDescriptionEventChain

__all__ = [
    # .TimingDescription.*,
    "TimingDescription",
    "TimingDescriptionEvent",
    "TimingDescriptionEventChain",
]
