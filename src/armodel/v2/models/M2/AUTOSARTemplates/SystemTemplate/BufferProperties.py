from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import Integer
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class BufferProperties(ARObject):
    """
    Configuration of the buffer properties the transformer needs to work.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::BufferProperties

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 199, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 767, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the length of the header (in bits) this transformer in front of the
        # data.
        self._headerLength: Optional["Integer"] = None

    @property
    def header_length(self) -> Optional["Integer"]:
        """Get headerLength (Pythonic accessor)."""
        return self._headerLength

    @header_length.setter
    def header_length(self, value: Optional["Integer"]) -> None:
        """
        Set headerLength with validation.

        Args:
            value: The headerLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerLength = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"headerLength must be Integer or None, got {type(value).__name__}"
            )
        self._headerLength = value
        # If set, the transformer uses the input buffer as output.
        self._inPlace: Optional["Boolean"] = None

    @property
    def in_place(self) -> Optional["Boolean"]:
        """Get inPlace (Pythonic accessor)."""
        return self._inPlace

    @in_place.setter
    def in_place(self, value: Optional["Boolean"]) -> None:
        """
        Set inPlace with validation.

        Args:
            value: The inPlace to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inPlace = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"inPlace must be Boolean or None, got {type(value).__name__}"
            )
        self._inPlace = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHeaderLength(self) -> "Integer":
        """
        AUTOSAR-compliant getter for headerLength.

        Returns:
            The headerLength value

        Note:
            Delegates to header_length property (CODING_RULE_V2_00017)
        """
        return self.header_length  # Delegates to property

    def setHeaderLength(self, value: "Integer") -> "BufferProperties":
        """
        AUTOSAR-compliant setter for headerLength with method chaining.

        Args:
            value: The headerLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to header_length property setter (gets validation automatically)
        """
        self.header_length = value  # Delegates to property setter
        return self

    def getInPlace(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for inPlace.

        Returns:
            The inPlace value

        Note:
            Delegates to in_place property (CODING_RULE_V2_00017)
        """
        return self.in_place  # Delegates to property

    def setInPlace(self, value: "Boolean") -> "BufferProperties":
        """
        AUTOSAR-compliant setter for inPlace with method chaining.

        Args:
            value: The inPlace to set

        Returns:
            self for method chaining

        Note:
            Delegates to in_place property setter (gets validation automatically)
        """
        self.in_place = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_header_length(self, value: Optional["Integer"]) -> "BufferProperties":
        """
        Set headerLength and return self for chaining.

        Args:
            value: The headerLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_header_length("value")
        """
        self.header_length = value  # Use property setter (gets validation)
        return self

    def with_in_place(self, value: Optional["Boolean"]) -> "BufferProperties":
        """
        Set inPlace and return self for chaining.

        Args:
            value: The inPlace to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_in_place("value")
        """
        self.in_place = value  # Use property setter (gets validation)
        return self
