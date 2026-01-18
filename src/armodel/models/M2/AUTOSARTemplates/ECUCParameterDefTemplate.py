from abc import ABCMeta
from typing import List

from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, CIdentifier, Float, Identifier, Limit
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, UnlimitedInteger
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RegularExpression, String, VerbatimString
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


# class EcucConditionFormula(FormulaExpression)

class EcucConditionSpecification(ARObject):
    """
    Represents an ECUC (Electronic Control Unit Configuration) condition specification
    in the AUTOSAR model.
    This class is used to define conditions that can be applied to ECUC parameters
    or configurations. It inherits from the ARObject base class.
    Attributes:
        conditionFormula (EcucConditionFormula): Represents the formula or expression
            that defines the condition.
    """
    def __init__(self):
        super().__init__()

        self.conditionFormula: "EcucConditionFormula" = None

    def getConditionFormula(self) -> "EcucConditionFormula":
        return self.conditionFormula

    def setConditionFormula(self, value: "EcucConditionFormula"):
        if value is not None:
            self.conditionFormula = value
        return self


class EcucValidationCondition(Identifiable):
    """
    Represents an ECUC validation condition in the AUTOSAR model.

    This class is used to define a validation condition for an ECUC parameter 
    within the AUTOSAR framework. It inherits from the `Identifiable` class.

    Attributes:
        parent (ARObject): The parent ARObject to which this validation condition belongs.
        short_name (str): A short name identifier for the validation condition.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucScopeEnum(AREnum):
    def __init__(self):
        super().__init__([])


class EcucDefinitionElement(Identifiable, metaclass=ABCMeta):
    """
    Represents an ECUC (Electronic Control Unit Configuration) definition element 
    with various attributes and methods to manage its properties.
    Attributes:
        ecucCond (EcucConditionSpecification): The condition specification for the ECUC element.
        ecucValidationConds (List[EcucValidationCondition]): A list of validation conditions for the ECUC element.
        lowerMultiplicity (PositiveInteger): The lower multiplicity of the ECUC element.
        relatedTraceItemRef (RefType): A reference to a related trace item.
        scope (EcucScopeEnum): The scope of the ECUC element.
        upperMultiplicity (PositiveInteger): The upper multiplicity of the ECUC element.
        upperMultiplicityInfinite (Boolean): Indicates if the upper multiplicity is infinite.
    Methods:
        getEcucCond() -> EcucConditionSpecification:
            Returns the ECUC condition specification.
        setEcucCond(value: EcucConditionSpecification):
            Sets the ECUC condition specification.
        getEcucValidationConds() -> List[EcucValidationCondition]:
            Returns the list of ECUC validation conditions.
        addEcucValidationCond(value: EcucValidationCondition):
            Adds a validation condition to the list of ECUC validation conditions.
        getLowerMultiplicity() -> PositiveInteger:
            Returns the lower multiplicity of the ECUC element.
        setLowerMultiplicity(value: PositiveInteger):
            Sets the lower multiplicity of the ECUC element.
        getRelatedTraceItemRef() -> RefType:
            Returns the reference to the related trace item.
        setRelatedTraceItemRef(value: RefType):
            Sets the reference to the related trace item.
        getScope() -> EcucScopeEnum:
            Returns the scope of the ECUC element.
        setScope(value: EcucScopeEnum):
            Sets the scope of the ECUC element.
        getUpperMultiplicity() -> PositiveInteger:
            Returns the upper multiplicity of the ECUC element.
        setUpperMultiplicity(value: PositiveInteger):
            Sets the upper multiplicity of the ECUC element.
        getUpperMultiplicityInfinite() -> Boolean:
            Returns whether the upper multiplicity is infinite.
        setUpperMultiplicityInfinite(value: Boolean):
            Sets whether the upper multiplicity is infinite.
    """
    def __init__(self, parent: ARObject, short_name: str):
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

    Methods:
        __init__(): Initializes an instance of EcucDestinationUriDefRefType 
        by invoking the constructor of the parent `RefType` class.
    """
    def __init__(self):
        super().__init__()


class EcucConfigurationClassEnum(AREnum):
    def __init__(self):
        super().__init__([])


