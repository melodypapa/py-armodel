from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef import (
    SdgAttribute,
)


class SdgReference(SdgAttribute):
    """
    Describes an attribute of a SdgClass which is used on the definition side to
    model a reference from one Sdg to another Sdg on the value side.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 101, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to a SdgClass which is used on the definition side the destination
                # type of the referenced Sdg.
        # On side the reference is realized by means of the defining an sdgx attribute
                # which refers to of the referenced Sdg.
        self._destSdg: Optional["SdgClass"] = None

    @property
    def dest_sdg(self) -> Optional["SdgClass"]:
        """Get destSdg (Pythonic accessor)."""
        return self._destSdg

    @dest_sdg.setter
    def dest_sdg(self, value: Optional["SdgClass"]) -> None:
        """
        Set destSdg with validation.

        Args:
            value: The destSdg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destSdg = None
            return

        if not isinstance(value, SdgClass):
            raise TypeError(
                f"destSdg must be SdgClass or None, got {type(value).__name__}"
            )
        self._destSdg = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestSdg(self) -> "SdgClass":
        """
        AUTOSAR-compliant getter for destSdg.

        Returns:
            The destSdg value

        Note:
            Delegates to dest_sdg property (CODING_RULE_V2_00017)
        """
        return self.dest_sdg  # Delegates to property

    def setDestSdg(self, value: "SdgClass") -> "SdgReference":
        """
        AUTOSAR-compliant setter for destSdg with method chaining.

        Args:
            value: The destSdg to set

        Returns:
            self for method chaining

        Note:
            Delegates to dest_sdg property setter (gets validation automatically)
        """
        self.dest_sdg = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dest_sdg(self, value: Optional["SdgClass"]) -> "SdgReference":
        """
        Set destSdg and return self for chaining.

        Args:
            value: The destSdg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dest_sdg("value")
        """
        self.dest_sdg = value  # Use property setter (gets validation)
        return self
