from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
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


class TriggerMapping(ARObject):
    def __init__(self):
        super().__init__()

        self.firstTriggerRef = None                             # type: RefType
        self.secondTriggerRef = None                            # type: RefType

    def getFirstTriggerRef(self):
        return self.firstTriggerRef

    def setFirstTriggerRef(self, value):
        if value is not None:
            self.firstTriggerRef = value
        return self

    def getSecondTriggerRef(self):
        return self.secondTriggerRef

    def setSecondTriggerRef(self, value):
        if value is not None:
            self.secondTriggerRef = value
        return self
