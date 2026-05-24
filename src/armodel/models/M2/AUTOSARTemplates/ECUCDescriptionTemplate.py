from abc import ABC
from typing import List

from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARLiteral, ARNumerical
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable


class EcucValueCollection(ARElement):
    """
    Collection of ECUC values with references to ECU extract.
    """
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


class EcucIndexableValue(ARObject, ABC):
    """
    Abstract base class for indexable ECUC values.
    """
    def __init__(self):
        if type(self) is EcucIndexableValue:
            raise TypeError("EcucIndexableValue is an abstract class.")

        super().__init__()


class EcucParameterValue(EcucIndexableValue, ABC):
    """
    Abstract base class for ECUC parameter values with annotation,
    definition reference, and auto value flag.
    """
    def __init__(self):
        if type(self) is EcucParameterValue:
            raise TypeError("EcucParameterValue is an abstract class.")

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
    """
    ECUC parameter value for additional info with documentation block
    content.
    """
    def __init__(self):
        super().__init__()

        self.value = None                           # type: DocumentationBlock

    def getValue(self) -> DocumentationBlock:
        return self.value

    def setValue(self, value: DocumentationBlock):
        self.value = value


class EcucTextualParamValue(EcucParameterValue):
    """
    ECUC parameter value for textual string values.
    """
    def __init__(self):
        super().__init__()

        self.value = None                           # type: ARLiteral

    def getValue(self) -> ARLiteral:
        return self.value

    def setValue(self, value: ARLiteral):
        self.value = value


class EcucNumericalParamValue(EcucParameterValue):
    """
    ECUC parameter value for numerical values.
    """
    def __init__(self):
        super().__init__()

        self.value = None                           # type: ARNumerical

    def getValue(self) -> ARNumerical:
        return self.value

    def setValue(self, value: ARNumerical):
        self.value = value


class EcucAbstractReferenceValue(EcucIndexableValue, ABC):
    """
    Abstract base class for ECUC reference values with annotation,
    definition reference, and auto value flag.
    """
    def __init__(self):
        if type(self) is EcucAbstractReferenceValue:
            raise TypeError("EcucAbstractReferenceValue is an abstract class.")

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
    """
    ECUC reference value using an AnyInstanceRef for instance-based
    references.
    """
    def __init__(self):
        super().__init__()

        self.valueIRef = None        # type: AnyInstanceRef

    def getValueIRef(self) -> AnyInstanceRef:
        return self.valueRef

    def setValueIRef(self, value: AnyInstanceRef):
        self.valueRef = value
        return self


class EcucReferenceValue(EcucAbstractReferenceValue):
    """
    ECUC reference value using a RefType for standard references.
    """
    def __init__(self):
        super().__init__()

        self.valueRef = None        # type: RefType

    def getValueRef(self) -> RefType:
        return self.valueRef

    def setValueRef(self, value: RefType):
        self.valueRef = value
        return self


class EcucContainerValue(Identifiable, EcucIndexableValue):
    """
    Container value holding parameter values, reference values, and
    sub-containers for ECUC configuration.
    """
    def __init__(self, parent: ARObject, short_name: str):
        Identifiable.__init__(self, parent, short_name)

        self.definitionRef = None                   # type: RefType
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
    """
    ECUC module configuration values with containers, definition
    reference, and variant configuration properties.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.containers = []                        # type: List[EcucContainerValue]
        self.definitionRef = None                   # type: RefType
        self.ecucDefEdition = None                  # type: ARLiteral
        self.implementationConfigVariant = None     # type: ARLiteral
        self.moduleDescriptionRef = None            # type: RefType
        self.postBuildVariantUsed = None            # type: ARBoolean

    def createContainer(self, short_name: str) -> EcucContainerValue:
        if not self.IsElementExists(short_name):
            container = EcucContainerValue(self, short_name)
            self.addElement(container)
            self.containers.append(container)
        return self.getElement(short_name, EcucContainerValue)

    def getContainers(self) -> List[EcucContainerValue]:
        return list(sorted(filter(lambda a: isinstance(a, EcucContainerValue), self.elements), key=lambda o: o.short_name))

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
    """
    Condition specification for ECUC definitions with condition formula
    and queries.
    """
    def __init__(self):
        super().__init__()

        # self.conditionFormula: EcucConditionFormula = None     # 0..1 aggr Definition of the formula used to define existence dependencies.
        # self.ecucQueries: List[EcucQuery] = []                  # *    aggr Query to the ECU Configuration Description.
        # self.informalFormula: MlFormula = None                 # 0..1 aggr Informal description of the condition used to to define existence dependencies. # noqa E501


class EcucConfigurationVariantEnum(AREnum):
    """
    Enumeration for ECUC configuration variant types.
    """
    def __init__(self):
        super().__init__([])
