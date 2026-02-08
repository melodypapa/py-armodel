from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class MsrQueryResultTopic1(ARObject):
    """
    This metaclass represents the ability to express the result of a query which
    is a set of topics.

    Package: M2::MSR::Documentation::MsrQuery::MsrQueryResultTopic1

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 345, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
