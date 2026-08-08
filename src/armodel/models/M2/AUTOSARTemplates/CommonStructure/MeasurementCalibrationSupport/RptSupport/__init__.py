"""
This module contains classes for representing AUTOSAR rapid prototyping support
data (RptSupport) in the measurement and calibration support templates.
"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, CIdentifier, Identifier, PositiveInteger, RefType
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import RoleBasedMcDataAssignment
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptExecutableEntityProperties, RptImplPolicy


class RptAccessEnum(AREnum):
    """
    Determines the access rights to a data object with respect to rapid prototyping.
    """

    # RptAccessEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.25, p.205
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # The related data element is accessible by RP tool. atp.EnumerationLiteralIndex=0
    ENABLED = "enabled"

    # The related data element is not accessible by RP tool. atp.EnumerationLiteralIndex=1
    NONE = "none"

    # The data element is known to the RP tool however its usage for RP can be restricted. Use case: limitation based on access rights atp.EnumerationLiteralIndex=2
    PROTECTED = "protected"

    def __init__(self):
        super().__init__(
            (
                RptAccessEnum.ENABLED,
                RptAccessEnum.NONE,
                RptAccessEnum.PROTECTED,
            )
        )


class RptEnablerImplTypeEnum(AREnum):
    """
    Describes the required / implemented usage of enabler flags for data access in the code.
    """

    # RptEnablerImplTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.19, p.202
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # No "RP enabler" is implemented. atp.EnumerationLiteralIndex=0
    NONE = "none"

    # "RP enabler" is implemented as a RAM variable atp.EnumerationLiteralIndex=1
    RPT_ENABLER_RAM = "rptEnablerRam"

    # "RP enabler" is implemented as a calibrateable ROM variable. atp.EnumerationLiteralIndex=2
    RPT_ENABLER_ROM = "rptEnablerRom"

    # The RTE generator implements both the RAM and ROM "RP enabler". atp.EnumerationLiteralIndex=3
    RPT_ENABLER_RAM_AND_ROM = "rptEnablerRamAndRom"

    def __init__(self):
        super().__init__(
            (
                RptEnablerImplTypeEnum.NONE,
                RptEnablerImplTypeEnum.RPT_ENABLER_RAM,
                RptEnablerImplTypeEnum.RPT_ENABLER_ROM,
                RptEnablerImplTypeEnum.RPT_ENABLER_RAM_AND_ROM,
            )
        )


class RptExecutionControlEnum(AREnum):
    """
    Determines rapid prototyping preparation of an ExecutableEntity.
    """

    # RptExecutionControlEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.22, p.203
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # The ExecutableEntity is only executed when the rapid prototyping disable flag is NOT set. atp.EnumerationLiteralIndex=0
    CONDITIONAL = "conditional"

    # The ExecutableEntity is executed without specific rapid prototyping condition. atp.EnumerationLiteralIndex=1
    NONE = "none"

    def __init__(self):
        super().__init__(
            (
                RptExecutionControlEnum.CONDITIONAL,
                RptExecutionControlEnum.NONE,
            )
        )


class RptPreparationEnum(AREnum):
    """
    Mandates RP preparation level for access to VariableDataPrototype within generated RTE implementation.
    """

    # RptPreparationEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.20, p.203
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # No RP preparation for VariableDataPrototype. atp.EnumerationLiteralIndex=0
    NONE = "none"

    # The RTE implementation uses an "RP global buffer" for measurement and post-build hooking purposes. atp.EnumerationLiteralIndex=1
    RPT_LEVEL_1 = "rptLevel1"

    # As rpLevel1 but the RTE implementation also uses both "RP enabler flag" to permit RP overwrite at run-time. atp.EnumerationLiteralIndex=2
    RPT_LEVEL_2 = "rptLevel2"

    # As rpLevel2 but the RTE implementation also uses "RP global measurement buffer" to record the original ECU-generated value in addition to the RP value. atp.EnumerationLiteralIndex=3
    RPT_LEVEL_3 = "rptLevel3"

    def __init__(self):
        super().__init__(
            (
                RptPreparationEnum.NONE,
                RptPreparationEnum.RPT_LEVEL_1,
                RptPreparationEnum.RPT_LEVEL_2,
                RptPreparationEnum.RPT_LEVEL_3,
            )
        )


class RptExecutionContext(Identifiable):
    """
    Defines an environment for the execution of ExecutableEntites which is qualified by • OSTask • communication buffer usage.
    """

    # RptExecutionContext method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.24, p.205
    # Spec verified: R23-11
    # [x] __init__                   [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the RptExecutionContext with a parent and short name.

        Args:
            parent: The parent ARObject that contains this execution context
            short_name: The unique short name of this execution context
        """
        super().__init__(parent, short_name)


