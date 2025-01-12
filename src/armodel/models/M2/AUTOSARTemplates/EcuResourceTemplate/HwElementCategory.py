from typing import List

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable


class HwType(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class HwAttributeDef(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.hwAttributeLiterals = []                       # type: List[HwAttributeLiteralDef]
        self.isRequired = None                              # type: Boolean
        self.unitRef = None                                 # type: RefType

    def getHwAttributeLiterals(self):
        return self.hwAttributeLiterals

    def setHwAttributeLiterals(self, value):
        if value is not None:
            self.hwAttributeLiterals = value
        return self

    def getIsRequired(self):
        return self.isRequired

    def setIsRequired(self, value):
        if value is not None:
            self.isRequired = value
        return self

    def getUnitRef(self):
        return self.unitRef

    def setUnitRef(self, value):
        if value is not None:
            self.unitRef = value
        return self


class HwCategory(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.hwAttributeDefs = []                           # type: List[HwAttributeDef]

    def getHwAttributeDefs(self):
        return self.hwAttributeDefs

    def createHwAttributeDef(self, short_name: str) -> HwAttributeDef:
        if (not self.IsElementExists(short_name)):
            pin_group = HwAttributeDef(self, short_name)
            self.addElement(pin_group)
            self.hwAttributeDefs.append(pin_group)
        return self.getElement(short_name)
