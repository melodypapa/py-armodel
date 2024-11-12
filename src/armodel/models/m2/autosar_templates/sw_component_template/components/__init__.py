from abc import ABCMeta
from typing import List

from .....ar_ref import RefType
from .....general_structure import ARElement, Identifiable
from .....port_prototype import PPortPrototype, PortPrototype, RPortPrototype
from .....ar_object import ARObject
from ...common_structure.implementation import ImplementationProps
from .instance_refs import InnerPortGroupInCompositionInstanceRef
class SymbolProps(ImplementationProps):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class PortGroup(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._inner_group_iref = []    # type: List[InnerPortGroupInCompositionInstanceRef]
        self._outer_port_ref = []      # type: List[RefType]

    def addInnerGroupIRef(self, iref: InnerPortGroupInCompositionInstanceRef):
        self._inner_group_iref.append(iref)

    def getInnerGroupIRefs(self) -> List[InnerPortGroupInCompositionInstanceRef]:
        return self._inner_group_iref
    
    def addOuterPortRef(self, ref: RefType):
        self._outer_port_ref.append(ref)

    def getOuterPortRefs(self) -> List[RefType]:
        return self._outer_port_ref

class SwComponentType(ARElement,  metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createPPortPrototype(self, short_name: str) -> PPortPrototype:
        prototype = PPortPrototype(self, short_name)
        if (short_name not in self.elements):
            self.elements[short_name] = prototype
        return self.elements[short_name]

    def createRPortPrototype(self, short_name) -> RPortPrototype:
        prototype = RPortPrototype(self, short_name)
        if (short_name not in self.elements):
            self.elements[short_name] = prototype
        return self.elements[short_name]
    
    def createPortGroup(self, short_name) -> PortGroup:
        port_group = PortGroup(self, short_name)
        if (short_name not in self.elements):
            self.elements[short_name] = port_group
        return self.elements[short_name]

    def getPPortPrototypes(self) -> List[PPortPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, PPortPrototype), self.elements.values()), key= lambda o: o.short_name))

    def getRPortPrototypes(self) -> List[RPortPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, RPortPrototype), self.elements.values()), key= lambda o: o.short_name))
    
    def getPortPrototypes(self) -> List[PortPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, PortPrototype), self.elements.values()), key= lambda o: o.short_name))
    
    def getPortGroups(self) -> List[PortGroup]:
        return list(sorted(filter(lambda c: isinstance(c, PortGroup), self.elements.values()), key= lambda o: o.short_name))
