from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    EcucCondition,
    EcucScopeEnum,
    EcucValidation,
    Traceable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


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
        # Collection of validation conditions which all need to evaluate to true in
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"lowerMultiplicity must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._lowerMultiplicity = value
        # This contains a sloppy reference to the Autosar identifier of the element
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
        # Specifies the scope of this configuration element.
        self._scope: Optional["EcucScopeEnum"] = None

    @property
    def scope(self) -> Optional["EcucScopeEnum"]:
        """Get scope (Pythonic accessor)."""
        return self._scope

    @scope.setter
    def scope(self, value: Optional["EcucScopeEnum"]) -> None:
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
        # To express an infinite number of occurrences of this this attribute has to be
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"upperMultiplicity must be Boolean or None, got {type(value).__name__}"
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

    def setEcucCond(self, value: "EcucCondition") -> "EcucDefinitionElement":
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

    def setLowerMultiplicity(self, value: "PositiveInteger") -> "EcucDefinitionElement":
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

    def setRelatedTrace(self, value: "Traceable") -> "EcucDefinitionElement":
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

    def getScope(self) -> "EcucScopeEnum":
        """
        AUTOSAR-compliant getter for scope.

        Returns:
            The scope value

        Note:
            Delegates to scope property (CODING_RULE_V2_00017)
        """
        return self.scope  # Delegates to property

    def setScope(self, value: "EcucScopeEnum") -> "EcucDefinitionElement":
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

    def setUpperMultiplicity(self, value: "Boolean") -> "EcucDefinitionElement":
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

    def with_ecuc_cond(self, value: Optional["EcucCondition"]) -> "EcucDefinitionElement":
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

    def with_lower_multiplicity(self, value: Optional["PositiveInteger"]) -> "EcucDefinitionElement":
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

    def with_related_trace(self, value: Optional["Traceable"]) -> "EcucDefinitionElement":
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

    def with_scope(self, value: Optional["EcucScopeEnum"]) -> "EcucDefinitionElement":
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

    def with_upper_multiplicity(self, value: Optional["Boolean"]) -> "EcucDefinitionElement":
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
