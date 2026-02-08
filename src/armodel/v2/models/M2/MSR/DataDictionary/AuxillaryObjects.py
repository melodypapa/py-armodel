from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)


class SwAddrMethod(AtpBlueprintable):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.memoryAllocationKeywordPolicy: Union[ARLiteral, None] = None
        self.options: List[ARLiteral] = []
        self.sectionInitializationPolicy: Union[ARLiteral, None] = None
        self.sectionType: Union[ARLiteral, None] = None

    def getMemoryAllocationKeywordPolicy(self):
        return self.memoryAllocationKeywordPolicy

    def setMemoryAllocationKeywordPolicy(self, value):
        self.memoryAllocationKeywordPolicy = value
        return self

    def getOptions(self):
        return self.options

    def addOption(self, value):
        self.options.append(value)
        return self

    def getSectionInitializationPolicy(self):
        return self.sectionInitializationPolicy

    def setSectionInitializationPolicy(self, value):
        self.sectionInitializationPolicy = value
        return self

    def getSectionType(self):
        return self.sectionType

    def setSectionType(self, value):
        self.sectionType = value
        return self