class RptSwPrototypingAccess(ARObject):
    """
    Describes the accessibility of data and modes by the rapid prototyping tooling.
    """

    # RptSwPrototypingAccess method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.14, p.199
    # Spec verified: R23-11
    # [x] __init__                   [x] impl  [x] docstring  [x] test
    # [x] getRptHookAccess           [x] impl  [x] docstring  [x] test
    # [x] setRptHookAccess           [x] impl  [x] docstring  [x] test
    # [x] getRptReadAccess           [x] impl  [x] docstring  [x] test
    # [x] setRptReadAccess           [x] impl  [x] docstring  [x] test
    # [x] getRptWriteAccess          [x] impl  [x] docstring  [x] test
    # [x] setRptWriteAccess          [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the RptSwPrototypingAccess.
        """
        super().__init__()

        # The related data element can be modified using a post-build hooking tool. An ENABLED VariableDataPrototype is implicitly READABLE/WRITABLE.
        self.rptHookAccess: Optional[RptAccessEnum] = None

        # The related data element can be used as input for bypass functionality by RP tool. If rptImplPolicy is not specified then RTE generation shall ensure at least suitable MC read points are created.
        self.rptReadAccess: Optional[RptAccessEnum] = None

        # The related data element can be used as output for bypass functionality by RP tool. The data element shall be prepared to rptLevel2 and related write service points are present.
        self.rptWriteAccess: Optional[RptAccessEnum] = None

    def getRptHookAccess(self) -> Optional[RptAccessEnum]:
        """
        Gets whether the related data element can be modified using a post-build hooking tool.

        Returns:
            RptAccessEnum describing the hook access, or None if not set
        """
        return self.rptHookAccess

    def setRptHookAccess(self, value: Optional[RptAccessEnum]) -> "RptSwPrototypingAccess":
        """
        Sets whether the related data element can be modified using a post-build hooking tool.
        A None value is a no-op and does not overwrite an existing access.

        Args:
            value: The RptAccessEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptHookAccess = value
        return self

    def getRptReadAccess(self) -> Optional[RptAccessEnum]:
        """
        Gets whether the related data element can be used as input for bypass functionality by the RP tool.

        Returns:
            RptAccessEnum describing the read access, or None if not set
        """
        return self.rptReadAccess

    def setRptReadAccess(self, value: Optional[RptAccessEnum]) -> "RptSwPrototypingAccess":
        """
        Sets whether the related data element can be used as input for bypass functionality by the RP tool.
        A None value is a no-op and does not overwrite an existing access.

        Args:
            value: The RptAccessEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptReadAccess = value
        return self

    def getRptWriteAccess(self) -> Optional[RptAccessEnum]:
        """
        Gets whether the related data element can be used as output for bypass functionality by the RP tool.

        Returns:
            RptAccessEnum describing the write access, or None if not set
        """
        return self.rptWriteAccess

    def setRptWriteAccess(self, value: Optional[RptAccessEnum]) -> "RptSwPrototypingAccess":
        """
        Sets whether the related data element can be used as output for bypass functionality by the RP tool.
        A None value is a no-op and does not overwrite an existing access.

        Args:
            value: The RptAccessEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptWriteAccess = value
        return self


