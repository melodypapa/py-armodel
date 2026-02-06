from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class McFunctionDataRefSet(ARObject):
    """
    Represents a set of MC function data references in AUTOSAR.
    Defines a collection of references to MC (Measurement and Calibration) function data.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the McFunctionDataRefSet with default values.
        """
        super().__init__()
        self.dataRefs: List[RefType] = []

    def addDataRef(self, ref: RefType):
        """
        Adds a data reference to this MC function data reference set.

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
