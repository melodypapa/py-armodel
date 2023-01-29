from abc import ABCMeta
from typing import List
from .ar_object import ARObject
from .ar_ref import RefType


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

        self._category = None
        self.desc = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

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

class SwcBswRunnableMapping(ARObject):
    def __init__(self):
        '''
            Maps a BswModuleEntity to a RunnableEntity if it is implemented as part of a BSW
            module (in the case of an AUTOSAR Service, a Complex Driver or an ECU
            Abstraction). The mapping can be used by a tool to find relevant information on the
            behavior, e.g. whether the bswEntity shall be running in interrupt context.

        '''
        super().__init__()

        self.bsw_entity_ref   = None        # type: RefType
        self.swc_runnable_ref = None        # type: RefType

class SwcBswMapping(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bsw_behavior_ref = None            # type: RefType
        self.runnable_mappings = []
        self.swc_behavior_ref = None            # type: RefType
        self.synchronized_mode_groups = []       
        self.synchronized_triggers = []

    def addRunnableMapping(self, mapping: SwcBswRunnableMapping):
        self.runnable_mappings.append(mapping)

    def getRunnableMappings(self) -> List[SwcBswRunnableMapping]:
        return self.runnable_mappings

class ARElement(PackageableElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ARElement:
            raise NotImplementedError("ARElement is an abstract class.")
        super().__init__(parent, short_name)

class AtpStructureElement(AtpFeature, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AtpFeature:
            raise NotImplementedError("AtpStructureElement is an abstract class.")
        super().__init__(parent, short_name)

class Limit:
    def __init__(self):
        self.interval_type = None
        self.value = None