class RptServicePoint(Identifiable):
    """
    Description of a Service Point implemented for rapid prototyping.
    """

    # RptServicePoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.26, p.206
    # Spec verified: R23-11
    # [x] __init__                   [x] impl  [x] docstring  [x] test
    # [x] getServiceId               [x] impl  [x] docstring  [x] test
    # [x] setServiceId               [x] impl  [x] docstring  [x] test
    # [x] getSymbol                  [x] impl  [x] docstring  [x] test
    # [x] setSymbol                  [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the RptServicePoint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this service point
            short_name: The unique short name of this service point
        """
        super().__init__(parent, short_name)

        # Unique ID (Range: 0 ... 65535) representing the service point.
        self.serviceId: Optional[PositiveInteger] = None

        # Complete symbol of the function implementing the service point. This symbol is used for post-build hooking purposes.
        self.symbol: Optional[CIdentifier] = None

    def getServiceId(self) -> Optional[PositiveInteger]:
        """
        Gets the unique ID representing the service point.

        Returns:
            PositiveInteger representing the service point ID, or None if not set
        """
        return self.serviceId

    def setServiceId(self, value: Optional[PositiveInteger]) -> "RptServicePoint":
        """
        Sets the unique ID representing the service point.
        A None value is a no-op and does not overwrite an existing ID.

        Args:
            value: The service point ID to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.serviceId = value
        return self

    def getSymbol(self) -> Optional[CIdentifier]:
        """
        Gets the complete symbol of the function implementing the service point.

        Returns:
            CIdentifier representing the symbol, or None if not set
        """
        return self.symbol

    def setSymbol(self, value: Optional[CIdentifier]) -> "RptServicePoint":
        """
        Sets the complete symbol of the function implementing the service point.
        A None value is a no-op and does not overwrite an existing symbol.

        Args:
            value: The CIdentifier symbol to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.symbol = value
        return self


class McFunctionDataRefSet(ARObject):
    """
    Refers to a set of data assigned to an McFunction in a particular role. The data are given • either by entries in a FlatMap • or by data instances that are part of MC support data. These two possibilities are exclusive within a given McFunctionDataRefSet. Which one to use depends on the process and tool environment. The set is subject to variability because the same functional model may be used with various representation of the data.
    """

    # McFunctionDataRefSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.9, p.187
    # Spec verified: R23-11
    # [x] __init__                       [x] impl  [x] docstring  [x] test
    # [x] addFlatMapEntryRef             [x] impl  [x] docstring  [x] test
    # [x] getFlatMapEntryRefs            [x] impl  [x] docstring  [x] test
    # [x] addMcDataInstanceRef           [x] impl  [x] docstring  [x] test
    # [x] getMcDataInstanceRefs          [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the McFunctionDataRefSet with default values.
        """
        super().__init__()

        # Refers to an entry in a FlatMap that is part of the set, for example a calibration parameter or measured variable. Tags: xml.sequenceOffset=10
        self.flatMapEntryRefs: List[RefType] = []

        # Refers to a data instance within MC support data that is part of the set, i.e. a calibration parameter or measured variable. Tags: xml.sequenceOffset=20
        self.mcDataInstanceRefs: List[RefType] = []

    def addFlatMapEntryRef(self, value: Optional[RefType]) -> "McFunctionDataRefSet":
        """
        Adds a reference to an entry in a FlatMap that is part of the set, for example a calibration parameter or measured variable.
        A None value is a no-op and does not append anything.

        Args:
            value: The FlatMap entry reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.flatMapEntryRefs.append(value)
        return self

    def getFlatMapEntryRefs(self) -> List[RefType]:
        """
        Gets the references to entries in a FlatMap that are part of the set, for example calibration parameters or measured variables.

        Returns:
            List of RefType instances referencing FlatInstanceDescriptor elements
        """
        return self.flatMapEntryRefs

    def addMcDataInstanceRef(self, value: Optional[RefType]) -> "McFunctionDataRefSet":
        """
        Adds a reference to a data instance within MC support data that is part of the set, i.e. a calibration parameter or measured variable.
        A None value is a no-op and does not append anything.

        Args:
            value: The MC data instance reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcDataInstanceRefs.append(value)
        return self

    def getMcDataInstanceRefs(self) -> List[RefType]:
        """
        Gets the references to data instances within MC support data that are part of the set, i.e. calibration parameters or measured variables.

        Returns:
            List of RefType instances referencing McDataInstance elements
        """
        return self.mcDataInstanceRefs


