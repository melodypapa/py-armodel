"""
Abstract base class of all AUTOSAR objects.
"""

from abc import ABC
from typing import TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
        DateTime,
        String,
    )

class ARObject(ABC):
    """
    Abstract base class of all AUTOSAR meta-classes
    (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 6.1).
    """

    # ARObject method parity checklist:
    # Spec verified: R23-11
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 6.1, p.192
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setChecksum   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getChecksum   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimestamp  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimestamp  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    #
    # Internal members (no spec counterpart, cf. CollectableElement decision):
    #   parent     — structural link to the owning object
    #   getTagName — parser helper for namespace-stripped tag names

    def __init__(self):
        if type(self) is ARObject:
            raise TypeError("ARObject is an abstract class.")

        self.parent: Optional["ARObject"] = None

        # Checksum calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine if an ArObject has changed. The checksum has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the checksum.
        self.checksum: Optional["String"] = None

        # Timestamp calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine the last change of an ArObject. The timestamp has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp.
        self.timestamp: Optional["DateTime"] = None

    def getChecksum(self) -> Optional["String"]:
        """
        Checksum calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine if an ArObject has changed. The checksum has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the checksum.
        """
        return self.checksum

    def setChecksum(self, value: Optional["String"]) -> "ARObject":
        """
        Checksum calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine if an ArObject has changed. The checksum has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the checksum. A None value is a no-op and does not overwrite an existing checksum.
        """
        if value is not None:
            self.checksum = value
        return self

    def getTimestamp(self) -> Optional["DateTime"]:
        """
        Timestamp calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine the last change of an ArObject. The timestamp has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp.
        """
        return self.timestamp

    def setTimestamp(self, value: Optional["DateTime"]) -> "ARObject":
        """
        Timestamp calculated by the user's tool environment for an ArObject. May be used in an own tool environment to determine the last change of an ArObject. The timestamp has no semantic meaning for an AUTOSAR model and there is no requirement for AUTOSAR tools to manage the timestamp. A None value is a no-op and does not overwrite an existing timestamp.
        """
        if value is not None:
            self.timestamp = value
        return self

    def getTagName(self, tag: str, nsmap: Dict) -> str:
        """
        Gets the tag name without namespace prefix.

        Args:
            tag: The full tag name with namespace prefix
            nsmap: The namespace map dictionary

        Returns:
            The tag name without namespace prefix
        """
        return tag.replace("{%s}" % nsmap["xmlns"], "")

class AbstractCondition(ARObject, ABC):
    pass

class AbstractMultiplicityRestriction(ARObject, ABC):
    pass
class AttributeCondition(AbstractCondition, ABC):
    pass

class AggregationCondition(AttributeCondition):
    pass

class ArParameterInImplementationDataInstanceRef(ARObject):
    pass

class Baseline(ARObject):
    pass

class CalibrationParameterValue(ARObject):
    pass

class ClassTailoring(ARObject, ABC):
    pass

class ClientServerOperationBlueprintMapping(ARObject):
    pass

class DiagnosticAbstractParameter(ARObject, ABC):
    pass

class DiagnosticClearResetEmissionRelatedInfo(ARObject):
    pass

class DiagnosticComControlSpecificChannel(ARObject):
    pass

class DiagnosticComControlSubNodeChannel(ARObject):
    pass

class DiagnosticCommonProps(ARObject):
    pass

class DiagnosticConnectedIndicator(ARObject):
    pass

class DiagnosticContributionSet(ARObject):
    pass

class DiagnosticControlDTCSetting(ARObject):
    pass

class DiagnosticControlEnableMaskBit(ARObject):
    pass

class DiagnosticEnableConditionPortMapping(ARObject):
    pass

class DiagnosticEnvModeCondition(ARObject):
    pass

class DiagnosticEventWindow(ARObject):
    pass

class DiagnosticFimFunctionMapping(ARObject):
    pass

class DiagnosticFunctionIdentifierInhibit(ARObject):
    pass

class DiagnosticInhibitSourceEventMapping(ARObject):
    pass

class DiagnosticIumprGroupIdentifier(ARObject):
    pass

class DiagnosticMemoryDestination(ARObject, ABC):
    pass

