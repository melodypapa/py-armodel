from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
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
        self._annotation: Optional["Annotation"] = None

    @property
    def annotation(self) -> Optional["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation

    @annotation.setter
    def annotation(self, value: Optional["Annotation"]) -> None:
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
        # This association represents the definition of the particular value.
        self._hwAttributeDef: Optional["HwAttributeDef"] = None

    @property
    def hw_attribute_def(self) -> Optional["HwAttributeDef"]:
        """Get hwAttributeDef (Pythonic accessor)."""
        return self._hwAttributeDef

    @hw_attribute_def.setter
    def hw_attribute_def(self, value: Optional["HwAttributeDef"]) -> None:
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
        # This represents a numerical hardware attribute value.
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
        # This represents a textual hardware attribute value.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAnnotation(self) -> "Annotation":
        """
        AUTOSAR-compliant getter for annotation.

        Returns:
            The annotation value

        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def setAnnotation(self, value: "Annotation") -> "HwAttributeValue":
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

    def getHwAttributeDef(self) -> "HwAttributeDef":
        """
        AUTOSAR-compliant getter for hwAttributeDef.

        Returns:
            The hwAttributeDef value

        Note:
            Delegates to hw_attribute_def property (CODING_RULE_V2_00017)
        """
        return self.hw_attribute_def  # Delegates to property

    def setHwAttributeDef(self, value: "HwAttributeDef") -> "HwAttributeValue":
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

    def setV(self, value: "Numerical") -> "HwAttributeValue":
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

    def setVt(self, value: "VerbatimString") -> "HwAttributeValue":
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

    def with_annotation(self, value: Optional["Annotation"]) -> "HwAttributeValue":
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

    def with_hw_attribute_def(self, value: Optional["HwAttributeDef"]) -> "HwAttributeValue":
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

    def with_v(self, value: Optional["Numerical"]) -> "HwAttributeValue":
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

    def with_vt(self, value: Optional["VerbatimString"]) -> "HwAttributeValue":
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
