from abc import ABCMeta
from typing import List

from ..autosar_templates.generic_structure.abstract_structure import AnyInstanceRef
from ..msr.documentation.block_elements import DocumentationBlock
from ...annotation import Annotation
from ...ar_ref import RefType
from ...ar_object import ARBoolean, ARLiteral, ARNumerical, ARObject
from ...general_structure import ARElement

class EcucValueCollection(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ecucValueRefs = []
        self.ecuExtractRef = None

    def getEcucValueRefs(self) -> List[RefType]:
        return self.ecucValueRefs

    def addEcucValueRef(self, ref: RefType):
        self.ecucValueRefs.append(ref)
        return self

    def getEcuExtractRef(self):
        return self.ecuExtractRef

    def setEcuExtractRef(self, value):
        self.ecuExtractRef = value
        return self
    
class EcucIndexableValue(ARObject, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == EcucIndexableValue:
            raise NotImplementedError("EcucIndexableValue is an abstract class.")
        
        super().__init__()

class EcucAbstractReferenceValue(EcucIndexableValue, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == EcucAbstractReferenceValue:
            raise NotImplementedError("EcucAbstractReferenceValue is an abstract class.")
        
        super().__init__()
    
class EcucParameterValue(EcucIndexableValue, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == EcucParameterValue:
            raise NotImplementedError("EcucParameterValue is an abstract class.")
        
        super().__init__()

        self.annotations = []                       # type: List[Annotation]
        self.definitionRef = None                   # type: RefType
        self.isAutoValue = None                     # type: ARBoolean

    def getAnnotations(self) -> List[Annotation]:
        return self.annotations

    def addAnnotation(self, value: Annotation):
        self.annotations.append(value)
        return self

    def getDefinitionRef(self) -> RefType:
        return self.definitionRef

    def setDefinitionRef(self, value: RefType):
        self.definitionRef = value
        return self

    def getIsAutoValue(self) -> ARBoolean:
        return self.isAutoValue

    def setIsAutoValue(self, value: ARBoolean):
        self.isAutoValue = value
        return self

class EcucAddInfoParamValue(EcucParameterValue):
    def __init__(self):
        super().__init__()

        self.value = None                           # type: DocumentationBlock

    def getValue(self) -> DocumentationBlock:
        return self.value

    def setValue(self, value: DocumentationBlock):
        self.value = value

class EcucTextualParamValue(EcucParameterValue):
    def __init__(self):
        super().__init__()

        self.value = None                           # type: ARLiteral

    def getValue(self) -> ARLiteral:
        return self.value

    def setValue(self, value:ARLiteral):
        self.value = value


class EcucNumericalParamValue(EcucParameterValue):
    def __init__(self):
        super().__init__()

        self.value = None                           # type: ARNumerical

    def getValue(self) -> ARNumerical:
        return self.value

    def setValue(self, value: ARNumerical):
        self.value = value

class EcucAbstractReferenceValue(EcucIndexableValue, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == EcucAbstractReferenceValue:
            raise NotImplementedError("EcucAbstractReferenceValue is an abstract class.")
        
        super().__init__()

        self.annotations = []                       # type: List[Annotation]
        self.definitionRef = None                   # type: RefType
        self.isAutoValue = None                     # type: ARBoolean

    def getAnnotations(self) -> List[Annotation]:
        return self.annotations

    def addAnnotation(self, value: Annotation):
        self.annotations.append(value)
        return self

    def getDefinitionRef(self) -> RefType:
        return self.definitionRef

    def setDefinitionRef(self, value: RefType):
        self.definitionRef = value
        return self

    def getIsAutoValue(self) -> ARBoolean:
        return self.isAutoValue

    def setIsAutoValue(self, value: ARBoolean):
        self.isAutoValue = value
        return self

class EcucInstanceReferenceValue(EcucAbstractReferenceValue):
    def __init__(self):
        super().__init__()

        self.valueIRef = None        # type: AnyInstanceRef

    def getValueIRef(self) -> AnyInstanceRef:
        return self.valueRef

    def setValueIRef(self, value: AnyInstanceRef):
        self.valueRef = value
        return self

class EcucReferenceValue(EcucAbstractReferenceValue):
    def __init__(self):
        super().__init__()

        self.valueRef = None        # type: RefType

    def getValueRef(self) -> RefType:
        return self.valueRef

    def setValueRef(self, value: RefType):
        self.valueRef = value
        return self

class EcucContainerValue(ARElement, EcucIndexableValue):
    def __init__(self, parent: ARObject, short_name: str):
        ARElement.__init__(self, parent, short_name)

        self.definitionRef = None                   # type: RefType
        self.parameterValues = []                   # type: List[EcucParameterValue]
        self.referenceValues = []                   # type: List[EcucAbstractReferenceValue]
        self.subContainers = []                     # type: List[EcucContainerValue]

    def getDefinitionRef(self) -> RefType:
        return self.definitionRef

    def setDefinitionRef(self, value: RefType):
        self.definitionRef = value
        return self

    def getParameterValues(self)-> List[EcucParameterValue]:
        return self.parameterValues

    def addParameterValue(self, value: EcucParameterValue):
        self.parameterValues.append(value)
        return self

    def getReferenceValues(self) -> EcucAbstractReferenceValue:
        return self.referenceValues

    def addReferenceValue(self, value: EcucAbstractReferenceValue):
        self.referenceValues.append(value)
        return self

    def getSubContainers(self):
        return self.subContainers

    def createSubContainer(self, short_name):
        if (short_name not in self.elements):
            container_value = EcucContainerValue(self, short_name)
            self.elements[short_name] = container_value
            self.subContainers.append(container_value)
        return self.elements[short_name]


class EcucModuleConfigurationValues(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.containers = []                        # type: List[EcucContainerValue]
        self.definitionRef = None                   # type: RefType
        self.ecucDefEdition = None                  # type: ARLiteral
        self.implementationConfigVariant = None     # type: ARLiteral
        self.moduleDescriptionRef = None            # type: RefType
        self.postBuildVariantUsed = None            # type: ARBoolean

    def createContainer(self, short_name: str) -> EcucContainerValue:
        if (short_name not in self.elements):
            container = EcucContainerValue(self, short_name)
            self.elements[short_name] = container
            self.containers.append(container)
        return self.elements[short_name]

    def getContainers(self) -> List[EcucContainerValue]:
        return list(sorted(filter(lambda a: isinstance(a, EcucContainerValue), self.elements.values()), key= lambda o:o.short_name))

    def getDefinitionRef(self) -> RefType:
        return self.definitionRef

    def setDefinitionRef(self, value: RefType):
        self.definitionRef = value
        return self

    def getEcucDefEdition(self) -> ARLiteral:
        return self.ecucDefEdition

    def setEcucDefEdition(self, value: ARLiteral):
        self.ecucDefEdition = value
        return self

    def getImplementationConfigVariant(self) -> ARLiteral:
        return self.implementationConfigVariant

    def setImplementationConfigVariant(self, value: ARLiteral):
        self.implementationConfigVariant = value
        return self

    def getModuleDescriptionRef(self) -> RefType:
        return self.moduleDescriptionRef

    def setModuleDescriptionRef(self, value: RefType):
        self.moduleDescriptionRef = value
        return self

    def getPostBuildVariantUsed(self) -> ARBoolean:
        return self.postBuildVariantUsed

    def setPostBuildVariantUsed(self, value: ARBoolean):
        self.postBuildVariantUsed = value
        return self

