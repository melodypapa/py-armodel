from ....MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from .....M2.MSR.AsamHdo.AdminData import AdminData
from .....M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from .....M2.MSR.Documentation.Annotation import Annotation
from .....M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, CategoryString
from abc import ABCMeta
from typing import Dict, List


class Referrable(ARObject, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):

        if type(self) is Referrable:
            raise TypeError("Referrable is an abstract class.")
        
        ARObject.__init__(self)

        self.parent = parent
        self.short_name = short_name

    @property
    def shortName(self):
        return self.short_name

    @shortName.setter
    def shortName(self, value):
        self.short_name = value

    def getShortName(self) -> str:
        return self.short_name
    
    def getParent(self):
        return self.parent

    @property
    def full_name(self) -> str:
        return self.parent.full_name + "/" + self.short_name

    def getFullName(self) -> str:
        return self.full_name


class MultilanguageReferrable(Referrable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is MultilanguageReferrable:
            raise TypeError("MultilanguageReferrable is an abstract class.")

        super().__init__(parent, short_name)

        # self._parent = parent
        self.longName = None            # type: MultilanguageLongName

    def getLongName(self) -> MultilanguageLongName:
        return self.longName

    def setLongName(self, value: MultilanguageLongName):
        self.longName = value
        return self


class CollectableElement(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) is CollectableElement:
            raise TypeError("CollectableElement is an abstract class.")
        
        # super().__init__()
        
        self.elements: List[Referrable] = []
        self.element_mappings: Dict[str, List[Referrable]] = {}

    def getTotalElement(self) -> int:
        # return len(list(filter(lambda a: not isinstance(a, ARPackage) , self.elements)))
        return len(self.elements)

    def removeElement(self, short_name: str, type=None):
        if short_name not in self.element_mappings:
            raise KeyError("Invalid key <%s> for removing element" % short_name)
        if type is None:
            item = self.element_mappings[short_name][0]
        else:
            item = next(filter(lambda a: isinstance(a, type), self.element_mappings[short_name]))
        if item is not None:
            self.elements.remove(item)
            self.element_mappings[short_name].remove(item)

    def getElements(self):
        return self.elements

    def addElement(self, element: Referrable):
        short_name = element.getShortName()
        if not self.IsElementExists(short_name, type(element)):
            self.elements.append(element)
            if short_name not in self.element_mappings:
                self.element_mappings[short_name] = []
            self.element_mappings[short_name].append(element)

    def getElement(self, short_name: str, type=None) -> Referrable:
        if (short_name not in self.element_mappings):
            return None
        if type is not None:
            result = list(filter(lambda a: isinstance(a, type), self.element_mappings[short_name]))
            if len(result) == 0:
                return None
            return result[0]
        return self.element_mappings[short_name][0]
    
    def IsElementExists(self, short_name: str, type=None) -> bool:
        if type is None:
            return short_name in self.element_mappings
        if short_name in self.element_mappings:
            return any(isinstance(a, type) for a in self.element_mappings[short_name])
        return False


class Identifiable(MultilanguageReferrable, CollectableElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Identifiable:
            raise TypeError("Identifiable is an abstract class.")
        
        MultilanguageReferrable.__init__(self, parent, short_name)
        CollectableElement.__init__(self)

        self.annotations = []                       # type: List[Annotation]
        self.adminData = None                       # type: AdminData
        self.category = None                        # type: CategoryString
        self.introduction = None                    # type: DocumentationBlock
        self.desc = None                            # type: MultiLanguageOverviewParagraph

    def getAdminData(self):
        return self.adminData

    def setAdminData(self, value):
        if value is not None:
            self.adminData = value
        return self
    
    def removeAdminData(self):
        self.adminData = None

    def getDesc(self):
        return self.desc

    def setDesc(self, value):
        self.desc = value
        return self

    def getCategory(self):
        return self.category

    def setCategory(self, value):
        if isinstance(value, str):
            self.category = CategoryString().setValue(value)
        else:
            self.category = value
        return self
    
    def getIntroduction(self):
        return self.introduction

    def setIntroduction(self, value):
        self.introduction = value
        return self

    def addAnnotation(self, annotation: Annotation):
        self.annotations.append(annotation)
        return self

    def getAnnotations(self) -> List[Annotation]:
        return self.annotations


class PackageableElement(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PackageableElement:
            raise TypeError("PackageableElement is an abstract class.")
        super().__init__(parent, short_name)


class ARElement(PackageableElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ARElement:
            raise TypeError("ARElement is an abstract class.")
        super().__init__(parent, short_name)


class Describable(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) is Describable:
            raise TypeError("Describable is an abstract class.")

        super().__init__()

        self.desc = None
        self.category = None
        self.adminData = None
        self.introduction = None

    def getDesc(self):
        return self.desc

    def setDesc(self, value):
        if value is not None:
            self.desc = value
        return self

    def getCategory(self):
        return self.category

    def setCategory(self, value):
        if value is not None:
            self.category = value
        return self

    def getAdminData(self):
        return self.adminData

    def setAdminData(self, value):
        if value is not None:
            self.adminData = value
        return self
    
    def removeAdminData(self):
        self.adminData = None

    def getIntroduction(self):
        return self.introduction

    def setIntroduction(self, value):
        if value is not None:
            self.introduction = value
        return self


    
