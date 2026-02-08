"""
V2 M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint package.
"""

# Classes:
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Baseline import (
    Baseline,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint import (
    DataExchangePoint,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common import (
    DataFormatElementReference,
    RestrictionWithSeverity,
    SpecElementReference,
    SpecElementScope,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data import (
    AbstractClassTailoring,
    AbstractCondition,
    AggregationCondition,
    AggregationTailoring,
    AttributeCondition,
    AttributeTailoring,
    ClassContentConditional,
    ClassTailoring,
    ConcreteClassTailoring,
    ConstraintTailoring,
    DataFormatElementScope,
    DataFormatTailoring,
    DefaultValueApplicationStrategyEnum,
    InvertCondition,
    MultiplicityRestrictionWithSeverity,
    PrimitiveAttributeCondition,
    PrimitiveAttributeTailoring,
    ReferenceCondition,
    ReferenceTailoring,
    SdgTailoring,
    TextualCondition,
    UnresolvedReferenceRestrictionWithSeverity,
    ValueRestrictionWithSeverity,
    VariationRestrictionWithSeverity,
)

__all__ = [
    # .Common.*,
    # .Data.*,
    "Baseline",
    "DataExchangePoint",
    "DataExchangePointKind",
    "SeverityEnum",
]
