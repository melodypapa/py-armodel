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
    Boolean,
    PositiveInteger,
    RefType,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucConfigurationVariantEnum
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
    Common class to all types of configuration values.
    """

    # EcucParameterValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.49, p.125
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addAnnotation                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAnnotations               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDefinition                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefinition                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIsAutoValue               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIsAutoValue               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is EcucParameterValue:
            raise TypeError("EcucParameterValue is an abstract class.")

        super().__init__()

        # Possibility to provide additional notes while defining the ECU Configuration Parameter Values. These are not intended as documentation but are mere design notes. Tags: xml.sequenceOffset=10
        self.annotations: List[Annotation] = []

        # Reference to the definition of this EcucParameterValue subclasses in the ECU Configuration Parameter Definition. Tags: xml.sequenceOffset=-10
        self.definition: Optional[RefType] = None

        # If withAuto is set to "true" for this parameter definition the isAutoValue can be set to "true". If isAutoValue is set to "true" the actual value will not be considered during ECU Configuration but will be (re-)calculated by the code generator and stored in the value attribute afterwards. These implicit updated values might require a re-generation of other modules which reference these values. If isAutoValue is not present the default is "false". Tags: xml.sequenceOffset=20
        self.isAutoValue: Optional[Boolean] = None

    def addAnnotation(self, value: Optional[Annotation]) -> "EcucParameterValue":
        """Possibility to provide additional notes while defining the ECU Configuration Parameter Values. These are not intended as documentation but are mere design notes. Tags: xml.sequenceOffset=10 A None value is a no-op and does not append to the existing annotations."""
        if value is not None:
            self.annotations.append(value)
        return self

    def getAnnotations(self) -> List[Annotation]:
        """Possibility to provide additional notes while defining the ECU Configuration Parameter Values. These are not intended as documentation but are mere design notes. Tags: xml.sequenceOffset=10"""
        return self.annotations

    def getDefinition(self) -> Optional[RefType]:
        """Reference to the definition of this EcucParameterValue subclasses in the ECU Configuration Parameter Definition. Tags: xml.sequenceOffset=-10"""
        return self.definition

    def setDefinition(self, value: Optional[RefType]) -> "EcucParameterValue":
        """Reference to the definition of this EcucParameterValue subclasses in the ECU Configuration Parameter Definition. Tags: xml.sequenceOffset=-10 A None value is a no-op and does not overwrite an existing reference."""
        if value is not None:
            self.definition = value
        return self

    def getIsAutoValue(self) -> Optional[Boolean]:
        """If withAuto is set to "true" for this parameter definition the isAutoValue can be set to "true". If isAutoValue is set to "true" the actual value will not be considered during ECU Configuration but will be (re-)calculated by the code generator and stored in the value attribute afterwards. These implicit updated values might require a re-generation of other modules which reference these values. If isAutoValue is not present the default is "false". Tags: xml.sequenceOffset=20"""
        return self.isAutoValue

    def setIsAutoValue(self, value: Optional[Boolean]) -> "EcucParameterValue":
        """If withAuto is set to "true" for this parameter definition the isAutoValue can be set to "true". If isAutoValue is set to "true" the actual value will not be considered during ECU Configuration but will be (re-)calculated by the code generator and stored in the value attribute afterwards. These implicit updated values might require a re-generation of other modules which reference these values. If isAutoValue is not present the default is "false". Tags: xml.sequenceOffset=20 A None value is a no-op and does not overwrite an existing flag."""
        if value is not None:
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
    Head of the configuration of one Module. A Module can be a BSW module as well as the RTE and ECU Infrastructure. As part of the BSW module description, the EcucModuleConfigurationValues element has two different roles: The recommendedConfiguration contains parameter values recommended by the BSW module vendor. The preconfiguredConfiguration contains values for those parameters which are fixed by the implementation and cannot be changed. These two EcucModuleConfigurationValues are used when the base EcucModuleConfigurationValues (as part of the base ECU configuration) is created to fill parameters with initial values. Tags: atp.recommendedPackage=EcucModuleConfigurationValuess
    """

    # EcucModuleConfigurationValues method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.47, p.111
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createContainer                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getContainers                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDefinition                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefinition                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEcucDefEdition                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEcucDefEdition                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getImplementationConfigVariant   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setImplementationConfigVariant   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModuleDescription             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setModuleDescription             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPostBuildVariantUsed          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPostBuildVariantUsed          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [—] getDefinitionRef (deprecated convenience)      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [—] setDefinitionRef (deprecated convenience)      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [—] getModuleDescriptionRef (deprecated convenience)  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [—] setModuleDescriptionRef (deprecated convenience)  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [—] definitionRef property (deprecated convenience)   [x] impl  [x] docstring  [—] test  [—] reader  [—] writer
    # [—] moduleDescriptionRef property (deprecated convenience)  [x] impl  [x] docstring  [—] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Aggregates all containers that belong to this module configuration. atpVariation: [RS_ECUC_00078] Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=container.shortName, container.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=10
        self.containers: List[EcucContainerValue] = []

        # Reference to the definition of this EcucModuleConfigurationValues element. Typically, this is a vendor specific module configuration. Tags: xml.sequenceOffset=-10
        self.definition: Optional[RefType] = None

        # This is the version info of the ModuleDef ECUC Parameter definition to which this values conform to / are based on. For the Definition of ModuleDef ECUC Parameters the AdminData shall be used to express the semantic changes. The compatibility rules between the definition and value revision labels is up to the module's vendor.
        self.ecucDefEdition: Optional[RevisionLabelString] = None

        # Specifies the kind of deliverable this EcucModuleConfigurationValues element provides. If this element is not used in a particular role (e.g. preconfiguredConfiguration or recommendedConfiguration) then the value shall be one of VariantPreCompile, VariantLinkTime, VariantPostBuild.
        self.implementationConfigVariant: Optional[EcucConfigurationVariantEnum] = None

        # Referencing the BSW module description, which this EcucModuleConfigurationValues element is configuring. This is optional because the EcucModuleConfigurationValues element is also used to configure the ECU infrastructure (memory map) or Application SW-Cs. However in case the EcucModuleConfigurationValues are used to configure the module, the reference is mandatory in order to fetch module specific "common" published information.
        self.moduleDescription: Optional[RefType] = None

        # Indicates whether a module implementation has or plans to have (i.e., introduced at link or post-build time) new post-build variation points. TRUE means yes, FALSE means no. If the attribute is not defined, FALSE semantics shall be assumed.
        self.postBuildVariantUsed: Optional[Boolean] = None

    def createContainer(self, short_name: str) -> EcucContainerValue:
        """Aggregates all containers that belong to this module configuration. atpVariation: [RS_ECUC_00078] Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=container.shortName, container.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=10"""
        if not self.IsElementExists(short_name):
            container = EcucContainerValue(self, short_name)
            self.addElement(container)
            self.containers.append(container)
        return self.getElement(short_name, EcucContainerValue)

    def getContainers(self) -> List[EcucContainerValue]:
        """Aggregates all containers that belong to this module configuration. atpVariation: [RS_ECUC_00078] Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=container.shortName, container.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=10"""
        return list(sorted(self.containers, key=lambda o: o.short_name))

    def getDefinition(self) -> Optional[RefType]:
        """Reference to the definition of this EcucModuleConfigurationValues element. Typically, this is a vendor specific module configuration. Tags: xml.sequenceOffset=-10"""
        return self.definition

    def setDefinition(self, value: RefType) -> "EcucModuleConfigurationValues":
        """Reference to the definition of this EcucModuleConfigurationValues element. Typically, this is a vendor specific module configuration. Tags: xml.sequenceOffset=-10 A None value is a no-op and does not overwrite an existing reference."""
        if value is not None:
            self.definition = value
        return self

    def getEcucDefEdition(self) -> Optional[RevisionLabelString]:
        """This is the version info of the ModuleDef ECUC Parameter definition to which this values conform to / are based on. For the Definition of ModuleDef ECUC Parameters the AdminData shall be used to express the semantic changes. The compatibility rules between the definition and value revision labels is up to the module's vendor."""
        return self.ecucDefEdition

    def setEcucDefEdition(self, value: RevisionLabelString) -> "EcucModuleConfigurationValues":
        """This is the version info of the ModuleDef ECUC Parameter definition to which this values conform to / are based on. For the Definition of ModuleDef ECUC Parameters the AdminData shall be used to express the semantic changes. The compatibility rules between the definition and value revision labels is up to the module's vendor. A None value is a no-op and does not overwrite an existing version info."""
        if value is not None:
            self.ecucDefEdition = value
        return self

    def getImplementationConfigVariant(self) -> Optional[EcucConfigurationVariantEnum]:
        """Specifies the kind of deliverable this EcucModuleConfigurationValues element provides. If this element is not used in a particular role (e.g. preconfiguredConfiguration or recommendedConfiguration) then the value shall be one of VariantPreCompile, VariantLinkTime, VariantPostBuild."""
        return self.implementationConfigVariant

    def setImplementationConfigVariant(self, value: EcucConfigurationVariantEnum) -> "EcucModuleConfigurationValues":
        """Specifies the kind of deliverable this EcucModuleConfigurationValues element provides. If this element is not used in a particular role (e.g. preconfiguredConfiguration or recommendedConfiguration) then the value shall be one of VariantPreCompile, VariantLinkTime, VariantPostBuild. A None value is a no-op and does not overwrite an existing configuration variant."""
        if value is not None:
            self.implementationConfigVariant = value
        return self

    def getModuleDescription(self) -> Optional[RefType]:
        """Referencing the BSW module description, which this EcucModuleConfigurationValues element is configuring. This is optional because the EcucModuleConfigurationValues element is also used to configure the ECU infrastructure (memory map) or Application SW-Cs. However in case the EcucModuleConfigurationValues are used to configure the module, the reference is mandatory in order to fetch module specific "common" published information."""
        return self.moduleDescription

    def setModuleDescription(self, value: RefType) -> "EcucModuleConfigurationValues":
        """Referencing the BSW module description, which this EcucModuleConfigurationValues element is configuring. This is optional because the EcucModuleConfigurationValues element is also used to configure the ECU infrastructure (memory map) or Application SW-Cs. However in case the EcucModuleConfigurationValues are used to configure the module, the reference is mandatory in order to fetch module specific "common" published information. A None value is a no-op and does not overwrite an existing reference."""
        if value is not None:
            self.moduleDescription = value
        return self

    def getPostBuildVariantUsed(self) -> Optional[Boolean]:
        """Indicates whether a module implementation has or plans to have (i.e., introduced at link or post-build time) new post-build variation points. TRUE means yes, FALSE means no. If the attribute is not defined, FALSE semantics shall be assumed."""
        return self.postBuildVariantUsed

    def setPostBuildVariantUsed(self, value: Boolean) -> "EcucModuleConfigurationValues":
        """Indicates whether a module implementation has or plans to have (i.e., introduced at link or post-build time) new post-build variation points. TRUE means yes, FALSE means no. If the attribute is not defined, FALSE semantics shall be assumed. A None value is a no-op and does not overwrite an existing flag."""
        if value is not None:
            self.postBuildVariantUsed = value
        return self

    # Backward compatibility aliases (deprecated - use definition/moduleDescription instead)
    def getDefinitionRef(self) -> Optional[RefType]:
        """Deprecated: use getDefinition() instead."""
        return self.definition

    def setDefinitionRef(self, value: RefType):
        """Deprecated: use setDefinition() instead."""
        self.definition = value
        return self

    def getModuleDescriptionRef(self) -> Optional[RefType]:
        """Deprecated: use getModuleDescription() instead."""
        return self.moduleDescription

    def setModuleDescriptionRef(self, value: RefType):
        """Deprecated: use setModuleDescription() instead."""
        self.moduleDescription = value
        return self

    # Backward compatibility properties (deprecated)
    @property
    def definitionRef(self) -> Optional[RefType]:
        """Deprecated: use definition instead."""
        return self.definition

    @definitionRef.setter
    def definitionRef(self, value: Optional[RefType]):
        """Deprecated: use definition instead."""
        self.definition = value

    @property
    def moduleDescriptionRef(self) -> Optional[RefType]:
        """Deprecated: use moduleDescription instead."""
        return self.moduleDescription

    @moduleDescriptionRef.setter
    def moduleDescriptionRef(self, value: Optional[RefType]):
        """Deprecated: use moduleDescription instead."""
        self.moduleDescription = value


# EcucConfigurationVariantEnum lives in ECUCParameterDefTemplate.py
# (canonical, # Spec verified: R23-11 — AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.13, p.53).
# The duplicate stub that used to sit here was removed; import it from
# armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate when needed.
