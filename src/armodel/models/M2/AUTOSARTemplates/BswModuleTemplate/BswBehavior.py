"""
This module contains classes for representing AUTOSAR Basic Software (BSW) module behavior.
BSW behavior describes how BSW modules execute, including their entities, events, and execution policies.

These classes are used to model:
- BSW module entities and their call points
- Different types of events that trigger execution
- Variable access patterns and data policies
- Internal behavior of BSW modules
"""

from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from abc import ABC
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.InstanceRefs import ModeInBswModuleDescriptionInstanceRef

from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import AbstractEvent, ApiPrincipleEnum, ExecutableEntity, InternalBehavior
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment, ServiceDependency, ServiceNeeds
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Float, Boolean
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String, TimeValue, Identifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping import BswServiceDependencyIdent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeActivationKind


class BswModuleCallPoint(Referrable, VariationPointCapable, ABC):
    """
    Represents a call point for a BSW module, which defines how the module can be called.
    This is an abstract base class for different types of call points.
    """

    # BswModuleCallPoint method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getContextLimitationRefs     [x] impl  [x] docstring  [ ] test
    # [x] addContextLimitationRef      [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswModuleCallPoint with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this call point
            short_name: The unique short name of this call point
        """
        if type(self) is BswModuleCallPoint:
            raise TypeError("BswModuleCallPoint is an abstract class.")
        super().__init__(parent, short_name)

        # List of context limitation references that apply to this call point
        self.contextLimitationRefs: List[RefType] = []

    def getContextLimitationRefs(self):
        """
        Gets the list of context limitation references for this call point.

        Returns:
            List of context limitation references
        """
        return self.contextLimitationRefs

    def addContextLimitationRef(self, value):
        """
        Adds a context limitation reference to this call point.

        Args:
            value: The context limitation reference to add

        Returns:
            self for method chaining
        """
        self.contextLimitationRefs.append(value)
        return self


class BswAsynchronousServerCallPoint(BswModuleCallPoint):
    """
    Represents an asynchronous procedure call point via the BSW Scheduler.
    """

    # BswAsynchronousServerCallPoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.13, p.80
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCalledEntryRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCalledEntryRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The entry to be called.
        self.calledEntryRef: Optional[RefType] = None

    def getCalledEntryRef(self) -> Optional[RefType]:
        """
        The entry to be called.
        """
        return self.calledEntryRef

    def setCalledEntryRef(self, value: Optional[RefType]) -> BswAsynchronousServerCallPoint:
        """
        The entry to be called.
        Only sets the value if it is not None.

        Args:
            value: The reference to the entry to be called

        Returns:
            self for method chaining
        """
        if value is not None:
            self.calledEntryRef = value
        return self


class BswDirectCallPoint(BswModuleCallPoint):
    """
    Represents a direct call point in a BSW module.
    This call point is used for direct synchronous calls to BSW module entries.
    """

    # BswDirectCallPoint method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getCalledEntryRef            [x] impl  [x] docstring  [ ] test
    # [x] setCalledEntryRef            [x] impl  [x] docstring  [x] test
    # [ ] getCalledFromWithinExclusiveAreaRef [x] impl  [x] docstring  [ ] test
    # [x] setCalledFromWithinExclusiveAreaRef [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswDirectCallPoint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this call point
            short_name: The unique short name of this call point
        """
        super().__init__(parent, short_name)

        # Reference to the entry that is called by this direct call point
        self.calledEntryRef: RefType = None
        # Reference to an exclusive area from which this call is made
        self.calledFromWithinExclusiveAreaRef: RefType = None

    def getCalledEntryRef(self):
        """
        Gets the reference to the entry that is called by this direct call point.

        Returns:
            Reference to the called entry
        """
        return self.calledEntryRef

    def setCalledEntryRef(self, value):
        """
        Sets the reference to the entry that is called by this direct call point.
        Only sets the value if it is not None.

        Args:
            value: The entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.calledEntryRef = value
        return self

    def getCalledFromWithinExclusiveAreaRef(self):
        """
        Gets the reference to the exclusive area from which this call is made.

        Returns:
            Reference to the exclusive area
        """
        return self.calledFromWithinExclusiveAreaRef

    def setCalledFromWithinExclusiveAreaRef(self, value):
        """
        Sets the reference to the exclusive area from which this call is made.
        Only sets the value if it is not None.

        Args:
            value: The exclusive area reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.calledFromWithinExclusiveAreaRef = value
        return self


class BswSynchronousServerCallPoint(BswModuleCallPoint):
    """
    Represents a synchronous server call point in a BSW module.
    This call point is used when the server operation is executed synchronously.
    """

    # BswSynchronousServerCallPoint method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getCalledEntryRef            [x] impl  [x] docstring  [ ] test
    # [x] setCalledEntryRef            [x] impl  [x] docstring  [x] test
    # [ ] getCalledFromWithinExclusiveAreaRef [x] impl  [x] docstring  [ ] test
    # [x] setCalledFromWithinExclusiveAreaRef [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswSynchronousServerCallPoint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this call point
            short_name: The unique short name of this call point
        """
        super().__init__(parent, short_name)

        # Reference to the entry that is called by this synchronous call point
        self.calledEntryRef: RefType = None
        # Reference to an exclusive area from which this call is made
        self.calledFromWithinExclusiveAreaRef: RefType = None

    def getCalledEntryRef(self):
        """
        Gets the reference to the entry that is called by this synchronous call point.

        Returns:
            Reference to the called entry
        """
        return self.calledEntryRef

    def setCalledEntryRef(self, value):
        """
        Sets the reference to the entry that is called by this synchronous call point.
        Only sets the value if it is not None.

        Args:
            value: The entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.calledEntryRef = value
        return self

    def getCalledFromWithinExclusiveAreaRef(self):
        """
        Gets the reference to the exclusive area from which this call is made.

        Returns:
            Reference to the exclusive area
        """
        return self.calledFromWithinExclusiveAreaRef

    def setCalledFromWithinExclusiveAreaRef(self, value):
        """
        Sets the reference to the exclusive area from which this call is made.
        Only sets the value if it is not None.

        Args:
            value: The exclusive area reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.calledFromWithinExclusiveAreaRef = value
        return self


class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):
    """
    The callback point for an BswAsynchronousServerCallPoint i.e. the point at
    which the result can be retrieved from the BSW Scheduler.
    """

    # BswAsynchronousServerCallResultPoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.14, p.80
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAsynchronousServerCallPointRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAsynchronousServerCallPointRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The call point invoking the call to which the result belongs.
        self.asynchronousServerCallPointRef: Optional[RefType] = None

    def getAsynchronousServerCallPointRef(self) -> Optional[RefType]:
        """
        The call point invoking the call to which the result belongs.
        """
        return self.asynchronousServerCallPointRef

    def setAsynchronousServerCallPointRef(self, value: Optional[RefType]) -> BswAsynchronousServerCallResultPoint:
        """
        The call point invoking the call to which the result belongs.
        Only sets the value if it is not None.

        Args:
            value: The reference to the call point invoking the call

        Returns:
            self for method chaining
        """
        if value is not None:
            self.asynchronousServerCallPointRef = value
        return self


class BswSchedulerNamePrefix(ImplementationProps, VariationPointCapable):
    """
    A prefix to be used in names of generated code artifacts which make up the
    interface of a BSW module to the BswScheduler.
    """

    # BswSchedulerNamePrefix method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.20, p.86
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswVariableAccess(Referrable, VariationPointCapable):
    """
    Represents access to a variable by a BSW module entity.
    This class defines how a BSW module accesses variables during execution.
    """

    # BswVariableAccess method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getAccessedVariableRef       [x] impl  [x] docstring  [ ] test
    # [x] setAccessedVariableRef       [x] impl  [x] docstring  [x] test
    # [ ] getContextLimitationRefs     [x] impl  [x] docstring  [ ] test
    # [x] addContextLimitationRef      [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswVariableAccess with a parent and short name.

        Args:
            parent: The parent ARObject that contains this variable access
            short_name: The unique short name of this variable access
        """
        super().__init__(parent, short_name)

        # Reference to the variable being accessed
        self.accessedVariableRef: RefType = None
        # List of context limitation references that apply to this variable access
        self.contextLimitationRefs: List[RefType] = []

    def getAccessedVariableRef(self):
        """
        Gets the reference to the variable being accessed.

        Returns:
            Reference to the accessed variable
        """
        return self.accessedVariableRef

    def setAccessedVariableRef(self, value):
        """
        Sets the reference to the variable being accessed.

        Args:
            value: The variable reference to set

        Returns:
            self for method chaining
        """
        self.accessedVariableRef = value
        return self

    def getContextLimitationRefs(self):
        """
        Gets the list of context limitation references for this variable access.

        Returns:
            List of context limitation references
        """
        return self.contextLimitationRefs

    def addContextLimitationRef(self, value):
        """
        Adds a context limitation reference to this variable access.

        Args:
            value: The context limitation reference to add

        Returns:
            self for method chaining
        """
        self.contextLimitationRefs.append(value)
        return self


