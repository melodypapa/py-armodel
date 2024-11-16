
from abc import ABCMeta

from ..M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

from ..M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical
from ..M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from .fibex_core.core_communication import Frame, FrameTriggering

class LinFrame(Frame):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == LinFrame:
            raise NotImplementedError("LinFrame is an abstract class.")
        
        super().__init__(parent, short_name)

class LinUnconditionalFrame(LinFrame):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class LinFrameTriggering(FrameTriggering):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.identifier = None                          # type: ARNumerical
        self.linChecksum = None                         # type: ARLiteral

    def getIdentifier(self):
        return self.identifier

    def setIdentifier(self, value):
        self.identifier = value
        return self

    def getLinChecksum(self):
        return self.linChecksum

    def setLinChecksum(self, value):
        self.linChecksum = value
        return self
