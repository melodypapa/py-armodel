"""
This module contains classes for representing AUTOSAR trigger elements
in software component internal behavior templates.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import (
    ExternalTriggeringPointIdent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)


class InternalTriggeringPoint(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.swImplPolicy: SwImplPolicyEnum = None

    def getSwImplPolicy(self) -> SwImplPolicyEnum:
        return self.swImplPolicy

    def setSwImplPolicy(self, value: SwImplPolicyEnum):
        if value is not None:
            self.swImplPolicy = value
        return self


class ExternalTriggeringPoint(ARObject):
    def __init__(self):
        super().__init__()

        self.ident: ExternalTriggeringPointIdent = None
        self.trigger: Trigger = None

    def getIdent(self) -> ExternalTriggeringPointIdent:
        return self.ident

    def setIdent(self, value: ExternalTriggeringPointIdent):
        if value is not None:
            self.ident = value
        return self

    def getTrigger(self) -> Trigger:
        return self.trigger

    def setTrigger(self, value: Trigger):
        if value is not None:
            self.trigger = value
        return self
