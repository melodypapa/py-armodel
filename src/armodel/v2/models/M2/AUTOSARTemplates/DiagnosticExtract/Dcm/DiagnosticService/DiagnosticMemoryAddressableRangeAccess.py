from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticMemory,
    DiagnosticMemoryByAddress,
)


class DiagnosticMemoryAddressableRangeAccess(DiagnosticMemoryByAddress, ABC):
    """
    This abstract base class

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticMemoryAddressableRangeAccess

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 140, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticMemoryAddressableRangeAccess:
            raise TypeError("DiagnosticMemoryAddressableRangeAccess is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the formal description of the memory to which the
        # DiagnosticMemoryByAddress.
        self._memoryRange: List["DiagnosticMemory"] = []

    @property
    def memory_range(self) -> List["DiagnosticMemory"]:
        """Get memoryRange (Pythonic accessor)."""
        return self._memoryRange

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMemoryRange(self) -> List["DiagnosticMemory"]:
        """
        AUTOSAR-compliant getter for memoryRange.

        Returns:
            The memoryRange value

        Note:
            Delegates to memory_range property (CODING_RULE_V2_00017)
        """
        return self.memory_range  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