class EcucConfigurationVariantEnum(AREnum):
    def __init__(self):
        super().__init__([])


class EcucAbstractConfigurationClass(ARObject, metaclass=ABCMeta):
    """
    Represents an abstract configuration class for ECUC (Electronic Control Unit Configuration).
    This class provides methods to get and set the configuration class and variant.
    Attributes:
        configClass (EcucConfigurationClassEnum): The configuration class of the ECUC.
        configVariant (EcucConfigurationVariantEnum): The configuration variant of the ECUC.
    Methods:
        getConfigClass() -> EcucConfigurationClassEnum:
            Retrieves the current configuration class.
        setConfigClass(value: EcucConfigurationClassEnum):
            Sets the configuration class to the specified value.
            Returns the instance for method chaining.
        getConfigVariant() -> EcucConfigurationVariantEnum:
            Retrieves the current configuration variant.
        setConfigVariant(value: EcucConfigurationVariantEnum):
            Sets the configuration variant to the specified value.
            Returns the instance for method chaining.
    """
    def __init__(self):
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
    EcucMultiplicityConfigurationClass is a subclass of EcucAbstractConfigurationClass.

    This class represents a specific configuration class for handling multiplicity
    in ECUC (Electronic Control Unit Configuration) parameter definitions. It
    inherits from the EcucAbstractConfigurationClass to provide base functionality
    and extend it for multiplicity-specific configurations.

    Methods:
        __init__(): Initializes an instance of EcucMultiplicityConfigurationClass
        and invokes the constructor of the parent class.
    """
    def __init__(self):
        super().__init__()


class EcucContainerDef(EcucDefinitionElement, metaclass=ABCMeta):
    """
    Represents an ECUC container definition in the AUTOSAR model.
    This class defines various properties and methods to manage ECUC container
    definitions, including destination URI references, multiplicity configuration
    classes, origin, and other configuration-related attributes.
    Attributes:
        destinationUriRef (EcucDestinationUriDefRefType): The destination URI reference.
        multiplicityConfigClasses (List[EcucMultiplicityConfigurationClass]): A list of
            multiplicity configuration classes associated with the container.
        origin (String): The origin of the container.
        postBuildVariantMultiplicity (Boolean): Indicates if the container supports
            post-build variant multiplicity.
        requiresIndex (Boolean): Indicates if the container requires an index.
        multipleConfigurationContainer (Boolean): Indicates if the container supports
            multiple configurations.
    Methods:
        getDestinationUriRef() -> EcucDestinationUriDefRefType:
            Returns the destination URI reference.
        setDestinationUriRef(value: EcucDestinationUriDefRefType):
            Sets the destination URI reference.
        getMultiplicityConfigClasses() -> List[EcucMultiplicityConfigurationClass]:
            Returns the list of multiplicity configuration classes.
        addMultiplicityConfigClass(value: EcucMultiplicityConfigurationClass):
            Adds a multiplicity configuration class to the list.
        getOrigin() -> String:
            Returns the origin of the container.
        setOrigin(value: String):
            Sets the origin of the container.
        getPostBuildVariantMultiplicity() -> Boolean:
            Returns whether the container supports post-build variant multiplicity.
        setPostBuildVariantMultiplicity(value: Boolean):
            Sets whether the container supports post-build variant multiplicity.
        getRequiresIndex() -> Boolean:
            Returns whether the container requires an index.
        setRequiresIndex(value: Boolean):
            Sets whether the container requires an index.
        getMultipleConfigurationContainer() -> Boolean:
            Returns whether the container supports multiple configurations.
        setMultipleConfigurationContainer(value: Boolean):
            Sets whether the container supports multiple configurations.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationUriRef: EcucDestinationUriDefRefType = None
        self.multiplicityConfigClasses: List[EcucMultiplicityConfigurationClass] = []
        self.origin: String = None
        self.postBuildVariantMultiplicity: Boolean = None
        self.requiresIndex: Boolean = None
        self.multipleConfigurationContainer: Boolean = None

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

    def getMultipleConfigurationContainer(self) -> Boolean:
        return self.multipleConfigurationContainer

    def setMultipleConfigurationContainer(self, value: Boolean):
        if value is not None:
            self.multipleConfigurationContainer = value
        return self

    
