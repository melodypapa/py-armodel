"""
This module defines age constraints in AUTOSAR timing specifications.

Age constraints specify the maximum allowed age of data between its creation
and its consumption, ensuring data freshness requirements are met.

Classes:
    AgeConstraint: Specifies the maximum allowed age of data
"""

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class AgeConstraint(TimingConstraint):
    """
    Specifies the maximum allowed age of data in AUTOSAR timing specifications.
    This constraint ensures that data is consumed within a specified time
    window after its creation, maintaining data freshness.
    """

    def __init__(self, parent, short_name: str):
        """
        Initializes the AgeConstraint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this age constraint
            short_name: The unique short name of this age constraint
        """
        super().__init__(parent, short_name)

        # Maximum allowed age of the data
        self.age: TimeValue = None

    def getAge(self):
        """
        Gets the maximum allowed age of the data.

        Returns:
            TimeValue: The maximum allowed age
        """
        return self.age

    def setAge(self, value):
        """
        Sets the maximum allowed age of the data.

        Args:
            value: The maximum allowed age to set

        Returns:
            self for method chaining
        """
        self.age = value
        return self
