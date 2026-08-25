"""
This module defines classes for execution order constraint entities in AUTOSAR timing specifications.

Classes:
    EOCExecutableEntityRefAbstract: Abstract base class for execution order constraint executable entity references
    EOCExecutableEntityRefGroup: Group (composite) of execution order constraint executable entity references
    EOCExecutableEntityRef: Reference to an executable entity in an execution order constraint
    EOCEventRef: Reference to an RTE or BSW event in an execution order constraint
    ExecutionOrderConstraint: Constraint defining the execution order of entities
"""

from typing import List, Optional
from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    Integer,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingCondition import ComponentInCompositionInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import TimingConstraint


class ExecutionOrderConstraintTypeEnum(AREnum):
    """
    Specifies the type of the executionOrderConstraintType for a ExecutionOrderConstraint .
    """

    # ExecutionOrderConstraintTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.69, p.119
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on ExecutionOrderConstraint.executionOrderConstraintType
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # Specifies that the Execution Order Constraint specifies a hierarchical execution order constraint.
    # Tags: atp.EnumerationLiteralIndex=0
    HIERARCHICAL_EOC = "hierarchicalEOC"

    # Specifies that the Execution Order Constraint specifies an ordinary execution order constraint.
    # Tags: atp.EnumerationLiteralIndex=1
    ORDINARY_EOC = "ordinaryEOC"

    # Specifies that the Execution Order Constraint specifies a repetitive execution order constraint.
    # Tags: atp.EnumerationLiteralIndex=2
    REPETITIVE_EOC = "repetitiveEOC"

    def __init__(self):
        """
        Initializes the ExecutionOrderConstraintTypeEnum with valid values.
        """
        super().__init__(
            (
                ExecutionOrderConstraintTypeEnum.HIERARCHICAL_EOC,
                ExecutionOrderConstraintTypeEnum.ORDINARY_EOC,
                ExecutionOrderConstraintTypeEnum.REPETITIVE_EOC,
            )
        )


class LetDataExchangeParadigmEnum(AREnum):
    """
    Specifies the data exchange paradigm between ExecutableEntity s within a LET interval.
    """

    # LetDataExchangeParadigmEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 4.4, p.143
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on EOCExecutableEntityRefGroup.letDataExchangeParadigm
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # All ExecutableEntity s mapped to this LET interval exchange data ONLY at the release and terminate event of the LET interval.
    # This allows for a straightforward translation of the required label buffering but results in longer end-to-end latencies (multiple of the period).
    # The execution order of \ARMetaClass{Executable Entity}s within the LET interval does not affect the data flow.
    # Tags: atp.EnumerationLiteralIndex=0 atp.Status=draft
    INTER_LET_ONLY = "interLetOnly"

    # The ExecutableEntity s that belong to the same EOCExecutableEntityRefGroup and are mapped to this LET interval are executed in the order defined by the EOCExecutableEntityRefGroup and exchange data directly within this LET interval according to implicit semantics.
    # Only at the borders of the LET interval or between independent EOCExecutableEntityRefGroup s, is data propagated according to the LET paradigm.
    # Tags: atp.EnumerationLiteralIndex=1 atp.Status=draft
    INTRA_LET_EOC = "intraLetEOC"

    def __init__(self):
        """
        Initializes the LetDataExchangeParadigmEnum with valid values.
        """
        super().__init__(
            (
                LetDataExchangeParadigmEnum.INTER_LET_ONLY,
                LetDataExchangeParadigmEnum.INTRA_LET_EOC,
            )
        )


class EOCExecutableEntityRefAbstract(Identifiable, ABC):
    """
    This is the abstractions for Execution Order Constraint Executable Entity References (leaves) and Execution Order Constraint Executable Entity Reference Groups (composites).
    """

    # EOCExecutableEntityRefAbstract method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.70, p.119
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addDirectSuccessorRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDirectSuccessorRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is EOCExecutableEntityRefAbstract:
            raise TypeError("EOCExecutableEntityRefAbstract is an abstract class.")

        super().__init__(parent, short_name)

        # The direct successor of an executable entity or a group of executable entities.
        self.directSuccessorRefs: List[RefType] = []

    def addDirectSuccessorRef(self, ref: Optional[RefType]) -> "EOCExecutableEntityRefAbstract":
        """The direct successor of an executable entity or a group of executable entities. A None value is a no-op."""
        if ref is not None:
            self.directSuccessorRefs.append(ref)
        return self

    def getDirectSuccessorRefs(self) -> List[RefType]:
        """The direct successor of an executable entity or a group of executable entities."""
        return self.directSuccessorRefs


