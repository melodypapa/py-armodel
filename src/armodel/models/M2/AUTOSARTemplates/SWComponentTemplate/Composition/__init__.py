from abc import ABCMeta
from .....M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import PPortInCompositionInstanceRef, PortInCompositionTypeInstanceRef
from .....M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import RPortInCompositionInstanceRef
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class SwComponentPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.typeTRef = None                       # type: RefType

    def getTypeTRef(self) -> RefType:
        return self.typeTRef

    def setTypeTRef(self, value: RefType):
        self.typeTRef = value
        return self


class SwConnector(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.mappingRef: RefType = None

    def getMappingRef(self) -> RefType:
        return self.mappingRef

    def setMappingRef(self, value: RefType):
        self.mappingRef = value
        return self


class AssemblySwConnector(SwConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.providerIRef: PPortInCompositionInstanceRef = None
        self.requesterIRef: RPortInCompositionInstanceRef = None

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
        
        self.innerPortIRref: PortInCompositionTypeInstanceRef = None
        self.outerPortRef: RefType = None

    def getInnerPortIRref(self) -> PortInCompositionTypeInstanceRef:
        return self.innerPortIRref

    def setInnerPortIRref(self, value: PortInCompositionTypeInstanceRef):
        self.innerPortIRref = value
        return self

    def getOuterPortRef(self) -> RefType:
        return self.outerPortRef

    def setOuterPortRef(self, value: RefType):
        self.outerPortRef = value
        return self


class PassThroughSwConnector(SwConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.providedOuterPortRef: RefType = None
        self.requiredOuterPortRef: RefType = None

    def getProvidedOuterPortRef(self) -> RefType:
        return self.providedOuterPortRef

    def setProvidedOuterPortRef(self, value: RefType):
        self.providedOuterPortRef = value
        return self

    def getRequiredOuterPortRef(self) -> RefType:
        return self.requiredOuterPortRef

    def setRequiredOuterPortRef(self, value: RefType):
        self.requiredOuterPortRef = value
        return self
