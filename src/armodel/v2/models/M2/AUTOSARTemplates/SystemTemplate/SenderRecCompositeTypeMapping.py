from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SenderRecCompositeTypeMapping(ARObject, ABC):
    """
    Two mappings exist for the composite data types: "ArrayTypeMapping" and
    "RecordTypeMapping". In both, a primitive datatype will be mapped to a
    system signal. But it is also possible to combine the arrays and the
    records, so that an "array" could be an element of a "record" and in the
    same manner a "record" could be an element of an "array". Nesting these data
    types is also possible. If an element of a composite data type is again a
    composite one, the "CompositeTypeMapping" element will be used one more time
    (aggregation between the ArrayElementMapping and CompositeType Mapping or
    aggregation between the RecordElementMapping and CompositeTypeMapping).

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderRecCompositeTypeMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 235, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is SenderRecCompositeTypeMapping:
            raise TypeError("SenderRecCompositeTypeMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
