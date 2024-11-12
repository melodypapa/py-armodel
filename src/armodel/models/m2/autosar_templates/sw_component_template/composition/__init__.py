from abc import ABCMeta
from typing import List

from ..components import SwComponentType
from ..composition.instance_refs import PPortInCompositionInstanceRef, PortInCompositionTypeInstanceRef, RPortInCompositionInstanceRef
from .....ar_ref import RefType
from .....ar_object import ARObject
from .....general_structure import Identifiable


class SwComponentPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.typeTRef = None                       # type: RefType

    def getTypeTRef(self):
        return self.typeTRef

    def setTypeTRef(self, value):
        self.typeTRef = value
        return self

class SwConnector(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.mappingRef = None                      # type: RefType

    def getMappingRef(self):
        return self.mappingRef

    def setMappingRef(self, value):
        self.mappingRef = value
        return self

class AssemblySwConnector(SwConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.providerIRef = None        # type: PPortInCompositionInstanceRef
        self.requesterIRef = None       # type: RPortInCompositionInstanceRef

    def getProviderIRef(self):
        return self.providerIRef

    def setProviderIRef(self, value):
        self.providerIRef = value
        return self

    def getRequesterIRef(self):
        return self.requesterIRef

    def setRequesterIRef(self, value):
        self.requesterIRef = value
        return self


class DelegationSwConnector(SwConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.innerPortIRref = None                          # type: PortInCompositionTypeInstanceRef
        self.outerPortRef = None                            # type: RefType

    def getInnerPortIRref(self):
        return self.innerPortIRref

    def setInnerPortIRref(self, value):
        self.innerPortIRref = value
        return self

    def getOuterPortRef(self):
        return self.outerPortRef

    def setOuterPortRef(self, value):
        self.outerPortRef = value
        return self


class PassThroughSwConnector(SwConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.providedOuterPortRef = None                    # type: RefType
        self.requiredOuterPortRef = None                    # type: RefType

    def getProvidedOuterPortRef(self):
        return self.providedOuterPortRef

    def setProvidedOuterPortRef(self, value):
        self.providedOuterPortRef = value
        return self

    def getRequiredOuterPortRef(self):
        return self.requiredOuterPortRef

    def setRequiredOuterPortRef(self, value):
        self.requiredOuterPortRef = value
        return self


class CompositionSwComponentType(SwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.constantValueMappingRefs = []                      # type: List[RefType]
        self.dataTypeMappingRefs = []                           # type: List[RefType]
        self.instantiationRTEEventProps = []                    # type: List[InstantiationRTEEventProps]

    def removeAllAssemblySwConnector(self):
        for sw_connector in self.getAssemblySwConnectors():
            self.elements.pop(sw_connector.short_name)

    def removeAllDelegationSwConnector(self):
        for sw_connector in self.getDelegationSwConnectors():
            self.elements.pop(sw_connector.short_name)

    def createAssemblySwConnector(self, short_name: str) -> AssemblySwConnector:
        if (short_name not in self.elements):
            connector = AssemblySwConnector(self, short_name)
            self.elements[short_name] = connector
        return self.elements[short_name]
    
    def createDelegationSwConnector(self, short_name: str) -> DelegationSwConnector:
        if short_name not in self.elements:
            connector = DelegationSwConnector(self, short_name)
            self.elements[short_name] = connector
        return self.elements[short_name]

    def getAssemblySwConnectors(self) -> List[AssemblySwConnector]:
        return list(sorted(filter(lambda e: isinstance(e, AssemblySwConnector), self.elements.values()), key = lambda c: c.short_name))
    
    def getDelegationSwConnectors(self) -> List[DelegationSwConnector]:
        return list(sorted(filter(lambda e: isinstance(e, DelegationSwConnector), self.elements.values()), key = lambda c: c.short_name))
    
    def getSwConnectors(self) -> List[SwConnector]:
        return list(sorted(filter(lambda e: isinstance(e, SwConnector), self.elements.values()), key = lambda c: c.short_name))
    
    def createSwComponentPrototype(self, short_name: str) -> SwComponentPrototype:
        if (short_name not in self.elements):
            connector = SwComponentPrototype(self, short_name)
            self.elements[short_name] = connector
        return self.elements[short_name] 

    def getSwComponentPrototypes(self) -> List[SwComponentPrototype]:
        return list(filter(lambda e: isinstance(e, SwComponentPrototype), self.elements.values()))
    
    def addDataTypeMapping(self, data_type_mapping_ref: RefType):
        self.dataTypeMappingRefs.append(data_type_mapping_ref)

    def getDataTypeMappings(self) -> List[RefType]:
        return self.dataTypeMappingRefs        
        