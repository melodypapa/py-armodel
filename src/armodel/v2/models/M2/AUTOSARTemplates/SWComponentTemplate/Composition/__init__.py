"""
V2 M2::AUTOSARTemplates::SWComponentTemplate::Composition package.
"""

from .InstanceRefs import *

# Classes:
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.AssemblySwConnector import AssemblySwConnector
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.CompositionSwComponentType import CompositionSwComponentType
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.DelegationSwConnector import DelegationSwConnector
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.InstantiationRTEEventProps import InstantiationRTEEventProps
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.InstantiationTimingEventProps import InstantiationTimingEventProps
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PassThroughSwConnector import PassThroughSwConnector
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentPrototype import SwComponentPrototype
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwConnector import SwConnector

__all__ = [
    # .InstanceRefs.*,
    "AssemblySwConnector",
    "CompositionSwComponentType",
    "DelegationSwConnector",
    "InstantiationRTEEventProps",
    "InstantiationTimingEventProps",
    "PassThroughSwConnector",
    "SwComponentPrototype",
    "SwConnector",
]
