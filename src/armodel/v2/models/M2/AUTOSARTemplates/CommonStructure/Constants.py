"""
AUTOSAR Package - Constants

Package: M2::AUTOSARTemplates::CommonStructure::Constants
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
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


class ConstantSpecification(ARElement):
    """
    Specification of a constant that can be part of a package, i.e. it can be
    defined stand-alone.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ConstantSpecification

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 311, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 433, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification of an expression leading to a value for this.
        self._valueSpec: Optional[ValueSpecification] = None

    @property
    def value_spec(self) -> Optional[ValueSpecification]:
        """Get valueSpec (Pythonic accessor)."""
        return self._valueSpec

    @value_spec.setter
    def value_spec(self, value: Optional[ValueSpecification]) -> None:
        """
        Set valueSpec with validation.

        Args:
            value: The valueSpec to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._valueSpec = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"valueSpec must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._valueSpec = value

    def with_mapping(self, value):
        """
        Set mapping and return self for chaining.

        Args:
            value: The mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapping("value")
        """
        self.mapping = value  # Use property setter (gets validation)
        return self

    def with_sw_axis_cont(self, value):
        """
        Set sw_axis_cont and return self for chaining.

        Args:
            value: The sw_axis_cont to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_axis_cont("value")
        """
        self.sw_axis_cont = value  # Use property setter (gets validation)
        return self

    def with_sw_axis_cont(self, value):
        """
        Set sw_axis_cont and return self for chaining.

        Args:
            value: The sw_axis_cont to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_axis_cont("value")
        """
        self.sw_axis_cont = value  # Use property setter (gets validation)
        return self

    def with_element(self, value):
        """
        Set element and return self for chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element("value")
        """
        self.element = value  # Use property setter (gets validation)
        return self

    def with_argument(self, value):
        """
        Set argument and return self for chaining.

        Args:
            value: The argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_argument("value")
        """
        self.argument = value  # Use property setter (gets validation)
        return self

    def with_compound(self, value):
        """
        Set compound and return self for chaining.

        Args:
            value: The compound to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compound("value")
        """
        self.compound = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValueSpec(self) -> ValueSpecification:
        """
        AUTOSAR-compliant getter for valueSpec.

        Returns:
            The valueSpec value

        Note:
            Delegates to value_spec property (CODING_RULE_V2_00017)
        """
        return self.value_spec  # Delegates to property

    def setValueSpec(self, value: ValueSpecification) -> ConstantSpecification:
        """
        AUTOSAR-compliant setter for valueSpec with method chaining.

        Args:
            value: The valueSpec to set

        Returns:
            self for method chaining

        Note:
            Delegates to value_spec property setter (gets validation automatically)
        """
        self.value_spec = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value_spec(self, value: Optional[ValueSpecification]) -> ConstantSpecification:
        """
        Set valueSpec and return self for chaining.

        Args:
            value: The valueSpec to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value_spec("value")
        """
        self.value_spec = value  # Use property setter (gets validation)
        return self



class NumericalOrText(ARObject):
    """
    This meta-class represents the ability to yield either a numerical or a
    string. A typical use case is that two or more instances of this meta-class
    are aggregated with a VariationPoint where some instances yield strings
    while other instances yield numerical depending on the resolution of the
    binding expression.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::NumericalOrText

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 323, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 455, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the ability to provide a numerical latest binding
        # time of the VariationPoint shall.
        self._vf: Optional["Numerical"] = None

    @property
    def vf(self) -> Optional["Numerical"]:
        """Get vf (Pythonic accessor)."""
        return self._vf

    @vf.setter
    def vf(self, value: Optional["Numerical"]) -> None:
        """
        Set vf with validation.

        Args:
            value: The vf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vf = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"vf must be Numerical or None, got {type(value).__name__}"
            )
        self._vf = value
        self._vt: Optional["String"] = None

    @property
    def vt(self) -> Optional["String"]:
        """Get vt (Pythonic accessor)."""
        return self._vt

    @vt.setter
    def vt(self, value: Optional["String"]) -> None:
        """
        Set vt with validation.

        Args:
            value: The vt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vt = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"vt must be String or str or None, got {type(value).__name__}"
            )
        self._vt = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVf(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for vf.

        Returns:
            The vf value

        Note:
            Delegates to vf property (CODING_RULE_V2_00017)
        """
        return self.vf  # Delegates to property

    def setVf(self, value: "Numerical") -> NumericalOrText:
        """
        AUTOSAR-compliant setter for vf with method chaining.

        Args:
            value: The vf to set

        Returns:
            self for method chaining

        Note:
            Delegates to vf property setter (gets validation automatically)
        """
        self.vf = value  # Delegates to property setter
        return self

    def getVt(self) -> "String":
        """
        AUTOSAR-compliant getter for vt.

        Returns:
            The vt value

        Note:
            Delegates to vt property (CODING_RULE_V2_00017)
        """
        return self.vt  # Delegates to property

    def setVt(self, value: "String") -> NumericalOrText:
        """
        AUTOSAR-compliant setter for vt with method chaining.

        Args:
            value: The vt to set

        Returns:
            self for method chaining

        Note:
            Delegates to vt property setter (gets validation automatically)
        """
        self.vt = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_vf(self, value: Optional["Numerical"]) -> NumericalOrText:
        """
        Set vf and return self for chaining.

        Args:
            value: The vf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vf("value")
        """
        self.vf = value  # Use property setter (gets validation)
        return self

    def with_vt(self, value: Optional["String"]) -> NumericalOrText:
        """
        Set vt and return self for chaining.

        Args:
            value: The vt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vt("value")
        """
        self.vt = value  # Use property setter (gets validation)
        return self



class RuleArguments(ARObject):
    """
    This represents the arguments for a rule-based value specification.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::RuleArguments

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 329, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 469, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a numerical value for the RuleBased.
        self._v: Optional["Numerical"] = None

    @property
    def v(self) -> Optional["Numerical"]:
        """Get v (Pythonic accessor)."""
        return self._v

    @v.setter
    def v(self, value: Optional["Numerical"]) -> None:
        """
        Set v with validation.

        Args:
            value: The v to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._v = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"v must be Numerical or None, got {type(value).__name__}"
            )
        self._v = value
                # variability.
        # The time of the VariationPoint shall be pre.
        self._vf: Optional["Numerical"] = None

    @property
    def vf(self) -> Optional["Numerical"]:
        """Get vf (Pythonic accessor)."""
        return self._vf

    @vf.setter
    def vf(self, value: Optional["Numerical"]) -> None:
        """
        Set vf with validation.

        Args:
            value: The vf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vf = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"vf must be Numerical or None, got {type(value).__name__}"
            )
        self._vf = value
        self._vt: Optional["VerbatimString"] = None

    @property
    def vt(self) -> Optional["VerbatimString"]:
        """Get vt (Pythonic accessor)."""
        return self._vt

    @vt.setter
    def vt(self, value: Optional["VerbatimString"]) -> None:
        """
        Set vt with validation.

        Args:
            value: The vt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vt = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"vt must be VerbatimString or None, got {type(value).__name__}"
            )
        self._vt = value
        # or text which existence is subject atpVariation.
        self._vtf: Optional[NumericalOrText] = None

    @property
    def vtf(self) -> Optional[NumericalOrText]:
        """Get vtf (Pythonic accessor)."""
        return self._vtf

    @vtf.setter
    def vtf(self, value: Optional[NumericalOrText]) -> None:
        """
        Set vtf with validation.

        Args:
            value: The vtf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vtf = None
            return

        if not isinstance(value, NumericalOrText):
            raise TypeError(
                f"vtf must be NumericalOrText or None, got {type(value).__name__}"
            )
        self._vtf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getV(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for v.

        Returns:
            The v value

        Note:
            Delegates to v property (CODING_RULE_V2_00017)
        """
        return self.v  # Delegates to property

    def setV(self, value: "Numerical") -> RuleArguments:
        """
        AUTOSAR-compliant setter for v with method chaining.

        Args:
            value: The v to set

        Returns:
            self for method chaining

        Note:
            Delegates to v property setter (gets validation automatically)
        """
        self.v = value  # Delegates to property setter
        return self

    def getVf(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for vf.

        Returns:
            The vf value

        Note:
            Delegates to vf property (CODING_RULE_V2_00017)
        """
        return self.vf  # Delegates to property

    def setVf(self, value: "Numerical") -> RuleArguments:
        """
        AUTOSAR-compliant setter for vf with method chaining.

        Args:
            value: The vf to set

        Returns:
            self for method chaining

        Note:
            Delegates to vf property setter (gets validation automatically)
        """
        self.vf = value  # Delegates to property setter
        return self

    def getVt(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for vt.

        Returns:
            The vt value

        Note:
            Delegates to vt property (CODING_RULE_V2_00017)
        """
        return self.vt  # Delegates to property

    def setVt(self, value: "VerbatimString") -> RuleArguments:
        """
        AUTOSAR-compliant setter for vt with method chaining.

        Args:
            value: The vt to set

        Returns:
            self for method chaining

        Note:
            Delegates to vt property setter (gets validation automatically)
        """
        self.vt = value  # Delegates to property setter
        return self

    def getVtf(self) -> NumericalOrText:
        """
        AUTOSAR-compliant getter for vtf.

        Returns:
            The vtf value

        Note:
            Delegates to vtf property (CODING_RULE_V2_00017)
        """
        return self.vtf  # Delegates to property

    def setVtf(self, value: NumericalOrText) -> RuleArguments:
        """
        AUTOSAR-compliant setter for vtf with method chaining.

        Args:
            value: The vtf to set

        Returns:
            self for method chaining

        Note:
            Delegates to vtf property setter (gets validation automatically)
        """
        self.vtf = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_v(self, value: Optional["Numerical"]) -> RuleArguments:
        """
        Set v and return self for chaining.

        Args:
            value: The v to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_v("value")
        """
        self.v = value  # Use property setter (gets validation)
        return self

    def with_vf(self, value: Optional["Numerical"]) -> RuleArguments:
        """
        Set vf and return self for chaining.

        Args:
            value: The vf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vf("value")
        """
        self.vf = value  # Use property setter (gets validation)
        return self

    def with_vt(self, value: Optional["VerbatimString"]) -> RuleArguments:
        """
        Set vt and return self for chaining.

        Args:
            value: The vt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vt("value")
        """
        self.vt = value  # Use property setter (gets validation)
        return self

    def with_vtf(self, value: Optional[NumericalOrText]) -> RuleArguments:
        """
        Set vtf and return self for chaining.

        Args:
            value: The vtf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vtf("value")
        """
        self.vtf = value  # Use property setter (gets validation)
        return self



class RuleBasedValueCont(ARObject):
    """
    This represents the values of a compound primitive (CURVE, MAP, CUBOID,
    CUBE_4, CUBE_5, VAL_ BLK) or an array.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::RuleBasedValueCont

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 330, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 464, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the rule based value specification for the array or compound
        # primitive (CURVE, MAP, CUBOID, VAL_BLK).
        self._ruleBased: Optional["RuleBasedValue"] = None

    @property
    def rule_based(self) -> Optional["RuleBasedValue"]:
        """Get ruleBased (Pythonic accessor)."""
        return self._ruleBased

    @rule_based.setter
    def rule_based(self, value: Optional["RuleBasedValue"]) -> None:
        """
        Set ruleBased with validation.

        Args:
            value: The ruleBased to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ruleBased = None
            return

        if not isinstance(value, RuleBasedValue):
            raise TypeError(
                f"ruleBased must be RuleBasedValue or None, got {type(value).__name__}"
            )
        self._ruleBased = value
                # CUBE_4, RES_AXIS, VAL_BLK.
        # dimension one value has to be defined, e.
        # g.
        # one of COM_AXIS and two or more in case of MAP.
        self._swArraysize: Optional["RefType"] = None

    @property
    def sw_arraysize(self) -> Optional["RefType"]:
        """Get swArraysize (Pythonic accessor)."""
        return self._swArraysize

    @sw_arraysize.setter
    def sw_arraysize(self, value: Optional["RefType"]) -> None:
        """
        Set swArraysize with validation.

        Args:
            value: The swArraysize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swArraysize = None
            return

        self._swArraysize = value
        self._unit: Optional["Unit"] = None

    @property
    def unit(self) -> Optional["Unit"]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional["Unit"]) -> None:
        """
        Set unit with validation.

        Args:
            value: The unit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unit = None
            return

        if not isinstance(value, Unit):
            raise TypeError(
                f"unit must be Unit or None, got {type(value).__name__}"
            )
        self._unit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRuleBased(self) -> "RuleBasedValue":
        """
        AUTOSAR-compliant getter for ruleBased.

        Returns:
            The ruleBased value

        Note:
            Delegates to rule_based property (CODING_RULE_V2_00017)
        """
        return self.rule_based  # Delegates to property

    def setRuleBased(self, value: "RuleBasedValue") -> RuleBasedValueCont:
        """
        AUTOSAR-compliant setter for ruleBased with method chaining.

        Args:
            value: The ruleBased to set

        Returns:
            self for method chaining

        Note:
            Delegates to rule_based property setter (gets validation automatically)
        """
        self.rule_based = value  # Delegates to property setter
        return self

    def getSwArraysize(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swArraysize.

        Returns:
            The swArraysize value

        Note:
            Delegates to sw_arraysize property (CODING_RULE_V2_00017)
        """
        return self.sw_arraysize  # Delegates to property

    def setSwArraysize(self, value: "RefType") -> RuleBasedValueCont:
        """
        AUTOSAR-compliant setter for swArraysize with method chaining.

        Args:
            value: The swArraysize to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_arraysize property setter (gets validation automatically)
        """
        self.sw_arraysize = value  # Delegates to property setter
        return self

    def getUnit(self) -> "Unit":
        """
        AUTOSAR-compliant getter for unit.

        Returns:
            The unit value

        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: "Unit") -> RuleBasedValueCont:
        """
        AUTOSAR-compliant setter for unit with method chaining.

        Args:
            value: The unit to set

        Returns:
            self for method chaining

        Note:
            Delegates to unit property setter (gets validation automatically)
        """
        self.unit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rule_based(self, value: Optional["RuleBasedValue"]) -> RuleBasedValueCont:
        """
        Set ruleBased and return self for chaining.

        Args:
            value: The ruleBased to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rule_based("value")
        """
        self.rule_based = value  # Use property setter (gets validation)
        return self

    def with_sw_arraysize(self, value: Optional[RefType]) -> RuleBasedValueCont:
        """
        Set swArraysize and return self for chaining.

        Args:
            value: The swArraysize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_arraysize("value")
        """
        self.sw_arraysize = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional["Unit"]) -> RuleBasedValueCont:
        """
        Set unit and return self for chaining.

        Args:
            value: The unit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unit("value")
        """
        self.unit = value  # Use property setter (gets validation)
        return self



class RuleBasedValueSpecification(ARObject):
    """
    This meta-class is used to support a rule-based initialization approach for
    data types with an array-nature (ApplicationArrayDataType and
    ImplementationDataType of category ARRAY) or a compound Application
    PrimitiveDataType (which also boils down to an array-nature).

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::RuleBasedValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 331, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 469, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the arguments for the RuleBasedValue atpVariation.
        self._arguments: Optional[RuleArguments] = None

    @property
    def arguments(self) -> Optional[RuleArguments]:
        """Get arguments (Pythonic accessor)."""
        return self._arguments

    @arguments.setter
    def arguments(self, value: Optional[RuleArguments]) -> None:
        """
        Set arguments with validation.

        Args:
            value: The arguments to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arguments = None
            return

        if not isinstance(value, RuleArguments):
            raise TypeError(
                f"arguments must be RuleArguments or None, got {type(value).__name__}"
            )
        self._arguments = value
        # rule shall fill the values.
        self._maxSizeToFill: Optional["Integer"] = None

    @property
    def max_size_to_fill(self) -> Optional["Integer"]:
        """Get maxSizeToFill (Pythonic accessor)."""
        return self._maxSizeToFill

    @max_size_to_fill.setter
    def max_size_to_fill(self, value: Optional["Integer"]) -> None:
        """
        Set maxSizeToFill with validation.

        Args:
            value: The maxSizeToFill to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSizeToFill = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxSizeToFill must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxSizeToFill = value
        # calculation which the arguments are used to values.
        self._rule: Optional["Identifier"] = None

    @property
    def rule(self) -> Optional["Identifier"]:
        """Get rule (Pythonic accessor)."""
        return self._rule

    @rule.setter
    def rule(self, value: Optional["Identifier"]) -> None:
        """
        Set rule with validation.

        Args:
            value: The rule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rule = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"rule must be Identifier or str or None, got {type(value).__name__}"
            )
        self._rule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArguments(self) -> RuleArguments:
        """
        AUTOSAR-compliant getter for arguments.

        Returns:
            The arguments value

        Note:
            Delegates to arguments property (CODING_RULE_V2_00017)
        """
        return self.arguments  # Delegates to property

    def setArguments(self, value: RuleArguments) -> RuleBasedValueSpecification:
        """
        AUTOSAR-compliant setter for arguments with method chaining.

        Args:
            value: The arguments to set

        Returns:
            self for method chaining

        Note:
            Delegates to arguments property setter (gets validation automatically)
        """
        self.arguments = value  # Delegates to property setter
        return self

    def getMaxSizeToFill(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxSizeToFill.

        Returns:
            The maxSizeToFill value

        Note:
            Delegates to max_size_to_fill property (CODING_RULE_V2_00017)
        """
        return self.max_size_to_fill  # Delegates to property

    def setMaxSizeToFill(self, value: "Integer") -> RuleBasedValueSpecification:
        """
        AUTOSAR-compliant setter for maxSizeToFill with method chaining.

        Args:
            value: The maxSizeToFill to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_size_to_fill property setter (gets validation automatically)
        """
        self.max_size_to_fill = value  # Delegates to property setter
        return self

    def getRule(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for rule.

        Returns:
            The rule value

        Note:
            Delegates to rule property (CODING_RULE_V2_00017)
        """
        return self.rule  # Delegates to property

    def setRule(self, value: "Identifier") -> RuleBasedValueSpecification:
        """
        AUTOSAR-compliant setter for rule with method chaining.

        Args:
            value: The rule to set

        Returns:
            self for method chaining

        Note:
            Delegates to rule property setter (gets validation automatically)
        """
        self.rule = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_arguments(self, value: Optional[RuleArguments]) -> RuleBasedValueSpecification:
        """
        Set arguments and return self for chaining.

        Args:
            value: The arguments to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_arguments("value")
        """
        self.arguments = value  # Use property setter (gets validation)
        return self

    def with_max_size_to_fill(self, value: Optional["Integer"]) -> RuleBasedValueSpecification:
        """
        Set maxSizeToFill and return self for chaining.

        Args:
            value: The maxSizeToFill to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_size_to_fill("value")
        """
        self.max_size_to_fill = value  # Use property setter (gets validation)
        return self

    def with_rule(self, value: Optional["Identifier"]) -> RuleBasedValueSpecification:
        """
        Set rule and return self for chaining.

        Args:
            value: The rule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rule("value")
        """
        self.rule = value  # Use property setter (gets validation)
        return self



class ValueSpecification(ARObject, ABC):
    """
    Base class for expressions leading to a value which can be used to
    initialize a data object.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 333, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 433, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2076, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ValueSpecification:
            raise TypeError("ValueSpecification is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This can be used to identify particular value specifications readers, for
        # example elements of a record type.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortLabel must be Identifier or str or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> ValueSpecification:
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_short_label(self, value: Optional["Identifier"]) -> ValueSpecification:
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self



class ConstantSpecificationMapping(ARObject):
    """
    This meta-class is used to create an association of two
    ConstantSpecifications. One Constant Specification is supposed to be defined
    in the application domain while the other should be defined in the
    implementation domain. Hence the ConstantSpecificationMapping needs to be
    used where a ConstantSpecification defined in one domain needs to be
    associated to a ConstantSpecification in the other domain. This information
    is crucial for the RTE generator.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ConstantSpecificationMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 443, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A ConstantSpecification defined in the application.
        self._applConstant: Optional[ConstantSpecification] = None

    @property
    def appl_constant(self) -> Optional[ConstantSpecification]:
        """Get applConstant (Pythonic accessor)."""
        return self._applConstant

    @appl_constant.setter
    def appl_constant(self, value: Optional[ConstantSpecification]) -> None:
        """
        Set applConstant with validation.

        Args:
            value: The applConstant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applConstant = None
            return

        if not isinstance(value, ConstantSpecification):
            raise TypeError(
                f"applConstant must be ConstantSpecification or None, got {type(value).__name__}"
            )
        self._applConstant = value
        self._implConstant: Optional[ConstantSpecification] = None

    @property
    def impl_constant(self) -> Optional[ConstantSpecification]:
        """Get implConstant (Pythonic accessor)."""
        return self._implConstant

    @impl_constant.setter
    def impl_constant(self, value: Optional[ConstantSpecification]) -> None:
        """
        Set implConstant with validation.

        Args:
            value: The implConstant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implConstant = None
            return

        if not isinstance(value, ConstantSpecification):
            raise TypeError(
                f"implConstant must be ConstantSpecification or None, got {type(value).__name__}"
            )
        self._implConstant = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplConstant(self) -> ConstantSpecification:
        """
        AUTOSAR-compliant getter for applConstant.

        Returns:
            The applConstant value

        Note:
            Delegates to appl_constant property (CODING_RULE_V2_00017)
        """
        return self.appl_constant  # Delegates to property

    def setApplConstant(self, value: ConstantSpecification) -> ConstantSpecificationMapping:
        """
        AUTOSAR-compliant setter for applConstant with method chaining.

        Args:
            value: The applConstant to set

        Returns:
            self for method chaining

        Note:
            Delegates to appl_constant property setter (gets validation automatically)
        """
        self.appl_constant = value  # Delegates to property setter
        return self

    def getImplConstant(self) -> ConstantSpecification:
        """
        AUTOSAR-compliant getter for implConstant.

        Returns:
            The implConstant value

        Note:
            Delegates to impl_constant property (CODING_RULE_V2_00017)
        """
        return self.impl_constant  # Delegates to property

    def setImplConstant(self, value: ConstantSpecification) -> ConstantSpecificationMapping:
        """
        AUTOSAR-compliant setter for implConstant with method chaining.

        Args:
            value: The implConstant to set

        Returns:
            self for method chaining

        Note:
            Delegates to impl_constant property setter (gets validation automatically)
        """
        self.impl_constant = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_appl_constant(self, value: Optional[ConstantSpecification]) -> ConstantSpecificationMapping:
        """
        Set applConstant and return self for chaining.

        Args:
            value: The applConstant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_appl_constant("value")
        """
        self.appl_constant = value  # Use property setter (gets validation)
        return self

    def with_impl_constant(self, value: Optional[ConstantSpecification]) -> ConstantSpecificationMapping:
        """
        Set implConstant and return self for chaining.

        Args:
            value: The implConstant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_impl_constant("value")
        """
        self.impl_constant = value  # Use property setter (gets validation)
        return self



class ConstantSpecificationMappingSet(ARElement):
    """
    This meta-class represents the ability to map two ConstantSpecifications to
    each others. One Constant Specification is supposed to be described in the
    application domain and the other should be described in the implementation
    domain.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ConstantSpecificationMappingSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 445, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ConstantSpecificationMappings owned by the Constant.
        self._mapping: List[ConstantSpecification] = []

    @property
    def mapping(self) -> List[ConstantSpecification]:
        """Get mapping (Pythonic accessor)."""
        return self._mapping

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMapping(self) -> List[ConstantSpecification]:
        """
        AUTOSAR-compliant getter for mapping.

        Returns:
            The mapping value

        Note:
            Delegates to mapping property (CODING_RULE_V2_00017)
        """
        return self.mapping  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class RuleBasedAxisCont(ARObject):
    """
    This represents the values for the axis of a compound primitive (curve,
    map). For standard and fix axes, SwAxisCont contains the values of the axis
    directly. The axis values of SwAxisCont with the category COM_AXIS, RES_AXIS
    are for display only. For editing and processing, only the values in the
    related GroupAxis are binding.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::RuleBasedAxisCont

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 464, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This category specifies the particular axis types: STD_AXIS (swArraysize
        # necessary).
        self._category: Optional["CalprmAxisCategory"] = None

    @property
    def category(self) -> Optional["CalprmAxisCategory"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["CalprmAxisCategory"]) -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, CalprmAxisCategory):
            raise TypeError(
                f"category must be CalprmAxisCategory or None, got {type(value).__name__}"
            )
        self._category = value
        # primitive (curve, map).
        self._ruleBased: Optional["RuleBasedValue"] = None

    @property
    def rule_based(self) -> Optional["RuleBasedValue"]:
        """Get ruleBased (Pythonic accessor)."""
        return self._ruleBased

    @rule_based.setter
    def rule_based(self, value: Optional["RuleBasedValue"]) -> None:
        """
        Set ruleBased with validation.

        Args:
            value: The ruleBased to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ruleBased = None
            return

        if not isinstance(value, RuleBasedValue):
            raise TypeError(
                f"ruleBased must be RuleBasedValue or None, got {type(value).__name__}"
            )
        self._ruleBased = value
        # ) necessary to know the dimensions.
        # They are specified.
        self._swArraysize: Optional["RefType"] = None

    @property
    def sw_arraysize(self) -> Optional["RefType"]:
        """Get swArraysize (Pythonic accessor)."""
        return self._swArraysize

    @sw_arraysize.setter
    def sw_arraysize(self, value: Optional["RefType"]) -> None:
        """
        Set swArraysize with validation.

        Args:
            value: The swArraysize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swArraysize = None
            return

        self._swArraysize = value
        # It is specified by numbers where 1 the x-axis.
        # It is also possible to derive the from the sequence of the parent.
        self._swAxisIndex: Optional["AxisIndexType"] = None

    @property
    def sw_axis_index(self) -> Optional["AxisIndexType"]:
        """Get swAxisIndex (Pythonic accessor)."""
        return self._swAxisIndex

    @sw_axis_index.setter
    def sw_axis_index(self, value: Optional["AxisIndexType"]) -> None:
        """
        Set swAxisIndex with validation.

        Args:
            value: The swAxisIndex to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swAxisIndex = None
            return

        if not isinstance(value, AxisIndexType):
            raise TypeError(
                f"swAxisIndex must be AxisIndexType or None, got {type(value).__name__}"
            )
        self._swAxisIndex = value
        self._unit: Optional["Unit"] = None

    @property
    def unit(self) -> Optional["Unit"]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional["Unit"]) -> None:
        """
        Set unit with validation.

        Args:
            value: The unit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unit = None
            return

        if not isinstance(value, Unit):
            raise TypeError(
                f"unit must be Unit or None, got {type(value).__name__}"
            )
        self._unit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> "CalprmAxisCategory":
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "CalprmAxisCategory") -> RuleBasedAxisCont:
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getRuleBased(self) -> "RuleBasedValue":
        """
        AUTOSAR-compliant getter for ruleBased.

        Returns:
            The ruleBased value

        Note:
            Delegates to rule_based property (CODING_RULE_V2_00017)
        """
        return self.rule_based  # Delegates to property

    def setRuleBased(self, value: "RuleBasedValue") -> RuleBasedAxisCont:
        """
        AUTOSAR-compliant setter for ruleBased with method chaining.

        Args:
            value: The ruleBased to set

        Returns:
            self for method chaining

        Note:
            Delegates to rule_based property setter (gets validation automatically)
        """
        self.rule_based = value  # Delegates to property setter
        return self

    def getSwArraysize(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swArraysize.

        Returns:
            The swArraysize value

        Note:
            Delegates to sw_arraysize property (CODING_RULE_V2_00017)
        """
        return self.sw_arraysize  # Delegates to property

    def setSwArraysize(self, value: "RefType") -> RuleBasedAxisCont:
        """
        AUTOSAR-compliant setter for swArraysize with method chaining.

        Args:
            value: The swArraysize to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_arraysize property setter (gets validation automatically)
        """
        self.sw_arraysize = value  # Delegates to property setter
        return self

    def getSwAxisIndex(self) -> "AxisIndexType":
        """
        AUTOSAR-compliant getter for swAxisIndex.

        Returns:
            The swAxisIndex value

        Note:
            Delegates to sw_axis_index property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_index  # Delegates to property

    def setSwAxisIndex(self, value: "AxisIndexType") -> RuleBasedAxisCont:
        """
        AUTOSAR-compliant setter for swAxisIndex with method chaining.

        Args:
            value: The swAxisIndex to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_axis_index property setter (gets validation automatically)
        """
        self.sw_axis_index = value  # Delegates to property setter
        return self

    def getUnit(self) -> "Unit":
        """
        AUTOSAR-compliant getter for unit.

        Returns:
            The unit value

        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: "Unit") -> RuleBasedAxisCont:
        """
        AUTOSAR-compliant setter for unit with method chaining.

        Args:
            value: The unit to set

        Returns:
            self for method chaining

        Note:
            Delegates to unit property setter (gets validation automatically)
        """
        self.unit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: Optional["CalprmAxisCategory"]) -> RuleBasedAxisCont:
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_rule_based(self, value: Optional["RuleBasedValue"]) -> RuleBasedAxisCont:
        """
        Set ruleBased and return self for chaining.

        Args:
            value: The ruleBased to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rule_based("value")
        """
        self.rule_based = value  # Use property setter (gets validation)
        return self

    def with_sw_arraysize(self, value: Optional[RefType]) -> RuleBasedAxisCont:
        """
        Set swArraysize and return self for chaining.

        Args:
            value: The swArraysize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_arraysize("value")
        """
        self.sw_arraysize = value  # Use property setter (gets validation)
        return self

    def with_sw_axis_index(self, value: Optional["AxisIndexType"]) -> RuleBasedAxisCont:
        """
        Set swAxisIndex and return self for chaining.

        Args:
            value: The swAxisIndex to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_axis_index("value")
        """
        self.sw_axis_index = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional["Unit"]) -> RuleBasedAxisCont:
        """
        Set unit and return self for chaining.

        Args:
            value: The unit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unit("value")
        """
        self.unit = value  # Use property setter (gets validation)
        return self



