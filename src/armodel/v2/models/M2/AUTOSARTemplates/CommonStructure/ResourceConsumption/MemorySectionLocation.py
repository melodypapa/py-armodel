from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class MemorySectionLocation(ARObject):
    """
    Specifies in which hardware ProvidedMemorySegment the softwareMemorySection
    is located.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 162, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the hardware ProvidedMemorySegment.
        self._providedMemory: Optional["HwElement"] = None

    @property
    def provided_memory(self) -> Optional["HwElement"]:
        """Get providedMemory (Pythonic accessor)."""
        return self._providedMemory

    @provided_memory.setter
    def provided_memory(self, value: Optional["HwElement"]) -> None:
        """
        Set providedMemory with validation.

        Args:
            value: The providedMemory to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._providedMemory = None
            return

        if not isinstance(value, HwElement):
            raise TypeError(
                f"providedMemory must be HwElement or None, got {type(value).__name__}"
            )
        self._providedMemory = value
        # Reference to the MemorySection which is mapped on a hardware memory segment.
        self._software: Optional["MemorySection"] = None

    @property
    def software(self) -> Optional["MemorySection"]:
        """Get software (Pythonic accessor)."""
        return self._software

    @software.setter
    def software(self, value: Optional["MemorySection"]) -> None:
        """
        Set software with validation.

        Args:
            value: The software to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._software = None
            return

        if not isinstance(value, MemorySection):
            raise TypeError(
                f"software must be MemorySection or None, got {type(value).__name__}"
            )
        self._software = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvidedMemory(self) -> "HwElement":
        """
        AUTOSAR-compliant getter for providedMemory.

        Returns:
            The providedMemory value

        Note:
            Delegates to provided_memory property (CODING_RULE_V2_00017)
        """
        return self.provided_memory  # Delegates to property

    def setProvidedMemory(self, value: "HwElement") -> "MemorySectionLocation":
        """
        AUTOSAR-compliant setter for providedMemory with method chaining.

        Args:
            value: The providedMemory to set

        Returns:
            self for method chaining

        Note:
            Delegates to provided_memory property setter (gets validation automatically)
        """
        self.provided_memory = value  # Delegates to property setter
        return self

    def getSoftware(self) -> "MemorySection":
        """
        AUTOSAR-compliant getter for software.

        Returns:
            The software value

        Note:
            Delegates to software property (CODING_RULE_V2_00017)
        """
        return self.software  # Delegates to property

    def setSoftware(self, value: "MemorySection") -> "MemorySectionLocation":
        """
        AUTOSAR-compliant setter for software with method chaining.

        Args:
            value: The software to set

        Returns:
            self for method chaining

        Note:
            Delegates to software property setter (gets validation automatically)
        """
        self.software = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provided_memory(self, value: Optional["HwElement"]) -> "MemorySectionLocation":
        """
        Set providedMemory and return self for chaining.

        Args:
            value: The providedMemory to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided_memory("value")
        """
        self.provided_memory = value  # Use property setter (gets validation)
        return self

    def with_software(self, value: Optional["MemorySection"]) -> "MemorySectionLocation":
        """
        Set software and return self for chaining.

        Args:
            value: The software to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_software("value")
        """
        self.software = value  # Use property setter (gets validation)
        return self
