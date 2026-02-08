"""
V2 M2::AUTOSARTemplates::CommonStructure::ServiceNeeds package.
"""
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.BswMgrNeeds import BswMgrNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ComMgrUserNeeds import ComMgrUserNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.CryptoKeyManagementNeeds import CryptoKeyManagementNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.CryptoServiceJobNeeds import CryptoServiceJobNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.CryptoServiceNeeds import CryptoServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DevelopmentError import DevelopmentError
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagEventDebounceAlgorithm import DiagEventDebounceAlgorithm
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagEventDebounceCounterBased import DiagEventDebounceCounterBased
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagEventDebounceMonitorInternal import DiagEventDebounceMonitorInternal
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagEventDebounceTimeBased import DiagEventDebounceTimeBased
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticCapabilityElement import DiagnosticCapabilityElement
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticCommunicationManagerNeeds import DiagnosticCommunicationManagerNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticComponentNeeds import DiagnosticComponentNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticControlNeeds import DiagnosticControlNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticEnableConditionNeeds import DiagnosticEnableConditionNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticEventInfoNeeds import DiagnosticEventInfoNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticEventManagerNeeds import DiagnosticEventManagerNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticEventNeeds import DiagnosticEventNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticIoControlNeeds import DiagnosticIoControlNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticOperationCycleNeeds import DiagnosticOperationCycleNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticRequestFileTransferNeeds import DiagnosticRequestFileTransferNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticRoutineNeeds import DiagnosticRoutineNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticStorageConditionNeeds import DiagnosticStorageConditionNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticUploadDownloadNeeds import DiagnosticUploadDownloadNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticValueNeeds import DiagnosticValueNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DiagnosticsCommunicationSecurityNeeds import DiagnosticsCommunicationSecurityNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DltUserNeeds import DltUserNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DoIpActivationLineNeeds import DoIpActivationLineNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DoIpGidNeeds import DoIpGidNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DoIpGidSynchronizationNeeds import DoIpGidSynchronizationNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DoIpPowerModeStatusNeeds import DoIpPowerModeStatusNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DoIpRoutingActivationAuthenticationNeeds import DoIpRoutingActivationAuthenticationNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DoIpRoutingActivationConfirmationNeeds import DoIpRoutingActivationConfirmationNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DoIpServiceNeeds import DoIpServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.DtcStatusChangeNotificationNeeds import DtcStatusChangeNotificationNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.EcuStateMgrUserNeeds import EcuStateMgrUserNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ErrorTracerNeeds import ErrorTracerNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.FunctionInhibitionAvailabilityNeeds import FunctionInhibitionAvailabilityNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.FunctionInhibitionNeeds import FunctionInhibitionNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.FurtherActionByteNeeds import FurtherActionByteNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.GlobalSupervisionNeeds import GlobalSupervisionNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.HardwareTestNeeds import HardwareTestNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.IdsMgrCustomTimestampNeeds import IdsMgrCustomTimestampNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.IdsMgrNeeds import IdsMgrNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.IndicatorStatusNeeds import IndicatorStatusNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.J1939DcmDm19Support import J1939DcmDm19Support
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.J1939RmIncomingRequestServiceNeeds import J1939RmIncomingRequestServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.J1939RmOutgoingRequestServiceNeeds import J1939RmOutgoingRequestServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.NvBlockNeeds import NvBlockNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ObdControlServiceNeeds import ObdControlServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ObdInfoServiceNeeds import ObdInfoServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ObdMonitorServiceNeeds import ObdMonitorServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ObdPidServiceNeeds import ObdPidServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ObdRatioDenominatorNeeds import ObdRatioDenominatorNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ObdRatioServiceNeeds import ObdRatioServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.RoleBasedDataAssignment import RoleBasedDataAssignment
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.RuntimeError import RuntimeError
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SecureOnBoardCommunicationNeeds import SecureOnBoardCommunicationNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceDependency import ServiceDependency
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SupervisedEntityCheckpointNeeds import SupervisedEntityCheckpointNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SupervisedEntityNeeds import SupervisedEntityNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SymbolicNameProps import SymbolicNameProps
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SyncTimeBaseMgrUserNeeds import SyncTimeBaseMgrUserNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.TracedFailure import TracedFailure
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.TransientFault import TransientFault
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.V2xDataManagerNeeds import V2xDataManagerNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.V2xFacUserNeeds import V2xFacUserNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.V2xMUserNeeds import V2xMUserNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.VendorSpecificServiceNeeds import VendorSpecificServiceNeeds
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.WarningIndicatorRequestedBitNeeds import WarningIndicatorRequestedBitNeeds

