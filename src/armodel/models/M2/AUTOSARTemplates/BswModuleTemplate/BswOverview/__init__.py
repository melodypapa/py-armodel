"""
This module contains classes for representing AUTOSAR Basic Software (BSW) module overview information.
BSW module overview describes the high-level structure and interfaces of BSW modules,
including their dependencies, behaviors, and data exchanges with other modules.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import SwComponentDocumentation
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleClientServerEntry, BswModuleDependency
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalBehavior
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from typing import List, Optional, cast


class BswModuleDescription(AtpStructureElement):
    """
    Root element for the description of a single BSW module or BSW cluster. In case it describes a BSW module, the short name of this element equals the name of the BSW module. Tags: atp.recommendedPackage=BswModuleDescriptions
    """

    # BswModuleDescription method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 3.1, p.29
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBswModuleDependencies          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createBswModuleDependency         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addBswModuleDependency            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBswModuleDocumentation         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBswModuleDocumentation         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getExpectedEntryRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setExpectedEntryRefs              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addExpectedEntryRef               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getImplementedEntryRefs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addImplementedEntryRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInternalBehaviors              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInternalBehaviors              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBswInternalBehavior         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModuleId                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setModuleId                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProvidedClientServerEntries    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createProvidedClientServerEntry   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProvidedDatas                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createProvidedData                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProvidedModeGroups             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createProvidedModeGroup           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReleasedTriggers               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createReleasedTrigger             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequiredClientServerEntries    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createRequiredClientServerEntry   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequiredDatas                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createRequiredData                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequiredModeGroups             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createRequiredModeGroup           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequiredTriggers               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createRequiredTrigger             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Describes the dependency to another BSW module. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=bswModuleDependency.shortName, bsw ModuleDependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=20
        self.bswModuleDependencies: List[BswModuleDependency] = []

        # This adds a documentation to the BSW module. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=bswModuleDocumentation, bswModule Documentation.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=6
        self.bswModuleDocumentation: Optional[SwComponentDocumentation] = None

        # Indicates an entry which is required by this module. Replacement of outgoingCallback / requiredEntry. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=expectedEntry.bswModuleEntry, expected Entry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.expectedEntryRefs: List[RefType] = []

        # Specifies an entry provided by this module which can be called by other modules. This includes "main" functions, interrupt routines, and callbacks. Replacement of providedEntry / expectedCallback. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=implementedEntry.bswModuleEntry, implementedEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.implementedEntryRefs: List[RefType] = []

        # The various BswInternalBehaviors associated with a BswModuleDescription can be distributed over several physical files. Therefore the aggregation is <<atpSplitable>>. Stereotypes: atpSplitable Tags: atp.Splitkey=internalBehavior.shortName
        self.internalBehaviors: List[BswInternalBehavior] = []

        # Refers to the BSW Module Identifier defined by the AUTOSAR standard. For non-standardized modules, a proprietary identifier can be optionally chosen.
        self.moduleId: Optional[PositiveInteger] = None

        # Specifies that this module provides a client server entry which can be called from another partition or core. This entry is declared locally to this context and will be connected to the requiredClientServerEntry of another or the same module via the configuration of the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedClientServerEntry.shortName, providedClientServerEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.providedClientServerEntries: List[BswModuleClientServerEntry] = []

        # Specifies a data prototype provided by this module in order to be read from another partition or core. The providedData is declared locally to this context and will be connected to the requiredData of another or the same module via the configuration of the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedData.shortName, provided Data.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=55
        self.providedDatas: List[VariableDataPrototype] = []

        # A set of modes which is owned and provided by this module or cluster. It can be connected to the requiredModeGroups of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with modes provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedModeGroup.shortName, provided ModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=25
        self.providedModeGroups: List[ModeDeclarationGroupPrototype] = []

        # A Trigger released by this module or cluster. It can be connected to the requiredTriggers of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with Triggers provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=releasedTrigger.shortName, released Trigger.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.releasedTriggers: List[Trigger] = []

        # Specifies that this module requires a client server entry which can be implemented on another partition or core. This entry is declared locally to this context and will be connected to the providedClientServerEntry of another or the same module via the configuration of the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredClientServerEntry.shortName, requiredClientServerEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=50
        self.requiredClientServerEntries: List[BswModuleClientServerEntry] = []

        # Specifies a data prototype required by this module in order to be provided from another partition or core. The requiredData is declared locally to this context and will be connected to the providedData of another or the same module via the configuration of the BswScheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredData.shortName, required Data.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=60
        self.requiredDatas: List[VariableDataPrototype] = []

        # Specifies that this module or cluster depends on a certain mode group. The requiredModeGroup is local to this context and will be connected to the providedModeGroup of another module or cluster via the configuration of the BswScheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredModeGroup.shortName, required ModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=30
        self.requiredModeGroups: List[ModeDeclarationGroupPrototype] = []

        # Specifies that this module or cluster reacts upon an external trigger. This requiredTrigger is declared locally to this context and will be connected to the providedTrigger of another module or cluster via the configuration of the BswScheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredTrigger.shortName, required Trigger.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=40
        self.requiredTriggers: List[Trigger] = []

    def getBswModuleDependencies(self) -> List[BswModuleDependency]:
        """
        Describes the dependency to another BSW module. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=bswModuleDependency.shortName, bsw ModuleDependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=20
        """
        return self.bswModuleDependencies

    def createBswModuleDependency(self, short_name: str) -> BswModuleDependency:
        """
        Describes the dependency to another BSW module. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=bswModuleDependency.shortName, bsw ModuleDependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=20

        Args:
            short_name: The short name for the new BSW module dependency

        Returns:
            The created BswModuleDependency instance
        """
        if not self.IsReferrableElementExists(short_name, BswModuleDependency):
            dependency = BswModuleDependency(self, short_name)
            self.addReferrableElement(dependency)
            self.bswModuleDependencies.append(dependency)
        return cast(BswModuleDependency, self.getReferrableElement(short_name, BswModuleDependency))

    def addBswModuleDependency(self, value: BswModuleDependency) -> "BswModuleDescription":
        """
        Describes the dependency to another BSW module. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=bswModuleDependency.shortName, bsw ModuleDependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=20
        A None value is a no-op and does not add to bswModuleDependencies.
        """
        if value is not None:
            self.bswModuleDependencies.append(value)
        return self

    def getBswModuleDocumentation(self) -> Optional[SwComponentDocumentation]:
        """
        This adds a documentation to the BSW module. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=bswModuleDocumentation, bswModule Documentation.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=6
        """
        return self.bswModuleDocumentation

    def setBswModuleDocumentation(self, value: SwComponentDocumentation) -> "BswModuleDescription":
        """
        This adds a documentation to the BSW module. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=bswModuleDocumentation, bswModule Documentation.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=6
        A None value is a no-op and does not overwrite an existing bswModuleDocumentation.
        """
        if value is not None:
            self.bswModuleDocumentation = value
        return self

    def getExpectedEntryRefs(self) -> List[RefType]:
        """
        Indicates an entry which is required by this module. Replacement of outgoingCallback / requiredEntry. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=expectedEntry.bswModuleEntry, expected Entry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.expectedEntryRefs

    def setExpectedEntryRefs(self, value: List[RefType]) -> "BswModuleDescription":
        """
        Indicates an entry which is required by this module. Replacement of outgoingCallback / requiredEntry. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=expectedEntry.bswModuleEntry, expected Entry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        A None value is a no-op and does not overwrite an existing expectedEntryRefs.
        """
        if value is not None:
            self.expectedEntryRefs = value
        return self

    def addExpectedEntryRef(self, value: RefType) -> "BswModuleDescription":
        """
        Indicates an entry which is required by this module. Replacement of outgoingCallback / requiredEntry. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=expectedEntry.bswModuleEntry, expected Entry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        A None value is a no-op and does not add to expectedEntryRefs.
        """
        if value is not None:
            self.expectedEntryRefs.append(value)
        return self

    def getImplementedEntryRefs(self) -> List[RefType]:
        """
        Specifies an entry provided by this module which can be called by other modules. This includes "main" functions, interrupt routines, and callbacks. Replacement of providedEntry / expectedCallback. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=implementedEntry.bswModuleEntry, implementedEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.implementedEntryRefs

    def addImplementedEntryRef(self, value: RefType) -> "BswModuleDescription":
        """
        Specifies an entry provided by this module which can be called by other modules. This includes "main" functions, interrupt routines, and callbacks. Replacement of providedEntry / expectedCallback. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=implementedEntry.bswModuleEntry, implementedEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        A None value is a no-op and does not add to implementedEntryRefs.
        """
        if value is not None:
            self.implementedEntryRefs.append(value)
        return self

    def getInternalBehaviors(self) -> List[BswInternalBehavior]:
        """
        The various BswInternalBehaviors associated with a BswModuleDescription can be distributed over several physical files. Therefore the aggregation is <<atpSplitable>>. Stereotypes: atpSplitable Tags: atp.Splitkey=internalBehavior.shortName
        """
        return self.internalBehaviors

    def setInternalBehaviors(self, value: List[BswInternalBehavior]) -> "BswModuleDescription":
        """
        The various BswInternalBehaviors associated with a BswModuleDescription can be distributed over several physical files. Therefore the aggregation is <<atpSplitable>>. Stereotypes: atpSplitable Tags: atp.Splitkey=internalBehavior.shortName
        A None value is a no-op and does not overwrite an existing internalBehaviors.
        """
        if value is not None:
            self.internalBehaviors = value
        return self

    def createBswInternalBehavior(self, short_name: str) -> BswInternalBehavior:
        """
        The various BswInternalBehaviors associated with a BswModuleDescription can be distributed over several physical files. Therefore the aggregation is <<atpSplitable>>. Stereotypes: atpSplitable Tags: atp.Splitkey=internalBehavior.shortName

        Args:
            short_name: The short name for the new internal behavior

        Returns:
            The created BswInternalBehavior instance
        """
        if not self.IsReferrableElementExists(short_name, BswInternalBehavior):
            behavior = BswInternalBehavior(self, short_name)
            self.addReferrableElement(behavior)
            self.internalBehaviors.append(behavior)
        return cast(BswInternalBehavior, self.getReferrableElement(short_name, BswInternalBehavior))

    def getModuleId(self) -> Optional[PositiveInteger]:
        """
        Refers to the BSW Module Identifier defined by the AUTOSAR standard. For non-standardized modules, a proprietary identifier can be optionally chosen.
        """
        return self.moduleId

    def setModuleId(self, value: PositiveInteger) -> "BswModuleDescription":
        """
        Refers to the BSW Module Identifier defined by the AUTOSAR standard. For non-standardized modules, a proprietary identifier can be optionally chosen.
        A None value is a no-op and does not overwrite an existing moduleId.
        """
        if value is not None:
            self.moduleId = value
        return self

    def getProvidedClientServerEntries(self) -> List[BswModuleClientServerEntry]:
        """
        Specifies that this module provides a client server entry which can be called from another partition or core. This entry is declared locally to this context and will be connected to the requiredClientServerEntry of another or the same module via the configuration of the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedClientServerEntry.shortName, providedClientServerEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.providedClientServerEntries

    def createProvidedClientServerEntry(self, short_name: str) -> BswModuleClientServerEntry:
        """
        Specifies that this module provides a client server entry which can be called from another partition or core. This entry is declared locally to this context and will be connected to the requiredClientServerEntry of another or the same module via the configuration of the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedClientServerEntry.shortName, providedClientServerEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            short_name: The short name for the new provided client-server entry

        Returns:
            The created BswModuleClientServerEntry instance
        """
        if not self.IsReferrableElementExists(short_name, BswModuleClientServerEntry):
            entry = BswModuleClientServerEntry(self, short_name)
            self.addReferrableElement(entry)
            self.providedClientServerEntries.append(entry)
        return cast(BswModuleClientServerEntry, self.getReferrableElement(short_name, BswModuleClientServerEntry))

    def getProvidedDatas(self) -> List[VariableDataPrototype]:
        """
        Specifies a data prototype provided by this module in order to be read from another partition or core. The providedData is declared locally to this context and will be connected to the requiredData of another or the same module via the configuration of the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedData.shortName, provided Data.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=55
        """
        return self.providedDatas

    def createProvidedData(self, short_name: str) -> VariableDataPrototype:
        """
        Specifies a data prototype provided by this module in order to be read from another partition or core. The providedData is declared locally to this context and will be connected to the requiredData of another or the same module via the configuration of the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedData.shortName, provided Data.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=55

        Args:
            short_name: The short name for the new provided data prototype

        Returns:
            The created VariableDataPrototype instance
        """
        if not self.IsReferrableElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.providedDatas.append(prototype)
        return cast(VariableDataPrototype, self.getReferrableElement(short_name, VariableDataPrototype))

    def getProvidedModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        """
        A set of modes which is owned and provided by this module or cluster. It can be connected to the requiredModeGroups of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with modes provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedModeGroup.shortName, provided ModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=25
        """
        return self.providedModeGroups

    def createProvidedModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        """
        A set of modes which is owned and provided by this module or cluster. It can be connected to the requiredModeGroups of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with modes provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=providedModeGroup.shortName, provided ModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=25

        Args:
            short_name: The short name for the new provided mode group

        Returns:
            The created ModeDeclarationGroupPrototype instance
        """
        if not self.IsReferrableElementExists(short_name, ModeDeclarationGroupPrototype):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.providedModeGroups.append(prototype)
        return cast(ModeDeclarationGroupPrototype, self.getReferrableElement(short_name, ModeDeclarationGroupPrototype))

    def getReleasedTriggers(self) -> List[Trigger]:
        """
        A Trigger released by this module or cluster. It can be connected to the requiredTriggers of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with Triggers provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=releasedTrigger.shortName, released Trigger.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.releasedTriggers

    def createReleasedTrigger(self, short_name: str) -> Trigger:
        """
        A Trigger released by this module or cluster. It can be connected to the requiredTriggers of other modules or clusters via the configuration of the BswScheduler. It can also be synchronized with Triggers provided via ports by an associated ServiceSwComponentType, EcuAbstractionSwComponentType or ComplexDeviceDriverSwComponentType. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=releasedTrigger.shortName, released Trigger.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            short_name: The short name for the new released trigger

        Returns:
            The created Trigger instance
        """
        if not self.IsReferrableElementExists(short_name, Trigger):
            trigger = Trigger(self, short_name)
            self.addReferrableElement(trigger)
            self.releasedTriggers.append(trigger)
        return cast(Trigger, self.getReferrableElement(short_name, Trigger))

    def getRequiredClientServerEntries(self) -> List[BswModuleClientServerEntry]:
        """
        Specifies that this module requires a client server entry which can be implemented on another partition or core. This entry is declared locally to this context and will be connected to the providedClientServerEntry of another or the same module via the configuration of the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredClientServerEntry.shortName, requiredClientServerEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=50
        """
        return self.requiredClientServerEntries

    def createRequiredClientServerEntry(self, short_name: str) -> BswModuleClientServerEntry:
        """
        Specifies that this module requires a client server entry which can be implemented on another partition or core. This entry is declared locally to this context and will be connected to the providedClientServerEntry of another or the same module via the configuration of the BSW Scheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredClientServerEntry.shortName, requiredClientServerEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=50

        Args:
            short_name: The short name for the new required client-server entry

        Returns:
            The created BswModuleClientServerEntry instance
        """
        if not self.IsReferrableElementExists(short_name, BswModuleClientServerEntry):
            entry = BswModuleClientServerEntry(self, short_name)
            self.addReferrableElement(entry)
            self.requiredClientServerEntries.append(entry)
        return cast(BswModuleClientServerEntry, self.getReferrableElement(short_name, BswModuleClientServerEntry))

    def getRequiredDatas(self) -> List[VariableDataPrototype]:
        """
        Specifies a data prototype required by this module in order to be provided from another partition or core. The requiredData is declared locally to this context and will be connected to the providedData of another or the same module via the configuration of the BswScheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredData.shortName, required Data.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=60
        """
        return self.requiredDatas

    def createRequiredData(self, short_name: str) -> VariableDataPrototype:
        """
        Specifies a data prototype required by this module in order to be provided from another partition or core. The requiredData is declared locally to this context and will be connected to the providedData of another or the same module via the configuration of the BswScheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredData.shortName, required Data.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=60

        Args:
            short_name: The short name for the new required data prototype

        Returns:
            The created VariableDataPrototype instance
        """
        if not self.IsReferrableElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.requiredDatas.append(prototype)
        return cast(VariableDataPrototype, self.getReferrableElement(short_name, VariableDataPrototype))

    def getRequiredModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        """
        Specifies that this module or cluster depends on a certain mode group. The requiredModeGroup is local to this context and will be connected to the providedModeGroup of another module or cluster via the configuration of the BswScheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredModeGroup.shortName, required ModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=30
        """
        return self.requiredModeGroups

    def createRequiredModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        """
        Specifies that this module or cluster depends on a certain mode group. The requiredModeGroup is local to this context and will be connected to the providedModeGroup of another module or cluster via the configuration of the BswScheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredModeGroup.shortName, required ModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=30

        Args:
            short_name: The short name for the new required mode group

        Returns:
            The created ModeDeclarationGroupPrototype instance
        """
        if not self.IsReferrableElementExists(short_name, ModeDeclarationGroupPrototype):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.requiredModeGroups.append(prototype)
        return cast(ModeDeclarationGroupPrototype, self.getReferrableElement(short_name, ModeDeclarationGroupPrototype))

    def getRequiredTriggers(self) -> List[Trigger]:
        """
        Specifies that this module or cluster reacts upon an external trigger. This requiredTrigger is declared locally to this context and will be connected to the providedTrigger of another module or cluster via the configuration of the BswScheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredTrigger.shortName, required Trigger.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=40
        """
        return self.requiredTriggers

    def createRequiredTrigger(self, short_name: str) -> Trigger:
        """
        Specifies that this module or cluster reacts upon an external trigger. This requiredTrigger is declared locally to this context and will be connected to the providedTrigger of another module or cluster via the configuration of the BswScheduler. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=requiredTrigger.shortName, required Trigger.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=40

        Args:
            short_name: The short name for the new required trigger

        Returns:
            The created Trigger instance
        """
        if not self.IsReferrableElementExists(short_name, Trigger):
            trigger = Trigger(self, short_name)
            self.addReferrableElement(trigger)
            self.requiredTriggers.append(trigger)
        return cast(Trigger, self.getReferrableElement(short_name, Trigger))
