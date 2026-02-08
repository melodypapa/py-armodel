from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class AdminData(ARObject):
    """
    that information about previous revisions can also be logged here. The
    entries shall be sorted descendant by date in order to reflect the history.
    Therefore the most recent entry representing the current version is denoted
    first. language LEnum 0..1 attr This attribute specifies the master language
    of the document or the document fragment. The master language is the one in
    which the document is maintained and from which the other languages are
    derived from. In particular in case of inconsistencies, the information in
    the master language is priority. sdg Sdg * aggr This property allows to keep
    special data which is not represented by the standard model. It can be
    utilized to keep e.g. tool specific data. Stereotypes: atpSplitable (cid:53)
    288 of 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration Specification of
    ECU Configuration AUTOSAR CP R23-11 (cid:52)

    Package: M2::MSR::AsamHdo::AdminData::AdminData

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 288, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 969, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1994, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 72, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 84, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This allows to denote information about the current of the object.
        self._docRevision: List["DocRevision"] = []

    @property
    def doc_revision(self) -> List["DocRevision"]:
        """Get docRevision (Pythonic accessor)."""
        return self._docRevision
        # This property specifies the languages which are provided document.
        # Therefore it should only be specified in level admin data.
        # For each language provided in there is one entry in MultilanguagePlain
                # content of each entry can be used for the language.
        # The used language itself the language attribute in the entry.
        self._usedLanguages: Optional["MultiLanguagePlainText"] = None

    @property
    def used_languages(self) -> Optional["MultiLanguagePlainText"]:
        """Get usedLanguages (Pythonic accessor)."""
        return self._usedLanguages

    @used_languages.setter
    def used_languages(self, value: Optional["MultiLanguagePlainText"]) -> None:
        """
        Set usedLanguages with validation.

        Args:
            value: The usedLanguages to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usedLanguages = None
            return

        if not isinstance(value, MultiLanguagePlainText):
            raise TypeError(
                f"usedLanguages must be MultiLanguagePlainText or None, got {type(value).__name__}"
            )
        self._usedLanguages = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDocRevision(self) -> List["DocRevision"]:
        """
        AUTOSAR-compliant getter for docRevision.

        Returns:
            The docRevision value

        Note:
            Delegates to doc_revision property (CODING_RULE_V2_00017)
        """
        return self.doc_revision  # Delegates to property

    def getUsedLanguages(self) -> "MultiLanguagePlainText":
        """
        AUTOSAR-compliant getter for usedLanguages.

        Returns:
            The usedLanguages value

        Note:
            Delegates to used_languages property (CODING_RULE_V2_00017)
        """
        return self.used_languages  # Delegates to property

    def setUsedLanguages(self, value: "MultiLanguagePlainText") -> "AdminData":
        """
        AUTOSAR-compliant setter for usedLanguages with method chaining.

        Args:
            value: The usedLanguages to set

        Returns:
            self for method chaining

        Note:
            Delegates to used_languages property setter (gets validation automatically)
        """
        self.used_languages = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_used_languages(self, value: Optional["MultiLanguagePlainText"]) -> "AdminData":
        """
        Set usedLanguages and return self for chaining.

        Args:
            value: The usedLanguages to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_used_languages("value")
        """
        self.used_languages = value  # Use property setter (gets validation)
        return self
