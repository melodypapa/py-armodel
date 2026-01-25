"""
Parser for AUTOSAR BSW module elements.

Handles:
- BswModuleDescription
- BswInternalBehavior
- BswModuleEntity
- BswCalledEntity
- BswSchedulableEntity
- BswInterruptEntity
- BswImplementation
- BswModuleEntry
- BswModuleClientServerEntry
- BswModuleDependency
- BSW Events
- BSW Call Points (BswDirectCallPoint, BswSynchronousServerCallPoint,
  BswAsynchronousServerCallPoint, BswAsynchronousServerCallResultPoint)
- Trigger declarations
- Engineering objects
"""
from typing import List
import xml.etree.ElementTree as ET

from ..base_arxml_parser import BaseARXMLParser
from ...models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

# Import BSW behavior-related model classes
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswApiOptions,
    BswAsynchronousServerCallPoint,
    BswBackgroundEvent,
    BswDataReceivedEvent,
    BswDataReceptionPolicy,
    BswExternalTriggerOccurredEvent,
    BswInternalBehavior,
    BswInternalTriggerOccurredEvent,
    BswInternalTriggeringPoint,
    BswInterruptEntity,
    BswModeSenderPolicy,
    BswModuleCallPoint,
    BswOperationInvokedEvent,
    BswQueuedDataReceptionPolicy,
    BswScheduleEvent,
    BswSynchronousServerCallPoint,
    BswTimingEvent,
    BswVariableAccess,
)
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswCalledEntity,
    BswModeSwitchEvent,
    BswModuleEntity,
    BswSchedulableEntity,
)
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import (
    BswImplementation,
)
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswModuleClientServerEntry,
    BswModuleEntry,
)
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import (
    BswModuleDescription,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ExecutableEntity,
    InternalBehavior,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Code,
    Implementation,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (
    IncludedModeDeclarationGroupSet,
)
from ...models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    VariableDataPrototype,
)
from ...models.M2.MSR.DataDictionary.ServiceProcessTask import SwServiceArg
from ...models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (
    AutosarEngineeringObject,
    EngineeringObject,
)


