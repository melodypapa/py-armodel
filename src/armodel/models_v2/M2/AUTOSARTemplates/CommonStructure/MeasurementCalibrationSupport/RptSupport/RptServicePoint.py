from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptAccessEnum import RptAccessEnum


class RptServicePoint(ARObject):
    """
    Represents an RPT service point in AUTOSAR.
    Defines a service point that supports read-protect-transform functionality.
    """

    def __init__(self):
        """
        Initializes the RptServicePoint with default values.
        """
        super().__init__()
        self.operationRef: RefType = None
        self.rptAccess: RptAccessEnum = None

    def getOperationRef(self) -> RefType:
        """
        Gets the operation reference.

        Returns:
            Reference to the operation
        """
        return self.operationRef

    def setOperationRef(self, value: RefType):
        """
        Sets the operation reference.

        Args:
            value: The operation reference to set

        Returns:
            self for method chaining
        """
        self.operationRef = value
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