from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import SwComponentDocumentation
from ....M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleClientServerEntry, BswModuleDependency
from ....M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalBehavior
from ....M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype
from ....M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from ....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from typing import List


class BswModuleDescription(ARElement):
    '''
        Root element for the description of a single BSW module or BSW cluster. In case it
        describes a BSW module, the short name of this element equals the name of the
        BSW module.

        **attributes**:
         module_id              : MODULE-ID  
         implemented_entry_refs : PROVIDED-ENTRYS
    '''
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bswModuleDependencies = []                         # type: List[BswModuleDependency]
        self.bswModuleDocumentation = None                      # type: SwComponentDocumentation
        self.expectedEntryRefs = []                             # type: List[RefType]
        self.implementedEntryRefs = []                          # type: List[RefType]
        self.internalBehaviors = []                             # type: List[BswInternalBehavior]
        self.moduleId = None                                    # type: PositiveInteger
        self.providedClientServerEntries = []                   # type: List[BswModuleClientServerEntry]
        self.providedDatas = []                                 # type: List[VariableDataPrototype]
        self.providedModeGroups = []                            # type: List[ModeDeclarationGroupPrototype]
        self.releasedTriggers = []                              # type: List[Trigger]
        self.requiredClientServerEntries = []                   # type: List[BswModuleClientServerEntry]
        self.requiredDatas = []                                 # type: List[VariableDataPrototype]
        self.requiredModeGroups = []                            # type: List[ModeDeclarationGroupPrototype]
        self.requiredTriggers = []                              # typeL List[Trigger]

    def getBswModuleDependencies(self):
        return self.bswModuleDependencies

    def setBswModuleDependencies(self, value):
        if value is not None:
            self.bswModuleDependencies = value
        return self

    def getBswModuleDocumentation(self):
        return self.bswModuleDocumentation

    def setBswModuleDocumentation(self, value):
        if value is not None:
            self.bswModuleDocumentation = value
        return self

    def getExpectedEntryRefs(self):
        return self.expectedEntryRefs

    def setExpectedEntryRefs(self, value):
        if value is not None:
            self.expectedEntryRefs = value
        return self

    def getImplementedEntryRefs(self):
        return self.implementedEntryRefs

    def addImplementedEntryRef(self, value):
        if value is not None:
            self.implementedEntryRefs.append(value)
        return self

    def getInternalBehaviors(self):
        return self.internalBehaviors

    def setInternalBehaviors(self, value):
        if value is not None:
            self.internalBehaviors = value
        return self
    
    def createBswInternalBehavior(self, short_name: str) -> BswInternalBehavior:
        '''
            Create the INTERNAL-BEHAVIORS tag
        '''
        if (not self.IsElementExists(short_name)):
            behavior = BswInternalBehavior(self, short_name)
            self.addElement(behavior)
            self.internalBehaviors.append(behavior)
        return self.getElement(short_name)

    def getModuleId(self):
        return self.moduleId

    def setModuleId(self, value):
        if value is not None:
            self.moduleId = value
        return self

    def getProvidedClientServerEntries(self):
        return self.providedClientServerEntries

    def createProvidedClientServerEntry(self, short_name: str) -> BswModuleClientServerEntry:
        if (not self.IsElementExists(short_name)):
            entry = BswModuleClientServerEntry(self, short_name)
            self.addElement(entry)
            self.providedClientServerEntries.append(entry)
        return self.getElement(short_name)

    def getProvidedDatas(self):
        return self.providedDatas

    def createProvidedData(self, short_name: str) -> VariableDataPrototype:
        if (not self.IsElementExists(short_name)):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.providedDatas.append(prototype)
        return self.getElement(short_name)

    def getProvidedModeGroups(self):
        return self.providedModeGroups
    
    def createProvidedModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        if (not self.IsElementExists(short_name)):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addElement(prototype)
            self.providedModeGroups.append(prototype)
        return self.getElement(short_name)

    def getReleasedTriggers(self):
        return self.releasedTriggers

    def createReleasedTrigger(self, short_name: str) -> Trigger:
        if (not self.IsElementExists(short_name)):
            trigger = Trigger(self, short_name)
            self.addElement(trigger)
            self.releasedTriggers.append(trigger)
        return self.getElement(short_name)

    def getRequiredClientServerEntries(self):
        return self.requiredClientServerEntries

    def createRequiredClientServerEntry(self, short_name: str) -> BswModuleClientServerEntry:
        if (not self.IsElementExists(short_name)):
            entry = BswModuleClientServerEntry(self, short_name)
            self.addElement(entry)
            self.requiredClientServerEntries.append(entry)
        return self.getElement(short_name)

    def getRequiredDatas(self):
        return self.requiredDatas

    def createRequiredData(self, short_name: str) -> VariableDataPrototype:
        if (not self.IsElementExists(short_name)):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.requiredDatas.append(prototype)
        return self.getElement(short_name)

    def getRequiredModeGroups(self):
        return self.requiredModeGroups

    def createRequiredModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        if (not self.IsElementExists(short_name)):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.addElement(prototype)
            self.requiredModeGroups.append(prototype)
        return self.getElement(short_name)

    def getRequiredTriggers(self):
        return self.requiredTriggers

    def createRequiredTrigger(self, short_name: str) -> Trigger:
        if (not self.IsElementExists(short_name)):
            trigger = Trigger(self, short_name)
            self.addElement(trigger)
            self.requiredTriggers.append(trigger)
        return self.getElement(short_name)

    