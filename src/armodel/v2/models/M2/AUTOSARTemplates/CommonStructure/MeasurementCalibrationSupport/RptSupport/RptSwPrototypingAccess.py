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


class RptSwPrototypingAccess(ARObject):
    """
    Represents RPT software prototyping access in AUTOSAR.
    Defines access controls for software prototyping through RPT.
    """


    def __init__(self) -> None:
        """
        Initializes the RptSwPrototypingAccess with default values.
        """
        super().__init__()
        self.portRef: Union[Union[RefType, None] , None] = None
        self.rptAccess: Union[Union[RptAccessEnum, None] , None] = None

    def getPortRef(self) -> Union[RefType, None]:
        """
        Gets the port reference.

        Returns:
            Reference to the port
        """
        return self.portRef

    def setPortRef(self, value: RefType) -> "RptSwPrototypingAccess":
        """
        Sets the port reference.

        Args:
            value: The port reference to set

        Returns:
            self for method chaining
        """
        self.portRef = value
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
