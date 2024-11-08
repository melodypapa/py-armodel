


from .....ar_ref import RModeGroupInAtomicSWCInstanceRef
from .....rpt_scenario import ModeAccessPointIdent
from .....ar_object import ARObject


class ModeAccessPoint(ARObject):
    def __init__(self):
        super().__init__()

        self.ident = None                   # type: ModeAccessPointIdent
        self.mode_group_iref = None         # type: RModeGroupInAtomicSWCInstanceRef

    @property
    def modeGroupIRef(self) -> RModeGroupInAtomicSWCInstanceRef:
        return self.mode_group_iref
    
    @modeGroupIRef.setter
    def modeGroupIRef(self, value: RModeGroupInAtomicSWCInstanceRef):
        self.mode_group_iref = value