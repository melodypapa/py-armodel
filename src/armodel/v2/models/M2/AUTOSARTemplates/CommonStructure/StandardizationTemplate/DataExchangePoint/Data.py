"""
AUTOSAR Package - Data

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common import (
    DataFormatElementReference,
    RestrictionWithSeverity,
    SpecElementScope,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    AbstractMultiplicityRestriction,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class ValueRestrictionWithSeverity(RestrictionWithSeverity):
    """
    Specifies valid values of primitive data types. A value is valid if all
    rules defined by this ValueRestriction evaluate to true.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ValueRestrictionWithSeverity

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 87, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    def with_class_content(self, value):
        """
        Set class_content and return self for chaining.

        Args:
            value: The class_content to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_class_content("value")
        """
        self.class_content = value  # Use property setter (gets validation)
        return self

    def with_sdg_tailoring(self, value):
        """
        Set sdg_tailoring and return self for chaining.

        Args:
            value: The sdg_tailoring to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdg_tailoring("value")
        """
        self.sdg_tailoring = value  # Use property setter (gets validation)
        return self

    def with_class_tailoring(self, value):
        """
        Set class_tailoring and return self for chaining.

        Args:
            value: The class_tailoring to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_class_tailoring("value")
        """
        self.class_tailoring = value  # Use property setter (gets validation)
        return self

    def with_sub_attribute(self, value):
        """
        Set sub_attribute and return self for chaining.

        Args:
            value: The sub_attribute to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_attribute("value")
        """
        self.sub_attribute = value  # Use property setter (gets validation)
        return self

    def with_type_tailoring(self, value):
        """
        Set type_tailoring and return self for chaining.

        Args:
            value: The type_tailoring to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_tailoring("value")
        """
        self.type_tailoring = value  # Use property setter (gets validation)
        return self

    def with_type_tailoring(self, value):
        """
        Set type_tailoring and return self for chaining.

        Args:
            value: The type_tailoring to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_tailoring("value")
        """
        self.type_tailoring = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class MultiplicityRestrictionWithSeverity(RestrictionWithSeverity):
    """
    Restriction that specifies the valid number of occurrences of an element in
    the current context.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::MultiplicityRestrictionWithSeverity

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 87, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class VariationRestrictionWithSeverity(RestrictionWithSeverity):
    """
    Defines constraints on the usage of variation and on the valid binding
    times.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::VariationRestrictionWithSeverity

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 88, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DataFormatElementScope(SpecElementScope, ABC):
    """
    This class specifies if a Meta Class, Meta Attribute, Constraint or SdgDef
    is relevant for the Data Exchange Point.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::DataFormatElementScope

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 91, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is DataFormatElementScope:
            raise TypeError("DataFormatElementScope is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AbstractClassTailoring(DataFormatElementReference, ABC):
    """
    Tailoring of abstract classes in the AUTOSAR meta-model

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::AbstractClassTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 101, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AbstractClassTailoring:
            raise TypeError("AbstractClassTailoring is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AbstractCondition(ARObject, ABC):
    """
    A premise upon which the fulfillment of an agreement depends

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::AbstractCondition

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 102, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCondition:
            raise TypeError("AbstractCondition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AttributeCondition(AbstractMultiplicityRestriction, ABC):
    """
    The AttributeCondition evaluates to true, if the referenced attribute is
    accepted by all rules of this condition.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::AttributeCondition

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 102, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AttributeCondition:
            raise TypeError("AttributeCondition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ClassTailoring(ARObject, ABC):
    """
    The ClassTailoring is an abstract class that allows the tailoring of its
    attributes, applicable constraints and Sdgs.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ClassTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 102, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is ClassTailoring:
            raise TypeError("ClassTailoring is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the accepted / not accepted content of the All rules apply that
        # fullfill the condition of the Class.
        self._classContent: List["ClassContent"] = []

    @property
    def class_content(self) -> List["ClassContent"]:
        """Get classContent (Pythonic accessor)."""
        return self._classContent
        # Specifies the multiplicity of the class in the current context.
        self._multiplicity: Optional["MultiplicityRestriction"] = None

    @property
    def multiplicity(self) -> Optional["MultiplicityRestriction"]:
        """Get multiplicity (Pythonic accessor)."""
        return self._multiplicity

    @multiplicity.setter
    def multiplicity(self, value: Optional["MultiplicityRestriction"]) -> None:
        """
        Set multiplicity with validation.

        Args:
            value: The multiplicity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multiplicity = None
            return

        if not isinstance(value, MultiplicityRestriction):
            raise TypeError(
                f"multiplicity must be MultiplicityRestriction or None, got {type(value).__name__}"
            )
        self._multiplicity = value
        # Tags: xml.
        # sequenceOffset=20.
        self._variation: Optional["VariationRestrictionWith"] = None

    @property
    def variation(self) -> Optional["VariationRestrictionWith"]:
        """Get variation (Pythonic accessor)."""
        return self._variation

    @variation.setter
    def variation(self, value: Optional["VariationRestrictionWith"]) -> None:
        """
        Set variation with validation.

        Args:
            value: The variation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variation = None
            return

        if not isinstance(value, VariationRestrictionWith):
            raise TypeError(
                f"variation must be VariationRestrictionWith or None, got {type(value).__name__}"
            )
        self._variation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClassContent(self) -> List["ClassContent"]:
        """
        AUTOSAR-compliant getter for classContent.

        Returns:
            The classContent value

        Note:
            Delegates to class_content property (CODING_RULE_V2_00017)
        """
        return self.class_content  # Delegates to property

    def getMultiplicity(self) -> "MultiplicityRestriction":
        """
        AUTOSAR-compliant getter for multiplicity.

        Returns:
            The multiplicity value

        Note:
            Delegates to multiplicity property (CODING_RULE_V2_00017)
        """
        return self.multiplicity  # Delegates to property

    def setMultiplicity(self, value: "MultiplicityRestriction") -> ClassTailoring:
        """
        AUTOSAR-compliant setter for multiplicity with method chaining.

        Args:
            value: The multiplicity to set

        Returns:
            self for method chaining

        Note:
            Delegates to multiplicity property setter (gets validation automatically)
        """
        self.multiplicity = value  # Delegates to property setter
        return self

    def getVariation(self) -> "VariationRestrictionWith":
        """
        AUTOSAR-compliant getter for variation.

        Returns:
            The variation value

        Note:
            Delegates to variation property (CODING_RULE_V2_00017)
        """
        return self.variation  # Delegates to property

    def setVariation(self, value: "VariationRestrictionWith") -> ClassTailoring:
        """
        AUTOSAR-compliant setter for variation with method chaining.

        Args:
            value: The variation to set

        Returns:
            self for method chaining

        Note:
            Delegates to variation property setter (gets validation automatically)
        """
        self.variation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_multiplicity(self, value: Optional["MultiplicityRestriction"]) -> ClassTailoring:
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

    def with_variation(self, value: Optional["VariationRestrictionWith"]) -> ClassTailoring:
        """
        Set variation and return self for chaining.

        Args:
            value: The variation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variation("value")
        """
        self.variation = value  # Use property setter (gets validation)
        return self



class ClassContentConditional(Identifiable):
    """
    Specifies the valid content of the class. The content can optionally depend
    on a condition. (E.g. value of attribute ’category’)

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ClassContentConditional

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 103, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tailorings of the owned and inherited attributes of this Classes.
        self._attribute: List[AttributeTailoring] = []

    @property
    def attribute(self) -> List[AttributeTailoring]:
        """Get attribute (Pythonic accessor)."""
        return self._attribute
        # The rules on the content of this class are enabled if the to true.
        self._condition: Optional[AbstractCondition] = None

    @property
    def condition(self) -> Optional[AbstractCondition]:
        """Get condition (Pythonic accessor)."""
        return self._condition

    @condition.setter
    def condition(self, value: Optional[AbstractCondition]) -> None:
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

        if not isinstance(value, AbstractCondition):
            raise TypeError(
                f"condition must be AbstractCondition or None, got {type(value).__name__}"
            )
        self._condition = value
        # Classes.
        self._constraint: List[ConstraintTailoring] = []

    @property
    def constraint(self) -> List[ConstraintTailoring]:
        """Get constraint (Pythonic accessor)."""
        return self._constraint
        # Specification of the applicable Special Data Group.
        self._sdgTailoring: List[SdgTailoring] = []

    @property
    def sdg_tailoring(self) -> List[SdgTailoring]:
        """Get sdgTailoring (Pythonic accessor)."""
        return self._sdgTailoring

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttribute(self) -> List[AttributeTailoring]:
        """
        AUTOSAR-compliant getter for attribute.

        Returns:
            The attribute value

        Note:
            Delegates to attribute property (CODING_RULE_V2_00017)
        """
        return self.attribute  # Delegates to property

    def getCondition(self) -> AbstractCondition:
        """
        AUTOSAR-compliant getter for condition.

        Returns:
            The condition value

        Note:
            Delegates to condition property (CODING_RULE_V2_00017)
        """
        return self.condition  # Delegates to property

    def setCondition(self, value: AbstractCondition) -> ClassContentConditional:
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

    def getConstraint(self) -> List[ConstraintTailoring]:
        """
        AUTOSAR-compliant getter for constraint.

        Returns:
            The constraint value

        Note:
            Delegates to constraint property (CODING_RULE_V2_00017)
        """
        return self.constraint  # Delegates to property

    def getSdgTailoring(self) -> List[SdgTailoring]:
        """
        AUTOSAR-compliant getter for sdgTailoring.

        Returns:
            The sdgTailoring value

        Note:
            Delegates to sdg_tailoring property (CODING_RULE_V2_00017)
        """
        return self.sdg_tailoring  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_condition(self, value: Optional[AbstractCondition]) -> ClassContentConditional:
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



class ConstraintTailoring(RestrictionWithSeverity):
    """
    Tailoring of constraints. If a constraint is in scope, then the severity
    defines its Error Severity Level. If it is not in scope, then the constraint
    is disabled.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ConstraintTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 117, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to custom specification of constraint.
        self._constraint: Optional["TraceableText"] = None

    @property
    def constraint(self) -> Optional["TraceableText"]:
        """Get constraint (Pythonic accessor)."""
        return self._constraint

    @constraint.setter
    def constraint(self, value: Optional["TraceableText"]) -> None:
        """
        Set constraint with validation.

        Args:
            value: The constraint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._constraint = None
            return

        if not isinstance(value, TraceableText):
            raise TypeError(
                f"constraint must be TraceableText or None, got {type(value).__name__}"
            )
        self._constraint = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConstraint(self) -> "TraceableText":
        """
        AUTOSAR-compliant getter for constraint.

        Returns:
            The constraint value

        Note:
            Delegates to constraint property (CODING_RULE_V2_00017)
        """
        return self.constraint  # Delegates to property

    def setConstraint(self, value: "TraceableText") -> ConstraintTailoring:
        """
        AUTOSAR-compliant setter for constraint with method chaining.

        Args:
            value: The constraint to set

        Returns:
            self for method chaining

        Note:
            Delegates to constraint property setter (gets validation automatically)
        """
        self.constraint = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_constraint(self, value: Optional["TraceableText"]) -> ConstraintTailoring:
        """
        Set constraint and return self for chaining.

        Args:
            value: The constraint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_constraint("value")
        """
        self.constraint = value  # Use property setter (gets validation)
        return self



class SdgTailoring(RestrictionWithSeverity):
    """
    Describes if the referenced Sdg may be attached to the current class.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::SdgTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 118, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification of the structure of the Special Data Group.
        self._sdgClass: Optional["SdgClass"] = None

    @property
    def sdg_class(self) -> Optional["SdgClass"]:
        """Get sdgClass (Pythonic accessor)."""
        return self._sdgClass

    @sdg_class.setter
    def sdg_class(self, value: Optional["SdgClass"]) -> None:
        """
        Set sdgClass with validation.

        Args:
            value: The sdgClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdgClass = None
            return

        if not isinstance(value, SdgClass):
            raise TypeError(
                f"sdgClass must be SdgClass or None, got {type(value).__name__}"
            )
        self._sdgClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSdgClass(self) -> "SdgClass":
        """
        AUTOSAR-compliant getter for sdgClass.

        Returns:
            The sdgClass value

        Note:
            Delegates to sdg_class property (CODING_RULE_V2_00017)
        """
        return self.sdg_class  # Delegates to property

    def setSdgClass(self, value: "SdgClass") -> SdgTailoring:
        """
        AUTOSAR-compliant setter for sdgClass with method chaining.

        Args:
            value: The sdgClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to sdg_class property setter (gets validation automatically)
        """
        self.sdg_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sdg_class(self, value: Optional["SdgClass"]) -> SdgTailoring:
        """
        Set sdgClass and return self for chaining.

        Args:
            value: The sdgClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdg_class("value")
        """
        self.sdg_class = value  # Use property setter (gets validation)
        return self



class DataFormatTailoring(ARObject):
    """
    This class collects all rules that tailor the AUTOSAR templates for a
    specific data exchange point.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::DataFormatTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 180, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification of tailorings of Meta Classes.
        self._classTailoring: List[ClassTailoring] = []

    @property
    def class_tailoring(self) -> List[ClassTailoring]:
        """Get classTailoring (Pythonic accessor)."""
        return self._classTailoring
        # Specification of tailorings of Constraints that are not owned by any
        # Meta-Class.
        self._constraint: List[ConstraintTailoring] = []

    @property
    def constraint(self) -> List[ConstraintTailoring]:
        """Get constraint (Pythonic accessor)."""
        return self._constraint

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClassTailoring(self) -> List[ClassTailoring]:
        """
        AUTOSAR-compliant getter for classTailoring.

        Returns:
            The classTailoring value

        Note:
            Delegates to class_tailoring property (CODING_RULE_V2_00017)
        """
        return self.class_tailoring  # Delegates to property

    def getConstraint(self) -> List[ConstraintTailoring]:
        """
        AUTOSAR-compliant getter for constraint.

        Returns:
            The constraint value

        Note:
            Delegates to constraint property (CODING_RULE_V2_00017)
        """
        return self.constraint  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class UnresolvedReferenceRestrictionWithSeverity(RestrictionWithSeverity):
    """
    This restriction defines the severity level of unresolved references.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::UnresolvedReferenceRestrictionWithSeverity

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 222, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ConcreteClassTailoring(DataFormatElementScope):
    """
    Tailoring of concrete meta classes.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ConcreteClassTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 103, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification if this concrete Meta-Class is a root element I.
        # e.
        # : The validation starts at an object of this and continues by following all
                # references that are in scope of this Point.
        self._validationRoot: Optional[Boolean] = None

    @property
    def validation_root(self) -> Optional[Boolean]:
        """Get validationRoot (Pythonic accessor)."""
        return self._validationRoot

    @validation_root.setter
    def validation_root(self, value: Optional[Boolean]) -> None:
        """
        Set validationRoot with validation.

        Args:
            value: The validationRoot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._validationRoot = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"validationRoot must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._validationRoot = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValidationRoot(self) -> Boolean:
        """
        AUTOSAR-compliant getter for validationRoot.

        Returns:
            The validationRoot value

        Note:
            Delegates to validation_root property (CODING_RULE_V2_00017)
        """
        return self.validation_root  # Delegates to property

    def setValidationRoot(self, value: Boolean) -> ConcreteClassTailoring:
        """
        AUTOSAR-compliant setter for validationRoot with method chaining.

        Args:
            value: The validationRoot to set

        Returns:
            self for method chaining

        Note:
            Delegates to validation_root property setter (gets validation automatically)
        """
        self.validation_root = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_validation_root(self, value: Optional[Boolean]) -> ConcreteClassTailoring:
        """
        Set validationRoot and return self for chaining.

        Args:
            value: The validationRoot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_validation_root("value")
        """
        self.validation_root = value  # Use property setter (gets validation)
        return self



class AttributeTailoring(DataFormatElementScope, ABC):
    """
    Tailoring of Attributes

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::AttributeTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 109, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AttributeTailoring:
            raise TypeError("AttributeTailoring is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Multiplicity restriction of the attribute Tags: xml.
        # sequenceOffset=10.
        self._multiplicity: Optional["MultiplicityRestriction"] = None

    @property
    def multiplicity(self) -> Optional["MultiplicityRestriction"]:
        """Get multiplicity (Pythonic accessor)."""
        return self._multiplicity

    @multiplicity.setter
    def multiplicity(self, value: Optional["MultiplicityRestriction"]) -> None:
        """
        Set multiplicity with validation.

        Args:
            value: The multiplicity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multiplicity = None
            return

        if not isinstance(value, MultiplicityRestriction):
            raise TypeError(
                f"multiplicity must be MultiplicityRestriction or None, got {type(value).__name__}"
            )
        self._multiplicity = value
        # Tags: xml.
        # sequenceOffset=20.
        self._variation: Optional["VariationRestrictionWith"] = None

    @property
    def variation(self) -> Optional["VariationRestrictionWith"]:
        """Get variation (Pythonic accessor)."""
        return self._variation

    @variation.setter
    def variation(self, value: Optional["VariationRestrictionWith"]) -> None:
        """
        Set variation with validation.

        Args:
            value: The variation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variation = None
            return

        if not isinstance(value, VariationRestrictionWith):
            raise TypeError(
                f"variation must be VariationRestrictionWith or None, got {type(value).__name__}"
            )
        self._variation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMultiplicity(self) -> "MultiplicityRestriction":
        """
        AUTOSAR-compliant getter for multiplicity.

        Returns:
            The multiplicity value

        Note:
            Delegates to multiplicity property (CODING_RULE_V2_00017)
        """
        return self.multiplicity  # Delegates to property

    def setMultiplicity(self, value: "MultiplicityRestriction") -> AttributeTailoring:
        """
        AUTOSAR-compliant setter for multiplicity with method chaining.

        Args:
            value: The multiplicity to set

        Returns:
            self for method chaining

        Note:
            Delegates to multiplicity property setter (gets validation automatically)
        """
        self.multiplicity = value  # Delegates to property setter
        return self

    def getVariation(self) -> "VariationRestrictionWith":
        """
        AUTOSAR-compliant getter for variation.

        Returns:
            The variation value

        Note:
            Delegates to variation property (CODING_RULE_V2_00017)
        """
        return self.variation  # Delegates to property

    def setVariation(self, value: "VariationRestrictionWith") -> AttributeTailoring:
        """
        AUTOSAR-compliant setter for variation with method chaining.

        Args:
            value: The variation to set

        Returns:
            self for method chaining

        Note:
            Delegates to variation property setter (gets validation automatically)
        """
        self.variation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_multiplicity(self, value: Optional["MultiplicityRestriction"]) -> AttributeTailoring:
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

    def with_variation(self, value: Optional["VariationRestrictionWith"]) -> AttributeTailoring:
        """
        Set variation and return self for chaining.

        Args:
            value: The variation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variation("value")
        """
        self.variation = value  # Use property setter (gets validation)
        return self



class InvertCondition(AbstractCondition):
    """
    inverts the nested condition

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::InvertCondition

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 104, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The inverted condition.
        self._condition: AbstractCondition = None

    @property
    def condition(self) -> AbstractCondition:
        """Get condition (Pythonic accessor)."""
        return self._condition

    @condition.setter
    def condition(self, value: AbstractCondition) -> None:
        """
        Set condition with validation.

        Args:
            value: The condition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AbstractCondition):
            raise TypeError(
                f"condition must be AbstractCondition, got {type(value).__name__}"
            )
        self._condition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCondition(self) -> AbstractCondition:
        """
        AUTOSAR-compliant getter for condition.

        Returns:
            The condition value

        Note:
            Delegates to condition property (CODING_RULE_V2_00017)
        """
        return self.condition  # Delegates to property

    def setCondition(self, value: AbstractCondition) -> InvertCondition:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_condition(self, value: AbstractCondition) -> InvertCondition:
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



class TextualCondition(AbstractCondition):
    """
    Specifies additional conditions for one or more model elements. The
    condition is described using human language.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::TextualCondition

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 105, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Human language description of the condition.
        self._text: String = None

    @property
    def text(self) -> String:
        """Get text (Pythonic accessor)."""
        return self._text

    @text.setter
    def text(self, value: String) -> None:
        """
        Set text with validation.

        Args:
            value: The text to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"text must be String or str, got {type(value).__name__}"
            )
        self._text = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getText(self) -> String:
        """
        AUTOSAR-compliant getter for text.

        Returns:
            The text value

        Note:
            Delegates to text property (CODING_RULE_V2_00017)
        """
        return self.text  # Delegates to property

    def setText(self, value: String) -> TextualCondition:
        """
        AUTOSAR-compliant setter for text with method chaining.

        Args:
            value: The text to set

        Returns:
            self for method chaining

        Note:
            Delegates to text property setter (gets validation automatically)
        """
        self.text = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_text(self, value: String) -> TextualCondition:
        """
        Set text and return self for chaining.

        Args:
            value: The text to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_text("value")
        """
        self.text = value  # Use property setter (gets validation)
        return self



class AggregationCondition(AttributeCondition):
    """
    The AggregationCondition evaluates to true, if the referenced aggregation is
    accepted by all rules of this condition.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::AggregationCondition

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 102, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The aggregation that has to be accepted by the this AggregationCondition.
        self._aggregation: AggregationTailoring = None

    @property
    def aggregation(self) -> AggregationTailoring:
        """Get aggregation (Pythonic accessor)."""
        return self._aggregation

    @aggregation.setter
    def aggregation(self, value: AggregationTailoring) -> None:
        """
        Set aggregation with validation.

        Args:
            value: The aggregation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AggregationTailoring):
            raise TypeError(
                f"aggregation must be AggregationTailoring, got {type(value).__name__}"
            )
        self._aggregation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAggregation(self) -> AggregationTailoring:
        """
        AUTOSAR-compliant getter for aggregation.

        Returns:
            The aggregation value

        Note:
            Delegates to aggregation property (CODING_RULE_V2_00017)
        """
        return self.aggregation  # Delegates to property

    def setAggregation(self, value: AggregationTailoring) -> AggregationCondition:
        """
        AUTOSAR-compliant setter for aggregation with method chaining.

        Args:
            value: The aggregation to set

        Returns:
            self for method chaining

        Note:
            Delegates to aggregation property setter (gets validation automatically)
        """
        self.aggregation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_aggregation(self, value: AggregationTailoring) -> AggregationCondition:
        """
        Set aggregation and return self for chaining.

        Args:
            value: The aggregation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aggregation("value")
        """
        self.aggregation = value  # Use property setter (gets validation)
        return self



class PrimitiveAttributeCondition(AttributeCondition):
    """
    The PrimitiveAttributeCondition evaluates to true, if the referenced
    primitive attribute is accepted by all rules of this condition.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::PrimitiveAttributeCondition

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 104, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The primitive attribute that has to be accepted by the of this
        # PrimitiveAttributeCondition.
        self._attribute: "PrimitiveAttribute" = None

    @property
    def attribute(self) -> "PrimitiveAttribute":
        """Get attribute (Pythonic accessor)."""
        return self._attribute

    @attribute.setter
    def attribute(self, value: "PrimitiveAttribute") -> None:
        """
        Set attribute with validation.

        Args:
            value: The attribute to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PrimitiveAttribute):
            raise TypeError(
                f"attribute must be PrimitiveAttribute, got {type(value).__name__}"
            )
        self._attribute = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttribute(self) -> "PrimitiveAttribute":
        """
        AUTOSAR-compliant getter for attribute.

        Returns:
            The attribute value

        Note:
            Delegates to attribute property (CODING_RULE_V2_00017)
        """
        return self.attribute  # Delegates to property

    def setAttribute(self, value: "PrimitiveAttribute") -> PrimitiveAttributeCondition:
        """
        AUTOSAR-compliant setter for attribute with method chaining.

        Args:
            value: The attribute to set

        Returns:
            self for method chaining

        Note:
            Delegates to attribute property setter (gets validation automatically)
        """
        self.attribute = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_attribute(self, value: "PrimitiveAttribute") -> PrimitiveAttributeCondition:
        """
        Set attribute and return self for chaining.

        Args:
            value: The attribute to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_attribute("value")
        """
        self.attribute = value  # Use property setter (gets validation)
        return self



class ReferenceCondition(AttributeCondition):
    """
    The ReferenceCondition evaluates to true, if the referenced reference is
    accepted by all rules of this condition.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ReferenceCondition

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 104, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The reference that has to be accepted by the restrictions ReferenceCondition.
        self._reference: RefType = None

    @property
    def reference(self) -> RefType:
        """Get reference (Pythonic accessor)."""
        return self._reference

    @reference.setter
    def reference(self, value: RefType) -> None:
        """
        Set reference with validation.

        Args:
            value: The reference to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._reference = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReference(self) -> RefType:
        """
        AUTOSAR-compliant getter for reference.

        Returns:
            The reference value

        Note:
            Delegates to reference property (CODING_RULE_V2_00017)
        """
        return self.reference  # Delegates to property

    def setReference(self, value: RefType) -> ReferenceCondition:
        """
        AUTOSAR-compliant setter for reference with method chaining.

        Args:
            value: The reference to set

        Returns:
            self for method chaining

        Note:
            Delegates to reference property setter (gets validation automatically)
        """
        self.reference = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_reference(self, value: RefType) -> ReferenceCondition:
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



class PrimitiveAttributeTailoring(AttributeTailoring):
    """
    Tailoring of primitive attributes. Primitive attributes are attributes that
    have a type which is marked by the stereotype <<primitive>> or
    <<enumeration>>

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::PrimitiveAttributeTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 111, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification of how to handle AUTOSAR defined default values.
        self._defaultValue: Optional["DefaultValueApplication"] = None

    @property
    def default_value(self) -> Optional["DefaultValueApplication"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["DefaultValueApplication"]) -> None:
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

        if not isinstance(value, DefaultValueApplication):
            raise TypeError(
                f"defaultValue must be DefaultValueApplication or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        self._subAttribute: List["PrimitiveAttribute"] = []

    @property
    def sub_attribute(self) -> List["PrimitiveAttribute"]:
        """Get subAttribute (Pythonic accessor)."""
        return self._subAttribute
        # The restriction of the attribute value.
        self._valueRestrictionSeverity: Optional["ValueRestrictionWith"] = None

    @property
    def value_restriction_severity(self) -> Optional["ValueRestrictionWith"]:
        """Get valueRestrictionSeverity (Pythonic accessor)."""
        return self._valueRestrictionSeverity

    @value_restriction_severity.setter
    def value_restriction_severity(self, value: Optional["ValueRestrictionWith"]) -> None:
        """
        Set valueRestrictionSeverity with validation.

        Args:
            value: The valueRestrictionSeverity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._valueRestrictionSeverity = None
            return

        if not isinstance(value, ValueRestrictionWith):
            raise TypeError(
                f"valueRestrictionSeverity must be ValueRestrictionWith or None, got {type(value).__name__}"
            )
        self._valueRestrictionSeverity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "DefaultValueApplication":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "DefaultValueApplication") -> PrimitiveAttributeTailoring:
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

    def getSubAttribute(self) -> List["PrimitiveAttribute"]:
        """
        AUTOSAR-compliant getter for subAttribute.

        Returns:
            The subAttribute value

        Note:
            Delegates to sub_attribute property (CODING_RULE_V2_00017)
        """
        return self.sub_attribute  # Delegates to property

    def getValueRestrictionSeverity(self) -> "ValueRestrictionWith":
        """
        AUTOSAR-compliant getter for valueRestrictionSeverity.

        Returns:
            The valueRestrictionSeverity value

        Note:
            Delegates to value_restriction_severity property (CODING_RULE_V2_00017)
        """
        return self.value_restriction_severity  # Delegates to property

    def setValueRestrictionSeverity(self, value: "ValueRestrictionWith") -> PrimitiveAttributeTailoring:
        """
        AUTOSAR-compliant setter for valueRestrictionSeverity with method chaining.

        Args:
            value: The valueRestrictionSeverity to set

        Returns:
            self for method chaining

        Note:
            Delegates to value_restriction_severity property setter (gets validation automatically)
        """
        self.value_restriction_severity = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["DefaultValueApplication"]) -> PrimitiveAttributeTailoring:
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

    def with_value_restriction_severity(self, value: Optional["ValueRestrictionWith"]) -> PrimitiveAttributeTailoring:
        """
        Set valueRestrictionSeverity and return self for chaining.

        Args:
            value: The valueRestrictionSeverity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value_restriction_severity("value")
        """
        self.value_restriction_severity = value  # Use property setter (gets validation)
        return self



class AggregationTailoring(AttributeTailoring):
    """
    Tailoring of aggregations in the AUTOSAR meta-model

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::AggregationTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 113, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Local class tailoring which is applied if the content is this aggregation.
        self._typeTailoring: List[ClassTailoring] = []

    @property
    def type_tailoring(self) -> List[ClassTailoring]:
        """Get typeTailoring (Pythonic accessor)."""
        return self._typeTailoring

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTypeTailoring(self) -> List[ClassTailoring]:
        """
        AUTOSAR-compliant getter for typeTailoring.

        Returns:
            The typeTailoring value

        Note:
            Delegates to type_tailoring property (CODING_RULE_V2_00017)
        """
        return self.type_tailoring  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ReferenceTailoring(AttributeTailoring):
    """
    Tailoring of Non-Containment References.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ReferenceTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 115, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Local class tailoring for content that is referenced by this.
        self._typeTailoring: List[ClassTailoring] = []

    @property
    def type_tailoring(self) -> List[ClassTailoring]:
        """Get typeTailoring (Pythonic accessor)."""
        return self._typeTailoring
        # Specifies the severity of unresolved references.
        self._unresolvedRestriction: Optional[RefType] = None

    @property
    def unresolved_restriction(self) -> Optional[RefType]:
        """Get unresolvedRestriction (Pythonic accessor)."""
        return self._unresolvedRestriction

    @unresolved_restriction.setter
    def unresolved_restriction(self, value: Optional[RefType]) -> None:
        """
        Set unresolvedRestriction with validation.

        Args:
            value: The unresolvedRestriction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unresolvedRestriction = None
            return

        self._unresolvedRestriction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTypeTailoring(self) -> List[ClassTailoring]:
        """
        AUTOSAR-compliant getter for typeTailoring.

        Returns:
            The typeTailoring value

        Note:
            Delegates to type_tailoring property (CODING_RULE_V2_00017)
        """
        return self.type_tailoring  # Delegates to property

    def getUnresolvedRestriction(self) -> RefType:
        """
        AUTOSAR-compliant getter for unresolvedRestriction.

        Returns:
            The unresolvedRestriction value

        Note:
            Delegates to unresolved_restriction property (CODING_RULE_V2_00017)
        """
        return self.unresolved_restriction  # Delegates to property

    def setUnresolvedRestriction(self, value: RefType) -> ReferenceTailoring:
        """
        AUTOSAR-compliant setter for unresolvedRestriction with method chaining.

        Args:
            value: The unresolvedRestriction to set

        Returns:
            self for method chaining

        Note:
            Delegates to unresolved_restriction property setter (gets validation automatically)
        """
        self.unresolved_restriction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_unresolved_restriction(self, value: Optional[RefType]) -> ReferenceTailoring:
        """
        Set unresolvedRestriction and return self for chaining.

        Args:
            value: The unresolvedRestriction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unresolved_restriction("value")
        """
        self.unresolved_restriction = value  # Use property setter (gets validation)
        return self


class DefaultValueApplicationStrategyEnum(AREnum):
    """
    DefaultValueApplicationStrategyEnum enumeration

Enumeration that describes how to handle AUTOSAR defined default values. If the strategy requires application of the AUTOSAR defined default value, then the value shall be added before further validation or processing. Aggregated by PrimitiveAttributeTailoring.defaultValueHandling

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data
    """
    # If the AUTOSAR model is older than the Baseline of the Data Exchange Point and the older version Update did not yet support the attribute, then the AUTOSAR defined default value SHALL be applied before further validation or processing.
    defaultIfRevision = "1"

    # If the AUTOSAR model does not explicitly specify a value, then the apply the AUTOSAR defined default value before further validation or processing. noDefault do not apply the AUTOSAR defined default value
    defaultIfUndefined = "0"
