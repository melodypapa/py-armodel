from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptAccessEnum import (
    RptAccessEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptExecutableEntityEvent(ARObject):
    """
    Represents an RPT executable entity event in AUTOSAR.
    Defines an event associated with an RPT executable entity.
    """


    def __init__(self) -> None:
        """
        Initializes the RptExecutableEntityEvent with default values.
        """
        super().__init__()
        self.eventRef: Union[Union[RefType, None] , None] = None
        self.rptAccess: Union[Union[RptAccessEnum, None] , None] = None

    def getEventRef(self) -> Union[RefType, None]:
        """
        Gets the event reference.

        Returns:
            Reference to the event
        """
        return self.eventRef

    def setEventRef(self, value: RefType) -> "RptExecutableEntityEvent":
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
