from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SlOverviewParagraph(ARObject):
    """
    MixedContentForOverviewParagraph in one particular language. The language is
    defined by the context. The attribute l is there only for backwards
    compatibility and shall be ignored.
    
    Package: M2::MSR::Documentation::TextModel::SingleLanguageData::SlOverviewParagraph
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 464, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====