class BswDistinguishedPartition(Referrable, VariationPointCapable):
    """
    Each instance of this meta-class represents an abstract partition in which context
    the code of the enclosing BswModuleBehavior can be executed. The intended use case
    is to distinguish between several partitions in order to implement different behavior
    per partition, for example to behave either as a master or satellite in a multicore
    ECU with shared BSW code.
    """

    # BswDistinguishedPartition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.50, p.118
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswModuleEntity(ExecutableEntity, VariationPointCapable, ABC):
    """
    Specifies the smallest code fragment which can be described for a BSW module or cluster within AUTOSAR.
    """

    # BswModuleEntity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.4, p.72
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAccessedModeGroupRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addAccessedModeGroupRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getActivationPointRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addActivationPointRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCallPoints                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createBswAsynchronousServerCallPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createBswSynchronousServerCallPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataReceivePoints         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createDataReceivePoint       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataSendPoints            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createDataSendPoint          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getImplementedEntryRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setImplementedEntryRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIssuedTriggerRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addIssuedTriggerRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getManagedModeGroupRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addManagedModeGroupRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSchedulerNamePrefixRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSchedulerNamePrefixRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is BswModuleEntity:
            raise TypeError("BswModuleEntity is an abstract class.")
        super().__init__(parent, short_name)

        # A mode group which is accessed via API call by this entity. It shall be a ModeDeclarationGroupPrototype required by this module or cluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=accessedModeGroup.modeDeclaration GroupPrototype, accessedModeGroup.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.accessedModeGroupRefs: List[RefType] = []

        # Activation point used by the module entity to activate one or more internal triggers. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=activationPoint.bswInternalTriggeringPoint, activationPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.activationPointRefs: List[RefType] = []

        # A call point used in the code of this entity. The variability of this association is especially targeted at debug scenarios: It is possible to have one variant calling into the AUTOSAR debug module and another one which doesn't. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=callPoint.shortName, callPoint.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.callPoints: List[BswModuleCallPoint] = []

        # The data is received via the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReceivePoint.shortName, dataReceive Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.dataReceivePoints: List[BswVariableAccess] = []

        # The data is sent via the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataSendPoint.shortName, dataSend Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.dataSendPoints: List[BswVariableAccess] = []

        # The entry which is implemented by this module entity.
        self.implementedEntryRef: Optional[RefType] = None

        # A trigger issued by this entity via BSW Scheduler API call. It shall be a BswTrigger released (i.e. owned) by this module or cluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=issuedTrigger.trigger, issuedTrigger.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.issuedTriggerRefs: List[RefType] = []

        # A mode group which is managed by this entity. It shall be a ModeDeclarationGroupPrototype provided by this module or cluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=managedModeGroup.modeDeclaration GroupPrototype, managedModeGroup.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.managedModeGroupRefs: List[RefType] = []

        # A prefix to be used in generated names for the Bsw ModuleScheduler in the context of this BswModuleEntity, for example entry point prototypes, macros for dealing with exclusive areas, header file names. Details are defined in the SWS RTE. The prefix supersedes default rules for the prefix of those names.
        self.schedulerNamePrefixRef: Optional[RefType] = None

    def getAccessedModeGroupRefs(self) -> List[RefType]:
        """
        Gets the mode groups which are accessed via API call by this entity. A mode group which is accessed via API call by this entity. It shall be a ModeDeclarationGroupPrototype required by this module or cluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=accessedModeGroup.modeDeclaration GroupPrototype, accessedModeGroup.variation Point.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of RefType instances
        """
        return self.accessedModeGroupRefs

    def addAccessedModeGroupRef(self, value: RefType) -> BswModuleEntity:
        """
        Adds a mode group accessed via API call by this entity. A mode group which is accessed via API call by this entity. It shall be a ModeDeclarationGroupPrototype required by this module or cluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=accessedModeGroup.modeDeclaration GroupPrototype, accessedModeGroup.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        Only adds the value if it is not None.

        Args:
            value: The mode group reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.accessedModeGroupRefs.append(value)
        return self

    def getActivationPointRefs(self) -> List[RefType]:
        """
        Gets the activation points used by the module entity to activate one or more internal triggers. Activation point used by the module entity to activate one or more internal triggers. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=activationPoint.bswInternalTriggeringPoint, activationPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of RefType instances
        """
        return self.activationPointRefs

    def addActivationPointRef(self, value: RefType) -> BswModuleEntity:
        """
        Adds an activation point used to activate one or more internal triggers. Activation point used by the module entity to activate one or more internal triggers. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=activationPoint.bswInternalTriggeringPoint, activationPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        Only adds the value if it is not None.

        Args:
            value: The activation point reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.activationPointRefs.append(value)
        return self

    def getCallPoints(self) -> List[BswModuleCallPoint]:
        """
        Gets the call points used in the code of this entity. A call point used in the code of this entity. The variability of this association is especially targeted at debug scenarios: It is possible to have one variant calling into the AUTOSAR debug module and another one which doesn't. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=callPoint.shortName, callPoint.variation Point.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of BswModuleCallPoint instances
        """
        return self.callPoints

    def createBswAsynchronousServerCallPoint(self, short_name: str) -> BswAsynchronousServerCallPoint:
        """
        Creates and adds a BswAsynchronousServerCallPoint to the call points
        used in the code of this entity. Returns the existing call point if the
        short name is already present.

        Args:
            short_name: The short name for the new call point

        Returns:
            The created BswAsynchronousServerCallPoint instance
        """
        if not self.IsElementExists(short_name, BswAsynchronousServerCallPoint):
            access = BswAsynchronousServerCallPoint(self, short_name)
            self.addElement(access)
            self.callPoints.append(access)
        return self.getElement(short_name, BswAsynchronousServerCallPoint)

    def createBswAsynchronousServerCallResultPoint(self, short_name: str) -> BswAsynchronousServerCallResultPoint:
        """
        Creates and adds a BswAsynchronousServerCallResultPoint to the call
        points used in the code of this entity. Returns the existing call point
        if the short name is already present.

        Args:
            short_name: The short name for the new result point

        Returns:
            The created BswAsynchronousServerCallResultPoint instance
        """
        if not self.IsElementExists(short_name, BswAsynchronousServerCallResultPoint):
            access = BswAsynchronousServerCallResultPoint(self, short_name)
            self.addElement(access)
            self.callPoints.append(access)
        return self.getElement(short_name, BswAsynchronousServerCallResultPoint)

    def createBswSynchronousServerCallPoint(self, short_name: str) -> BswSynchronousServerCallPoint:
        """
        Creates and adds a BswSynchronousServerCallPoint to the call points
        used in the code of this entity. Returns the existing call point if the
        short name is already present.

        Args:
            short_name: The short name for the new call point

        Returns:
            The created BswSynchronousServerCallPoint instance
        """
        if not self.IsElementExists(short_name, BswSynchronousServerCallPoint):
            access = BswSynchronousServerCallPoint(self, short_name)
            self.addElement(access)
            self.callPoints.append(access)
        return self.getElement(short_name, BswSynchronousServerCallPoint)

    def getDataReceivePoints(self) -> List[BswVariableAccess]:
        """
        Gets the variable accesses through which data is received via the BSW Scheduler. The data is received via the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReceivePoint.shortName, dataReceive Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of BswVariableAccess instances
        """
        return self.dataReceivePoints

    def createDataReceivePoint(self, short_name: str) -> BswVariableAccess:
        """
        Creates and adds a BswVariableAccess through which data is received via
        the BSW Scheduler. Returns the existing access if the short name is
        already present.

        Args:
            short_name: The short name for the new data receive point

        Returns:
            The created BswVariableAccess instance
        """
        if not self.IsElementExists(short_name, BswVariableAccess):
            access = BswVariableAccess(self, short_name)
            self.addElement(access)
            self.dataReceivePoints.append(access)
        return self.getElement(short_name, BswVariableAccess)

    def getDataSendPoints(self) -> List[BswVariableAccess]:
        """
        Gets the variable accesses through which data is sent via the BSW Scheduler. The data is sent via the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataSendPoint.shortName, dataSend Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of BswVariableAccess instances
        """
        return self.dataSendPoints

    def createDataSendPoint(self, short_name: str) -> BswVariableAccess:
        """
        Creates and adds a BswVariableAccess through which data is sent via the
        BSW Scheduler. Returns the existing access if the short name is already
        present.

        Args:
            short_name: The short name for the new data send point

        Returns:
            The created BswVariableAccess instance
        """
        if not self.IsElementExists(short_name, BswVariableAccess):
            access = BswVariableAccess(self, short_name)
            self.addElement(access)
            self.dataSendPoints.append(access)
        return self.getElement(short_name, BswVariableAccess)

    def getImplementedEntryRef(self) -> Optional[RefType]:
        """
        Gets the entry which is implemented by this module entity. The entry which is implemented by this module entity.

        Returns:
            RefType: The implemented entry reference, or None if not set
        """
        return self.implementedEntryRef

    def setImplementedEntryRef(self, value: Optional[RefType]) -> BswModuleEntity:
        """
        Sets the entry which is implemented by this module entity. The entry which is implemented by this module entity.
        Only sets the value if it is not None.

        Args:
            value: The implemented entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.implementedEntryRef = value
        return self

    def getIssuedTriggerRefs(self) -> List[RefType]:
        """
        Gets the triggers issued by this entity via BSW Scheduler API call. A trigger issued by this entity via BSW Scheduler API call. It shall be a BswTrigger released (i.e. owned) by this module or cluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=issuedTrigger.trigger, issuedTrigger.variation Point.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of RefType instances
        """
        return self.issuedTriggerRefs

    def addIssuedTriggerRef(self, value: RefType) -> BswModuleEntity:
        """
        Adds a trigger issued by this entity via BSW Scheduler API call. A trigger issued by this entity via BSW Scheduler API call. It shall be a BswTrigger released (i.e. owned) by this module or cluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=issuedTrigger.trigger, issuedTrigger.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        Only adds the value if it is not None.

        Args:
            value: The trigger reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.issuedTriggerRefs.append(value)
        return self

    def getManagedModeGroupRefs(self) -> List[RefType]:
        """
        Gets the mode groups which are managed by this entity. A mode group which is managed by this entity. It shall be a ModeDeclarationGroupPrototype provided by this module or cluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=managedModeGroup.modeDeclaration GroupPrototype, managedModeGroup.variation Point.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of RefType instances
        """
        return self.managedModeGroupRefs

    def addManagedModeGroupRef(self, value: RefType) -> BswModuleEntity:
        """
        Adds a mode group managed by this entity. A mode group which is managed by this entity. It shall be a ModeDeclarationGroupPrototype provided by this module or cluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=managedModeGroup.modeDeclaration GroupPrototype, managedModeGroup.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        Only adds the value if it is not None.

        Args:
            value: The mode group reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.managedModeGroupRefs.append(value)
        return self

    def getSchedulerNamePrefixRef(self) -> Optional[RefType]:
        """
        Gets the prefix to be used in generated names for the BswModuleScheduler in the context of this BswModuleEntity. A prefix to be used in generated names for the Bsw ModuleScheduler in the context of this BswModuleEntity, for example entry point prototypes, macros for dealing with exclusive areas, header file names. Details are defined in the SWS RTE. The prefix supersedes default rules for the prefix of those names.

        Returns:
            RefType: The scheduler name prefix reference, or None if not set
        """
        return self.schedulerNamePrefixRef

    def setSchedulerNamePrefixRef(self, value: Optional[RefType]) -> BswModuleEntity:
        """
        Sets the prefix to be used in generated names for the BswModuleScheduler in the context of this BswModuleEntity. A prefix to be used in generated names for the Bsw ModuleScheduler in the context of this BswModuleEntity, for example entry point prototypes, macros for dealing with exclusive areas, header file names. Details are defined in the SWS RTE. The prefix supersedes default rules for the prefix of those names.
        Only sets the value if it is not None.

        Args:
            value: The scheduler name prefix reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.schedulerNamePrefixRef = value
        return self


class BswCalledEntity(BswModuleEntity):
    """
    BSW module entity which is designed to be called from another BSW module
    or cluster.
    """

    # BswCalledEntity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.6, p.74
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswSchedulableEntity(BswModuleEntity):
    """
    BSW module entity, which is designed for control by the BSW Scheduler. It
    may for example implement a so-called "main" function.
    """

    # BswSchedulableEntity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.7, p.75
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswInterruptCategory(AREnum):
    """
    Enumeration for BSW interrupt categories.
    Defines whether an interrupt is a Category 1 (CAT1) or Category 2 (CAT2) interrupt.
    """

    # BswInterruptCategory method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Category 1 interrupt - directly handled by the OS
    CAT1 = "cat1"
    # Category 2 interrupt - handled by the interrupt service routine
    CAT2 = "cat2"

    def __init__(self):
        """
        Initializes the BswInterruptCategory with valid values.
        """
        super().__init__(
            (
                BswInterruptCategory.CAT1,
                BswInterruptCategory.CAT2,
            )
        )


class BswInterruptEntity(BswModuleEntity):
    """
    Represents an interrupt entity in a BSW module.
    This defines how interrupt service routines are handled in the BSW module.
    """

    # BswInterruptEntity method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getInterruptCategory         [x] impl  [x] docstring  [ ] test
    # [x] setInterruptCategory         [x] impl  [x] docstring  [x] test
    # [ ] getInterruptSource           [x] impl  [x] docstring  [ ] test
    # [x] setInterruptSource           [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswInterruptEntity with a parent and short name.

        Args:
            parent: The parent ARObject that contains this interrupt entity
            short_name: The unique short name of this interrupt entity
        """
        super().__init__(parent, short_name)

        # Category of the interrupt (CAT1 or CAT2)
        self.interruptCategory: BswInterruptCategory = None
        # Source identifier for the interrupt
        self.interruptSource: String = None

    def getInterruptCategory(self):
        """
        Gets the interrupt category for this interrupt entity.

        Returns:
            The interrupt category (CAT1 or CAT2)
        """
        return self.interruptCategory

    def setInterruptCategory(self, value):
        """
        Sets the interrupt category for this interrupt entity.

        Args:
            value: The interrupt category to set

        Returns:
            self for method chaining
        """
        self.interruptCategory = value
        return self

    def getInterruptSource(self):
        """
        Gets the interrupt source identifier for this interrupt entity.

        Returns:
            The interrupt source identifier
        """
        return self.interruptSource

    def setInterruptSource(self, value):
        """
        Sets the interrupt source identifier for this interrupt entity.

        Args:
            value: The interrupt source identifier to set

        Returns:
            self for method chaining
        """
        self.interruptSource = value
        return self


class BswEvent(AbstractEvent, VariationPointCapable, ABC):
    """
    Base class of various kinds of events which are used to trigger a BswModuleEntity of this BSW module or cluster. The event is local to the BSW module or cluster. The short name of the meta-class instance is intended as an input to configure the required API of the BSW Scheduler.
    """

    # BswEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.22, p.87
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextLimitationRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextLimitationRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDisabledInModeIRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addDisabledInModeIRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getStartsOnEventRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setStartsOnEventRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is BswEvent:
            raise TypeError("BswEvent is an abstract class.")

        super().__init__(parent, short_name)

        # The existence of this reference indicates that the usage of the event is limited to the context of the referred Bsw DistinguishedPartitions.
        self.contextLimitationRefs: List[RefType] = []

        # The modes, in which this event is disabled. Stereotypes: atpSplitable Tags: atp.Splitkey=disabledInMode.contextMode DeclarationGroup, disabledInMode.targetMode InstanceRef implemented by: ModeInBswModule DescriptionInstanceRef
        self.disabledInModeIRefs: List[ModeInBswModuleDescriptionInstanceRef] = []

        # The entity which is started by the event.
        self.startsOnEventRef: Optional[RefType] = None

    def getContextLimitationRefs(self) -> List[RefType]:
        """
        The existence of this reference indicates that the usage of the event is limited to the context of the referred Bsw DistinguishedPartitions.

        Returns:
            The list of context limitation references
        """
        return self.contextLimitationRefs

    def addContextLimitationRef(self, value: RefType) -> BswEvent:
        """
        The existence of this reference indicates that the usage of the event is limited to the context of the referred Bsw DistinguishedPartitions.
        Only adds the value if it is not None.

        Args:
            value: The context limitation reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextLimitationRefs.append(value)
        return self

    def getDisabledInModeIRefs(self) -> List[ModeInBswModuleDescriptionInstanceRef]:
        """
        The modes, in which this event is disabled. Stereotypes: atpSplitable Tags: atp.Splitkey=disabledInMode.contextMode DeclarationGroup, disabledInMode.targetMode InstanceRef implemented by: ModeInBswModule DescriptionInstanceRef

        Returns:
            The list of disabled-in-mode instance references
        """
        return self.disabledInModeIRefs

    def addDisabledInModeIRef(self, value: ModeInBswModuleDescriptionInstanceRef) -> BswEvent:
        """
        The modes, in which this event is disabled. Stereotypes: atpSplitable Tags: atp.Splitkey=disabledInMode.contextMode DeclarationGroup, disabledInMode.targetMode InstanceRef implemented by: ModeInBswModule DescriptionInstanceRef
        Only adds the value if it is not None.

        Args:
            value: The disabled-in-mode instance reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.disabledInModeIRefs.append(value)
        return self

    def getStartsOnEventRef(self) -> Optional[RefType]:
        """
        The entity which is started by the event.

        Returns:
            The start-on-event reference
        """
        return self.startsOnEventRef

    def setStartsOnEventRef(self, value: Optional[RefType]) -> BswEvent:
        """
        The entity which is started by the event.
        Only sets the value if it is not None.

        Args:
            value: The start-on-event reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.startsOnEventRef = value
        return self


