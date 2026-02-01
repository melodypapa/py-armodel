from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptAccessEnum import RptAccessEnum


class RptSwPrototypingAccess(ARObject):
    """
    Represents RPT software prototyping access in AUTOSAR.
    Defines access controls for software prototyping through RPT.
    """

    def __init__(self):
        """
        Initializes the RptSwPrototypingAccess with default values.
        """
        super().__init__()
        self.portRef: RefType = None
        self.rptAccess: RptAccessEnum = None

    def getPortRef(self) -> RefType:
        """
        Gets the port reference.

        Returns:
            Reference to the port
        """
        return self.portRef

    def setPortRef(self, value: RefType):
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