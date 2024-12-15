from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SoftwareContext(ARObject):
    def __init__(self):
        super().__init__()

        self.input = None                       # type: String
        self.state = None                       # type: String

    def getInput(self):
        return self.input

    def setInput(self, value):
        self.input = value
        return self

    def getState(self):
        return self.state

    def setState(self, value):
        self.state = value
        return self
