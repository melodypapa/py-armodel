from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import NameToken
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SdgElementWithGid(ARObject, ABC):
    """
    A special data group element with gid is an abstract element that shall have
    a name (gid, "Generic Identifier").

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgElementWithGid

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 99, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SdgElementWithGid:
            raise TypeError("SdgElementWithGid is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the name that identifies the element.
        self._gid: Optional["NameToken"] = None

    @property
    def gid(self) -> Optional["NameToken"]:
        """Get gid (Pythonic accessor)."""
        return self._gid

    @gid.setter
    def gid(self, value: Optional["NameToken"]) -> None:
        """
        Set gid with validation.

        Args:
            value: The gid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._gid = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"gid must be NameToken or None, got {type(value).__name__}"
            )
        self._gid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGid(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for gid.

        Returns:
            The gid value

        Note:
            Delegates to gid property (CODING_RULE_V2_00017)
        """
        return self.gid  # Delegates to property

    def setGid(self, value: "NameToken") -> "SdgElementWithGid":
        """
        AUTOSAR-compliant setter for gid with method chaining.

        Args:
            value: The gid to set

        Returns:
            self for method chaining

        Note:
            Delegates to gid property setter (gets validation automatically)
        """
        self.gid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_gid(self, value: Optional["NameToken"]) -> "SdgElementWithGid":
        """
        Set gid and return self for chaining.

        Args:
            value: The gid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_gid("value")
        """
        self.gid = value  # Use property setter (gets validation)
        return self
