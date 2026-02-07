"""
This module defines synchronization point constraints in AUTOSAR timing specifications.

Synchronization point constraints specify synchronization requirements
between distributed AUTOSAR elements.

Classes:
    SynchronizationPointConstraint: Specifies synchronization point requirements
"""

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SynchronizationPointConstraint(TimingConstraint):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Specifies synchronization point requirements in AUTOSAR timing specifications.
    This constraint defines synchronization requirements between distributed
    AUTOSAR elements.
    """

    def __init__(self, parent, short_name: str) -> None:
        """
        Initializes the SynchronizationPointConstraint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this synchronization point constraint
            short_name: The unique short name of this synchronization point constraint
        """
        super().__init__(parent, short_name)

        # Synchronization point identifier
        self.synchronization_point: Union[Union[String, None] , None] = None

    def getSynchronizationPoint(self):
        """
        Gets the synchronization point identifier.

        Returns:
            String: The synchronization point identifier
        """
        return self.synchronization_point

    def setSynchronizationPoint(self, value):
        """
        Sets the synchronization point identifier.

        Args:
            value: The synchronization point identifier to set

        Returns:
            self for method chaining
        """
        self.synchronization_point = value
        return self
