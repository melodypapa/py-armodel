"""
This module contains classes for representing AUTOSAR trigger elements
in software component internal behavior templates.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import IdentCaption


class InternalTriggeringPoint(AbstractAccessPoint):
    """
    An internal triggering point that can be referenced by an
    InternalTriggerOccurredEvent.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.swImplPolicy: SwImplPolicyEnum = None

    def getSwImplPolicy(self) -> SwImplPolicyEnum:
        """
        Gets the software implementation policy.

        Returns:
            SwImplPolicyEnum: The software implementation policy
        """
        return self.swImplPolicy

    def setSwImplPolicy(self, value: SwImplPolicyEnum):
        """
        Sets the software implementation policy.

        Args:
            value: The software implementation policy to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swImplPolicy = value
        return self


class ExternalTriggeringPointIdent(IdentCaption):
    """
    Identification of an external triggering point.
    """

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class ExternalTriggeringPoint(ARObject):
    """
    An external triggering point that references a trigger defined in a
    TriggerInterface.
    """

    def __init__(self):
        super().__init__()

        self.ident: ExternalTriggeringPointIdent = None
        self.trigger: Trigger = None

    def getIdent(self) -> ExternalTriggeringPointIdent:
        """
        Gets the identification of this external triggering point.

        Returns:
            ExternalTriggeringPointIdent: The identification
        """
        return self.ident

    def setIdent(self, value: ExternalTriggeringPointIdent):
        """
        Sets the identification of this external triggering point.

        Args:
            value: The identification to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ident = value
        return self

    def getTrigger(self) -> Trigger:
        """
        Gets the trigger.

        Returns:
            Trigger: The trigger
        """
        return self.trigger

    def setTrigger(self, value: Trigger):
        """
        Sets the trigger.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.trigger = value
        return self
