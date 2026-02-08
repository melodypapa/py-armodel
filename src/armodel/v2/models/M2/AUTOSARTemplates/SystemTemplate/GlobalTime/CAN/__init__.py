"""
V2 M2::AUTOSARTemplates::SystemTemplate::GlobalTime::CAN package.
"""
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.CanGlobalTimeDomainProps import (
    CanGlobalTimeDomainProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.GlobalTimeCanMaster import (
    GlobalTimeCanMaster,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.GlobalTimeCanSlave import (
    GlobalTimeCanSlave,
)

__all__ = [
    "CanGlobalTimeDomainProps",
    "GlobalTimeCanMaster",
    "GlobalTimeCanSlave",
]