class EOCExecutableEntityRef(EOCExecutableEntityRefAbstract):
    """
    This is used to define a reference to an ExecutableEntity If the ExecutionOrderConstraint is defined on VFB, System or ECU level, a reference to the SwComponentPrototype, via the ComponentInCompositionInstanceRef, the referenced ExecutableEntity belongs to, shall be provided as context information.
    """

    # EOCExecutableEntityRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.72, p.120
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBswModuleInstanceRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBswModuleInstanceRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getComponentIRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setComponentIRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExecutableRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExecutableRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addSuccessorRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSuccessorRefs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the BSW module instance the BSW module entity belongs to.
        self.bswModuleInstanceRef: Optional[RefType] = None

        # This association references the specific instance of the SW-C prototype. InstanceRef implemented by: ComponentInCompositionInstanceRef
        self.componentIRef: Optional[ComponentInCompositionInstanceRef] = None

        # The ExecutableEntity whose execution order is restricted by the contraint.
        self.executableRef: Optional[RefType] = None

        # The logical successor of an executable entity or a group of executable entities.
        self.successorRefs: List[RefType] = []

    def getBswModuleInstanceRef(self) -> Optional[RefType]:
        """Specifies the BSW module instance the BSW module entity belongs to."""
        return self.bswModuleInstanceRef

    def setBswModuleInstanceRef(self, value: Optional[RefType]) -> "EOCExecutableEntityRef":
        """Specifies the BSW module instance the BSW module entity belongs to. A None value is a no-op and does not overwrite an existing bswModuleInstanceRef."""
        if value is not None:
            self.bswModuleInstanceRef = value
        return self

    def getComponentIRef(self) -> Optional[ComponentInCompositionInstanceRef]:
        """This association references the specific instance of the SW-C prototype. InstanceRef implemented by: ComponentInCompositionInstanceRef"""
        return self.componentIRef

    def setComponentIRef(self, value: Optional[ComponentInCompositionInstanceRef]) -> "EOCExecutableEntityRef":
        """This association references the specific instance of the SW-C prototype. InstanceRef implemented by: ComponentInCompositionInstanceRef. A None value is a no-op and does not overwrite an existing componentIRef."""
        if value is not None:
            self.componentIRef = value
        return self

    def getExecutableRef(self) -> Optional[RefType]:
        """The ExecutableEntity whose execution order is restricted by the contraint."""
        return self.executableRef

    def setExecutableRef(self, value: Optional[RefType]) -> "EOCExecutableEntityRef":
        """The ExecutableEntity whose execution order is restricted by the contraint. A None value is a no-op and does not overwrite an existing executableRef."""
        if value is not None:
            self.executableRef = value
        return self

    def addSuccessorRef(self, ref: Optional[RefType]) -> "EOCExecutableEntityRef":
        """The logical successor of an executable entity or a group of executable entities. A None value is a no-op."""
        if ref is not None:
            self.successorRefs.append(ref)
        return self

    def getSuccessorRefs(self) -> List[RefType]:
        """The logical successor of an executable entity or a group of executable entities."""
        return self.successorRefs