class BswInterruptEvent(BswEvent):
    """
    This meta-class represents an event triggered by an interrupt.
    """

    # BswInterruptEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.24, p.88
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswOperationInvokedEvent(BswEvent):
    """
    Represents an event that is triggered when a BSW operation is invoked.
    This event occurs when a client calls a BSW service function.
    """

    # BswOperationInvokedEvent method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getEntryRef                  [x] impl  [x] docstring  [ ] test
    # [x] setEntryRef                  [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswOperationInvokedEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Reference to the entry that was invoked to trigger this event
        self.entryRef: RefType = None

    def getEntryRef(self):
        """
        Gets the reference to the entry that was invoked to trigger this event.

        Returns:
            Reference to the invoked entry
        """
        return self.entryRef

    def setEntryRef(self, value):
        """
        Sets the reference to the entry that was invoked to trigger this event.
        Only sets the value if it is not None.

        Args:
            value: The entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.entryRef = value
        return self


class BswScheduleEvent(BswEvent, ABC):
    """
    BswEvent that is able to start a BswSchedulabeEntity.
    """

    # BswScheduleEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.23, p.88
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BSW schedule event with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        if type(self) is BswScheduleEvent:
            raise TypeError("BswScheduleEvent is an abstract class.")
        super().__init__(parent, short_name)


class BswAsynchronousServerCallReturnsEvent(BswScheduleEvent):
    """
    This is the "callback" event for asynchronous Client-Server-Communication
    via the BSW Scheduler which is thrown after completion of the asynchronous
    Client-Server call. Its eventSource specifies the call point to be used
    for retrieving the result.
    """

    # BswAsynchronousServerCallReturnsEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.36, p.98
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getEventSourceRef            [x] impl  [x] docstring  [x] test
    # [x] setEventSourceRef            [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswAsynchronousServerCallReturnsEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # The call point to be used for retrieving the result. The reference
        # in the role eventSource shall exist at the time when the
        # configuration of the BSW module is finished (constr_10288).
        self.eventSourceRef: Optional[RefType] = None

    def getEventSourceRef(self) -> Optional[RefType]:
        """
        Gets the call point to be used for retrieving the result of the
        asynchronous Client-Server call.

        Returns:
            The event source reference
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value: RefType) -> BswAsynchronousServerCallReturnsEvent:
        """
        Sets the call point to be used for retrieving the result.
        Only sets if value is not None.

        Args:
            value: The event source reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.eventSourceRef = value
        return self


class BswModeSwitchEvent(BswScheduleEvent):
    """
    A BswEvent resulting from a mode switch.
    """

    # BswModeSwitchEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.31, p.95
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getActivation                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setActivation                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModeIRefs                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addModeIRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Kind of activation w.r.t. to the referred mode.
        self.activation: Optional[ModeActivationKind] = None

        # Reference to one or two Modes that initiate the Mode Switch Event. InstanceRef implemented by: ModeInBswModule DescriptionInstanceRef
        self.modeIRefs: List[ModeInBswModuleDescriptionInstanceRef] = []

    def getActivation(self) -> Optional[ModeActivationKind]:
        """
        Kind of activation w.r.t. to the referred mode.

        Returns:
            The activation information
        """
        return self.activation

    def setActivation(self, value: ModeActivationKind) -> BswModeSwitchEvent:
        """
        Kind of activation w.r.t. to the referred mode.
        Only sets the value if it is not None.

        Args:
            value: The activation information to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.activation = value
        return self

    def getModeIRefs(self) -> List[ModeInBswModuleDescriptionInstanceRef]:
        """
        Reference to one or two Modes that initiate the Mode Switch Event. InstanceRef implemented by: ModeInBswModule DescriptionInstanceRef

        Returns:
            The list of mode instance references
        """
        return self.modeIRefs

    def addModeIRef(self, value: ModeInBswModuleDescriptionInstanceRef) -> BswModeSwitchEvent:
        """
        Reference to one or two Modes that initiate the Mode Switch Event. InstanceRef implemented by: ModeInBswModule DescriptionInstanceRef
        Only adds the value if it is not None.

        Args:
            value: The mode instance reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeIRefs.append(value)
        return self


class BswModeSwitchedAckEvent(BswScheduleEvent):
    """
    The event is raised after a switch of the referenced mode group has been
    acknowledged or an error occurs. The referenced mode group shall be
    provided by this module. The ModeDeclarationGroupPrototype used by this
    event shall be referred as BswModuleDescription.providedModeGroup by the
    same module (constr_4026).
    """

    # BswModeSwitchedAckEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.32, p.95
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getModeGroupRef              [x] impl  [x] docstring  [x] test
    # [x] setModeGroupRef              [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswModeSwitchedAckEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # A mode group provided by this module. The acknowledgement of a
        # switch of this group raises this event. The reference in the role
        # modeGroup shall exist at the time when the configuration of the BSW
        # module is finished (constr_10285).
        self.modeGroupRef: Optional[RefType] = None

    def getModeGroupRef(self) -> Optional[RefType]:
        """
        Gets the mode group provided by this module. The acknowledgement of a
        switch of this group raises this event.

        Returns:
            The mode group reference
        """
        return self.modeGroupRef

    def setModeGroupRef(self, value: RefType) -> BswModeSwitchedAckEvent:
        """
        Sets the mode group provided by this module. Only sets if value is
        not None.

        Args:
            value: The mode group reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeGroupRef = value
        return self


class BswModeManagerErrorEvent(BswScheduleEvent):
    """
    This represents the ability to react on errors occurring during mode
    handling. The event can be used to start a BswModuleEntity after an error
    has been announced by the mode manager. The ModeDeclarationGroupPrototype
    used by this event shall be referred as BswModuleDescription.providedModeGroup
    by the same module (constr_4081).
    """

    # BswModeManagerErrorEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.33, p.95
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getModeGroupRef              [x] impl  [x] docstring  [x] test
    # [x] setModeGroupRef              [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswModeManagerErrorEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # This represents the ModeDeclarationGroupPrototype for which the
        # error behavior of the mode manager applies. The reference in the
        # role modeGroup shall exist at the time when the configuration of
        # the BSW module is finished (constr_10286).
        self.modeGroupRef: Optional[RefType] = None

    def getModeGroupRef(self) -> Optional[RefType]:
        """
        Gets the ModeDeclarationGroupPrototype for which the error behavior
        of the mode manager applies.

        Returns:
            The mode group reference
        """
        return self.modeGroupRef

    def setModeGroupRef(self, value: RefType) -> BswModeManagerErrorEvent:
        """
        Sets the ModeDeclarationGroupPrototype for which the error behavior
        of the mode manager applies. Only sets if value is not None.

        Args:
            value: The mode group reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeGroupRef = value
        return self


class BswTimingEvent(BswScheduleEvent):
    """
    A recurring BswEvent driven by a time period. The event is triggered by
    the BswScheduler via the OS timer at the configured period.
    """

    # BswTimingEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.25, p.89
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getPeriod                    [x] impl  [x] docstring  [x] test
    # [x] setPeriod                    [x] impl  [x] docstring  [x] test
    # [x] periodMs                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswTimingEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Requirement for the time period (in seconds) by which this event is
        # triggered. Shall be greater than 0.
        self.period: Optional[TimeValue] = None

    def getPeriod(self) -> Optional[TimeValue]:
        """
        Gets the requirement for the time period (in seconds) by which this
        event is triggered.

        Returns:
            The period as a TimeValue, or None if not set
        """
        return self.period

    def setPeriod(self, value: TimeValue) -> BswTimingEvent:
        """
        Sets the time period (in seconds) by which this event is triggered.
        Only sets if value is not None.

        Args:
            value: The period to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.period = value
        return self

    @property
    def periodMs(self) -> Optional[int]:
        """
        Gets the period of this timing event in milliseconds.

        Returns:
            The period in milliseconds, or None if the period is not set
        """
        if self.period is not None:
            return int(self.period.value * 1000)
        return None


class BswDataReceivedEvent(BswScheduleEvent):
    """
    Represents an event that is triggered when data is received by a BSW module.
    This event handles data reception from other modules or communication interfaces.
    """

    # BswDataReceivedEvent method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getDataRef                   [x] impl  [x] docstring  [ ] test
    # [x] setDataRef                   [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswDataReceivedEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Reference to the data that was received to trigger this event
        self.dataRef: RefType = None

    def getDataRef(self):
        """
        Gets the reference to the data that was received to trigger this event.

        Returns:
            Reference to the received data
        """
        return self.dataRef

    def setDataRef(self, value):
        """
        Sets the reference to the data that was received to trigger this event.

        Args:
            value: The data reference to set

        Returns:
            self for method chaining
        """
        self.dataRef = value
        return self


class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    """
    Represents an event that is triggered by an internal trigger in a BSW module.
    This event occurs when a BSW module internally generates a trigger.
    """

    # BswInternalTriggerOccurredEvent method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getEventSourceRef            [x] impl  [x] docstring  [ ] test
    # [x] setEventSourceRef            [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswInternalTriggerOccurredEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Reference to the event source that triggered this event
        self.eventSourceRef: RefType = None

    def getEventSourceRef(self):
        """
        Gets the reference to the event source that triggered this event.

        Returns:
            Reference to the event source
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        """
        Sets the reference to the event source that triggered this event.

        Args:
            value: The event source reference to set

        Returns:
            self for method chaining
        """
        self.eventSourceRef = value
        return self


class BswModeSwitchAckRequest(ARObject):
    """
    Represents an acknowledgment request for a mode switch operation.
    This is used in BSW modules to handle mode switch acknowledgments.
    """

    # BswModeSwitchAckRequest method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getTimeout                   [x] impl  [x] docstring  [ ] test
    # [x] setTimeout                   [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the BswModeSwitchAckRequest.
        """
        super().__init__()

        # Timeout value for the mode switch acknowledgment
        self.timeout: Float = None

    def getTimeout(self):
        """
        Gets the timeout value for the mode switch acknowledgment.

        Returns:
            Float representing the timeout value
        """
        return self.timeout

    def setTimeout(self, value):
        """
        Sets the timeout value for the mode switch acknowledgment.

        Args:
            value: The timeout value to set

        Returns:
            self for method chaining
        """
        self.timeout = value
        return self


