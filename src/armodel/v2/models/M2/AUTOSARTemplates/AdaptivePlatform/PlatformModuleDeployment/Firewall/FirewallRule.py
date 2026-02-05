from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class FirewallRule(ARObject):
    """
    Represents a firewall rule in AUTOSAR Adaptive Platform PlatformModuleDeployment.
    Defines rules for firewall configuration in adaptive platform modules.
    """

    def __init__(self):
        """
        Initializes the FirewallRule with default values.
        """
        super().__init__()
        self.destRefs: List[RefType] = []
        self.srcRefs: List[RefType] = []

    def addDestRef(self, ref: RefType):
        """
        Adds a destination reference to this firewall rule.

        Args:
            ref: The destination reference to add

        Returns:
            self for method chaining
        """
        self.destRefs.append(ref)
        return self

    def getDestRefs(self) -> List[RefType]:
        """
        Gets the list of destination references.

        Returns:
            List of destination references
        """
        return self.destRefs

    def addSrcRef(self, ref: RefType):
        """
        Adds a source reference to this firewall rule.

        Args:
            ref: The source reference to add

        Returns:
            self for method chaining
        """
        self.srcRefs.append(ref)
        return self

    def getSrcRefs(self) -> List[RefType]:
        """
        Gets the list of source references.

        Returns:
            List of source references
        """
        return self.srcRefs
