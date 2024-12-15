from ....M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalBehavior
from ....M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARPositiveInteger, RefType
from typing import Dict, List

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

        # MODULE-ID
        self.moduleId = None                           # type: ARPositiveInteger

        # PROVIDED-ENTRYS
        self.implementedEntryRefs = []                 # type: List[RefType]

        self.providedModeGroups   = {}                  # type: Dict[str, ModeDeclarationGroupPrototype]
        self.requiredModeGroups   = {}                  # type: Dict[str, ModeDeclarationGroupPrototype] 
    
    def getModuleId(self):
        return self.moduleId

    def setModuleId(self, value):
        self.moduleId = value
        return self

    def addImplementedEntry(self, entry_ref: RefType):
        self.implementedEntryRefs.append(entry_ref)

    def getImplementedEntries(self) -> List[RefType]:
        return self.implementedEntryRefs

    def createProvidedModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        if (short_name not in self.elements):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.providedModeGroups[short_name] = prototype
        return self.elements[short_name]

    def getProvidedModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        return sorted(self.providedModeGroups.values(), key=lambda v: v.short_name)

    def createRequiredModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        if (short_name not in self.elements):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.requiredModeGroups[short_name] = property
        return self.elements[short_name]

    def getRequiredModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        return sorted(self.requiredModeGroups.values(), key=lambda v: v.short_name)

    def createBswInternalBehavior(self, short_name: str) -> BswInternalBehavior:
        '''
            Create the INTERNAL-BEHAVIORS tag
        '''
        if (short_name not in self.elements):
            prototype = BswInternalBehavior(self, short_name)
            self.elements[short_name] = prototype
        return self.elements[short_name]

    def getBswInternalBehaviors(self) -> List[BswInternalBehavior]:
        return list(filter(lambda a: isinstance(a, BswInternalBehavior), self.elements.values()))