class CompositeRuleBasedValueArgument(ARObject, ABC):
    """
    This meta-class has the ability to serve as the abstract base class for
    ValueSpecifications that can be used for compound primitive data types.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::CompositeRuleBasedValueArgument

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 473, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is CompositeRuleBasedValueArgument:
            raise TypeError("CompositeRuleBasedValueArgument is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class NumericalValueSpecification(ValueSpecification):
    """
    A numerical ValueSpecification which is intended to be assigned to a
    Primitive data element. Note that the numerical value is a variant, it can
    be computed by a formula.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::NumericalValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 324, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 436, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2040, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the value itself.
        self._value: Optional["Numerical"] = None

    @property
    def value(self) -> Optional["Numerical"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["Numerical"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"value must be Numerical or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Numerical") -> NumericalValueSpecification:
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["Numerical"]) -> NumericalValueSpecification:
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



class ApplicationValueSpecification(ValueSpecification):
    """
    This meta-class represents values for DataPrototypes typed by
    ApplicationDataTypes (this includes in particular compound primitives). For
    further details refer to ASAM CDF 2.0. This meta-class corresponds to some
    extent with SW-INSTANCE in ASAM CDF 2.0.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ApplicationValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 299, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 455, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies to which category of ApplicationDataType this be applied (e.
        # g.
        # as an thus imposing constraints on the structure of the contained values, see
                # [constr_1006] 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate
                # Template R23-11.
        self._category: Optional["Identifier"] = None

    @property
    def category(self) -> Optional["Identifier"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["Identifier"]) -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"category must be Identifier or str or None, got {type(value).__name__}"
            )
        self._category = value
        # swAxisCont describes the x-axis, the second sw the y-axis, the third
                # swAxisCont z-axis.
        # In addition to this, the axis can be swAxisIndex.
        self._swAxisCont: List["SwAxisCont"] = []

    @property
    def sw_axis_cont(self) -> List["SwAxisCont"]:
        """Get swAxisCont (Pythonic accessor)."""
        return self._swAxisCont
        # This represents the values of a Compound Primitive Data.
        self._swValueCont: Optional["SwValueCont"] = None

    @property
    def sw_value_cont(self) -> Optional["SwValueCont"]:
        """Get swValueCont (Pythonic accessor)."""
        return self._swValueCont

    @sw_value_cont.setter
    def sw_value_cont(self, value: Optional["SwValueCont"]) -> None:
        """
        Set swValueCont with validation.

        Args:
            value: The swValueCont to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swValueCont = None
            return

        if not isinstance(value, SwValueCont):
            raise TypeError(
                f"swValueCont must be SwValueCont or None, got {type(value).__name__}"
            )
        self._swValueCont = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "Identifier") -> ApplicationValueSpecification:
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getSwAxisCont(self) -> List["SwAxisCont"]:
        """
        AUTOSAR-compliant getter for swAxisCont.

        Returns:
            The swAxisCont value

        Note:
            Delegates to sw_axis_cont property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_cont  # Delegates to property

    def getSwValueCont(self) -> "SwValueCont":
        """
        AUTOSAR-compliant getter for swValueCont.

        Returns:
            The swValueCont value

        Note:
            Delegates to sw_value_cont property (CODING_RULE_V2_00017)
        """
        return self.sw_value_cont  # Delegates to property

    def setSwValueCont(self, value: "SwValueCont") -> ApplicationValueSpecification:
        """
        AUTOSAR-compliant setter for swValueCont with method chaining.

        Args:
            value: The swValueCont to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_value_cont property setter (gets validation automatically)
        """
        self.sw_value_cont = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: Optional["Identifier"]) -> ApplicationValueSpecification:
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_sw_value_cont(self, value: Optional["SwValueCont"]) -> ApplicationValueSpecification:
        """
        Set swValueCont and return self for chaining.

        Args:
            value: The swValueCont to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_value_cont("value")
        """
        self.sw_value_cont = value  # Use property setter (gets validation)
        return self



class CompositeValueSpecification(ValueSpecification, ABC):
    """
    This abstract meta-class acts a base class for ValueSpecifications that have
    a composite form.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::CompositeValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 434, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is CompositeValueSpecification:
            raise TypeError("CompositeValueSpecification is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TextValueSpecification(ValueSpecification):
    """
    that vt uses the | operator to separate the values for the different
    bitfield masks in case that the semantics of the related DataPrototype is
    described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod.
    Table 5.113: TextValueSpecification [constr_1919] Existence of
    TextValueSpecification.value (cid:100)For each TextValueSpecification,
    attribute value shall exist at the time when the contract phase generation
    is executed.(cid:99)()

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::TextValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 435, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2074, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the value itself.
        self._value: Optional["VerbatimString"] = None

    @property
    def value(self) -> Optional["VerbatimString"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["VerbatimString"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"value must be VerbatimString or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "VerbatimString") -> TextValueSpecification:
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["VerbatimString"]) -> TextValueSpecification:
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



class ReferenceValueSpecification(ValueSpecification):
    """
    Specifies a reference to a data prototype to be used as an initial value for
    a pointer in the software.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ReferenceValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 436, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced data prototype.
        self._referenceValue: Optional["RefType"] = None

    @property
    def reference_value(self) -> Optional["RefType"]:
        """Get referenceValue (Pythonic accessor)."""
        return self._referenceValue

    @reference_value.setter
    def reference_value(self, value: Optional["RefType"]) -> None:
        """
        Set referenceValue with validation.

        Args:
            value: The referenceValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._referenceValue = None
            return

        self._referenceValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReferenceValue(self) -> "RefType":
        """
        AUTOSAR-compliant getter for referenceValue.

        Returns:
            The referenceValue value

        Note:
            Delegates to reference_value property (CODING_RULE_V2_00017)
        """
        return self.reference_value  # Delegates to property

    def setReferenceValue(self, value: "RefType") -> ReferenceValueSpecification:
        """
        AUTOSAR-compliant setter for referenceValue with method chaining.

        Args:
            value: The referenceValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to reference_value property setter (gets validation automatically)
        """
        self.reference_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_reference_value(self, value: Optional[RefType]) -> ReferenceValueSpecification:
        """
        Set referenceValue and return self for chaining.

        Args:
            value: The referenceValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reference_value("value")
        """
        self.reference_value = value  # Use property setter (gets validation)
        return self



class NotAvailableValueSpecification(ValueSpecification):
    """
    This meta-class provides the ability to specify a ValueSpecification to
    state that the respective element is not available. This ability is needed
    to support the existence of ApplicationRecordElements where attribute
    isOptional ist set to the value true.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::NotAvailableValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 440, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The content of this attribute shall be used to initialize gaps memory
                # occupied by a structured data type in the an NotAvailableValueSpecification
                # is used.
        # Note pattern is only applied during initialization!.
        self._defaultPattern: Optional["PositiveInteger"] = None

    @property
    def default_pattern(self) -> Optional["PositiveInteger"]:
        """Get defaultPattern (Pythonic accessor)."""
        return self._defaultPattern

    @default_pattern.setter
    def default_pattern(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set defaultPattern with validation.

        Args:
            value: The defaultPattern to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultPattern = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"defaultPattern must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._defaultPattern = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultPattern(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for defaultPattern.

        Returns:
            The defaultPattern value

        Note:
            Delegates to default_pattern property (CODING_RULE_V2_00017)
        """
        return self.default_pattern  # Delegates to property

    def setDefaultPattern(self, value: "PositiveInteger") -> NotAvailableValueSpecification:
        """
        AUTOSAR-compliant setter for defaultPattern with method chaining.

        Args:
            value: The defaultPattern to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_pattern property setter (gets validation automatically)
        """
        self.default_pattern = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_pattern(self, value: Optional["PositiveInteger"]) -> NotAvailableValueSpecification:
        """
        Set defaultPattern and return self for chaining.

        Args:
            value: The defaultPattern to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_pattern("value")
        """
        self.default_pattern = value  # Use property setter (gets validation)
        return self



class ConstantReference(ValueSpecification):
    """
    Instead of defining this value inline, a constant is referenced.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ConstantReference

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 440, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced constant.
        self._constant: Optional[ConstantSpecification] = None

    @property
    def constant(self) -> Optional[ConstantSpecification]:
        """Get constant (Pythonic accessor)."""
        return self._constant

    @constant.setter
    def constant(self, value: Optional[ConstantSpecification]) -> None:
        """
        Set constant with validation.

        Args:
            value: The constant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._constant = None
            return

        if not isinstance(value, ConstantSpecification):
            raise TypeError(
                f"constant must be ConstantSpecification or None, got {type(value).__name__}"
            )
        self._constant = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConstant(self) -> ConstantSpecification:
        """
        AUTOSAR-compliant getter for constant.

        Returns:
            The constant value

        Note:
            Delegates to constant property (CODING_RULE_V2_00017)
        """
        return self.constant  # Delegates to property

    def setConstant(self, value: ConstantSpecification) -> ConstantReference:
        """
        AUTOSAR-compliant setter for constant with method chaining.

        Args:
            value: The constant to set

        Returns:
            self for method chaining

        Note:
            Delegates to constant property setter (gets validation automatically)
        """
        self.constant = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_constant(self, value: Optional[ConstantSpecification]) -> ConstantReference:
        """
        Set constant and return self for chaining.

        Args:
            value: The constant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_constant("value")
        """
        self.constant = value  # Use property setter (gets validation)
        return self



class AbstractRuleBasedValueSpecification(ValueSpecification, ABC):
    """
    This represents an abstract base class for all rule-based value
    specifications.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::AbstractRuleBasedValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 462, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractRuleBasedValueSpecification:
            raise TypeError("AbstractRuleBasedValueSpecification is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ApplicationRuleBasedValueSpecification(CompositeRuleBasedValueArgument):
    """
    This meta-class represents rule based values for DataPrototypes typed by
    ApplicationDataTypes (ApplicationArrayDataType or a compound
    ApplicationPrimitiveDataType which also boils down to an array-nature).

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ApplicationRuleBasedValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 302, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 462, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the category of the RuleBasedValue.
        self._category: Optional["Identifier"] = None

    @property
    def category(self) -> Optional["Identifier"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["Identifier"]) -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"category must be Identifier or str or None, got {type(value).__name__}"
            )
        self._category = value
        # swAxisCont describes the x-axis, the second sw the y-axis, the third
                # swAxisCont z-axis.
        # In addition to this, the axis can be swAxisIndex.
        self._swAxisCont: List[RuleBasedAxisCont] = []

    @property
    def sw_axis_cont(self) -> List[RuleBasedAxisCont]:
        """Get swAxisCont (Pythonic accessor)."""
        return self._swAxisCont
        # This represents the values of an array or Compound.
        self._swValueCont: Optional[RuleBasedValueCont] = None

    @property
    def sw_value_cont(self) -> Optional[RuleBasedValueCont]:
        """Get swValueCont (Pythonic accessor)."""
        return self._swValueCont

    @sw_value_cont.setter
    def sw_value_cont(self, value: Optional[RuleBasedValueCont]) -> None:
        """
        Set swValueCont with validation.

        Args:
            value: The swValueCont to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swValueCont = None
            return

        if not isinstance(value, RuleBasedValueCont):
            raise TypeError(
                f"swValueCont must be RuleBasedValueCont or None, got {type(value).__name__}"
            )
        self._swValueCont = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "Identifier") -> ApplicationRuleBasedValueSpecification:
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getSwAxisCont(self) -> List[RuleBasedAxisCont]:
        """
        AUTOSAR-compliant getter for swAxisCont.

        Returns:
            The swAxisCont value

        Note:
            Delegates to sw_axis_cont property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_cont  # Delegates to property

    def getSwValueCont(self) -> RuleBasedValueCont:
        """
        AUTOSAR-compliant getter for swValueCont.

        Returns:
            The swValueCont value

        Note:
            Delegates to sw_value_cont property (CODING_RULE_V2_00017)
        """
        return self.sw_value_cont  # Delegates to property

    def setSwValueCont(self, value: RuleBasedValueCont) -> ApplicationRuleBasedValueSpecification:
        """
        AUTOSAR-compliant setter for swValueCont with method chaining.

        Args:
            value: The swValueCont to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_value_cont property setter (gets validation automatically)
        """
        self.sw_value_cont = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: Optional["Identifier"]) -> ApplicationRuleBasedValueSpecification:
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_sw_value_cont(self, value: Optional[RuleBasedValueCont]) -> ApplicationRuleBasedValueSpecification:
        """
        Set swValueCont and return self for chaining.

        Args:
            value: The swValueCont to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_value_cont("value")
        """
        self.sw_value_cont = value  # Use property setter (gets validation)
        return self



class ArrayValueSpecification(CompositeValueSpecification):
    """
    Specifies the values for an array.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ArrayValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 303, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 434, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1999, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The value for a single array element.
        # All Value aggregated by ArrayValueSpecification the same structure.
        # atpVariation.
        self._element: List[ValueSpecification] = []

    @property
    def element(self) -> List[ValueSpecification]:
        """Get element (Pythonic accessor)."""
        return self._element
        # This attribute shall only have a meaning for dynamic and shall be taken as a
        # sanity check: the number in the attribute shall be identical to the number of
        # attribute does not exist it means that no partial intended.
        self._intendedPartial: Optional["PositiveInteger"] = None

    @property
    def intended_partial(self) -> Optional["PositiveInteger"]:
        """Get intendedPartial (Pythonic accessor)."""
        return self._intendedPartial

    @intended_partial.setter
    def intended_partial(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set intendedPartial with validation.

        Args:
            value: The intendedPartial to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._intendedPartial = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"intendedPartial must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._intendedPartial = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElement(self) -> List[ValueSpecification]:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def getIntendedPartial(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for intendedPartial.

        Returns:
            The intendedPartial value

        Note:
            Delegates to intended_partial property (CODING_RULE_V2_00017)
        """
        return self.intended_partial  # Delegates to property

    def setIntendedPartial(self, value: "PositiveInteger") -> ArrayValueSpecification:
        """
        AUTOSAR-compliant setter for intendedPartial with method chaining.

        Args:
            value: The intendedPartial to set

        Returns:
            self for method chaining

        Note:
            Delegates to intended_partial property setter (gets validation automatically)
        """
        self.intended_partial = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_intended_partial(self, value: Optional["PositiveInteger"]) -> ArrayValueSpecification:
        """
        Set intendedPartial and return self for chaining.

        Args:
            value: The intendedPartial to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_intended_partial("value")
        """
        self.intended_partial = value  # Use property setter (gets validation)
        return self



class RecordValueSpecification(CompositeValueSpecification):
    """
    Specifies the values for a record.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::RecordValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 328, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 435, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class NumericalRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """
    This meta-class is used to support a rule-based initialization approach for
    data types with an array-nature (ImplementationDataType of category ARRAY).

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::NumericalRuleBasedValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 467, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the rule based value specification for the array.
        self._ruleBased: Optional["RuleBasedValue"] = None

    @property
    def rule_based(self) -> Optional["RuleBasedValue"]:
        """Get ruleBased (Pythonic accessor)."""
        return self._ruleBased

    @rule_based.setter
    def rule_based(self, value: Optional["RuleBasedValue"]) -> None:
        """
        Set ruleBased with validation.

        Args:
            value: The ruleBased to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ruleBased = None
            return

        if not isinstance(value, RuleBasedValue):
            raise TypeError(
                f"ruleBased must be RuleBasedValue or None, got {type(value).__name__}"
            )
        self._ruleBased = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRuleBased(self) -> "RuleBasedValue":
        """
        AUTOSAR-compliant getter for ruleBased.

        Returns:
            The ruleBased value

        Note:
            Delegates to rule_based property (CODING_RULE_V2_00017)
        """
        return self.rule_based  # Delegates to property

    def setRuleBased(self, value: "RuleBasedValue") -> NumericalRuleBasedValueSpecification:
        """
        AUTOSAR-compliant setter for ruleBased with method chaining.

        Args:
            value: The ruleBased to set

        Returns:
            self for method chaining

        Note:
            Delegates to rule_based property setter (gets validation automatically)
        """
        self.rule_based = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rule_based(self, value: Optional["RuleBasedValue"]) -> NumericalRuleBasedValueSpecification:
        """
        Set ruleBased and return self for chaining.

        Args:
            value: The ruleBased to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rule_based("value")
        """
        self.rule_based = value  # Use property setter (gets validation)
        return self



class CompositeRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """
    This meta-class represents rule-based values for DataPrototypes typed by
    composite AutosarDataTypes.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::CompositeRuleBasedValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 471, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the collection of aggregated Value Specifications.
        # The last ValueSpecification in the be taken to execute the filling rule.
        self._argument: List["CompositeValue"] = []

    @property
    def argument(self) -> List["CompositeValue"]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # This represents the collection of aggregated Value in the collection shall be
        # taken to the filling rule.
        self._compound: List["CompositeRuleBased"] = []

    @property
    def compound(self) -> List["CompositeRuleBased"]:
        """Get compound (Pythonic accessor)."""
        return self._compound
        # If a rule is chosen which does not fill until the end, this which size the
        # rule shall fill the values.
        self._maxSizeToFill: Optional["PositiveInteger"] = None

    @property
    def max_size_to_fill(self) -> Optional["PositiveInteger"]:
        """Get maxSizeToFill (Pythonic accessor)."""
        return self._maxSizeToFill

    @max_size_to_fill.setter
    def max_size_to_fill(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxSizeToFill with validation.

        Args:
            value: The maxSizeToFill to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSizeToFill = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxSizeToFill must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxSizeToFill = value
        # calculation which the arguments are used to values.
        self._rule: Optional["Identifier"] = None

    @property
    def rule(self) -> Optional["Identifier"]:
        """Get rule (Pythonic accessor)."""
        return self._rule

    @rule.setter
    def rule(self, value: Optional["Identifier"]) -> None:
        """
        Set rule with validation.

        Args:
            value: The rule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rule = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"rule must be Identifier or str or None, got {type(value).__name__}"
            )
        self._rule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List["CompositeValue"]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getCompound(self) -> List["CompositeRuleBased"]:
        """
        AUTOSAR-compliant getter for compound.

        Returns:
            The compound value

        Note:
            Delegates to compound property (CODING_RULE_V2_00017)
        """
        return self.compound  # Delegates to property

    def getMaxSizeToFill(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxSizeToFill.

        Returns:
            The maxSizeToFill value

        Note:
            Delegates to max_size_to_fill property (CODING_RULE_V2_00017)
        """
        return self.max_size_to_fill  # Delegates to property

    def setMaxSizeToFill(self, value: "PositiveInteger") -> CompositeRuleBasedValueSpecification:
        """
        AUTOSAR-compliant setter for maxSizeToFill with method chaining.

        Args:
            value: The maxSizeToFill to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_size_to_fill property setter (gets validation automatically)
        """
        self.max_size_to_fill = value  # Delegates to property setter
        return self

    def getRule(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for rule.

        Returns:
            The rule value

        Note:
            Delegates to rule property (CODING_RULE_V2_00017)
        """
        return self.rule  # Delegates to property

    def setRule(self, value: "Identifier") -> CompositeRuleBasedValueSpecification:
        """
        AUTOSAR-compliant setter for rule with method chaining.

        Args:
            value: The rule to set

        Returns:
            self for method chaining

        Note:
            Delegates to rule property setter (gets validation automatically)
        """
        self.rule = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_size_to_fill(self, value: Optional["PositiveInteger"]) -> CompositeRuleBasedValueSpecification:
        """
        Set maxSizeToFill and return self for chaining.

        Args:
            value: The maxSizeToFill to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_size_to_fill("value")
        """
        self.max_size_to_fill = value  # Use property setter (gets validation)
        return self

    def with_rule(self, value: Optional["Identifier"]) -> CompositeRuleBasedValueSpecification:
        """
        Set rule and return self for chaining.

        Args:
            value: The rule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rule("value")
        """
        self.rule = value  # Use property setter (gets validation)
        return self
