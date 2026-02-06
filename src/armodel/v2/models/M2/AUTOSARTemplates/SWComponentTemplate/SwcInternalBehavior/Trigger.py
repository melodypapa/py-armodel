"""
This module contains classes for representing AUTOSAR trigger elements
in software component internal behavior templates.
"""

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import (
    Trigger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import (
    ExternalTriggeringPointIdent,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)
from armodel.v2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)


class InternalTriggeringPoint(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.swImplPolicy: Union[Union[SwImplPolicyEnum, None] , None] = None

    def getSwImplPolicy(self) -> SwImplPolicyEnum:
        return self.swImplPolicy

    def setSwImplPolicy(self, value: SwImplPolicyEnum):
        if value is not None:
            self.swImplPolicy = value
        return self


class ExternalTriggeringPoint(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.ident: Union[Union[ExternalTriggeringPointIdent, None] , None] = None
        self.trigger: Union[Union[Trigger, None] , None] = None

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
