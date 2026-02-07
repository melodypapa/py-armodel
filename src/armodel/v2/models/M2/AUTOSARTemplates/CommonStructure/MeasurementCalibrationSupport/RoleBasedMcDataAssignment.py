from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RoleBasedMcDataAssignment(ARObject):
    """
    Represents a role-based MC (Measurement and Calibration) data assignment in AUTOSAR.
    Defines assignment of MC data based on roles.
    """


    def __init__(self) -> None:
        """
        Initializes the RoleBasedMcDataAssignment with default values.
        """
        super().__init__()
        self.dataRef: Union[Union[RefType, None] , None] = None
        self.role: Union[str, None] = None

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

    def getRole(self) -> str:
        """
        Gets the role.

        Returns:
            String representing the role
        """
        return self.role

    def setRole(self, value: str):
        """
        Sets the role.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.role = value
        return self