__all__ = [
    "BswMgrNeeds",
    "ComMgrUserNeeds",
    "CryptoKeyManagementNeeds",
    "CryptoServiceJobNeeds",
    "CryptoServiceNeeds",
    "DevelopmentError",
    "DiagEventDebounceAlgorithm",
    "DiagEventDebounceCounterBased",
    "DiagEventDebounceMonitorInternal",
    "DiagEventDebounceTimeBased",
    "DiagnosticAudienceEnum",
    "DiagnosticCapabilityElement",
    "DiagnosticClearDtcNotificationEnum",
    "DiagnosticCommunicationManagerNeeds",
    "DiagnosticComponentNeeds",
    "DiagnosticControlNeeds",
    "DiagnosticDenominatorConditionEnum",
    "DiagnosticEnableConditionNeeds",
    "DiagnosticEventInfoNeeds",
    "DiagnosticEventManagerNeeds",
    "DiagnosticEventNeeds",
    "DiagnosticIoControlNeeds",
    "DiagnosticMonitorUpdateKindEnum",
    "DiagnosticOperationCycleNeeds",
    "DiagnosticProcessingStyleEnum",
    "DiagnosticRequestFileTransferNeeds",
    "DiagnosticRoutineNeeds",
    "DiagnosticRoutineTypeEnum",
    "DiagnosticServiceRequestCallbackTypeEnum",
    "DiagnosticStorageConditionNeeds",
    "DiagnosticUploadDownloadNeeds",
    "DiagnosticValueAccessEnum",
    "DiagnosticValueNeeds",
    "DiagnosticsCommunicationSecurityNeeds",
    "DltUserNeeds",
    "DoIpActivationLineNeeds",
    "DoIpGidNeeds",
    "DoIpGidSynchronizationNeeds",
    "DoIpPowerModeStatusNeeds",
    "DoIpRoutingActivationAuthenticationNeeds",
    "DoIpRoutingActivationConfirmationNeeds",
    "DoIpServiceNeeds",
    "DtcStatusChangeNotificationNeeds",
    "EcuStateMgrUserNeeds",
    "ErrorTracerNeeds",
    "EventAcceptanceStatusEnum",
    "FunctionInhibitionAvailabilityNeeds",
    "FunctionInhibitionNeeds",
    "FurtherActionByteNeeds",
    "GlobalSupervisionNeeds",
    "HardwareTestNeeds",
    "IdsMgrCustomTimestampNeeds",
    "IdsMgrNeeds",
    "IndicatorStatusNeeds",
    "J1939DcmDm19Support",
    "J1939RmIncomingRequestServiceNeeds",
    "J1939RmOutgoingRequestServiceNeeds",
    "MaxCommModeEnum",
    "NvBlockNeeds",
    "NvBlockNeedsReliabilityEnum",
    "NvBlockNeedsWritingPriorityEnum",
    "ObdControlServiceNeeds",
    "ObdInfoServiceNeeds",
    "ObdMonitorServiceNeeds",
    "ObdPidServiceNeeds",
    "ObdRatioConnectionKindEnum",
    "ObdRatioDenominatorNeeds",
    "ObdRatioServiceNeeds",
    "OperationCycleTypeEnum",
    "RoleBasedDataAssignment",
    "RuntimeError",
    "SecureOnBoardCommunicationNeeds",
    "ServiceDependency",
    "ServiceDiagnosticRelevanceEnum",
    "ServiceNeeds",
    "ServiceProviderEnum",
    "StorageConditionStatusEnum",
    "SupervisedEntityCheckpointNeeds",
    "SupervisedEntityNeeds",
    "SymbolicNameProps",
    "SyncTimeBaseMgrUserNeeds",
    "TracedFailure",
    "TransientFault",
    "V2xDataManagerNeeds",
    "V2xFacUserNeeds",
    "V2xMUserNeeds",
    "VendorSpecificServiceNeeds",
    "VerificationStatusIndicationModeEnum",
    "WarningIndicatorRequestedBitNeeds",
]
