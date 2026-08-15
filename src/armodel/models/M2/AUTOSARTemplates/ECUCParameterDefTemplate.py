from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, CIdentifier, Float, Identifier, Limit
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, UnlimitedInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RegularExpression, String, VerbatimString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import MlFormula


class EcucConditionSpecification(ARObject):
    """
    Allows to define existence dependencies based on the value of parameter
    values.
    """

    # EcucConditionSpecification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.42, p.100
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getConditionFormula          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setConditionFormula          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQueries               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createEcucQuery              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQuery                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getInformalFormula           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setInformalFormula           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The condition that shall be evaluated to infer whether the existence dependency holds.
        self.conditionFormula: Optional[EcucConditionFormula] = None

        # The EcucQuery executed to evaluate the existence dependency.
        self.ecucQueries: List[EcucQuery] = []

        # The informal specification of the existence dependency.
        self.informalFormula: Optional[MlFormula] = None

    def getConditionFormula(self) -> Optional["EcucConditionFormula"]:
        """
        Gets the condition that shall be evaluated to infer whether the existence dependency holds.
        """
        return self.conditionFormula

    def setConditionFormula(self, value: "EcucConditionFormula") -> "EcucConditionSpecification":
        """
        Sets the condition that shall be evaluated to infer whether the existence dependency holds.
        A None value is a no-op.
        """
        if value is not None:
            self.conditionFormula = value
        return self

    def getEcucQueries(self) -> List["EcucQuery"]:
        """
        Gets the EcucQueries executed to evaluate the existence dependency.
        """
        return self.ecucQueries

    def createEcucQuery(self, short_name: str) -> Optional["EcucQuery"]:
        """
        Creates or returns an existing EcucQuery aggregated by this condition specification.
        """
        if short_name is None:
            return None
        for query in self.ecucQueries:
            if query.getShortName() == short_name:
                return query
        query = EcucQuery(self, short_name)
        self.ecucQueries.append(query)
        return query

    def getEcucQuery(self, short_name: str) -> Optional["EcucQuery"]:
        """
        Gets the EcucQuery with the given short name, or None if not present.
        """
        for query in self.ecucQueries:
            if query.getShortName() == short_name:
                return query
        return None

    def getInformalFormula(self) -> Optional[MlFormula]:
        """
        Gets the informal specification of the existence dependency.
        """
        return self.informalFormula

    def setInformalFormula(self, value: MlFormula) -> "EcucConditionSpecification":
        """
        Sets the informal specification of the existence dependency.
        A None value is a no-op.
        """
        if value is not None:
            self.informalFormula = value
        return self


class EcucValidationCondition(Identifiable):
    """
    Validation condition to perform a formula calculation based on EcucQueries.
    """

    # EcucValidationCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.44, p.103
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQueries               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createEcucQuery              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQuery                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getValidationFormula         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setValidationFormula         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The EcucQuery used to validate the Ecuc configuration.
        self.ecucQueries: List["EcucQuery"] = []

        # The validation condition applied to the Ecuc configuration.
        self.validationFormula: Optional["EcucConditionFormula"] = None

    def getEcucQueries(self) -> List["EcucQuery"]:
        """
        Gets the EcucQueries used to validate the Ecuc configuration.
        """
        return self.ecucQueries

    def createEcucQuery(self, short_name: str) -> Optional["EcucQuery"]:
        """
        Creates or returns an existing EcucQuery aggregated by this validation condition.
        """
        if short_name is None:
            return None
        for query in self.ecucQueries:
            if query.getShortName() == short_name:
                return query
        query = EcucQuery(self, short_name)
        self.ecucQueries.append(query)
        return query

    def getEcucQuery(self, short_name: str) -> Optional["EcucQuery"]:
        """
        Gets the EcucQuery with the given short name, or None if not present.
        """
        for query in self.ecucQueries:
            if query.getShortName() == short_name:
                return query
        return None

    def getValidationFormula(self) -> Optional["EcucConditionFormula"]:
        """
        Gets the validation condition applied to the Ecuc configuration.
        """
        return self.validationFormula

    def setValidationFormula(self, value: "EcucConditionFormula") -> "EcucValidationCondition":
        """
        Sets the validation condition applied to the Ecuc configuration.
        A None value is a no-op.
        """
        if value is not None:
            self.validationFormula = value
        return self


class EcucScopeEnum(AREnum):
    """
    Possible scope settings for a configuration element.
    """

    # EcucScopeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.7, p.46
    # (no methods)

    # An element may be shared with other modules. Tags: atp.EnumerationLiteralIndex=0
    ECU = "ECU"

    # An element is only be applicable for the module it is defined in. Tags: atp.EnumerationLiteralIndex=1
    LOCAL = "LOCAL"

    def __init__(self):
        super().__init__(
            [
                EcucScopeEnum.ECU,
                EcucScopeEnum.LOCAL,
            ]
        )


