"""
This module defines offset constraints in AUTOSAR timing specifications.

Offset constraints specify timing offsets relative to a reference event or time base.

Classes:
    OffsetTimingConstraint: Specifies timing offset requirements
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class OffsetTimingConstraint(TimingConstraint):
    """
    Specifies timing offset requirements in AUTOSAR timing specifications.
    This constraint defines a time offset relative to a reference event
    or time base.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the OffsetTimingConstraint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this offset constraint
            short_name: The unique short name of this offset constraint
        """
        super().__init__(parent, short_name)

        # Timing offset value
        self.offset: TimeValue = None

    def getOffset(self):
        """
        Gets the timing offset.

        Returns:
            TimeValue: The timing offset
        """
        return self.offset

    def setOffset(self, value):
        """
        Sets the timing offset.

        Args:
            value: The timing offset to set

        Returns:
            self for method chaining
        """
        self.offset = value
        return self
