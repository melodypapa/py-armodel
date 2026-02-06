"""
AUTOSAR V2 Models - GenericStructure Module.

V2 Implementation:
- Absolute imports only (CODING_RULE_V2_00001)
- Explicit __all__ exports (CODING_RULE_V2_00003)
"""

# Leaf package files
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpClassifier,
    AtpFeature,
    AtpInstanceRef,
    AtpPrototype,
    AtpStructureElement,
    AtpType,
)

# Subdirectory packages
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import (
    Documentation,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import (
    LifeCycleInfo,
    LifeCycleInfoSet,
    LifeCyclePeriod,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AtpDefinition,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    PostBuildVariantCriterion,
    PostBuildVariantCriterionValue,
    PredefinedVariant,
    SwSystemconstantValueSet,
    VariationPoint,
)

__all__ = [
    "AtpClassifier",
    "AtpDefinition",
    "AtpFeature",
    "AtpInstanceRef",
    "AtpPrototype",
    "AtpStructureElement",
    "AtpType",
    "Documentation",
    "LifeCycleInfo",
    "LifeCycleInfoSet",
    "LifeCyclePeriod",
    "PostBuildVariantCriterion",
    "PostBuildVariantCriterionValue",
    "PredefinedVariant",
    "SwSystemconstantValueSet",
    "VariationPoint",
]
