"""
This module defines BSW service dependency in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class BswServiceDependency(ARObject):
    """
    Represents a BSW service dependency in AUTOSAR.
    This class defines dependencies between BSW services.
    """

    def __init__(self):
        """
        Initializes the BswServiceDependency with default values.
        """
        super().__init__()
        self.requiredServiceRef: RefType = None

    def getRequiredServiceRef(self):
        return self.requiredServiceRef

    def setRequiredServiceRef(self, value):
        self.requiredServiceRef = value
        return self