class EcucDefinitionElement(Identifiable, ABC):
    """
    Common class used to express the commonalities of configuration parameters, references and containers. If not stated otherwise the default multiplicity is exactly one mandatory instance per definition.
    """

    # EcucDefinitionElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.6, p.46
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucCond                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setEcucCond                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucValidationConds       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addEcucValidationCond        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLowerMultiplicity         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLowerMultiplicity         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRelatedTraceItemRef       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setRelatedTraceItemRef       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getScope                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setScope                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUpperMultiplicity         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpperMultiplicity         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUpperMultiplicityInfinite [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setUpperMultiplicityInfinite [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is EcucDefinitionElement:
            raise TypeError("EcucDefinitionElement is an abstract class.")
        super().__init__(parent, short_name)

        self.ecucCond: EcucConditionSpecification = None
        self.ecucValidationConds: List[EcucValidationCondition] = []
        self.lowerMultiplicity: PositiveInteger = None
        self.relatedTraceItemRef: RefType = None
        self.scope: EcucScopeEnum = None
        self.upperMultiplicity: PositiveInteger = None
        self.upperMultiplicityInfinite: Boolean = None

    def getEcucCond(self) -> EcucConditionSpecification:
        return self.ecucCond

    def setEcucCond(self, value: EcucConditionSpecification):
        if value is not None:
            self.ecucCond = value
        return self

    def getEcucValidationConds(self) -> List[EcucValidationCondition]:
        return self.ecucValidationConds

    def addEcucValidationCond(self, value: EcucValidationCondition):
        if value is not None:
            self.ecucValidationConds.append(value)
        return self

    def getLowerMultiplicity(self) -> PositiveInteger:
        return self.lowerMultiplicity

    def setLowerMultiplicity(self, value: PositiveInteger):
        if value is not None:
            self.lowerMultiplicity = value
        return self

    def getRelatedTraceItemRef(self) -> RefType:
        return self.relatedTraceItemRef

    def setRelatedTraceItemRef(self, value: RefType):
        if value is not None:
            self.relatedTraceItemRef = value
        return self

    def getScope(self) -> EcucScopeEnum:
        return self.scope

    def setScope(self, value: EcucScopeEnum):
        if value is not None:
            self.scope = value
        return self

    def getUpperMultiplicity(self) -> PositiveInteger:
        return self.upperMultiplicity

    def setUpperMultiplicity(self, value: PositiveInteger):
        if value is not None:
            self.upperMultiplicity = value
        return self

    def getUpperMultiplicityInfinite(self) -> Boolean:
        return self.upperMultiplicityInfinite

    def setUpperMultiplicityInfinite(self, value: Boolean):
        if value is not None:
            self.upperMultiplicityInfinite = value
        return self


class EcucDestinationUriDefRefType(RefType):
    """
    EcucDestinationUriDefRefType is a class that represents a reference type
    specific to ECUC Destination URI definitions.

    This class inherits from the `RefType` base class and is used to define
    references to ECUC Destination URI definitions in the AUTOSAR model.
    """

    # EcucDestinationUriDefRefType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test

    def __init__(self):
        super().__init__()


class EcucConfigurationClassEnum(AREnum):
    """
    Possible configuration classes for the AUTOSAR configuration parameters.
    """

    # EcucConfigurationClassEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.12, p.52
    # (no methods)

    # Link Time: parts of configuration are delivered from another object code file Tags: atp.EnumerationLiteralIndex=0
    LINK = "LINK"

    # PostBuildTime: after compilation a configuration parameter can be changed. Tags: atp.EnumerationLiteralIndex=1
    POST_BUILD = "POST-BUILD"

    # PreCompile Time: after compilation a configuration parameter can not be changed any more. Tags: atp.EnumerationLiteralIndex=2
    PRE_COMPILE = "PRE-COMPILE"

    # PublishedInformation is used to specify the fact that certain information is fixed even before the pre-compile stage. Tags: atp.EnumerationLiteralIndex=3
    PUBLISHED_INFORMATION = "PUBLISHED-INFORMATION"

    def __init__(self):
        super().__init__(
            [
                EcucConfigurationClassEnum.LINK,
                EcucConfigurationClassEnum.POST_BUILD,
                EcucConfigurationClassEnum.PRE_COMPILE,
                EcucConfigurationClassEnum.PUBLISHED_INFORMATION,
            ]
        )


class EcucConfigurationVariantEnum(AREnum):
    """
    Specifies which ConfigurationVariants are supported by this software module.
    """

    # EcucConfigurationVariantEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.13, p.53
    # Spec verified: R23-11
    # (no methods)

    # Recommended configuration for a module. Tags: atp.EnumerationLiteralIndex=1
    RECOMMENDED_CONFIGURATION = "RECOMMENDED-CONFIGURATION"

    # Specifies that the BSW Module implementation may use PreCompileTime and LinkTime configuration parameters. Tags: atp.EnumerationLiteralIndex=2
    VARIANT_LINK_TIME = "VARIANT-LINK-TIME"

    # Specifies that the BSW Module implementation may use PreCompileTime, LinkTime and PostBuild configuration parameters. Tags: atp.EnumerationLiteralIndex=3
    VARIANT_POST_BUILD = "VARIANT-POST-BUILD"

    # Specifies that the BSW Module implementation uses only PreCompileTime configuration parameters. Tags: atp.EnumerationLiteralIndex=6
    VARIANT_PRE_COMPILE = "VARIANT-PRE-COMPILE"

    def __init__(self):
        super().__init__(
            [
                EcucConfigurationVariantEnum.RECOMMENDED_CONFIGURATION,
                EcucConfigurationVariantEnum.VARIANT_LINK_TIME,
                EcucConfigurationVariantEnum.VARIANT_POST_BUILD,
                EcucConfigurationVariantEnum.VARIANT_PRE_COMPILE,
            ]
        )


class EcucAbstractConfigurationClass(ARObject, ABC):
    """
    Specifies the ValueConfigurationClass of a parameter/reference or the MultiplicityConfigurationClass of a parameter/reference or a container for each ConfigurationVariant of the EcucModuleDef.
    """

    # EcucAbstractConfigurationClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.9, p.51
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getConfigClass               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConfigClass               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConfigVariant             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConfigVariant             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is EcucAbstractConfigurationClass:
            raise TypeError("EcucAbstractConfigurationClass is an abstract class.")
        super().__init__()

        self.configClass: EcucConfigurationClassEnum = None
        self.configVariant: EcucConfigurationVariantEnum = None

    def getConfigClass(self) -> EcucConfigurationClassEnum:
        return self.configClass

    def setConfigClass(self, value: EcucConfigurationClassEnum):
        if value is not None:
            self.configClass = value
        return self

    def getConfigVariant(self) -> EcucConfigurationVariantEnum:
        return self.configVariant

    def setConfigVariant(self, value: EcucConfigurationVariantEnum):
        if value is not None:
            self.configVariant = value
        return self


class EcucMultiplicityConfigurationClass(EcucAbstractConfigurationClass):
    """
    Specifies the MultiplicityConfigurationClass of a parameter/reference or a container for each ConfigurationVariant of the EcucModuleDef.
    """

    # EcucMultiplicityConfigurationClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.11, p.52
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class EcucContainerDef(EcucDefinitionElement, ABC):
    """
    Base class used to gather common attributes of configuration container definitions.
    """

    # EcucContainerDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.3, p.37
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationUriRef         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setDestinationUriRef         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMultiplicityConfigClasses [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addMultiplicityConfigClass   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOrigin                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setOrigin                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPostBuildVariantMultiplicity [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPostBuildVariantMultiplicity [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRequiresIndex             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRequiresIndex             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is EcucContainerDef:
            raise TypeError("EcucContainerDef is an abstract class.")
        super().__init__(parent, short_name)

        self.destinationUriRef: EcucDestinationUriDefRefType = None
        self.multiplicityConfigClasses: List[EcucMultiplicityConfigurationClass] = []
        self.origin: String = None
        self.postBuildVariantMultiplicity: Boolean = None
        self.requiresIndex: Boolean = None

    def getDestinationUriRef(self) -> EcucDestinationUriDefRefType:
        return self.destinationUriRef

    def setDestinationUriRef(self, value: EcucDestinationUriDefRefType):
        if value is not None:
            self.destinationUriRef = value
        return self

    def getMultiplicityConfigClasses(self) -> List[EcucMultiplicityConfigurationClass]:
        return self.multiplicityConfigClasses

    def addMultiplicityConfigClass(self, value: EcucMultiplicityConfigurationClass):
        if value is not None:
            self.multiplicityConfigClasses.append(value)
        return self

    def getOrigin(self) -> String:
        return self.origin

    def setOrigin(self, value: String):
        if value is not None:
            self.origin = value
        return self

    def getPostBuildVariantMultiplicity(self) -> Boolean:
        return self.postBuildVariantMultiplicity

    def setPostBuildVariantMultiplicity(self, value: Boolean):
        if value is not None:
            self.postBuildVariantMultiplicity = value
        return self

    def getRequiresIndex(self) -> Boolean:
        return self.requiresIndex

    def setRequiresIndex(self, value: Boolean):
        if value is not None:
            self.requiresIndex = value
        return self


class EcucValueConfigurationClass(EcucAbstractConfigurationClass):
    """
    Specifies the ValueConfigurationClass of a parameter/reference for each ConfigurationVariant of the EcucModuleDef.
    """

    # EcucValueConfigurationClass method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.10, p.52
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class EcucCommonAttributes(EcucDefinitionElement, ABC):
    """
    Attributes used by Configuration Parameters as well as References.
    """

    # EcucCommonAttributes method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.8, p.49
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMultiplicityConfigClasses [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addMultiplicityConfigClass   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOrigin                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOrigin                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPostBuildVariantMultiplicity [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPostBuildVariantMultiplicity [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPostBuildVariantValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPostBuildVariantValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRequiresIndex             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRequiresIndex             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValueConfigClasses        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addValueConfigClass          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is EcucCommonAttributes:
            raise TypeError("Cannot instantiate abstract class EcucCommonAttributes")

        super().__init__(parent, short_name)

        self.multiplicityConfigClasses: List[EcucMultiplicityConfigurationClass] = []
        self.origin: String = None
        self.postBuildVariantMultiplicity: Boolean = None
        self.postBuildVariantValue: Boolean = None
        self.requiresIndex: Boolean = None
        self.valueConfigClasses: List[EcucValueConfigurationClass] = []

    def getMultiplicityConfigClasses(self) -> List[EcucMultiplicityConfigurationClass]:
        return self.multiplicityConfigClasses

    def addMultiplicityConfigClass(self, value: EcucMultiplicityConfigurationClass):
        if value is not None:
            self.multiplicityConfigClasses.append(value)
        return self

    def getOrigin(self) -> String:
        return self.origin

    def setOrigin(self, value: String):
        if value is not None:
            self.origin = value
        return self

    def getPostBuildVariantMultiplicity(self) -> Boolean:
        return self.postBuildVariantMultiplicity

    def setPostBuildVariantMultiplicity(self, value: Boolean):
        if value is not None:
            self.postBuildVariantMultiplicity = value
        return self

    def getPostBuildVariantValue(self) -> Boolean:
        return self.postBuildVariantValue

    def setPostBuildVariantValue(self, value: Boolean):
        if value is not None:
            self.postBuildVariantValue = value
        return self

    def getRequiresIndex(self) -> Boolean:
        return self.requiresIndex

    def setRequiresIndex(self, value: Boolean):
        if value is not None:
            self.requiresIndex = value
        return self

    def getValueConfigClasses(self) -> List[EcucValueConfigurationClass]:
        return self.valueConfigClasses

    def addValueConfigClass(self, value: EcucValueConfigurationClass):
        if value is not None:
            self.valueConfigClasses.append(value)
        return self


class EcucDerivationSpecification(ARObject):
    """
    Allows to define configuration items that are calculated based on the value of
    other parameter values, or of elements (attributes/classes) defined in other
    AUTOSAR templates such as System template and SW component template.
    """

    # EcucDerivationSpecification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.38, p.87
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCalculationFormula        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setCalculationFormula        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQueries               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createEcucQuery              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQuery                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getInformalFormula           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setInformalFormula           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Definition of the formula used to calculate the value of the configuration element.
        self.calculationFormula: Optional["EcucParameterDerivationFormula"] = None

        # Query to the ECU Configuration Description.
        self.ecucQueries: List["EcucQuery"] = []

        # Informal description of the derivation used to calculate the value of the configuration element.
        self.informalFormula: Optional[MlFormula] = None

    def getCalculationFormula(self) -> Optional["EcucParameterDerivationFormula"]:
        """
        Gets the formula used to calculate the value of the configuration element.
        """
        return self.calculationFormula

    def setCalculationFormula(self, value: "EcucParameterDerivationFormula") -> "EcucDerivationSpecification":
        """
        Sets the formula used to calculate the value of the configuration element.
        A None value is a no-op.
        """
        if value is not None:
            self.calculationFormula = value
        return self

    def getEcucQueries(self) -> List["EcucQuery"]:
        """
        Gets the queries to the ECU Configuration Description.
        """
        return self.ecucQueries

    def createEcucQuery(self, short_name: str) -> Optional["EcucQuery"]:
        """
        Creates or returns an existing EcucQuery aggregated by this derivation specification.
        """
        if short_name is None:
            return None
        for query in self.ecucQueries:
            if query.getShortName() == short_name:
                return query
        query = EcucQuery(self, short_name)
        self.ecucQueries.append(query)
        return query

    def getEcucQuery(self, short_name: str) -> Optional["EcucQuery"]:
        """
        Gets the EcucQuery with the given short name, or None if not present.
        """
        for query in self.ecucQueries:
            if query.getShortName() == short_name:
                return query
        return None

    def getInformalFormula(self) -> Optional[MlFormula]:
        """
        Gets the informal description of the derivation.
        """
        return self.informalFormula

    def setInformalFormula(self, value: MlFormula) -> "EcucDerivationSpecification":
        """
        Sets the informal description of the derivation.
        A None value is a no-op.
        """
        if value is not None:
            self.informalFormula = value
        return self


class EcucParameterDef(EcucCommonAttributes, ABC):
    """
    Abstract class used to define the similarities of all ECU Configuration Parameter types defined as subclasses.
    """

    # EcucParameterDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.14, p.57
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDerivation                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDerivation                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSymbolicNameValue         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSymbolicNameValue         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWithAuto                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWithAuto                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is EcucParameterDef:
            raise TypeError("EcucParameterDef is an abstract class.")
        super().__init__(parent, short_name)

        self.derivation: EcucDerivationSpecification = None
        self.symbolicNameValue: Boolean = None
        self.withAuto: Boolean = None

    def getDerivation(self) -> EcucDerivationSpecification:
        return self.derivation

    def setDerivation(self, value: EcucDerivationSpecification):
        if value is not None:
            self.derivation = value
        return self

    def getSymbolicNameValue(self) -> Boolean:
        return self.symbolicNameValue

    def setSymbolicNameValue(self, value: Boolean):
        if value is not None:
            self.symbolicNameValue = value
        return self

    def getWithAuto(self) -> Boolean:
        return self.withAuto

    def setWithAuto(self, value: Boolean):
        if value is not None:
            self.withAuto = value
        return self


class EcucBooleanParamDef(EcucParameterDef):
    """
    Configuration parameter type for Boolean. Allowed values are true and false.
    """

    # EcucBooleanParamDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.15, p.58
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDefaultValue              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultValue              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.defaultValue: Boolean = None

    def getDefaultValue(self) -> Boolean:
        return self.defaultValue

    def setDefaultValue(self, value: Boolean):
        if value is not None:
            self.defaultValue = value
        return self


class EcucAbstractReferenceDef(EcucCommonAttributes, ABC):
    """
    Common class to gather the attributes for the definition of references.
    """

    # EcucAbstractReferenceDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.26, p.71
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent, short_name):
        if type(self) is EcucAbstractReferenceDef:
            raise TypeError("Cannot instantiate abstract class EcucAbstractReferenceDef")

        super().__init__(parent, short_name)


class EcucAbstractInternalReferenceDef(EcucAbstractReferenceDef, ABC):
    """
    Common abstract class to gather attributes for internal references (where
    the destination is located in the Ecu Configuration Description).
    """

    # EcucAbstractInternalReferenceDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.27, p.72
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRequiresSymbolicNameValue [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRequiresSymbolicNameValue [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        if type(self) is EcucAbstractInternalReferenceDef:
            raise TypeError("Cannot instantiate abstract class EcucAbstractInternalReferenceDef")
        super().__init__(parent, short_name)

        # If this attribute is set to true the implementation of the reference is done using a Symbolic Name defined by the referenced container.
        self.requiresSymbolicNameValue: Boolean = None

    def getRequiresSymbolicNameValue(self) -> Boolean:
        """
        Gets whether the implementation of the reference is done using a Symbolic Name.
        """
        return self.requiresSymbolicNameValue

    def setRequiresSymbolicNameValue(self, value: Boolean) -> "EcucAbstractInternalReferenceDef":
        """
        Sets whether the implementation of the reference is done using a Symbolic Name.
        A None value is a no-op.
        """
        if value is not None:
            self.requiresSymbolicNameValue = value
        return self


class EcucAbstractExternalReferenceDef(EcucAbstractReferenceDef, ABC):
    """
    Common abstract class to gather attributes for external references (where the
    destination is not located in the ECU Configuration Description but in an
    another AUTOSAR Template).
    """

    # EcucAbstractExternalReferenceDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.28, p.72
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent, short_name):
        if type(self) is EcucAbstractExternalReferenceDef:
            raise TypeError("Cannot instantiate abstract class EcucAbstractExternalReferenceDef")

        super().__init__(parent, short_name)


class EcucSymbolicNameReferenceDef(EcucAbstractInternalReferenceDef):
    """
    ECUC reference definition using symbolic names with a destination reference.
    """

    # EcucSymbolicNameReferenceDef method parity checklist:
    # (legacy class, removed in R23-11; no spec table)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDestinationRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationRef: RefType = None

    def getDestinationRef(self) -> RefType:
        """
        Gets the reference to a parameter container.
        """
        return self.destinationRef

    def setDestinationRef(self, value: RefType) -> "EcucSymbolicNameReferenceDef":
        """
        Sets the reference to a parameter container.
        A None value is a no-op.
        """
        if value is not None:
            self.destinationRef = value
        return self


class EcucChoiceReferenceDef(EcucAbstractInternalReferenceDef):
    """
    Specify alternative references where in the ECU Configuration description
    only one of the specified references will actually be used.
    """

    # EcucChoiceReferenceDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.30, p.74
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationRefs           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addDestinationRef            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # All the possible parameter containers for the reference are specified.
        self.destinationRefs: List[RefType] = []

    def getDestinationRefs(self) -> List[RefType]:
        """
        Gets all the possible parameter containers for the reference.
        """
        return self.destinationRefs

    def addDestinationRef(self, value: RefType) -> "EcucChoiceReferenceDef":
        """
        Adds a possible parameter container for the reference.
        A None value is a no-op.
        """
        if value is not None:
            self.destinationRefs.append(value)
        return self


class EcucReferenceDef(EcucAbstractInternalReferenceDef):
    """
    Specify references within the ECU Configuration Description between parameter
    containers.
    """

    # EcucReferenceDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.29, p.73
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDestinationRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Exactly one reference to a parameter container is allowed as destination.
        self.destinationRef: RefType = None

    def getDestinationRef(self) -> RefType:
        """
        Gets the reference to a parameter container.
        """
        return self.destinationRef

    def setDestinationRef(self, value: RefType) -> "EcucReferenceDef":
        """
        Sets the reference to a parameter container.
        A None value is a no-op.
        """
        if value is not None:
            self.destinationRef = value
        return self


class EcucUriReferenceDef(EcucAbstractInternalReferenceDef):
    """
    Definition of reference with a destination that is specified via a destinationUri. With such a reference it is possible to define a reference to a EcucContainerDef in a different module independent from the concrete definition of the target container.
    """

    # EcucUriReferenceDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.33, p.81
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationUriRef         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setDestinationUriRef         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationUriRef: EcucDestinationUriDefRefType = None

    def getDestinationUriRef(self) -> EcucDestinationUriDefRefType:
        """
        Gets the destination URI reference.
        """
        return self.destinationUriRef

    def setDestinationUriRef(self, value: EcucDestinationUriDefRefType) -> "EcucUriReferenceDef":
        """
        Sets the destination URI reference.
        A None value is a no-op.
        """
        if value is not None:
            self.destinationUriRef = value
        return self


class EcucForeignReferenceDef(EcucAbstractExternalReferenceDef):
    """
    Specify a reference to an XML description of an entity described in another
    AUTOSAR template.
    """

    # EcucForeignReferenceDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.31, p.75
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationType           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setDestinationType           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The type in the AUTOSAR Metamodel to which instance this reference is allowed to point to.
        self.destinationType: String = None

    def getDestinationType(self) -> String:
        """
        Gets the type in the AUTOSAR Metamodel to which this reference may point.
        """
        return self.destinationType

    def setDestinationType(self, value: String) -> "EcucForeignReferenceDef":
        """
        Sets the type in the AUTOSAR Metamodel to which this reference may point.
        A None value is a no-op.
        """
        if value is not None:
            self.destinationType = value
        return self


class EcucInstanceReferenceDef(EcucAbstractExternalReferenceDef):
    """
    Specify a reference to an XML description of an entity described in another
    AUTOSAR template using the INSTANCE REFERENCE semantics.
    """

    # EcucInstanceReferenceDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.32, p.77
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationContext        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setDestinationContext        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationType           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setDestinationType           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The context in the AUTOSAR Metamodel to which this reference is allowed to point to.
        self.destinationContext: String = None

        # The type in the AUTOSAR Metamodel to which instance this reference is allowed to point to.
        self.destinationType: String = None

    def getDestinationContext(self) -> String:
        """
        Gets the context in the AUTOSAR Metamodel to which this reference may point.
        """
        return self.destinationContext

    def setDestinationContext(self, value: String) -> "EcucInstanceReferenceDef":
        """
        Sets the context in the AUTOSAR Metamodel to which this reference may point.
        A None value is a no-op.
        """
        if value is not None:
            self.destinationContext = value
        return self

    def getDestinationType(self) -> String:
        """
        Gets the type in the AUTOSAR Metamodel to which this reference may point.
        """
        return self.destinationType

    def setDestinationType(self, value: String) -> "EcucInstanceReferenceDef":
        """
        Sets the type in the AUTOSAR Metamodel to which this reference may point.
        A None value is a no-op.
        """
        if value is not None:
            self.destinationType = value
        return self


class EcucAbstractStringParamDef(EcucParameterDef, ABC):
    """
    Abstract class that is used to collect the common properties for StringParamDefs, LinkerSymbolDef, FunctionNameDef and MultilineStringParamDefs.
    """

    # EcucAbstractStringParamDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.18, p.63
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDefaultValue              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultValue              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxLength                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxLength                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinLength                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinLength                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRegularExpression         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setRegularExpression         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        if type(self) is EcucAbstractStringParamDef:
            raise TypeError("Cannot instantiate abstract class EcucAbstractStringParamDef")

        super().__init__(parent, short_name)

        self.defaultValue: VerbatimString = None
        self.maxLength: PositiveInteger = None
        self.minLength: PositiveInteger = None
        self.regularExpression: RegularExpression = None

    def getDefaultValue(self) -> VerbatimString:
        return self.defaultValue

    def setDefaultValue(self, value: VerbatimString):
        if value is not None:
            self.defaultValue = value
        return self

    def getMaxLength(self) -> PositiveInteger:
        return self.maxLength

    def setMaxLength(self, value: PositiveInteger):
        if value is not None:
            self.maxLength = value
        return self

    def getMinLength(self) -> PositiveInteger:
        return self.minLength

    def setMinLength(self, value: PositiveInteger):
        if value is not None:
            self.minLength = value
        return self

    def getRegularExpression(self) -> RegularExpression:
        return self.regularExpression

    def setRegularExpression(self, value: RegularExpression):
        if value is not None:
            self.regularExpression = value
        return self


class EcucStringParamDef(EcucAbstractStringParamDef):
    """
    Configuration parameter type for String.
    """

    # EcucStringParamDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.19, p.64
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucFunctionNameDef(EcucAbstractStringParamDef):
    """
    Configuration parameter type for Function Names like those used to specify callback functions.
    """

    # EcucFunctionNameDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.22, p.65
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucIntegerParamDef(EcucParameterDef):
    """
    Configuration parameter type for Integer.
    """

    # EcucIntegerParamDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.16, p.60
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDefaultValue              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultValue              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMax                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMax                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMin                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMin                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.defaultValue: UnlimitedInteger = None
        self.max: UnlimitedInteger = None
        self.min: UnlimitedInteger = None

    def getDefaultValue(self) -> UnlimitedInteger:
        return self.defaultValue

    def setDefaultValue(self, value: UnlimitedInteger):
        if value is not None:
            self.defaultValue = value
        return self

    def getMax(self) -> UnlimitedInteger:
        return self.max

    def setMax(self, value: UnlimitedInteger):
        if value is not None:
            self.max = value
        return self

    def getMin(self) -> UnlimitedInteger:
        return self.min

    def setMin(self, value: UnlimitedInteger):
        if value is not None:
            self.min = value
        return self


class EcucEnumerationLiteralDef(Identifiable):
    """
    Configuration parameter type for enumeration literals definition.
    """

    # EcucEnumerationLiteralDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.24, p.67
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucCond                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setEcucCond                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getOrigin                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOrigin                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ecucCond: EcucConditionSpecification = None
        self.origin: String = None

    def getEcucCond(self) -> EcucConditionSpecification:
        """
        Gets the condition specification of the literal.
        """
        return self.ecucCond

    def setEcucCond(self, value: EcucConditionSpecification) -> "EcucEnumerationLiteralDef":
        """
        Sets the condition specification of the literal.
        A None value is a no-op.
        """
        if value is not None:
            self.ecucCond = value
        return self

    def getOrigin(self) -> String:
        """
        Gets the origin of the literal.
        """
        return self.origin

    def setOrigin(self, value: String) -> "EcucEnumerationLiteralDef":
        """
        Sets the origin of the literal.
        A None value is a no-op.
        """
        if value is not None:
            self.origin = value
        return self


class EcucEnumerationParamDef(EcucParameterDef):
    """
    Configuration parameter type for Enumeration.
    """

    # EcucEnumerationParamDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.23, p.68
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDefaultValue              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultValue              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLiterals                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createLiteral                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.defaultValue: Identifier = None
        self.literals: List[EcucEnumerationLiteralDef] = []

    def getDefaultValue(self) -> Identifier:
        """
        Gets the default value of the parameter.
        """
        return self.defaultValue

    def setDefaultValue(self, value: Identifier) -> "EcucEnumerationParamDef":
        """
        Sets the default value of the parameter.
        A None value is a no-op.
        """
        if value is not None:
            self.defaultValue = value
        return self

    def getLiterals(self) -> List[EcucEnumerationLiteralDef]:
        """
        Gets the list of enumeration literals.
        """
        return self.literals

    def createLiteral(self, short_name: str) -> EcucEnumerationLiteralDef:
        """
        Creates or returns an existing EcucEnumerationLiteralDef aggregated by this parameter definition.
        """
        if not self.IsElementExists(short_name):
            literal = EcucEnumerationLiteralDef(self, short_name)
            self.addElement(literal)
            self.literals.append(literal)
        return self.getElement(short_name)


class EcucFloatParamDef(EcucParameterDef):
    """
    Configuration parameter type for Float.
    """

    # EcucFloatParamDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.17, p.62
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDefaultValue              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultValue              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMax                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMax                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMin                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMin                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.defaultValue: Float = None
        self.max: Limit = None
        self.min: Limit = None

    def getDefaultValue(self) -> Float:
        return self.defaultValue

    def setDefaultValue(self, value: Float):
        if value is not None:
            self.defaultValue = value
        return self

    def getMax(self) -> Limit:
        return self.max

    def setMax(self, value: Limit):
        if value is not None:
            self.max = value
        return self

    def getMin(self) -> Limit:
        return self.min

    def setMin(self, value: Limit):
        if value is not None:
            self.min = value
        return self


class EcucChoiceContainerDef(EcucContainerDef):
    """
    Used to define configuration containers that provide a choice between several EcucParamConfContainerDef. But in the actual ECU Configuration Value description only one of the given containers will actually be present.
    """

    # EcucChoiceContainerDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.5, p.41
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getChoices                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createEcucParamConfContainerDef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.choices: List["EcucParamConfContainerDef"] = []

    def getChoices(self) -> List["EcucParamConfContainerDef"]:
        return self.choices

    def createEcucParamConfContainerDef(self, short_name: str) -> "EcucParamConfContainerDef":
        if not self.IsElementExists(short_name):
            choice = EcucParamConfContainerDef(self, short_name)
            self.addElement(choice)
            self.choices.append(choice)
        return self.getElement(short_name)


class EcucParamConfContainerDef(EcucContainerDef):
    """
    Used to define configuration containers that can hierarchically contain other containers and/or parameter definitions.
    """

    # EcucParamConfContainerDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.4, p.39
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getParameters                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createEcucBooleanParamDef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEcucStringParamDef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEcucIntegerParamDef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEcucFloatParamDef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEcucEnumerationParamDef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEcucFunctionNameDef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getReferences                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createEcucSymbolicNameReferenceDef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEcucReferenceDef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSubContainers             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createEcucChoiceContainerDef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEcucParamConfContainerDef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes an ECUCParameterDefTemplate instance.
        Args:
            parent (ARObject): The parent ARObject to which this template belongs.
            short_name (str): The short name identifier for this template.
        Attributes:
            parameters (List[EcucParameterDef]): A list of ECUC parameter definitions.
            references (List[EcucAbstractReferenceDef]): A list of ECUC abstract reference definitions.
            subContainers (List[EcucContainerDef]): A list of ECUC container definitions.
        """
        super().__init__(parent, short_name)

        self.parameters: List[EcucParameterDef] = []
        self.references: List[EcucAbstractReferenceDef] = []
        self.subContainers: List[EcucContainerDef] = []

    def getParameters(self) -> List[EcucParameterDef]:
        """
        Retrieves the list of ECUC parameter definitions.

        Returns:
            List[EcucParameterDef]: A list of ECUC parameter definitions.
        """
        return self.parameters

    def createEcucBooleanParamDef(self, short_name: str) -> EcucBooleanParamDef:
        """
        Creates a new ECUC boolean parameter definition and adds it to the container.

        Args:
            short_name (str): The short name identifier for the new parameter definition.

        Returns:
            EcucBooleanParamDef: The newly created ECUC boolean parameter definition.
        """
        if not self.IsElementExists(short_name):
            param = EcucBooleanParamDef(self, short_name)
            self.addElement(param)
            self.parameters.append(param)
        return self.getElement(short_name)

    def createEcucStringParamDef(self, short_name: str) -> EcucStringParamDef:
        """
        Creates an ECUC string parameter definition with the given short name.

        Args:
            short_name (str): The short name of the ECUC string parameter definition.

        Returns:
            EcucStringParamDef: The ECUC string parameter definition instance associated
            with the given short name.
        """
        if not self.IsElementExists(short_name):
            param = EcucStringParamDef(self, short_name)
            self.addElement(param)
            self.parameters.append(param)
        return self.getElement(short_name)

    def createEcucIntegerParamDef(self, short_name: str) -> EcucIntegerParamDef:
        """
        Creates an ECUC integer parameter definition with the given short name.

        Args:
            short_name (str): The short name of the ECUC integer parameter definition.

        Returns:
            EcucIntegerParamDef: The ECUC integer parameter definition instance associated
            with the given short name.
        """
        if not self.IsElementExists(short_name):
            param = EcucIntegerParamDef(self, short_name)
            self.addElement(param)
            self.parameters.append(param)
        return self.getElement(short_name)

    def createEcucFloatParamDef(self, short_name: str) -> EcucFloatParamDef:
        """
        Creates an ECUC float parameter definition with the given short name.

        Args:
            short_name (str): The short name of the ECUC float parameter definition.

        Returns:
            EcucFloatParamDef: The ECUC float parameter definition instance associated
            with the given short name.
        """
        if not self.IsElementExists(short_name):
            param = EcucFloatParamDef(self, short_name)
            self.addElement(param)
            self.parameters.append(param)
        return self.getElement(short_name)

    def createEcucEnumerationParamDef(self, short_name: str) -> EcucEnumerationParamDef:
        """
        Creates an ECUC enumeration parameter definition with the given short name.

        Args:
            short_name (str): The short name of the ECUC enumeration parameter definition.

        Returns:
            EcucEnumerationParamDef: The ECUC enumeration parameter definition instance associated
            with the given short name.
        """
        if not self.IsElementExists(short_name):
            param = EcucEnumerationParamDef(self, short_name)
            self.addElement(param)
            self.parameters.append(param)
        return self.getElement(short_name)

    def createEcucFunctionNameDef(self, short_name: str) -> EcucFunctionNameDef:
        """
        Creates a new ECUC function name definition and adds it to the container.

        Args:
            short_name (str): The short name identifier for the new reference definition.

        Returns:
            EcucFunctionNameDef: The newly created ECUC function name definition.
        """
        if not self.IsElementExists(short_name):
            ref = EcucFunctionNameDef(self, short_name)
            self.addElement(ref)
            self.parameters.append(ref)
        return self.getElement(short_name)

    def getReferences(self) -> List[EcucAbstractReferenceDef]:
        """
        Retrieves the list of ECUC abstract reference definitions.

        Returns:
            List[EcucAbstractReferenceDef]: A list of ECUC abstract reference definitions.
        """
        return self.references

    def createEcucSymbolicNameReferenceDef(self, short_name: str) -> EcucSymbolicNameReferenceDef:
        """
        Creates a new ECUC symbolic name reference definition and adds it to the container.

        Args:
            short_name (str): The short name identifier for the new reference definition.

        Returns:
            EcucSymbolicNameReferenceDef: The newly created ECUC symbolic name reference definition.
        """
        if not self.IsElementExists(short_name):
            ref = EcucSymbolicNameReferenceDef(self, short_name)
            self.addElement(ref)
            self.references.append(ref)
        return self.getElement(short_name)

    def createEcucReferenceDef(self, short_name: str) -> EcucReferenceDef:
        """
        Creates a new ECUC reference definition and adds it to the container.

        Args:
            short_name (str): The short name identifier for the new reference definition.

        Returns:
            EcucReferenceDef: The newly created ECUC reference definition.
        """
        if not self.IsElementExists(short_name):
            ref = EcucReferenceDef(self, short_name)
            self.addElement(ref)
            self.references.append(ref)
        return self.getElement(short_name)

    def getSubContainers(self) -> List[EcucContainerDef]:
        """
        Retrieves the list of ECUC container definitions.

        Returns:
            List[EcucContainerDef]: A list of ECUC container definitions.
        """
        return self.subContainers

    def createEcucChoiceContainerDef(self, short_name: str) -> EcucChoiceContainerDef:
        """
        Creates a new ECUC choice container definition and adds it to the container.

        Args:
            short_name (str): The short name identifier for the new container definition.

        Returns:
            EcucChoiceContainerDef: The newly created ECUC choice container definition.
        """
        if not self.IsElementExists(short_name):
            container = EcucChoiceContainerDef(self, short_name)
            self.addElement(container)
            self.subContainers.append(container)
        return self.getElement(short_name)

    def createEcucParamConfContainerDef(self, short_name: str) -> "EcucParamConfContainerDef":
        """
        Creates a new ECUC parameter configuration container definition and adds it to the container.

        Args:
            short_name (str): The short name identifier for the new container definition.

        Returns:
            EcucParamConfContainerDef: The newly created ECUC parameter configuration container definition.
        """
        if not self.IsElementExists(short_name):
            container = EcucParamConfContainerDef(self, short_name)
            self.addElement(container)
            self.subContainers.append(container)
        return self.getElement(short_name)


class EcucAddInfoParamDef(EcucParameterDef):
    """
    Configuration Parameter Definition for the specification of formatted text in the ECU Configuration Parameter Description.
    """

    # EcucAddInfoParamDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.25, p.68
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucConditionFormula(ARObject):
    """
    This formula shall yield a boolean expression depending on ecuc queries.
    Note that the EcucConditionFormula is a mixed string. Therefore, the
    properties have the upper multiplicity 1.
    """

    # EcucConditionFormula method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.43, p.100
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQueryRef              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setEcucQueryRef              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQueryStringRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setEcucQueryStringRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The EcucQuery serves as an argument for the formula.
        self.ecucQueryRef: RefType = None

        # This indicates that the referenced query shall return a string.
        self.ecucQueryStringRef: RefType = None

    def getEcucQueryRef(self) -> RefType:
        """
        Gets the EcucQuery that serves as an argument for the formula.
        """
        return self.ecucQueryRef

    def setEcucQueryRef(self, value: RefType) -> "EcucConditionFormula":
        """
        Sets the EcucQuery that serves as an argument for the formula.
        A None value is a no-op.
        """
        if value is not None:
            self.ecucQueryRef = value
        return self

    def getEcucQueryStringRef(self) -> RefType:
        """
        Gets the reference indicating that the query shall return a string.
        """
        return self.ecucQueryStringRef

    def setEcucQueryStringRef(self, value: RefType) -> "EcucConditionFormula":
        """
        Sets the reference indicating that the query shall return a string.
        A None value is a no-op.
        """
        if value is not None:
            self.ecucQueryStringRef = value
        return self


class EcucDefinitionCollection(AtpBlueprintable):
    """
    This represents the anchor point of an ECU Configuration Parameter Definition within the AUTOSAR templates structure. Tags: atp.recommendedPackage=EcucDefinitionCollections
    """

    # EcucDefinitionCollection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.1, p.25
    # Spec verified: R23-11
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addModuleRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModuleRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # References to the module definitions of individual software modules.
        self.moduleRefs: List[RefType] = []

    def addModuleRef(self, value: RefType) -> "EcucDefinitionCollection":
        """
        Adds a reference to the module definition of an individual software module.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.moduleRefs.append(value)
        return self

    def getModuleRefs(self) -> List[RefType]:
        """
        Gets the references to the module definitions of individual software modules.
        """
        return self.moduleRefs


class EcucDestinationUriDef(Identifiable):
    """
    Description of an EcucDestinationUriDef that is used as target of EcucUriReferenceDefs.
    """

    # EcucDestinationUriDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.35, p.82
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationUriPolicy      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setDestinationUriPolicy      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationUriPolicy: Optional["EcucDestinationUriPolicy"] = None

    def getDestinationUriPolicy(self) -> Optional["EcucDestinationUriPolicy"]:
        """
        Gets the destination URI policy.
        """
        return self.destinationUriPolicy

    def setDestinationUriPolicy(self, value: "EcucDestinationUriPolicy") -> "EcucDestinationUriDef":
        """
        Sets the destination URI policy.
        A None value is a no-op.
        """
        if value is not None:
            self.destinationUriPolicy = value
        return self


class EcucDestinationUriDefSet(AtpBlueprintable):
    """
    This class represents a list of EcucDestinationUriDefs.
    """

    # EcucDestinationUriDefSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.34, p.82
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationUriDefs        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addDestinationUriDef         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationUriDefs: List[EcucDestinationUriDef] = []

    def getDestinationUriDefs(self) -> List[EcucDestinationUriDef]:
        """
        Gets the list of destination URI definitions.
        """
        return self.destinationUriDefs

    def addDestinationUriDef(self, value: EcucDestinationUriDef) -> "EcucDestinationUriDefSet":
        """
        Adds a destination URI definition to the list.
        A None value is a no-op.
        """
        if value is not None:
            self.destinationUriDefs.append(value)
        return self


class EcucDestinationUriPolicy(ARObject):
    """
    The EcucDestinationUriPolicy describes the EcucContainerDef that will be targeted by EcucUriReferenceDefs. The type of the description is dependent of the destinationUriNestingContract attribute.
    """

    # EcucDestinationUriPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.36, p.83
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContainers                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addContainer                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDestinationUriNestingContract [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setDestinationUriNestingContract [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getParameters                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addParameter                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getReferences                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addReference                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()

        self.containers: List[EcucContainerDef] = []
        self.destinationUriNestingContract: Optional["EcucDestinationUriNestingContractEnum"] = None
        self.parameters: List[EcucParameterDef] = []
        self.references: List[EcucAbstractReferenceDef] = []

    def getContainers(self) -> List[EcucContainerDef]:
        """
        Gets the list of container definitions.
        """
        return self.containers

    def addContainer(self, value: EcucContainerDef) -> "EcucDestinationUriPolicy":
        """
        Adds a container definition to the list.
        A None value is a no-op.
        """
        if value is not None:
            self.containers.append(value)
        return self

    def getDestinationUriNestingContract(self) -> Optional["EcucDestinationUriNestingContractEnum"]:
        """
        Gets the destination URI nesting contract.
        """
        return self.destinationUriNestingContract

    def setDestinationUriNestingContract(self, value: "EcucDestinationUriNestingContractEnum") -> "EcucDestinationUriPolicy":
        """
        Sets the destination URI nesting contract.
        A None value is a no-op.
        """
        if value is not None:
            self.destinationUriNestingContract = value
        return self

    def getParameters(self) -> List[EcucParameterDef]:
        """
        Gets the list of parameter definitions.
        """
        return self.parameters

    def addParameter(self, value: EcucParameterDef) -> "EcucDestinationUriPolicy":
        """
        Adds a parameter definition to the list.
        A None value is a no-op.
        """
        if value is not None:
            self.parameters.append(value)
        return self

    def getReferences(self) -> List[EcucAbstractReferenceDef]:
        """
        Gets the list of reference definitions.
        """
        return self.references

    def addReference(self, value: EcucAbstractReferenceDef) -> "EcucDestinationUriPolicy":
        """
        Adds a reference definition to the list.
        A None value is a no-op.
        """
        if value is not None:
            self.references.append(value)
        return self


class EcucDestinationUriNestingContractEnum(AREnum):
    """
    EcucDestinationUriNestingContractEnum is used to determine what is qualified by the EcucDestinationUriPolicy.
    """

    # EcucDestinationUriNestingContractEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.37, p.83
    # (no methods)

    # EcucDestinationUriPolicy describes elements (subContainers, Parameters, References) that are directly owned by the target container. Tags: atp.EnumerationLiteralIndex=0
    LEAF_OF_TARGET_CONTAINER = "LEAF-OF-TARGET-CONTAINER"

    # EcucDestinationUriPolicy describes the target container of EcucUriReferenceDef. Tags: atp.EnumerationLiteralIndex=1
    TARGET_CONTAINER = "TARGET-CONTAINER"

    # EcucDestinationUriPolicy describes elements (subContainers, Parameters, References) of the target container which can be defined in arbitrary nested subContainer structure. Tags: atp.EnumerationLiteralIndex=2
    VERTEX_OF_TARGET_CONTAINER = "VERTEX-OF-TARGET-CONTAINER"

    def __init__(self):
        super().__init__(
            [
                EcucDestinationUriNestingContractEnum.LEAF_OF_TARGET_CONTAINER,
                EcucDestinationUriNestingContractEnum.TARGET_CONTAINER,
                EcucDestinationUriNestingContractEnum.VERTEX_OF_TARGET_CONTAINER,
            ]
        )


class EcucLinkerSymbolDef(EcucAbstractStringParamDef):
    """
    Configuration parameter type for Linker Symbol Names like those used to specify memory locations of variables and constants.
    """

    # EcucLinkerSymbolDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.21, p.65
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucMultilineStringParamDef(EcucAbstractStringParamDef):
    """
    Configuration parameter type for multiline Strings (including "carriage return").
    """

    # EcucMultilineStringParamDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.20, p.64
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucParameterDerivationFormula(ARObject):
    """
    This formula is intended to specify how an ecu parameter can be derived
    from other information in the Autosar Templates.
    """

    # EcucParameterDerivationFormula method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.39, p.88
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQueryRef              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setEcucQueryRef              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQueryStringRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setEcucQueryStringRef        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is one particular EcucQuery used in the calculation formula.
        self.ecucQueryRef: RefType = None

        # This indicates that the referenced query shall return a string.
        self.ecucQueryStringRef: RefType = None

    def getEcucQueryRef(self) -> RefType:
        """
        Gets the EcucQuery used in the calculation formula.
        """
        return self.ecucQueryRef

    def setEcucQueryRef(self, value: RefType) -> "EcucParameterDerivationFormula":
        """
        Sets the EcucQuery used in the calculation formula.
        A None value is a no-op.
        """
        if value is not None:
            self.ecucQueryRef = value
        return self

    def getEcucQueryStringRef(self) -> RefType:
        """
        Gets the reference indicating that the query shall return a string.
        """
        return self.ecucQueryStringRef

    def setEcucQueryStringRef(self, value: RefType) -> "EcucParameterDerivationFormula":
        """
        Sets the reference indicating that the query shall return a string.
        A None value is a no-op.
        """
        if value is not None:
            self.ecucQueryStringRef = value
        return self


class EcucQuery(Identifiable):
    """
    Defines a query to the ECUC Description.
    """

    # EcucQuery method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.40, p.89
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEcucQueryExpression       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setEcucQueryExpression       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The EcucQuery used in the calculation formula or the condition formula.
        self.ecucQueryExpression: "EcucQueryExpression" = None

    def getEcucQueryExpression(self) -> "EcucQueryExpression":
        """
        Gets the EcucQuery used in the calculation or condition formula.
        """
        return self.ecucQueryExpression

    def setEcucQueryExpression(self, value: "EcucQueryExpression") -> "EcucQuery":
        """
        Sets the EcucQuery used in the calculation or condition formula.
        A None value is a no-op.
        """
        if value is not None:
            self.ecucQueryExpression = value
        return self


class EcucQueryExpression(ARObject):
    """
    Defines a query expression to the ECUC Description and outputs the result
    as a numerical value. Due to the "mixedString" nature of the formula
    there can be several EcucQueryExpressions used.
    """

    # EcucQueryExpression method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.41, p.90
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getConfigElementDefGlobalRef  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setConfigElementDefGlobalRef  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getConfigElementDefLocalRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setConfigElementDefLocalRef   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Global reference to find an element in the Ecuc Description.
        self.configElementDefGlobalRef: RefType = None

        # Local reference to find an element within the same module.
        self.configElementDefLocalRef: RefType = None

    def getConfigElementDefGlobalRef(self) -> RefType:
        """
        Gets the global reference to find an element in the Ecuc Description.
        """
        return self.configElementDefGlobalRef

    def setConfigElementDefGlobalRef(self, value: RefType) -> "EcucQueryExpression":
        """
        Sets the global reference to find an element in the Ecuc Description.
        A None value is a no-op.
        """
        if value is not None:
            self.configElementDefGlobalRef = value
        return self

    def getConfigElementDefLocalRef(self) -> RefType:
        """
        Gets the local reference to find an element within the same module.
        """
        return self.configElementDefLocalRef

    def setConfigElementDefLocalRef(self, value: RefType) -> "EcucQueryExpression":
        """
        Sets the local reference to find an element within the same module.
        A None value is a no-op.
        """
        if value is not None:
            self.configElementDefLocalRef = value
        return self


class EcucModuleDef(EcucDefinitionElement):
    """
    Used as the top-level element for configuration definition for Software Modules, including BSW and RTE as well as ECU Infrastructure. Tags: atp.recommendedPackage=EcucModuleDefs
    """

    # EcucModuleDef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.2, p.32
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getApiServicePrefix            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setApiServicePrefix            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContainers                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createEcucParamConfContainerDef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEcucChoiceContainerDef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPostBuildVariantSupport     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPostBuildVariantSupport     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRefinedModuleDefRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRefinedModuleDefRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSupportedConfigVariants     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSupportedConfigVariant      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # For modules where several instances of the VSMD can be defined the apiServicePrefix defines the API namespace of the derived instances, e.g. Cdd, Xfrm (ComXf, SomeIpXf, E2EXf).
        self.apiServicePrefix: CIdentifier = None

        # Aggregates the top-level container definitions of this specific module definition. Stereotypes: atpSplitable Tags: atp.Splitkey=container.shortName xml.sequenceOffset=11
        self.containers: List[EcucContainerDef] = []

        # Indicates if a module supports different post-build variants (previously known as post-build selectable configuration sets). TRUE means yes, FALSE means no.
        self.postBuildVariantSupport: Boolean = None

        # Optional reference from the Vendor Specific Module Definition to the Standardized Module Definition it refines. In case this EcucModuleDef has the category STANDARDIZED_MODULE_DEFINITION this reference shall not be provided. In case this EcucModuleDef has the category VENDOR_SPECIFIC_MODULE_DEFINITION this reference is mandatory. Stereotypes: atpUriDef
        self.refinedModuleDefRef: RefType = None

        # Specifies which ConfigurationVariants are supported by this software module. This attribute is optional if the EcucModuleDef has the category STANDARDIZED_MODULE_DEFINITION. If the category attribute of the EcucModuleDef is set to VENDOR_SPECIFIC_MODULE_DEFINITION then this attribute is mandatory.
        self.supportedConfigVariants: List[EcucConfigurationVariantEnum] = []

    def getApiServicePrefix(self) -> Optional[CIdentifier]:
        """
        Gets the API namespace of the derived instances, e.g. Cdd, Xfrm (ComXf, SomeIpXf, E2EXf).
        """
        return self.apiServicePrefix

    def setApiServicePrefix(self, value: Optional[CIdentifier]):
        """
        Sets the API namespace of the derived instances, e.g. Cdd, Xfrm (ComXf, SomeIpXf, E2EXf).
        A None value is a no-op and does not change the current value.
        """
        if value is not None:
            self.apiServicePrefix = value
        return self

    def getContainers(self) -> List[EcucContainerDef]:
        """
        Gets the top-level container definitions of this specific module definition.
        """
        return self.containers

    def createEcucParamConfContainerDef(self, short_name: str) -> "EcucParamConfContainerDef":
        """
        Creates or returns an existing EcucParamConfContainerDef aggregated as a top-level container of this module definition.
        """
        if not self.IsElementExists(short_name):
            container_def = EcucParamConfContainerDef(self, short_name)
            self.addElement(container_def)
            self.containers.append(container_def)
        return self.getElement(short_name)

    def createEcucChoiceContainerDef(self, short_name: str) -> EcucChoiceContainerDef:
        """
        Creates or returns an existing EcucChoiceContainerDef aggregated as a top-level container of this module definition.
        """
        if not self.IsElementExists(short_name):
            container_def = EcucChoiceContainerDef(self, short_name)
            self.addElement(container_def)
            self.containers.append(container_def)
        return self.getElement(short_name)

    def getPostBuildVariantSupport(self) -> Boolean:
        """
        Gets whether a module supports different post-build variants. TRUE means yes, FALSE means no.
        """
        return self.postBuildVariantSupport

    def setPostBuildVariantSupport(self, value: Boolean):
        """
        Sets whether a module supports different post-build variants. TRUE means yes, FALSE means no.
        A None value is a no-op and does not change the current value.
        """
        if value is not None:
            self.postBuildVariantSupport = value
        return self

    def getRefinedModuleDefRef(self) -> RefType:
        """
        Gets the optional reference from the Vendor Specific Module Definition to the Standardized Module Definition it refines.
        """
        return self.refinedModuleDefRef

    def setRefinedModuleDefRef(self, value: RefType):
        """
        Sets the optional reference from the Vendor Specific Module Definition to the Standardized Module Definition it refines.
        A None value is a no-op and does not change the current value.
        """
        if value is not None:
            self.refinedModuleDefRef = value
        return self

    def getSupportedConfigVariants(self) -> List[EcucConfigurationVariantEnum]:
        """
        Gets the ConfigurationVariants supported by this software module.
        """
        return self.supportedConfigVariants

    def addSupportedConfigVariant(self, value: EcucConfigurationVariantEnum):
        """
        Adds a ConfigurationVariant supported by this software module.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.supportedConfigVariants.append(value)
        return self
