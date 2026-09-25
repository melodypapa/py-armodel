"""
This module contains classes for representing AUTOSAR trigger elements
in software component internal behavior templates.
"""

from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from typing import TYPE_CHECKING, Optional

from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import ExternalTriggeringPointIdent

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import PTriggerInAtomicSwcTypeInstanceRef


class InternalTriggeringPoint(AbstractAccessPoint, VariationPointCapable):
    """
    If a RunnableEntity owns an InternalTriggeringPoint it is entitled to trigger the execution of Runnable Entities of the corresponding software-component.

    [constr_1182] Allowed values for InternalTriggeringPoint.swImplPolicy: The only allowed values for the attribute swImplPolicy of meta-class InternalTriggeringPoint are either STANDARD (in which case the processing of the internal triggering does not use a queue) or QUEUED (in which case the processing of internal triggering positively uses a queue). This rule shall be imposed at the time when the RTE is generated.
    """

    # InternalTriggeringPoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.30, p.561
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSwImplPolicy [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwImplPolicy [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute, when set to value queued, allows for a queued processing of Triggers.
        self.swImplPolicy: Optional[SwImplPolicyEnum] = None

    def getSwImplPolicy(self) -> Optional[SwImplPolicyEnum]:
        """
        This attribute, when set to value queued, allows for a queued processing of Triggers.
        """
        return self.swImplPolicy

    def setSwImplPolicy(self, value: Optional[SwImplPolicyEnum]) -> InternalTriggeringPoint:
        """
        This attribute, when set to value queued, allows for a queued processing of Triggers.
        A None value is a no-op and does not overwrite an existing swImplPolicy.
        """
        if value is not None:
            self.swImplPolicy = value
        return self


class ExternalTriggeringPoint(ARObject, VariationPointCapable):
    """
    If a RunnableEntity owns an ExternalTriggeringPoint it is entitled to
    raise an ExternalTriggerOccurred Event.
    """

    # ExternalTriggeringPoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.39, p.584
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createIdent  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIdent     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getTrigger   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTrigger   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The aggregation in the role ident provides the ability to make the
        # ExternalTriggeringPoint identifiable. From the semantical point of view,
        # the ExternalTriggering Point is considered a first-class Identifiable and
        # therefore the aggregation in the role ident shall always exist (until it
        # may be possible to let ModeAccessPoint directly inherit from Identifiable).
        self.ident: ExternalTriggeringPointIdent = None

        # The trigger taken for the ExternalTriggeringPoint.
        self.trigger: Optional["PTriggerInAtomicSwcTypeInstanceRef"] = None

    def createIdent(self, short_name: str) -> ExternalTriggeringPointIdent:
        """
        Creates the identification of this external triggering point.

        Returns:
            ExternalTriggeringPointIdent: The identification
        """
        if self.ident is None:
            self.ident = ExternalTriggeringPointIdent(self, short_name)
        return self.ident

    def getIdent(self) -> ExternalTriggeringPointIdent:
        """
        Gets the identification of this external triggering point.

        Returns:
            ExternalTriggeringPointIdent: The identification
        """
        return self.ident

    def getTrigger(self) -> Optional["PTriggerInAtomicSwcTypeInstanceRef"]:
        """
        Gets the trigger taken for the ExternalTriggeringPoint. The trigger is
        represented as a PTriggerInAtomicSwcTypeInstanceRef.

        Returns:
            PTriggerInAtomicSwcTypeInstanceRef: The trigger instance reference
        """
        return self.trigger

    def setTrigger(self, value: Optional["PTriggerInAtomicSwcTypeInstanceRef"]) -> ExternalTriggeringPoint:
        """
        Sets the trigger taken for the ExternalTriggeringPoint. The trigger is
        represented as a PTriggerInAtomicSwcTypeInstanceRef. A None value is a
        no-op and does not overwrite an existing trigger.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.trigger = value
        return self