class EcucValueConfigurationClass(EcucAbstractConfigurationClass):
    """
    EcucValueConfigurationClass is a subclass of EcucAbstractConfigurationClass.

    This class represents a specific type of ECU configuration class used in the AUTOSAR standard.
    It is designed to handle value-based configurations for ECU parameters.

    Methods:
        __init__(): Initializes an instance of EcucValueConfigurationClass by invoking the constructor
                    of its superclass, EcucAbstractConfigurationClass.
    """
    def __init__(self):
        super().__init__()


class EcucCommonAttributes(EcucDefinitionElement, metaclass=ABCMeta):
    """
    EcucCommonAttributes is an abstract base class that represents common attributes 
    for ECUC (Electronic Control Unit Configuration) definition elements. This class 
    cannot be instantiated directly and must be subclassed.
    Attributes:
        multiplicityConfigClasses (List[EcucMultiplicityConfigurationClass]): 
            A list of multiplicity configuration classes associated with the ECUC element.
        origin (String): 
            The origin of the ECUC element.
        postBuildVariantMultiplicity (Boolean): 
            Indicates whether the ECUC element supports post-build variant multiplicity.
        postBuildVariantValue (Boolean): 
            Indicates whether the ECUC element supports post-build variant values.
        requiresIndex (Boolean): 
            Specifies whether the ECUC element requires an index.
        valueConfigClasses (List[EcucValueConfigurationClass]): 
            A list of value configuration classes associated with the ECUC element.
    Methods:
        getMultiplicityConfigClasses() -> List[EcucMultiplicityConfigurationClass]:
            Returns the list of multiplicity configuration classes.
        addMultiplicityConfigClass(value: EcucMultiplicityConfigurationClass):
            Adds a multiplicity configuration class to the list.
        getOrigin() -> String:
            Returns the origin of the ECUC element.
        setOrigin(value: String):
            Sets the origin of the ECUC element.
        getPostBuildVariantMultiplicity() -> Boolean:
            Returns whether the ECUC element supports post-build variant multiplicity.
        setPostBuildVariantMultiplicity(value: Boolean):
            Sets whether the ECUC element supports post-build variant multiplicity.
        getPostBuildVariantValue() -> Boolean:
            Returns whether the ECUC element supports post-build variant values.
        setPostBuildVariantValue(value: Boolean):
            Sets whether the ECUC element supports post-build variant values.
        getRequiresIndex() -> Boolean:
            Returns whether the ECUC element requires an index.
        setRequiresIndex(value: Boolean):
            Sets whether the ECUC element requires an index.
        getValueConfigClasses() -> List[EcucValueConfigurationClass]:
            Returns the list of value configuration classes.
        addValueConfigClass(value: EcucValueConfigurationClass):
            Adds a value configuration class to the list.
    """
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

    def getValueConfigClasses(self) -> EcucValueConfigurationClass:
        return self.valueConfigClasses

    def addValueConfigClass(self, value: EcucValueConfigurationClass):
        if value is not None:
            self.valueConfigClasses.append(value)
        return self


class EcucDerivationSpecification(ARObject):
    """
    Represents an ECUC Derivation Specification in the AUTOSAR model.

    This class is a specialization of the ARObject base class and is used to define
    derivation specifications for ECUC parameters in the AUTOSAR standard.
    """
    def __init__(self):
        super().__init__()


