"""
This module contains classes for representing AUTOSAR mode declaration groups
in software component internal behavior templates.
"""

from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import ModeAccessPointIdent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import PModeGroupInAtomicSwcInstanceRef, RModeGroupInAtomicSWCInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ModeAccessPoint(ARObject):
    def __init__(self):
        super().__init__()

        self.ident: 'ModeAccessPointIdent' = None
        self.modeGroupIRef: 'RModeGroupInAtomicSWCInstanceRef' = None

    def getIdent(self):
        return self.ident

    def setIdent(self, value):
        self.ident = value
        return self

    def getModeGroupIRef(self):
        return self.modeGroupIRef

    def setModeGroupIRef(self, value):
        self.modeGroupIRef = value
        return self

class ModeSwitchPoint(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.modeGroupIRef: 'PModeGroupInAtomicSwcInstanceRef' = None

    def getModeGroupIRef(self):
        return self.modeGroupIRef

    def setModeGroupIRef(self, value):
        self.modeGroupIRef = value
        return self


class IncludedModeDeclarationGroupSet(ARObject):
    def __init__(self):
        super().__init__()

        self.mode_declaration_group_refs: List['RefType'] = []
        self.prefix: 'Identifier' = None

    def addModeDeclarationGroupRef(self, ref: RefType):
        self.mode_declaration_group_refs.append(ref)
        return self

    def getModeDeclarationGroupRefs(self) -> List[RefType]:
        return self.mode_declaration_group_refs

    def setPrefix(self, prefix: str):
        self.prefix = prefix
        return self

    def getPrefix(self) -> ARLiteral:
        return self.prefix
