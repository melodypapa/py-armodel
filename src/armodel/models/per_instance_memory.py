
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .M2.MSR.data_dictionary.data_def_properties import SwDataDefProps
from .ar_object import ARLiteral
from .general_structure import Identifiable


class PerInstanceMemory(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initValue = None           # type: ARLiteral
        self.swDataDefProps = None      # type: SwDataDefProps
        self.type = None                # type: ARLiteral
        self.typeDefinition = None      # type: ARLiteral

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
