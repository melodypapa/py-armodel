"""
This module contains classes for representing AUTOSAR per-instance memory elements
in software component internal behavior templates.
"""

from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

class PerInstanceMemory(AtpStructureElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initValue: ARLiteral = None
        self.swDataDefProps: 'SwDataDefProps' = None
        self.type: ARLiteral = None
        self.typeDefinition: ARLiteral = None

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self

    def getType(self):
        return self.type

    def setType(self, value):
        self.type = value
        return self

    def getTypeDefinition(self):
        return self.typeDefinition

    def setTypeDefinition(self, value):
        self.typeDefinition = value
        return self