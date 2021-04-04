from abc import ABCMeta, abstractmethod


class ARObject(metaclass=ABCMeta):
    def __init__(self):
        if type(self) == ARObject:
            raise NotImplementedError("ARObject is an abstract class.")
        self.parent = None


class Referrable(ARObject, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == Referrable:
            raise NotImplementedError("Referrable is an abstract class.")
        self.parent = parent
        self.short_name = short_name

    @property
    def full_name(self) -> str:
        return self.parent.full_name + "/" + self.short_name

class MultilanguageReferrable(Referrable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == MultilanguageReferrable:
            raise NotImplementedError("MultilanguageReferrable is an abstract class.")
        super().__init__(parent, short_name)
        self.parent = parent
        self.long_name = None

class CollectableElement(metaclass=ABCMeta):
    def __init__(self):
        if type(self) == CollectableElement:
            raise NotImplementedError("CollectableElement is an abstract class.")
        self.elements = {}              # type: dict(PackageableElement)

    def getElements(self):
        return self.elements.values()

    def getElement(self, short_name: str) -> Referrable:
        if (short_name not in self.elements):
            return None
        return self.elements[short_name]

class Identifiable(MultilanguageReferrable, CollectableElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == Identifiable:
            raise NotImplementedError("Identifiable is an abstract class.")
        MultilanguageReferrable.__init__(self, parent, short_name)
        CollectableElement.__init__(self)

        self.category = ""
        self.desc = None

class AtpFeature(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AtpFeature:
            raise NotImplementedError("AtpFeature is an abstract class.")
        super().__init__(parent, short_name)

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


class Limit:
    def __init__(self):
        self.interval_type = None
        self.value = None
