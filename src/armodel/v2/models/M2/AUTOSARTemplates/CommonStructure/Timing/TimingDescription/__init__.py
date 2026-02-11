"""
Timing Description package.

This module imports and re-exports classes from TimingDescription.py.
All class definitions are consolidated in TimingDescription.py.
"""

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescription,
    TimingDescriptionEventChain,
    TimingDescriptionEvent,
)

__all__ = [
    TimingDescription,
    TimingDescriptionEventChain,
    TimingDescriptionEvent,
]