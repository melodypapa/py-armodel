from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TDLETZoneClock(ARObject):
    """
    Represents a TDLET zone clock in AUTOSAR timing specifications.
    Defines a clock for TDLET (Time Domain LET) zones.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        """
        Initializes the TDLETZoneClock with default values.
        """
        super().__init__()
        self.clockRef: RefType = None
        self.zoneRef: RefType = None

    def getClockRef(self) -> RefType:
        """
        Gets the clock reference.

        Returns:
            Reference to the clock
        """
        return self.clockRef

    def setClockRef(self, value: RefType):
        """
        Sets the clock reference.

        Args:
            value: The clock reference to set

        Returns:
            self for method chaining
        """
        self.clockRef = value
        return self

    def getZoneRef(self) -> RefType:
        """
        Gets the zone reference.

        Returns:
            Reference to the zone
        """
        return self.zoneRef

    def setZoneRef(self, value: RefType):
        """
        Sets the zone reference.

        Args:
            value: The zone reference to set

        Returns:
            self for method chaining
        """
        self.zoneRef = value
        return self