class EcucParameterDef(EcucCommonAttributes):
    """
    Represents an ECUC (Electronic Control Unit Configuration) parameter definition
    in the AUTOSAR model. This class extends common attributes for ECUC elements
    and provides additional properties and methods specific to parameter definitions.
    Attributes:
        derivation (EcucDerivationSpecification): Specifies the derivation of the parameter.
        symbolicNameValue (Boolean): Indicates whether the parameter has a symbolic name value.
        withAuto (Boolean): Indicates whether the parameter supports automatic configuration.
    Methods:
        getDerivation() -> EcucDerivationSpecification:
            Retrieves the derivation specification of the parameter.
        setDerivation(value: EcucDerivationSpecification):
            Sets the derivation specification of the parameter.
            Returns the current instance for method chaining.
        getSymbolicNameValue() -> Boolean:
            Retrieves the symbolic name value of the parameter.
        setSymbolicNameValue(value: Boolean):
            Sets the symbolic name value of the parameter.
            Returns the current instance for method chaining.
        getWithAuto() -> Boolean:
            Retrieves the automatic configuration status of the parameter.
        setWithAuto(value: Boolean):
            Sets the automatic configuration status of the parameter.
            Returns the current instance for method chaining.
    """
    def __init__(self, parent: ARObject, short_name: str):
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
    Represents a boolean parameter definition in the AUTOSAR ECUC model.

    This class is a specialized type of `EcucParameterDef` that allows for the
    definition of boolean parameters within the ECUC parameter configuration.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR model hierarchy.
        short_name (str): The short name of the ECUC boolean parameter definition.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.defaultValue: Boolean = None

    def getDefaultValue(self) -> Boolean:
        return self.defaultValue
    
    def setDefaultValue(self, value: Boolean):
        if value is not None:
            self.defaultValue = value
        return self


class EcucAbstractReferenceDef(EcucCommonAttributes, metaclass=ABCMeta):
    """
    EcucAbstractReferenceDef is an abstract class that extends EcucCommonAttributes and uses ABCMeta as its metaclass.
    It represents an ECUC (Electronic Control Unit Configuration) abstract reference definition.
    Attributes:
        withAuto (Boolean): A flag indicating whether the reference is automatic. Defaults to None.
    Methods:
        getWithAuto() -> Boolean:
            Retrieves the value of the `withAuto` attribute.
        setWithAuto(value: Boolean):
            Sets the value of the `withAuto` attribute. If the provided value is not None, it updates the attribute.
            Returns the instance itself for method chaining.
    Raises:
        TypeError: If an attempt is made to instantiate this abstract class directly.
    """
    def __init__(self, parent, short_name):
        if type(self) is EcucAbstractReferenceDef:
            raise TypeError("Cannot instantiate abstract class EcucAbstractReferenceDef")

        super().__init__(parent, short_name)

        self.withAuto: Boolean = None

    def getWithAuto(self) -> Boolean:
        return self.withAuto

    def setWithAuto(self, value: Boolean):
        if value is not None:
            self.withAuto = value
        return self


class EcucAbstractInternalReferenceDef(EcucAbstractReferenceDef, metaclass=ABCMeta):
    """
    EcucAbstractInternalReferenceDef is an abstract class that extends EcucAbstractReferenceDef 
    and uses ABCMeta as its metaclass. This class cannot be instantiated directly.
    Attributes:
        requiresSymbolicNameValue (Boolean): A boolean attribute that indicates whether 
            a symbolic name value is required. Defaults to None.
    Methods:
        getRequiresSymbolicNameValue() -> Boolean:
            Returns the value of the requiresSymbolicNameValue attribute.
        setRequiresSymbolicNameValue(value: Boolean):
            Sets the value of the requiresSymbolicNameValue attribute if the provided value 
            is not None. Returns the instance of the class.
    """
    def __init__(self, parent, short_name):
        if type(self) is EcucAbstractInternalReferenceDef:
            raise TypeError("Cannot instantiate abstract class EcucAbstractInternalReferenceDef")
        super().__init__(parent, short_name)

        self.requiresSymbolicNameValue: Boolean = None

    def getRequiresSymbolicNameValue(self) -> Boolean:
        return self.requiresSymbolicNameValue

    def setRequiresSymbolicNameValue(self, value: Boolean):
        if value is not None:
            self.requiresSymbolicNameValue = value
        return self


class EcucAbstractExternalReferenceDef(EcucAbstractReferenceDef, metaclass=ABCMeta):
    def __init__(self, parent, short_name):
        if type(self) is EcucAbstractExternalReferenceDef:
            raise TypeError("Cannot instantiate abstract class EcucAbstractExternalReferenceDef")
        
        super().__init__(parent, short_name)


