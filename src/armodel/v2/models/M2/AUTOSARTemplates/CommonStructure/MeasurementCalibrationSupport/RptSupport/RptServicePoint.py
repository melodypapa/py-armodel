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


class RptServicePoint(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    Represents an RPT service point in AUTOSAR.
    Defines a service point that supports read-protect-transform functionality.
    """


    def __init__(self) -> None:
        """
        Initializes the RptServicePoint with default values.
        """
        super().__init__()
        self.operationRef: Union[Union[RefType, None] , None] = None
        self.rptAccess: Union[Union[RptAccessEnum, None] , None] = None

    def getOperationRef(self) -> Union[RefType, None]:
        """
        Gets the operation reference.

        Returns:
            Reference to the operation
        """
        return self.operationRef

    def setOperationRef(self, value: RefType) -> "RptServicePoint":
        """
        Sets the operation reference.

        Args:
            value: The operation reference to set

        Returns:
            self for method chaining
        """
        self.operationRef = value
        return self

    def getRptAccess(self) -> Union[RptAccessEnum, None]:
        """
        Gets the RPT access type.

        Returns:
            RPT access enum value
        """
        return self.rptAccess

    def setRptAccess(self, value: RptAccessEnum) -> "RptServicePoint":
        """
        Sets the RPT access type.

        Args:
            value: RPT access enum value to set

        Returns:
            self for method chaining
        """
        self.rptAccess = value
        return self