class RptExecutableEntityEvent(Identifiable):
    """
    This describes an ExecutableEntity event instance which can be bypassed.
    """

    # RptExecutableEntityEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.17, p.201
    # Spec verified: R23-11
    # [x] __init__                        [x] impl  [x] docstring  [x] test
    # [x] addExecutionContextRef          [x] impl  [x] docstring  [x] test
    # [x] getExecutionContextRefs         [x] impl  [x] docstring  [x] test
    # [x] addMcDataAssignment             [x] impl  [x] docstring  [x] test
    # [x] getMcDataAssignments            [x] impl  [x] docstring  [x] test
    # [x] getRptEventId                   [x] impl  [x] docstring  [x] test
    # [x] setRptEventId                   [x] impl  [x] docstring  [x] test
    # [x] getRptExecutableEntityProperties [x] impl [x] docstring  [x] test
    # [x] setRptExecutableEntityProperties [x] impl [x] docstring  [x] test
    # [x] getRptImplPolicy                [x] impl  [x] docstring  [x] test
    # [x] setRptImplPolicy                [x] impl  [x] docstring  [x] test
    # [x] addRptServicePointPostRef       [x] impl  [x] docstring  [x] test
    # [x] getRptServicePointPostRefs      [x] impl  [x] docstring  [x] test
    # [x] addRptServicePointPreRef        [x] impl  [x] docstring  [x] test
    # [x] getRptServicePointPreRefs       [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the RptExecutableEntityEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # This describes the context in which the event of the executable entity is executed.
        self.executionContextRefs: List[RefType] = []

        # Reference to related McDataElements describing the implementation of "RP runnable disabler flag" and "stimulation enabler flag" The possible roles of the RoleBasedMcDataAssignment.role attribute are: • RpRunnableDisablerFlag"
        self.mcDataAssignments: List[RoleBasedMcDataAssignment] = []

        # RPT event id used for service points call.
        self.rptEventId: Optional[PositiveInteger] = None

        # Describes the implemented code preparation for rapid prototyping at ExecutableEntity invocation.
        self.rptExecutableEntityProperties: Optional[RptExecutableEntityProperties] = None

        # Describes the RptImplPolicy of a RptExecutableEvent for service based bypassing.
        self.rptImplPolicy: Optional[RptImplPolicy] = None

        # This describes the applicable Post Service Points for a RTEEvent / BswEvent of a bypassed ExecutableEntity.
        self.rptServicePointPostRefs: List[RefType] = []

        # This describes the applicable Pre Service Points for a RTEEvent / BswEvent of a bypassed ExecutableEntity.
        self.rptServicePointPreRefs: List[RefType] = []

    def addExecutionContextRef(self, value: Optional[RefType]) -> "RptExecutableEntityEvent":
        """
        Adds a reference to the context in which the event of the executable entity is executed.
        A None value is a no-op and does not append anything.

        Args:
            value: The reference to a RptExecutionContext

        Returns:
            self for method chaining
        """
        if value is not None:
            self.executionContextRefs.append(value)
        return self

    def getExecutionContextRefs(self) -> List[RefType]:
        """
        Gets the references to the contexts in which the event of the executable entity is executed.

        Returns:
            List of RefType instances referencing RptExecutionContext elements
        """
        return self.executionContextRefs

    def addMcDataAssignment(self, value: Optional[RoleBasedMcDataAssignment]) -> "RptExecutableEntityEvent":
        """
        Adds a reference to related McDataElements describing the implementation of "RP runnable disabler flag" and "stimulation enabler flag".
        A None value is a no-op and does not append anything.

        Args:
            value: The role-based MC data assignment to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcDataAssignments.append(value)
        return self

    def getMcDataAssignments(self) -> List[RoleBasedMcDataAssignment]:
        """
        Gets the references to related McDataElements describing the implementation of "RP runnable disabler flag" and "stimulation enabler flag".

        Returns:
            List of RoleBasedMcDataAssignment instances
        """
        return self.mcDataAssignments

    def getRptEventId(self) -> Optional[PositiveInteger]:
        """
        Gets the RPT event id used for service points call.

        Returns:
            PositiveInteger representing the RPT event id, or None if not set
        """
        return self.rptEventId

    def setRptEventId(self, value: Optional[PositiveInteger]) -> "RptExecutableEntityEvent":
        """
        Sets the RPT event id used for service points call.
        A None value is a no-op and does not overwrite an existing id.

        Args:
            value: The RPT event id to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptEventId = value
        return self

    def getRptExecutableEntityProperties(self) -> Optional[RptExecutableEntityProperties]:
        """
        Gets the implemented code preparation for rapid prototyping at ExecutableEntity invocation.

        Returns:
            RptExecutableEntityProperties instance, or None if not set
        """
        return self.rptExecutableEntityProperties

    def setRptExecutableEntityProperties(self, value: Optional[RptExecutableEntityProperties]) -> "RptExecutableEntityEvent":
        """
        Sets the implemented code preparation for rapid prototyping at ExecutableEntity invocation.
        A None value is a no-op and does not overwrite existing properties.

        Args:
            value: The RptExecutableEntityProperties to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptExecutableEntityProperties = value
        return self

    def getRptImplPolicy(self) -> Optional[RptImplPolicy]:
        """
        Gets the RptImplPolicy of a RptExecutableEvent for service based bypassing.

        Returns:
            RptImplPolicy instance, or None if not set
        """
        return self.rptImplPolicy

    def setRptImplPolicy(self, value: Optional[RptImplPolicy]) -> "RptExecutableEntityEvent":
        """
        Sets the RptImplPolicy of a RptExecutableEvent for service based bypassing.
        A None value is a no-op and does not overwrite an existing policy.

        Args:
            value: The RptImplPolicy to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptImplPolicy = value
        return self

    def addRptServicePointPostRef(self, value: Optional[RefType]) -> "RptExecutableEntityEvent":
        """
        Adds a reference to an applicable Post Service Point for a RTEEvent / BswEvent of a bypassed ExecutableEntity.
        A None value is a no-op and does not append anything.

        Args:
            value: The reference to a RptServicePoint

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptServicePointPostRefs.append(value)
        return self

    def getRptServicePointPostRefs(self) -> List[RefType]:
        """
        Gets the references to applicable Post Service Points for a RTEEvent / BswEvent of a bypassed ExecutableEntity.

        Returns:
            List of RefType instances referencing RptServicePoint elements
        """
        return self.rptServicePointPostRefs

    def addRptServicePointPreRef(self, value: Optional[RefType]) -> "RptExecutableEntityEvent":
        """
        Adds a reference to an applicable Pre Service Point for a RTEEvent / BswEvent of a bypassed ExecutableEntity.
        A None value is a no-op and does not append anything.

        Args:
            value: The reference to a RptServicePoint

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptServicePointPreRefs.append(value)
        return self

    def getRptServicePointPreRefs(self) -> List[RefType]:
        """
        Gets the references to applicable Pre Service Points for a RTEEvent / BswEvent of a bypassed ExecutableEntity.

        Returns:
            List of RefType instances referencing RptServicePoint elements
        """
        return self.rptServicePointPreRefs


