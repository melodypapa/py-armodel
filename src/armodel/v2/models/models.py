"""
V2 Model Classes - Core AUTOSAR models (V2 base).

V2 Implementation:
- Imports classes from M2 package paths (correct AUTOSAR M2 locations)
- Maintains backward compatibility for reader/writer infrastructure

These are convenience imports for V2 infrastructure.
"""
from armodel.v2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.AUTOSAR import (
    AUTOSAR,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)

__all__ = ["AUTOSAR", "Identifiable", "ARPackage"]
