"""
This module contains classes for representing AUTOSAR trigger elements
in software component internal behavior templates.
"""

from .....M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from .....M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


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


class ExternalTriggeringPointIdent(AbstractAccessPoint):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


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
