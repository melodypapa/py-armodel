"""
V2 M2::AUTOSARTemplates::SystemTemplate::GlobalTime package.
"""

from .CAN import *
from .ETH import *
from .FR import *
from .UserDefined import *

# Classes:
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.AbstractGlobalTimeDomainProps import AbstractGlobalTimeDomainProps
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTimeCorrectionProps import GlobalTimeCorrectionProps
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTimeDomain import GlobalTimeDomain
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTimeGateway import GlobalTimeGateway
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTimeMaster import GlobalTimeMaster
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTimeSlave import GlobalTimeSlave
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkSegmentIdentification import NetworkSegmentIdentification

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
