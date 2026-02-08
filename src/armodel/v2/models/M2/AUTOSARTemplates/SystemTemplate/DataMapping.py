from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import DocumentationBlock
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DataMapping(ARObject, ABC):
    """
    Mapping of port elements (data elements and parameters) to frames and
    signals.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::DataMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 981, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 217, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DataMapping:
            raise TypeError("DataMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents introductory documentation about the.
        self._introduction: Optional["DocumentationBlock"] = None

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set introduction with validation.

        Args:
            value: The introduction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "DataMapping":
        """
        AUTOSAR-compliant setter for introduction with method chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "DataMapping":
        """
        Set introduction and return self for chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self