class BswModuleParser(BaseARXMLParser):
    """
    Parser for AUTOSAR BSW module elements.

    Handles basic software module descriptions, behaviors,
    implementations, and their interfaces.
    """

    def __init__(self, options=None, main_parser=None):
        """Initialize BswModuleParser."""
        super().__init__(options)
        self._main_parser = main_parser

    # ========================================================================
    # Helper Methods
    # ========================================================================

    def getBswModeSenderPolicy(self, element: ET.Element) -> BswModeSenderPolicy:
        """Get BSW mode sender policy."""
        policy = BswModeSenderPolicy()
        policy.setProvidedModeGroupRef(
            self.getChildElementOptionalRefType(element, "PROVIDED-MODE-GROUP-REF")
        )
        policy.setQueueLength(
            self.getChildElementOptionalNumericalValue(element, "QUEUE-LENGTH")
        )
        return policy

    # ========================================================================
    # BSW Events
    # ========================================================================

    def readBswEvent(self, element: ET.Element, event: BswScheduleEvent):
        """Read BSW event."""
        event.startsOnEventRef = self.getChildElementOptionalRefType(
            element, "STARTS-ON-EVENT-REF"
        )

    def readBswScheduleEvent(self, element, event: BswScheduleEvent):
        """Read BSW schedule event."""
        self.readBswEvent(element, event)

    def readBswModeSwitchEvent(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readBswModeSwitchEvent(
                *args, **kwargs
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readBswTimingEvent(self, element: ET.Element, event: BswTimingEvent):
        """Read BSW timing event."""
        self.logger.debug("Read BswTimingEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setPeriod(self.getChildElementOptionalTimeValue(element, "PERIOD"))
        if event.getPeriod() is None:
            self.logger.warning(
                "Period of BswTimingEvent <%s> is invalid." % event.getShortName()
            )
        else:
            self.logger.debug(
                " Period: <%f, %s>"
                % (event.getPeriod().getValue(), event.getPeriod().getText())
            )

    def readBswDataReceivedEvent(
        self, element: ET.Element, event: BswDataReceivedEvent
    ):
        """Read BSW data received event."""
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setDataRef(self.getChildElementOptionalRefType(element, "DATA-REF"))

    def readBswInternalTriggerOccurredEvent(
        self, element: ET.Element, event: BswInternalTriggerOccurredEvent
    ):
        """Read BSW internal trigger occurred event."""
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setEventSourceRef(
            self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF")
        )

    def readBswBackgroundEvent(
        self, element: ET.Element, event: BswBackgroundEvent
    ):
        """Read BSW background event."""
        self.readBswScheduleEvent(element, event)

    def readBswExternalTriggerOccurredEvent(
        self, element: ET.Element, event: BswExternalTriggerOccurredEvent
    ):
        """Read BSW external trigger occurred event."""
        self.readBswScheduleEvent(element, event)
        event.setTriggerRef(self.getChildElementOptionalRefType(element, "TRIGGER-REF"))

    def readBswOperationInvokedEvent(
        self, element: ET.Element, event: BswOperationInvokedEvent
    ):
        """Read BSW operation invoked event."""
        self.readBswEvent(element, event)
        event.setEntryRef(self.getChildElementOptionalRefType(element, "ENTRY-REF"))

    # ========================================================================
    # BSW Module Entity
    # ========================================================================

    def readBswVariableAccess(
        self, element: ET.Element, access: BswVariableAccess
    ):
        """Read BSW variable access."""
        self.readReferrable(element, access)
        access.setAccessedVariableRef(
            self.getChildElementOptionalRefType(element, "ACCESSED-VARIABLE-REF")
        )

    def readBswModuleEntityDataSendPoints(
        self, element: ET.Element, entity: BswModuleEntity
    ):
        """Read BSW module entity data send points."""
        for child_element in self.findall(element, "DATA-SEND-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-VARIABLE-ACCESS":
                point = entity.createDataSendPoint(self.getShortName(child_element))
                self.readBswVariableAccess(child_element, point)
            else:
                self.notImplemented("Unsupported Data Send Point <%s>" % tag_name)

    def readBswModuleEntityDataReceiverPoints(
        self, element: ET.Element, entity: BswModuleEntity
    ):
        """Read BSW module entity data receiver points."""
        for child_element in self.findall(element, "DATA-RECEIVE-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-VARIABLE-ACCESS":
                point = entity.createDataReceivePoint(self.getShortName(child_element))
                self.readBswVariableAccess(child_element, point)
            else:
                self.notImplemented("Unsupported Data Receive Point <%s>" % tag_name)

    def readBswModuleEntityIssuedTriggerRefs(
        self, element: ET.Element, entity: BswModuleEntity
    ):
        """Read BSW module entity issued trigger refs."""
        for ref in self.getChildElementRefTypeList(
            element, "ISSUED-TRIGGERS/TRIGGER-REF-CONDITIONAL/TRIGGER-REF"
        ):
            entity.addIssuedTriggerRef(ref)

    def readBswModuleEntityActivationPointRefs(
        self, element: ET.Element, entity: BswModuleEntity
    ):
        """Read BSW module entity activation point refs."""
        for ref in self.getChildElementRefTypeList(
            element,
            "ACTIVATION-POINTS/BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL/BSW-INTERNAL-TRIGGERING-POINT-REF",
        ):
            entity.addActivationPointRef(ref)

    def readBswModuleCallPoint(
        self, element: ET.Element, point: BswModuleCallPoint
    ):
        """Read BSW module call point."""
        self.readReferrable(element, point)

    def readBswAsynchronousServerCallPoint(
        self, element: ET.Element, point: BswAsynchronousServerCallPoint
    ):
        """Read BSW asynchronous server call point."""
        self.readBswModuleCallPoint(element, point)
        point.setCalledEntryRef(
            self.getChildElementOptionalRefType(element, "CALLED-ENTRY-REF")
        )

    def readBswSynchronousServerCallPoint(
        self, element: ET.Element, point: BswSynchronousServerCallPoint
    ):
        """Read BSW synchronous server call point."""
        self.readBswModuleCallPoint(element, point)
        point.setCalledEntryRef(
            self.getChildElementOptionalRefType(element, "CALLED-ENTRY-REF")
        )

    def readBswModuleEntityCallPoints(
        self, element: ET.Element, entity: BswModuleEntity
    ):
        """Read BSW module entity call points."""
        for child_element in self.findall(element, "CALL-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-ASYNCHRONOUS-SERVER-CALL-POINT":
                point = entity.createBswAsynchronousServerCallPoint(
                    self.getShortName(child_element)
                )
                self.readBswAsynchronousServerCallPoint(child_element, point)
            elif tag_name == "BSW-SYNCHRONOUS-SERVER-CALL-POINT":
                point = entity.createBswSynchronousServerCallPoint(
                    self.getShortName(child_element)
                )
                self.readBswSynchronousServerCallPoint(child_element, point)
            else:
                self.notImplemented("Unsupported Call Point <%s>" % tag_name)

    def readBswModuleEntityManagedModeGroups(self, element, entity):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readBswModuleEntityManagedModeGroups(
                element, entity
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readBswModuleEntity(self, element: ET.Element, entity: BswModuleEntity):
        """Read BSW module entity."""
        self.readExecutableEntity(element, entity)
        self.readBswModuleEntityActivationPointRefs(element, entity)
        self.readBswModuleEntityCallPoints(element, entity)
        self.readBswModuleEntityDataReceiverPoints(element, entity)
        self.readBswModuleEntityDataSendPoints(element, entity)
        entity.setImplementedEntryRef(
            self.getChildElementRefType(entity.getShortName(), element, "IMPLEMENTED-ENTRY-REF")
        )
        self.readBswModuleEntityManagedModeGroups(element, entity)
        self.readBswModuleEntityIssuedTriggerRefs(element, entity)

    def readBswCalledEntity(self, element: ET.Element, entity: BswCalledEntity):
        """Read BSW called entity."""
        self.readBswModuleEntity(element, entity)

    def readBswSchedulableEntity(
        self, element: ET.Element, entity: BswSchedulableEntity
    ):
        """Read BSW schedulable entity."""
        self.readBswModuleEntity(element, entity)

    def readBswInterruptEntity(
        self, element: ET.Element, entity: BswInterruptEntity
    ):
        """Read BSW interrupt entity."""
        self.readBswModuleEntity(element, entity)
        entity.setInterruptCategory(
            self.getChildElementOptionalLiteral(element, "INTERRUPT-CATEGORY")
        ).setInterruptSource(
            self.getChildElementOptionalLiteral(element, "INTERRUPT-SOURCE")
        )

    # ========================================================================
    # BSW Internal Behavior
    # ========================================================================

    def readBswInternalBehaviorEntities(
        self, element: ET.Element, behavior: BswInternalBehavior
    ):
        """Read BSW internal behavior entities."""
        for child_element in self.findall(element, "ENTITYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-CALLED-ENTITY":
                entity = behavior.createBswCalledEntity(self.getShortName(child_element))
                self.readBswCalledEntity(child_element, entity)
            elif tag_name == "BSW-SCHEDULABLE-ENTITY":
                entity = behavior.createBswSchedulableEntity(
                    self.getShortName(child_element)
                )
                self.readBswSchedulableEntity(child_element, entity)
            elif tag_name == "BSW-INTERRUPT-ENTITY":
                entity = behavior.createBswInterruptEntity(
                    self.getShortName(child_element)
                )
                self.readBswInterruptEntity(child_element, entity)
            else:
                self.notImplemented("Unsupported BswModuleEntity <%s>" % tag_name)

    def readBswInternalBehaviorEvents(
        self, element: ET.Element, behavior: BswInternalBehavior
    ):
        """Read BSW internal behavior events."""
        for child_element in self.findall(element, "EVENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODE-SWITCH-EVENT":
                event = behavior.createBswModeSwitchEvent(self.getShortName(child_element))
                # Delegate to PortInterfaceParser
                if self._main_parser:
                    self._main_parser._port_interface_parser.readBswModeSwitchEvent(
                        child_element, event
                    )
                else:
                    self.raiseError("PortInterfaceParser not available")
            elif tag_name == "BSW-TIMING-EVENT":
                event = behavior.createBswTimingEvent(self.getShortName(child_element))
                self.readBswTimingEvent(child_element, event)
            elif tag_name == "BSW-DATA-RECEIVED-EVENT":
                event = behavior.createBswDataReceivedEvent(
                    self.getShortName(child_element)
                )
                self.readBswDataReceivedEvent(child_element, event)
            elif tag_name == "BSW-INTERNAL-TRIGGER-OCCURRED-EVENT":
                event = behavior.createBswInternalTriggerOccurredEvent(
                    self.getShortName(child_element)
                )
                self.readBswInternalTriggerOccurredEvent(child_element, event)
            elif tag_name == "BSW-BACKGROUND-EVENT":
                event = behavior.createBswBackgroundEvent(
                    self.getShortName(child_element)
                )
                self.readBswBackgroundEvent(child_element, event)
            elif tag_name == "BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT":
                event = behavior.createBswExternalTriggerOccurredEvent(
                    self.getShortName(child_element)
                )
                self.readBswExternalTriggerOccurredEvent(child_element, event)
            elif tag_name == "BSW-OPERATION-INVOKED-EVENT":
                event = behavior.createBswOperationInvokedEvent(
                    self.getShortName(child_element)
                )
                self.readBswOperationInvokedEvent(child_element, event)
            else:
                self.notImplemented("Unsupported BswModuleEntity <%s>" % tag_name)

    def readBswApiOptions(self, element: ET.Element, options: BswApiOptions):
        """Read BSW API options."""
        self.readARObjectAttributes(element, options)
        options.setEnableTakeAddress(
            self.getChildElementOptionalBooleanValue(element, "ENABLE-TAKE-ADDRESS")
        )

    def readBswDataReceptionPolicy(
        self, element: ET.Element, policy: BswDataReceptionPolicy
    ):
        """Read BSW data reception policy."""
        self.readBswApiOptions(element, policy)
        policy.setReceivedDataRef(
            self.getChildElementOptionalRefType(element, "RECEIVED-DATA-REF")
        )

    def readBswQueuedDataReceptionPolicy(
        self, element: ET.Element, policy: BswQueuedDataReceptionPolicy
    ):
        """Read BSW queued data reception policy."""
        self.readBswDataReceptionPolicy(element, policy)
        policy.setQueueLength(
            self.getChildElementOptionalPositiveInteger(element, "QUEUE-LENGTH")
        )

    def readBswInternalBehaviorReceptionPolicies(
        self, element: ET.Element, behavior: BswInternalBehavior
    ):
        """Read BSW internal behavior reception policies."""
        for child_element in self.findall(element, "RECEPTION-POLICYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-QUEUED-DATA-RECEPTION-POLICY":
                policy = BswQueuedDataReceptionPolicy()
                self.readBswQueuedDataReceptionPolicy(child_element, policy)
                behavior.addReceptionPolicy(policy)
            else:
                self.notImplemented("Unsupported Reception Policies <%s>" % tag_name)

    def readBswInternalTriggeringPoint(
        self, element: ET.Element, point: BswInternalTriggeringPoint
    ):
        """Read BSW internal triggering point."""
        self.readIdentifiable(element, point)

    def readBswInternalBehaviorInternalTriggeringPoints(
        self, element: ET.Element, behavior: BswInternalBehavior
    ):
        """Read BSW internal behavior internal triggering points."""
        for child_element in self.findall(element, "INTERNAL-TRIGGERING-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-INTERNAL-TRIGGERING-POINT":
                point = behavior.createBswInternalTriggeringPoint(
                    self.getShortName(child_element)
                )
                self.readBswInternalTriggeringPoint(child_element, point)
            else:
                self.notImplemented(
                    "Unsupported Internal Triggering Points <%s>" % tag_name
                )

    def readBswInternalBehaviorModeSenderPolicy(
        self, element: ET.Element, parent: BswInternalBehavior
    ):
        """Read BSW internal behavior mode sender policy."""
        for child_element in self.findall(element, "MODE-SENDER-POLICYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODE-SENDER-POLICY":
                parent.addModeSenderPolicy(self.getBswModeSenderPolicy(child_element))
            else:
                self.raiseError("Unsupported ModeSenderPolicy type <%s>." % tag_name)

    def readBswInternalBehavior(
        self, element: ET.Element, behavior: BswInternalBehavior
    ):
        """Read BSW internal behavior."""
        self.logger.debug("Read BswInternalBehavior <%s>" % behavior.full_name)

        # read the internal behavior
        self.readInternalBehavior(element, behavior)
        self.readBswInternalBehaviorInternalTriggeringPoints(element, behavior)
        self.readBswInternalBehaviorEntities(element, behavior)
        self.readBswInternalBehaviorEvents(element, behavior)
        self.readBswInternalBehaviorModeSenderPolicy(element, behavior)
        for group_set in self.getIncludedModeDeclarationGroupSets(element):
            behavior.addIncludedModeDeclarationGroupSet(group_set)
        self.readBswInternalBehaviorReceptionPolicies(element, behavior)

    # ========================================================================
    # BSW Module Description
    # ========================================================================

    def readBswModuleDescriptionImplementedEntryRefs(
        self, element: ET.Element, parent: BswModuleDescription
    ):
        """Read BSW module description implemented entry refs."""
        for child_element in self.findall(
            element, "PROVIDED-ENTRYS/BSW-MODULE-ENTRY-REF-CONDITIONAL"
        ):
            ref = self.getChildElementOptionalRefType(child_element, "BSW-MODULE-ENTRY-REF")
            if ref is not None:
                parent.addImplementedEntryRef(ref)

    def readBswModuleDescriptionProvidedModeGroups(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readBswModuleDescriptionProvidedModeGroups(
                *args, **kwargs
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readBswModuleDescriptionRequiredModeGroups(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readBswModuleDescriptionRequiredModeGroups(
                *args, **kwargs
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readBswModuleDescriptionBswInternalBehaviors(
        self, element: ET.Element, desc: BswModuleDescription
    ):
        """Read BSW module description BSW internal behaviors."""
        for child_element in self.findall(element, "INTERNAL-BEHAVIORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-INTERNAL-BEHAVIOR":
                behavior = desc.createBswInternalBehavior(
                    self.getShortName(child_element)
                )
                self.readBswInternalBehavior(child_element, behavior)
            else:
                self.notImplemented("Unsupported Internal Behavior <%s>" % tag_name)

    def readTrigger(self, element: ET.Element, trigger: Trigger):
        """Read trigger."""
        self.readIdentifiable(element, trigger)

    def readBswModuleDescriptionReleasedTriggers(
        self, element: ET.Element, desc: BswModuleDescription
    ):
        """Read BSW module description released triggers."""
        for child_element in self.findall(element, "RELEASED-TRIGGERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TRIGGER":
                trigger = desc.createReleasedTrigger(self.getShortName(child_element))
                self.readTrigger(child_element, trigger)
            else:
                self.notImplemented("Unsupported Released Trigger <%s>" % tag_name)

    def readBswModuleDescriptionRequiredTriggers(
        self, element: ET.Element, desc: BswModuleDescription
    ):
        """Read BSW module description required triggers."""
        for child_element in self.findall(element, "REQUIRED-TRIGGERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TRIGGER":
                trigger = desc.createRequiredTrigger(self.getShortName(child_element))
                self.readTrigger(child_element, trigger)
            else:
                self.notImplemented("Unsupported Required Trigger <%s>" % tag_name)

    def readVariableDataPrototype(self, *args, **kwargs):
        """Delegate to DataTypeParser."""
        if self._main_parser:
            return self._main_parser._datatype_parser.readVariableDataPrototype(
                *args, **kwargs
            )
        else:
            self.raiseError("DataTypeParser not available")

    def readBswModuleDescriptionProvidedDatas(
        self, element: ET.Element, desc: BswModuleDescription
    ):
        """Read BSW module description provided datas."""
        for child_element in self.findall(element, "PROVIDED-DATAS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-DATA-PROTOTYPE":
                data = desc.createProvidedData(self.getShortName(child_element))
                self.readVariableDataPrototype(child_element, data)
            else:
                self.notImplemented("Unsupported Provided Data <%s>" % tag_name)

    def readBswModuleDescriptionRequiredDatas(
        self, element: ET.Element, desc: BswModuleDescription
    ):
        """Read BSW module description required datas."""
        for child_element in self.findall(element, "REQUIRED-DATAS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-DATA-PROTOTYPE":
                data = desc.createRequiredData(self.getShortName(child_element))
                self.readVariableDataPrototype(child_element, data)
            else:
                self.notImplemented("Unsupported Required Data <%s>" % tag_name)

    def readBswModuleClientServerEntry(
        self, element: ET.Element, entry: BswModuleClientServerEntry
    ):
        """Read BSW module client server entry."""
        self.readReferrable(element, entry)
        entry.setEncapsulatedEntryRef(
            self.getChildElementOptionalRefType(element, "ENCAPSULATED-ENTRY-REF")
        ).setIsReentrant(
            self.getChildElementOptionalBooleanValue(element, "IS-REENTRANT")
        ).setIsSynchronous(
            self.getChildElementOptionalBooleanValue(element, "IS-SYNCHRONOUS")
        )

    def readBswModuleDescriptionProvidedClientServerEntries(
        self, element: ET.Element, desc: BswModuleDescription
    ):
        """Read BSW module description provided client server entries."""
        for child_element in self.findall(element, "PROVIDED-CLIENT-SERVER-ENTRYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODULE-CLIENT-SERVER-ENTRY":
                entry = desc.createProvidedClientServerEntry(
                    self.getShortName(child_element)
                )
                self.readBswModuleClientServerEntry(child_element, entry)
            else:
                self.notImplemented(
                    "Unsupported Provided Client Server Entry <%s>" % tag_name
                )

    def readBswModuleDescriptionRequiredClientServerEntries(
        self, element: ET.Element, desc: BswModuleDescription
    ):
        """Read BSW module description required client server entries."""
        for child_element in self.findall(element, "REQUIRED-CLIENT-SERVER-ENTRYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODULE-CLIENT-SERVER-ENTRY":
                entry = desc.createRequiredClientServerEntry(
                    self.getShortName(child_element)
                )
                self.readBswModuleClientServerEntry(child_element, entry)
            else:
                self.notImplemented(
                    "Unsupported Required Client Server Entry <%s>" % tag_name
                )

    def readBswModuleDescription(
        self, element: ET.Element, desc: BswModuleDescription
    ):
        """Read BSW module description."""
        self.logger.debug("Read BswModuleDescription <%s>" % desc.getShortName())

        self.readIdentifiable(element, desc)
        desc.setModuleId(self.getChildElementOptionalNumericalValue(element, "MODULE-ID"))
        self.readBswModuleDescriptionImplementedEntryRefs(element, desc)
        self.readBswModuleDescriptionProvidedModeGroups(element, desc)
        self.readBswModuleDescriptionRequiredModeGroups(element, desc)
        self.readBswModuleDescriptionProvidedClientServerEntries(element, desc)
        self.readBswModuleDescriptionRequiredClientServerEntries(element, desc)
        self.readBswModuleDescriptionProvidedDatas(element, desc)
        self.readBswModuleDescriptionRequiredDatas(element, desc)
        self.readBswModuleDescriptionBswInternalBehaviors(element, desc)
        self.readBswModuleDescriptionRequiredTriggers(element, desc)

    # ========================================================================
    # BSW Module Entry
    # ========================================================================

    def getSwDataDefProps(self, *args, **kwargs):
        """Delegate to DataTypeParser."""
        if self._main_parser:
            return self._main_parser._datatype_parser.getSwDataDefProps(
                *args, **kwargs
            )
        else:
            self.raiseError("DataTypeParser not available")

    def readSwServiceArg(self, element: ET.Element, arg: SwServiceArg):
        """Read SW service argument."""
        self.readIdentifiable(element, arg)
        arg.setDirection(self.getChildElementOptionalLiteral(element, "DIRECTION")).setSwDataDefProps(
            self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        )

    def readBswModuleEntryArguments(
        self, element: ET.Element, entry: BswModuleEntry
    ):
        """Read BSW module entry arguments."""
        for child_element in self.findall(element, "ARGUMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SW-SERVICE-ARG":
                arg = entry.createArgument(self.getShortName(child_element))
                self.readSwServiceArg(child_element, arg)
            else:
                self.notImplemented("Unsupported Argument <%s>" % tag_name)

    def readBswModuleEntryReturnType(
        self, element: ET.Element, entry: BswModuleEntry
    ):
        """Read BSW module entry return type."""
        child_element = self.find(element, "RETURN-TYPE")
        if child_element is not None:
            self.logger.debug(
                "Read ReturnType of BswModuleEntry <%s>" % entry.getShortName()
            )
            return_type = entry.createReturnType(self.getShortName(child_element))
            self.readSwServiceArg(child_element, return_type)

    def readBswModuleEntry(self, element: ET.Element, entry: BswModuleEntry):
        """Read BSW module entry."""
        self.logger.debug("Read BswModuleEntry <%s>" % entry.getShortName())
        self.readIdentifiable(element, entry)
        self.readBswModuleEntryArguments(element, entry)
        entry.setIsReentrant(
            self.getChildElementOptionalBooleanValue(element, "IS-REENTRANT")
        )
        entry.setIsSynchronous(
            self.getChildElementOptionalBooleanValue(element, "IS-SYNCHRONOUS")
        )
        entry.setServiceId(self.getChildElementOptionalNumericalValue(element, "SERVICE-ID"))
        entry.setCallType(self.getChildElementOptionalLiteral(element, "CALL-TYPE"))
        entry.setExecutionContext(
            self.getChildElementOptionalLiteral(element, "EXECUTION-CONTEXT")
        )
        entry.setSwServiceImplPolicy(
            self.getChildElementOptionalLiteral(element, "SW-SERVICE-IMPL-POLICY")
        )
        entry.setBswEntryKind(
            self.getChildElementOptionalLiteral(element, "BSW-ENTRY-KIND")
        )
        self.readBswModuleEntryReturnType(element, entry)

    # ========================================================================
    # BSW Implementation
    # ========================================================================

    def readEngineeringObject(
        self, element: ET.Element, engineering_obj: EngineeringObject
    ):
        """Read engineering object."""
        self.readARObjectAttributes(element, engineering_obj)
        engineering_obj.setShortLabel(
            self.getChildElementOptionalLiteral(element, "SHORT-LABEL")
        ).setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))

    def getAutosarEngineeringObject(
        self, element: ET.Element
    ) -> AutosarEngineeringObject:
        """Get AUTOSAR engineering object."""
        obj = AutosarEngineeringObject()
        self.readEngineeringObject(element, obj)
        return obj

    def readArtifactDescriptor(self, element: ET.Element, code_desc: Code):
        """Read artifact descriptor."""
        for child_element in self.findall(element, "ARTIFACT-DESCRIPTORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "AUTOSAR-ENGINEERING-OBJECT":
                code_desc.addArtifactDescriptor(self.getAutosarEngineeringObject(child_element))
            else:
                self.notImplemented("Unsupported Artifact Descriptor <%s>" % tag_name)

    def readCodeDescriptor(self, element: ET.Element, impl: Implementation):
        """Read code descriptor."""
        for child_element in self.findall(element, "CODE-DESCRIPTORS/CODE"):
            short_name = self.getShortName(child_element)
            code_desc = impl.createCodeDescriptor(short_name)
            self.readIdentifiable(child_element, code_desc)
            self.readArtifactDescriptor(child_element, code_desc)

    def readImplementation(self, element: ET.Element, impl: Implementation):
        """Read implementation."""
        self.readIdentifiable(element, impl)
        self.readCodeDescriptor(element, impl)
        impl.setProgrammingLanguage(
            self.getChildElementOptionalLiteral(element, "PROGRAMMING-LANGUAGE")
        )
        # Delegate to BehaviorParser for ResourceConsumption
        if self._main_parser:
            self._main_parser._behavior_parser.readResourceConsumption(element, impl)
        else:
            self.notImplemented("BehaviorParser not available for ResourceConsumption")
        impl.setSwVersion(
            self.getChildElementOptionalLiteral(element, "SW-VERSION")
        ).setSwcBswMappingRef(
            self.getChildElementOptionalRefType(element, "SWC-BSW-MAPPING-REF")
        ).setUsedCodeGenerator(
            self.getChildElementOptionalLiteral(element, "USED-CODE-GENERATOR")
        ).setVendorId(self.getChildElementOptionalNumericalValue(element, "VENDOR-ID"))

    def readBswImplementationVendorSpecificModuleDefRefs(
        self, element: ET.Element, impl: BswImplementation
    ):
        """Read BSW implementation vendor specific module def refs."""
        child_element = self.find(element, "VENDOR-SPECIFIC-MODULE-DEF-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(
                child_element, "VENDOR-SPECIFIC-MODULE-DEF-REF"
            ):
                impl.addVendorSpecificModuleDefRef(ref)

    def readBswImplementation(self, element: ET.Element, impl: BswImplementation):
        """Read BSW implementation."""
        self.logger.debug("Read BswImplementation <%s>" % impl.getShortName())
        self.readImplementation(element, impl)
        impl.setArReleaseVersion(
            self.getChildElementOptionalLiteral(element, "AR-RELEASE-VERSION")
        ).setBehaviorRef(self.getChildElementOptionalRefType(element, "BEHAVIOR-REF")).setVendorApiInfix(
            self.getChildElementOptionalLiteral(element, "VENDOR-API-INFIX")
        )
        self.readBswImplementationVendorSpecificModuleDefRefs(element, impl)
        AUTOSAR.getInstance().addImplementationBehaviorMap(
            impl.getFullName(), impl.getBehaviorRef().getValue()
        )

    # ========================================================================
    # Internal Behavior Helpers (delegated to BehaviorParser)
    # ========================================================================

    def readInternalBehavior(self, element: ET.Element, behavior: InternalBehavior):
        """Read internal behavior - delegate to BehaviorParser."""
        if self._main_parser:
            return self._main_parser._behavior_parser.readInternalBehavior(
                element, behavior
            )
        else:
            self.raiseError("BehaviorParser not available")

    # ========================================================================
    # Additional Helper Methods
    # ========================================================================

    def getIncludedModeDeclarationGroupSets(
        self, element: ET.Element
    ) -> List[IncludedModeDeclarationGroupSet]:
        """Get included mode declaration group sets."""
        group_sets = []
        for child_element in self.findall(
            element, "INCLUDED-MODE-DECLARATION-GROUP-SETS/INCLUDED-MODE-DECLARATION-GROUP-SET"
        ):
            group_set = IncludedModeDeclarationGroupSet()
            for ref_type in self.getChildElementRefTypeList(
                child_element, "MODE-DECLARATION-GROUP-REFS/MODE-DECLARATION-GROUP-REF"
            ):
                group_set.addModeDeclarationGroupRef(ref_type)
            group_sets.append(group_set)
        return group_sets