class EcucSymbolicNameReferenceDef(EcucAbstractInternalReferenceDef):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationRef: RefType = None

    def getDestinationRef(self) -> RefType:
        return self.destinationRef

    def setDestinationRef(self, value: RefType):
        if value is not None:
            self.destinationRef = value
        return self


class EcucChoiceReferenceDef(EcucAbstractInternalReferenceDef):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationRef: RefType = None

    def getDestinationRef(self) -> RefType:
        return self.destinationRef

    def setDestinationRef(self, value: RefType):
        if value is not None:
            self.destinationRef = value
        return self


class EcucReferenceDef(EcucAbstractInternalReferenceDef):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationRef: RefType = None

    def getDestinationRef(self) -> RefType:
        return self.destinationRef

    def setDestinationRef(self, value: RefType):
        if value is not None:
            self.destinationRef = value
        return self


class EcucUriReferenceDef(EcucAbstractInternalReferenceDef):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationUriRef: EcucDestinationUriDefRefType = None

    def getDestinationUriRef(self) -> EcucDestinationUriDefRefType:
        return self.destinationUriRef

    def setDestinationUriRef(self, value: EcucDestinationUriDefRefType):
        if value is not None:
            self.destinationUriRef = value
        return self


class EcucForeignReferenceDef(EcucAbstractExternalReferenceDef):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationContext: String = None
        self.destinationType: String = None

    def getDestinationContext(self) -> String:
        return self.destinationContext

    def setDestinationContext(self, value: String):
        if value is not None:
            self.destinationContext = value
        return self

    def getDestinationType(self) -> String:
        return self.destinationType

    def setDestinationType(self, value: String):
        if value is not None:
            self.destinationType = value
        return self


class EcucInstanceReferenceDef(EcucAbstractExternalReferenceDef):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationType: String = None

    def getDestinationType(self) -> String:
        return self.destinationType

    def setDestinationType(self, value: String):
        if value is not None:
            self.destinationType = value
        return self


