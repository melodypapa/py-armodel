from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class EcucIndexableValue(ARObject, ABC):
    """
    Used to support the specification of ordering of parameter values.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucIndexableValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 110, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucIndexableValue:
            raise TypeError("EcucIndexableValue is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Used to support the specification of ordering of parameter.
        self._index: Optional["PositiveInteger"] = None

    @property
    def index(self) -> Optional["PositiveInteger"]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set index with validation.

        Args:
            value: The index to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._index = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"index must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._index = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIndex(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: "PositiveInteger") -> "EcucIndexableValue":
        """
        AUTOSAR-compliant setter for index with method chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Note:
            Delegates to index property setter (gets validation automatically)
        """
        self.index = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_index(self, value: Optional["PositiveInteger"]) -> "EcucIndexableValue":
        """
        Set index and return self for chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index("value")
        """
        self.index = value  # Use property setter (gets validation)
        return self
