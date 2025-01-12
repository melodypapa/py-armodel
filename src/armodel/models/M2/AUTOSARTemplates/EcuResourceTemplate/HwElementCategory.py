from typing import List
from .....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement


class HwCategory(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.hwAttributeDefs = []                           # type: List[HwAttributeDef]

    def getHwAttributeDefs(self):
        return self.hwAttributeDefs

    def setHwAttributeDefs(self, value):
        if value is not None:
            self.hwAttributeDefs = value
        return self
