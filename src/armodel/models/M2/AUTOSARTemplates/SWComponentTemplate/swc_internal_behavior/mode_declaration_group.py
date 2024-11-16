from .access_count import AbstractAccessPoint
from ..Components.InstanceRefs import PModeGroupInAtomicSwcInstanceRef, RModeGroupInAtomicSWCInstanceRef
from .....rpt_scenario import ModeAccessPointIdent
from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ModeAccessPoint(ARObject):
    def __init__(self):
        super().__init__()

        self.ident = None                   # type: ModeAccessPointIdent
        self.modeGroupIRef = None           # type: RModeGroupInAtomicSWCInstanceRef

    def getIdent(self):
        return self.ident

    def setIdent(self, value):
        self.ident = value
        return self

    def getModeGroupIRef(self):
        return self.modeGroupIRef

    def setModeGroupIRef(self, value):
        self.modeGroupIRef = value
        return self

class ModeSwitchPoint(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.modeGroupIRef = None           # type: PModeGroupInAtomicSwcInstanceRef

    def getModeGroupIRef(self):
        return self.modeGroupIRef

    def setModeGroupIRef(self, value):
        self.modeGroupIRef = value
        return self
