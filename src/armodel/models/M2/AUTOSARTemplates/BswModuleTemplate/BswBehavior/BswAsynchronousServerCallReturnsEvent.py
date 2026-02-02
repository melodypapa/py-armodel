"""
This module defines BSW asynchronous server call returns event in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent


class BswAsynchronousServerCallReturnsEvent(BswEvent):
    """
    Represents a BSW asynchronous server call returns event in AUTOSAR.
    This event occurs when an asynchronous server call returns.
    """

    def __init__(self):
        """
        Initializes the BswAsynchronousServerCallReturnsEvent with default values.
        """
        super().__init__()
        self.serverCallPointRef: RefType = None

    def getServerCallPointRef(self):
        return self.serverCallPointRef

    def setServerCallPointRef(self, value):
        self.serverCallPointRef = value
        return self