class BswModeSenderPolicy(ARObject, VariationPointCapable):
    """
    Specifies the details for the sending of a mode switch for the referred
    mode group.
    """

    # BswModeSenderPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.39, p.102
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getAckRequest                [x] impl  [x] docstring  [x] test
    # [x] setAckRequest                [x] impl  [x] docstring  [x] test
    # [x] getEnhancedModeApi           [x] impl  [x] docstring  [x] test
    # [x] setEnhancedModeApi           [x] impl  [x] docstring  [x] test
    # [x] getProvidedModeGroupRef      [x] impl  [x] docstring  [x] test
    # [x] setProvidedModeGroupRef      [x] impl  [x] docstring  [x] test
    # [x] getQueueLength               [x] impl  [x] docstring  [x] test
    # [x] setQueueLength               [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the BswModeSenderPolicy with default values.
        """
        super().__init__()

        # Request for acknowledgement.
        self.ackRequest: Optional[BswModeSwitchAckRequest] = None

        # This controls the creation of the enhanced mode API that returns
        # information about the previous mode and the next mode. If set to TRUE
        # the enhanced mode API is supposed to be generated. For more details
        # please refer to the SWS_RTE.
        self.enhancedModeApi: Optional[Boolean] = None

        # The provided mode group for which the policy is specified. The
        # reference in the role providedModeGroup shall exist at the time when
        # the configuration of the BSW module is finished (constr_10291).
        self.providedModeGroupRef: Optional[RefType] = None

        # Length of call queue on the sender side. The queue is implemented by
        # the RTE resp. BswScheduler. The value shall be greater or equal to 0.
        # Setting the value of queueLength to 0 implies non-queued
        # communication. The attribute queueLength shall exist at the time when
        # the configuration of the BSW module is finished (constr_10292).
        self.queueLength: Optional[PositiveInteger] = None

    def getAckRequest(self) -> Optional[BswModeSwitchAckRequest]:
        """
        Gets the request for acknowledgement.

        Returns:
            The acknowledgement request
        """
        return self.ackRequest

    def setAckRequest(self, value: BswModeSwitchAckRequest) -> BswModeSenderPolicy:
        """
        Sets the request for acknowledgement. Only sets if value is not None.

        Args:
            value: The acknowledgement request to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ackRequest = value
        return self

    def getEnhancedModeApi(self) -> Optional[Boolean]:
        """
        Gets the flag that controls the creation of the enhanced mode API that
        returns information about the previous mode and the next mode.

        Returns:
            The enhanced mode API flag
        """
        return self.enhancedModeApi

    def setEnhancedModeApi(self, value: Boolean) -> BswModeSenderPolicy:
        """
        Sets the flag that controls the creation of the enhanced mode API.
        Only sets if value is not None.

        Args:
            value: The enhanced mode API flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.enhancedModeApi = value
        return self

    def getProvidedModeGroupRef(self) -> Optional[RefType]:
        """
        Gets the provided mode group for which the policy is specified.

        Returns:
            The provided mode group reference
        """
        return self.providedModeGroupRef

    def setProvidedModeGroupRef(self, value: RefType) -> BswModeSenderPolicy:
        """
        Sets the provided mode group for which the policy is specified. Only
        sets if value is not None.

        Args:
            value: The provided mode group reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.providedModeGroupRef = value
        return self

    def getQueueLength(self) -> Optional[PositiveInteger]:
        """
        Gets the length of the call queue on the sender side.

        Returns:
            The queue length
        """
        return self.queueLength

    def setQueueLength(self, value: PositiveInteger) -> BswModeSenderPolicy:
        """
        Sets the length of the call queue on the sender side. Only sets if
        value is not None.

        Args:
            value: The queue length to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.queueLength = value
        return self


class BswModeReceiverPolicy(ARObject, VariationPointCapable):
    """
    Specifies the details for the reception of a mode switch for the referred mode group.
    """

    # BswModeReceiverPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.41, p.162
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getEnhancedModeApi           [x] impl  [x] docstring  [x] test
    # [x] setEnhancedModeApi           [x] impl  [x] docstring  [x] test
    # [x] getRequiredModeGroupRef      [x] impl  [x] docstring  [x] test
    # [x] setRequiredModeGroupRef      [x] impl  [x] docstring  [x] test
    # [x] getSupportsAsynchronousModeSwitch  [x] impl  [x] docstring  [x] test
    # [x] setSupportsAsynchronousModeSwitch  [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes BswModeReceiverPolicy with default values.
        """
        super().__init__()

        # Controls the creation of the enhanced mode API that returns information about the previous mode and the next mode.
        self.enhancedModeApi: Optional[Boolean] = None

        # The required mode group for which the policy is specified. The
        # reference in the role requiredModeGroup shall exist at the time when
        # the configuration of the BSW module is finished (constr_10294).
        self.requiredModeGroupRef: Optional[RefType] = None

        # Specifies whether the module can handle the reception of an asynchronous mode switch (true) or not (false).
        # This attribute shall exist at the time when the configuration of the BSW module is finished (constr_10295).
        self.supportsAsynchronousModeSwitch: Optional[Boolean] = None

    def getEnhancedModeApi(self) -> Optional[Boolean]:
        """
        Gets the enhanced mode API flag.
        Controls the creation of the enhanced mode API that returns information about the previous and next mode.
        Returns None if not set.
        """
        return self.enhancedModeApi

    def setEnhancedModeApi(self, value: Optional[Boolean]) -> BswModeReceiverPolicy:
        """
        Sets the enhanced mode API flag.
        Controls the creation of the enhanced mode API that returns information about the previous and next mode.
        Setting None is a no-op and preserves the existing value.
        Returns self for method chaining.
        """
        if value is not None:
            self.enhancedModeApi = value
        return self

    def getRequiredModeGroupRef(self) -> Optional[RefType]:
        """
        Gets the required mode group reference.
        Returns the reference to the mode group for which the policy is specified, or None if not set.
        """
        return self.requiredModeGroupRef

    def setRequiredModeGroupRef(self, value: Optional[RefType]) -> BswModeReceiverPolicy:
        """
        Sets the required mode group reference.
        The required mode group for which the policy is specified.
        Setting None is a no-op and preserves the existing value.
        Returns self for method chaining.
        """
        if value is not None:
            self.requiredModeGroupRef = value
        return self

    def getSupportsAsynchronousModeSwitch(self) -> Optional[Boolean]:
        """
        Gets the asynchronous mode switch support flag.
        Specifies whether the module can handle the reception of an asynchronous mode switch.
        Returns None if not set.
        """
        return self.supportsAsynchronousModeSwitch

    def setSupportsAsynchronousModeSwitch(self, value: Optional[Boolean]) -> BswModeReceiverPolicy:
        """
        Sets the asynchronous mode switch support flag.
        Specifies whether the module can handle the reception of an asynchronous mode switch (true) or not (false).
        Setting None is a no-op and preserves the existing value.
        Returns self for method chaining.
        """
        if value is not None:
            self.supportsAsynchronousModeSwitch = value
        return self


class BswBackgroundEvent(BswScheduleEvent):
    """
    A recurring BswEvent which is used to perform background activities. It is
    similar to a BswTimingEvent but has no fixed time period and is activated
    only with low priority.
    """

    # BswBackgroundEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.26, p.89
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswOsTaskExecutionEvent(BswScheduleEvent):
    """
    This BswEvent is supposed to execute BswSchedulableEntitys which have to
    react on the execution of specific OsTasks. Therefore, this event is
    unconditionally raised whenever the OsTask on which it is mapped is
    executed. The main use case for this event is scheduling of Runnables of
    Complex Drivers which have to react on task executions.
    Tags: atp.Status=draft
    """

    # BswOsTaskExecutionEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.27, p.89
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswExternalTriggerOccurredEvent(BswScheduleEvent):
    """
    Represents an event that is triggered by an external trigger in a BSW module.
    This event occurs when an external source generates a trigger.
    """

    # BswExternalTriggerOccurredEvent method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getTriggerRef                [x] impl  [x] docstring  [ ] test
    # [x] setTriggerRef                [x] impl  [x] docstring  [x] test

    def __init__(self, parent, short_name):
        """
        Initializes the BswExternalTriggerOccurredEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Reference to the external trigger that caused this event
        self.triggerRef: RefType = None

    def getTriggerRef(self):
        """
        Gets the reference to the external trigger that caused this event.

        Returns:
            Reference to the external trigger
        """
        return self.triggerRef

    def setTriggerRef(self, value):
        """
        Sets the reference to the external trigger that caused this event.
        Only sets the value if it is not None.

        Args:
            value: The trigger reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.triggerRef = value
        return self


class BswApiOptions(ARObject, ABC):
    """
    This meta-class represents the ability to define options for the definition of the signature of function prototypes.
    """

    # BswApiOptions method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate (BSW behavior policies), class BswApiOptions, AUTOSAR_00052.xsd line 9379 (XSD-only; no own table in repo corpus)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEnableTakeAddress         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEnableTakeAddress         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is BswApiOptions:
            raise TypeError("BswApiOptions is an abstract class.")

        super().__init__()

        # If set to true, the BSW Module is able to use the API reference for deriving a pointer to an object
        self.enableTakeAddress: Optional[Boolean] = None

    def getEnableTakeAddress(self) -> Optional[Boolean]:
        """
        If set to true, the BSW Module is able to use the API reference for deriving a pointer to an object
        """
        return self.enableTakeAddress

    def setEnableTakeAddress(self, value: Optional[Boolean]) -> BswApiOptions:
        """
        If set to true, the BSW Module is able to use the API reference for deriving a pointer to an object

        A None value is a no-op and does not overwrite an existing enableTakeAddress.
        """
        if value is not None:
            self.enableTakeAddress = value
        return self


