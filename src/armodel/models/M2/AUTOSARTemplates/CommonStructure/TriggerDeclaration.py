from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ..GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class Trigger(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.swImplPolicy = None    # type: str
        self.triggerPeriod = None   # type: float