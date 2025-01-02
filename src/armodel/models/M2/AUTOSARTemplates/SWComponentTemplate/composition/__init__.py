from abc import ABCMeta
from .....M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import PPortInCompositionInstanceRef, PortInCompositionTypeInstanceRef, RPortInCompositionInstanceRef
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

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

        self.mappingRef = None          # type: RefType
        self.providerIRef = None        # type: PPortInCompositionInstanceRef
        self.requesterIRef = None       # type: RPortInCompositionInstanceRef

    def getMappingRef(self):
        return self.mappingRef

    def setMappingRef(self, value):
        self.mappingRef = value
        return self

    def getProviderIRef(self) -> PPortInCompositionInstanceRef:
        return self.providerIRef

    def setProviderIRef(self, value: PPortInCompositionInstanceRef):
        self.providerIRef = value
        return self

    def getRequesterIRef(self) -> RPortInCompositionInstanceRef:
        return self.requesterIRef

    def setRequesterIRef(self, value: RPortInCompositionInstanceRef):
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
        