class BswExclusiveAreaPolicy(BswApiOptions, VariationPointCapable):
    """
    The ExclusiveArea for which the BSW Scheduler uses this policy.
    """

    # BswExclusiveAreaPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.17, p.83
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getApiPrinciple              [x] impl  [x] docstring  [x] test
    # [x] setApiPrinciple              [x] impl  [x] docstring  [x] test
    # [x] getExclusiveAreaRef          [x] impl  [x] docstring  [x] test
    # [x] setExclusiveAreaRef          [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the BswExclusiveAreaPolicy with default values.
        """
        super().__init__()

        # Specifies for this ExclusiveArea if either one common set of Enter
        # and Exit APIs for the whole BSW module is requested from the SchM or
        # if the set of Enter and Exit APIs is expected per BswModuleEntity.
        # The default value is "common".
        self.apiPrinciple: Optional[ApiPrincipleEnum] = None

        # The ExclusiveArea for which the BSW Scheduler uses this policy.
        self.exclusiveAreaRef: Optional[RefType] = None

    def getApiPrinciple(self) -> Optional[ApiPrincipleEnum]:
        """
        Gets the API principle for this ExclusiveArea.

        Returns:
            The API principle (common or per-executable) for this policy
        """
        return self.apiPrinciple

    def setApiPrinciple(self, value: Optional[ApiPrincipleEnum]) -> BswExclusiveAreaPolicy:
        """
        Sets the API principle for this ExclusiveArea.
        Only sets the value if it is not None.

        Args:
            value: The API principle to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.apiPrinciple = value
        return self

    def getExclusiveAreaRef(self) -> Optional[RefType]:
        """
        Gets the ExclusiveArea for which the BSW Scheduler uses this policy.

        Returns:
            The referenced ExclusiveArea
        """
        return self.exclusiveAreaRef

    def setExclusiveAreaRef(self, value: Optional[RefType]) -> BswExclusiveAreaPolicy:
        """
        Sets the ExclusiveArea for which the BSW Scheduler uses this policy.
        Only sets the value if it is not None.

        Args:
            value: The ExclusiveArea reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.exclusiveAreaRef = value
        return self


class BswPerInstanceMemoryPolicy(BswApiOptions, VariationPointCapable):
    """
    The per-instance memory for which the BSW Scheduler using this policy.
    """

    # BswPerInstanceMemoryPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate (BSW behavior policies), class BswPerInstanceMemoryPolicy, AUTOSAR_00052.xsd line 12370 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArTypedPerInstanceMemoryRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArTypedPerInstanceMemoryRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The arTypedPerInstanceMemory for which the BSW Scheduler using this policy
        self.arTypedPerInstanceMemoryRef: Optional[RefType] = None

    def getArTypedPerInstanceMemoryRef(self) -> Optional[RefType]:
        """
        The arTypedPerInstanceMemory for which the BSW Scheduler using this policy
        """
        return self.arTypedPerInstanceMemoryRef

    def setArTypedPerInstanceMemoryRef(self, value: Optional[RefType]) -> BswPerInstanceMemoryPolicy:
        """
        The arTypedPerInstanceMemory for which the BSW Scheduler using this policy

        A None value is a no-op and does not overwrite an existing arTypedPerInstanceMemoryRef.
        """
        if value is not None:
            self.arTypedPerInstanceMemoryRef = value
        return self


class BswClientPolicy(BswApiOptions, VariationPointCapable):
    """
    The requiredClientServerEntry for which the BSW Scheduler using this policy.
    """

    # BswClientPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate (BSW behavior policies), class BswClientPolicy, AUTOSAR_00052.xsd line 9616 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRequiredClientServerEntryRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequiredClientServerEntryRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The requiredClientServerEntry for which the BSW Scheduler using this policy.
        self.requiredClientServerEntryRef: Optional[RefType] = None

    def getRequiredClientServerEntryRef(self) -> Optional[RefType]:
        """
        The requiredClientServerEntry for which the BSW Scheduler using this policy.
        """
        return self.requiredClientServerEntryRef

    def setRequiredClientServerEntryRef(self, value: Optional[RefType]) -> BswClientPolicy:
        """
        The requiredClientServerEntry for which the BSW Scheduler using this policy.

        A None value is a no-op and does not overwrite an existing requiredClientServerEntryRef.
        """
        if value is not None:
            self.requiredClientServerEntryRef = value
        return self


class BswInternalTriggeringPointPolicy(BswApiOptions, VariationPointCapable):
    """
    The internal triggering point for which the BSW Scheduler using this policy.
    """

    # BswInternalTriggeringPointPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate (BSW behavior policies), class BswInternalTriggeringPointPolicy, AUTOSAR_00052.xsd line 10850 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBswInternalTriggeringPointRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBswInternalTriggeringPointRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The BswInternalTriggeringPoint for which the BSW Scheduler using this policy.
        self.bswInternalTriggeringPointRef: Optional[RefType] = None

    def getBswInternalTriggeringPointRef(self) -> Optional[RefType]:
        """
        The BswInternalTriggeringPoint for which the BSW Scheduler using this policy.
        """
        return self.bswInternalTriggeringPointRef

    def setBswInternalTriggeringPointRef(self, value: Optional[RefType]) -> BswInternalTriggeringPointPolicy:
        """
        The BswInternalTriggeringPoint for which the BSW Scheduler using this policy.

        A None value is a no-op and does not overwrite an existing bswInternalTriggeringPointRef.
        """
        if value is not None:
            self.bswInternalTriggeringPointRef = value
        return self


class BswParameterPolicy(BswApiOptions, VariationPointCapable):
    """
    The perInstanceParameter for which the BSW Scheduler using this policy.
    """

    # BswParameterPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate (BSW behavior policies), class BswParameterPolicy, AUTOSAR_00052.xsd line 12325 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPerInstanceParameterRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPerInstanceParameterRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The perInstanceParameter for which the BSW Scheduler using this policy.
        self.perInstanceParameterRef: Optional[RefType] = None

    def getPerInstanceParameterRef(self) -> Optional[RefType]:
        """
        The perInstanceParameter for which the BSW Scheduler using this policy.
        """
        return self.perInstanceParameterRef

    def setPerInstanceParameterRef(self, value: Optional[RefType]) -> BswParameterPolicy:
        """
        The perInstanceParameter for which the BSW Scheduler using this policy.

        A None value is a no-op and does not overwrite an existing perInstanceParameterRef.
        """
        if value is not None:
            self.perInstanceParameterRef = value
        return self


class BswReleasedTriggerPolicy(BswApiOptions, VariationPointCapable):
    """
    The Trigger for which the BSW Scheduler using this policy.
    """

    # BswReleasedTriggerPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate (BSW behavior policies), class BswReleasedTriggerPolicy, AUTOSAR_00052.xsd line 12446 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getReleasedTriggerRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReleasedTriggerRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The Trigger for which the BSW Scheduler using this policy.
        self.releasedTriggerRef: Optional[RefType] = None

    def getReleasedTriggerRef(self) -> Optional[RefType]:
        """
        The Trigger for which the BSW Scheduler using this policy.
        """
        return self.releasedTriggerRef

    def setReleasedTriggerRef(self, value: Optional[RefType]) -> BswReleasedTriggerPolicy:
        """
        The Trigger for which the BSW Scheduler using this policy.

        A None value is a no-op and does not overwrite an existing releasedTriggerRef.
        """
        if value is not None:
            self.releasedTriggerRef = value
        return self


class BswDataSendPolicy(BswApiOptions, VariationPointCapable):
    """
    The data sent over the BSW Scheduler using this policy.
    """

    # BswDataSendPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate (BSW behavior policies), class BswDataSendPolicy, AUTOSAR_00052.xsd line 9802 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getProvidedDataRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProvidedDataRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProviedeDataRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11  (obsolete, PROVIEDE-DATA-REF)
    # [x] setProviedeDataRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11  (obsolete, PROVIEDE-DATA-REF)

    def __init__(self):
        super().__init__()

        # The data sent over the BSW Scheduler using this policy.
        self.providedDataRef: Optional[RefType] = None

        # The data sent over the BSW Scheduler using this policy. (obsolete, PROVIEDE-DATA-REF)
        self.proviedeDataRef: Optional[RefType] = None

    def getProvidedDataRef(self) -> Optional[RefType]:
        """
        The data sent over the BSW Scheduler using this policy.
        """
        return self.providedDataRef

    def setProvidedDataRef(self, value: Optional[RefType]) -> BswDataSendPolicy:
        """
        The data sent over the BSW Scheduler using this policy.

        A None value is a no-op and does not overwrite an existing providedDataRef.
        """
        if value is not None:
            self.providedDataRef = value
        return self

    def getProviedeDataRef(self) -> Optional[RefType]:
        """
        The data sent over the BSW Scheduler using this policy.
        """
        return self.proviedeDataRef

    def setProviedeDataRef(self, value: Optional[RefType]) -> BswDataSendPolicy:
        """
        The data sent over the BSW Scheduler using this policy.

        A None value is a no-op and does not overwrite an existing proviedeDataRef.
        """
        if value is not None:
            self.proviedeDataRef = value
        return self


class BswDataReceptionPolicy(BswApiOptions, VariationPointCapable, ABC):
    """
    Abstract base class for BSW data reception policies.
    Defines how BSW modules receive data.
    """

    # BswDataReceptionPolicy method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getReceivedDataRef           [x] impl  [x] docstring  [ ] test
    # [ ] setReceivedDataRef           [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the BSW data reception policy.
        Raises TypeError if this abstract class is instantiated directly.
        """
        if type(self) is BswDataReceptionPolicy:
            raise TypeError("BswDataReceptionPolicy is an abstract class.")

        super().__init__()

        # Reference to the data being received
        self.receivedDataRef: RefType = None

    def getReceivedDataRef(self):
        """
        Gets the reference to the data being received.

        Returns:
            Reference to the received data
        """
        return self.receivedDataRef

    def setReceivedDataRef(self, value):
        """
        Sets the reference to the data being received.
        Only sets the value if it is not None.

        Args:
            value: The received data reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.receivedDataRef = value
        return self


class BswQueuedDataReceptionPolicy(BswDataReceptionPolicy):
    """
    Represents a queued data reception policy in a BSW module.
    This policy handles data reception using a queue mechanism.
    """

    # BswQueuedDataReceptionPolicy method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getQueueLength               [x] impl  [x] docstring  [ ] test
    # [x] setQueueLength               [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the BswQueuedDataReceptionPolicy.
        """
        super().__init__()

        # Maximum queue length for received data
        self.queueLength: PositiveInteger = None

    def getQueueLength(self):
        """
        Gets the maximum queue length for received data.

        Returns:
            Positive integer representing the queue length
        """
        return self.queueLength

    def setQueueLength(self, value):
        """
        Sets the maximum queue length for received data.
        Only sets the value if it is not None.

        Args:
            value: The queue length value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.queueLength = value
        return self


class BswInternalTriggeringPoint(Identifiable, VariationPointCapable):
    """
    Represents an internal triggering point in a BSW module's internal behavior.
    This is used to define points from which triggers can be issued internally.
    """

    # BswInternalTriggeringPoint method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getSwImplPolicy              [x] impl  [x] docstring  [ ] test
    # [x] setSwImplPolicy              [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswInternalTriggeringPoint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this triggering point
            short_name: The unique short name of this triggering point
        """
        super().__init__(parent, short_name)

        # Software implementation policy for this triggering point
        self.swImplPolicy: SwImplPolicyEnum = None

    def getSwImplPolicy(self):
        """
        Gets the software implementation policy for this triggering point.

        Returns:
            SwImplPolicyEnum value
        """
        return self.swImplPolicy

    def setSwImplPolicy(self, value):
        """
        Sets the software implementation policy for this triggering point.
        Only sets the value if it is not None.

        Args:
            value: The SwImplPolicyEnum value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swImplPolicy = value
        return self


class RoleBasedBswModuleEntryAssignment(ARObject, VariationPointCapable):
    """
    This class specifies an assignment of a role to a particular BswModuleEntry (usually
    a configurable callback). With this assignment, the role of the callback is mapped to
    a specific ServiceNeeds element, so that a tool is able to create appropriate
    configuration values for the module that implements the AUTOSAR Service.
    """

    # RoleBasedBswModuleEntryAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.3, p.226
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getAssignedEntryRef          [x] impl  [x] docstring  [x] test
    # [x] setAssignedEntryRef          [x] impl  [x] docstring  [x] test
    # [x] getRole                      [x] impl  [x] docstring  [x] test
    # [x] setRole                      [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the RoleBasedBswModuleEntryAssignment with default values.
        """
        super().__init__()

        # The assigned entry. It should be an implementedEntry or expectedEntry of the
        # module or cluster of the ServiceNeeds. [constr_10258]: shall exist
        # when the configuration of the BSW module is finished.
        self.assignedEntryRef: Optional[RefType] = None

        # This is the role of the assigned BswModuleEntry in the given context. Required
        # because different kinds of callbacks may be associated with the same
        # ServiceNeeds (e.g. end-notification vs. error-notification). [constr_10259]:
        # shall exist when the configuration of the BSW module is finished.
        self.role: Optional[Identifier] = None

    def getAssignedEntryRef(self) -> Optional[RefType]:
        """
        Gets the reference to the assigned BswModuleEntry. It should be an
        implementedEntry or expectedEntry of the module or cluster that requires
        the ServiceNeeds. [constr_10258]: shall exist when the configuration of
        the BSW module is finished.

        Returns:
            RefType: The assigned entry reference
        """
        return self.assignedEntryRef

    def setAssignedEntryRef(self, value: Optional[RefType]) -> RoleBasedBswModuleEntryAssignment:
        """
        Sets the reference to the assigned BswModuleEntry. It should be an
        implementedEntry or expectedEntry of the module or cluster that requires
        the ServiceNeeds. [constr_10258]: the reference shall exist when the
        configuration of the BSW module is finished.
        A None value is a no-op and does not overwrite an existing assignedEntryRef.

        Args:
            value: The assigned entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.assignedEntryRef = value
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        Gets the role of the assigned BswModuleEntry in the given context. The value
        shall be the role name of a configurable function call (usually a callback)
        as standardized in the Software Specification of the related AUTOSAR Service.
        [constr_10259]: the attribute shall exist when the configuration of the BSW
        module is finished.

        Returns:
            Identifier: The role
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> RoleBasedBswModuleEntryAssignment:
        """
        Sets the role of the assigned BswModuleEntry in the given context. The value
        shall be the role name of a configurable function call (usually a callback)
        as standardized in the Software Specification of the related AUTOSAR Service.
        [constr_10259]: the attribute shall exist when the configuration of the BSW
        module is finished. [TPS_BSWMDT_04113]: the value cannot be arbitrarily set
        but shall equal the shortName of the applicable BswModuleEntry taken from the
        standardized AUTOSAR BswModuleEntry model.
        A None value is a no-op and does not overwrite an existing role.

        Args:
            value: The role to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.role = value
        return self


