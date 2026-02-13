"""
AUTOSAR Package - TagWithOptionalValue

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::TagWithOptionalValue
"""


from __future__ import annotations
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TagWithOptionalValue(ARObject):
    """
    A tagged value is a combination of a tag (key) and a value that gives
    supplementary information that is attached to a model element. Please note
    that keys without a value are allowed.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::TagWithOptionalValue::TagWithOptionalValue

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 477, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 166, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines a key.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._key: Optional[String] = None

    @property
    def key(self) -> Optional[String]:
        """Get key (Pythonic accessor)."""
        return self._key

    @key.setter
    def key(self, value: Optional[String]) -> None:
        """
        Set key with validation.

        Args:
            value: The key to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._key = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"key must be String or str or None, got {type(value).__name__}"
            )
        self._key = value
                # splitable.
        # If define the same value of attribute the order in which the value collection
                # is merged significant.
        # As an example consider the the $PATH environment variable by means of class
                # TagWithOptionalValue.
        # The sequenceOffset relative position of each contribution in the The
                # contributions are sorted in order.
        self._sequenceOffset: Optional[Integer] = None

    @property
    def sequence_offset(self) -> Optional[Integer]:
        """Get sequenceOffset (Pythonic accessor)."""
        return self._sequenceOffset

    @sequence_offset.setter
    def sequence_offset(self, value: Optional[Integer]) -> None:
        """
        Set sequenceOffset with validation.

        Args:
            value: The sequenceOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sequenceOffset = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"sequenceOffset must be Integer or int or None, got {type(value).__name__}"
            )
        self._sequenceOffset = value
        self._value: Optional[String] = None

    @property
    def value(self) -> Optional[String]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"value must be String or str or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getKey(self) -> String:
        """
        AUTOSAR-compliant getter for key.

        Returns:
            The key value

        Note:
            Delegates to key property (CODING_RULE_V2_00017)
        """
        return self.key  # Delegates to property

    def setKey(self, value: String) -> TagWithOptionalValue:
        """
        AUTOSAR-compliant setter for key with method chaining.

        Args:
            value: The key to set

        Returns:
            self for method chaining

        Note:
            Delegates to key property setter (gets validation automatically)
        """
        self.key = value  # Delegates to property setter
        return self

    def getSequenceOffset(self) -> Integer:
        """
        AUTOSAR-compliant getter for sequenceOffset.

        Returns:
            The sequenceOffset value

        Note:
            Delegates to sequence_offset property (CODING_RULE_V2_00017)
        """
        return self.sequence_offset  # Delegates to property

    def setSequenceOffset(self, value: Integer) -> TagWithOptionalValue:
        """
        AUTOSAR-compliant setter for sequenceOffset with method chaining.

        Args:
            value: The sequenceOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to sequence_offset property setter (gets validation automatically)
        """
        self.sequence_offset = value  # Delegates to property setter
        return self

    def getValue(self) -> String:
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: String) -> TagWithOptionalValue:
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

    def with_key(self, value: Optional[String]) -> TagWithOptionalValue:
        """
        Set key and return self for chaining.

        Args:
            value: The key to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key("value")
        """
        self.key = value  # Use property setter (gets validation)
        return self

    def with_sequence_offset(self, value: Optional[Integer]) -> TagWithOptionalValue:
        """
        Set sequenceOffset and return self for chaining.

        Args:
            value: The sequenceOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sequence_offset("value")
        """
        self.sequence_offset = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional[String]) -> TagWithOptionalValue:
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
