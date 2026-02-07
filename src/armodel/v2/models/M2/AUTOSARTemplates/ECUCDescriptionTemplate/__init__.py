from abc import ABC
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (
    AnyInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    AREnum,
    ARLiteral,
    ARNumerical,
    RefType,
)
from armodel.v2.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)


class EcucValueCollection(ARElement):
    def __init__(self, parent: ARObject, short_name: str) -> None:
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


class EcucIndexableValue(ARObject, ABC):
    def __init__(self) -> None:
        if type(self) is EcucIndexableValue:
            raise TypeError("EcucIndexableValue is an abstract class.")

        super().__init__()


class EcucParameterValue(EcucIndexableValue, ABC):
    def __init__(self) -> None:
        if type(self) is EcucParameterValue:
            raise TypeError("EcucParameterValue is an abstract class.")

        super().__init__()

        self.annotations = []                       # type: List[Annotation]
        self.definitionRef: Union[RefType, None] = None
        self.isAutoValue: Union[ARBoolean, None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.value: Union[DocumentationBlock, None] = None

    def getValue(self) -> DocumentationBlock:
        return self.value

    def setValue(self, value: DocumentationBlock) -> None:
        self.value = value


class EcucTextualParamValue(EcucParameterValue):
    def __init__(self) -> None:
        super().__init__()

        self.value: Union[ARLiteral, None] = None

    def getValue(self) -> ARLiteral:
        return self.value

    def setValue(self, value: ARLiteral) -> None:
        self.value = value


class EcucNumericalParamValue(EcucParameterValue):
    def __init__(self) -> None:
        super().__init__()

        self.value: Union[ARNumerical, None] = None

    def getValue(self) -> ARNumerical:
        return self.value

    def setValue(self, value: ARNumerical) -> None:
        self.value = value


class EcucAbstractReferenceValue(EcucIndexableValue, ABC):
    def __init__(self) -> None:
        if type(self) is EcucAbstractReferenceValue:
            raise TypeError("EcucAbstractReferenceValue is an abstract class.")

        super().__init__()

        self.annotations = []                       # type: List[Annotation]
        self.definitionRef: Union[RefType, None] = None
        self.isAutoValue: Union[ARBoolean, None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.valueIRef: Union[AnyInstanceRef, None] = None

    def getValueIRef(self) -> AnyInstanceRef:
        return self.valueRef

    def setValueIRef(self, value: AnyInstanceRef):
        self.valueRef = value
        return self


class EcucReferenceValue(EcucAbstractReferenceValue):
    def __init__(self) -> None:
        super().__init__()

        self.valueRef: Union[RefType, None] = None

    def getValueRef(self) -> RefType:
        return self.valueRef

    def setValueRef(self, value: RefType):
        self.valueRef = value
        return self


class EcucContainerValue(Identifiable, EcucIndexableValue):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        Identifiable.__init__(self, parent, short_name)

        self.definitionRef: Union[RefType, None] = None
        self.parameterValues = []                   # type: List[EcucParameterValue]
        self.referenceValues = []                   # type: List[EcucAbstractReferenceValue]
        self.subContainers = []                     # type: List[EcucContainerValue]

    def getDefinitionRef(self) -> RefType:
        return self.definitionRef

    def setDefinitionRef(self, value: RefType):
        self.definitionRef = value
        return self

    def getParameterValues(self) -> List[EcucParameterValue]:
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
        if not self.IsElementExists(short_name):
            container_value = EcucContainerValue(self, short_name)
            self.addElement(container_value)
            self.subContainers.append(container_value)
        return self.getElement(short_name, EcucContainerValue)


class EcucModuleConfigurationValues(ARElement):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.containers = []                        # type: List[EcucContainerValue]
        self.definitionRef: Union[RefType, None] = None
        self.ecucDefEdition: Union[ARLiteral, None] = None
        self.implementationConfigVariant: Union[ARLiteral, None] = None
        self.moduleDescriptionRef: Union[RefType, None] = None
        self.postBuildVariantUsed: Union[ARBoolean, None] = None

    def createContainer(self, short_name: str) -> EcucContainerValue:
        if not self.IsElementExists(short_name):
            container = EcucContainerValue(self, short_name)
            self.addElement(container)
            self.containers.append(container)
        return self.getElement(short_name, EcucContainerValue)

    def getContainers(self) -> List[EcucContainerValue]:
        return sorted(filter(lambda a: isinstance(a, EcucContainerValue), self.elements), key=lambda o: o.short_name)

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


class EcucConditionSpecification(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        # self.conditionFormula: Union[Union[EcucConditionFormula, None] , None] = None     # 0..1 aggr Definition of the formula used to define existence dependencies.
        # self.ecucQueries: List[EcucQuery] = []                  # *    aggr Query to the ECU Configuration Description.
        # self.informalFormula: Union[Union[MlFormula, None] , None] = None                 # 0..1 aggr Informal description of the condition used to to define existence dependencies. # noqa E501


class EcucConfigurationVariantEnum(AREnum):
    def __init__(self) -> None:
        super().__init__([])


__all__ = []
