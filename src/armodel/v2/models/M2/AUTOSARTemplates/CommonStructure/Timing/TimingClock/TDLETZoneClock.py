from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TDLETZoneClock(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock
    Represents a TDLET zone clock in AUTOSAR timing specifications.
    Defines a clock for TDLET (Time Domain LET) zones.
    """


    def __init__(self) -> None:
        """
        Initializes the TDLETZoneClock with default values.
        """
        super().__init__()
        self.clockRef: Union[Union[RefType, None] , None] = None
        self.zoneRef: Union[Union[RefType, None] , None] = None

    def getClockRef(self) -> Union[RefType, None]:
        """
        Gets the clock reference.

        Returns:
            Reference to the clock
        """
        return self.clockRef

    def setClockRef(self, value: RefType) -> "TDLETZoneClock":
        """
        Sets the clock reference.

        Args:
            value: The clock reference to set

        Returns:
            self for method chaining
        """
        self.clockRef = value
        return self

    def getZoneRef(self) -> Union[RefType, None]:
        """
        Gets the zone reference.

        Returns:
            Reference to the zone
        """
        return self.zoneRef

    def setZoneRef(self, value: RefType) -> "TDLETZoneClock":
        """
        Sets the zone reference.

        Args:
            value: The zone reference to set

        Returns:
            self for method chaining
        """
        self.zoneRef = value
        return self
