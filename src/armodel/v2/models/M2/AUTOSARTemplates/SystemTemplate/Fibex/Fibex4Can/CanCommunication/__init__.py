"""
V2 M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication package.
"""
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanFrame import CanFrame
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanFrameTriggering import CanFrameTriggering
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanXlFrameTriggeringProps import CanXlFrameTriggeringProps
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.RxIdentifierRange import RxIdentifierRange

__all__ = [
    "CanAddressingModeType",
    "CanFrame",
    "CanFrameRxBehaviorEnum",
    "CanFrameTriggering",
    "CanFrameTxBehaviorEnum",
    "CanXlFrameTriggeringProps",
    "RxIdentifierRange",
]