class BswServiceDependency(ServiceDependency, VariationPointCapable):
    """
    Specialization of ServiceDependency in the context of an BswInternalBehavior. It
    allows to associate BswModuleEntries and data defined for a BSW module or cluster
    to a given ServiceNeeds element.
    """

    # BswServiceDependency method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.2, p.225
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getAssignedData              [x] impl  [x] docstring  [x] test
    # [x] addAssignedData              [x] impl  [x] docstring  [x] test
    # [x] getAssignedEntryRole         [x] impl  [x] docstring  [x] test
    # [x] addAssignedEntryRole         [x] impl  [x] docstring  [x] test
    # [x] getIdent                     [x] impl  [x] docstring  [x] test
    # [x] setIdent                     [x] impl  [x] docstring  [x] test
    # [x] getServiceNeeds              [x] impl  [x] docstring  [x] test
    # [x] setServiceNeeds              [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the BswServiceDependency with default values.
        """
        super().__init__()

        # Defines the role of an associated data object (owned by this module or
        # cluster) in the context of the ServiceNeeds element.
        self.assignedData: List[RoleBasedDataAssignment] = []

        # Defines the role of an associated BswModuleEntry in the context of the
        # ServiceNeeds element.
        self.assignedEntryRole: List[RoleBasedBswModuleEntryAssignment] = []

        # This adds the ability to become referrable to BswServiceDependency.
        self.ident: Optional[BswServiceDependencyIdent] = None

        # The associated ServiceNeeds. [constr_10257]: shall exist when the
        # configuration of the BSW module is finished.
        self.serviceNeeds: Optional[ServiceNeeds] = None

    def getAssignedData(self) -> List[RoleBasedDataAssignment]:
        """
        Gets the list of associated data objects (owned by this module or cluster)
        assigned a role in the context of the ServiceNeeds element.

        Returns:
            List of RoleBasedDataAssignment instances
        """
        return self.assignedData

    def addAssignedData(self, value: Optional[RoleBasedDataAssignment]) -> BswServiceDependency:
        """
        Adds a role-based data assignment defining the role of an associated data
        object (owned by this module or cluster) in the context of the ServiceNeeds
        element.
        A None value is a no-op and is not appended to the list.

        Args:
            value: The RoleBasedDataAssignment instance to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.assignedData.append(value)
        return self

    def getAssignedEntryRole(self) -> List[RoleBasedBswModuleEntryAssignment]:
        """
        Gets the list of associated BswModuleEntry role assignments in the context
        of the ServiceNeeds element.

        Returns:
            List of RoleBasedBswModuleEntryAssignment instances
        """
        return self.assignedEntryRole

    def addAssignedEntryRole(self, value: Optional[RoleBasedBswModuleEntryAssignment]) -> BswServiceDependency:
        """
        Adds a role-based BSW module entry assignment defining the role of an
        associated BswModuleEntry in the context of the ServiceNeeds element.
        A None value is a no-op and is not appended to the list.

        Args:
            value: The RoleBasedBswModuleEntryAssignment instance to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.assignedEntryRole.append(value)
        return self

    def getIdent(self) -> Optional[BswServiceDependencyIdent]:
        """
        Gets the identification caption that adds the ability to become referrable
        to this BswServiceDependency.

        Returns:
            BswServiceDependencyIdent: The identification caption
        """
        return self.ident

    def setIdent(self, value: Optional[BswServiceDependencyIdent]) -> BswServiceDependency:
        """
        Sets the identification caption that adds the ability to become referrable
        to this BswServiceDependency.
        A None value is a no-op and does not overwrite an existing ident.

        Args:
            value: The BswServiceDependencyIdent to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ident = value
        return self

    def getServiceNeeds(self) -> Optional[ServiceNeeds]:
        """
        Gets the associated ServiceNeeds. [constr_10257]: shall exist when the
        configuration of the BSW module is finished.

        Returns:
            ServiceNeeds: The associated service needs instance
        """
        return self.serviceNeeds

    def setServiceNeeds(self, value: Optional[ServiceNeeds]) -> BswServiceDependency:
        """
        Sets the associated ServiceNeeds. [constr_10257]: shall exist when the
        configuration of the BSW module is finished.
        A None value is a no-op and does not overwrite an existing serviceNeeds.

        Args:
            value: The ServiceNeeds instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.serviceNeeds = value
        return self


class BswInternalBehavior(InternalBehavior):
    """
    Specifies the behavior of a BSW module or a BSW cluster w.r.t. the code entities visible by the BSW Scheduler. It is possible to have several different BswInternalBehaviors referring to the same BswModuleDescription.
    """

    # BswInternalBehavior method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.2, p.68 (page-split pp.67-68)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArTypedPerInstanceMemories          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArTypedPerInstanceMemories          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addArTypedPerInstanceMemory            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswPerInstanceMemoryPolicies        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBswPerInstanceMemoryPolicies        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addBswPerInstanceMemoryPolicy          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addClientPolicy                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getClientPolicies                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setClientPolicies                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDistinguishedPartitions             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDistinguishedPartition           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setDistinguishedPartitions             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getExclusiveAreaPolicies               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setExclusiveAreaPolicies               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addExclusiveAreaPolicy                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInternalTriggeringPoints            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createBswInternalTriggeringPoint       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInternalTriggeringPointPolicies     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInternalTriggeringPointPolicies     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addInternalTriggeringPointPolicy       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeReceiverPolicies                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setModeReceiverPolicies                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addModeReceiverPolicy                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setModeSenderPolicies                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getParameterPolicies                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setParameterPolicies                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addParameterPolicy                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPerInstanceParameters               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPerInstanceParameters               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addPerInstanceParameter                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReceptionPolicies                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addReceptionPolicy                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReleasedTriggerPolicies             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReleasedTriggerPolicies             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addReleasedTriggerPolicy               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSchedulerNamePrefixes               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSchedulerNamePrefix              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] setSchedulerNamePrefixes               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSendPolicies                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSendPolicies                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addSendPolicy                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceDependencies                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceDependencies                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addServiceDependency                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTriggerDirectImplementations        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTriggerDirectImplementations        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addTriggerDirectImplementation         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVariationPointProxies               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVariationPointProxies               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addVariationPointProxy                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addModeSenderPolicy                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeSenderPolicies                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createBswCalledEntity                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswCalledEntities                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswSchedulableEntity             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswSchedulableEntities              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswInterruptEntity               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswInterruptEntities                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBswModuleEntities                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createBswModeSwitchEvent               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswModeSwitchEvents                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswTimingEvent                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswTimingEvents                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswDataReceivedEvent             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswDataReceivedEvents               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswInternalTriggerOccurredEvent  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswInternalTriggerOccurredEvents    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswExternalTriggerOccurredEvent  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswOperationInvokedEvents           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswOperationInvokedEvent         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswExternalTriggerOccurredEvents    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswBackgroundEvent               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createBswInterruptEvent                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createBswOsTaskExecutionEvent          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswBackgroundEvents                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswModeManagerErrorEvent         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswModeManagerErrorEvents           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswModeSwitchedAckEvent          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswModeSwitchedAckEvents            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswAsynchronousServerCallReturnsEvent [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswAsynchronousServerCallReturnsEvents [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBswEvents                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addIncludedModeDeclarationGroupSet     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIncludedModeDeclarationGroupSets    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addIncludedDataTypeSet                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIncludedDataTypeSets                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines an AUTOSAR typed memory-block that needs to be available for each instance of the Basic Software Module. The aggregation of arTypedPerInstanceMemory is subject to variability with the purpose to support variability in the Basic Software Module's implementations. Typically different algorithms in the implementation are requiring different number of memory objects.
        self.arTypedPerInstanceMemories: List[VariableDataPrototype] = []

        # Policy for a arTypedPerInstanceMemory The policy selects the options of the Schedule Manager API generation.
        self.bswPerInstanceMemoryPolicies: List[BswPerInstanceMemoryPolicy] = []

        # Policy for a requiredClientServerEntry. The policy selects the options of the Schedule Manager API generation.
        self.clientPolicies: List[BswClientPolicy] = []

        # Indicates an abstract partition context in which the enclosing BswModuleEntity can be executed.
        self.distinguishedPartitions: List[BswDistinguishedPartition] = []

        # A code entity for which the behavior is described
        self.entities: List[BswModuleEntity] = []

        # An event required by this module behavior.
        self.events: List[BswEvent] = []

        # Policy for an ExclusiveArea in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation.
        self.exclusiveAreaPolicies: List[BswExclusiveAreaPolicy] = []

        # The includedDataTypeSet is used by a basic software module for its implementation.
        self.includedDataTypeSets: List[IncludedDataTypeSet] = []

        # This aggregation represents the included ModeDeclarationGroups
        self.includedModeDeclarationGroupSets: List[IncludedModeDeclarationGroupSet] = []

        # An internal triggering point.
        self.internalTriggeringPoints: List[BswInternalTriggeringPoint] = []

        # Policy for an internalTriggeringPoint in this BswInternalBehavior.. The policy selects the options of the Schedule Manager API generation.
        self.internalTriggeringPointPolicies: List[BswInternalTriggeringPointPolicy] = []

        # Implementation policy for the reception of mode switches.
        self.modeReceiverPolicies: List[BswModeReceiverPolicy] = []

        # Implementation policy for providing a mode group.
        self.modeSenderPolicies: List[BswModeSenderPolicy] = []

        # Policy for a perInstanceParameter in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation.
        self.parameterPolicies: List[BswParameterPolicy] = []

        # Describes a read only memory object containing characteristic value(s) needed by this BswInternalBehavior. The role name perInstanceParameter is chosen in analogy to the similar role in the context of SwcInternalBehavior. In contrast to constantMemory, this object is not allocated locally by the module's code, but by the BSW Scheduler and it is accessed from the BSW module via the BSW Scheduler API. The main use case is the support of software emulation of calibration data. The aggregation is subject to variability with the purpose to support implementation variants.
        self.perInstanceParameters: List[ParameterDataPrototype] = []

        # Data reception policy for inter-partition and/or inter-core communication.
        self.receptionPolicies: List[BswDataReceptionPolicy] = []

        # Policy for a releasedTrigger. The policy selects the options of the Schedule Manager API generation.
        self.releasedTriggerPolicies: List[BswReleasedTriggerPolicy] = []

        # Optional definition of one or more prefixes to be used for the BswScheduler.
        self.schedulerNamePrefixes: List[BswSchedulerNamePrefix] = []

        # Policy for a providedData. The policy selects the options of the Schedule Manager API generation.
        self.sendPolicies: List[BswDataSendPolicy] = []

        # Defines the requirements on AUTOSAR Services for a particular item. The aggregation is subject to variability with the purpose to support the conditional existence of ServiceNeeds. The aggregation is splitable in order to support that ServiceNeeds might be provided in later development steps.
        self.serviceDependencies: List[BswServiceDependency] = []

        # Specifies a trigger to be directly implemented via OS calls.
        self.triggerDirectImplementations: List[BswTriggerDirectImplementation] = []

        # Proxy of a variation points in the C/C++ implementation.
        self.variationPointProxies: List[VariationPointProxy] = []

    def getArTypedPerInstanceMemories(self):
        """
        Defines an AUTOSAR typed memory-block that needs to be available for each instance of the Basic Software Module. The aggregation of arTypedPerInstanceMemory is subject to variability with the purpose to support variability in the Basic Software Module's implementations. Typically different algorithms in the implementation are requiring different number of memory objects.
        """
        return self.arTypedPerInstanceMemories

    def setArTypedPerInstanceMemories(self, value):
        """
        Defines an AUTOSAR typed memory-block that needs to be available for each instance of the Basic Software Module. The aggregation of arTypedPerInstanceMemory is subject to variability with the purpose to support variability in the Basic Software Module's implementations. Typically different algorithms in the implementation are requiring different number of memory objects.

        A None value is a no-op and does not overwrite an existing arTypedPerInstanceMemories.
        """
        if value is not None:
            self.arTypedPerInstanceMemories = value
        return self

    def addArTypedPerInstanceMemory(self, value: Optional[VariableDataPrototype]) -> BswInternalBehavior:
        """
        Defines an AUTOSAR typed memory-block that needs to be available for each instance of the Basic Software Module. The aggregation of arTypedPerInstanceMemory is subject to variability with the purpose to support variability in the Basic Software Module's implementations. Typically different algorithms in the implementation are requiring different number of memory objects.

        A None value is a no-op and does not append to the existing arTypedPerInstanceMemories.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arTypedPerInstanceMemories.append(value)
        return self

    def getBswPerInstanceMemoryPolicies(self):
        """
        Policy for a arTypedPerInstanceMemory The policy selects the options of the Schedule Manager API generation.
        """
        return self.bswPerInstanceMemoryPolicies

    def setBswPerInstanceMemoryPolicies(self, value):
        """
        Policy for a arTypedPerInstanceMemory The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not overwrite an existing bswPerInstanceMemoryPolicies.
        """
        if value is not None:
            self.bswPerInstanceMemoryPolicies = value
        return self

    def addBswPerInstanceMemoryPolicy(self, value: Optional[BswPerInstanceMemoryPolicy]) -> BswInternalBehavior:
        """
        Policy for a arTypedPerInstanceMemory The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not append to the existing bswPerInstanceMemoryPolicies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswPerInstanceMemoryPolicies.append(value)
        return self

    def addClientPolicy(self, value: Optional[BswClientPolicy]) -> BswInternalBehavior:
        """
        Policy for a requiredClientServerEntry. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not append to the existing clientPolicies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.clientPolicies.append(value)
        return self

    def getClientPolicies(self):
        """
        Policy for a requiredClientServerEntry. The policy selects the options of the Schedule Manager API generation.
        """
        return self.clientPolicies

    def setClientPolicies(self, value):
        """
        Policy for a requiredClientServerEntry. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not overwrite an existing clientPolicies.
        """
        if value is not None:
            self.clientPolicies = value
        return self

    def getDistinguishedPartitions(self):
        """
        Indicates an abstract partition context in which the enclosing BswModuleEntity can be executed.
        """
        return self.distinguishedPartitions

    def createDistinguishedPartition(self, short_name: str) -> BswDistinguishedPartition:
        """
        Indicates an abstract partition context in which the enclosing BswModuleEntity can be executed.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswDistinguishedPartition):
            partition = BswDistinguishedPartition(self, short_name)
            self.addElement(partition)
            self.distinguishedPartitions.append(partition)
        return self.getElement(short_name, BswDistinguishedPartition)

    def setDistinguishedPartitions(self, value):
        """
        Indicates an abstract partition context in which the enclosing BswModuleEntity can be executed.

        A None value is a no-op and does not overwrite an existing distinguishedPartitions.
        """
        if value is not None:
            self.distinguishedPartitions = value
        return self

    def getExclusiveAreaPolicies(self):
        """
        Policy for an ExclusiveArea in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation.
        """
        return self.exclusiveAreaPolicies

    def setExclusiveAreaPolicies(self, value):
        """
        Policy for an ExclusiveArea in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not overwrite an existing exclusiveAreaPolicies.
        """
        if value is not None:
            self.exclusiveAreaPolicies = value
        return self

    def addExclusiveAreaPolicy(self, value: Optional[BswExclusiveAreaPolicy]) -> BswInternalBehavior:
        """
        Policy for an ExclusiveArea in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not append to the existing exclusiveAreaPolicies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.exclusiveAreaPolicies.append(value)
        return self

    def getInternalTriggeringPoints(self):
        """
        An internal triggering point.
        """
        return self.internalTriggeringPoints

    def createBswInternalTriggeringPoint(self, short_name: str) -> BswInternalTriggeringPoint:
        """
        An internal triggering point.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswInternalTriggeringPoint):
            entity = BswInternalTriggeringPoint(self, short_name)
            self.addElement(entity)
            self.internalTriggeringPoints.append(entity)
        return self.getElement(short_name, BswInternalTriggeringPoint)

    def getInternalTriggeringPointPolicies(self):
        """
        Policy for an internalTriggeringPoint in this BswInternalBehavior.. The policy selects the options of the Schedule Manager API generation.
        """
        return self.internalTriggeringPointPolicies

    def setInternalTriggeringPointPolicies(self, value):
        """
        Policy for an internalTriggeringPoint in this BswInternalBehavior.. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not overwrite an existing internalTriggeringPointPolicies.
        """
        if value is not None:
            self.internalTriggeringPointPolicies = value
        return self

    def addInternalTriggeringPointPolicy(self, value: Optional[BswInternalTriggeringPointPolicy]) -> BswInternalBehavior:
        """
        Policy for an internalTriggeringPoint in this BswInternalBehavior.. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not append to the existing internalTriggeringPointPolicies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.internalTriggeringPointPolicies.append(value)
        return self

    def getModeReceiverPolicies(self):
        """
        Implementation policy for the reception of mode switches.
        """
        return self.modeReceiverPolicies

    def setModeReceiverPolicies(self, value):
        """
        Implementation policy for the reception of mode switches.

        A None value is a no-op and does not overwrite an existing modeReceiverPolicies.
        """
        if value is not None:
            self.modeReceiverPolicies = value
        return self

    def addModeReceiverPolicy(self, value: Optional[BswModeReceiverPolicy]) -> BswInternalBehavior:
        """
        Implementation policy for the reception of mode switches.

        A None value is a no-op and does not append to the existing modeReceiverPolicies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeReceiverPolicies.append(value)
        return self

    def setModeSenderPolicies(self, value):
        """
        Implementation policy for providing a mode group.

        A None value is a no-op and does not overwrite an existing modeSenderPolicies.
        """
        if value is not None:
            self.modeSenderPolicies = value
        return self

    def getParameterPolicies(self):
        """
        Policy for a perInstanceParameter in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation.
        """
        return self.parameterPolicies

    def setParameterPolicies(self, value):
        """
        Policy for a perInstanceParameter in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not overwrite an existing parameterPolicies.
        """
        if value is not None:
            self.parameterPolicies = value
        return self

    def addParameterPolicy(self, value: Optional[BswParameterPolicy]) -> BswInternalBehavior:
        """
        Policy for a perInstanceParameter in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not append to the existing parameterPolicies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.parameterPolicies.append(value)
        return self

    def getPerInstanceParameters(self):
        """
        Describes a read only memory object containing characteristic value(s) needed by this BswInternalBehavior. The role name perInstanceParameter is chosen in analogy to the similar role in the context of SwcInternalBehavior. In contrast to constantMemory, this object is not allocated locally by the module's code, but by the BSW Scheduler and it is accessed from the BSW module via the BSW Scheduler API. The main use case is the support of software emulation of calibration data. The aggregation is subject to variability with the purpose to support implementation variants.
        """
        return self.perInstanceParameters

    def setPerInstanceParameters(self, value):
        """
        Describes a read only memory object containing characteristic value(s) needed by this BswInternalBehavior. The role name perInstanceParameter is chosen in analogy to the similar role in the context of SwcInternalBehavior. In contrast to constantMemory, this object is not allocated locally by the module's code, but by the BSW Scheduler and it is accessed from the BSW module via the BSW Scheduler API. The main use case is the support of software emulation of calibration data. The aggregation is subject to variability with the purpose to support implementation variants.

        A None value is a no-op and does not overwrite an existing perInstanceParameters.
        """
        if value is not None:
            self.perInstanceParameters = value
        return self

    def addPerInstanceParameter(self, value: Optional[ParameterDataPrototype]) -> BswInternalBehavior:
        """
        Describes a read only memory object containing characteristic value(s) needed by this BswInternalBehavior. The role name perInstanceParameter is chosen in analogy to the similar role in the context of SwcInternalBehavior. In contrast to constantMemory, this object is not allocated locally by the module's code, but by the BSW Scheduler and it is accessed from the BSW module via the BSW Scheduler API. The main use case is the support of software emulation of calibration data. The aggregation is subject to variability with the purpose to support implementation variants.

        A None value is a no-op and does not append to the existing perInstanceParameters.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.perInstanceParameters.append(value)
        return self

    def getReceptionPolicies(self):
        """
        Data reception policy for inter-partition and/or inter-core communication.
        """
        return self.receptionPolicies

    def addReceptionPolicy(self, value):
        """
        Data reception policy for inter-partition and/or inter-core communication.

        A None value is a no-op and does not append to the existing receptionPolicies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.receptionPolicies.append(value)
        return self

    def getReleasedTriggerPolicies(self):
        """
        Policy for a releasedTrigger. The policy selects the options of the Schedule Manager API generation.
        """
        return self.releasedTriggerPolicies

    def setReleasedTriggerPolicies(self, value):
        """
        Policy for a releasedTrigger. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not overwrite an existing releasedTriggerPolicies.
        """
        if value is not None:
            self.releasedTriggerPolicies = value
        return self

    def addReleasedTriggerPolicy(self, value: Optional[BswReleasedTriggerPolicy]) -> BswInternalBehavior:
        """
        Policy for a releasedTrigger. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not append to the existing releasedTriggerPolicies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.releasedTriggerPolicies.append(value)
        return self

    def getSchedulerNamePrefixes(self) -> List[BswSchedulerNamePrefix]:
        """
        Optional definition of one or more prefixes to be used for the BswScheduler.
        """
        return self.schedulerNamePrefixes

    def createSchedulerNamePrefix(self, short_name: str) -> BswSchedulerNamePrefix:
        """
        Optional definition of one or more prefixes to be used for the BswScheduler.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswSchedulerNamePrefix):
            prefix = BswSchedulerNamePrefix(self, short_name)
            self.addElement(prefix)
            self.schedulerNamePrefixes.append(prefix)
        return self.getElement(short_name, BswSchedulerNamePrefix)

    def setSchedulerNamePrefixes(self, value):
        """
        Optional definition of one or more prefixes to be used for the BswScheduler.

        A None value is a no-op and does not overwrite an existing schedulerNamePrefixes.
        """
        if value is not None:
            self.schedulerNamePrefixes = value
        return self

    def getSendPolicies(self):
        """
        Policy for a providedData. The policy selects the options of the Schedule Manager API generation.
        """
        return self.sendPolicies

    def setSendPolicies(self, value):
        """
        Policy for a providedData. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not overwrite an existing sendPolicies.
        """
        if value is not None:
            self.sendPolicies = value
        return self

    def addSendPolicy(self, value: Optional[BswDataSendPolicy]) -> BswInternalBehavior:
        """
        Policy for a providedData. The policy selects the options of the Schedule Manager API generation.

        A None value is a no-op and does not append to the existing sendPolicies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sendPolicies.append(value)
        return self

    def getServiceDependencies(self):
        """
        Defines the requirements on AUTOSAR Services for a particular item. The aggregation is subject to variability with the purpose to support the conditional existence of ServiceNeeds. The aggregation is splitable in order to support that ServiceNeeds might be provided in later development steps.
        """
        return self.serviceDependencies

    def setServiceDependencies(self, value):
        """
        Defines the requirements on AUTOSAR Services for a particular item. The aggregation is subject to variability with the purpose to support the conditional existence of ServiceNeeds. The aggregation is splitable in order to support that ServiceNeeds might be provided in later development steps.

        A None value is a no-op and does not overwrite an existing serviceDependencies.
        """
        if value is not None:
            self.serviceDependencies = value
        return self

    def addServiceDependency(self, dependency: BswServiceDependency):
        """
        Defines the requirements on AUTOSAR Services for a particular item. The aggregation is subject to variability with the purpose to support the conditional existence of ServiceNeeds. The aggregation is splitable in order to support that ServiceNeeds might be provided in later development steps.

        A None value is a no-op and does not append to the existing serviceDependencies.

        Returns:
            self for method chaining
        """
        self.serviceDependencies.append(dependency)
        return self

    def getTriggerDirectImplementations(self):
        """
        Specifies a trigger to be directly implemented via OS calls.
        """
        return self.triggerDirectImplementations

    def setTriggerDirectImplementations(self, value):
        """
        Specifies a trigger to be directly implemented via OS calls.

        A None value is a no-op and does not overwrite an existing triggerDirectImplementations.
        """
        if value is not None:
            self.triggerDirectImplementations = value
        return self

    def addTriggerDirectImplementation(self, value: Optional[BswTriggerDirectImplementation]) -> BswInternalBehavior:
        """
        Specifies a trigger to be directly implemented via OS calls.

        A None value is a no-op and does not append to the existing triggerDirectImplementations.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.triggerDirectImplementations.append(value)
        return self

    def getVariationPointProxies(self):
        """
        Proxy of a variation points in the C/C++ implementation.
        """
        return self.variationPointProxies

    def setVariationPointProxies(self, value):
        """
        Proxy of a variation points in the C/C++ implementation.

        A None value is a no-op and does not overwrite an existing variationPointProxies.
        """
        if value is not None:
            self.variationPointProxies = value
        return self

    def addVariationPointProxy(self, value: Optional[VariationPointProxy]) -> BswInternalBehavior:
        """
        Proxy of a variation points in the C/C++ implementation.

        A None value is a no-op and does not append to the existing variationPointProxies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.variationPointProxies.append(value)
        return self

    def addModeSenderPolicy(self, policy: BswModeSenderPolicy):
        """
        Implementation policy for providing a mode group.

        A None value is a no-op and does not append to the existing modeSenderPolicies.

        Returns:
            self for method chaining
        """
        self.modeSenderPolicies.append(policy)

    def getModeSenderPolicies(self) -> List[BswModeSenderPolicy]:
        """
        Implementation policy for providing a mode group.
        """
        return self.modeSenderPolicies

    def createBswCalledEntity(self, short_name: str) -> BswCalledEntity:
        """
        A code entity for which the behavior is described

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswCalledEntity):
            entity = BswCalledEntity(self, short_name)
            self.addElement(entity)
            self.entities.append(entity)
        return self.getElement(short_name, BswCalledEntity)

    def getBswCalledEntities(self) -> List[BswCalledEntity]:
        """
        A code entity for which the behavior is described
        """
        return list(filter(lambda a: isinstance(a, BswCalledEntity), self.entities))

    def createBswSchedulableEntity(self, short_name: str) -> BswSchedulableEntity:
        """
        A code entity for which the behavior is described

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswSchedulableEntity):
            entity = BswSchedulableEntity(self, short_name)
            self.addElement(entity)
            self.entities.append(entity)
        return self.getElement(short_name, BswSchedulableEntity)

    def getBswSchedulableEntities(self) -> List[BswSchedulableEntity]:
        """
        A code entity for which the behavior is described
        """
        return list(filter(lambda a: isinstance(a, BswSchedulableEntity), self.entities))

    def createBswInterruptEntity(self, short_name: str) -> BswInterruptEntity:
        """
        A code entity for which the behavior is described

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswInterruptEntity):
            entity = BswInterruptEntity(self, short_name)
            self.addElement(entity)
            self.entities.append(entity)
        return self.getElement(short_name, BswInterruptEntity)

    def getBswInterruptEntities(self) -> List[BswInterruptEntity]:
        """
        A code entity for which the behavior is described
        """
        return list(filter(lambda a: isinstance(a, BswInterruptEntity), self.entities))

    def getBswModuleEntities(self) -> List[BswModuleEntity]:
        """
        A code entity for which the behavior is described
        """
        return list(filter(lambda a: isinstance(a, BswModuleEntity), self.entities))

    def createBswModeSwitchEvent(self, short_name: str) -> BswModeSwitchEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswModeSwitchEvent):
            event = BswModeSwitchEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswModeSwitchEvent)

    def getBswModeSwitchEvents(self) -> List[BswModeSwitchEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswModeSwitchEvent), self.events))

    def createBswTimingEvent(self, short_name: str) -> BswTimingEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswTimingEvent):
            event = BswTimingEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswTimingEvent)

    def getBswTimingEvents(self) -> List[BswTimingEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswTimingEvent), self.events))

    def createBswDataReceivedEvent(self, short_name: str) -> BswDataReceivedEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswDataReceivedEvent):
            event = BswDataReceivedEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswDataReceivedEvent)

    def getBswDataReceivedEvents(self) -> List[BswDataReceivedEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswDataReceivedEvent), self.events))

    def createBswInternalTriggerOccurredEvent(self, short_name: str) -> BswInternalTriggerOccurredEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswInternalTriggerOccurredEvent):
            event = BswInternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswInternalTriggerOccurredEvent)

    def getBswInternalTriggerOccurredEvents(self) -> List[BswInternalTriggerOccurredEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswInternalTriggerOccurredEvent), self.events))

    def createBswExternalTriggerOccurredEvent(self, short_name: str) -> BswExternalTriggerOccurredEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswExternalTriggerOccurredEvent):
            event = BswExternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswExternalTriggerOccurredEvent)

    def getBswOperationInvokedEvents(self) -> List[BswOperationInvokedEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswOperationInvokedEvent), self.events))

    def createBswOperationInvokedEvent(self, short_name: str) -> BswOperationInvokedEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswOperationInvokedEvent):
            event = BswOperationInvokedEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswOperationInvokedEvent)

    def getBswExternalTriggerOccurredEvents(self) -> List[BswExternalTriggerOccurredEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswExternalTriggerOccurredEvent), self.events))

    def createBswBackgroundEvent(self, short_name: str) -> BswBackgroundEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswBackgroundEvent):
            event = BswBackgroundEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswBackgroundEvent)

    def createBswInterruptEvent(self, short_name: str) -> BswEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """

        if not self.IsElementExists(short_name, BswInterruptEvent):
            event = BswInterruptEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswInterruptEvent)

    def createBswOsTaskExecutionEvent(self, short_name: str) -> BswOsTaskExecutionEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswOsTaskExecutionEvent):
            event = BswOsTaskExecutionEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswOsTaskExecutionEvent)

    def getBswBackgroundEvents(self) -> List[BswBackgroundEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswBackgroundEvent), self.events))

    def createBswModeManagerErrorEvent(self, short_name: str) -> BswModeManagerErrorEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswModeManagerErrorEvent):
            event = BswModeManagerErrorEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswModeManagerErrorEvent)

    def getBswModeManagerErrorEvents(self) -> List[BswModeManagerErrorEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswModeManagerErrorEvent), self.events))

    def createBswModeSwitchedAckEvent(self, short_name: str) -> BswModeSwitchedAckEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswModeSwitchedAckEvent):
            event = BswModeSwitchedAckEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswModeSwitchedAckEvent)

    def getBswModeSwitchedAckEvents(self) -> List[BswModeSwitchedAckEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswModeSwitchedAckEvent), self.events))

    def createBswAsynchronousServerCallReturnsEvent(self, short_name: str) -> BswAsynchronousServerCallReturnsEvent:
        """
        An event required by this module behavior.

        Args:
            short_name: The short name of the created element

        Returns:
            The created element
        """
        if not self.IsElementExists(short_name, BswAsynchronousServerCallReturnsEvent):
            event = BswAsynchronousServerCallReturnsEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name, BswAsynchronousServerCallReturnsEvent)

    def getBswAsynchronousServerCallReturnsEvents(self) -> List[BswAsynchronousServerCallReturnsEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswAsynchronousServerCallReturnsEvent), self.events))

    def getBswEvents(self) -> List[BswEvent]:
        """
        An event required by this module behavior.
        """
        return list(filter(lambda a: isinstance(a, BswEvent), self.events))

    def addIncludedModeDeclarationGroupSet(self, group_set: IncludedModeDeclarationGroupSet):
        """
        This aggregation represents the included ModeDeclarationGroups

        A None value is a no-op and does not append to the existing includedModeDeclarationGroupSets.

        Returns:
            self for method chaining
        """
        self.includedModeDeclarationGroupSets.append(group_set)

    def getIncludedModeDeclarationGroupSets(self) -> List[IncludedModeDeclarationGroupSet]:
        """
        This aggregation represents the included ModeDeclarationGroups
        """
        return self.includedModeDeclarationGroupSets

    def addIncludedDataTypeSet(self, type_set: IncludedDataTypeSet):
        """
        The includedDataTypeSet is used by a basic software module for its implementation.

        A None value is a no-op and does not append to the existing includedDataTypeSets.

        Returns:
            self for method chaining
        """
        self.includedDataTypeSets.append(type_set)

    def getIncludedDataTypeSets(self) -> List[IncludedDataTypeSet]:
        """
        The includedDataTypeSet is used by a basic software module for its implementation.
        """
        return self.includedDataTypeSets


class BswTriggerDirectImplementation(ARObject, VariationPointCapable):
    """
    Specifies a released trigger to be directly implemented via OS calls, for example in a Complex Driver module.
    Constraints: constr_10290 (masteredTrigger reference shall exist) and constr_4105 (only one of task or cat2Isr).
    """

    # BswTriggerDirectImplementation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.38, p.99
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getCat2Isr                   [x] impl  [x] docstring  [x] test
    # [x] setCat2Isr                   [x] impl  [x] docstring  [x] test
    # [x] getMasteredTriggerRef        [x] impl  [x] docstring  [x] test
    # [x] setMasteredTriggerRef        [x] impl  [x] docstring  [x] test
    # [x] getTask                      [x] impl  [x] docstring  [x] test
    # [x] setTask                      [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initialize BswTriggerDirectImplementation with default values.
        """
        super().__init__()

        # The name of the OS category 2 ISR, which is controlled by the referred trigger.
        # This means, that the module manages the category 2 ISR (e.g. according hardware
        # initialization and enabling of ISR). Instead of calling an RTE / SchM API to
        # raise the appropriate events in components or modules receiving the trigger,
        # this ISR directly schedules the triggered ExecutableEntitys. The ISR name is
        # required by the integrator to map the Bsw Events and RTEEvents to this ISR.
        # Constraint: constr_4105 (only one of task or cat2Isr).
        self.cat2Isr: Optional[Identifier] = None

        # The trigger which is directly mastered by this module. There may be several
        # different BswTriggerDirect Implementations mastering the same Trigger. This may
        # be required e.g. due to memory partitioning.
        # Constraint: constr_10290 (masteredTrigger reference shall exist).
        self.masteredTriggerRef: Optional[RefType] = None

        # The name of the OS task, which is controlled by the referred trigger. This means,
        # that the module uses the trigger condition to directly activate an OS task instead
        # of calling an API of the BswScheduler. The task name is required by the RTE
        # generator resp. BswScheduler to raise the appropriate events in components or
        # modules receiving the trigger.
        # Constraint: constr_4105 (only one of task or cat2Isr).
        self.task: Optional[Identifier] = None

    def getCat2Isr(self) -> Optional[Identifier]:
        """
        Gets the name of the OS category 2 ISR controlled by the referred trigger.
        Returns the ISR name or None if not set.
        """
        return self.cat2Isr

    def setCat2Isr(self, value: Optional[Identifier]) -> BswTriggerDirectImplementation:
        """
        Sets the name of the OS category 2 ISR. Only sets if value is not None.
        Returns self for method chaining.
        """
        if value is not None:
            self.cat2Isr = value
        return self

    def getMasteredTriggerRef(self) -> Optional[RefType]:
        """
        Gets the reference to the trigger which is directly mastered by this module.
        Returns the trigger reference or None if not set.
        """
        return self.masteredTriggerRef

    def setMasteredTriggerRef(self, value: Optional[RefType]) -> BswTriggerDirectImplementation:
        """
        Sets the trigger reference. Only sets if value is not None.
        Returns self for method chaining.
        """
        if value is not None:
            self.masteredTriggerRef = value
        return self

    def getTask(self) -> Optional[Identifier]:
        """
        Gets the name of the OS task controlled by the referred trigger.
        Returns the task name or None if not set.
        """
        return self.task

    def setTask(self, value: Optional[Identifier]) -> BswTriggerDirectImplementation:
        """
        Sets the name of the OS task. Only sets if value is not None.
        Returns self for method chaining.
        """
        if value is not None:
            self.task = value
        return self
