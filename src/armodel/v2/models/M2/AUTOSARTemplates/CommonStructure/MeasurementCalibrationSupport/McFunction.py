from typing import Union, List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class McFunction(ARObject):
    """
    Represents an MC (Measurement and Calibration) function in AUTOSAR.
    Defines a function that can be used for measurement and calibration purposes.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the McFunction with default values.
        """
        super().__init__()
        self.dataRefs: List[RefType] = []
        self.functionName: Union[str, None] = None

    def addDataRef(self, ref: RefType):
        """
        Adds a data reference to this MC function.

        Args:
            ref: The data reference to add

        Returns:
            self for method chaining
        """
        self.dataRefs.append(ref)
        return self

    def getDataRefs(self) -> List[RefType]:
        """
        Gets the list of data references.

        Returns:
            List of data references
        """
        return self.dataRefs

    def getFunctionName(self) -> str:
        """
        Gets the function name.

        Returns:
            String representing the function name
        """
        return self.functionName

    def setFunctionName(self, value: str):
        """
        Sets the function name.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.functionName = value
        return self