class RptExecutableEntity(Identifiable):
    """
    This describes a ExecutableEntity instance which can be bypassed.
    """

    # RptExecutableEntity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.16, p.200
    # Spec verified: R23-11
    # [x] __init__                       [x] impl  [x] docstring  [x] test
    # [x] createRptExecutableEntityEvent [x] impl  [x] docstring  [x] test
    # [x] getRptExecutableEntityEvents   [x] impl  [x] docstring  [x] test
    # [x] addRptRead                     [x] impl  [x] docstring  [x] test
    # [x] getRptReads                    [x] impl  [x] docstring  [x] test
    # [x] addRptWrite                    [x] impl  [x] docstring  [x] test
    # [x] getRptWrites                   [x] impl  [x] docstring  [x] test
    # [x] getSymbol                      [x] impl  [x] docstring  [x] test
    # [x] setSymbol                      [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the RptExecutableEntity with a parent and short name.

        Args:
            parent: The parent ARObject that contains this executable entity
            short_name: The unique short name of this executable entity
        """
        super().__init__(parent, short_name)

        # ExecutableEntity event instance activation the owning RptExecutableEntity.
        self.rptExecutableEntityEvents: List[RptExecutableEntityEvent] = []

        # read access to a variable
        self.rptReads: List[RoleBasedMcDataAssignment] = []

        # write access to a variable
        self.rptWrites: List[RoleBasedMcDataAssignment] = []

        # The symbol describing this ExecutableEntity's entry point.
        self.symbol: Optional[CIdentifier] = None

    def createRptExecutableEntityEvent(self, short_name: str) -> RptExecutableEntityEvent:
        """
        Creates a RptExecutableEntityEvent and adds it to this executable entity.
        If an event with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new executable entity event

        Returns:
            The created (or existing) RptExecutableEntityEvent
        """
        for event in self.rptExecutableEntityEvents:
            if event.short_name == short_name:
                return event
        event = RptExecutableEntityEvent(self, short_name)
        self.rptExecutableEntityEvents.append(event)
        return event

    def getRptExecutableEntityEvents(self) -> List[RptExecutableEntityEvent]:
        """
        Gets the executable entity events aggregated by this executable entity.

        Returns:
            List of RptExecutableEntityEvent instances
        """
        return self.rptExecutableEntityEvents

    def addRptRead(self, value: Optional[RoleBasedMcDataAssignment]) -> "RptExecutableEntity":
        """
        Adds a read access to a variable to this executable entity.
        A None value is a no-op and does not append anything.

        Args:
            value: The role-based MC data assignment for the read access

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptReads.append(value)
        return self

    def getRptReads(self) -> List[RoleBasedMcDataAssignment]:
        """
        Gets the read accesses to variables aggregated by this executable entity.

        Returns:
            List of RoleBasedMcDataAssignment instances
        """
        return self.rptReads

    def addRptWrite(self, value: Optional[RoleBasedMcDataAssignment]) -> "RptExecutableEntity":
        """
        Adds a write access to a variable to this executable entity.
        A None value is a no-op and does not append anything.

        Args:
            value: The role-based MC data assignment for the write access

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rptWrites.append(value)
        return self

    def getRptWrites(self) -> List[RoleBasedMcDataAssignment]:
        """
        Gets the write accesses to variables aggregated by this executable entity.

        Returns:
            List of RoleBasedMcDataAssignment instances
        """
        return self.rptWrites

    def getSymbol(self) -> Optional[CIdentifier]:
        """
        Gets the symbol describing this ExecutableEntity's entry point.

        Returns:
            CIdentifier representing the entry point symbol, or None if not set
        """
        return self.symbol

    def setSymbol(self, value: Optional[CIdentifier]) -> "RptExecutableEntity":
        """
        Sets the symbol describing this ExecutableEntity's entry point.
        A None value is a no-op and does not overwrite an existing symbol.

        Args:
            value: The CIdentifier symbol to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.symbol = value
        return self


