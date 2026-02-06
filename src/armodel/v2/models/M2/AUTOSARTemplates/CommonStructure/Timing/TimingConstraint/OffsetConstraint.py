"""
This module defines offset constraints in AUTOSAR timing specifications.

Offset constraints specify timing offsets relative to a reference event or time base.

Classes:
    OffsetTimingConstraint: Specifies timing offset requirements
"""

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class OffsetTimingConstraint(TimingConstraint):
    """
    Specifies timing offset requirements in AUTOSAR timing specifications.
    This constraint defines a time offset relative to a reference event
    or time base.
    """

    def __init__(self, parent, short_name: str) -> None:
        """
        Initializes the OffsetTimingConstraint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this offset constraint
            short_name: The unique short name of this offset constraint
        """
        super().__init__(parent, short_name)

        # Timing offset value
        self.offset: Union[Union[TimeValue, None] , None] = None

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
