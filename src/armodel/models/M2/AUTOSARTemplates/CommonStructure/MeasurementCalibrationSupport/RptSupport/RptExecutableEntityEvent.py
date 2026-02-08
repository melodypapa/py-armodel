from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptAccessEnum import (
    RptAccessEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptExecutableEntityEvent(ARObject):
    """
    Represents an RPT executable entity event in AUTOSAR.
    Defines an event associated with an RPT executable entity.
    """

    def __init__(self):
        """
        Initializes the RptExecutableEntityEvent with default values.
        """
        super().__init__()
        self.eventRef: RefType = None
        self.rptAccess: RptAccessEnum = None

    def getEventRef(self) -> RefType:
        """
        Gets the event reference.

        Returns:
            Reference to the event
        """
        return self.eventRef

    def setEventRef(self, value: RefType):
        """
        Sets the event reference.

        Args:
            value: The event reference to set

        Returns:
            self for method chaining
        """
        self.eventRef = value
        return self

    def getRptAccess(self) -> RptAccessEnum:
        """
        Gets the RPT access type.

        Returns:
            RPT access enum value
        """
        return self.rptAccess

    def setRptAccess(self, value: RptAccessEnum):
        """
        Sets the RPT access type.

        Args:
            value: RPT access enum value to set

        Returns:
            self for method chaining
        """
        self.rptAccess = value
        return self