class EcucAbstractStringParamDef(EcucParameterDef, metaclass=ABCMeta):
    """
    EcucAbstractStringParamDef is an abstract class that represents a string parameter definition
    in the AUTOSAR ECUC model. It inherits from EcucParameterDef and uses ABCMeta as its metaclass
    to enforce abstraction.
    Attributes:
        defaultValue (VerbatimString): The default value of the string parameter.
        maxLength (PositiveInteger): The maximum length of the string parameter.
        minLength (PositiveInteger): The minimum length of the string parameter.
        regularExpression (RegularExpression): A regular expression that the string parameter must match.
    Methods:
        getDefaultValue() -> VerbatimString:
            Returns the default value of the string parameter.
        setDefaultValue(value: VerbatimString):
            Sets the default value of the string parameter. Returns the instance for chaining.
        getMaxLength() -> PositiveInteger:
            Returns the maximum length of the string parameter.
        setMaxLength(value: PositiveInteger):
            Sets the maximum length of the string parameter. Returns the instance for chaining.
        getMinLength() -> PositiveInteger:
            Returns the minimum length of the string parameter.
        setMinLength(value: PositiveInteger):
            Sets the minimum length of the string parameter. Returns the instance for chaining.
        getRegularExpression() -> RegularExpression:
            Returns the regular expression constraint of the string parameter.
        setRegularExpression(value: RegularExpression):
            Sets the regular expression constraint of the string parameter. Returns the instance for chaining.
    Raises:
        TypeError: If an attempt is made to instantiate the abstract class directly.
    """
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
    Represents a specific type of ECUC parameter definition for string parameters.

    This class is a specialization of `EcucAbstractStringParamDef` and is used to
    define string parameters in the AUTOSAR ECUC configuration.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR model hierarchy.
        short_name (str): The short name of the ECUC string parameter definition.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucFunctionNameDef(EcucAbstractStringParamDef):
    """
    Represents a specific type of ECUC parameter definition for function names.

    This class is a specialization of `EcucAbstractStringParamDef` and is used
    to define ECUC parameters that represent function names in the AUTOSAR model.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR hierarchy.
        short_name (str): The short name of the ECUC parameter definition.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucIntegerParamDef(EcucParameterDef):
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
    Represents an ECUC Enumeration Literal Definition in the AUTOSAR model.
    This class is used to define enumeration literals for ECUC parameters, 
    including their associated condition specifications and origin information.
    Attributes:
        ecucCond (EcucConditionSpecification): The condition specification associated with the enumeration literal.
        origin (String): The origin information for the enumeration literal.
    Methods:
        getEcucCond() -> EcucConditionSpecification:
            Retrieves the condition specification associated with the enumeration literal.
        setEcucCond(value: EcucConditionSpecification):
            Sets the condition specification for the enumeration literal.
            Returns the current instance for method chaining.
        getOrigin() -> String:
            Retrieves the origin information for the enumeration literal.
        setOrigin(value: String):
            Sets the origin information for the enumeration literal.
            Returns the current instance for method chaining.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ecucCond: EcucConditionSpecification = None
        self.origin: String = None

    def getEcucCond(self) -> EcucConditionSpecification:
        return self.ecucCond

    def setEcucCond(self, value: EcucConditionSpecification):
        if value is not None:
            self.ecucCond = value
        return self

    def getOrigin(self) -> String:
        return self.origin

    def setOrigin(self, value: String):
        if value is not None:
            self.origin = value
        return self


class EcucEnumerationParamDef(EcucParameterDef):
    """
    Represents an ECUC (Electronic Control Unit Configuration) enumeration parameter definition.
    This class is used to define an enumeration parameter in an AUTOSAR ECUC model. It allows
    setting a default value and managing a list of enumeration literals.
    Attributes:
        defaultValue (Identifier): The default value of the enumeration parameter.
        literals (List[EcucEnumerationLiteralDef]): A list of enumeration literal definitions.
    Methods:
        getDefaultValue() -> UnlimitedInteger:
            Retrieves the default value of the enumeration parameter.
        setDefaultValue(value: UnlimitedInteger):
            Sets the default value of the enumeration parameter.
            Returns the current instance for method chaining.
        getLiterals() -> List[EcucEnumerationLiteralDef]:
            Retrieves the list of enumeration literal definitions.
        createLiteral(short_name: str) -> EcucEnumerationLiteralDef:
            Creates a new enumeration literal with the specified short name if it does not already exist.
            Adds the literal to the list of literals and returns it.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.defaultValue: Identifier = None
        self.literals: List[EcucEnumerationLiteralDef] = []

    def getDefaultValue(self) -> UnlimitedInteger:
        return self.defaultValue

    def setDefaultValue(self, value: UnlimitedInteger):
        if value is not None:
            self.defaultValue = value
        return self

    def getLiterals(self) -> List[EcucEnumerationLiteralDef]:
        return self.literals

    def createLiteral(self, short_name: str) -> EcucEnumerationLiteralDef:
        if not self.IsElementExists(short_name):
            literal = EcucEnumerationLiteralDef(self, short_name)
            self.addElement(literal)
            self.literals.append(literal)
        return self.getElement(short_name)


