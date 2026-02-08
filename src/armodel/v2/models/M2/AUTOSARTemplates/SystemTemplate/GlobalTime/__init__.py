"""
V2 M2::AUTOSARTemplates::SystemTemplate::GlobalTime package.
"""

# Classes:
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.AbstractGlobalTimeDomainProps import (
    AbstractGlobalTimeDomainProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.CAN import (
    CanGlobalTimeDomainProps,
    GlobalTimeCanMaster,
    GlobalTimeCanSlave,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH import (
    EthGlobalTimeDomainProps,
    EthGlobalTimeManagedCouplingPort,
    EthGlobalTimeMessageFormatEnum,
    EthTSynCrcFlags,
    EthTSynSubTlvConfig,
    GlobalTimeEthMaster,
    GlobalTimeEthSlave,
    GlobalTimePortRoleEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.FR import (
    FrGlobalTimeDomainProps,
    GlobalTimeFrMaster,
    GlobalTimeFrSlave,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.UserDefined import (
    UserDefinedGlobalTimeMaster,
    UserDefinedGlobalTimeSlave,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTimeCorrectionProps import (
    GlobalTimeCorrectionProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTimeDomain import (
    GlobalTimeDomain,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTimeGateway import (
    GlobalTimeGateway,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTimeMaster import (
    GlobalTimeMaster,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTimeSlave import (
    GlobalTimeSlave,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkSegmentIdentification import (
    NetworkSegmentIdentification,
)

__all__ = [
    # .CAN.*,
    # .ETH.*,
    # .FR.*,
    # .UserDefined.*,
    "AbstractGlobalTimeDomainProps",
    "GlobalTimeCorrectionProps",
    "GlobalTimeCrcSupportEnum",
    "GlobalTimeCrcValidationEnum",
    "GlobalTimeDomain",
    "GlobalTimeGateway",
    "GlobalTimeIcvSupportEnum",
    "GlobalTimeIcvVerificationEnum",
    "GlobalTimeMaster",
    "GlobalTimeSlave",
    "NetworkSegmentIdentification",
]
