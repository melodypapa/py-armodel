"""
AUTOSAR Package - SingleLanguageData

Package: M2::MSR::Documentation::TextModel::SingleLanguageData
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)




class SingleLanguageUnitNames(ARObject):
    """
    This represents the ability to express a display name.
    
    Package: M2::MSR::Documentation::TextModel::SingleLanguageData::SingleLanguageUnitNames
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 400, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SingleLanguageLongName(ARObject):
    """
    SingleLanguageLongName
    
    Package: M2::MSR::Documentation::TextModel::SingleLanguageData::SingleLanguageLongName
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



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



class SlParagraph(ARObject):
    """
    This is the text for a paragraph in one particular language. The language is
    defined by the context. The attribute l is there only for backwards
    compatibility and shall be ignored.
    
    Package: M2::MSR::Documentation::TextModel::SingleLanguageData::SlParagraph
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 465, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====