class DiagnosticMemoryDestinationUserDefined(ARObject):
    pass

class DiagnosticParameter(DiagnosticAbstractParameter):
    pass

class DiagnosticParameterElementAccess(ARObject):
    pass

class DiagnosticParameterSupportInfo(ARObject):
    pass

class DiagnosticPeriodicRate(ARObject):
    pass

class DiagnosticReadMemoryByAddress(ARObject):
    pass

class DiagnosticRequestCurrentPowertrainData(ARObject):
    pass

class DiagnosticRequestDownloadClass(ARObject):
    pass

class DiagnosticRequestEmissionRelatedDTC(ARObject):
    pass

class DiagnosticRequestOnBoardMonitoringTestResultsClass(ARObject):
    pass

class DiagnosticServiceMappingDiagTarget(ARObject, ABC):
    pass

class DiagnosticServiceSwMapping(ARObject):
    pass

class DiagnosticSupportInfoByte(ARObject):
    pass

class DiagnosticTestIdentifier(ARObject):
    pass

class DiagnosticTroubleCodeJ1939(ARObject):
    pass

class DiagnosticTroubleCodeObd(ARObject):
    pass

class DiagnosticTroubleCodeProps(ARObject):
    pass

class DiagnosticTroubleCodeUds(ARObject):
    pass

class DiagnosticWriteMemoryByAddress(ARObject):
    pass

class EventObdReadinessGroup(ARObject):
    pass

class FMAttributeValue(ARObject):
    pass

class FMFeatureDecomposition(ARObject):
    pass

class InvertCondition(AbstractCondition):
    pass

class MultiplicityRestrictionWithSeverity(AbstractMultiplicityRestriction):
    pass

class PhysicalDimensionMapping(ARObject):
    pass

class PrimitiveAttributeCondition(AttributeCondition):
    pass

class ReferenceCondition(AttributeCondition):
    pass

class RestrictionWithSeverity(ARObject, ABC):
    pass

class RoleBasedResourceDependency(ARObject):
    pass

class RptHook(ARObject):
    pass

class RptProfile(ARObject):
    pass

class SpecificationScope(ARObject):
    pass

class SwAxisCont(ARObject):
    pass

class SwcModeManagerErrorEvent(ARObject):
    pass

class TextualCondition(AbstractCondition):
    pass
class AbstractGlobalTimeDomainProps(ARObject, ABC):
    pass

class BinaryManifestAddressableObject(ARObject, ABC):
    pass

class BinaryManifestItemValue(ARObject, ABC):
    pass

class BinaryManifestResource(ARObject, ABC):
    pass

class BusMirrorCanIdRangeMapping(ARObject):
    pass

class BusMirrorCanIdToCanIdMapping(ARObject):
    pass

class BusMirrorChannel(ARObject):
    pass

class BusMirrorChannelMappingCan(ARObject):
    pass

class BusMirrorChannelMappingIp(ARObject):
    pass

class BusMirrorLinPidToCanIdMapping(ARObject):
    pass

class CommonSignalPath(ARObject):
    pass

class ContainerIPdu(ARObject):
    pass

class CouplingElement(ARObject):
    pass

class CpSoftwareClusterCommunicationResourceProps(ARObject, ABC):
    pass

class DdsCpISignalToDdsTopicMapping(ARObject):
    pass

class DdsCpProvidedServiceInstance(ARObject):
    pass

class DdsCpQosProfile(ARObject):
    pass

class DdsCpServiceInstanceEvent(ARObject):
    pass

class DdsCpServiceInstanceOperation(ARObject):
    pass

class DdsCpTopic(ARObject):
    pass

class DdsDeadline(ARObject):
    pass

class DdsDestinationOrder(ARObject):
    pass

class DdsDurability(ARObject):
    pass

class DdsDurabilityService(ARObject):
    pass

class DdsHistory(ARObject):
    pass

class DdsLatencyBudget(ARObject):
    pass

class DdsLifespan(ARObject):
    pass

class DdsLiveliness(ARObject):
    pass

class DdsOwnership(ARObject):
    pass

class DdsOwnershipStrength(ARObject):
    pass

class DdsReliability(ARObject):
    pass