class EcucFloatParamDef(EcucParameterDef):
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
    Represents an ECUC choice container definition in the AUTOSAR model.

    This class is a specialized type of `EcucContainerDef` that allows for the
    definition of choice containers within the ECUC parameter configuration.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR model hierarchy.
        short_name (str): The short name of the ECUC choice container definition.
    """
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
    class EcucParamConfContainerDef:
        """
        Represents a configuration container definition in the AUTOSAR ECUC model.
        This class is used to define a container that can hold parameters, references,
        and sub-containers as part of the AUTOSAR ECUC configuration.
        Attributes:
            parameters (List[EcucParameterDef]): A list of parameter definitions associated with this container.
            references (List[EcucAbstractReferenceDef]): A list of reference definitions associated with this container.
            subContainers (List[EcucContainerDef]): A list of sub-container definitions associated with this container.
        Methods:
            getParameters() -> List[EcucParameterDef]:
                Retrieves the list of parameter definitions.
            addParameter(value: EcucParameterDef):
                Adds a parameter definition to the container.
                Returns the current instance for method chaining.
            getReferences() -> List[EcucAbstractReferenceDef]:
                Retrieves the list of reference definitions.
            addReference(value: EcucAbstractReferenceDef):
                Adds a reference definition to the container.
                Returns the current instance for method chaining.
            getSubContainers() -> List[EcucContainerDef]:
                Retrieves the list of sub-container definitions.
            addSubContainers(value: EcucContainerDef):
                Adds a sub-container definition to the container.
                Returns the current instance for method chaining.
        """

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
    
    def createEcucParamConfContainerDef(self, short_name: str) -> EcucParamConfContainerDef:
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
    Represents an ECUC additional info parameter definition in the AUTOSAR model.

    This class is a specialized type of `EcucParameterDef` that allows for the
    definition of additional info parameters within the ECUC parameter configuration.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR model hierarchy.
        short_name (str): The short name of the ECUC additional info parameter definition.
        defaultValue (VerbatimString): The default value of the additional info parameter.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.defaultValue: VerbatimString = None

    def getDefaultValue(self) -> VerbatimString:
        return self.defaultValue

    def setDefaultValue(self, value: VerbatimString):
        if value is not None:
            self.defaultValue = value
        return self


class EcucConditionFormula(ARObject):
    """
    Represents an ECUC condition formula in the AUTOSAR model.

    This class is used to define formulas or expressions that can be used
    in ECUC condition specifications.

    Attributes:
        formula (String): The formula expression.
    """
    def __init__(self):
        super().__init__()

        self.formula: String = None

    def getFormula(self) -> String:
        return self.formula

    def setFormula(self, value: String):
        if value is not None:
            self.formula = value
        return self


class EcucDefinitionCollection(ARObject):
    """
    Represents an ECUC definition collection in the AUTOSAR model.

    This class is used to group related ECUC definitions together.

    Attributes:
        definitions (List[EcucDefinitionElement]): A list of ECUC definition elements.
    """
    def __init__(self):
        super().__init__()

        self.definitions: List[EcucDefinitionElement] = []

    def getDefinitions(self) -> List[EcucDefinitionElement]:
        return self.definitions

    def addDefinition(self, value: EcucDefinitionElement):
        if value is not None:
            self.definitions.append(value)
        return self


class EcucDestinationUriDef(Identifiable):
    """
    Represents an ECUC destination URI definition in the AUTOSAR model.

    This class is used to define destination URIs for ECUC references.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR model hierarchy.
        short_name (str): The short name of the ECUC destination URI definition.
        destinationUri (String): The destination URI.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationUri: String = None

    def getDestinationUri(self) -> String:
        return self.destinationUri

    def setDestinationUri(self, value: String):
        if value is not None:
            self.destinationUri = value
        return self


class EcucDestinationUriDefSet(Identifiable):
    """
    Represents an ECUC destination URI definition set in the AUTOSAR model.

    This class is used to group related ECUC destination URI definitions.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR model hierarchy.
        short_name (str): The short name of the ECUC destination URI definition set.
        destinationUriDefs (List[EcucDestinationUriDef]): A list of ECUC destination URI definitions.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.destinationUriDefs: List[EcucDestinationUriDef] = []

    def getDestinationUriDefs(self) -> List[EcucDestinationUriDef]:
        return self.destinationUriDefs

    def addDestinationUriDef(self, value: EcucDestinationUriDef):
        if value is not None:
            self.destinationUriDefs.append(value)
        return self


class EcucDestinationUriPolicy(ARObject):
    """
    Represents an ECUC destination URI policy in the AUTOSAR model.

    This class is used to define policies for ECUC destination URIs.

    Attributes:
        policy (String): The policy definition.
    """
    def __init__(self):
        super().__init__()

        self.policy: String = None

    def getPolicy(self) -> String:
        return self.policy

    def setPolicy(self, value: String):
        if value is not None:
            self.policy = value
        return self


class EcucLinkerSymbolDef(Identifiable):
    """
    Represents an ECUC linker symbol definition in the AUTOSAR model.

    This class is used to define linker symbols for ECUC parameters.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR model hierarchy.
        short_name (str): The short name of the ECUC linker symbol definition.
        linkerSymbol (CIdentifier): The linker symbol.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.linkerSymbol: CIdentifier = None

    def getLinkerSymbol(self) -> CIdentifier:
        return self.linkerSymbol

    def setLinkerSymbol(self, value: CIdentifier):
        if value is not None:
            self.linkerSymbol = value
        return self


