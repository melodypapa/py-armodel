from abc import ABC
from typing import List, Optional

from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    ARLiteral,
    ARNumerical,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable


class EcucValueCollection(ARElement):
    """
    Collection of ECUC values with references to ECU extract.
    """

    # EcucValueCollection method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEcucValueRefs             [x] impl  [ ] docstring  [ ] test
    # [ ] addEcucValueRef              [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuExtractRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setEcuExtractRef             [x] impl  [ ] docstring  [ ] test

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
    Used to support the specification of ordering of parameter values.
    """

    # EcucIndexableValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.46, p.110
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIndex                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIndex                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is EcucIndexableValue:
            raise TypeError("EcucIndexableValue is an abstract class.")

        super().__init__()

        # Used to support the specification of ordering of parameter values. Tags: xml.sequenceOffset=-5
        self.index: Optional[PositiveInteger] = None

    def getIndex(self) -> Optional[PositiveInteger]:
        """
        Used to support the specification of ordering of parameter values.
        """
        return self.index

    def setIndex(self, value: Optional[PositiveInteger]) -> "EcucIndexableValue":
        """
        Used to support the specification of ordering of parameter values.

        A None value is a no-op and does not overwrite an existing index.
        """
        if value is not None:
            self.index = value
        return self


class EcucParameterValue(EcucIndexableValue, ABC):
    """
    Abstract base class for ECUC parameter values with annotation,
    definition reference, and auto value flag.
    """

    # EcucParameterValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAnnotations               [x] impl  [ ] docstring  [ ] test
    # [ ] addAnnotation                [x] impl  [ ] docstring  [ ] test
    # [ ] getDefinitionRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setDefinitionRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getIsAutoValue               [x] impl  [ ] docstring  [ ] test
    # [ ] setIsAutoValue               [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is EcucParameterValue:
            raise TypeError("EcucParameterValue is an abstract class.")

        super().__init__()

        self.annotations = []  # type: List[Annotation]
        self.definitionRef = None  # type: RefType
        self.isAutoValue = None  # type: ARBoolean

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

    # EcucAddInfoParamValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getValue                     [x] impl  [ ] docstring  [ ] test
    # [ ] setValue                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.value = None  # type: DocumentationBlock

    def getValue(self) -> DocumentationBlock:
        return self.value

    def setValue(self, value: DocumentationBlock):
        self.value = value


class EcucTextualParamValue(EcucParameterValue):
    """
    ECUC parameter value for textual string values.
    """

    # EcucTextualParamValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getValue                     [x] impl  [ ] docstring  [ ] test
    # [ ] setValue                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.value = None  # type: ARLiteral

    def getValue(self) -> ARLiteral:
        return self.value

    def setValue(self, value: ARLiteral):
        self.value = value


class EcucNumericalParamValue(EcucParameterValue):
    """
    ECUC parameter value for numerical values.
    """

    # EcucNumericalParamValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getValue                     [x] impl  [ ] docstring  [ ] test
    # [ ] setValue                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.value = None  # type: ARNumerical

    def getValue(self) -> ARNumerical:
        return self.value

    def setValue(self, value: ARNumerical):
        self.value = value


class EcucAbstractReferenceValue(EcucIndexableValue, ABC):
    """
    Abstract base class for ECUC reference values with annotation,
    definition reference, and auto value flag.
    """

    # EcucAbstractReferenceValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAnnotations               [x] impl  [ ] docstring  [ ] test
    # [ ] addAnnotation                [x] impl  [ ] docstring  [ ] test
    # [ ] getDefinitionRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setDefinitionRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getIsAutoValue               [x] impl  [ ] docstring  [ ] test
    # [ ] setIsAutoValue               [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is EcucAbstractReferenceValue:
            raise TypeError("EcucAbstractReferenceValue is an abstract class.")

        super().__init__()

        self.annotations = []  # type: List[Annotation]
        self.definitionRef = None  # type: RefType
        self.isAutoValue = None  # type: ARBoolean

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

    # EcucInstanceReferenceValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getValueIRef                 [x] impl  [ ] docstring  [ ] test
    # [ ] setValueIRef                 [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.valueIRef = None  # type: AnyInstanceRef

    def getValueIRef(self) -> AnyInstanceRef:
        return self.valueRef

    def setValueIRef(self, value: AnyInstanceRef):
        self.valueRef = value
        return self


class EcucReferenceValue(EcucAbstractReferenceValue):
    """
    ECUC reference value using a RefType for standard references.
    """

    # EcucReferenceValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getValueRef                  [x] impl  [ ] docstring  [ ] test
    # [ ] setValueRef                  [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.valueRef = None  # type: RefType

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

    # EcucContainerValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDefinitionRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setDefinitionRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getParameterValues           [x] impl  [ ] docstring  [ ] test
    # [ ] addParameterValue            [x] impl  [ ] docstring  [ ] test
    # [ ] getReferenceValues           [x] impl  [ ] docstring  [ ] test
    # [ ] addReferenceValue            [x] impl  [ ] docstring  [ ] test
    # [ ] getSubContainers             [x] impl  [ ] docstring  [ ] test
    # [ ] createSubContainer           [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        EcucIndexableValue.__init__(self)
        Identifiable.__init__(self, parent, short_name)

        self.definitionRef = None  # type: RefType
        self.parameterValues = []  # type: List[EcucParameterValue]
        self.referenceValues = []  # type: List[EcucAbstractReferenceValue]
        self.subContainers = []  # type: List[EcucContainerValue]

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

    # EcucModuleConfigurationValues method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.47, p.111
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                         [x] impl  [ ] docstring  [x] test  [—] reader  [—] writer
    # [x] createContainer                  [x] impl  [ ] docstring  [x] test  [—] reader  [x] writer
    # [x] getContainers                    [x] impl  [ ] docstring  [x] test  [x] reader  [—] writer
    # [x] getDefinitionRef                 [x] impl  [ ] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefinitionRef                 [x] impl  [ ] docstring  [x] test  [x] reader  [—] writer
    # [x] getEcucDefEdition                [x] impl  [ ] docstring  [x] test  [—] reader  [x] writer
    # [x] setEcucDefEdition                [x] impl  [ ] docstring  [x] test  [x] reader  [—] writer
    # [x] getImplementationConfigVariant   [x] impl  [ ] docstring  [x] test  [—] reader  [x] writer
    # [x] setImplementationConfigVariant   [x] impl  [ ] docstring  [x] test  [x] reader  [—] writer
    # [x] getModuleDescriptionRef          [x] impl  [ ] docstring  [x] test  [—] reader  [x] writer
    # [x] setModuleDescriptionRef          [x] impl  [ ] docstring  [x] test  [x] reader  [—] writer
    # [x] getPostBuildVariantUsed          [x] impl  [ ] docstring  [x] test  [—] reader  [x] writer
    # [x] setPostBuildVariantUsed          [x] impl  [ ] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.containers: List[EcucContainerValue] = []
        self.definitionRef: Optional[RefType] = None
        self.ecucDefEdition: Optional[ARLiteral] = None
        self.implementationConfigVariant: Optional[ARLiteral] = None
        self.moduleDescriptionRef: Optional[RefType] = None
        self.postBuildVariantUsed: Optional[ARBoolean] = None

    def createContainer(self, short_name: str) -> EcucContainerValue:
        if not self.IsElementExists(short_name):
            container = EcucContainerValue(self, short_name)
            self.addElement(container)
            self.containers.append(container)
        return self.getElement(short_name, EcucContainerValue)

    def getContainers(self) -> List[EcucContainerValue]:
        return list(sorted(filter(lambda a: isinstance(a, EcucContainerValue), self.elements), key=lambda o: o.short_name))

    def getDefinitionRef(self) -> Optional[RefType]:
        return self.definitionRef

    def setDefinitionRef(self, value: RefType):
        self.definitionRef = value
        return self

    def getEcucDefEdition(self) -> Optional[ARLiteral]:
        return self.ecucDefEdition

    def setEcucDefEdition(self, value: ARLiteral):
        self.ecucDefEdition = value
        return self

    def getImplementationConfigVariant(self) -> Optional[ARLiteral]:
        return self.implementationConfigVariant

    def setImplementationConfigVariant(self, value: ARLiteral):
        self.implementationConfigVariant = value
        return self

    def getModuleDescriptionRef(self) -> Optional[RefType]:
        return self.moduleDescriptionRef

    def setModuleDescriptionRef(self, value: RefType):
        self.moduleDescriptionRef = value
        return self

    def getPostBuildVariantUsed(self) -> Optional[ARBoolean]:
        return self.postBuildVariantUsed

    def setPostBuildVariantUsed(self, value: ARBoolean):
        self.postBuildVariantUsed = value
        return self


# EcucConfigurationVariantEnum lives in ECUCParameterDefTemplate.py
# (canonical, # Spec verified: R23-11 — AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.13, p.53).
# The duplicate stub that used to sit here was removed; import it from
# armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate when needed.
