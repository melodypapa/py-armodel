"""
Abstract base class of all AUTOSAR objects.
"""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Dict, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
        DateTime,
        String,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import DiagnosticParameterIdent
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDataElement


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

    def setChecksum(self, value: Optional["String"]) -> ARObject:
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

    def setTimestamp(self, value: Optional["DateTime"]) -> ARObject:
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


class AbstractValueRestriction(ARObject, ABC):
    pass


class AbstractVariationRestriction(ARObject, ABC):
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
    """
    This meta-class represents an abstract base class for modeling a diagnostic parameter.

    [constr_1790] Existence of attribute DiagnosticAbstractParameter.bitOffset: For each DiagnosticParameter, attribute bitOffset shall exist at the time when the DEXT is complete.
    [constr_1470] Value of DiagnosticAbstractParameter.bitOffset: The value of DiagnosticAbstractParameter.bitOffset shall only be set to a multiple of 8 at the time when the DEXT is complete.
    """

    # DiagnosticAbstractParameter method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.8, p.37
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBitOffset       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBitOffset       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDataElement  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataElement     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getParameterSize   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setParameterSize   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # Subclasses: DiagnosticParameter (Table 4.5), DiagnosticParameterElement
    # (Table 4.6). PDF Mult of dataElement is 0..1 — the XSD resolves the
    # atpVariation/atpSplitable stereotypes into the DATA-ELEMENTS wrapper with an
    # unbounded choice (single-field model stays PDF-correct, Rule 0001.4); the
    # wrapper is absorbed by the reusable read/write helpers (Rule 0001.7).
    # __init__ calls ARObject.__init__ directly (Referrable precedent): cooperative
    # super() would dispatch to Identifiable.__init__(parent, short_name) under the
    # DiagnosticParameterElement(DiagnosticAbstractParameter, Identifiable) MRO and
    # fail on missing arguments.

    def __init__(self):
        if type(self) is DiagnosticAbstractParameter:
            raise TypeError("DiagnosticAbstractParameter is an abstract class.")

        ARObject.__init__(self)

        # This represents the bitOffset of the DiagnosticParameter. The value of the bitOffset shall always be interpreted as relative to the start of the enclosing DiagnosticData Identifier, DiagnosticParameterIdentifier, or Diagnostic RoutineSubfunction.
        self.bitOffset: Optional[PositiveInteger] = None

        # This represents the related dataElement of the Diagnostic Parameter
        self.dataElement: Optional[DiagnosticDataElement] = None

        # This attribute allows for the specification of the parameter size. This information is relevant if there is a gap between one diagnostic parameter and the following diagnostic parameter (or the tail of the telegram). The unit is bit and the values shall be multiples of 8.
        self.parameterSize: Optional[PositiveInteger] = None

    def getBitOffset(self) -> Optional[PositiveInteger]:
        """
        This represents the bitOffset of the DiagnosticParameter. The value of the bitOffset shall always be interpreted as relative to the start of the enclosing DiagnosticData Identifier, DiagnosticParameterIdentifier, or Diagnostic RoutineSubfunction.
        """
        return self.bitOffset

    def setBitOffset(self, value: Optional[PositiveInteger]) -> DiagnosticAbstractParameter:
        """
        This represents the bitOffset of the DiagnosticParameter. The value of the bitOffset shall always be interpreted as relative to the start of the enclosing DiagnosticData Identifier, DiagnosticParameterIdentifier, or Diagnostic RoutineSubfunction.
        A None value is a no-op and does not overwrite an existing bitOffset.
        """
        if value is not None:
            self.bitOffset = value
        return self

    def createDataElement(self, short_name: str) -> DiagnosticDataElement:
        """
        This represents the related dataElement of the Diagnostic Parameter
        The existing data element is returned when the short name already exists (no duplicate creation).
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDataElement

        if self.dataElement is None or self.dataElement.getShortName() != short_name:
            self.dataElement = DiagnosticDataElement(self, short_name)
        return self.dataElement

    def getDataElement(self) -> Optional[DiagnosticDataElement]:
        """
        This represents the related dataElement of the Diagnostic Parameter
        """
        return self.dataElement

    def getParameterSize(self) -> Optional[PositiveInteger]:
        """
        This attribute allows for the specification of the parameter size. This information is relevant if there is a gap between one diagnostic parameter and the following diagnostic parameter (or the tail of the telegram). The unit is bit and the values shall be multiples of 8.
        """
        return self.parameterSize

    def setParameterSize(self, value: Optional[PositiveInteger]) -> DiagnosticAbstractParameter:
        """
        This attribute allows for the specification of the parameter size. This information is relevant if there is a gap between one diagnostic parameter and the following diagnostic parameter (or the tail of the telegram). The unit is bit and the values shall be multiples of 8.
        A None value is a no-op and does not overwrite an existing parameterSize.
        """
        if value is not None:
            self.parameterSize = value
        return self


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


class DiagnosticParameter(DiagnosticAbstractParameter, VariationPointCapable):
    """
    This meta-class represents the ability to describe information relevant for the execution of a specific diagnostic service, i.e. it can be taken to parameterize the service.
    """

    # DiagnosticParameter method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.5, p.36
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createIdent     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIdent        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSupportInfo  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSupportInfo  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # getVariationPoint / setVariationPoint provided by the VariationPointCapable base (mixin) — no spec row (stereotype-inherent)

    def __init__(self):
        super().__init__()

        # The aggregation in the role ident provides the ability to make the DiagnosticAbstractParameter identifiable. From the semantical point of view, the AbstractDiagnostic Parameter is considered a first-class Identifiable and therefore the aggregation in the role ident shall always exist (until it may be possible to let AbstractDiagnostic Parameter directly inherit from Identifiable). Stereotypes: atpIdentityContributor
        self.ident: Optional[DiagnosticParameterIdent] = None

        # This attribute represents the ability to define which bit of the support info byte is representing this part of the PID.
        self.supportInfo: Optional[DiagnosticParameterSupportInfo] = None

    def createIdent(self, short_name: str) -> DiagnosticParameterIdent:
        """
        The aggregation in the role ident provides the ability to make the DiagnosticAbstractParameter identifiable. From the semantical point of view, the AbstractDiagnostic Parameter is considered a first-class Identifiable and therefore the aggregation in the role ident shall always exist (until it may be possible to let AbstractDiagnostic Parameter directly inherit from Identifiable).
        The existing ident is returned when the short name already exists (no duplicate creation).
        """
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import DiagnosticParameterIdent

        if self.ident is None or self.ident.getShortName() != short_name:
            self.ident = DiagnosticParameterIdent(self, short_name)
        return self.ident

    def getIdent(self) -> Optional[DiagnosticParameterIdent]:
        """
        The aggregation in the role ident provides the ability to make the DiagnosticAbstractParameter identifiable. From the semantical point of view, the AbstractDiagnostic Parameter is considered a first-class Identifiable and therefore the aggregation in the role ident shall always exist (until it may be possible to let AbstractDiagnostic Parameter directly inherit from Identifiable).
        """
        return self.ident

    def getSupportInfo(self) -> Optional[DiagnosticParameterSupportInfo]:
        """
        This attribute represents the ability to define which bit of the support info byte is representing this part of the PID.
        """
        return self.supportInfo

    def setSupportInfo(self, value: Optional[DiagnosticParameterSupportInfo]) -> DiagnosticParameter:
        """
        This attribute represents the ability to define which bit of the support info byte is representing this part of the PID.
        A None value is a no-op and does not overwrite an existing supportInfo.
        """
        if value is not None:
            self.supportInfo = value
        return self


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


class List(ARObject):
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


class SdgElementWithGid(ARObject, ABC):
    pass


class SpecificationScope(ARObject):
    pass


class SwAxisCont(ARObject):
    pass


class SwcModeManagerErrorEvent(ARObject):
    pass


class TextualCondition(AbstractCondition):
    pass


class ValueRestrictionWithSeverity(AbstractValueRestriction):
    pass


class VariationRestrictionWithSeverity(AbstractVariationRestriction):
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


# Cycle-breaker (Rule 0005): PrimitiveTypes imports ARObject from this module, so the
# PositiveInteger name needed by DiagnosticAbstractParameter's annotations must be bound
# at the bottom, after every class above is defined. Placed here so get_type_hints can
# resolve the bitOffset/parameterSize annotations at runtime on Python 3.8.
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger  # noqa: E402