class EcucMultilineStringParamDef(EcucAbstractStringParamDef):
    """
    Represents an ECUC multiline string parameter definition in the AUTOSAR model.

    This class is a specialized type of `EcucAbstractStringParamDef` that allows for
    multiline string parameters within the ECUC parameter configuration.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR model hierarchy.
        short_name (str): The short name of the ECUC multiline string parameter definition.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucParameterDerivationFormula(ARObject):
    """
    Represents an ECUC parameter derivation formula in the AUTOSAR model.

    This class is used to define formulas for deriving ECUC parameter values.

    Attributes:
        formula (String): The derivation formula.
    """
    def __init__(self):
        super().__init__()

        self.formula: String = None

    def getFormula(self) -> String:
        return self.formula

    def setFormula(self, value: String):
        if value is not None:
            self.formula = value
        return self


class EcucQuery(ARObject):
    """
    Represents an ECUC query in the AUTOSAR model.

    This class is used to define queries for ECUC parameter values.

    Attributes:
        queryExpression (EcucQueryExpression): The query expression.
    """
    def __init__(self):
        super().__init__()

        self.queryExpression: "EcucQueryExpression" = None

    def getQueryExpression(self) -> "EcucQueryExpression":
        return self.queryExpression

    def setQueryExpression(self, value: "EcucQueryExpression"):
        if value is not None:
            self.queryExpression = value
        return self


class EcucQueryExpression(ARObject):
    """
    Represents an ECUC query expression in the AUTOSAR model.

    This class is used to define query expressions for ECUC parameters.

    Attributes:
        expression (String): The query expression.
    """
    def __init__(self):
        super().__init__()

        self.expression: String = None

    def getExpression(self) -> String:
        return self.expression

    def setExpression(self, value: String):
        if value is not None:
            self.expression = value
        return self


class EcucModuleDef(EcucDefinitionElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.apiServicePrefix: CIdentifier = None
        self.containers: List[EcucContainerDef] = []
        self.postBuildVariantSupport: Boolean = None
        self.refinedModuleDefRef: RefType = None
        self.supportedConfigVariants: List[EcucConfigurationVariantEnum] = []

    def getApiServicePrefix(self) -> CIdentifier:
        return self.apiServicePrefix

    def setApiServicePrefix(self, value: CIdentifier):
        if value is not None:
            self.apiServicePrefix = value
        return self

    def getContainers(self) -> List[EcucContainerDef]:
        return self.containers

    def createEcucParamConfContainerDef(self, short_name: str) -> EcucParamConfContainerDef:
        if (not self.IsElementExists(short_name)):
            container_def = EcucParamConfContainerDef(self, short_name)
            self.addElement(container_def)
            self.containers.append(container_def)
        return self.getElement(short_name)

    def createEcucChoiceContainerDef(self, short_name: str) -> EcucChoiceContainerDef:
        if (not self.IsElementExists(short_name)):
            container_def = EcucChoiceContainerDef(self, short_name)
            self.addElement(container_def)
            self.containers.append(container_def)
        return self.getElement(short_name)

    def getPostBuildVariantSupport(self) -> Boolean:
        return self.postBuildVariantSupport

    def setPostBuildVariantSupport(self, value: Boolean):
        if value is not None:
            self.postBuildVariantSupport = value
        return self

    def getRefinedModuleDefRef(self) -> RefType:
        return self.refinedModuleDefRef

    def setRefinedModuleDefRef(self, value: RefType):
        if value is not None:
            self.refinedModuleDefRef = value
        return self

    def getSupportedConfigVariants(self) -> List[EcucConfigurationVariantEnum]:
        return self.supportedConfigVariants

    def addSupportedConfigVariant(self, value: EcucConfigurationVariantEnum):
        if value is not None:
            self.supportedConfigVariants.append(value)
        return self