class ExecutionOrderConstraint(TimingConstraint):
    """
    This constraint is used to restrict the order of execution for a set of ExecutableEntity s. The ExecutionOrderConstraint can be used in any timing view. The various scopes for ExecutionOrderConstraint are described below. Generally, each ExecutionOrder Constraint has a scope of software components and can reference all ExecutableEntity s available in the corresponding internal behavior (RunnableEntity and BswModuleEntity) either directly or by the events activating respectively starting them (RteEvent and BswEvent). On VFB level an ExecutionOrderConstraint can be specified for RunnableEntities part of the composition hierarchy referenced by the VfbTiming. On SW-C level an ExecutionOrderConstraint can be specified for RunnableEntities part of the Internal Behavior referenced by the SwcTiming. On System level an ExecutionOrderConstraint can be specified for RunnableEntities part of the composition hierarchy of the system referenced by the SystemTiming. On BSW Module level, an ExectionOrderConstraint can be specified for BswModuleEntities part of an BswInternalBehavior referenced by the BswModuleTiming. On ECU level an ExecutionOrderConstraint can be specified for all ExecutableEntity s and Events available via the EcucValueCollection, covering ECU Extract and BSW Module Configuration, referenced by the EcuTiming.
    """

    # ExecutionOrderConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.68, p.118
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseCompositionRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseCompositionRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExecutionOrderConstraintType   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExecutionOrderConstraintType   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIgnoreOrderAllowed             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIgnoreOrderAllowed             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIsEvent                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIsEvent                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEOCEventRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEOCExecutableEntityRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEOCExecutableEntityRefGroup [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOrderedElements                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getPermitMultipleReferencesToEE   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPermitMultipleReferencesToEE   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the composition SW-C type playing the role of a SW-C containing further SW-Cs and represents the scope of the Execution Order Constraint.
        self.baseCompositionRef: Optional[RefType] = None

        # Specifies the specific type of ExecutionOrderConstraint.
        self.executionOrderConstraintType: Optional[ExecutionOrderConstraintTypeEnum] = None

        # Controls whether the order of execution specified by this constraint can be intentionally ignored (TRUE), or shall be respected (FALSE).
        self.ignoreOrderAllowed: Optional[Boolean] = None

        # Indicates whether the ExecutionOrderConstraint is only referring to Executable Entities (FALSE) or only to RTE and/or BSW Events (TRUE).
        self.isEvent: Optional[Boolean] = None

        # This aggregation represents an unordered collection of references to RunnableEntities which shall be considered in the ExecutionOrderConstraint. The role does not imply that the collection of references itself shall be ordered.
        self.orderedElements: List[EOCExecutableEntityRefAbstract] = []

        # Indicates that the ExecutionOrderConstraints permits that an Executable Entity is referenced multiple times (TRUE) or only once (FALSE) in the constraint.
        self.permitMultipleReferencesToEE: Optional[Boolean] = None

    def getBaseCompositionRef(self) -> Optional[RefType]:
        """Specifies the composition SW-C type playing the role of a SW-C containing further SW-Cs and represents the scope of the Execution Order Constraint."""
        return self.baseCompositionRef

    def setBaseCompositionRef(self, value: Optional[RefType]) -> "ExecutionOrderConstraint":
        """Specifies the composition SW-C type playing the role of a SW-C containing further SW-Cs and represents the scope of the Execution Order Constraint. A None value is a no-op and does not overwrite an existing baseComposition."""
        if value is not None:
            self.baseCompositionRef = value
        return self

    def getExecutionOrderConstraintType(self) -> Optional[ExecutionOrderConstraintTypeEnum]:
        """Specifies the specific type of ExecutionOrderConstraint."""
        return self.executionOrderConstraintType

    def setExecutionOrderConstraintType(self, value: Optional[ExecutionOrderConstraintTypeEnum]) -> "ExecutionOrderConstraint":
        """Specifies the specific type of ExecutionOrderConstraint. A None value is a no-op and does not overwrite an existing executionOrderConstraintType."""
        if value is not None:
            self.executionOrderConstraintType = value
        return self

    def getIgnoreOrderAllowed(self) -> Optional[Boolean]:
        """Controls whether the order of execution specified by this constraint can be intentionally ignored (TRUE), or shall be respected (FALSE)."""
        return self.ignoreOrderAllowed

    def setIgnoreOrderAllowed(self, value: Optional[Boolean]) -> "ExecutionOrderConstraint":
        """Controls whether the order of execution specified by this constraint can be intentionally ignored (TRUE), or shall be respected (FALSE). A None value is a no-op and does not overwrite an existing ignoreOrderAllowed."""
        if value is not None:
            self.ignoreOrderAllowed = value
        return self

    def getIsEvent(self) -> Optional[Boolean]:
        """Indicates whether the ExecutionOrderConstraint is only referring to Executable Entities (FALSE) or only to RTE and/or BSW Events (TRUE)."""
        return self.isEvent

    def setIsEvent(self, value: Optional[Boolean]) -> "ExecutionOrderConstraint":
        """Indicates whether the ExecutionOrderConstraint is only referring to Executable Entities (FALSE) or only to RTE and/or BSW Events (TRUE). A None value is a no-op and does not overwrite an existing isEvent."""
        if value is not None:
            self.isEvent = value
        return self

    def createEOCEventRef(self, short_name: str) -> "EOCEventRef":
        """This aggregation represents an unordered collection of references to RunnableEntities which shall be considered in the ExecutionOrderConstraint. The role does not imply that the collection of references itself shall be ordered."""
        if not self.IsElementExists(short_name):
            event_ref = EOCEventRef(self, short_name)
            self.addElement(event_ref)
            self.orderedElements.append(event_ref)
        return self.getElement(short_name, EOCEventRef)

    def createEOCExecutableEntityRef(self, short_name: str) -> EOCExecutableEntityRef:
        """This aggregation represents an unordered collection of references to RunnableEntities which shall be considered in the ExecutionOrderConstraint. The role does not imply that the collection of references itself shall be ordered."""
        if not self.IsElementExists(short_name):
            entity_ref = EOCExecutableEntityRef(self, short_name)
            self.addElement(entity_ref)
            self.orderedElements.append(entity_ref)
        return self.getElement(short_name, EOCExecutableEntityRef)

    def createEOCExecutableEntityRefGroup(self, short_name: str) -> "EOCExecutableEntityRefGroup":
        """This aggregation represents an unordered collection of references to RunnableEntities which shall be considered in the ExecutionOrderConstraint. The role does not imply that the collection of references itself shall be ordered."""
        if not self.IsElementExists(short_name):
            entity_ref_group = EOCExecutableEntityRefGroup(self, short_name)
            self.addElement(entity_ref_group)
            self.orderedElements.append(entity_ref_group)
        return self.getElement(short_name, EOCExecutableEntityRefGroup)

    def getOrderedElements(self) -> List[EOCExecutableEntityRefAbstract]:
        """This aggregation represents an unordered collection of references to RunnableEntities which shall be considered in the ExecutionOrderConstraint. The role does not imply that the collection of references itself shall be ordered."""
        return self.orderedElements

    def getPermitMultipleReferencesToEE(self) -> Optional[Boolean]:
        """Indicates that the ExecutionOrderConstraints permits that an Executable Entity is referenced multiple times (TRUE) or only once (FALSE) in the constraint."""
        return self.permitMultipleReferencesToEE

    def setPermitMultipleReferencesToEE(self, value: Optional[Boolean]) -> "ExecutionOrderConstraint":
        """Indicates that the ExecutionOrderConstraints permits that an Executable Entity is referenced multiple times (TRUE) or only once (FALSE) in the constraint. A None value is a no-op and does not overwrite an existing permitMultipleReferencesToEE."""
        if value is not None:
            self.permitMultipleReferencesToEE = value
        return self


class EOCEventRef(EOCExecutableEntityRefAbstract):
    """
    This is used to define a reference to an RTE or BSW Event.
    """

    # EOCEventRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.73, p.121
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBswModuleInstanceRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBswModuleInstanceRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getComponentIRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setComponentIRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEventRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEventRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addSuccessorRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSuccessorRefs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the BSW module instance the BSW event is related to.
        self.bswModuleInstanceRef: Optional[RefType] = None

        # This association references the specific instance of the SW-C prototype. InstanceRef implemented by: ComponentInCompositionInstanceRef
        self.componentIRef: Optional[ComponentInCompositionInstanceRef] = None

        # The AbstractEvent (event) whose execution order is restricted by the contraint.
        self.eventRef: Optional[RefType] = None

        # The logical successor of an executable entity or a group of executable entities.
        self.successorRefs: List[RefType] = []

    def getBswModuleInstanceRef(self) -> Optional[RefType]:
        """Specifies the BSW module instance the BSW event is related to."""
        return self.bswModuleInstanceRef

    def setBswModuleInstanceRef(self, value: Optional[RefType]) -> "EOCEventRef":
        """Specifies the BSW module instance the BSW event is related to. A None value is a no-op and does not overwrite an existing bswModuleInstanceRef."""
        if value is not None:
            self.bswModuleInstanceRef = value
        return self

    def getComponentIRef(self) -> Optional[ComponentInCompositionInstanceRef]:
        """This association references the specific instance of the SW-C prototype. InstanceRef implemented by: ComponentInCompositionInstanceRef"""
        return self.componentIRef

    def setComponentIRef(self, value: Optional[ComponentInCompositionInstanceRef]) -> "EOCEventRef":
        """This association references the specific instance of the SW-C prototype. InstanceRef implemented by: ComponentInCompositionInstanceRef. A None value is a no-op and does not overwrite an existing componentIRef."""
        if value is not None:
            self.componentIRef = value
        return self

    def getEventRef(self) -> Optional[RefType]:
        """The AbstractEvent (event) whose execution order is restricted by the contraint."""
        return self.eventRef

    def setEventRef(self, value: Optional[RefType]) -> "EOCEventRef":
        """The AbstractEvent (event) whose execution order is restricted by the contraint. A None value is a no-op and does not overwrite an existing eventRef."""
        if value is not None:
            self.eventRef = value
        return self

    def addSuccessorRef(self, ref: Optional[RefType]) -> "EOCEventRef":
        """The logical successor of an executable entity or a group of executable entities. A None value is a no-op."""
        if ref is not None:
            self.successorRefs.append(ref)
        return self

    def getSuccessorRefs(self) -> List[RefType]:
        """The logical successor of an executable entity or a group of executable entities."""
        return self.successorRefs


class EOCExecutableEntityRefGroup(EOCExecutableEntityRefAbstract):
    """
    This is used to specify a group (composite) consisting of Execution Order Constraint Executable Entity References (leaves) and/or further Execution Order Constraint Executable Entity Reference Groups (composite).
    """

    # EOCExecutableEntityRefGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.71, p.120
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLetDataExchangeParadigm     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLetDataExchangeParadigm     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addLetIntervalRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLetIntervalRefs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getMaxCycleRepetitions         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxCycleRepetitions         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxCycles                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxCycles                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxSlots                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxSlots                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxSlotsPerCycle            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxSlotsPerCycle            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addNestedElementRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNestedElementRefs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSuccessorRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSuccessorRefs               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getTriggeringEventRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTriggeringEventRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the data exchange paradigm between ExecutableEntity s within a LET interval.
        self.letDataExchangeParadigm: Optional[LetDataExchangeParadigmEnum] = None

        # This association references the TimingDescriptionEventChain that plays the role of a LET interval the executable entities in the group are assigned to.
        self.letIntervalRefs: List[RefType] = []

        # Repetitive Execution Order Constraint only: The number of repetitions (cycles) of the event in the Repetitive Execution Order Constraint.
        self.maxCycleRepetitions: Optional[PositiveInteger] = None

        # In case of a Repetitive Execution Order Constraint this attribute specifies the number of cycles the Execution Order Constraint is considering.
        self.maxCycles: Optional[Integer] = None

        # In case of a Repetitive Execution Order Constraint this attribute specifies the number of slots every cycle of the Execution Order Constraint is consisting of.
        self.maxSlots: Optional[Integer] = None

        # Repetitive Execution Order Constraint only: The number of ExecutableEntity s (slots) that are executed in a given order within a cycle, for the Repetitive Execution Order Constraint.
        self.maxSlotsPerCycle: Optional[PositiveInteger] = None

        # This association is used to establish hierarchies of EOCEER Groups and References.
        self.nestedElementRefs: List[RefType] = []

        # The logical successor of an executable entity or a group of executable entities.
        self.successorRefs: List[RefType] = []

        # In case of a Repetitive Execution Order Constraint this association references the timing description event triggering every cycle.
        self.triggeringEventRef: Optional[RefType] = None

    def getLetDataExchangeParadigm(self) -> Optional[LetDataExchangeParadigmEnum]:
        """Specifies the data exchange paradigm between ExecutableEntity s within a LET interval."""
        return self.letDataExchangeParadigm

    def setLetDataExchangeParadigm(self, value: Optional[LetDataExchangeParadigmEnum]) -> "EOCExecutableEntityRefGroup":
        """Specifies the data exchange paradigm between ExecutableEntity s within a LET interval. A None value is a no-op and does not overwrite an existing letDataExchangeParadigm."""
        if value is not None:
            self.letDataExchangeParadigm = value
        return self

    def addLetIntervalRef(self, ref: Optional[RefType]) -> "EOCExecutableEntityRefGroup":
        """This association references the TimingDescriptionEventChain that plays the role of a LET interval the executable entities in the group are assigned to. A None value is a no-op."""
        if ref is not None:
            self.letIntervalRefs.append(ref)
        return self

    def getLetIntervalRefs(self) -> List[RefType]:
        """This association references the TimingDescriptionEventChain that plays the role of a LET interval the executable entities in the group are assigned to."""
        return self.letIntervalRefs

    def getMaxCycleRepetitions(self) -> Optional[PositiveInteger]:
        """Repetitive Execution Order Constraint only: The number of repetitions (cycles) of the event in the Repetitive Execution Order Constraint."""
        return self.maxCycleRepetitions

    def setMaxCycleRepetitions(self, value: Optional[PositiveInteger]) -> "EOCExecutableEntityRefGroup":
        """Repetitive Execution Order Constraint only: The number of repetitions (cycles) of the event in the Repetitive Execution Order Constraint. A None value is a no-op and does not overwrite an existing maxCycleRepetitions."""
        if value is not None:
            self.maxCycleRepetitions = value
        return self

    def getMaxCycles(self) -> Optional[Integer]:
        """In case of a Repetitive Execution Order Constraint this attribute specifies the number of cycles the Execution Order Constraint is considering."""
        return self.maxCycles

    def setMaxCycles(self, value: Optional[Integer]) -> "EOCExecutableEntityRefGroup":
        """In case of a Repetitive Execution Order Constraint this attribute specifies the number of cycles the Execution Order Constraint is considering. A None value is a no-op and does not overwrite an existing maxCycles."""
        if value is not None:
            self.maxCycles = value
        return self

    def getMaxSlots(self) -> Optional[Integer]:
        """In case of a Repetitive Execution Order Constraint this attribute specifies the number of slots every cycle of the Execution Order Constraint is consisting of."""
        return self.maxSlots

    def setMaxSlots(self, value: Optional[Integer]) -> "EOCExecutableEntityRefGroup":
        """In case of a Repetitive Execution Order Constraint this attribute specifies the number of slots every cycle of the Execution Order Constraint is consisting of. A None value is a no-op and does not overwrite an existing maxSlots."""
        if value is not None:
            self.maxSlots = value
        return self

    def getMaxSlotsPerCycle(self) -> Optional[PositiveInteger]:
        """Repetitive Execution Order Constraint only: The number of ExecutableEntity s (slots) that are executed in a given order within a cycle, for the Repetitive Execution Order Constraint."""
        return self.maxSlotsPerCycle

    def setMaxSlotsPerCycle(self, value: Optional[PositiveInteger]) -> "EOCExecutableEntityRefGroup":
        """Repetitive Execution Order Constraint only: The number of ExecutableEntity s (slots) that are executed in a given order within a cycle, for the Repetitive Execution Order Constraint. A None value is a no-op and does not overwrite an existing maxSlotsPerCycle."""
        if value is not None:
            self.maxSlotsPerCycle = value
        return self

    def addNestedElementRef(self, ref: Optional[RefType]) -> "EOCExecutableEntityRefGroup":
        """This association is used to establish hierarchies of EOCEER Groups and References. A None value is a no-op."""
        if ref is not None:
            self.nestedElementRefs.append(ref)
        return self

    def getNestedElementRefs(self) -> List[RefType]:
        """This association is used to establish hierarchies of EOCEER Groups and References."""
        return self.nestedElementRefs

    def addSuccessorRef(self, ref: Optional[RefType]) -> "EOCExecutableEntityRefGroup":
        """The logical successor of an executable entity or a group of executable entities. A None value is a no-op."""
        if ref is not None:
            self.successorRefs.append(ref)
        return self

    def getSuccessorRefs(self) -> List[RefType]:
        """The logical successor of an executable entity or a group of executable entities."""
        return self.successorRefs

    def getTriggeringEventRef(self) -> Optional[RefType]:
        """In case of a Repetitive Execution Order Constraint this association references the timing description event triggering every cycle."""
        return self.triggeringEventRef

    def setTriggeringEventRef(self, value: Optional[RefType]) -> "EOCExecutableEntityRefGroup":
        """In case of a Repetitive Execution Order Constraint this association references the timing description event triggering every cycle. A None value is a no-op and does not overwrite an existing triggeringEventRef."""
        if value is not None:
            self.triggeringEventRef = value
        return self
