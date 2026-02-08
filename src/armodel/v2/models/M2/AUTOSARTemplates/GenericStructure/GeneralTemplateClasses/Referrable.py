from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import ShortNameFragment
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class Referrable(ARObject, ABC):
    """
    Instances of this class can be referred to by their identifier (while
    adhering to namespace borders).

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::Referrable

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 328, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 328, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 305, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 63, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1002, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2049, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 238, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (Page 31, Foundation R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 49, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 78, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 63, Foundation R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 33, Foundation R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 66, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 202, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is Referrable:
            raise TypeError("Referrable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies how the Referrable.
        # shortName is of several shortNameFragments.
        self._shortName: List["ShortNameFragment"] = []

    @property
    def short_name(self) -> List["ShortNameFragment"]:
        """Get shortName (Pythonic accessor)."""
        return self._shortName

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getShortName(self) -> List["ShortNameFragment"]:
        """
        AUTOSAR-compliant getter for shortName.

        Returns:
            The shortName value

        Note:
            Delegates to short_name property (CODING_RULE_V2_00017)
        """
        return self.short_name  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
