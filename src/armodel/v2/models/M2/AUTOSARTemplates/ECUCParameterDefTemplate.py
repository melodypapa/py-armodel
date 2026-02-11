"""
AUTOSAR Package - ECUCParameterDefTemplate

Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    Identifier,
    PositiveInteger,
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class EcucDefinitionCollection(ARElement):
    """
    This represents the anchor point of an ECU Configuration Parameter
    Definition within the AUTOSAR templates structure.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDefinitionCollection

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 25, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 185, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # References to the module definitions of individual.
        self._module: List[EcucModuleDef] = []

    @property
    def module(self) -> List[EcucModuleDef]:
        """Get module (Pythonic accessor)."""
        return self._module

    def with_module(self, value):
        """
        Set module and return self for chaining.

        Args:
            value: The module to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_module("value")
        """
        self.module = value  # Use property setter (gets validation)
        return self

    def with_ecuc_validation(self, value):
        """
        Set ecuc_validation and return self for chaining.

        Args:
            value: The ecuc_validation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_validation("value")
        """
        self.ecuc_validation = value  # Use property setter (gets validation)
        return self

    def with_destination_uri_def(self, value):
        """
        Set destination_uri_def and return self for chaining.

        Args:
            value: The destination_uri_def to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_uri_def("value")
        """
        self.destination_uri_def = value  # Use property setter (gets validation)
        return self

    def with_container(self, value):
        """
        Set container and return self for chaining.

        Args:
            value: The container to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_container("value")
        """
        self.container = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value):
        """
        Set parameter and return self for chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self

    def with_reference(self, value):
        """
        Set reference and return self for chaining.

        Args:
            value: The reference to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reference("value")
        """
        self.reference = value  # Use property setter (gets validation)
        return self

    def with_container(self, value):
        """
        Set container and return self for chaining.

        Args:
            value: The container to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_container("value")
        """
        self.container = value  # Use property setter (gets validation)
        return self

    def with_supported(self, value):
        """
        Set supported and return self for chaining.

        Args:
            value: The supported to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supported("value")
        """
        self.supported = value  # Use property setter (gets validation)
        return self

    def with_multiplicity(self, value):
        """
        Set multiplicity and return self for chaining.

        Args:
            value: The multiplicity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_multiplicity("value")
        """
        self.multiplicity = value  # Use property setter (gets validation)
        return self

    def with_multiplicity(self, value):
        """
        Set multiplicity and return self for chaining.

        Args:
            value: The multiplicity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_multiplicity("value")
        """
        self.multiplicity = value  # Use property setter (gets validation)
        return self

    def with_value_config(self, value):
        """
        Set value_config and return self for chaining.

        Args:
            value: The value_config to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value_config("value")
        """
        self.value_config = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value):
        """
        Set parameter and return self for chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self

    def with_reference(self, value):
        """
        Set reference and return self for chaining.

        Args:
            value: The reference to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reference("value")
        """
        self.reference = value  # Use property setter (gets validation)
        return self

    def with_sub_container(self, value):
        """
        Set sub_container and return self for chaining.

        Args:
            value: The sub_container to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_container("value")
        """
        self.sub_container = value  # Use property setter (gets validation)
        return self

    def with_choice(self, value):
        """
        Set choice and return self for chaining.

        Args:
            value: The choice to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_choice("value")
        """
        self.choice = value  # Use property setter (gets validation)
        return self

    def with_literal(self, value):
        """
        Set literal and return self for chaining.

        Args:
            value: The literal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_literal("value")
        """
        self.literal = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModule(self) -> List[EcucModuleDef]:
        """
        AUTOSAR-compliant getter for module.

        Returns:
            The module value

        Note:
            Delegates to module property (CODING_RULE_V2_00017)
        """
        return self.module  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucDefinitionElement(Identifiable, ABC):
    """
    Common class used to express the commonalities of configuration parameters,
    references and containers. If not stated otherwise the default multiplicity
    is exactly one mandatory occurrence of the specified element.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDefinitionElement

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 45, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 440, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is EcucDefinitionElement:
            raise TypeError("EcucDefinitionElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If it evaluates to true the Ecu Parameter definition shall be as specified.
        # Otherwise the parameter be ignored.
        self._ecucCond: Optional["EcucCondition"] = None

    @property
    def ecuc_cond(self) -> Optional["EcucCondition"]:
        """Get ecucCond (Pythonic accessor)."""
        return self._ecucCond

    @ecuc_cond.setter
    def ecuc_cond(self, value: Optional["EcucCondition"]) -> None:
        """
        Set ecucCond with validation.

        Args:
            value: The ecucCond to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecucCond = None
            return

        if not isinstance(value, EcucCondition):
            raise TypeError(
                f"ecucCond must be EcucCondition or None, got {type(value).__name__}"
            )
        self._ecucCond = value
        # order to indicate a valid validation the EcucDefinitionElement.
        self._ecucValidation: List["EcucValidation"] = []

    @property
    def ecuc_validation(self) -> List["EcucValidation"]:
        """Get ecucValidation (Pythonic accessor)."""
        return self._ecucValidation
        # The lower multiplicity of the specified element.
        # least one occurrence least n occurrences 318 Document ID 87:
                # AUTOSAR_CP_TPS_ECUConfiguration ECU Configuration R23-11.
        self._lowerMultiplicity: Optional["PositiveInteger"] = None

    @property
    def lower_multiplicity(self) -> Optional["PositiveInteger"]:
        """Get lowerMultiplicity (Pythonic accessor)."""
        return self._lowerMultiplicity

    @lower_multiplicity.setter
    def lower_multiplicity(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set lowerMultiplicity with validation.

        Args:
            value: The lowerMultiplicity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerMultiplicity = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"lowerMultiplicity must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._lowerMultiplicity = value
        # (EcucId).
        self._relatedTrace: Optional["Traceable"] = None

    @property
    def related_trace(self) -> Optional["Traceable"]:
        """Get relatedTrace (Pythonic accessor)."""
        return self._relatedTrace

    @related_trace.setter
    def related_trace(self, value: Optional["Traceable"]) -> None:
        """
        Set relatedTrace with validation.

        Args:
            value: The relatedTrace to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._relatedTrace = None
            return

        if not isinstance(value, Traceable):
            raise TypeError(
                f"relatedTrace must be Traceable or None, got {type(value).__name__}"
            )
        self._relatedTrace = value
        self._scope: Optional[EcucScopeEnum] = None

    @property
    def scope(self) -> Optional[EcucScopeEnum]:
        """Get scope (Pythonic accessor)."""
        return self._scope

    @scope.setter
    def scope(self, value: Optional[EcucScopeEnum]) -> None:
        """
        Set scope with validation.

        Args:
            value: The scope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._scope = None
            return

        if not isinstance(value, EcucScopeEnum):
            raise TypeError(
                f"scope must be EcucScopeEnum or None, got {type(value).__name__}"
            )
        self._scope = value
                # set to true.
        # is set than upperMultiplicity shall used.
        self._upperMultiplicity: Optional["Boolean"] = None

    @property
    def upper_multiplicity(self) -> Optional["Boolean"]:
        """Get upperMultiplicity (Pythonic accessor)."""
        return self._upperMultiplicity

    @upper_multiplicity.setter
    def upper_multiplicity(self, value: Optional["Boolean"]) -> None:
        """
        Set upperMultiplicity with validation.

        Args:
            value: The upperMultiplicity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperMultiplicity = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"upperMultiplicity must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._upperMultiplicity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucCond(self) -> "EcucCondition":
        """
        AUTOSAR-compliant getter for ecucCond.

        Returns:
            The ecucCond value

        Note:
            Delegates to ecuc_cond property (CODING_RULE_V2_00017)
        """
        return self.ecuc_cond  # Delegates to property

    def setEcucCond(self, value: "EcucCondition") -> EcucDefinitionElement:
        """
        AUTOSAR-compliant setter for ecucCond with method chaining.

        Args:
            value: The ecucCond to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecuc_cond property setter (gets validation automatically)
        """
        self.ecuc_cond = value  # Delegates to property setter
        return self

    def getEcucValidation(self) -> List["EcucValidation"]:
        """
        AUTOSAR-compliant getter for ecucValidation.

        Returns:
            The ecucValidation value

        Note:
            Delegates to ecuc_validation property (CODING_RULE_V2_00017)
        """
        return self.ecuc_validation  # Delegates to property

    def getLowerMultiplicity(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for lowerMultiplicity.

        Returns:
            The lowerMultiplicity value

        Note:
            Delegates to lower_multiplicity property (CODING_RULE_V2_00017)
        """
        return self.lower_multiplicity  # Delegates to property

    def setLowerMultiplicity(self, value: "PositiveInteger") -> EcucDefinitionElement:
        """
        AUTOSAR-compliant setter for lowerMultiplicity with method chaining.

        Args:
            value: The lowerMultiplicity to set

        Returns:
            self for method chaining

        Note:
            Delegates to lower_multiplicity property setter (gets validation automatically)
        """
        self.lower_multiplicity = value  # Delegates to property setter
        return self

    def getRelatedTrace(self) -> "Traceable":
        """
        AUTOSAR-compliant getter for relatedTrace.

        Returns:
            The relatedTrace value

        Note:
            Delegates to related_trace property (CODING_RULE_V2_00017)
        """
        return self.related_trace  # Delegates to property

    def setRelatedTrace(self, value: "Traceable") -> EcucDefinitionElement:
        """
        AUTOSAR-compliant setter for relatedTrace with method chaining.

        Args:
            value: The relatedTrace to set

        Returns:
            self for method chaining

        Note:
            Delegates to related_trace property setter (gets validation automatically)
        """
        self.related_trace = value  # Delegates to property setter
        return self

    def getScope(self) -> EcucScopeEnum:
        """
        AUTOSAR-compliant getter for scope.

        Returns:
            The scope value

        Note:
            Delegates to scope property (CODING_RULE_V2_00017)
        """
        return self.scope  # Delegates to property

    def setScope(self, value: EcucScopeEnum) -> EcucDefinitionElement:
        """
        AUTOSAR-compliant setter for scope with method chaining.

        Args:
            value: The scope to set

        Returns:
            self for method chaining

        Note:
            Delegates to scope property setter (gets validation automatically)
        """
        self.scope = value  # Delegates to property setter
        return self

    def getUpperMultiplicity(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for upperMultiplicity.

        Returns:
            The upperMultiplicity value

        Note:
            Delegates to upper_multiplicity property (CODING_RULE_V2_00017)
        """
        return self.upper_multiplicity  # Delegates to property

    def setUpperMultiplicity(self, value: "Boolean") -> EcucDefinitionElement:
        """
        AUTOSAR-compliant setter for upperMultiplicity with method chaining.

        Args:
            value: The upperMultiplicity to set

        Returns:
            self for method chaining

        Note:
            Delegates to upper_multiplicity property setter (gets validation automatically)
        """
        self.upper_multiplicity = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecuc_cond(self, value: Optional["EcucCondition"]) -> EcucDefinitionElement:
        """
        Set ecucCond and return self for chaining.

        Args:
            value: The ecucCond to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_cond("value")
        """
        self.ecuc_cond = value  # Use property setter (gets validation)
        return self

    def with_lower_multiplicity(self, value: Optional["PositiveInteger"]) -> EcucDefinitionElement:
        """
        Set lowerMultiplicity and return self for chaining.

        Args:
            value: The lowerMultiplicity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lower_multiplicity("value")
        """
        self.lower_multiplicity = value  # Use property setter (gets validation)
        return self

    def with_related_trace(self, value: Optional["Traceable"]) -> EcucDefinitionElement:
        """
        Set relatedTrace and return self for chaining.

        Args:
            value: The relatedTrace to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_related_trace("value")
        """
        self.related_trace = value  # Use property setter (gets validation)
        return self

    def with_scope(self, value: Optional[EcucScopeEnum]) -> EcucDefinitionElement:
        """
        Set scope and return self for chaining.

        Args:
            value: The scope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scope("value")
        """
        self.scope = value  # Use property setter (gets validation)
        return self

    def with_upper_multiplicity(self, value: Optional["Boolean"]) -> EcucDefinitionElement:
        """
        Set upperMultiplicity and return self for chaining.

        Args:
            value: The upperMultiplicity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upper_multiplicity("value")
        """
        self.upper_multiplicity = value  # Use property setter (gets validation)
        return self



class EcucAbstractConfigurationClass(ARObject, ABC):
    """
    Specifies the ValueConfigurationClass of a parameter/reference or the
    MultiplicityConfigurationClass of a parameter/reference or a container for
    each ConfigurationVariant of the EcucModuleDef.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucAbstractConfigurationClass

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 51, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractConfigurationClass:
            raise TypeError("EcucAbstractConfigurationClass is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the ConfigurationClass for the given.
        self._configClass: Optional["EcucConfigurationClass"] = None

    @property
    def config_class(self) -> Optional["EcucConfigurationClass"]:
        """Get configClass (Pythonic accessor)."""
        return self._configClass

    @config_class.setter
    def config_class(self, value: Optional["EcucConfigurationClass"]) -> None:
        """
        Set configClass with validation.

        Args:
            value: The configClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._configClass = None
            return

        if not isinstance(value, EcucConfigurationClass):
            raise TypeError(
                f"configClass must be EcucConfigurationClass or None, got {type(value).__name__}"
            )
        self._configClass = value
        self._configVariant: Optional["EcucConfiguration"] = None

    @property
    def config_variant(self) -> Optional["EcucConfiguration"]:
        """Get configVariant (Pythonic accessor)."""
        return self._configVariant

    @config_variant.setter
    def config_variant(self, value: Optional["EcucConfiguration"]) -> None:
        """
        Set configVariant with validation.

        Args:
            value: The configVariant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._configVariant = None
            return

        if not isinstance(value, EcucConfiguration):
            raise TypeError(
                f"configVariant must be EcucConfiguration or None, got {type(value).__name__}"
            )
        self._configVariant = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConfigClass(self) -> "EcucConfigurationClass":
        """
        AUTOSAR-compliant getter for configClass.

        Returns:
            The configClass value

        Note:
            Delegates to config_class property (CODING_RULE_V2_00017)
        """
        return self.config_class  # Delegates to property

    def setConfigClass(self, value: "EcucConfigurationClass") -> EcucAbstractConfigurationClass:
        """
        AUTOSAR-compliant setter for configClass with method chaining.

        Args:
            value: The configClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to config_class property setter (gets validation automatically)
        """
        self.config_class = value  # Delegates to property setter
        return self

    def getConfigVariant(self) -> "EcucConfiguration":
        """
        AUTOSAR-compliant getter for configVariant.

        Returns:
            The configVariant value

        Note:
            Delegates to config_variant property (CODING_RULE_V2_00017)
        """
        return self.config_variant  # Delegates to property

    def setConfigVariant(self, value: "EcucConfiguration") -> EcucAbstractConfigurationClass:
        """
        AUTOSAR-compliant setter for configVariant with method chaining.

        Args:
            value: The configVariant to set

        Returns:
            self for method chaining

        Note:
            Delegates to config_variant property setter (gets validation automatically)
        """
        self.config_variant = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_config_class(self, value: Optional["EcucConfigurationClass"]) -> EcucAbstractConfigurationClass:
        """
        Set configClass and return self for chaining.

        Args:
            value: The configClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_config_class("value")
        """
        self.config_class = value  # Use property setter (gets validation)
        return self

    def with_config_variant(self, value: Optional["EcucConfiguration"]) -> EcucAbstractConfigurationClass:
        """
        Set configVariant and return self for chaining.

        Args:
            value: The configVariant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_config_variant("value")
        """
        self.config_variant = value  # Use property setter (gets validation)
        return self



class EcucAbstractStringParamDef(ARObject, ABC):
    """
    Abstract class that is used to collect the common properties for
    StringParamDefs, LinkerSymbolDef, FunctionNameDef and
    MultilineStringParamDefs. atpVariation: [RS_ECUC_00083] Tags:
    vh.latestBindingTime=codeGenerationTime

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucAbstractStringParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 63, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 183, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractStringParamDef:
            raise TypeError("EcucAbstractStringParamDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default value of the string configuration parameter.
        self._defaultValue: Optional["VerbatimString"] = None

    @property
    def default_value(self) -> Optional["VerbatimString"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["VerbatimString"]) -> None:
        """
        Set defaultValue with validation.

        Args:
            value: The defaultValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"defaultValue must be VerbatimString or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        self._maxLength: Optional["PositiveInteger"] = None

    @property
    def max_length(self) -> Optional["PositiveInteger"]:
        """Get maxLength (Pythonic accessor)."""
        return self._maxLength

    @max_length.setter
    def max_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxLength with validation.

        Args:
            value: The maxLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxLength = value
        self._minLength: Optional["PositiveInteger"] = None

    @property
    def min_length(self) -> Optional["PositiveInteger"]:
        """Get minLength (Pythonic accessor)."""
        return self._minLength

    @min_length.setter
    def min_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minLength with validation.

        Args:
            value: The minLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minLength = value
        # parameter value.
        self._regular: Optional["RegularExpression"] = None

    @property
    def regular(self) -> Optional["RegularExpression"]:
        """Get regular (Pythonic accessor)."""
        return self._regular

    @regular.setter
    def regular(self, value: Optional["RegularExpression"]) -> None:
        """
        Set regular with validation.

        Args:
            value: The regular to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._regular = None
            return

        if not isinstance(value, RegularExpression):
            raise TypeError(
                f"regular must be RegularExpression or None, got {type(value).__name__}"
            )
        self._regular = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "VerbatimString") -> EcucAbstractStringParamDef:
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getMaxLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxLength.

        Returns:
            The maxLength value

        Note:
            Delegates to max_length property (CODING_RULE_V2_00017)
        """
        return self.max_length  # Delegates to property

    def setMaxLength(self, value: "PositiveInteger") -> EcucAbstractStringParamDef:
        """
        AUTOSAR-compliant setter for maxLength with method chaining.

        Args:
            value: The maxLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_length property setter (gets validation automatically)
        """
        self.max_length = value  # Delegates to property setter
        return self

    def getMinLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minLength.

        Returns:
            The minLength value

        Note:
            Delegates to min_length property (CODING_RULE_V2_00017)
        """
        return self.min_length  # Delegates to property

    def setMinLength(self, value: "PositiveInteger") -> EcucAbstractStringParamDef:
        """
        AUTOSAR-compliant setter for minLength with method chaining.

        Args:
            value: The minLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_length property setter (gets validation automatically)
        """
        self.min_length = value  # Delegates to property setter
        return self

    def getRegular(self) -> "RegularExpression":
        """
        AUTOSAR-compliant getter for regular.

        Returns:
            The regular value

        Note:
            Delegates to regular property (CODING_RULE_V2_00017)
        """
        return self.regular  # Delegates to property

    def setRegular(self, value: "RegularExpression") -> EcucAbstractStringParamDef:
        """
        AUTOSAR-compliant setter for regular with method chaining.

        Args:
            value: The regular to set

        Returns:
            self for method chaining

        Note:
            Delegates to regular property setter (gets validation automatically)
        """
        self.regular = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["VerbatimString"]) -> EcucAbstractStringParamDef:
        """
        Set defaultValue and return self for chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self

    def with_max_length(self, value: Optional["PositiveInteger"]) -> EcucAbstractStringParamDef:
        """
        Set maxLength and return self for chaining.

        Args:
            value: The maxLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_length("value")
        """
        self.max_length = value  # Use property setter (gets validation)
        return self

    def with_min_length(self, value: Optional["PositiveInteger"]) -> EcucAbstractStringParamDef:
        """
        Set minLength and return self for chaining.

        Args:
            value: The minLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_length("value")
        """
        self.min_length = value  # Use property setter (gets validation)
        return self

    def with_regular(self, value: Optional["RegularExpression"]) -> EcucAbstractStringParamDef:
        """
        Set regular and return self for chaining.

        Args:
            value: The regular to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_regular("value")
        """
        self.regular = value  # Use property setter (gets validation)
        return self



class EcucStringParamDef(ARObject):
    """
    Configuration parameter type for String.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucStringParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 64, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucMultilineStringParamDef(ARObject):
    """
    Configuration parameter type for multiline Strings (including "carriage
    return").

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucMultilineStringParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 64, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucLinkerSymbolDef(ARObject):
    """
    Configuration parameter type for Linker Symbol Names like those used to
    specify memory locations of variables and constants.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucLinkerSymbolDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 65, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucFunctionNameDef(ARObject):
    """
    Configuration parameter type for Function Names like those used to specify
    callback functions.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucFunctionNameDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 65, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucEnumerationLiteralDef(Identifiable):
    """
    Configuration parameter type for enumeration literals definition.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucEnumerationLiteralDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 67, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If it evaluates to true the literal definition shall be as specified.
        # Otherwise the literal definition ignored.
        self._ecucCond: Optional["EcucCondition"] = None

    @property
    def ecuc_cond(self) -> Optional["EcucCondition"]:
        """Get ecucCond (Pythonic accessor)."""
        return self._ecucCond

    @ecuc_cond.setter
    def ecuc_cond(self, value: Optional["EcucCondition"]) -> None:
        """
        Set ecucCond with validation.

        Args:
            value: The ecucCond to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecucCond = None
            return

        if not isinstance(value, EcucCondition):
            raise TypeError(
                f"ecucCond must be EcucCondition or None, got {type(value).__name__}"
            )
        self._ecucCond = value
        # vendor-specific.
        self._origin: Optional["String"] = None

    @property
    def origin(self) -> Optional["String"]:
        """Get origin (Pythonic accessor)."""
        return self._origin

    @origin.setter
    def origin(self, value: Optional["String"]) -> None:
        """
        Set origin with validation.

        Args:
            value: The origin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._origin = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"origin must be String or str or None, got {type(value).__name__}"
            )
        self._origin = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucCond(self) -> "EcucCondition":
        """
        AUTOSAR-compliant getter for ecucCond.

        Returns:
            The ecucCond value

        Note:
            Delegates to ecuc_cond property (CODING_RULE_V2_00017)
        """
        return self.ecuc_cond  # Delegates to property

    def setEcucCond(self, value: "EcucCondition") -> EcucEnumerationLiteralDef:
        """
        AUTOSAR-compliant setter for ecucCond with method chaining.

        Args:
            value: The ecucCond to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecuc_cond property setter (gets validation automatically)
        """
        self.ecuc_cond = value  # Delegates to property setter
        return self

    def getOrigin(self) -> "String":
        """
        AUTOSAR-compliant getter for origin.

        Returns:
            The origin value

        Note:
            Delegates to origin property (CODING_RULE_V2_00017)
        """
        return self.origin  # Delegates to property

    def setOrigin(self, value: "String") -> EcucEnumerationLiteralDef:
        """
        AUTOSAR-compliant setter for origin with method chaining.

        Args:
            value: The origin to set

        Returns:
            self for method chaining

        Note:
            Delegates to origin property setter (gets validation automatically)
        """
        self.origin = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecuc_cond(self, value: Optional["EcucCondition"]) -> EcucEnumerationLiteralDef:
        """
        Set ecucCond and return self for chaining.

        Args:
            value: The ecucCond to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_cond("value")
        """
        self.ecuc_cond = value  # Use property setter (gets validation)
        return self

    def with_origin(self, value: Optional["String"]) -> EcucEnumerationLiteralDef:
        """
        Set origin and return self for chaining.

        Args:
            value: The origin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_origin("value")
        """
        self.origin = value  # Use property setter (gets validation)
        return self



class EcucDestinationUriDefSet(ARElement):
    """
    This class represents a list of EcucDestinationUriDefs.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDestinationUriDefSet

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 82, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular EcucDestinationUriDef.
        self._destinationUriDef: List[EcucDestinationUriDef] = []

    @property
    def destination_uri_def(self) -> List[EcucDestinationUriDef]:
        """Get destinationUriDef (Pythonic accessor)."""
        return self._destinationUriDef

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationUriDef(self) -> List[EcucDestinationUriDef]:
        """
        AUTOSAR-compliant getter for destinationUriDef.

        Returns:
            The destinationUriDef value

        Note:
            Delegates to destination_uri_def property (CODING_RULE_V2_00017)
        """
        return self.destination_uri_def  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucDestinationUriDef(Identifiable):
    """
    Description of an EcucDestinationUriDef that is used as target of
    EcucUriReferenceDefs.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDestinationUriDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 82, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Description of the targeted EcucContainerDef.
        self._destinationUri: Optional["EcucDestinationUri"] = None

    @property
    def destination_uri(self) -> Optional["EcucDestinationUri"]:
        """Get destinationUri (Pythonic accessor)."""
        return self._destinationUri

    @destination_uri.setter
    def destination_uri(self, value: Optional["EcucDestinationUri"]) -> None:
        """
        Set destinationUri with validation.

        Args:
            value: The destinationUri to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationUri = None
            return

        if not isinstance(value, EcucDestinationUri):
            raise TypeError(
                f"destinationUri must be EcucDestinationUri or None, got {type(value).__name__}"
            )
        self._destinationUri = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationUri(self) -> "EcucDestinationUri":
        """
        AUTOSAR-compliant getter for destinationUri.

        Returns:
            The destinationUri value

        Note:
            Delegates to destination_uri property (CODING_RULE_V2_00017)
        """
        return self.destination_uri  # Delegates to property

    def setDestinationUri(self, value: "EcucDestinationUri") -> EcucDestinationUriDef:
        """
        AUTOSAR-compliant setter for destinationUri with method chaining.

        Args:
            value: The destinationUri to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_uri property setter (gets validation automatically)
        """
        self.destination_uri = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_uri(self, value: Optional["EcucDestinationUri"]) -> EcucDestinationUriDef:
        """
        Set destinationUri and return self for chaining.

        Args:
            value: The destinationUri to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_uri("value")
        """
        self.destination_uri = value  # Use property setter (gets validation)
        return self



class EcucDestinationUriPolicy(ARObject):
    """
    The EcucDestinationUriPolicy describes the EcucContainerDef that will be
    targeted by EcucUriReference Defs. The type of the description is dependent
    of the destinationUriNestingContract attribute.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDestinationUriPolicy

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 83, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Description of the targetContainer in case that the set to targetContainer.
        # In cases the subContainers of the target container here.
        self._container: List[EcucContainerDef] = []

    @property
    def container(self) -> List[EcucContainerDef]:
        """Get container (Pythonic accessor)."""
        return self._container
        # This attribute defines how the referenced target Ecuc ContainerDef is
        # described.
        self._destinationUri: Optional["EcucDestinationUri"] = None

    @property
    def destination_uri(self) -> Optional["EcucDestinationUri"]:
        """Get destinationUri (Pythonic accessor)."""
        return self._destinationUri

    @destination_uri.setter
    def destination_uri(self, value: Optional["EcucDestinationUri"]) -> None:
        """
        Set destinationUri with validation.

        Args:
            value: The destinationUri to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationUri = None
            return

        if not isinstance(value, EcucDestinationUri):
            raise TypeError(
                f"destinationUri must be EcucDestinationUri or None, got {type(value).__name__}"
            )
        self._destinationUri = value
        self._parameter: List[EcucParameterDef] = []

    @property
    def parameter(self) -> List[EcucParameterDef]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter
        # Description of references that are contained in the target.
        self._reference: List["RefType"] = []

    @property
    def reference(self) -> List["RefType"]:
        """Get reference (Pythonic accessor)."""
        return self._reference

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContainer(self) -> List[EcucContainerDef]:
        """
        AUTOSAR-compliant getter for container.

        Returns:
            The container value

        Note:
            Delegates to container property (CODING_RULE_V2_00017)
        """
        return self.container  # Delegates to property

    def getDestinationUri(self) -> "EcucDestinationUri":
        """
        AUTOSAR-compliant getter for destinationUri.

        Returns:
            The destinationUri value

        Note:
            Delegates to destination_uri property (CODING_RULE_V2_00017)
        """
        return self.destination_uri  # Delegates to property

    def setDestinationUri(self, value: "EcucDestinationUri") -> EcucDestinationUriPolicy:
        """
        AUTOSAR-compliant setter for destinationUri with method chaining.

        Args:
            value: The destinationUri to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_uri property setter (gets validation automatically)
        """
        self.destination_uri = value  # Delegates to property setter
        return self

    def getParameter(self) -> List[EcucParameterDef]:
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def getReference(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for reference.

        Returns:
            The reference value

        Note:
            Delegates to reference property (CODING_RULE_V2_00017)
        """
        return self.reference  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_uri(self, value: Optional["EcucDestinationUri"]) -> EcucDestinationUriPolicy:
        """
        Set destinationUri and return self for chaining.

        Args:
            value: The destinationUri to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_uri("value")
        """
        self.destination_uri = value  # Use property setter (gets validation)
        return self



class EcucDerivationSpecification(ARObject):
    """
    Allows to define configuration items that are calculated based on the value
    of • other parameter values • elements (attributes/classes) defined in other
    AUTOSAR templates such as System template and SW component template

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDerivationSpecification

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 87, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the formula used to calculate the value of the configuration
        # element.
        self._calculation: Optional["EcucParameter"] = None

    @property
    def calculation(self) -> Optional["EcucParameter"]:
        """Get calculation (Pythonic accessor)."""
        return self._calculation

    @calculation.setter
    def calculation(self, value: Optional["EcucParameter"]) -> None:
        """
        Set calculation with validation.

        Args:
            value: The calculation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calculation = None
            return

        if not isinstance(value, EcucParameter):
            raise TypeError(
                f"calculation must be EcucParameter or None, got {type(value).__name__}"
            )
        self._calculation = value
        self._ecucQuery: List[EcucQuery] = []

    @property
    def ecuc_query(self) -> List[EcucQuery]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery
        # Informal description of the derivation used to calculate the the
        # configuration element.
        self._informalFormula: Optional["MlFormula"] = None

    @property
    def informal_formula(self) -> Optional["MlFormula"]:
        """Get informalFormula (Pythonic accessor)."""
        return self._informalFormula

    @informal_formula.setter
    def informal_formula(self, value: Optional["MlFormula"]) -> None:
        """
        Set informalFormula with validation.

        Args:
            value: The informalFormula to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._informalFormula = None
            return

        if not isinstance(value, MlFormula):
            raise TypeError(
                f"informalFormula must be MlFormula or None, got {type(value).__name__}"
            )
        self._informalFormula = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalculation(self) -> "EcucParameter":
        """
        AUTOSAR-compliant getter for calculation.

        Returns:
            The calculation value

        Note:
            Delegates to calculation property (CODING_RULE_V2_00017)
        """
        return self.calculation  # Delegates to property

    def setCalculation(self, value: "EcucParameter") -> EcucDerivationSpecification:
        """
        AUTOSAR-compliant setter for calculation with method chaining.

        Args:
            value: The calculation to set

        Returns:
            self for method chaining

        Note:
            Delegates to calculation property setter (gets validation automatically)
        """
        self.calculation = value  # Delegates to property setter
        return self

    def getEcucQuery(self) -> List[EcucQuery]:
        """
        AUTOSAR-compliant getter for ecucQuery.

        Returns:
            The ecucQuery value

        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def getInformalFormula(self) -> "MlFormula":
        """
        AUTOSAR-compliant getter for informalFormula.

        Returns:
            The informalFormula value

        Note:
            Delegates to informal_formula property (CODING_RULE_V2_00017)
        """
        return self.informal_formula  # Delegates to property

    def setInformalFormula(self, value: "MlFormula") -> EcucDerivationSpecification:
        """
        AUTOSAR-compliant setter for informalFormula with method chaining.

        Args:
            value: The informalFormula to set

        Returns:
            self for method chaining

        Note:
            Delegates to informal_formula property setter (gets validation automatically)
        """
        self.informal_formula = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_calculation(self, value: Optional["EcucParameter"]) -> EcucDerivationSpecification:
        """
        Set calculation and return self for chaining.

        Args:
            value: The calculation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_calculation("value")
        """
        self.calculation = value  # Use property setter (gets validation)
        return self

    def with_informal_formula(self, value: Optional["MlFormula"]) -> EcucDerivationSpecification:
        """
        Set informalFormula and return self for chaining.

        Args:
            value: The informalFormula to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_informal_formula("value")
        """
        self.informal_formula = value  # Use property setter (gets validation)
        return self



class EcucParameterDerivationFormula(ARObject):
    """
    This formula is intended to specify how an ecu parameter can be derived from
    other information in the Autosar Templates.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucParameterDerivationFormula

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 88, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This indicates that the referenced query shall return a.
        self._ecucQuery: Optional[EcucQuery] = None

    @property
    def ecuc_query(self) -> Optional[EcucQuery]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery

    @ecuc_query.setter
    def ecuc_query(self, value: Optional[EcucQuery]) -> None:
        """
        Set ecucQuery with validation.

        Args:
            value: The ecucQuery to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecucQuery = None
            return

        if not isinstance(value, EcucQuery):
            raise TypeError(
                f"ecucQuery must be EcucQuery or None, got {type(value).__name__}"
            )
        self._ecucQuery = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucQuery(self) -> EcucQuery:
        """
        AUTOSAR-compliant getter for ecucQuery.

        Returns:
            The ecucQuery value

        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def setEcucQuery(self, value: EcucQuery) -> EcucParameterDerivationFormula:
        """
        AUTOSAR-compliant setter for ecucQuery with method chaining.

        Args:
            value: The ecucQuery to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecuc_query property setter (gets validation automatically)
        """
        self.ecuc_query = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecuc_query(self, value: Optional[EcucQuery]) -> EcucParameterDerivationFormula:
        """
        Set ecucQuery and return self for chaining.

        Args:
            value: The ecucQuery to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_query("value")
        """
        self.ecuc_query = value  # Use property setter (gets validation)
        return self



class EcucQuery(Identifiable):
    """
    Defines a query to the ECUC Description.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucQuery

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 89, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the EcucQuery used in the calculation formula or condition formula.
        self._ecucQuery: Optional[EcucQueryExpression] = None

    @property
    def ecuc_query(self) -> Optional[EcucQueryExpression]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery

    @ecuc_query.setter
    def ecuc_query(self, value: Optional[EcucQueryExpression]) -> None:
        """
        Set ecucQuery with validation.

        Args:
            value: The ecucQuery to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecucQuery = None
            return

        if not isinstance(value, EcucQueryExpression):
            raise TypeError(
                f"ecucQuery must be EcucQueryExpression or None, got {type(value).__name__}"
            )
        self._ecucQuery = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucQuery(self) -> EcucQueryExpression:
        """
        AUTOSAR-compliant getter for ecucQuery.

        Returns:
            The ecucQuery value

        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def setEcucQuery(self, value: EcucQueryExpression) -> EcucQuery:
        """
        AUTOSAR-compliant setter for ecucQuery with method chaining.

        Args:
            value: The ecucQuery to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecuc_query property setter (gets validation automatically)
        """
        self.ecuc_query = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecuc_query(self, value: Optional[EcucQueryExpression]) -> EcucQuery:
        """
        Set ecucQuery and return self for chaining.

        Args:
            value: The ecucQuery to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_query("value")
        """
        self.ecuc_query = value  # Use property setter (gets validation)
        return self



class EcucQueryExpression(ARObject):
    """
    Defines a query expression to the ECUC Description and output the result as
    an numerical value. Due to the "mixedString" nature of the formula there can
    be several EcuQueryExpressions used.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucQueryExpression

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 89, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The EcucQueryExpression points to an EcucDefinition that is used to find an
                # element in the Ecuc order to find the right element in the Ecuc search is
                # necessary.
        # If the search is of the same module that contains the local reference shall
                # be used.
        # Due to the of the EcucQueryExpression several EcucDefintionElements can be
                # used in one.
        self._configElement: Optional[EcucDefinitionElement] = None

    @property
    def config_element(self) -> Optional[EcucDefinitionElement]:
        """Get configElement (Pythonic accessor)."""
        return self._configElement

    @config_element.setter
    def config_element(self, value: Optional[EcucDefinitionElement]) -> None:
        """
        Set configElement with validation.

        Args:
            value: The configElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._configElement = None
            return

        if not isinstance(value, EcucDefinitionElement):
            raise TypeError(
                f"configElement must be EcucDefinitionElement or None, got {type(value).__name__}"
            )
        self._configElement = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConfigElement(self) -> EcucDefinitionElement:
        """
        AUTOSAR-compliant getter for configElement.

        Returns:
            The configElement value

        Note:
            Delegates to config_element property (CODING_RULE_V2_00017)
        """
        return self.config_element  # Delegates to property

    def setConfigElement(self, value: EcucDefinitionElement) -> EcucQueryExpression:
        """
        AUTOSAR-compliant setter for configElement with method chaining.

        Args:
            value: The configElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to config_element property setter (gets validation automatically)
        """
        self.config_element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_config_element(self, value: Optional[EcucDefinitionElement]) -> EcucQueryExpression:
        """
        Set configElement and return self for chaining.

        Args:
            value: The configElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_config_element("value")
        """
        self.config_element = value  # Use property setter (gets validation)
        return self



class EcucConditionSpecification(ARObject):
    """
    Allows to define existence dependencies based on the value of parameter
    values.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucConditionSpecification

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 100, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the formula used to define existence.
        self._condition: Optional[EcucConditionFormula] = None

    @property
    def condition(self) -> Optional[EcucConditionFormula]:
        """Get condition (Pythonic accessor)."""
        return self._condition

    @condition.setter
    def condition(self, value: Optional[EcucConditionFormula]) -> None:
        """
        Set condition with validation.

        Args:
            value: The condition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._condition = None
            return

        if not isinstance(value, EcucConditionFormula):
            raise TypeError(
                f"condition must be EcucConditionFormula or None, got {type(value).__name__}"
            )
        self._condition = value
        self._ecucQuery: List[EcucQuery] = []

    @property
    def ecuc_query(self) -> List[EcucQuery]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery
        # Informal description of the condition used to to define.
        self._informalFormula: Optional["MlFormula"] = None

    @property
    def informal_formula(self) -> Optional["MlFormula"]:
        """Get informalFormula (Pythonic accessor)."""
        return self._informalFormula

    @informal_formula.setter
    def informal_formula(self, value: Optional["MlFormula"]) -> None:
        """
        Set informalFormula with validation.

        Args:
            value: The informalFormula to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._informalFormula = None
            return

        if not isinstance(value, MlFormula):
            raise TypeError(
                f"informalFormula must be MlFormula or None, got {type(value).__name__}"
            )
        self._informalFormula = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCondition(self) -> EcucConditionFormula:
        """
        AUTOSAR-compliant getter for condition.

        Returns:
            The condition value

        Note:
            Delegates to condition property (CODING_RULE_V2_00017)
        """
        return self.condition  # Delegates to property

    def setCondition(self, value: EcucConditionFormula) -> EcucConditionSpecification:
        """
        AUTOSAR-compliant setter for condition with method chaining.

        Args:
            value: The condition to set

        Returns:
            self for method chaining

        Note:
            Delegates to condition property setter (gets validation automatically)
        """
        self.condition = value  # Delegates to property setter
        return self

    def getEcucQuery(self) -> List[EcucQuery]:
        """
        AUTOSAR-compliant getter for ecucQuery.

        Returns:
            The ecucQuery value

        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def getInformalFormula(self) -> "MlFormula":
        """
        AUTOSAR-compliant getter for informalFormula.

        Returns:
            The informalFormula value

        Note:
            Delegates to informal_formula property (CODING_RULE_V2_00017)
        """
        return self.informal_formula  # Delegates to property

    def setInformalFormula(self, value: "MlFormula") -> EcucConditionSpecification:
        """
        AUTOSAR-compliant setter for informalFormula with method chaining.

        Args:
            value: The informalFormula to set

        Returns:
            self for method chaining

        Note:
            Delegates to informal_formula property setter (gets validation automatically)
        """
        self.informal_formula = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_condition(self, value: Optional[EcucConditionFormula]) -> EcucConditionSpecification:
        """
        Set condition and return self for chaining.

        Args:
            value: The condition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_condition("value")
        """
        self.condition = value  # Use property setter (gets validation)
        return self

    def with_informal_formula(self, value: Optional["MlFormula"]) -> EcucConditionSpecification:
        """
        Set informalFormula and return self for chaining.

        Args:
            value: The informalFormula to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_informal_formula("value")
        """
        self.informal_formula = value  # Use property setter (gets validation)
        return self



class EcucConditionFormula(ARObject):
    """
    This formula shall yield a boolean expression depending on ecuc queries.
    Note that the EcucCondition Formula is a mixed string. Therefore, the
    properties have the upper multiplicity 1.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucConditionFormula

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 100, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This indicates that the referenced query shall return a.
        self._ecucQuery: Optional[EcucQuery] = None

    @property
    def ecuc_query(self) -> Optional[EcucQuery]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery

    @ecuc_query.setter
    def ecuc_query(self, value: Optional[EcucQuery]) -> None:
        """
        Set ecucQuery with validation.

        Args:
            value: The ecucQuery to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecucQuery = None
            return

        if not isinstance(value, EcucQuery):
            raise TypeError(
                f"ecucQuery must be EcucQuery or None, got {type(value).__name__}"
            )
        self._ecucQuery = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucQuery(self) -> EcucQuery:
        """
        AUTOSAR-compliant getter for ecucQuery.

        Returns:
            The ecucQuery value

        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def setEcucQuery(self, value: EcucQuery) -> EcucConditionFormula:
        """
        AUTOSAR-compliant setter for ecucQuery with method chaining.

        Args:
            value: The ecucQuery to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecuc_query property setter (gets validation automatically)
        """
        self.ecuc_query = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecuc_query(self, value: Optional[EcucQuery]) -> EcucConditionFormula:
        """
        Set ecucQuery and return self for chaining.

        Args:
            value: The ecucQuery to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_query("value")
        """
        self.ecuc_query = value  # Use property setter (gets validation)
        return self



class EcucValidationCondition(Identifiable):
    """
    Validation condition to perform a formula calculation based on EcucQueries.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucValidationCondition

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 103, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Query to the ECU Configuration Description.
        self._ecucQuery: List[EcucQuery] = []

    @property
    def ecuc_query(self) -> List[EcucQuery]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery
        # Definition of the formula used to define validation.
        self._validation: Optional[EcucConditionFormula] = None

    @property
    def validation(self) -> Optional[EcucConditionFormula]:
        """Get validation (Pythonic accessor)."""
        return self._validation

    @validation.setter
    def validation(self, value: Optional[EcucConditionFormula]) -> None:
        """
        Set validation with validation.

        Args:
            value: The validation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._validation = None
            return

        if not isinstance(value, EcucConditionFormula):
            raise TypeError(
                f"validation must be EcucConditionFormula or None, got {type(value).__name__}"
            )
        self._validation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucQuery(self) -> List[EcucQuery]:
        """
        AUTOSAR-compliant getter for ecucQuery.

        Returns:
            The ecucQuery value

        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def getValidation(self) -> EcucConditionFormula:
        """
        AUTOSAR-compliant getter for validation.

        Returns:
            The validation value

        Note:
            Delegates to validation property (CODING_RULE_V2_00017)
        """
        return self.validation  # Delegates to property

    def setValidation(self, value: EcucConditionFormula) -> EcucValidationCondition:
        """
        AUTOSAR-compliant setter for validation with method chaining.

        Args:
            value: The validation to set

        Returns:
            self for method chaining

        Note:
            Delegates to validation property setter (gets validation automatically)
        """
        self.validation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_validation(self, value: Optional[EcucConditionFormula]) -> EcucValidationCondition:
        """
        Set validation and return self for chaining.

        Args:
            value: The validation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_validation("value")
        """
        self.validation = value  # Use property setter (gets validation)
        return self



class EcucModuleDef(EcucDefinitionElement):
    """
    Used as the top-level element for configuration definition for Software
    Modules, including BSW and RTE as well as ECU Infrastructure.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucModuleDef

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 314, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 32, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 187, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # For modules where several instances of the VSMD can the apiServicePrefix
                # defines the API the derived instances, e.
        # g.
        # Cdd, Xfrm E2EXf).
        self._apiServicePrefix: Optional["CIdentifier"] = None

    @property
    def api_service_prefix(self) -> Optional["CIdentifier"]:
        """Get apiServicePrefix (Pythonic accessor)."""
        return self._apiServicePrefix

    @api_service_prefix.setter
    def api_service_prefix(self, value: Optional["CIdentifier"]) -> None:
        """
        Set apiServicePrefix with validation.

        Args:
            value: The apiServicePrefix to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._apiServicePrefix = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"apiServicePrefix must be CIdentifier or None, got {type(value).__name__}"
            )
        self._apiServicePrefix = value
        self._container: List[EcucContainerDef] = []

    @property
    def container(self) -> List[EcucContainerDef]:
        """Get container (Pythonic accessor)."""
        return self._container
        # Indicates if a module supports different post-build variants known as
        # post-build selectable configuration means yes, FALSE means no.
        self._postBuildVariant: Optional["Boolean"] = None

    @property
    def post_build_variant(self) -> Optional["Boolean"]:
        """Get postBuildVariant (Pythonic accessor)."""
        return self._postBuildVariant

    @post_build_variant.setter
    def post_build_variant(self, value: Optional["Boolean"]) -> None:
        """
        Set postBuildVariant with validation.

        Args:
            value: The postBuildVariant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._postBuildVariant = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"postBuildVariant must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._postBuildVariant = value
                # Definition it refines.
        # this EcucModuleDef has the category reference be provided.
        # In case this EcucModuleDef has VENDOR_SPECIFIC_MODULE_ reference is
                # mandatory.
        self._refinedModule: Optional[EcucModuleDef] = None

    @property
    def refined_module(self) -> Optional[EcucModuleDef]:
        """Get refinedModule (Pythonic accessor)."""
        return self._refinedModule

    @refined_module.setter
    def refined_module(self, value: Optional[EcucModuleDef]) -> None:
        """
        Set refinedModule with validation.

        Args:
            value: The refinedModule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._refinedModule = None
            return

        if not isinstance(value, EcucModuleDef):
            raise TypeError(
                f"refinedModule must be EcucModuleDef or None, got {type(value).__name__}"
            )
        self._refinedModule = value
        # This attribute is optional if the Ecuc the category STANDARDIZED_ the
                # category attribute of the set to VENDOR_SPECIFIC_ this attribute is
                # mandatory.
        self._supported: List["EcucConfiguration"] = []

    @property
    def supported(self) -> List["EcucConfiguration"]:
        """Get supported (Pythonic accessor)."""
        return self._supported

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApiServicePrefix(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for apiServicePrefix.

        Returns:
            The apiServicePrefix value

        Note:
            Delegates to api_service_prefix property (CODING_RULE_V2_00017)
        """
        return self.api_service_prefix  # Delegates to property

    def setApiServicePrefix(self, value: "CIdentifier") -> EcucModuleDef:
        """
        AUTOSAR-compliant setter for apiServicePrefix with method chaining.

        Args:
            value: The apiServicePrefix to set

        Returns:
            self for method chaining

        Note:
            Delegates to api_service_prefix property setter (gets validation automatically)
        """
        self.api_service_prefix = value  # Delegates to property setter
        return self

    def getContainer(self) -> List[EcucContainerDef]:
        """
        AUTOSAR-compliant getter for container.

        Returns:
            The container value

        Note:
            Delegates to container property (CODING_RULE_V2_00017)
        """
        return self.container  # Delegates to property

    def getPostBuildVariant(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for postBuildVariant.

        Returns:
            The postBuildVariant value

        Note:
            Delegates to post_build_variant property (CODING_RULE_V2_00017)
        """
        return self.post_build_variant  # Delegates to property

    def setPostBuildVariant(self, value: "Boolean") -> EcucModuleDef:
        """
        AUTOSAR-compliant setter for postBuildVariant with method chaining.

        Args:
            value: The postBuildVariant to set

        Returns:
            self for method chaining

        Note:
            Delegates to post_build_variant property setter (gets validation automatically)
        """
        self.post_build_variant = value  # Delegates to property setter
        return self

    def getRefinedModule(self) -> EcucModuleDef:
        """
        AUTOSAR-compliant getter for refinedModule.

        Returns:
            The refinedModule value

        Note:
            Delegates to refined_module property (CODING_RULE_V2_00017)
        """
        return self.refined_module  # Delegates to property

    def setRefinedModule(self, value: EcucModuleDef) -> EcucModuleDef:
        """
        AUTOSAR-compliant setter for refinedModule with method chaining.

        Args:
            value: The refinedModule to set

        Returns:
            self for method chaining

        Note:
            Delegates to refined_module property setter (gets validation automatically)
        """
        self.refined_module = value  # Delegates to property setter
        return self

    def getSupported(self) -> List["EcucConfiguration"]:
        """
        AUTOSAR-compliant getter for supported.

        Returns:
            The supported value

        Note:
            Delegates to supported property (CODING_RULE_V2_00017)
        """
        return self.supported  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_api_service_prefix(self, value: Optional["CIdentifier"]) -> EcucModuleDef:
        """
        Set apiServicePrefix and return self for chaining.

        Args:
            value: The apiServicePrefix to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_api_service_prefix("value")
        """
        self.api_service_prefix = value  # Use property setter (gets validation)
        return self

    def with_post_build_variant(self, value: Optional["Boolean"]) -> EcucModuleDef:
        """
        Set postBuildVariant and return self for chaining.

        Args:
            value: The postBuildVariant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_post_build_variant("value")
        """
        self.post_build_variant = value  # Use property setter (gets validation)
        return self

    def with_refined_module(self, value: Optional[EcucModuleDef]) -> EcucModuleDef:
        """
        Set refinedModule and return self for chaining.

        Args:
            value: The refinedModule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_refined_module("value")
        """
        self.refined_module = value  # Use property setter (gets validation)
        return self



class EcucContainerDef(EcucDefinitionElement, ABC):
    """
    Base class used to gather common attributes of configuration container
    definitions.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucContainerDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 36, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2020, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 184, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is EcucContainerDef:
            raise TypeError("EcucContainerDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Several destinationUris can be defined for an Ecuc such destinationUris an
        # Ecuc applicable for several EcucUriReference.
        self._destinationUri: List[EcucDestinationUriDef] = []

    @property
    def destination_uri(self) -> List[EcucDestinationUriDef]:
        """Get destinationUri (Pythonic accessor)."""
        return self._destinationUri
        # Specifies which MultiplicityConfigurationClass this container is available
                # for which ConfigurationVariant.
        # This optional if the surrounding EcucModuleDef Category STANDARDIZED_MODULE_
                # the category attribute of the EcucModule set to VENDOR_SPECIFIC_MODULE_ if
                # the upperMultiplicity is greater than then this aggregation is mandatory.
        self._multiplicity: List["EcucMultiplicity"] = []

    @property
    def multiplicity(self) -> List["EcucMultiplicity"]:
        """Get multiplicity (Pythonic accessor)."""
        return self._multiplicity
        # This attribute specifies whether this configuration an AUTOSAR standardized
                # container or is vendor-specific.
        # 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration ECU Configuration R23-11.
        self._origin: Optional["String"] = None

    @property
    def origin(self) -> Optional["String"]:
        """Get origin (Pythonic accessor)."""
        return self._origin

    @origin.setter
    def origin(self, value: Optional["String"]) -> None:
        """
        Set origin with validation.

        Args:
            value: The origin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._origin = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"origin must be String or str or None, got {type(value).__name__}"
            )
        self._origin = value
                # variants (previously post-build selectable configuration sets).
        # TRUE FALSE means no.
        self._postBuildVariant: Optional["Boolean"] = None

    @property
    def post_build_variant(self) -> Optional["Boolean"]:
        """Get postBuildVariant (Pythonic accessor)."""
        return self._postBuildVariant

    @post_build_variant.setter
    def post_build_variant(self, value: Optional["Boolean"]) -> None:
        """
        Set postBuildVariant with validation.

        Args:
            value: The postBuildVariant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._postBuildVariant = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"postBuildVariant must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._postBuildVariant = value
        self._requiresIndex: Optional["Boolean"] = None

    @property
    def requires_index(self) -> Optional["Boolean"]:
        """Get requiresIndex (Pythonic accessor)."""
        return self._requiresIndex

    @requires_index.setter
    def requires_index(self, value: Optional["Boolean"]) -> None:
        """
        Set requiresIndex with validation.

        Args:
            value: The requiresIndex to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requiresIndex = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"requiresIndex must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._requiresIndex = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationUri(self) -> List[EcucDestinationUriDef]:
        """
        AUTOSAR-compliant getter for destinationUri.

        Returns:
            The destinationUri value

        Note:
            Delegates to destination_uri property (CODING_RULE_V2_00017)
        """
        return self.destination_uri  # Delegates to property

    def getMultiplicity(self) -> List["EcucMultiplicity"]:
        """
        AUTOSAR-compliant getter for multiplicity.

        Returns:
            The multiplicity value

        Note:
            Delegates to multiplicity property (CODING_RULE_V2_00017)
        """
        return self.multiplicity  # Delegates to property

    def getOrigin(self) -> "String":
        """
        AUTOSAR-compliant getter for origin.

        Returns:
            The origin value

        Note:
            Delegates to origin property (CODING_RULE_V2_00017)
        """
        return self.origin  # Delegates to property

    def setOrigin(self, value: "String") -> EcucContainerDef:
        """
        AUTOSAR-compliant setter for origin with method chaining.

        Args:
            value: The origin to set

        Returns:
            self for method chaining

        Note:
            Delegates to origin property setter (gets validation automatically)
        """
        self.origin = value  # Delegates to property setter
        return self

    def getPostBuildVariant(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for postBuildVariant.

        Returns:
            The postBuildVariant value

        Note:
            Delegates to post_build_variant property (CODING_RULE_V2_00017)
        """
        return self.post_build_variant  # Delegates to property

    def setPostBuildVariant(self, value: "Boolean") -> EcucContainerDef:
        """
        AUTOSAR-compliant setter for postBuildVariant with method chaining.

        Args:
            value: The postBuildVariant to set

        Returns:
            self for method chaining

        Note:
            Delegates to post_build_variant property setter (gets validation automatically)
        """
        self.post_build_variant = value  # Delegates to property setter
        return self

    def getRequiresIndex(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for requiresIndex.

        Returns:
            The requiresIndex value

        Note:
            Delegates to requires_index property (CODING_RULE_V2_00017)
        """
        return self.requires_index  # Delegates to property

    def setRequiresIndex(self, value: "Boolean") -> EcucContainerDef:
        """
        AUTOSAR-compliant setter for requiresIndex with method chaining.

        Args:
            value: The requiresIndex to set

        Returns:
            self for method chaining

        Note:
            Delegates to requires_index property setter (gets validation automatically)
        """
        self.requires_index = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_origin(self, value: Optional["String"]) -> EcucContainerDef:
        """
        Set origin and return self for chaining.

        Args:
            value: The origin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_origin("value")
        """
        self.origin = value  # Use property setter (gets validation)
        return self

    def with_post_build_variant(self, value: Optional["Boolean"]) -> EcucContainerDef:
        """
        Set postBuildVariant and return self for chaining.

        Args:
            value: The postBuildVariant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_post_build_variant("value")
        """
        self.post_build_variant = value  # Use property setter (gets validation)
        return self

    def with_requires_index(self, value: Optional["Boolean"]) -> EcucContainerDef:
        """
        Set requiresIndex and return self for chaining.

        Args:
            value: The requiresIndex to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requires_index("value")
        """
        self.requires_index = value  # Use property setter (gets validation)
        return self



class EcucCommonAttributes(EcucDefinitionElement, ABC):
    """
    Attributes used by Configuration Parameters as well as References.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucCommonAttributes

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 48, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucCommonAttributes:
            raise TypeError("EcucCommonAttributes is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies in which MultiplicityConfigurationClass this parameter or reference
        # is available in a particular aggregation is optional if the has the Category
        # the of the EcucModuleDef is set to this mandatory.
        self._multiplicity: List["EcucMultiplicity"] = []

    @property
    def multiplicity(self) -> List["EcucMultiplicity"]:
        """Get multiplicity (Pythonic accessor)."""
        return self._multiplicity
        # String specifying if this configuration parameter is an configuration
        # parameter or if the hardware- or vendor-specific.
        self._origin: Optional["String"] = None

    @property
    def origin(self) -> Optional["String"]:
        """Get origin (Pythonic accessor)."""
        return self._origin

    @origin.setter
    def origin(self, value: Optional["String"]) -> None:
        """
        Set origin with validation.

        Args:
            value: The origin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._origin = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"origin must be String or str or None, got {type(value).__name__}"
            )
        self._origin = value
                # post-build variants (previously known as configuration sets).
        # TRUE means means no.
        self._postBuildVariant: Optional["Boolean"] = None

    @property
    def post_build_variant(self) -> Optional["Boolean"]:
        """Get postBuildVariant (Pythonic accessor)."""
        return self._postBuildVariant

    @post_build_variant.setter
    def post_build_variant(self, value: Optional["Boolean"]) -> None:
        """
        Set postBuildVariant with validation.

        Args:
            value: The postBuildVariant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._postBuildVariant = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"postBuildVariant must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._postBuildVariant = value
        # 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration ECU Configuration R23-11.
        self._requiresIndex: Optional["Boolean"] = None

    @property
    def requires_index(self) -> Optional["Boolean"]:
        """Get requiresIndex (Pythonic accessor)."""
        return self._requiresIndex

    @requires_index.setter
    def requires_index(self, value: Optional["Boolean"]) -> None:
        """
        Set requiresIndex with validation.

        Args:
            value: The requiresIndex to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requiresIndex = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"requiresIndex must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._requiresIndex = value
        # the has the Category the of the EcucModuleDef is set to this mandatory.
        self._valueConfig: List["EcucValueConfiguration"] = []

    @property
    def value_config(self) -> List["EcucValueConfiguration"]:
        """Get valueConfig (Pythonic accessor)."""
        return self._valueConfig

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMultiplicity(self) -> List["EcucMultiplicity"]:
        """
        AUTOSAR-compliant getter for multiplicity.

        Returns:
            The multiplicity value

        Note:
            Delegates to multiplicity property (CODING_RULE_V2_00017)
        """
        return self.multiplicity  # Delegates to property

    def getOrigin(self) -> "String":
        """
        AUTOSAR-compliant getter for origin.

        Returns:
            The origin value

        Note:
            Delegates to origin property (CODING_RULE_V2_00017)
        """
        return self.origin  # Delegates to property

    def setOrigin(self, value: "String") -> EcucCommonAttributes:
        """
        AUTOSAR-compliant setter for origin with method chaining.

        Args:
            value: The origin to set

        Returns:
            self for method chaining

        Note:
            Delegates to origin property setter (gets validation automatically)
        """
        self.origin = value  # Delegates to property setter
        return self

    def getPostBuildVariant(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for postBuildVariant.

        Returns:
            The postBuildVariant value

        Note:
            Delegates to post_build_variant property (CODING_RULE_V2_00017)
        """
        return self.post_build_variant  # Delegates to property

    def setPostBuildVariant(self, value: "Boolean") -> EcucCommonAttributes:
        """
        AUTOSAR-compliant setter for postBuildVariant with method chaining.

        Args:
            value: The postBuildVariant to set

        Returns:
            self for method chaining

        Note:
            Delegates to post_build_variant property setter (gets validation automatically)
        """
        self.post_build_variant = value  # Delegates to property setter
        return self

    def getRequiresIndex(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for requiresIndex.

        Returns:
            The requiresIndex value

        Note:
            Delegates to requires_index property (CODING_RULE_V2_00017)
        """
        return self.requires_index  # Delegates to property

    def setRequiresIndex(self, value: "Boolean") -> EcucCommonAttributes:
        """
        AUTOSAR-compliant setter for requiresIndex with method chaining.

        Args:
            value: The requiresIndex to set

        Returns:
            self for method chaining

        Note:
            Delegates to requires_index property setter (gets validation automatically)
        """
        self.requires_index = value  # Delegates to property setter
        return self

    def getValueConfig(self) -> List["EcucValueConfiguration"]:
        """
        AUTOSAR-compliant getter for valueConfig.

        Returns:
            The valueConfig value

        Note:
            Delegates to value_config property (CODING_RULE_V2_00017)
        """
        return self.value_config  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_origin(self, value: Optional["String"]) -> EcucCommonAttributes:
        """
        Set origin and return self for chaining.

        Args:
            value: The origin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_origin("value")
        """
        self.origin = value  # Use property setter (gets validation)
        return self

    def with_post_build_variant(self, value: Optional["Boolean"]) -> EcucCommonAttributes:
        """
        Set postBuildVariant and return self for chaining.

        Args:
            value: The postBuildVariant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_post_build_variant("value")
        """
        self.post_build_variant = value  # Use property setter (gets validation)
        return self

    def with_requires_index(self, value: Optional["Boolean"]) -> EcucCommonAttributes:
        """
        Set requiresIndex and return self for chaining.

        Args:
            value: The requiresIndex to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requires_index("value")
        """
        self.requires_index = value  # Use property setter (gets validation)
        return self



class EcucValueConfigurationClass(EcucAbstractConfigurationClass):
    """
    Specifies the ValueConfigurationClass of a parameter/reference for each
    ConfigurationVariant of the EcucModuleDef.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucValueConfigurationClass

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 52, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucMultiplicityConfigurationClass(EcucAbstractConfigurationClass):
    """
    Specifies the MultiplicityConfigurationClass of a parameter/reference or a
    container for each ConfigurationVariant of the EcucModuleDef.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucMultiplicityConfigurationClass

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 52, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucParamConfContainerDef(EcucContainerDef):
    """
    Used to define configuration containers that can hierarchically contain
    other containers and/or parameter definitions.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucParamConfContainerDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 39, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The parameters defined within the EcucParamConf.
        self._parameter: List[EcucParameterDef] = []

    @property
    def parameter(self) -> List[EcucParameterDef]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter
        # The references defined within the EcucParamConf.
        self._reference: List["RefType"] = []

    @property
    def reference(self) -> List["RefType"]:
        """Get reference (Pythonic accessor)."""
        return self._reference
        # The containers defined within the EcucParamConf.
        self._subContainer: List[EcucContainerDef] = []

    @property
    def sub_container(self) -> List[EcucContainerDef]:
        """Get subContainer (Pythonic accessor)."""
        return self._subContainer

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getParameter(self) -> List[EcucParameterDef]:
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def getReference(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for reference.

        Returns:
            The reference value

        Note:
            Delegates to reference property (CODING_RULE_V2_00017)
        """
        return self.reference  # Delegates to property

    def getSubContainer(self) -> List[EcucContainerDef]:
        """
        AUTOSAR-compliant getter for subContainer.

        Returns:
            The subContainer value

        Note:
            Delegates to sub_container property (CODING_RULE_V2_00017)
        """
        return self.sub_container  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucChoiceContainerDef(EcucContainerDef):
    """
    Used to define configuration containers that provide a choice between
    several EcucParamConfContainer Def. But in the actual ECU Configuration
    Values only one instance from the choice list will be present.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucChoiceContainerDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 41, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The choices available in a EcucChoiceContainerDef.
        # atpSplitable.
        self._choice: List["EcucParamConf"] = []

    @property
    def choice(self) -> List["EcucParamConf"]:
        """Get choice (Pythonic accessor)."""
        return self._choice

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChoice(self) -> List["EcucParamConf"]:
        """
        AUTOSAR-compliant getter for choice.

        Returns:
            The choice value

        Note:
            Delegates to choice property (CODING_RULE_V2_00017)
        """
        return self.choice  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucParameterDef(EcucCommonAttributes, ABC):
    """
    Abstract class used to define the similarities of all ECU Configuration
    Parameter types defined as subclasses.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucParameterDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 57, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 188, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is EcucParameterDef:
            raise TypeError("EcucParameterDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A derivation of a Configuration Parameter value can be by an informal
        # Calculation Formula or by a that can be used to specify the.
        self._derivation: Optional["EcucDerivation"] = None

    @property
    def derivation(self) -> Optional["EcucDerivation"]:
        """Get derivation (Pythonic accessor)."""
        return self._derivation

    @derivation.setter
    def derivation(self, value: Optional["EcucDerivation"]) -> None:
        """
        Set derivation with validation.

        Args:
            value: The derivation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._derivation = None
            return

        if not isinstance(value, EcucDerivation):
            raise TypeError(
                f"derivation must be EcucDerivation or None, got {type(value).__name__}"
            )
        self._derivation = value
        # container, to derive a symbolic name chapter "Representation of Symbolic Ecuc
        # specification for more details.
        self._symbolicName: Optional["Boolean"] = None

    @property
    def symbolic_name(self) -> Optional["Boolean"]:
        """Get symbolicName (Pythonic accessor)."""
        return self._symbolicName

    @symbolic_name.setter
    def symbolic_name(self, value: Optional["Boolean"]) -> None:
        """
        Set symbolicName with validation.

        Args:
            value: The symbolicName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbolicName = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"symbolicName must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._symbolicName = value
                # "AUTO".
        # is "true" it shall be possible to set the "isAuto of the respective parameter
                # to "true".
        # This the actual value will not be considered during but will be
                # (re-)calculated by the code stored in the value attribute afterwards.
        # updated values might require a other modules which reference these is "false"
                # it shall not be possible to set the "is of the respective parameter to
                # "true".
        # is not present the default is "false".
        self._withAuto: Optional["Boolean"] = None

    @property
    def with_auto(self) -> Optional["Boolean"]:
        """Get withAuto (Pythonic accessor)."""
        return self._withAuto

    @with_auto.setter
    def with_auto(self, value: Optional["Boolean"]) -> None:
        """
        Set withAuto with validation.

        Args:
            value: The withAuto to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._withAuto = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"withAuto must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._withAuto = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDerivation(self) -> "EcucDerivation":
        """
        AUTOSAR-compliant getter for derivation.

        Returns:
            The derivation value

        Note:
            Delegates to derivation property (CODING_RULE_V2_00017)
        """
        return self.derivation  # Delegates to property

    def setDerivation(self, value: "EcucDerivation") -> EcucParameterDef:
        """
        AUTOSAR-compliant setter for derivation with method chaining.

        Args:
            value: The derivation to set

        Returns:
            self for method chaining

        Note:
            Delegates to derivation property setter (gets validation automatically)
        """
        self.derivation = value  # Delegates to property setter
        return self

    def getSymbolicName(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for symbolicName.

        Returns:
            The symbolicName value

        Note:
            Delegates to symbolic_name property (CODING_RULE_V2_00017)
        """
        return self.symbolic_name  # Delegates to property

    def setSymbolicName(self, value: "Boolean") -> EcucParameterDef:
        """
        AUTOSAR-compliant setter for symbolicName with method chaining.

        Args:
            value: The symbolicName to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbolic_name property setter (gets validation automatically)
        """
        self.symbolic_name = value  # Delegates to property setter
        return self

    def getWithAuto(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for withAuto.

        Returns:
            The withAuto value

        Note:
            Delegates to with_auto property (CODING_RULE_V2_00017)
        """
        return self.with_auto  # Delegates to property

    def setWithAuto(self, value: "Boolean") -> EcucParameterDef:
        """
        AUTOSAR-compliant setter for withAuto with method chaining.

        Args:
            value: The withAuto to set

        Returns:
            self for method chaining

        Note:
            Delegates to with_auto property setter (gets validation automatically)
        """
        self.with_auto = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_derivation(self, value: Optional["EcucDerivation"]) -> EcucParameterDef:
        """
        Set derivation and return self for chaining.

        Args:
            value: The derivation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_derivation("value")
        """
        self.derivation = value  # Use property setter (gets validation)
        return self

    def with_symbolic_name(self, value: Optional["Boolean"]) -> EcucParameterDef:
        """
        Set symbolicName and return self for chaining.

        Args:
            value: The symbolicName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbolic_name("value")
        """
        self.symbolic_name = value  # Use property setter (gets validation)
        return self

    def with_with_auto(self, value: Optional["Boolean"]) -> EcucParameterDef:
        """
        Set withAuto and return self for chaining.

        Args:
            value: The withAuto to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_with_auto("value")
        """
        self.with_auto = value  # Use property setter (gets validation)
        return self



class EcucAbstractReferenceDef(EcucCommonAttributes, ABC):
    """
    Common class to gather the attributes for the definition of references.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucAbstractReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 71, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractReferenceDef:
            raise TypeError("EcucAbstractReferenceDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies whether it shall be allowed on the value side to reference value as
                # "AUTO".
        # is "true" it shall be possible to set the "isAuto of the respective reference
                # to "true".
        # This the actual value will not be considered during but will be
                # (re-)calculated by the code stored in the value attribute afterwards.
        # updated values might require a other modules which reference these is "false"
                # it shall not be possible to set the "is of the respective reference to
                # "true".
        # is not present the default is "false".
        self._withAuto: Optional["Boolean"] = None

    @property
    def with_auto(self) -> Optional["Boolean"]:
        """Get withAuto (Pythonic accessor)."""
        return self._withAuto

    @with_auto.setter
    def with_auto(self, value: Optional["Boolean"]) -> None:
        """
        Set withAuto with validation.

        Args:
            value: The withAuto to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._withAuto = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"withAuto must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._withAuto = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getWithAuto(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for withAuto.

        Returns:
            The withAuto value

        Note:
            Delegates to with_auto property (CODING_RULE_V2_00017)
        """
        return self.with_auto  # Delegates to property

    def setWithAuto(self, value: "Boolean") -> EcucAbstractReferenceDef:
        """
        AUTOSAR-compliant setter for withAuto with method chaining.

        Args:
            value: The withAuto to set

        Returns:
            self for method chaining

        Note:
            Delegates to with_auto property setter (gets validation automatically)
        """
        self.with_auto = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_with_auto(self, value: Optional["Boolean"]) -> EcucAbstractReferenceDef:
        """
        Set withAuto and return self for chaining.

        Args:
            value: The withAuto to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_with_auto("value")
        """
        self.with_auto = value  # Use property setter (gets validation)
        return self



class EcucBooleanParamDef(EcucParameterDef):
    """
    Configuration parameter type for Boolean. Allowed values are true and false.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucBooleanParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 58, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 183, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default value of the boolean configuration parameter.
        self._defaultValue: Optional["Boolean"] = None

    @property
    def default_value(self) -> Optional["Boolean"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["Boolean"]) -> None:
        """
        Set defaultValue with validation.

        Args:
            value: The defaultValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"defaultValue must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._defaultValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "Boolean") -> EcucBooleanParamDef:
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["Boolean"]) -> EcucBooleanParamDef:
        """
        Set defaultValue and return self for chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self



class EcucIntegerParamDef(EcucParameterDef):
    """
    Configuration parameter type for Integer.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucIntegerParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 60, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 187, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default value of the integer configuration parameter.
        self._defaultValue: Optional["UnlimitedInteger"] = None

    @property
    def default_value(self) -> Optional["UnlimitedInteger"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set defaultValue with validation.

        Args:
            value: The defaultValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"defaultValue must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        self._max: Optional["UnlimitedInteger"] = None

    @property
    def max(self) -> Optional["UnlimitedInteger"]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set max with validation.

        Args:
            value: The max to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._max = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"max must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._max = value
        self._min: Optional["UnlimitedInteger"] = None

    @property
    def min(self) -> Optional["UnlimitedInteger"]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set min with validation.

        Args:
            value: The min to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._min = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"min must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._min = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "UnlimitedInteger") -> EcucIntegerParamDef:
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getMax(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for max.

        Returns:
            The max value

        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: "UnlimitedInteger") -> EcucIntegerParamDef:
        """
        AUTOSAR-compliant setter for max with method chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Note:
            Delegates to max property setter (gets validation automatically)
        """
        self.max = value  # Delegates to property setter
        return self

    def getMin(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for min.

        Returns:
            The min value

        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: "UnlimitedInteger") -> EcucIntegerParamDef:
        """
        AUTOSAR-compliant setter for min with method chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Note:
            Delegates to min property setter (gets validation automatically)
        """
        self.min = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["UnlimitedInteger"]) -> EcucIntegerParamDef:
        """
        Set defaultValue and return self for chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self

    def with_max(self, value: Optional["UnlimitedInteger"]) -> EcucIntegerParamDef:
        """
        Set max and return self for chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max("value")
        """
        self.max = value  # Use property setter (gets validation)
        return self

    def with_min(self, value: Optional["UnlimitedInteger"]) -> EcucIntegerParamDef:
        """
        Set min and return self for chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min("value")
        """
        self.min = value  # Use property setter (gets validation)
        return self



class EcucFloatParamDef(EcucParameterDef):
    """
    Configuration parameter type for Float.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucFloatParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 61, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 186, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default value of the float configuration parameter.
        self._defaultValue: Optional["Float"] = None

    @property
    def default_value(self) -> Optional["Float"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["Float"]) -> None:
        """
        Set defaultValue with validation.

        Args:
            value: The defaultValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"defaultValue must be Float or float or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        # 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration ECU Configuration R23-11.
        self._max: Optional["Limit"] = None

    @property
    def max(self) -> Optional["Limit"]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional["Limit"]) -> None:
        """
        Set max with validation.

        Args:
            value: The max to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._max = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"max must be Limit or None, got {type(value).__name__}"
            )
        self._max = value
        self._min: Optional["Limit"] = None

    @property
    def min(self) -> Optional["Limit"]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional["Limit"]) -> None:
        """
        Set min with validation.

        Args:
            value: The min to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._min = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"min must be Limit or None, got {type(value).__name__}"
            )
        self._min = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "Float":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "Float") -> EcucFloatParamDef:
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getMax(self) -> "Limit":
        """
        AUTOSAR-compliant getter for max.

        Returns:
            The max value

        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: "Limit") -> EcucFloatParamDef:
        """
        AUTOSAR-compliant setter for max with method chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Note:
            Delegates to max property setter (gets validation automatically)
        """
        self.max = value  # Delegates to property setter
        return self

    def getMin(self) -> "Limit":
        """
        AUTOSAR-compliant getter for min.

        Returns:
            The min value

        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: "Limit") -> EcucFloatParamDef:
        """
        AUTOSAR-compliant setter for min with method chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Note:
            Delegates to min property setter (gets validation automatically)
        """
        self.min = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["Float"]) -> EcucFloatParamDef:
        """
        Set defaultValue and return self for chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self

    def with_max(self, value: Optional["Limit"]) -> EcucFloatParamDef:
        """
        Set max and return self for chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max("value")
        """
        self.max = value  # Use property setter (gets validation)
        return self

    def with_min(self, value: Optional["Limit"]) -> EcucFloatParamDef:
        """
        Set min and return self for chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min("value")
        """
        self.min = value  # Use property setter (gets validation)
        return self



class EcucEnumerationParamDef(EcucParameterDef):
    """
    Configuration parameter type for Enumeration.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucEnumerationParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 66, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 186, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default value of the enumeration configuration parameter.
        # needs to be one of the literals specified for this.
        self._defaultValue: Optional["Identifier"] = None

    @property
    def default_value(self) -> Optional["Identifier"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["Identifier"]) -> None:
        """
        Set defaultValue with validation.

        Args:
            value: The defaultValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"defaultValue must be Identifier or str or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        # This aggregation is optional if the has the category the of the EcucModuleDef
                # is set to this mandatory.
        self._literal: List["EcucEnumerationLiteral"] = []

    @property
    def literal(self) -> List["EcucEnumerationLiteral"]:
        """Get literal (Pythonic accessor)."""
        return self._literal

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "Identifier") -> EcucEnumerationParamDef:
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getLiteral(self) -> List["EcucEnumerationLiteral"]:
        """
        AUTOSAR-compliant getter for literal.

        Returns:
            The literal value

        Note:
            Delegates to literal property (CODING_RULE_V2_00017)
        """
        return self.literal  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["Identifier"]) -> EcucEnumerationParamDef:
        """
        Set defaultValue and return self for chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self



class EcucAddInfoParamDef(EcucParameterDef):
    """
    Configuration Parameter Definition for the specification of formatted text
    in the ECU Configuration Parameter Description.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucAddInfoParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 68, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucAbstractInternalReferenceDef(EcucAbstractReferenceDef, ABC):
    """
    Common abstract class to gather attributes for internal references (where
    the destination is located in the Ecu Configuration Description). (cid:53)
    71 of 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration Specification of
    ECU Configuration AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucAbstractInternalReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 71, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractInternalReferenceDef:
            raise TypeError("EcucAbstractInternalReferenceDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If this attribute is set to true the implementation of the is done using a
        # Symbolic Name defined by the container according to TPS_ECUC_02108.
        self._requires: Optional["Boolean"] = None

    @property
    def requires(self) -> Optional["Boolean"]:
        """Get requires (Pythonic accessor)."""
        return self._requires

    @requires.setter
    def requires(self, value: Optional["Boolean"]) -> None:
        """
        Set requires with validation.

        Args:
            value: The requires to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requires = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"requires must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._requires = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequires(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for requires.

        Returns:
            The requires value

        Note:
            Delegates to requires property (CODING_RULE_V2_00017)
        """
        return self.requires  # Delegates to property

    def setRequires(self, value: "Boolean") -> EcucAbstractInternalReferenceDef:
        """
        AUTOSAR-compliant setter for requires with method chaining.

        Args:
            value: The requires to set

        Returns:
            self for method chaining

        Note:
            Delegates to requires property setter (gets validation automatically)
        """
        self.requires = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_requires(self, value: Optional["Boolean"]) -> EcucAbstractInternalReferenceDef:
        """
        Set requires and return self for chaining.

        Args:
            value: The requires to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requires("value")
        """
        self.requires = value  # Use property setter (gets validation)
        return self



class EcucAbstractExternalReferenceDef(EcucAbstractReferenceDef, ABC):
    """
    Common abstract class to gather attributes for external references (where
    the destination is not located in the ECU Configuration Description but in
    an another AUTOSAR Template).

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucAbstractExternalReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 72, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractExternalReferenceDef:
            raise TypeError("EcucAbstractExternalReferenceDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucReferenceDef(EcucAbstractInternalReferenceDef):
    """
    Specify references within the ECU Configuration Description between
    parameter containers.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 73, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 442, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 189, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Exactly one reference to a parameter container is allowed.
        self._destination: Optional[EcucContainerDef] = None

    @property
    def destination(self) -> Optional[EcucContainerDef]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    @destination.setter
    def destination(self, value: Optional[EcucContainerDef]) -> None:
        """
        Set destination with validation.

        Args:
            value: The destination to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destination = None
            return

        if not isinstance(value, EcucContainerDef):
            raise TypeError(
                f"destination must be EcucContainerDef or None, got {type(value).__name__}"
            )
        self._destination = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestination(self) -> EcucContainerDef:
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    def setDestination(self, value: EcucContainerDef) -> EcucReferenceDef:
        """
        AUTOSAR-compliant setter for destination with method chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination property setter (gets validation automatically)
        """
        self.destination = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination(self, value: Optional[EcucContainerDef]) -> EcucReferenceDef:
        """
        Set destination and return self for chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination("value")
        """
        self.destination = value  # Use property setter (gets validation)
        return self



class EcucChoiceReferenceDef(EcucAbstractInternalReferenceDef):
    """
    Specify alternative references where in the ECU Configuration description
    only one of the specified references will actually be used.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucChoiceReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 74, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 184, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # All the possible parameter containers for the reference.
        self._destination: List[EcucContainerDef] = []

    @property
    def destination(self) -> List[EcucContainerDef]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestination(self) -> List[EcucContainerDef]:
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcucUriReferenceDef(EcucAbstractInternalReferenceDef):
    """
    Definition of reference with a destination that is specified via a
    destinationUri. With such a reference it is possible to define a reference
    to a EcucContainerDef in a different module independent from the concrete
    definition of the target container.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucUriReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 81, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 190, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Any EcucContainerDef with a destinationUri that is the destinationUri that is
        # referenced here valid target.
        self._destinationUri: Optional[EcucDestinationUriDef] = None

    @property
    def destination_uri(self) -> Optional[EcucDestinationUriDef]:
        """Get destinationUri (Pythonic accessor)."""
        return self._destinationUri

    @destination_uri.setter
    def destination_uri(self, value: Optional[EcucDestinationUriDef]) -> None:
        """
        Set destinationUri with validation.

        Args:
            value: The destinationUri to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationUri = None
            return

        if not isinstance(value, EcucDestinationUriDef):
            raise TypeError(
                f"destinationUri must be EcucDestinationUriDef or None, got {type(value).__name__}"
            )
        self._destinationUri = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationUri(self) -> EcucDestinationUriDef:
        """
        AUTOSAR-compliant getter for destinationUri.

        Returns:
            The destinationUri value

        Note:
            Delegates to destination_uri property (CODING_RULE_V2_00017)
        """
        return self.destination_uri  # Delegates to property

    def setDestinationUri(self, value: EcucDestinationUriDef) -> EcucUriReferenceDef:
        """
        AUTOSAR-compliant setter for destinationUri with method chaining.

        Args:
            value: The destinationUri to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_uri property setter (gets validation automatically)
        """
        self.destination_uri = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_uri(self, value: Optional[EcucDestinationUriDef]) -> EcucUriReferenceDef:
        """
        Set destinationUri and return self for chaining.

        Args:
            value: The destinationUri to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_uri("value")
        """
        self.destination_uri = value  # Use property setter (gets validation)
        return self



class EcucForeignReferenceDef(EcucAbstractExternalReferenceDef):
    """
    Specify a reference to an XML description of an entity described in another
    AUTOSAR template.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucForeignReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 75, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The type in the AUTOSAR Metamodel to which instance is allowed to point to.
        self._destinationType: Optional["String"] = None

    @property
    def destination_type(self) -> Optional["String"]:
        """Get destinationType (Pythonic accessor)."""
        return self._destinationType

    @destination_type.setter
    def destination_type(self, value: Optional["String"]) -> None:
        """
        Set destinationType with validation.

        Args:
            value: The destinationType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationType = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"destinationType must be String or str or None, got {type(value).__name__}"
            )
        self._destinationType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationType(self) -> "String":
        """
        AUTOSAR-compliant getter for destinationType.

        Returns:
            The destinationType value

        Note:
            Delegates to destination_type property (CODING_RULE_V2_00017)
        """
        return self.destination_type  # Delegates to property

    def setDestinationType(self, value: "String") -> EcucForeignReferenceDef:
        """
        AUTOSAR-compliant setter for destinationType with method chaining.

        Args:
            value: The destinationType to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_type property setter (gets validation automatically)
        """
        self.destination_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_type(self, value: Optional["String"]) -> EcucForeignReferenceDef:
        """
        Set destinationType and return self for chaining.

        Args:
            value: The destinationType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_type("value")
        """
        self.destination_type = value  # Use property setter (gets validation)
        return self



class EcucInstanceReferenceDef(EcucAbstractExternalReferenceDef):
    """
    Specify a reference to an XML description of an entity described in another
    AUTOSAR template using the INSTANCE REFERENCE semantics.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucInstanceReferenceDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 77, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The context in the AUTOSAR Metamodel to which’ this is allowed to point to.
        self._destination: Optional["String"] = None

    @property
    def destination(self) -> Optional["String"]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    @destination.setter
    def destination(self, value: Optional["String"]) -> None:
        """
        Set destination with validation.

        Args:
            value: The destination to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destination = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"destination must be String or str or None, got {type(value).__name__}"
            )
        self._destination = value
        self._destinationType: Optional["String"] = None

    @property
    def destination_type(self) -> Optional["String"]:
        """Get destinationType (Pythonic accessor)."""
        return self._destinationType

    @destination_type.setter
    def destination_type(self, value: Optional["String"]) -> None:
        """
        Set destinationType with validation.

        Args:
            value: The destinationType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationType = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"destinationType must be String or str or None, got {type(value).__name__}"
            )
        self._destinationType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestination(self) -> "String":
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    def setDestination(self, value: "String") -> EcucInstanceReferenceDef:
        """
        AUTOSAR-compliant setter for destination with method chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination property setter (gets validation automatically)
        """
        self.destination = value  # Delegates to property setter
        return self

    def getDestinationType(self) -> "String":
        """
        AUTOSAR-compliant getter for destinationType.

        Returns:
            The destinationType value

        Note:
            Delegates to destination_type property (CODING_RULE_V2_00017)
        """
        return self.destination_type  # Delegates to property

    def setDestinationType(self, value: "String") -> EcucInstanceReferenceDef:
        """
        AUTOSAR-compliant setter for destinationType with method chaining.

        Args:
            value: The destinationType to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_type property setter (gets validation automatically)
        """
        self.destination_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination(self, value: Optional["String"]) -> EcucInstanceReferenceDef:
        """
        Set destination and return self for chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination("value")
        """
        self.destination = value  # Use property setter (gets validation)
        return self

    def with_destination_type(self, value: Optional["String"]) -> EcucInstanceReferenceDef:
        """
        Set destinationType and return self for chaining.

        Args:
            value: The destinationType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_type("value")
        """
        self.destination_type = value  # Use property setter (gets validation)
        return self


class EcucScopeEnum(AREnum):
    """
    EcucScopeEnum enumeration

Possible scope settings for a configuration element. Aggregated by EcucDefinitionElement.scope

Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate
    """
    # An element may be shared with other modules.
    ECU = "0"

    # An element is only be applicable for the module it is defined in.
    local = "1"



class EcucConfigurationClassEnum(AREnum):
    """
    EcucConfigurationClassEnum enumeration

Possible configuration classes for the AUTOSAR configuration parameters. Aggregated by EcucAbstractConfigurationClass.configClass

Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate
    """
    # Link Time: parts of configuration are delivered from another object code file
    Link = "0"

    # PostBuildTime: after compilation a configuration parameter can be changed.
    PostBuild = "1"

    # PreCompile Time: after compilation a configuration parameter can not be changed any more.
    PreCompile = "2"

    # PublishedInformation is used to specify the fact that certain information is fixed even before the Information pre-compile stage.
    Published = "3"



class EcucConfigurationVariantEnum(AREnum):
    """
    EcucConfigurationVariantEnum enumeration

Specifies the possible Configuration Variants used for AUTOSAR BSW Modules. Aggregated by EcucAbstractConfigurationClass.configVariant, EcucModuleConfigurationValues.implementation ConfigVariant, EcucModuleDef.supportedConfigVariant

Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate
    """
    # Preconfigured (i.e. fixed) configuration which cannot be changed. Specification of ECU Configuration
    PreconfiguredConfiguration = "0"

    # CP R23-11
    AUTOSAR = "None"

    # Recommended configuration for a module.
    RecommendedConfiguration = "1"

    # Specifies that the BSW Module implementation may use PreCompileTime and LinkTime configuration
    VariantLinkTime = "2"

    # Specifies that the BSW Module implementation may use PreCompileTime, LinkTime and PostBuild configuration parameters.
    VariantPostBuild = "3"

    # Specifies that the BSW Module implementation uses only PreCompileTime configuration parameters.
    VariantPreCompile = "6"



class EcucDestinationUriNestingContractEnum(AREnum):
    """
    EcucDestinationUriNestingContractEnum enumeration

EcucDestinationUriNestingContractEnum is used to determine what is qualified by the Ecuc DestinationUriPolicy. Aggregated by EcucDestinationUriPolicy.destinationUriNestingContract

Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate
    """
    # EcucDestinationUriPolicy describes elements (subContainers, Parameters, References) that are Container directly owned by the target container.
    leafOfTarget = "0"

    # EcucDestinationUriPolicy describes the target container of EcucUriReferenceDef.
    targetContainer = "1"

    # EcucDestinationUriPolicy describes elements (subContainers, Parameters, References) of the target Container container which can be defined in arbitrary nested subContainer structure.
    vertexOfTarget = "2"
