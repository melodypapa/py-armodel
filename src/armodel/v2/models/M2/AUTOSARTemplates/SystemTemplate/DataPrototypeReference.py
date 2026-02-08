from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DataPrototypeReference(ARObject, ABC):
    """
    This meta-class provides the ability to reference a DataPrototype.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::DataPrototypeReference

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 787, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DataPrototypeReference:
            raise TypeError("DataPrototypeReference is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the ability to specify a tag-id for of a specific
        # DataPrototype in the context (potentially deeply-nested) composite data
        # structure.
        self._tagId: Optional["PositiveInteger"] = None

    @property
    def tag_id(self) -> Optional["PositiveInteger"]:
        """Get tagId (Pythonic accessor)."""
        return self._tagId

    @tag_id.setter
    def tag_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tagId with validation.

        Args:
            value: The tagId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tagId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tagId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tagId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTagId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tagId.

        Returns:
            The tagId value

        Note:
            Delegates to tag_id property (CODING_RULE_V2_00017)
        """
        return self.tag_id  # Delegates to property

    def setTagId(self, value: "PositiveInteger") -> "DataPrototypeReference":
        """
        AUTOSAR-compliant setter for tagId with method chaining.

        Args:
            value: The tagId to set

        Returns:
            self for method chaining

        Note:
            Delegates to tag_id property setter (gets validation automatically)
        """
        self.tag_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tag_id(self, value: Optional["PositiveInteger"]) -> "DataPrototypeReference":
        """
        Set tagId and return self for chaining.

        Args:
            value: The tagId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tag_id("value")
        """
        self.tag_id = value  # Use property setter (gets validation)
        return self
