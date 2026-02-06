"""
This module contains the AnyInstanceRef class for AUTOSAR models
in the GenericStructure module.
"""

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class AnyInstanceRef(AtpInstanceRef):
    """
    Represents a generic instance reference in AUTOSAR models.
    This class defines the structure for referencing any type of instance.
    """

    def __init__(self):
        super().__init__()

        self.baseRef: Optional[RefType] = None
        self.contextElementRefs: List[RefType] = []
        self.targetRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Gets the base reference.

        Returns:
            RefType representing the base reference, or None if not set
        """
        return self.baseRef

    def setBaseRef(self, value: RefType):
        """
        Sets the base reference.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        self.baseRef = value
        return self

    def getContextElementRefs(self) -> List[RefType]:
        """
        Gets the list of context element references.

        Returns:
            List of RefType instances representing context element references
        """
        return self.contextElementRefs

    def addContextElementRef(self, value: RefType):
        """
        Adds a context element reference.

        Args:
            value: The context element reference to add

        Returns:
            self for method chaining
        """
        self.contextElementRefs.append(value)
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """
        Gets the target reference.

        Returns:
            RefType representing the target reference, or None if not set
        """
        return self.targetRef

    def setTargetRef(self, value: RefType):
        """
        Sets the target reference.

        Args:
            value: The target reference to set

        Returns:
            self for method chaining
        """
        self.targetRef = value
        return self
