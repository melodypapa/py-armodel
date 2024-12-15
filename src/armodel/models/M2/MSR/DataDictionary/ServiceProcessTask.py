from ....M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps, ValueList
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ArgumentDirectionEnum
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

class SwServiceArg(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.direction = None                   # type: ArgumentDirectionEnum
        self.swArraysize = None                 # type: ValueList
        self.swDataDefProps = None              # type: SwDataDefProps

    def getDirection(self):
        return self.direction

    def setDirection(self, value):
        self.direction = value
        return self

    def getSwArraysize(self):
        return self.swArraysize

    def setSwArraysize(self, value):
        self.swArraysize = value
        return self

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self
