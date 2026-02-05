from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptAccessEnum import RptAccessEnum


class RptExecutableEntity(ARObject):
    """
    Represents an RPT executable entity in AUTOSAR.
    Defines an executable entity that supports read-protect-transform functionality.
    """

    def __init__(self):
        """
        Initializes the RptExecutableEntity with default values.
        """
        super().__init__()
        self.executableEntityRef: RefType = None
        self.rptAccess: RptAccessEnum = None

    def getExecutableEntityRef(self) -> RefType:
        """
        Gets the executable entity reference.

        Returns:
            Reference to the executable entity
        """
        return self.executableEntityRef

    def setExecutableEntityRef(self, value: RefType):
        """
        Sets the executable entity reference.

        Args:
            value: The executable entity reference to set

        Returns:
            self for method chaining
        """
        self.executableEntityRef = value
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