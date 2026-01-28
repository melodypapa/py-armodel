from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from typing import List


class McDataInstance(ARObject):
    """
    Represents an MC (Measurement and Calibration) data instance in AUTOSAR.
    Defines an instance of MC data that can be accessed or modified.
    """

    def __init__(self):
        """
        Initializes the McDataInstance with default values.
        """
        super().__init__()
        self.dataAccessDetails: List[RefType] = []
        self.dataRef: RefType = None

    def addDataAccessDetail(self, ref: RefType):
        """
        Adds a data access detail reference.

        Args:
            ref: The data access detail reference to add

        Returns:
            self for method chaining
        """
        self.dataAccessDetails.append(ref)
        return self

    def getDataAccessDetails(self) -> List[RefType]:
        """
        Gets the list of data access detail references.

        Returns:
            List of data access detail references
        """
        return self.dataAccessDetails

    def getDataRef(self) -> RefType:
        """
        Gets the data reference.

        Returns:
            Reference to the data
        """
        return self.dataRef

    def setDataRef(self, value: RefType):
        """
        Sets the data reference.

        Args:
            value: The data reference to set

        Returns:
            self for method chaining
        """
        self.dataRef = value
        return self