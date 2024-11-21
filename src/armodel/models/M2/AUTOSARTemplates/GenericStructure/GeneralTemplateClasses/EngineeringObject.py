from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from abc import ABCMeta

class EngineeringObject(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == EngineeringObject:
            raise NotImplementedError("EngineeringObject is an abstract class.")

        super().__init__()

        self.category = None                # type: ARLiteral
        self.domain = None                  # type: ARLiteral
        self.revision_label = None           # type: ARLiteral
        self.short_label = None              # type: ARLiteral

    def setCategory(self, category: any):
        if isinstance(category, ARLiteral):
            self.category = category
        else:
            self.category = ARLiteral()
            self.category.setValue(str(category))
        return self

    def getCategory(self) -> ARLiteral:
        return self.category

    def setDomain(self, domain: ARLiteral):
        self.domain = domain
        return self

    def getDomain(self) -> ARLiteral:
        return self.domain

    def setRevisionLabel(self, revision_label: ARLiteral):
        self.revision_label = revision_label
        return self

    def getRevisionLabel(self) -> ARLiteral:
        return self.revision_label

    def setShortLabel(self, label: ARLiteral):
        self.short_label = label
        return self

    def getShortLabel(self) -> ARLiteral:
        return self.short_label


class AutosarEngineeringObject(EngineeringObject):
    def __init__(self):
        super().__init__()