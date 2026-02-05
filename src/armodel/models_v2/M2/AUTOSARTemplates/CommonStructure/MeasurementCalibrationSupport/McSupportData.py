from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from typing import List


class McSupportData(ARObject):
    """
    Represents MC (Measurement and Calibration) support data in AUTOSAR.
    Defines data structures for supporting measurement and calibration functionality.
    """

    def __init__(self):
        """
        Initializes the McSupportData with default values.
        """
        super().__init__()
        self.dataInstances: List[RefType] = []
        self.functions: List[RefType] = []

    def addDataInstance(self, ref: RefType):
        """
        Adds a data instance reference.

        Args:
            ref: The data instance reference to add

        Returns:
            self for method chaining
        """
        self.dataInstances.append(ref)
        return self

    def getDataInstances(self) -> List[RefType]:
        """
        Gets the list of data instance references.

        Returns:
            List of data instance references
        """
        return self.dataInstances

    def addFunction(self, ref: RefType):
        """
        Adds a function reference.

        Args:
            ref: The function reference to add

        Returns:
            self for method chaining
        """
        self.functions.append(ref)
        return self

    def getFunctions(self) -> List[RefType]:
        """
        Gets the list of function references.

        Returns:
            List of function references
        """
        return self.functions