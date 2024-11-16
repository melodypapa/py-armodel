from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from .ArObject import ARObject
from .PrimitiveTypes import ARLiteral
from ....MSR.Documentation.Annotation import Annotation
from ....MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from abc import ABCMeta
from typing import List

class Referrable(ARObject, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):

        if type(self) == Referrable:
            raise NotImplementedError("Referrable is an abstract class.")
        ARObject.__init__(self)

        self._parent = parent
        self.short_name = short_name

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def shortName(self):
        return self.short_name

    @shortName.setter
    def shortName(self, value):
        self.short_name = value

    def getShortName(self) -> str:
        return self.short_name

    @property
    def full_name(self) -> str:
        return self._parent.full_name + "/" + self.short_name

    def getFullName(self) -> str:
        return self.full_name

class MultilanguageReferrable(Referrable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == MultilanguageReferrable:
            raise NotImplementedError("MultilanguageReferrable is an abstract class.")

        super().__init__(parent, short_name)

        #self._parent = parent
        self.longName = None            # type: MultilanguageLongName

    def getLongName(self) -> MultilanguageLongName:
        return self.longName

    def setLongName(self, value: MultilanguageLongName):
        self.longName = value
        return self


class CollectableElement(ARObject, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == CollectableElement:
            raise NotImplementedError("CollectableElement is an abstract class.")
        self.elements = {}              # type: dict[str, Referrable]

    def getTotalElement(self) -> int:
        #return len(list(filter(lambda a: not isinstance(a, ARPackage) , self.elements.values())))
        return len(self.elements.values())

    def removeElement(self, key):
        if key not in self.elements:
            raise KeyError("Invalid key <%s> for removing element" % key)
        self.elements.pop(key)

    def getElements(self):
        return self.elements.values()

    def addElement(self, element: Referrable):
        self.elements[element.getShortName()] = element

    def getElement(self, short_name: str) -> Referrable:
        if (short_name not in self.elements):
            return None
        return self.elements[short_name]

class Identifiable(MultilanguageReferrable, CollectableElement, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == Identifiable:
            raise NotImplementedError("Identifiable is an abstract class.")
        MultilanguageReferrable.__init__(self, parent, short_name)
        CollectableElement.__init__(self)

        self.annotations = []       # type: List[Annotation]
        self.adminData = None       # type: AdminData
        self.category = None        # type: ARLiteral
        self.desc = None            # type: MultiLanguageOverviewParagraph

    def getAdminData(self):
        return self.adminData

    def setAdminData(self, value):
        self.adminData = value
        return self

    def getDesc(self):
        return self.desc

    def setDesc(self, value):
        self.desc = value
        return self

    def getCategory(self):
        return self.category

    def setCategory(self, value):
        self.category = value
        return self

    def addAnnotation(self, annotation: Annotation):
        self.annotations.append(annotation)
        return self

    def getAnnotations(self) -> List[Annotation]:
        return self.annotations


class PackageableElement(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == PackageableElement:
            raise NotImplementedError("PackageableElement is an abstract class.")
        super().__init__(parent, short_name)


class ARElement(PackageableElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ARElement:
            raise NotImplementedError("ARElement is an abstract class.")
        super().__init__(parent, short_name)


class Describable(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == Describable:
            raise NotImplementedError("Describable is an abstract class.")

        super().__init__()

        self._desc = None
        self._category = None
        self._adminData = None
        self._introduction = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value: ARLiteral):
        self._category = value


