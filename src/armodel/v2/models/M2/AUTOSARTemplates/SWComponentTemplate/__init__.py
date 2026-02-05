"""
SWComponentTemplate module for AUTOSAR software component templates.
"""

"""V2 module."""
__all__ = ["__doc__"]

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import *  # noqa: F401, F403
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import *  # noqa: F401, F403

# Components wildcard import removed to avoid circular import with InternalBehavior
# Import specific classes that don't cause circular imports
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    PPortPrototype,
)  # noqa: F401, F403
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import *  # noqa: F401, F403
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype import *  # noqa: F401, F403
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import *  # noqa: F401, F403
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import *  # noqa: F401, F403
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import *  # noqa: F401, F403
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import *  # noqa: F401, F403
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import *  # noqa: F401, F403

# SwcInternalBehavior import removed to avoid circular import with InternalBehavior
# from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import *  # noqa: F401, F403
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import *  # noqa: F401, F403
