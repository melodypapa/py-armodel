from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import PerInstanceMemory
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class PerInstanceMemorySize(ARObject):
    """
    Resources needed by the allocation of PerInstanceMemory for each SWC
    instance. Note that these resources are not covered by an ObjectFileSection,
    because they are supposed to be allocated by the RTE.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcImplementation::PerInstanceMemorySize

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 623, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Required alignment (1,2,4,.
        # ) of the referenced Per byte.
        self._alignment: Optional["PositiveInteger"] = None

    @property
    def alignment(self) -> Optional["PositiveInteger"]:
        """Get alignment (Pythonic accessor)."""
        return self._alignment

    @alignment.setter
    def alignment(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set alignment with validation.

        Args:
            value: The alignment to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._alignment = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"alignment must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._alignment = value
        # This represents the referenced PerInstanceMemory.
        self._perInstanceMemory: Optional["PerInstanceMemory"] = None

    @property
    def per_instance_memory(self) -> Optional["PerInstanceMemory"]:
        """Get perInstanceMemory (Pythonic accessor)."""
        return self._perInstanceMemory

    @per_instance_memory.setter
    def per_instance_memory(self, value: Optional["PerInstanceMemory"]) -> None:
        """
        Set perInstanceMemory with validation.

        Args:
            value: The perInstanceMemory to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._perInstanceMemory = None
            return

        if not isinstance(value, PerInstanceMemory):
            raise TypeError(
                f"perInstanceMemory must be PerInstanceMemory or None, got {type(value).__name__}"
            )
        self._perInstanceMemory = value
        # Size (in bytes) of the reference perInstanceMemory.
        # The PerInstanceMemorySize is subject to the purpose to support variability in
                # the implementations.
        # Different the implementation might require a different.
        self._size: Optional["PositiveInteger"] = None

    @property
    def size(self) -> Optional["PositiveInteger"]:
        """Get size (Pythonic accessor)."""
        return self._size

    @size.setter
    def size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set size with validation.

        Args:
            value: The size to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._size = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"size must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._size = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlignment(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for alignment.

        Returns:
            The alignment value

        Note:
            Delegates to alignment property (CODING_RULE_V2_00017)
        """
        return self.alignment  # Delegates to property

    def setAlignment(self, value: "PositiveInteger") -> "PerInstanceMemorySize":
        """
        AUTOSAR-compliant setter for alignment with method chaining.

        Args:
            value: The alignment to set

        Returns:
            self for method chaining

        Note:
            Delegates to alignment property setter (gets validation automatically)
        """
        self.alignment = value  # Delegates to property setter
        return self

    def getPerInstanceMemory(self) -> "PerInstanceMemory":
        """
        AUTOSAR-compliant getter for perInstanceMemory.

        Returns:
            The perInstanceMemory value

        Note:
            Delegates to per_instance_memory property (CODING_RULE_V2_00017)
        """
        return self.per_instance_memory  # Delegates to property

    def setPerInstanceMemory(self, value: "PerInstanceMemory") -> "PerInstanceMemorySize":
        """
        AUTOSAR-compliant setter for perInstanceMemory with method chaining.

        Args:
            value: The perInstanceMemory to set

        Returns:
            self for method chaining

        Note:
            Delegates to per_instance_memory property setter (gets validation automatically)
        """
        self.per_instance_memory = value  # Delegates to property setter
        return self

    def getSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for size.

        Returns:
            The size value

        Note:
            Delegates to size property (CODING_RULE_V2_00017)
        """
        return self.size  # Delegates to property

    def setSize(self, value: "PositiveInteger") -> "PerInstanceMemorySize":
        """
        AUTOSAR-compliant setter for size with method chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Note:
            Delegates to size property setter (gets validation automatically)
        """
        self.size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alignment(self, value: Optional["PositiveInteger"]) -> "PerInstanceMemorySize":
        """
        Set alignment and return self for chaining.

        Args:
            value: The alignment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_alignment("value")
        """
        self.alignment = value  # Use property setter (gets validation)
        return self

    def with_per_instance_memory(self, value: Optional["PerInstanceMemory"]) -> "PerInstanceMemorySize":
        """
        Set perInstanceMemory and return self for chaining.

        Args:
            value: The perInstanceMemory to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_per_instance_memory("value")
        """
        self.per_instance_memory = value  # Use property setter (gets validation)
        return self

    def with_size(self, value: Optional["PositiveInteger"]) -> "PerInstanceMemorySize":
        """
        Set size and return self for chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_size("value")
        """
        self.size = value  # Use property setter (gets validation)
        return self
