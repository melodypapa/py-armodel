from typing import List

from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class McParameterElementGroup(ARObject):
    """
    Represents an MC (Measurement and Calibration) parameter element group in AUTOSAR.
    Defines a group of parameter elements for measurement and calibration purposes.
    """

    def __init__(self):
        """
        Initializes the McParameterElementGroup with default values.
        """
        super().__init__()
        self.parameterRefs: List[RefType] = []

    def addParameterRef(self, ref: RefType):
        """
        Adds a parameter reference to this MC parameter element group.

        Args:
            ref: The parameter reference to add

        Returns:
            self for method chaining
        """
        self.parameterRefs.append(ref)
        return self

    def getParameterRefs(self) -> List[RefType]:
        """
        Gets the list of parameter references.

        Returns:
            List of parameter references
        """
        return self.parameterRefs
