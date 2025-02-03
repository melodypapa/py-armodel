from ....MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from .....M2.MSR.AsamHdo.AdminData import AdminData
from .....M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from .....M2.MSR.Documentation.Annotation import Annotation
from .....M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, CategoryString
from abc import ABCMeta
from typing import List


class Referrable(ARObject, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):

        if type(self) is Referrable:
            raise NotImplementedError("Referrable is an abstract class.")
        
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
            raise NotImplementedError("MultilanguageReferrable is an abstract class.")

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
            raise NotImplementedError("CollectableElement is an abstract class.")
        
        self.elements = {}              # type: dict[str, Referrable]

    def getTotalElement(self) -> int:
        # return len(list(filter(lambda a: not isinstance(a, ARPackage) , self.elements.values())))
        return len(self.elements.values())

    def removeElement(self, key):
        if key not in self.elements:
            raise KeyError("Invalid key <%s> for removing element" % key)
        self.elements.pop(key)

    def getElements(self):
        return self.elements.values()

    def addElement(self, element: Referrable):
        short_name = element.getShortName()
        if not self.IsElementExists(short_name):
            self.elements[short_name] = element

    def getElement(self, short_name: str) -> Referrable:
        if (short_name not in self.elements):
            return None
        return self.elements[short_name]
    
    def IsElementExists(self, short_name: str) -> bool:
        return short_name in self.elements


class Identifiable(MultilanguageReferrable, CollectableElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Identifiable:
            raise NotImplementedError("Identifiable is an abstract class.")
        
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
            raise NotImplementedError("PackageableElement is an abstract class.")
        super().__init__(parent, short_name)


class ARElement(PackageableElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ARElement:
            raise NotImplementedError("ARElement is an abstract class.")
        super().__init__(parent, short_name)


class Describable(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) is Describable:
            raise NotImplementedError("Describable is an abstract class.")

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


    
