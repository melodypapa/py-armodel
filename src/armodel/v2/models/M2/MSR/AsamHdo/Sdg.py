from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class Sdg(ARObject):
    """
    Sdg (SpecialDataGroup) is a generic model which can be used to keep
    arbitrary information which is not explicitly modeled in the meta-model. Sdg
    can have various contents as defined by sdgContentsType. Special Data should
    only be used moderately since all elements should be defined in the
    meta-model. Thereby SDG should be considered as a temporary solution when no
    explicit model is available. If an sdg Caption is available, it is possible
    to establish a reference to the sdg structure.

    Package: M2::MSR::AsamHdo::SpecialData::Sdg

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 328, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1004, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 78, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 90, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes specifies an identifier.
        # Gid comes from the Identifier" which is the in XML.
        # The role of this attribute is the the name of an XML - element.
        self._gid: "NameToken" = None

    @property
    def gid(self) -> "NameToken":
        """Get gid (Pythonic accessor)."""
        return self._gid

    @gid.setter
    def gid(self, value: "NameToken") -> None:
        """
        Set gid with validation.

        Args:
            value: The gid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NameToken):
            raise TypeError(
                f"gid must be NameToken, got {type(value).__name__}"
            )
        self._gid = value
        # This aggregation allows to assign the properties of the sdg.
        # By this, a shortName etc.
        # can be the Sdg.
        self._sdgCaption: Optional["SdgCaption"] = None

    @property
    def sdg_caption(self) -> Optional["SdgCaption"]:
        """Get sdgCaption (Pythonic accessor)."""
        return self._sdgCaption

    @sdg_caption.setter
    def sdg_caption(self, value: Optional["SdgCaption"]) -> None:
        """
        Set sdgCaption with validation.

        Args:
            value: The sdgCaption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdgCaption = None
            return

        if not isinstance(value, SdgCaption):
            raise TypeError(
                f"sdgCaption must be SdgCaption or None, got {type(value).__name__}"
            )
        self._sdgCaption = value
        # This is the content of the Sdg.
        self._sdgContents: Optional["SdgContents"] = None

    @property
    def sdg_contents(self) -> Optional["SdgContents"]:
        """Get sdgContents (Pythonic accessor)."""
        return self._sdgContents

    @sdg_contents.setter
    def sdg_contents(self, value: Optional["SdgContents"]) -> None:
        """
        Set sdgContents with validation.

        Args:
            value: The sdgContents to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdgContents = None
            return

        if not isinstance(value, SdgContents):
            raise TypeError(
                f"sdgContents must be SdgContents or None, got {type(value).__name__}"
            )
        self._sdgContents = value

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

    def setGid(self, value: "NameToken") -> "Sdg":
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

    def getSdgCaption(self) -> "SdgCaption":
        """
        AUTOSAR-compliant getter for sdgCaption.

        Returns:
            The sdgCaption value

        Note:
            Delegates to sdg_caption property (CODING_RULE_V2_00017)
        """
        return self.sdg_caption  # Delegates to property

    def setSdgCaption(self, value: "SdgCaption") -> "Sdg":
        """
        AUTOSAR-compliant setter for sdgCaption with method chaining.

        Args:
            value: The sdgCaption to set

        Returns:
            self for method chaining

        Note:
            Delegates to sdg_caption property setter (gets validation automatically)
        """
        self.sdg_caption = value  # Delegates to property setter
        return self

    def getSdgContents(self) -> "SdgContents":
        """
        AUTOSAR-compliant getter for sdgContents.

        Returns:
            The sdgContents value

        Note:
            Delegates to sdg_contents property (CODING_RULE_V2_00017)
        """
        return self.sdg_contents  # Delegates to property

    def setSdgContents(self, value: "SdgContents") -> "Sdg":
        """
        AUTOSAR-compliant setter for sdgContents with method chaining.

        Args:
            value: The sdgContents to set

        Returns:
            self for method chaining

        Note:
            Delegates to sdg_contents property setter (gets validation automatically)
        """
        self.sdg_contents = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_gid(self, value: "NameToken") -> "Sdg":
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

    def with_sdg_caption(self, value: Optional["SdgCaption"]) -> "Sdg":
        """
        Set sdgCaption and return self for chaining.

        Args:
            value: The sdgCaption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdg_caption("value")
        """
        self.sdg_caption = value  # Use property setter (gets validation)
        return self

    def with_sdg_contents(self, value: Optional["SdgContents"]) -> "Sdg":
        """
        Set sdgContents and return self for chaining.

        Args:
            value: The sdgContents to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdg_contents("value")
        """
        self.sdg_contents = value  # Use property setter (gets validation)
        return self
