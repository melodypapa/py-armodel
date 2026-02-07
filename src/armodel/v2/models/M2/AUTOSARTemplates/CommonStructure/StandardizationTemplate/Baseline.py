from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class Baseline(ARObject):
    """
    Specification of the baseline of the AUTOSAR standard this Data Exchange
    Point relates to. The baseline is specified by listing the AUTOSAR products
    and their revisions. Custom defined functionality and deviations to the
    standard can be provided as well. All references to specification elements
    in this Data Exchange Point refer to specification elements that are part of
    this specification baseline.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Baseline

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 79, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to custom SdgDefs that extend the data format baseline,.
        self._customSdgDef: List["SdgDef"] = []

    @property
    def custom_sdg_def(self) -> List["SdgDef"]:
        """Get customSdgDef (Pythonic accessor)."""
        return self._customSdgDef
        # Reference to custom specifications that extend this.
        self._custom: List["Documentation"] = []

    @property
    def custom(self) -> List["Documentation"]:
        """Get custom (Pythonic accessor)."""
        return self._custom
        # Specifies a combination of revisions of AUTOSAR that are used as the
                # specification baseline of Exchange Point.
        # All standard specification are referenced by this Profile of Data have to be
                # part of specifications that the defined AUTOSAR standards.
        self._standard: List["String"] = []

    @property
    def standard(self) -> List["String"]:
        """Get standard (Pythonic accessor)."""
        return self._standard

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustomSdgDef(self) -> List["SdgDef"]:
        """
        AUTOSAR-compliant getter for customSdgDef.

        Returns:
            The customSdgDef value

        Note:
            Delegates to custom_sdg_def property (CODING_RULE_V2_00017)
        """
        return self.custom_sdg_def  # Delegates to property

    def getCustom(self) -> List["Documentation"]:
        """
        AUTOSAR-compliant getter for custom.

        Returns:
            The custom value

        Note:
            Delegates to custom property (CODING_RULE_V2_00017)
        """
        return self.custom  # Delegates to property

    def getStandard(self) -> List["String"]:
        """
        AUTOSAR-compliant getter for standard.

        Returns:
            The standard value

        Note:
            Delegates to standard property (CODING_RULE_V2_00017)
        """
        return self.standard  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
