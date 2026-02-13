"""
AUTOSAR Package - HwElementCategory

Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.__init__ import (
    HwDescriptionEntity,
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
    Boolean,
)


class HwAttributeValue(ARObject):
    """
    This metaclass represents the ability to assign a hardware attribute value.
    Note that v and vt are mutually exclusive.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory::HwAttributeValue

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 16, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional annotation that can be added to each Hw.
        self._annotation: Optional[Annotation] = None

    @property
    def annotation(self) -> Optional[Annotation]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation

    @annotation.setter
    def annotation(self, value: Optional[Annotation]) -> None:
        """
        Set annotation with validation.

        Args:
            value: The annotation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._annotation = None
            return

        if not isinstance(value, Annotation):
            raise TypeError(
                f"annotation must be Annotation or None, got {type(value).__name__}"
            )
        self._annotation = value
        self._hwAttributeDef: Optional[HwAttributeDef] = None

    @property
    def hw_attribute_def(self) -> Optional[HwAttributeDef]:
        """Get hwAttributeDef (Pythonic accessor)."""
        return self._hwAttributeDef

    @hw_attribute_def.setter
    def hw_attribute_def(self, value: Optional[HwAttributeDef]) -> None:
        """
        Set hwAttributeDef with validation.

        Args:
            value: The hwAttributeDef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hwAttributeDef = None
            return

        if not isinstance(value, HwAttributeDef):
            raise TypeError(
                f"hwAttributeDef must be HwAttributeDef or None, got {type(value).__name__}"
            )
        self._hwAttributeDef = value
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

    def with_hw_attribute(self, value):
        """
        Set hw_attribute and return self for chaining.

        Args:
            value: The hw_attribute to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hw_attribute("value")
        """
        self.hw_attribute = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAnnotation(self) -> Annotation:
        """
        AUTOSAR-compliant getter for annotation.

        Returns:
            The annotation value

        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def setAnnotation(self, value: Annotation) -> HwAttributeValue:
        """
        AUTOSAR-compliant setter for annotation with method chaining.

        Args:
            value: The annotation to set

        Returns:
            self for method chaining

        Note:
            Delegates to annotation property setter (gets validation automatically)
        """
        self.annotation = value  # Delegates to property setter
        return self

    def getHwAttributeDef(self) -> HwAttributeDef:
        """
        AUTOSAR-compliant getter for hwAttributeDef.

        Returns:
            The hwAttributeDef value

        Note:
            Delegates to hw_attribute_def property (CODING_RULE_V2_00017)
        """
        return self.hw_attribute_def  # Delegates to property

    def setHwAttributeDef(self, value: HwAttributeDef) -> HwAttributeValue:
        """
        AUTOSAR-compliant setter for hwAttributeDef with method chaining.

        Args:
            value: The hwAttributeDef to set

        Returns:
            self for method chaining

        Note:
            Delegates to hw_attribute_def property setter (gets validation automatically)
        """
        self.hw_attribute_def = value  # Delegates to property setter
        return self

    def getV(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for v.

        Returns:
            The v value

        Note:
            Delegates to v property (CODING_RULE_V2_00017)
        """
        return self.v  # Delegates to property

    def setV(self, value: "Numerical") -> HwAttributeValue:
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

    def getVt(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for vt.

        Returns:
            The vt value

        Note:
            Delegates to vt property (CODING_RULE_V2_00017)
        """
        return self.vt  # Delegates to property

    def setVt(self, value: "VerbatimString") -> HwAttributeValue:
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

    def with_annotation(self, value: Optional[Annotation]) -> HwAttributeValue:
        """
        Set annotation and return self for chaining.

        Args:
            value: The annotation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_annotation("value")
        """
        self.annotation = value  # Use property setter (gets validation)
        return self

    def with_hw_attribute_def(self, value: Optional[HwAttributeDef]) -> HwAttributeValue:
        """
        Set hwAttributeDef and return self for chaining.

        Args:
            value: The hwAttributeDef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hw_attribute_def("value")
        """
        self.hw_attribute_def = value  # Use property setter (gets validation)
        return self

    def with_v(self, value: Optional["Numerical"]) -> HwAttributeValue:
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

    def with_vt(self, value: Optional["VerbatimString"]) -> HwAttributeValue:
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



class HwType(HwDescriptionEntity):
    """
    This represents the ability to describe Hardware types on an abstract level.
    The particular types of hardware are distinguished by the category. This
    category determines the applicable attributes. The possible categories and
    attributes are defined in HwCategory.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory::HwType

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 17, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 991, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class HwCategory(ARElement):
    """
    This metaclass represents the ability to declare hardware categories and its
    particular attributes.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory::HwCategory

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 24, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation describes particular hardware attribute.
        self._hwAttributeDef: List[HwAttributeDef] = []

    @property
    def hw_attribute_def(self) -> List[HwAttributeDef]:
        """Get hwAttributeDef (Pythonic accessor)."""
        return self._hwAttributeDef

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwAttributeDef(self) -> List[HwAttributeDef]:
        """
        AUTOSAR-compliant getter for hwAttributeDef.

        Returns:
            The hwAttributeDef value

        Note:
            Delegates to hw_attribute_def property (CODING_RULE_V2_00017)
        """
        return self.hw_attribute_def  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class HwAttributeDef(Identifiable):
    """
    This metaclass represents the ability to define a particular hardware
    attribute. The category of this element defines the type of the
    attributeValue. If the category is Enumeration the hw
    AttributeEnumerationLiterals specify the available literals.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory::HwAttributeDef

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 26, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The available EnumerationLiterals of the Enumeration Only applicable if the
        # category of the Hw Enumeration.
        self._hwAttribute: List[HwAttributeLiteralDef] = []

    @property
    def hw_attribute(self) -> List[HwAttributeLiteralDef]:
        """Get hwAttribute (Pythonic accessor)."""
        return self._hwAttribute
        # This attribute specifies if the defined attribute value is be provided.
        self._isRequired: Optional[Boolean] = None

    @property
    def is_required(self) -> Optional[Boolean]:
        """Get isRequired (Pythonic accessor)."""
        return self._isRequired

    @is_required.setter
    def is_required(self, value: Optional[Boolean]) -> None:
        """
        Set isRequired with validation.

        Args:
            value: The isRequired to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isRequired = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isRequired must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isRequired = value
        # due to the fact that textual attributes.
        self._unit: Optional[Unit] = None

    @property
    def unit(self) -> Optional[Unit]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional[Unit]) -> None:
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

    def getHwAttribute(self) -> List[HwAttributeLiteralDef]:
        """
        AUTOSAR-compliant getter for hwAttribute.

        Returns:
            The hwAttribute value

        Note:
            Delegates to hw_attribute property (CODING_RULE_V2_00017)
        """
        return self.hw_attribute  # Delegates to property

    def getIsRequired(self) -> Boolean:
        """
        AUTOSAR-compliant getter for isRequired.

        Returns:
            The isRequired value

        Note:
            Delegates to is_required property (CODING_RULE_V2_00017)
        """
        return self.is_required  # Delegates to property

    def setIsRequired(self, value: Boolean) -> HwAttributeDef:
        """
        AUTOSAR-compliant setter for isRequired with method chaining.

        Args:
            value: The isRequired to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_required property setter (gets validation automatically)
        """
        self.is_required = value  # Delegates to property setter
        return self

    def getUnit(self) -> Unit:
        """
        AUTOSAR-compliant getter for unit.

        Returns:
            The unit value

        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: Unit) -> HwAttributeDef:
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

    def with_is_required(self, value: Optional[Boolean]) -> HwAttributeDef:
        """
        Set isRequired and return self for chaining.

        Args:
            value: The isRequired to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_required("value")
        """
        self.is_required = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional[Unit]) -> HwAttributeDef:
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



class HwAttributeLiteralDef(Identifiable):
    """
    One available EnumerationLiteral of the Enumeration definition. Only
    applicable if the category of the Hw AttributeDef equals Enumeration.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory::HwAttributeLiteralDef

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 26, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
