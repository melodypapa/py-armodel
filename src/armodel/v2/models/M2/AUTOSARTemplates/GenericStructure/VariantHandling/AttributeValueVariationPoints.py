"""
AUTOSAR Package - AttributeValueVariationPoints

Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
"""


from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    PackageableElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
    PositiveInteger,
    PrimitiveIdentifier,
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
    IntervalTypeEnum,
)


class NumericalValueVariationPoint(ARObject):
    """
    that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::NumericalValueVariationPoint

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 302, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 241, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    def with_entry(self, value):
        """
        Set entry and return self for chaining.

        Args:
            value: The entry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_entry("value")
        """
        self.entry = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AttributeValueVariationPoint(ARObject, ABC):
    """
    This class represents the ability to derive the value of the Attribute from
    a system constant (by Sw SystemconstDependentFormula). It also provides a
    bindingTime.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::AttributeValueVariationPoint

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 617, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 209, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 41, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AttributeValueVariationPoint:
            raise TypeError("AttributeValueVariationPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the binding time in which the attribute value needs bound.
        # attribute is missing, the attribute is not a variation particular this means
                # that It needs to be a single to the type specified in the pure model.
        # It error if it is still a formula.
        self._bindingTime: Optional[BindingTimeEnum] = None

    @property
    def binding_time(self) -> Optional[BindingTimeEnum]:
        """Get bindingTime (Pythonic accessor)."""
        return self._bindingTime

    @binding_time.setter
    def binding_time(self, value: Optional[BindingTimeEnum]) -> None:
        """
        Set bindingTime with validation.

        Args:
            value: The bindingTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bindingTime = None
            return

        if not isinstance(value, BindingTimeEnum):
            raise TypeError(
                f"bindingTime must be BindingTimeEnum or None, got {type(value).__name__}"
            )
        self._bindingTime = value
        # objects from the.
        self._blueprintValue: Optional[String] = None

    @property
    def blueprint_value(self) -> Optional[String]:
        """Get blueprintValue (Pythonic accessor)."""
        return self._blueprintValue

    @blueprint_value.setter
    def blueprint_value(self, value: Optional[String]) -> None:
        """
        Set blueprintValue with validation.

        Args:
            value: The blueprintValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._blueprintValue = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"blueprintValue must be String or str or None, got {type(value).__name__}"
            )
        self._blueprintValue = value
        # with variant management usage is subject of agreement between the.
        self._sd: Optional[String] = None

    @property
    def sd(self) -> Optional[String]:
        """Get sd (Pythonic accessor)."""
        return self._sd

    @sd.setter
    def sd(self, value: Optional[String]) -> None:
        """
        Set sd with validation.

        Args:
            value: The sd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sd = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"sd must be String or str or None, got {type(value).__name__}"
            )
        self._sd = value
        # It is also allow RTE support for CompileTime Variation.
        self._shortLabel: Optional[PrimitiveIdentifier] = None

    @property
    def short_label(self) -> Optional[PrimitiveIdentifier]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional[PrimitiveIdentifier]) -> None:
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

        if not isinstance(value, PrimitiveIdentifier):
            raise TypeError(
                f"shortLabel must be PrimitiveIdentifier or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBindingTime(self) -> BindingTimeEnum:
        """
        AUTOSAR-compliant getter for bindingTime.

        Returns:
            The bindingTime value

        Note:
            Delegates to binding_time property (CODING_RULE_V2_00017)
        """
        return self.binding_time  # Delegates to property

    def setBindingTime(self, value: BindingTimeEnum) -> AttributeValueVariationPoint:
        """
        AUTOSAR-compliant setter for bindingTime with method chaining.

        Args:
            value: The bindingTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to binding_time property setter (gets validation automatically)
        """
        self.binding_time = value  # Delegates to property setter
        return self

    def getBlueprintValue(self) -> String:
        """
        AUTOSAR-compliant getter for blueprintValue.

        Returns:
            The blueprintValue value

        Note:
            Delegates to blueprint_value property (CODING_RULE_V2_00017)
        """
        return self.blueprint_value  # Delegates to property

    def setBlueprintValue(self, value: String) -> AttributeValueVariationPoint:
        """
        AUTOSAR-compliant setter for blueprintValue with method chaining.

        Args:
            value: The blueprintValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to blueprint_value property setter (gets validation automatically)
        """
        self.blueprint_value = value  # Delegates to property setter
        return self

    def getSd(self) -> String:
        """
        AUTOSAR-compliant getter for sd.

        Returns:
            The sd value

        Note:
            Delegates to sd property (CODING_RULE_V2_00017)
        """
        return self.sd  # Delegates to property

    def setSd(self, value: String) -> AttributeValueVariationPoint:
        """
        AUTOSAR-compliant setter for sd with method chaining.

        Args:
            value: The sd to set

        Returns:
            self for method chaining

        Note:
            Delegates to sd property setter (gets validation automatically)
        """
        self.sd = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> PrimitiveIdentifier:
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: PrimitiveIdentifier) -> AttributeValueVariationPoint:
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

    def with_binding_time(self, value: Optional[BindingTimeEnum]) -> AttributeValueVariationPoint:
        """
        Set bindingTime and return self for chaining.

        Args:
            value: The bindingTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_binding_time("value")
        """
        self.binding_time = value  # Use property setter (gets validation)
        return self

    def with_blueprint_value(self, value: Optional[String]) -> AttributeValueVariationPoint:
        """
        Set blueprintValue and return self for chaining.

        Args:
            value: The blueprintValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_blueprint_value("value")
        """
        self.blueprint_value = value  # Use property setter (gets validation)
        return self

    def with_sd(self, value: Optional[String]) -> AttributeValueVariationPoint:
        """
        Set sd and return self for chaining.

        Args:
            value: The sd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sd("value")
        """
        self.sd = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional[PrimitiveIdentifier]) -> AttributeValueVariationPoint:
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



class AbstractNumericalVariationPoint(ARObject, ABC):
    """
    This is an abstract NumericalValueVariationPoint. It is introduced to
    support the case that additional attributes are required for particular
    purposes.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::AbstractNumericalVariationPoint

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 969, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 240, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractNumericalVariationPoint:
            raise TypeError("AbstractNumericalVariationPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BooleanValueVariationPoint(ARObject):
    """
    that this class might be used in the extended meta-model on

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::BooleanValueVariationPoint

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 240, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class FloatValueVariationPoint(ARObject):
    """
    that this class might be used in the extended meta-model only

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::FloatValueVariationPoint

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 240, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class IntegerValueVariationPoint(ARObject):
    """
    that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::IntegerValueVariationPoint

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 241, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class LimitValueVariationPoint(ARObject):
    """
    that the xml.name is "LIMIT" for backward compatibility reasons.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::LimitValueVariationPoint

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 241, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the type of the interval.
        # If the attribute is interval shall be considered as "CLOSED".
        self._intervalType: Optional[IntervalTypeEnum] = None

    @property
    def interval_type(self) -> Optional[IntervalTypeEnum]:
        """Get intervalType (Pythonic accessor)."""
        return self._intervalType

    @interval_type.setter
    def interval_type(self, value: Optional[IntervalTypeEnum]) -> None:
        """
        Set intervalType with validation.

        Args:
            value: The intervalType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._intervalType = None
            return

        if not isinstance(value, IntervalTypeEnum):
            raise TypeError(
                f"intervalType must be IntervalTypeEnum or None, got {type(value).__name__}"
            )
        self._intervalType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntervalType(self) -> IntervalTypeEnum:
        """
        AUTOSAR-compliant getter for intervalType.

        Returns:
            The intervalType value

        Note:
            Delegates to interval_type property (CODING_RULE_V2_00017)
        """
        return self.interval_type  # Delegates to property

    def setIntervalType(self, value: IntervalTypeEnum) -> LimitValueVariationPoint:
        """
        AUTOSAR-compliant setter for intervalType with method chaining.

        Args:
            value: The intervalType to set

        Returns:
            self for method chaining

        Note:
            Delegates to interval_type property setter (gets validation automatically)
        """
        self.interval_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_interval_type(self, value: Optional[IntervalTypeEnum]) -> LimitValueVariationPoint:
        """
        Set intervalType and return self for chaining.

        Args:
            value: The intervalType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interval_type("value")
        """
        self.interval_type = value  # Use property setter (gets validation)
        return self



class PositiveIntegerValueVariationPoint(ARObject):
    """
    that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::PositiveIntegerValueVariationPoint

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 241, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class UnlimitedIntegerValueVariationPoint(ARObject):
    """
    that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::UnlimitedIntegerValueVariationPoint

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 242, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TimeValueValueVariationPoint(ARObject):
    """
    This class represents the ability to express a formula for a numerical time
    value.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::TimeValueValueVariationPoint

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 242, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AbstractEnumerationValueVariationPoint(ARObject, ABC):
    """
    This is an abstract EnumerationValueVariationPoint. It is introduced to
    support the case that additional attributes are required for particular
    purposes.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::AbstractEnumerationValueVariationPoint

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 421, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractEnumerationValueVariationPoint:
            raise TypeError("AbstractEnumerationValueVariationPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute reflects the base to be used in context of this reference.
        self._base: Optional[Identifier] = None

    @property
    def base(self) -> Optional[Identifier]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional[Identifier]) -> None:
        """
        Set base with validation.

        Args:
            value: The base to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"base must be Identifier or str or None, got {type(value).__name__}"
            )
        self._base = value
        self._enumTable: Optional[RefType] = None

    @property
    def enum_table(self) -> Optional[RefType]:
        """Get enumTable (Pythonic accessor)."""
        return self._enumTable

    @enum_table.setter
    def enum_table(self, value: Optional[RefType]) -> None:
        """
        Set enumTable with validation.

        Args:
            value: The enumTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enumTable = None
            return

        self._enumTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> Identifier:
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: Identifier) -> AbstractEnumerationValueVariationPoint:
        """
        AUTOSAR-compliant setter for base with method chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getEnumTable(self) -> RefType:
        """
        AUTOSAR-compliant getter for enumTable.

        Returns:
            The enumTable value

        Note:
            Delegates to enum_table property (CODING_RULE_V2_00017)
        """
        return self.enum_table  # Delegates to property

    def setEnumTable(self, value: RefType) -> AbstractEnumerationValueVariationPoint:
        """
        AUTOSAR-compliant setter for enumTable with method chaining.

        Args:
            value: The enumTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to enum_table property setter (gets validation automatically)
        """
        self.enum_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional[Identifier]) -> AbstractEnumerationValueVariationPoint:
        """
        Set base and return self for chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_enum_table(self, value: Optional[RefType]) -> AbstractEnumerationValueVariationPoint:
        """
        Set enumTable and return self for chaining.

        Args:
            value: The enumTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enum_table("value")
        """
        self.enum_table = value  # Use property setter (gets validation)
        return self



class EnumerationMappingEntry(ARObject):
    """
    that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::EnumerationMappingEntry

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 443, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the symbolic value (e.
        # g.
        # in, out) of enumeration entry.
        self._enumerator: NameToken = None

    @property
    def enumerator(self) -> NameToken:
        """Get enumerator (Pythonic accessor)."""
        return self._enumerator

    @enumerator.setter
    def enumerator(self, value: NameToken) -> None:
        """
        Set enumerator with validation.

        Args:
            value: The enumerator to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"enumerator must be NameToken or str, got {type(value).__name__}"
            )
        self._enumerator = value
        # g.
        # 0, 1) of entry.
        # The numericalValue marks an M2 level.
        # It is not used in C-Code or at runtime.
        # is only given to be able to calculate a represents the enumerator literal in
                # a numerical.
        self._numericalValue: PositiveInteger = None

    @property
    def numerical_value(self) -> PositiveInteger:
        """Get numericalValue (Pythonic accessor)."""
        return self._numericalValue

    @numerical_value.setter
    def numerical_value(self, value: PositiveInteger) -> None:
        """
        Set numericalValue with validation.

        Args:
            value: The numericalValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"numericalValue must be PositiveInteger or str, got {type(value).__name__}"
            )
        self._numericalValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnumerator(self) -> NameToken:
        """
        AUTOSAR-compliant getter for enumerator.

        Returns:
            The enumerator value

        Note:
            Delegates to enumerator property (CODING_RULE_V2_00017)
        """
        return self.enumerator  # Delegates to property

    def setEnumerator(self, value: NameToken) -> EnumerationMappingEntry:
        """
        AUTOSAR-compliant setter for enumerator with method chaining.

        Args:
            value: The enumerator to set

        Returns:
            self for method chaining

        Note:
            Delegates to enumerator property setter (gets validation automatically)
        """
        self.enumerator = value  # Delegates to property setter
        return self

    def getNumericalValue(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for numericalValue.

        Returns:
            The numericalValue value

        Note:
            Delegates to numerical_value property (CODING_RULE_V2_00017)
        """
        return self.numerical_value  # Delegates to property

    def setNumericalValue(self, value: PositiveInteger) -> EnumerationMappingEntry:
        """
        AUTOSAR-compliant setter for numericalValue with method chaining.

        Args:
            value: The numericalValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to numerical_value property setter (gets validation automatically)
        """
        self.numerical_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_enumerator(self, value: NameToken) -> EnumerationMappingEntry:
        """
        Set enumerator and return self for chaining.

        Args:
            value: The enumerator to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enumerator("value")
        """
        self.enumerator = value  # Use property setter (gets validation)
        return self

    def with_numerical_value(self, value: PositiveInteger) -> EnumerationMappingEntry:
        """
        Set numericalValue and return self for chaining.

        Args:
            value: The numericalValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_numerical_value("value")
        """
        self.numerical_value = value  # Use property setter (gets validation)
        return self



class EnumerationMappingTable(PackageableElement):
    """
    that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::EnumerationMappingTable

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 444, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Key-value pair mapping enumeration values to unique.
        self._entry: List[RefType] = []

    @property
    def entry(self) -> List[RefType]:
        """Get entry (Pythonic accessor)."""
        return self._entry

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEntry(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for entry.

        Returns:
            The entry value

        Note:
            Delegates to entry property (CODING_RULE_V2_00017)
        """
        return self.entry  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