class RptComponent(Identifiable):
    """
    Description of component instance for which rapid prototyping support is implemented.
    """

    # RptComponent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.15, p.199
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] addMcDataAssignment          [x] impl  [x] docstring  [x] test
    # [x] getMcDataAssignments         [x] impl  [x] docstring  [x] test
    # [x] getRpImplPolicy              [x] impl  [x] docstring  [x] test
    # [x] setRpImplPolicy              [x] impl  [x] docstring  [x] test
    # [x] createRptExecutableEntity    [x] impl  [x] docstring  [x] test
    # [x] getRptExecutableEntities     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the RptComponent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this component
            short_name: The unique short name of this component
        """
        super().__init__(parent, short_name)

        # Reference to related McDataElement describing the implementation of "RP global buffer", "RP global measurement buffer", "RP enabler flag" and the "RP runnable disabler flag".
        self.mcDataAssignments: List[RoleBasedMcDataAssignment] = []

        # Describes the implemented code preparation for rapid prototyping at data accesses.
        self.rpImplPolicy: Optional[RptImplPolicy] = None

        # ExecutableEntity instance which can be bypassed.
        self.rptExecutableEntities: List[RptExecutableEntity] = []

    def addMcDataAssignment(self, value: Optional[RoleBasedMcDataAssignment]) -> "RptComponent":
        """
        Adds a reference to a related McDataElement describing the implementation of "RP global buffer", "RP global measurement buffer", "RP enabler flag" and the "RP runnable disabler flag".
        A None value is a no-op and does not append anything.

        Args:
            value: The role-based MC data assignment to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.mcDataAssignments.append(value)
        return self

    def getMcDataAssignments(self) -> List[RoleBasedMcDataAssignment]:
        """
        Gets the references to related McDataElements describing the implementation of "RP global buffer", "RP global measurement buffer", "RP enabler flag" and the "RP runnable disabler flag".

        Returns:
            List of RoleBasedMcDataAssignment instances
        """
        return self.mcDataAssignments

    def getRpImplPolicy(self) -> Optional[RptImplPolicy]:
        """
        Gets the implemented code preparation for rapid prototyping at data accesses.

        Returns:
            RptImplPolicy instance, or None if not set
        """
        return self.rpImplPolicy

    def setRpImplPolicy(self, value: Optional[RptImplPolicy]) -> "RptComponent":
        """
        Sets the implemented code preparation for rapid prototyping at data accesses.
        A None value is a no-op and does not overwrite an existing policy.

        Args:
            value: The RptImplPolicy to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rpImplPolicy = value
        return self

    def createRptExecutableEntity(self, short_name: str) -> RptExecutableEntity:
        """
        Creates a RptExecutableEntity and adds it to this component.
        If an executable entity with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new executable entity

        Returns:
            The created (or existing) RptExecutableEntity
        """
        for executable_entity in self.rptExecutableEntities:
            if executable_entity.short_name == short_name:
                return executable_entity
        executable_entity = RptExecutableEntity(self, short_name)
        self.rptExecutableEntities.append(executable_entity)
        return executable_entity

    def getRptExecutableEntities(self) -> List[RptExecutableEntity]:
        """
        Gets the executable entity instances which can be bypassed.

        Returns:
            List of RptExecutableEntity instances
        """
        return self.rptExecutableEntities


class RptSupportData(ARObject):
    """
    Root element for rapid prototyping support data related to one Implementation artifact on an ECU, in particular the RTE. The rapid prototyping support data may reference to elements provided for McSupportData.
    """

    # RptSupportData method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 9.13, p.198
    # Spec verified: R23-11
    # [x] __init__                   [x] impl  [x] docstring  [x] test
    # [x] createExecutionContext     [x] impl  [x] docstring  [x] test
    # [x] getExecutionContexts       [x] impl  [x] docstring  [x] test
    # [x] createRptComponent         [x] impl  [x] docstring  [x] test
    # [x] getRptComponents           [x] impl  [x] docstring  [x] test
    # [x] createRptServicePoint      [x] impl  [x] docstring  [x] test
    # [x] getRptServicePoints        [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the RptSupportData.
        """
        super().__init__()

        # Defines an environment for the execution of ExecutableEntites.
        self.executionContexts: List[RptExecutionContext] = []

        # Description of components for which rapid prototyping support is implemented.
        self.rptComponents: List[RptComponent] = []

        # This aggregation represents the collection of service points associated with the enclosing RptSuportData
        self.rptServicePoints: List[RptServicePoint] = []

    def createExecutionContext(self, short_name: str) -> RptExecutionContext:
        """
        Creates a RptExecutionContext and adds it to this support data.
        If an execution context with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new execution context

        Returns:
            The created (or existing) RptExecutionContext
        """
        for context in self.executionContexts:
            if context.short_name == short_name:
                return context
        context = RptExecutionContext(self, short_name)
        self.executionContexts.append(context)
        return context

    def getExecutionContexts(self) -> List[RptExecutionContext]:
        """
        Gets the execution environments aggregated by this support data.

        Returns:
            List of RptExecutionContext instances
        """
        return self.executionContexts

    def createRptComponent(self, short_name: str) -> RptComponent:
        """
        Creates a RptComponent and adds it to this support data.
        If a component with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new component

        Returns:
            The created (or existing) RptComponent
        """
        for component in self.rptComponents:
            if component.short_name == short_name:
                return component
        component = RptComponent(self, short_name)
        self.rptComponents.append(component)
        return component

    def getRptComponents(self) -> List[RptComponent]:
        """
        Gets the components for which rapid prototyping support is implemented.

        Returns:
            List of RptComponent instances
        """
        return self.rptComponents

    def createRptServicePoint(self, short_name: str) -> RptServicePoint:
        """
        Creates a RptServicePoint and adds it to this support data.
        If a service point with the given short name already exists, it is returned instead.

        Args:
            short_name: The short name for the new service point

        Returns:
            The created (or existing) RptServicePoint
        """
        for service_point in self.rptServicePoints:
            if service_point.short_name == short_name:
                return service_point
        service_point = RptServicePoint(self, short_name)
        self.rptServicePoints.append(service_point)
        return service_point

    def getRptServicePoints(self) -> List[RptServicePoint]:
        """
        Gets the service points associated with this support data.

        Returns:
            List of RptServicePoint instances
        """
        return self.rptServicePoints


__all__ = [
    "McFunctionDataRefSet",
    "RptAccessEnum",
    "RptComponent",
    "RptEnablerImplTypeEnum",
    "RptExecutableEntity",
    "RptExecutableEntityEvent",
    "RptExecutionContext",
    "RptExecutionControlEnum",
    "RptPreparationEnum",
    "RptServicePoint",
    "RptSupportData",
    "RptSwPrototypingAccess",
]
