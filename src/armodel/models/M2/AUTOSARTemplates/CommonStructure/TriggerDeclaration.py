from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class Trigger(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.swImplPolicy = None                                # type: SwImplPolicyEnum
        self.triggerPeriod = None                               # type: MultidimensionalTime

    def getSwImplPolicy(self):
        return self.swImplPolicy

    def setSwImplPolicy(self, value):
        if value is not None:
            self.swImplPolicy = value
        return self

    def getTriggerPeriod(self):
        return self.triggerPeriod

    def setTriggerPeriod(self, value):
        if value is not None:
            self.triggerPeriod = value
        return self
