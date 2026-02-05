"""
AUTOSAR V2 Models - GenericStructure Module.

V2 Implementation:
- Absolute imports only (CODING_RULE_V2_00001)
- Explicit __all__ exports (CODING_RULE_V2_00003)
"""

# Leaf package files
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import *

# Subdirectory packages
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import *
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import *

__all__ = ["__doc__"]