class DdsResourceLimits(ARObject):
    pass

class DdsTopicData(ARObject):
    pass

class DdsTransportPriority(ARObject):
    pass

class Dhcpv6Props(ARObject):
    pass

class EcuResourceEstimation(ARObject):
    pass

class EthGlobalTimeManagedCouplingPort(ARObject):
    pass

class EthTSynCrcFlags(ARObject):
    pass

class EthTSynSubTlvConfig(ARObject):
    pass

class EthernetWakeupSleepOnDatalineConfig(ARObject):
    pass

class FlexrayArTpChannel(ARObject):
    pass

class FlexrayTpEcu(ARObject):
    pass

class ForbiddenSignalPath(ARObject):
    pass

class GlobalTimeCorrectionProps(ARObject):
    pass

class GlobalTimeSlave(ARObject, ABC):
    pass

class IEEE1722TpAcfBusPart(ARObject, ABC):
    pass

class IEEE1722TpAcfLin(ARObject):
    pass

class IEEE1722TpConfig(ARObject):
    pass

class IdsmInstance(ARObject):
    pass

class IdsmTrafficLimitation(ARObject):
    pass

class Ipv4ArpProps(ARObject):
    pass

class Ipv4AutoIpProps(ARObject):
    pass

class Ipv4FragmentationProps(ARObject):
    pass

class Ipv4Props(ARObject):
    pass

class Ipv6FragmentationProps(ARObject):
    pass

class Ipv6NdpProps(ARObject):
    pass

class Ipv6Props(ARObject):
    pass

class J1939ControllerApplicationToJ1939NmNodeMapping(ARObject):
    pass

class J1939TpConfig(ARObject):
    pass

class J1939TpConnection(ARObject):
    pass

class J1939TpPg(ARObject):
    pass

class MappingConstraint(ARObject, ABC):
    pass

class NetworkSegmentIdentification(ARObject):
    pass

class NmCoordinator(ARObject):
    pass

class PermissibleSignalPath(ARObject):
    pass

class PncMapping(ARObject):
    pass

class RteEventInCompositionToOsTaskProxyMapping(ARObject):
    pass

class RteEventInSystemToOsTaskProxyMapping(ARObject):
    pass

class SecurityEventAggregationFilter(ARObject):
    pass

class SecurityEventContextMapping(ARObject, ABC):
    pass

class SecurityEventContextMappingCommConnector(ARObject):
    pass

class SecurityEventContextProps(ARObject):
    pass

class SecurityEventFilterChain(ARObject):
    pass

class SecurityEventStateFilter(ARObject):
    pass

class SeparateSignalPath(ARObject):
    pass

class SomeipSdServerServiceInstanceConfig(ARObject):
    pass

class SomeipTpConnection(ARObject):
    pass

class StreamFilterIEEE1722Tp(ARObject):
    pass

class StreamFilterIpv4Address(ARObject):
    pass

class StreamFilterIpv6Address(ARObject):
    pass

class StreamFilterMACAddress(ARObject):
    pass

class StreamFilterPortRange(ARObject):
    pass

class StreamFilterRuleDataLinkLayer(ARObject):
    pass

class StreamFilterRuleIpTp(ARObject):
    pass

class SwcToSwcOperationArguments(ARObject):
    pass

class SwcToSwcSignal(ARObject):
    pass

class SystemTiming(ARObject):
    pass

class TDCpSoftwareClusterMappingSet(ARObject):
    pass

class TransformationProps(ARObject, ABC):
    pass

class TriggerToSignalMapping(ARObject):
    pass

class TtcanCommunicationController(ARObject):
    pass

class UserDefinedCommunicationConnector(ARObject):
    pass

class BinaryManifestItemNumericalValue(BinaryManifestItemValue):
    pass

class BinaryManifestItemPointerValue(BinaryManifestItemValue):
    pass

class CanGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    pass

class ClientServerOperationComProps(CpSoftwareClusterCommunicationResourceProps):
    pass

class ComponentClustering(MappingConstraint):
    pass

class ComponentSeparation(MappingConstraint):
    pass

class DataComProps(CpSoftwareClusterCommunicationResourceProps):
    pass

class EthGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    pass

class FrGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    pass
