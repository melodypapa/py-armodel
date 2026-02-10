"""
AUTOSAR Package - Annotation

Package: M2::MSR::Documentation::Annotation
"""

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation import (
    GeneralAnnotation,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.MlFigure import (
    MlFigure,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.MlFormula import (
    MlFormula,
)
from armodel.v2.models.M2.MSR.Documentation.MsrQueryP2 import (
    MsrQueryP2,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.MultiLanguageVerbatim import (
    MultiLanguageVerbatim,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.Note import (
    Note,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.StructuredReq import (
    StructuredReq,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.TraceableText import (
    TraceableText,
)


class Annotation(GeneralAnnotation):
    """
    This is a plain annotation which does not have further formal data.
    
    Package: M2::MSR::Documentation::Annotation::Annotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 334, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 163, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
