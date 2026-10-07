from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from abc import ABC
from typing import TYPE_CHECKING, List, Optional, cast

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
    Identifiable,
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    Integer,
    Ip4AddressString,
    Ip6AddressString,
    MacAddressString,
    PositiveInteger,
    PositiveUnlimitedInteger,
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector, PhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationController
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPSecConfig, MacSecProps

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
        ConsumedServiceInstance,
        ProvidedServiceInstance,
        SoAdConfig,
    )


class MacMulticastGroup(Identifiable):
    """
    Per EthernetCluster globally defined MacMulticastGroup. One sender can handle many receivers simultaneously if the receivers have all the same macMulticastAddress. The addresses need to be unique for the particular EthernetCluster.
    """

    # MacMulticastGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.48, p.104
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMacMulticastAddress    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMacMulticastAddress    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # A multicast MAC address (Media Access Control address) is a identifier for a group of hosts in a network.
        self.macMulticastAddress: Optional[MacAddressString] = None

    def getMacMulticastAddress(self) -> Optional[MacAddressString]:
        """
        A multicast MAC address (Media Access Control address) is a identifier for a group of hosts in a network.
        """
        return self.macMulticastAddress

    def setMacMulticastAddress(self, value: Optional[MacAddressString]) -> MacMulticastGroup:
        """
        A multicast MAC address (Media Access Control address) is a identifier for a group of hosts in a network.
        A None value is a no-op and does not overwrite an existing macMulticastAddress.
        """
        if value is not None:
            self.macMulticastAddress = value
        return self


class EthernetCluster(CommunicationCluster):
    """
    Ethernet-specific cluster attributes. Tags: atp.recommendedPackage=CommunicationClusters
    """

    # EthernetCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.47, p.103
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addCouplingPortConnection         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCouplingPortConnections        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getCouplingPortStartupActiveTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCouplingPortStartupActiveTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCouplingPortSwitchoffDelay     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCouplingPortSwitchoffDelay     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createMacMulticastGroup           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMacMulticastGroups             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specification of connections between CouplingElements and EcuInstances. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=postBuild
        self.couplingPortConnections: List[CouplingPortConnection] = []

        # The attribute specifies the time in second a coupling port is switched on to enable the host ECU (ECU that maintains an Ethernet switch) to listen to the network for potential network management requests.
        self.couplingPortStartupActiveTime: Optional[TimeValue] = None

        # Switch off delay for CouplingPorts in seconds. It denotes the delay of switching off couplingPorts after the request to switch off a couplingPort was issued. (e.g. switch off of Ethernet switch ports).
        self.couplingPortSwitchoffDelay: Optional[TimeValue] = None

        # MacMulticastGroup that is defined for the Subnet (EthernetCluster).
        self.macMulticastGroups: List[MacMulticastGroup] = []

    def addCouplingPortConnection(self, value: Optional[CouplingPortConnection]) -> EthernetCluster:
        """
        Specification of connections between CouplingElements and EcuInstances. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=postBuild
        A None value is a no-op and does not append to couplingPortConnections.
        """
        if value is not None:
            self.couplingPortConnections.append(value)
        return self

    def getCouplingPortConnections(self) -> List[CouplingPortConnection]:
        """
        Specification of connections between CouplingElements and EcuInstances. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=postBuild
        """
        return self.couplingPortConnections

    def getCouplingPortStartupActiveTime(self) -> Optional[TimeValue]:
        """
        The attribute specifies the time in second a coupling port is switched on to enable the host ECU (ECU that maintains an Ethernet switch) to listen to the network for potential network management requests.
        """
        return self.couplingPortStartupActiveTime

    def setCouplingPortStartupActiveTime(self, value: Optional[TimeValue]) -> EthernetCluster:
        """
        The attribute specifies the time in second a coupling port is switched on to enable the host ECU (ECU that maintains an Ethernet switch) to listen to the network for potential network management requests.
        A None value is a no-op and does not overwrite an existing couplingPortStartupActiveTime.
        """
        if value is not None:
            self.couplingPortStartupActiveTime = value
        return self

    def getCouplingPortSwitchoffDelay(self) -> Optional[TimeValue]:
        """
        Switch off delay for CouplingPorts in seconds. It denotes the delay of switching off couplingPorts after the request to switch off a couplingPort was issued. (e.g. switch off of Ethernet switch ports).
        """
        return self.couplingPortSwitchoffDelay

    def setCouplingPortSwitchoffDelay(self, value: Optional[TimeValue]) -> EthernetCluster:
        """
        Switch off delay for CouplingPorts in seconds. It denotes the delay of switching off couplingPorts after the request to switch off a couplingPort was issued. (e.g. switch off of Ethernet switch ports).
        A None value is a no-op and does not overwrite an existing couplingPortSwitchoffDelay.
        """
        if value is not None:
            self.couplingPortSwitchoffDelay = value
        return self

    def createMacMulticastGroup(self, short_name: str) -> MacMulticastGroup:
        """
        MacMulticastGroup that is defined for the Subnet (EthernetCluster).
        """
        if not self.IsReferrableElementExists(short_name, MacMulticastGroup):
            group = MacMulticastGroup(self, short_name)
            self.addReferrableElement(group)
            self.macMulticastGroups.append(group)
        return cast(MacMulticastGroup, self.getReferrableElement(short_name, MacMulticastGroup))

    def getMacMulticastGroups(self) -> List[MacMulticastGroup]:
        """
        MacMulticastGroup that is defined for the Subnet (EthernetCluster).
        """
        return self.macMulticastGroups


class CouplingElement(FibexElement):
    """
    A CouplingElement is used to connect EcuInstances to the VLAN of an EthernetCluster. Coupling Elements can reach from a simple hub to a complex managed switch or even devices with functionalities in higher layers. A CouplingElement that is not related to an EcuInstance occurs as a dedicated single device. Tags: atp.recommendedPackage=CouplingElements
    """

    # CouplingElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.52, p.108
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommunicationClusterRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommunicationClusterRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createCouplingElementSwitchDetails  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCouplingElementDetails           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createCouplingPort                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCouplingPorts                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getCouplingType                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCouplingType                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcuInstanceRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuInstanceRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addFirewallRuleRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFirewallRuleRefs                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This relationship defines to which cluster the Coupling Element belongs.
        self.communicationClusterRef: Optional[RefType] = None

        # Definition of details for this specific CouplingElement. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=couplingElementDetails.shortName, couplingElementDetails.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild xml.namePlural=COUPLING-ELEMENT-DETAILS
        self.couplingElementDetails: Optional[CouplingElementAbstractDetails] = None

        # Hardware Port of the CouplingElement that is used to connect this CouplingPort to EcuInstances or other CouplingElements. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=couplingPort.shortName, coupling Port.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.couplingPorts: List[CouplingPort] = []

        # Describes the coupling type of this CouplingElement.
        self.couplingType: Optional[CouplingElementEnum] = None

        # Optional reference to the ECU where the Coupling Element is located.
        self.ecuInstanceRef: Optional[RefType] = None

        # Firewall rules defined in the context of a Coupling Element. Tags: atp.Status=candidate
        self.firewallRuleRefs: List[RefType] = []

    def getCommunicationClusterRef(self) -> Optional[RefType]:
        """
        This relationship defines to which cluster the Coupling Element belongs.
        """
        return self.communicationClusterRef

    def setCommunicationClusterRef(self, value: Optional[RefType]) -> CouplingElement:
        """
        This relationship defines to which cluster the Coupling Element belongs.

        A None value is a no-op and does not overwrite an existing communicationClusterRef.
        """
        if value is not None:
            self.communicationClusterRef = value
        return self

    def createCouplingElementSwitchDetails(self, short_name: str) -> CouplingElementSwitchDetails:
        """
        Definition of details for this specific CouplingElement. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=couplingElementDetails.shortName, couplingElementDetails.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild xml.namePlural=COUPLING-ELEMENT-DETAILS
        The existing element is returned when the short name already exists (no duplicate creation).
        """
        if self.couplingElementDetails is None or self.couplingElementDetails.getShortName() != short_name:
            self.couplingElementDetails = CouplingElementSwitchDetails(self, short_name)
        return cast(CouplingElementSwitchDetails, self.couplingElementDetails)

    def getCouplingElementDetails(self) -> Optional[CouplingElementAbstractDetails]:
        """
        Definition of details for this specific CouplingElement. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=couplingElementDetails.shortName, couplingElementDetails.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild xml.namePlural=COUPLING-ELEMENT-DETAILS
        """
        return self.couplingElementDetails

    def createCouplingPort(self, short_name: str) -> CouplingPort:
        """
        Hardware Port of the CouplingElement that is used to connect this CouplingPort to EcuInstances or other CouplingElements. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=couplingPort.shortName, coupling Port.variationPoint.shortLabel vh.latestBindingTime=postBuild
        The existing element is returned when the short name already exists (no duplicate creation).
        """
        if not self.IsReferrableElementExists(short_name, CouplingPort):
            port = CouplingPort(self, short_name)
            self.addReferrableElement(port)
            self.couplingPorts.append(port)
        return cast(CouplingPort, self.getReferrableElement(short_name, CouplingPort))

    def getCouplingPorts(self) -> List[CouplingPort]:
        """
        Hardware Port of the CouplingElement that is used to connect this CouplingPort to EcuInstances or other CouplingElements. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=couplingPort.shortName, coupling Port.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.couplingPorts

    def getCouplingType(self) -> Optional[CouplingElementEnum]:
        """
        Describes the coupling type of this CouplingElement.
        """
        return self.couplingType

    def setCouplingType(self, value: Optional[CouplingElementEnum]) -> CouplingElement:
        """
        Describes the coupling type of this CouplingElement.

        A None value is a no-op and does not overwrite an existing couplingType.
        """
        if value is not None:
            self.couplingType = value
        return self

    def getEcuInstanceRef(self) -> Optional[RefType]:
        """
        Optional reference to the ECU where the Coupling Element is located.
        """
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value: Optional[RefType]) -> CouplingElement:
        """
        Optional reference to the ECU where the Coupling Element is located.

        A None value is a no-op and does not overwrite an existing ecuInstanceRef.
        """
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def addFirewallRuleRef(self, value: Optional[RefType]) -> CouplingElement:
        """
        Firewall rules defined in the context of a Coupling Element. Tags: atp.Status=candidate

        A None value is a no-op and does not append a firewallRuleRef.
        """
        if value is not None:
            self.firewallRuleRefs.append(value)
        return self

    def getFirewallRuleRefs(self) -> List[RefType]:
        """
        Firewall rules defined in the context of a Coupling Element. Tags: atp.Status=candidate
        """
        return self.firewallRuleRefs


class CouplingElementAbstractDetails(Identifiable, VariationPointCapable):
    """
    Collection of specific details for the CouplingElement.
    """

    # CouplingElementAbstractDetails method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.82, p.133
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (the spec table defines no Attribute rows; Base = ARObject, Identifiable, MultilanguageReferrable,
    #  Referrable → Identifiable is the most-derived model class. The XSD models the class as the
    #  xsd:group COUPLING-ELEMENT-ABSTRACT-DETAILS (AUTOSAR_00052.xsd l.23155, atp.Status="candidate")
    #  whose only child is VARIATION-POINT (atpVariation, xml.sequenceOffset=10000) — carried by the
    #  VariationPointCapable mixin (getVariationPoint/setVariationPoint have no spec rows,
    #  stereotype-inherent) and round-tripped through the shared readIdentifiable/writeIdentifiable
    #  helpers via the named readCouplingElementAbstractDetails/writeCouplingElementAbstractDetails
    #  dispatch level the concrete subclass calls)

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CouplingElementAbstractDetails:
            raise TypeError("CouplingElementAbstractDetails is an abstract class.")

        super().__init__(parent, short_name)


class CouplingElementSwitchDetails(CouplingElementAbstractDetails):
    """
    Collection of specific details for the CouplingElement of couplingType switch. Tags: atp.Status=candidate atp.recommendedPackage=SwitchStreamIdentificationTables
    """

    # CouplingElementSwitchDetails method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.83, p.133
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createFlowMetering                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFlowMeterings                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createStreamFilter                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStreamFilters                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createStreamGate                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStreamGates                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwitchStreamIdentification     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwitchStreamIdentifications       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createTrafficShaperGroup             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTrafficShaperGroups               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of Flow Metering Entries. Tags: atp.Status=candidate
        self.flowMeterings: List[SwitchFlowMeteringEntry] = []

        # Collection of Stream Filter Entries. Tags: atp.Status=candidate
        self.streamFilters: List[SwitchStreamFilterEntry] = []

        # Collection of Stream Gate Entries. Tags: atp.Status=candidate
        self.streamGates: List[SwitchStreamGateEntry] = []

        # Collection of switch stream identification entries. Tags: atp.Status=candidate
        self.switchStreamIdentifications: List[SwitchStreamIdentification] = []

        # Collection of Traffic Shaper Groups. Tags: atp.Status=candidate
        self.trafficShaperGroups: List[SwitchAsynchronousTrafficShaperGroupEntry] = []

    def createFlowMetering(self, short_name: str) -> SwitchFlowMeteringEntry:
        """
        Collection of Flow Metering Entries. Tags: atp.Status=candidate
        The existing element is returned when the short name already exists (no duplicate creation).
        """
        for entry in self.flowMeterings:
            if entry.getShortName() == short_name:
                return entry
        entry = SwitchFlowMeteringEntry(self, short_name)
        self.flowMeterings.append(entry)
        return entry

    def getFlowMeterings(self) -> List[SwitchFlowMeteringEntry]:
        """
        Collection of Flow Metering Entries. Tags: atp.Status=candidate
        """
        return self.flowMeterings

    def createStreamFilter(self, short_name: str) -> SwitchStreamFilterEntry:
        """
        Collection of Stream Filter Entries. Tags: atp.Status=candidate
        The existing element is returned when the short name already exists (no duplicate creation).
        """
        for entry in self.streamFilters:
            if entry.getShortName() == short_name:
                return entry
        entry = SwitchStreamFilterEntry(self, short_name)
        self.streamFilters.append(entry)
        return entry

    def getStreamFilters(self) -> List[SwitchStreamFilterEntry]:
        """
        Collection of Stream Filter Entries. Tags: atp.Status=candidate
        """
        return self.streamFilters

    def createStreamGate(self, short_name: str) -> SwitchStreamGateEntry:
        """
        Collection of Stream Gate Entries. Tags: atp.Status=candidate
        The existing element is returned when the short name already exists (no duplicate creation).
        """
        for entry in self.streamGates:
            if entry.getShortName() == short_name:
                return entry
        entry = SwitchStreamGateEntry(self, short_name)
        self.streamGates.append(entry)
        return entry

    def getStreamGates(self) -> List[SwitchStreamGateEntry]:
        """
        Collection of Stream Gate Entries. Tags: atp.Status=candidate
        """
        return self.streamGates

    def createSwitchStreamIdentification(self, short_name: str) -> SwitchStreamIdentification:
        """
        Collection of switch stream identification entries. Tags: atp.Status=candidate
        The existing element is returned when the short name already exists (no duplicate creation).
        """
        for entry in self.switchStreamIdentifications:
            if entry.getShortName() == short_name:
                return entry
        entry = SwitchStreamIdentification(self, short_name)
        self.switchStreamIdentifications.append(entry)
        return entry

    def getSwitchStreamIdentifications(self) -> List[SwitchStreamIdentification]:
        """
        Collection of switch stream identification entries. Tags: atp.Status=candidate
        """
        return self.switchStreamIdentifications

    def createTrafficShaperGroup(self, short_name: str) -> SwitchAsynchronousTrafficShaperGroupEntry:
        """
        Collection of Traffic Shaper Groups. Tags: atp.Status=candidate
        The existing element is returned when the short name already exists (no duplicate creation).
        """
        for entry in self.trafficShaperGroups:
            if entry.getShortName() == short_name:
                return entry
        entry = SwitchAsynchronousTrafficShaperGroupEntry(self, short_name)
        self.trafficShaperGroups.append(entry)
        return entry

    def getTrafficShaperGroups(self) -> List[SwitchAsynchronousTrafficShaperGroupEntry]:
        """
        Collection of Traffic Shaper Groups. Tags: atp.Status=candidate
        """
        return self.trafficShaperGroups


class SwitchAsynchronousTrafficShaperGroupEntry(Identifiable):
    """
    Defines an Asynchronous Traffic Shapter (ATS) Group for a switch. Tags: atp.Status=candidate
    """

    # SwitchAsynchronousTrafficShaperGroupEntry method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.96, p.142
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMaximumResidenceTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaximumResidenceTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the maximum duration limit for which frames can reside in a switch (in seconds). Tags: atp.Status=candidate
        self.maximumResidenceTime: Optional[PositiveInteger] = None

    def getMaximumResidenceTime(self) -> Optional[PositiveInteger]:
        """
        Defines the maximum duration limit for which frames can reside in a switch (in seconds). Tags: atp.Status=candidate
        """
        return self.maximumResidenceTime

    def setMaximumResidenceTime(self, value: Optional[PositiveInteger]) -> SwitchAsynchronousTrafficShaperGroupEntry:
        """
        Defines the maximum duration limit for which frames can reside in a switch (in seconds). Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing maximumResidenceTime.
        """
        if value is not None:
            self.maximumResidenceTime = value
        return self


class SwitchStreamGateEntry(Identifiable):
    """
    Defines a Asynchronous Traffic Shapter (ATS) Group for a switch. Tags: atp.Status=candidate
    """

    # SwitchStreamGateEntry method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.97, p.143
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInternalPriorityValue  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInternalPriorityValue  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Internal Priority Value (IPV), a priority value that determines the assigned traffic class. Tags: atp.Status=candidate
        self.internalPriorityValue: Optional[PositiveInteger] = None

    def getInternalPriorityValue(self) -> Optional[PositiveInteger]:
        """
        Internal Priority Value (IPV), a priority value that determines the assigned traffic class. Tags: atp.Status=candidate
        """
        return self.internalPriorityValue

    def setInternalPriorityValue(self, value: Optional[PositiveInteger]) -> SwitchStreamGateEntry:
        """
        Internal Priority Value (IPV), a priority value that determines the assigned traffic class. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing internalPriorityValue.
        """
        if value is not None:
            self.internalPriorityValue = value
        return self


class FlowMeteringColorModeEnum(AREnum):
    """
    Defines whether Flow Metering color-aware or color-blind mode is used. Tags: atp.Status=candidate
    """

    # FlowMeteringColorModeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.99, p.144
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on SwitchFlowMeteringEntry.colorMode
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Flow Metering color aware mode. Tags: atp.EnumerationLiteralIndex=1 atp.Status=candidate
    COLOR_AWARE = "COLOR-AWARE"

    # Flow Metering color blind mode. Tags: atp.EnumerationLiteralIndex=0 atp.Status=candidate
    COLOR_BLIND = "COLOR-BLIND"

    def __init__(self):
        super().__init__([FlowMeteringColorModeEnum.COLOR_AWARE, FlowMeteringColorModeEnum.COLOR_BLIND])


class SwitchFlowMeteringEntry(Identifiable):
    """
    Defines a Flow Metering Entry for a switch. Tags: atp.Status=candidate
    """

    # SwitchFlowMeteringEntry method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.98, p.143
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getColorMode                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setColorMode                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCommittedBurstSize        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommittedBurstSize        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCommittedInformationRate  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommittedInformationRate  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCouplingFlag              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCouplingFlag              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getExcessBurstSize           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setExcessBurstSize           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getExcessInformationRate     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setExcessInformationRate     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines whether color-aware or color-blind mode shall be used. Tags: atp.Status=candidate
        self.colorMode: Optional[FlowMeteringColorModeEnum] = None

        # Committed Burst Size (CBS) (accepted burst size in green token bucket). Tags: atp.Status=candidate
        self.committedBurstSize: Optional[PositiveInteger] = None

        # Committed Information Rate (CIR) (accepted rate in green token bucket) in bits per second. Tags: atp.Status=candidate
        self.committedInformationRate: Optional[PositiveInteger] = None

        # Coupling Flag that defines if unused "green" tokens in the first bucket are transferred to the second bucket as "yellow" tokens. Tags: atp.Status=candidate
        self.couplingFlag: Optional[Boolean] = None

        # Excess burst size (EBS) (accepted burst size in yellow token bucket). Tags: atp.Status=candidate
        self.excessBurstSize: Optional[PositiveInteger] = None

        # Excess Information Rate (EIR) (accepted rate in yellow token bucket) in bits per second. Tags: atp.Status=candidate
        self.excessInformationRate: Optional[PositiveInteger] = None

    def getColorMode(self) -> Optional[FlowMeteringColorModeEnum]:
        """
        Defines whether color-aware or color-blind mode shall be used. Tags: atp.Status=candidate
        """
        return self.colorMode

    def setColorMode(self, value: Optional[FlowMeteringColorModeEnum]) -> SwitchFlowMeteringEntry:
        """
        Defines whether color-aware or color-blind mode shall be used. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing colorMode.
        """
        if value is not None:
            self.colorMode = value
        return self

    def getCommittedBurstSize(self) -> Optional[PositiveInteger]:
        """
        Committed Burst Size (CBS) (accepted burst size in green token bucket). Tags: atp.Status=candidate
        """
        return self.committedBurstSize

    def setCommittedBurstSize(self, value: Optional[PositiveInteger]) -> SwitchFlowMeteringEntry:
        """
        Committed Burst Size (CBS) (accepted burst size in green token bucket). Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing committedBurstSize.
        """
        if value is not None:
            self.committedBurstSize = value
        return self

    def getCommittedInformationRate(self) -> Optional[PositiveInteger]:
        """
        Committed Information Rate (CIR) (accepted rate in green token bucket) in bits per second. Tags: atp.Status=candidate
        """
        return self.committedInformationRate

    def setCommittedInformationRate(self, value: Optional[PositiveInteger]) -> SwitchFlowMeteringEntry:
        """
        Committed Information Rate (CIR) (accepted rate in green token bucket) in bits per second. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing committedInformationRate.
        """
        if value is not None:
            self.committedInformationRate = value
        return self

    def getCouplingFlag(self) -> Optional[Boolean]:
        """
        Coupling Flag that defines if unused "green" tokens in the first bucket are transferred to the second bucket as "yellow" tokens. Tags: atp.Status=candidate
        """
        return self.couplingFlag

    def setCouplingFlag(self, value: Optional[Boolean]) -> SwitchFlowMeteringEntry:
        """
        Coupling Flag that defines if unused "green" tokens in the first bucket are transferred to the second bucket as "yellow" tokens. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing couplingFlag.
        """
        if value is not None:
            self.couplingFlag = value
        return self

    def getExcessBurstSize(self) -> Optional[PositiveInteger]:
        """
        Excess burst size (EBS) (accepted burst size in yellow token bucket). Tags: atp.Status=candidate
        """
        return self.excessBurstSize

    def setExcessBurstSize(self, value: Optional[PositiveInteger]) -> SwitchFlowMeteringEntry:
        """
        Excess burst size (EBS) (accepted burst size in yellow token bucket). Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing excessBurstSize.
        """
        if value is not None:
            self.excessBurstSize = value
        return self

    def getExcessInformationRate(self) -> Optional[PositiveInteger]:
        """
        Excess Information Rate (EIR) (accepted rate in yellow token bucket) in bits per second. Tags: atp.Status=candidate
        """
        return self.excessInformationRate

    def setExcessInformationRate(self, value: Optional[PositiveInteger]) -> SwitchFlowMeteringEntry:
        """
        Excess Information Rate (EIR) (accepted rate in yellow token bucket) in bits per second. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing excessInformationRate.
        """
        if value is not None:
            self.excessInformationRate = value
        return self


class SwitchStreamIdentification(Identifiable):
    """
    SwitchStreamIdentification Tags: atp.Status=candidate
    """

    # SwitchStreamIdentification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.84, p.135
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addEgressPortRef                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEgressPortRefs                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getFilterActionBlockSource              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFilterActionBlockSource              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createFilterActionDestPortModification  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFilterActionDestPortModification     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getFilterActionDropFrame                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFilterActionDropFrame                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFilterActionVlanModification         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFilterActionVlanModification         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addIngressPortRef                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIngressPortRefs                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createStreamFilterRule                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStreamFilterRule                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the CouplingPort to be taken into account as the egress role for this SwitchStreamIdentification. Tags: atp.Status=candidate
        self.egressPortRefs: List[RefType] = []

        # Enables Blocking all frames from the MAC address. Tags: atp.Status=candidate
        self.filterActionBlockSource: Optional[Boolean] = None

        # Defines the action to modify the destination port(s) determined by the frame forwarding process for an particular Ethernet frame. Tags: atp.Status=candidate
        self.filterActionDestPortModification: Optional[SwitchStreamFilterActionDestPortModification] = None

        # Enables Drop Frame action. Tags: atp.Status=candidate
        self.filterActionDropFrame: Optional[Boolean] = None

        # Defines the action to modify the VLAN-ID within a VLAN tag of an Ethernet frame. Tags: atp.Status=candidate
        self.filterActionVlanModification: Optional[PositiveInteger] = None

        # Reference to the CouplingPort to be taken into account as the ingress role for this SwitchStreamIdentification. Tags: atp.Status=candidate
        self.ingressPortRefs: List[RefType] = []

        # Definition of a stream filter rule for this SwitchStream Identification. Tags: atp.Status=candidate
        self.streamFilterRule: Optional[SwitchStreamFilterRule] = None

    def addEgressPortRef(self, value: Optional[RefType]) -> SwitchStreamIdentification:
        """
        Reference to the CouplingPort to be taken into account as the egress role for this SwitchStreamIdentification. Tags: atp.Status=candidate

        A None value is a no-op and does not append a egressPortRef.
        """
        if value is not None:
            self.egressPortRefs.append(value)
        return self

    def getEgressPortRefs(self) -> List[RefType]:
        """
        Reference to the CouplingPort to be taken into account as the egress role for this SwitchStreamIdentification. Tags: atp.Status=candidate
        """
        return self.egressPortRefs

    def getFilterActionBlockSource(self) -> Optional[Boolean]:
        """
        Enables Blocking all frames from the MAC address. Tags: atp.Status=candidate
        """
        return self.filterActionBlockSource

    def setFilterActionBlockSource(self, value: Optional[Boolean]) -> SwitchStreamIdentification:
        """
        Enables Blocking all frames from the MAC address. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing filterActionBlockSource.
        """
        if value is not None:
            self.filterActionBlockSource = value
        return self

    def createFilterActionDestPortModification(self, short_name: str) -> SwitchStreamFilterActionDestPortModification:
        """
        Defines the action to modify the destination port(s) determined by the frame forwarding process for an particular Ethernet frame. Tags: atp.Status=candidate
        The existing element is returned when the short name already exists (no duplicate creation).
        """
        if self.filterActionDestPortModification is None or self.filterActionDestPortModification.getShortName() != short_name:
            self.filterActionDestPortModification = SwitchStreamFilterActionDestPortModification(self, short_name)
        return self.filterActionDestPortModification

    def getFilterActionDestPortModification(self) -> Optional[SwitchStreamFilterActionDestPortModification]:
        """
        Defines the action to modify the destination port(s) determined by the frame forwarding process for an particular Ethernet frame. Tags: atp.Status=candidate
        """
        return self.filterActionDestPortModification

    def getFilterActionDropFrame(self) -> Optional[Boolean]:
        """
        Enables Drop Frame action. Tags: atp.Status=candidate
        """
        return self.filterActionDropFrame

    def setFilterActionDropFrame(self, value: Optional[Boolean]) -> SwitchStreamIdentification:
        """
        Enables Drop Frame action. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing filterActionDropFrame.
        """
        if value is not None:
            self.filterActionDropFrame = value
        return self

    def getFilterActionVlanModification(self) -> Optional[PositiveInteger]:
        """
        Defines the action to modify the VLAN-ID within a VLAN tag of an Ethernet frame. Tags: atp.Status=candidate
        """
        return self.filterActionVlanModification

    def setFilterActionVlanModification(self, value: Optional[PositiveInteger]) -> SwitchStreamIdentification:
        """
        Defines the action to modify the VLAN-ID within a VLAN tag of an Ethernet frame. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing filterActionVlanModification.
        """
        if value is not None:
            self.filterActionVlanModification = value
        return self

    def addIngressPortRef(self, value: Optional[RefType]) -> SwitchStreamIdentification:
        """
        Reference to the CouplingPort to be taken into account as the ingress role for this SwitchStreamIdentification. Tags: atp.Status=candidate

        A None value is a no-op and does not append a ingressPortRef.
        """
        if value is not None:
            self.ingressPortRefs.append(value)
        return self

    def getIngressPortRefs(self) -> List[RefType]:
        """
        Reference to the CouplingPort to be taken into account as the ingress role for this SwitchStreamIdentification. Tags: atp.Status=candidate
        """
        return self.ingressPortRefs

    def createStreamFilterRule(self, short_name: str) -> SwitchStreamFilterRule:
        """
        Definition of a stream filter rule for this SwitchStream Identification. Tags: atp.Status=candidate
        The existing element is returned when the short name already exists (no duplicate creation).
        """
        if self.streamFilterRule is None or self.streamFilterRule.getShortName() != short_name:
            self.streamFilterRule = SwitchStreamFilterRule(self, short_name)
        return self.streamFilterRule

    def getStreamFilterRule(self) -> Optional[SwitchStreamFilterRule]:
        """
        Definition of a stream filter rule for this SwitchStream Identification. Tags: atp.Status=candidate
        """
        return self.streamFilterRule


class SwitchStreamFilterRule(Identifiable):
    """
    SwitchStreamIdentification Tags: atp.Status=candidate
    """

    # SwitchStreamFilterRule method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.85, p.136
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataLinkLayerRule  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataLinkLayerRule  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIeee1722TpRule     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIeee1722TpRule     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpTpRule           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpTpRule           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Definition of a filter rule on the data link layer. Tags: atp.Status=candidate
        self.dataLinkLayerRule: Optional[StreamFilterRuleDataLinkLayer] = None

        # Definition of a filter rule for IEEE1722Tp. Tags: atp.Status=candidate
        self.ieee1722TpRule: Optional[StreamFilterIEEE1722Tp] = None

        # Definition of a filter rule IP and TP. Tags: atp.Status=candidate
        self.ipTpRule: Optional[StreamFilterRuleIpTp] = None

    def getDataLinkLayerRule(self) -> Optional[StreamFilterRuleDataLinkLayer]:
        """
        Definition of a filter rule on the data link layer. Tags: atp.Status=candidate
        """
        return self.dataLinkLayerRule

    def setDataLinkLayerRule(self, value: Optional[StreamFilterRuleDataLinkLayer]) -> SwitchStreamFilterRule:
        """
        Definition of a filter rule on the data link layer. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing dataLinkLayerRule.
        """
        if value is not None:
            self.dataLinkLayerRule = value
        return self

    def getIeee1722TpRule(self) -> Optional[StreamFilterIEEE1722Tp]:
        """
        Definition of a filter rule for IEEE1722Tp. Tags: atp.Status=candidate
        """
        return self.ieee1722TpRule

    def setIeee1722TpRule(self, value: Optional[StreamFilterIEEE1722Tp]) -> SwitchStreamFilterRule:
        """
        Definition of a filter rule for IEEE1722Tp. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ieee1722TpRule.
        """
        if value is not None:
            self.ieee1722TpRule = value
        return self

    def getIpTpRule(self) -> Optional[StreamFilterRuleIpTp]:
        """
        Definition of a filter rule IP and TP. Tags: atp.Status=candidate
        """
        return self.ipTpRule

    def setIpTpRule(self, value: Optional[StreamFilterRuleIpTp]) -> SwitchStreamFilterRule:
        """
        Definition of a filter rule IP and TP. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ipTpRule.
        """
        if value is not None:
            self.ipTpRule = value
        return self


class SwitchStreamFilterActionPortModificationEnum(AREnum):
    """
    Definition how the SwitchStreamFilterActionPortModification is applied. Tags: atp.Status=candidate
    """

    # SwitchStreamFilterActionPortModificationEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.94, p.140
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on SwitchStreamFilterActionDestPortModification.modification (queued next; no token map — XSD facets EXTEND/OVERWRITE are the serialized form)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Extend the egress destination of an Ethernet frame. Tags: atp.EnumerationLiteralIndex=0 atp.Status=candidate
    EXTEND = "EXTEND"

    # Overwrite the egress destination of an Ethernet frame. Tags: atp.EnumerationLiteralIndex=1 atp.Status=candidate
    OVERWRITE = "OVERWRITE"

    def __init__(self):
        super().__init__([SwitchStreamFilterActionPortModificationEnum.EXTEND, SwitchStreamFilterActionPortModificationEnum.OVERWRITE])


class SwitchStreamFilterActionDestPortModification(Identifiable):
    """
    Defines the action to modify the destination port(s) determined by the frame forwarding process for an particular Ethernet frame. Either the egress destination of an Ethernet frame is extended or overwritten. Tags: atp.Status=candidate
    """

    # SwitchStreamFilterActionDestPortModification method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.93, p.140
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addEgressPortRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEgressPortRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getModification    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setModification    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the egress ports used as the target of the filter action to modify the egress port. Tags: atp.Status=candidate
        self.egressPortRefs: List[RefType] = []

        # Defines the method to modify the egress destination. Either overwrite or extend the egress destination. Tags: atp.Status=candidate
        self.modification: Optional[SwitchStreamFilterActionPortModificationEnum] = None

    def addEgressPortRef(self, value: Optional[RefType]) -> SwitchStreamFilterActionDestPortModification:
        """
        Reference to the egress ports used as the target of the filter action to modify the egress port. Tags: atp.Status=candidate

        A None value is a no-op and does not append a egressPortRef.
        """
        if value is not None:
            self.egressPortRefs.append(value)
        return self

    def getEgressPortRefs(self) -> List[RefType]:
        """
        Reference to the egress ports used as the target of the filter action to modify the egress port. Tags: atp.Status=candidate
        """
        return self.egressPortRefs

    def getModification(self) -> Optional[SwitchStreamFilterActionPortModificationEnum]:
        """
        Defines the method to modify the egress destination. Either overwrite or extend the egress destination. Tags: atp.Status=candidate
        """
        return self.modification

    def setModification(self, value: Optional[SwitchStreamFilterActionPortModificationEnum]) -> SwitchStreamFilterActionDestPortModification:
        """
        Defines the method to modify the egress destination. Either overwrite or extend the egress destination. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing modification.
        """
        if value is not None:
            self.modification = value
        return self


class SwitchStreamFilterEntry(Identifiable):
    """
    Defines a Stream Filter Entry. Tags: atp.Status=candidate
    """

    # SwitchStreamFilterEntry method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.95, p.142
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addStreamIdentificationHandleRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAsynchronousTrafficShaperRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAsynchronousTrafficShaperRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFilterPriority                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFilterPriority                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFlowMeteringRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFlowMeteringRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaxSduSize                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxSduSize                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStreamGateRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStreamGateRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStreamIdentificationHandleRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getStreamIdentificationWildcard   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStreamIdentificationWildcard   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the Asynchronous Traffic Shaper (ATS). Tags: atp.Status=candidate
        self.asynchronousTrafficShaperRef: Optional[RefType] = None

        # Defines the Priority of this Stream Filter Entry. Tags: atp.Status=candidate
        self.filterPriority: Optional[PositiveInteger] = None

        # Reference to a Flow Metering Entry. Tags: atp.Status=candidate
        self.flowMeteringRef: Optional[RefType] = None

        # Defines the maximum SDU size (size of an Ethernet package) which is acceptable to be processed by the Ethernet switch. Tags: atp.Status=candidate
        self.maxSduSize: Optional[PositiveInteger] = None

        # Reference to a Stream Gate Entry. Tags: atp.Status=candidate
        self.streamGateRef: Optional[RefType] = None

        # Reference to the SwitchStreamIdentifications this Stream FilterEntry applies to. Tags: atp.Status=candidate
        self.streamIdentificationHandleRefs: List[RefType] = []

        # Defines whether this Stream Filter Entry includes the wildcard for SwitchStreamIdentification. Tags: atp.Status=candidate
        self.streamIdentificationWildcard: Optional[Boolean] = None

    def addStreamIdentificationHandleRef(self, value: Optional[RefType]) -> SwitchStreamFilterEntry:
        """
        Reference to the SwitchStreamIdentifications this Stream FilterEntry applies to. Tags: atp.Status=candidate

        A None value is a no-op and does not append a streamIdentificationHandleRef.
        """
        if value is not None:
            self.streamIdentificationHandleRefs.append(value)
        return self

    def getAsynchronousTrafficShaperRef(self) -> Optional[RefType]:
        """
        Reference to the Asynchronous Traffic Shaper (ATS). Tags: atp.Status=candidate
        """
        return self.asynchronousTrafficShaperRef

    def setAsynchronousTrafficShaperRef(self, value: Optional[RefType]) -> SwitchStreamFilterEntry:
        """
        Reference to the Asynchronous Traffic Shaper (ATS). Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing asynchronousTrafficShaperRef.
        """
        if value is not None:
            self.asynchronousTrafficShaperRef = value
        return self

    def getFilterPriority(self) -> Optional[PositiveInteger]:
        """
        Defines the Priority of this Stream Filter Entry. Tags: atp.Status=candidate
        """
        return self.filterPriority

    def setFilterPriority(self, value: Optional[PositiveInteger]) -> SwitchStreamFilterEntry:
        """
        Defines the Priority of this Stream Filter Entry. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing filterPriority.
        """
        if value is not None:
            self.filterPriority = value
        return self

    def getFlowMeteringRef(self) -> Optional[RefType]:
        """
        Reference to a Flow Metering Entry. Tags: atp.Status=candidate
        """
        return self.flowMeteringRef

    def setFlowMeteringRef(self, value: Optional[RefType]) -> SwitchStreamFilterEntry:
        """
        Reference to a Flow Metering Entry. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing flowMeteringRef.
        """
        if value is not None:
            self.flowMeteringRef = value
        return self

    def getMaxSduSize(self) -> Optional[PositiveInteger]:
        """
        Defines the maximum SDU size (size of an Ethernet package) which is acceptable to be processed by the Ethernet switch. Tags: atp.Status=candidate
        """
        return self.maxSduSize

    def setMaxSduSize(self, value: Optional[PositiveInteger]) -> SwitchStreamFilterEntry:
        """
        Defines the maximum SDU size (size of an Ethernet package) which is acceptable to be processed by the Ethernet switch. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing maxSduSize.
        """
        if value is not None:
            self.maxSduSize = value
        return self

    def getStreamGateRef(self) -> Optional[RefType]:
        """
        Reference to a Stream Gate Entry. Tags: atp.Status=candidate
        """
        return self.streamGateRef

    def setStreamGateRef(self, value: Optional[RefType]) -> SwitchStreamFilterEntry:
        """
        Reference to a Stream Gate Entry. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing streamGateRef.
        """
        if value is not None:
            self.streamGateRef = value
        return self

    def getStreamIdentificationHandleRefs(self) -> List[RefType]:
        """
        Reference to the SwitchStreamIdentifications this Stream FilterEntry applies to. Tags: atp.Status=candidate
        """
        return self.streamIdentificationHandleRefs

    def getStreamIdentificationWildcard(self) -> Optional[Boolean]:
        """
        Defines whether this Stream Filter Entry includes the wildcard for SwitchStreamIdentification. Tags: atp.Status=candidate
        """
        return self.streamIdentificationWildcard

    def setStreamIdentificationWildcard(self, value: Optional[Boolean]) -> SwitchStreamFilterEntry:
        """
        Defines whether this Stream Filter Entry includes the wildcard for SwitchStreamIdentification. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing streamIdentificationWildcard.
        """
        if value is not None:
            self.streamIdentificationWildcard = value
        return self


class StreamFilterMACAddress(ARObject):
    """
    Configuration of filter rules on the DataLink layer Tags: atp.Status=candidate
    """

    # StreamFilterMACAddress method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.87, p.137
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMacAddress        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMacAddress        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMacAddressMask    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMacAddressMask    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Filter to match packets with the MAC address. Tags: atp.Status=candidate
        self.macAddress: Optional[MacAddressString] = None

        # Filter to match packets with the MAC address range. Tags: atp.Status=candidate
        self.macAddressMask: Optional[MacAddressString] = None

    def getMacAddress(self) -> Optional[MacAddressString]:
        """
        Filter to match packets with the MAC address. Tags: atp.Status=candidate
        """
        return self.macAddress

    def setMacAddress(self, value: Optional[MacAddressString]) -> StreamFilterMACAddress:
        """
        Filter to match packets with the MAC address. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing macAddress.
        """
        if value is not None:
            self.macAddress = value
        return self

    def getMacAddressMask(self) -> Optional[MacAddressString]:
        """
        Filter to match packets with the MAC address range. Tags: atp.Status=candidate
        """
        return self.macAddressMask

    def setMacAddressMask(self, value: Optional[MacAddressString]) -> StreamFilterMACAddress:
        """
        Filter to match packets with the MAC address range. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing macAddressMask.
        """
        if value is not None:
            self.macAddressMask = value
        return self


class StreamFilterRuleDataLinkLayer(ARObject):
    """
    Configuration of filter rules on the DataLink layer Tags: atp.Status=candidate
    """

    # StreamFilterRuleDataLinkLayer method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.86, p.137
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDestinationMacAddress [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestinationMacAddress [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEtherType             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEtherType             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceMacAddress      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceMacAddress      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlanId                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVlanId                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlanPriority          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVlanPriority          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Filter to match packets with the destination MAC address/ mask. Tags: atp.Status=candidate
        self.destinationMacAddress: Optional[StreamFilterMACAddress] = None

        # Filter to match packets based on the EtherType field in the Ethernet frame. Tags: atp.Status=candidate
        self.etherType: Optional[PositiveInteger] = None

        # Filter to match packets with the source MAC address/ mask. Tags: atp.Status=candidate
        self.sourceMacAddress: Optional[StreamFilterMACAddress] = None

        # Filter of packets with a VlanId. Tags: atp.Status=candidate
        self.vlanId: Optional[PositiveInteger] = None

        # Filter of packets with a Vlan priority. Tags: atp.Status=candidate
        self.vlanPriority: Optional[PositiveInteger] = None

    def getDestinationMacAddress(self) -> Optional[StreamFilterMACAddress]:
        """
        Filter to match packets with the destination MAC address/ mask. Tags: atp.Status=candidate
        """
        return self.destinationMacAddress

    def setDestinationMacAddress(self, value: Optional[StreamFilterMACAddress]) -> StreamFilterRuleDataLinkLayer:
        """
        Filter to match packets with the destination MAC address/ mask. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing destinationMacAddress.
        """
        if value is not None:
            self.destinationMacAddress = value
        return self

    def getEtherType(self) -> Optional[PositiveInteger]:
        """
        Filter to match packets based on the EtherType field in the Ethernet frame. Tags: atp.Status=candidate
        """
        return self.etherType

    def setEtherType(self, value: Optional[PositiveInteger]) -> StreamFilterRuleDataLinkLayer:
        """
        Filter to match packets based on the EtherType field in the Ethernet frame. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing etherType.
        """
        if value is not None:
            self.etherType = value
        return self

    def getSourceMacAddress(self) -> Optional[StreamFilterMACAddress]:
        """
        Filter to match packets with the source MAC address/ mask. Tags: atp.Status=candidate
        """
        return self.sourceMacAddress

    def setSourceMacAddress(self, value: Optional[StreamFilterMACAddress]) -> StreamFilterRuleDataLinkLayer:
        """
        Filter to match packets with the source MAC address/ mask. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing sourceMacAddress.
        """
        if value is not None:
            self.sourceMacAddress = value
        return self

    def getVlanId(self) -> Optional[PositiveInteger]:
        """
        Filter of packets with a VlanId. Tags: atp.Status=candidate
        """
        return self.vlanId

    def setVlanId(self, value: Optional[PositiveInteger]) -> StreamFilterRuleDataLinkLayer:
        """
        Filter of packets with a VlanId. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing vlanId.
        """
        if value is not None:
            self.vlanId = value
        return self

    def getVlanPriority(self) -> Optional[PositiveInteger]:
        """
        Filter of packets with a Vlan priority. Tags: atp.Status=candidate
        """
        return self.vlanPriority

    def setVlanPriority(self, value: Optional[PositiveInteger]) -> StreamFilterRuleDataLinkLayer:
        """
        Filter of packets with a Vlan priority. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing vlanPriority.
        """
        if value is not None:
            self.vlanPriority = value
        return self


class StreamFilterRuleIpTp(ARObject):
    """
    Configuration of filter rules for IP and TP. Tags: atp.Status=candidate
    """

    # StreamFilterRuleIpTp method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.88, p.138
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDestinationIpv4Address  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestinationIpv4Address  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDestinationIpv6Address  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestinationIpv6Address  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addDestinationPort         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDestinationPorts        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSourceIpv4Address       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceIpv4Address       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceIpv6Address       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceIpv6Address       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSourcePort              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourcePorts             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Filter to match packets with the destination IPv4 address range. Tags: atp.Status=candidate
        self.destinationIpv4Address: Optional[StreamFilterIpv4Address] = None

        # Filter to match packets with the destination IPv6 address range. Tags: atp.Status=candidate
        self.destinationIpv6Address: Optional[StreamFilterIpv6Address] = None

        # Filter to match packets with the set of destination UDP/TCP port ranges. Tags: atp.Status=candidate
        self.destinationPorts: List[StreamFilterPortRange] = []

        # Filter to match packets with the source IPv4 address range. Tags: atp.Status=candidate
        self.sourceIpv4Address: Optional[StreamFilterIpv4Address] = None

        # Filter to match packets with the source IPv6 address range. Tags: atp.Status=candidate
        self.sourceIpv6Address: Optional[StreamFilterIpv6Address] = None

        # Filter to match packets with the set of source UDP/TCP port ranges. Tags: atp.Status=candidate
        self.sourcePorts: List[StreamFilterPortRange] = []

    def getDestinationIpv4Address(self) -> Optional[StreamFilterIpv4Address]:
        """
        Filter to match packets with the destination IPv4 address range. Tags: atp.Status=candidate
        """
        return self.destinationIpv4Address

    def setDestinationIpv4Address(self, value: Optional[StreamFilterIpv4Address]) -> StreamFilterRuleIpTp:
        """
        Filter to match packets with the destination IPv4 address range. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing destinationIpv4Address.
        """
        if value is not None:
            self.destinationIpv4Address = value
        return self

    def getDestinationIpv6Address(self) -> Optional[StreamFilterIpv6Address]:
        """
        Filter to match packets with the destination IPv6 address range. Tags: atp.Status=candidate
        """
        return self.destinationIpv6Address

    def setDestinationIpv6Address(self, value: Optional[StreamFilterIpv6Address]) -> StreamFilterRuleIpTp:
        """
        Filter to match packets with the destination IPv6 address range. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing destinationIpv6Address.
        """
        if value is not None:
            self.destinationIpv6Address = value
        return self

    def addDestinationPort(self, value: Optional[StreamFilterPortRange]) -> StreamFilterRuleIpTp:
        """
        Filter to match packets with the set of destination UDP/TCP port ranges. Tags: atp.Status=candidate

        A None value is a no-op and does not add to destinationPorts.
        """
        if value is not None:
            self.destinationPorts.append(value)
        return self

    def getDestinationPorts(self) -> List[StreamFilterPortRange]:
        """
        Filter to match packets with the set of destination UDP/TCP port ranges. Tags: atp.Status=candidate
        """
        return self.destinationPorts

    def getSourceIpv4Address(self) -> Optional[StreamFilterIpv4Address]:
        """
        Filter to match packets with the source IPv4 address range. Tags: atp.Status=candidate
        """
        return self.sourceIpv4Address

    def setSourceIpv4Address(self, value: Optional[StreamFilterIpv4Address]) -> StreamFilterRuleIpTp:
        """
        Filter to match packets with the source IPv4 address range. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing sourceIpv4Address.
        """
        if value is not None:
            self.sourceIpv4Address = value
        return self

    def getSourceIpv6Address(self) -> Optional[StreamFilterIpv6Address]:
        """
        Filter to match packets with the source IPv6 address range. Tags: atp.Status=candidate
        """
        return self.sourceIpv6Address

    def setSourceIpv6Address(self, value: Optional[StreamFilterIpv6Address]) -> StreamFilterRuleIpTp:
        """
        Filter to match packets with the source IPv6 address range. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing sourceIpv6Address.
        """
        if value is not None:
            self.sourceIpv6Address = value
        return self

    def addSourcePort(self, value: Optional[StreamFilterPortRange]) -> StreamFilterRuleIpTp:
        """
        Filter to match packets with the set of source UDP/TCP port ranges. Tags: atp.Status=candidate

        A None value is a no-op and does not add to sourcePorts.
        """
        if value is not None:
            self.sourcePorts.append(value)
        return self

    def getSourcePorts(self) -> List[StreamFilterPortRange]:
        """
        Filter to match packets with the set of source UDP/TCP port ranges. Tags: atp.Status=candidate
        """
        return self.sourcePorts


class StreamFilterIpv4Address(ARObject):
    """
    IPv4 address range definition. Tags: atp.Status=candidate
    """

    # StreamFilterIpv4Address method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.89, p.138
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIpv4Address       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv4Address       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpv4AddressMask   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv4AddressMask   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Filter to match packets with the IPv4 address. Tags: atp.Status=candidate
        self.ipv4Address: Optional[Ip4AddressString] = None

        # Filter to match packets with the IPv4 address range. Tags: atp.Status=candidate
        self.ipv4AddressMask: Optional[Ip4AddressString] = None

    def getIpv4Address(self) -> Optional[Ip4AddressString]:
        """
        Filter to match packets with the IPv4 address. Tags: atp.Status=candidate
        """
        return self.ipv4Address

    def setIpv4Address(self, value: Optional[Ip4AddressString]) -> StreamFilterIpv4Address:
        """
        Filter to match packets with the IPv4 address. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ipv4Address.
        """
        if value is not None:
            self.ipv4Address = value
        return self

    def getIpv4AddressMask(self) -> Optional[Ip4AddressString]:
        """
        Filter to match packets with the IPv4 address range. Tags: atp.Status=candidate
        """
        return self.ipv4AddressMask

    def setIpv4AddressMask(self, value: Optional[Ip4AddressString]) -> StreamFilterIpv4Address:
        """
        Filter to match packets with the IPv4 address range. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ipv4AddressMask.
        """
        if value is not None:
            self.ipv4AddressMask = value
        return self


class StreamFilterIpv6Address(ARObject):
    """
    IPv6 address range definition. Tags: atp.Status=candidate
    """

    # StreamFilterIpv6Address method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.90, p.138
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIpv6Address       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv6Address       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpv6AddressMask   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv6AddressMask   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Filter to match packets with the IPv6 address. Tags: atp.Status=candidate
        self.ipv6Address: Optional[Ip6AddressString] = None

        # Filter to match packets with the IPv6 address range. Tags: atp.Status=candidate
        self.ipv6AddressMask: Optional[Ip6AddressString] = None

    def getIpv6Address(self) -> Optional[Ip6AddressString]:
        """
        Filter to match packets with the IPv6 address. Tags: atp.Status=candidate
        """
        return self.ipv6Address

    def setIpv6Address(self, value: Optional[Ip6AddressString]) -> StreamFilterIpv6Address:
        """
        Filter to match packets with the IPv6 address. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ipv6Address.
        """
        if value is not None:
            self.ipv6Address = value
        return self

    def getIpv6AddressMask(self) -> Optional[Ip6AddressString]:
        """
        Filter to match packets with the IPv6 address range. Tags: atp.Status=candidate
        """
        return self.ipv6AddressMask

    def setIpv6AddressMask(self, value: Optional[Ip6AddressString]) -> StreamFilterIpv6Address:
        """
        Filter to match packets with the IPv6 address range. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing ipv6AddressMask.
        """
        if value is not None:
            self.ipv6AddressMask = value
        return self


class StreamFilterPortRange(ARObject):
    """
    Configuration of filter rules for IP and TP. Tags: atp.Status=candidate
    """

    # StreamFilterPortRange method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.91, p.139
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMax      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMax      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMin      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMin      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Filter to match packets with the maximum UDP/TCP port number. Tags: atp.Status=candidate
        self.max: Optional[PositiveInteger] = None

        # Filter to match packets with the minimum UDP/TCP port number. Tags: atp.Status=candidate
        self.min: Optional[PositiveInteger] = None

    def getMax(self) -> Optional[PositiveInteger]:
        """
        Filter to match packets with the maximum UDP/TCP port number. Tags: atp.Status=candidate
        """
        return self.max

    def setMax(self, value: Optional[PositiveInteger]) -> StreamFilterPortRange:
        """
        Filter to match packets with the maximum UDP/TCP port number. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing max.
        """
        if value is not None:
            self.max = value
        return self

    def getMin(self) -> Optional[PositiveInteger]:
        """
        Filter to match packets with the minimum UDP/TCP port number. Tags: atp.Status=candidate
        """
        return self.min

    def setMin(self, value: Optional[PositiveInteger]) -> StreamFilterPortRange:
        """
        Filter to match packets with the minimum UDP/TCP port number. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing min.
        """
        if value is not None:
            self.min = value
        return self


class StreamFilterIEEE1722Tp(ARObject):
    """
    Configuration of filter rules for IP and TP. Tags: atp.Status=candidate
    """

    # StreamFilterIEEE1722Tp method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.92, p.139
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getStreamId  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStreamId  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Filter to match IEEE1722Tp packets with the stream Id number. Defined as 64bit stream id. Tags: atp.Status=candidate
        self.streamId: Optional[PositiveUnlimitedInteger] = None

    def getStreamId(self) -> Optional[PositiveUnlimitedInteger]:
        """
        Filter to match IEEE1722Tp packets with the stream Id number. Defined as 64bit stream id. Tags: atp.Status=candidate
        """
        return self.streamId

    def setStreamId(self, value: Optional[PositiveUnlimitedInteger]) -> StreamFilterIEEE1722Tp:
        """
        Filter to match IEEE1722Tp packets with the stream Id number. Defined as 64bit stream id. Tags: atp.Status=candidate

        A None value is a no-op and does not overwrite an existing streamId.
        """
        if value is not None:
            self.streamId = value
        return self


class CouplingPortStructuralElement(Identifiable, ABC):
    """
    General class to define structural elements a CouplingPort may consist of.
    """

    # CouplingPortStructuralElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.64, p.122
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CouplingPortStructuralElement:
            raise TypeError("CouplingPortStructuralElement is an abstract class.")

        super().__init__(parent, short_name)


class CouplingPortAbstractShaper(Identifiable, ABC):
    """
    Abstract class for the definition of coupling port shapers.
    """

    # CouplingPortAbstractShaper method parity checklist:
    # Spec: AUTOSAR_00052.xsd line 23449 (xsd:group COUPLING-PORT-ABSTRACT-SHAPER, atp.Status="candidate"; XSD-only, no Class/Enumeration table in the repo corpora)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (the XSD models this abstract class as the empty xsd:group COUPLING-PORT-ABSTRACT-SHAPER,
    #  consumed by the CouplingPortFifo.shaper choice (xsd L23763:
    #  COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER | COUPLING-PORT-CREDIT-BASED-SHAPER); the reader and
    #  writer dispatch that choice by comparing the element name against those two XSD tags)

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CouplingPortAbstractShaper:
            raise TypeError("CouplingPortAbstractShaper is an abstract class.")

        super().__init__(parent, short_name)


class CouplingPortAsynchronousTrafficShaper(CouplingPortAbstractShaper):
    """
    Defines an Asynchronous Traffic Shaper (ATS) for the CouplingPort egress structure.
    """

    # CouplingPortAsynchronousTrafficShaper method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.36, p.2012
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommittedBurstSize        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommittedBurstSize        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCommittedInformationRate  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommittedInformationRate  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTrafficShaperGroupRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTrafficShaperGroupRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (concrete child of the abstract CouplingPortAbstractShaper: the XSD models the polymorphic
    #  CouplingPortFifo.shaper choice via this class's xsd:group — the reader and writer dispatch that
    #  choice by matching the element name against this class's XSD tag)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Maximum token capacity of the token bucket in bit.
        self.committedBurstSize: Optional[PositiveInteger] = None

        # Defines the rate at which the token bucket is refilled with tokens in bit per second.
        self.committedInformationRate: Optional[PositiveInteger] = None

        # Reference to the Traffic Shaper Group this Asynchronous Traffic Shaper is part of.
        self.trafficShaperGroupRef: Optional[RefType] = None

    def getCommittedBurstSize(self) -> Optional[PositiveInteger]:
        """
        Maximum token capacity of the token bucket in bit.
        """
        return self.committedBurstSize

    def setCommittedBurstSize(self, value: Optional[PositiveInteger]) -> CouplingPortAsynchronousTrafficShaper:
        """
        Maximum token capacity of the token bucket in bit.
        A None value is a no-op and does not overwrite an existing committedBurstSize.
        """
        if value is not None:
            self.committedBurstSize = value
        return self

    def getCommittedInformationRate(self) -> Optional[PositiveInteger]:
        """
        Defines the rate at which the token bucket is refilled with tokens in bit per second.
        """
        return self.committedInformationRate

    def setCommittedInformationRate(self, value: Optional[PositiveInteger]) -> CouplingPortAsynchronousTrafficShaper:
        """
        Defines the rate at which the token bucket is refilled with tokens in bit per second.
        A None value is a no-op and does not overwrite an existing committedInformationRate.
        """
        if value is not None:
            self.committedInformationRate = value
        return self

    def getTrafficShaperGroupRef(self) -> Optional[RefType]:
        """
        Reference to the Traffic Shaper Group this Asynchronous Traffic Shaper is part of.
        """
        return self.trafficShaperGroupRef

    def setTrafficShaperGroupRef(self, value: Optional[RefType]) -> CouplingPortAsynchronousTrafficShaper:
        """
        Reference to the Traffic Shaper Group this Asynchronous Traffic Shaper is part of.
        A None value is a no-op and does not overwrite an existing trafficShaperGroupRef.
        """
        if value is not None:
            self.trafficShaperGroupRef = value
        return self


class CouplingPortCreditBasedShaper(CouplingPortAbstractShaper):
    """
    Defines a Credit Based Shaper (CBS) for the CouplingPort egress structure.
    """

    # CouplingPortCreditBasedShaper method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.37, p.2013
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIdleSlope        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIdleSlope        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLowerBoundary    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLowerBoundary    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUpperBoundary    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUpperBoundary    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (concrete child of the abstract CouplingPortAbstractShaper: the XSD models the polymorphic
    #  CouplingPortFifo.shaper choice via this class's xsd:group — the reader and writer dispatch that
    #  choice by matching the element name against this class's XSD tag)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the increase of credit in bits per second for the CBS shaper.
        self.idleSlope: Optional[PositiveInteger] = None

        # Defines the lower boundary of credit for the CBS shaper.
        self.lowerBoundary: Optional[PositiveInteger] = None

        # Defines the upper boundary of credit for the CBS shaper.
        self.upperBoundary: Optional[PositiveInteger] = None

    def getIdleSlope(self) -> Optional[PositiveInteger]:
        """
        Defines the increase of credit in bits per second for the CBS shaper.
        """
        return self.idleSlope

    def setIdleSlope(self, value: Optional[PositiveInteger]) -> CouplingPortCreditBasedShaper:
        """
        Defines the increase of credit in bits per second for the CBS shaper.
        A None value is a no-op and does not overwrite an existing idleSlope.
        """
        if value is not None:
            self.idleSlope = value
        return self

    def getLowerBoundary(self) -> Optional[PositiveInteger]:
        """
        Defines the lower boundary of credit for the CBS shaper.
        """
        return self.lowerBoundary

    def setLowerBoundary(self, value: Optional[PositiveInteger]) -> CouplingPortCreditBasedShaper:
        """
        Defines the lower boundary of credit for the CBS shaper.
        A None value is a no-op and does not overwrite an existing lowerBoundary.
        """
        if value is not None:
            self.lowerBoundary = value
        return self

    def getUpperBoundary(self) -> Optional[PositiveInteger]:
        """
        Defines the upper boundary of credit for the CBS shaper.
        """
        return self.upperBoundary

    def setUpperBoundary(self, value: Optional[PositiveInteger]) -> CouplingPortCreditBasedShaper:
        """
        Defines the upper boundary of credit for the CBS shaper.
        A None value is a no-op and does not overwrite an existing upperBoundary.
        """
        if value is not None:
            self.upperBoundary = value
        return self


class CouplingPortFifo(CouplingPortStructuralElement):
    """
    Defines a FIFO for the CouplingPort egress structure.
    """

    # CouplingPortFifo method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.68, p.124
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAssignedTrafficClass      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAssignedTrafficClasses    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getMinimumFifoLength         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMinimumFifoLength         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShaper                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setShaper                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines a set of Traffic Classes which shall be handled by this FIFO. range: 0-7
        self.assignedTrafficClasses: List[PositiveInteger] = []

        # FIFO minimum length in Byte. An actual configuration/ hardware may use a bigger value.
        self.minimumFifoLength: Optional[PositiveInteger] = None

        # Definition of the shaper to be used for the processing of this FIFO. Tags: atp.Status=candidate
        self.shaper: Optional[CouplingPortAbstractShaper] = None

    def addAssignedTrafficClass(self, value: Optional[PositiveInteger]) -> CouplingPortFifo:
        """
        Defines a set of Traffic Classes which shall be handled by this FIFO. range: 0-7
        A None value is a no-op and does not append to assignedTrafficClasses.
        """
        if value is not None:
            self.assignedTrafficClasses.append(value)
        return self

    def getAssignedTrafficClasses(self) -> List[PositiveInteger]:
        """
        Defines a set of Traffic Classes which shall be handled by this FIFO. range: 0-7
        """
        return self.assignedTrafficClasses

    def getMinimumFifoLength(self) -> Optional[PositiveInteger]:
        """
        FIFO minimum length in Byte. An actual configuration/ hardware may use a bigger value.
        """
        return self.minimumFifoLength

    def setMinimumFifoLength(self, value: Optional[PositiveInteger]) -> CouplingPortFifo:
        """
        FIFO minimum length in Byte. An actual configuration/ hardware may use a bigger value.
        A None value is a no-op and does not overwrite an existing minimumFifoLength.
        """
        if value is not None:
            self.minimumFifoLength = value
        return self

    def getShaper(self) -> Optional[CouplingPortAbstractShaper]:
        """
        Definition of the shaper to be used for the processing of this FIFO. Tags: atp.Status=candidate
        """
        return self.shaper

    def setShaper(self, value: Optional[CouplingPortAbstractShaper]) -> CouplingPortFifo:
        """
        Definition of the shaper to be used for the processing of this FIFO. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing shaper.
        """
        if value is not None:
            self.shaper = value
        return self


class CouplingPortScheduler(CouplingPortStructuralElement):
    """
    Defines a scheduler for the CouplingPort egress structure.
    """

    # CouplingPortScheduler method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.65, p.123
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPortScheduler        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPortScheduler        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPredecessorRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPredecessorRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the schedule algorithm to be used.
        self.portScheduler: Optional[EthernetCouplingPortSchedulerEnum] = None

        # Ordered List of predecessor inputs. The first element has the highest priority. The following elements have decreasing priorities.
        self.predecessorRefs: List[RefType] = []

    def getPortScheduler(self) -> Optional[EthernetCouplingPortSchedulerEnum]:
        """
        Defines the schedule algorithm to be used.
        """
        return self.portScheduler

    def setPortScheduler(self, value: Optional[EthernetCouplingPortSchedulerEnum]) -> CouplingPortScheduler:
        """
        Defines the schedule algorithm to be used.
        A None value is a no-op and does not overwrite an existing portScheduler.
        """
        if value is not None:
            self.portScheduler = value
        return self

    def getPredecessorRefs(self) -> List[RefType]:
        """
        Ordered List of predecessor inputs. The first element has the highest priority. The following elements have decreasing priorities.
        """
        return self.predecessorRefs

    def addPredecessorRef(self, value: RefType) -> CouplingPortScheduler:
        """
        Ordered List of predecessor inputs. The first element has the highest priority. The following elements have decreasing priorities.
        A None value is a no-op and does not extend the predecessor list.
        """
        if value is not None:
            self.predecessorRefs.append(value)
        return self


class CouplingPortShaper(CouplingPortStructuralElement):
    """
    Defines a shaper for the CouplingPort egress structure. Tags: atp.Status=obsolete
    """

    # CouplingPortShaper method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.67, p.123
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIdleSlope           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIdleSlope           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPredecessorFifoRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPredecessorFifoRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the increase of credit in bits per second for the AVB shaper. Tags: atp.Status=obsolete
        self.idleSlope: Optional[PositiveInteger] = None

        # Defines the CouplingPortFifo which provides the input to this shaper. Tags: atp.Status=obsolete
        self.predecessorFifoRef: Optional[RefType] = None

    def getIdleSlope(self) -> Optional[PositiveInteger]:
        """
        Defines the increase of credit in bits per second for the AVB shaper. Tags: atp.Status=obsolete
        """
        return self.idleSlope

    def setIdleSlope(self, value: Optional[PositiveInteger]) -> CouplingPortShaper:
        """
        Defines the increase of credit in bits per second for the AVB shaper. Tags: atp.Status=obsolete
        A None value is a no-op and does not overwrite an existing idleSlope.
        """
        if value is not None:
            self.idleSlope = value
        return self

    def getPredecessorFifoRef(self) -> Optional[RefType]:
        """
        Defines the CouplingPortFifo which provides the input to this shaper. Tags: atp.Status=obsolete
        """
        return self.predecessorFifoRef

    def setPredecessorFifoRef(self, value: Optional[RefType]) -> CouplingPortShaper:
        """
        Defines the CouplingPortFifo which provides the input to this shaper. Tags: atp.Status=obsolete
        A None value is a no-op and does not overwrite an existing predecessorFifoRef.
        """
        if value is not None:
            self.predecessorFifoRef = value
        return self


class EthernetPriorityRegeneration(Referrable):
    """
    Defines a priority regeneration where the ingressPriority is replaced by regeneratedPriority. The ethernetPriorityRegeneration is optional in case no priority regeneration shall be performed. In case a ethernetPriorityRegeneration is defined it shall have 8 mappings, one for each priority.
    """

    # EthernetPriorityRegeneration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.74, p.128
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIngressPriority         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIngressPriority         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRegeneratedPriority     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRegeneratedPriority     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Message priority of the incoming message. range: 0-7
        self.ingressPriority: Optional[PositiveInteger] = None

        # Regenerated message priority. range: 0-7
        self.regeneratedPriority: Optional[PositiveInteger] = None

    def getIngressPriority(self) -> Optional[PositiveInteger]:
        """
        Message priority of the incoming message. range: 0-7
        """
        return self.ingressPriority

    def setIngressPriority(self, value: Optional[PositiveInteger]) -> EthernetPriorityRegeneration:
        """
        Message priority of the incoming message. range: 0-7
        A None value is a no-op and does not overwrite an existing ingressPriority.
        """
        if value is not None:
            self.ingressPriority = value
        return self

    def getRegeneratedPriority(self) -> Optional[PositiveInteger]:
        """
        Regenerated message priority. range: 0-7
        """
        return self.regeneratedPriority

    def setRegeneratedPriority(self, value: Optional[PositiveInteger]) -> EthernetPriorityRegeneration:
        """
        Regenerated message priority. range: 0-7
        A None value is a no-op and does not overwrite an existing regeneratedPriority.
        """
        if value is not None:
            self.regeneratedPriority = value
        return self


class CouplingPortDetails(ARObject):
    """
    Defines details of a CouplingPort. May be used to configure the structures of a switch.
    """

    # CouplingPortDetails method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.63, p.122
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCouplingPortStructuralElements   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createCouplingPortFifo              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createCouplingPortScheduler         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createCouplingPortShaper            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createEthernetPriorityRegeneration  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEthernetPriorityRegenerations    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addEthernetTrafficClassAssignment   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEthernetTrafficClassAssignments  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getGlobalTimeProps                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setGlobalTimeProps                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLastEgressSchedulerRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLastEgressSchedulerRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addRatePolicy                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRatePolicies                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Collects all the structural parts at which a CouplingPort may be configurable.
        self.couplingPortStructuralElements: List[CouplingPortStructuralElement] = []

        # Defines a priority regeneration where the ingress priority is replaced by regenerated priority.
        self.ethernetPriorityRegenerations: List[EthernetPriorityRegeneration] = []

        # Defines the ingress port to EthernetTrafficClass assignment.
        self.ethernetTrafficClassAssignments: List[CouplingPortTrafficClassAssignment] = []

        # Specifies properties for the usage of the CouplingPort in the scope of Global Time Sync.
        self.globalTimeProps: Optional[GlobalTimeCouplingPortProps] = None

        # Defines which CouplingPortScheduler is the last in the egress port structure.
        self.lastEgressSchedulerRef: Optional[RefType] = None

        # Rate policies to be applied for this CouplingPort.
        self.ratePolicies: List[CouplingPortRatePolicy] = []

    def getCouplingPortStructuralElements(self) -> List[CouplingPortStructuralElement]:
        """Collects all the structural parts at which a CouplingPort may be configurable."""
        return self.couplingPortStructuralElements

    def createCouplingPortFifo(self, short_name: str) -> CouplingPortFifo:
        """Collects all the structural parts at which a CouplingPort may be configurable."""
        fifo = CouplingPortFifo(self, short_name)
        self.couplingPortStructuralElements.append(fifo)
        return fifo

    def createCouplingPortScheduler(self, short_name: str) -> CouplingPortScheduler:
        """Collects all the structural parts at which a CouplingPort may be configurable."""
        scheduler = CouplingPortScheduler(self, short_name)
        self.couplingPortStructuralElements.append(scheduler)
        return scheduler

    def createCouplingPortShaper(self, short_name: str) -> CouplingPortShaper:
        """Collects all the structural parts at which a CouplingPort may be configurable."""
        shaper = CouplingPortShaper(self, short_name)
        self.couplingPortStructuralElements.append(shaper)
        return shaper

    def createEthernetPriorityRegeneration(self, short_name: str) -> EthernetPriorityRegeneration:
        """Defines a priority regeneration where the ingress priority is replaced by regenerated priority."""
        regeneration = EthernetPriorityRegeneration(self, short_name)
        self.ethernetPriorityRegenerations.append(regeneration)
        return regeneration

    def getEthernetPriorityRegenerations(self) -> List[EthernetPriorityRegeneration]:
        """Defines a priority regeneration where the ingress priority is replaced by regenerated priority."""
        return self.ethernetPriorityRegenerations

    def addEthernetTrafficClassAssignment(self, value: Optional[CouplingPortTrafficClassAssignment]) -> CouplingPortDetails:
        """
        Defines the ingress port to EthernetTrafficClass assignment.
        A None value is a no-op and does not append to ethernetTrafficClassAssignments.
        """
        if value is not None:
            self.ethernetTrafficClassAssignments.append(value)
        return self

    def getEthernetTrafficClassAssignments(self) -> List[CouplingPortTrafficClassAssignment]:
        """Defines the ingress port to EthernetTrafficClass assignment."""
        return self.ethernetTrafficClassAssignments

    def getGlobalTimeProps(self) -> Optional[GlobalTimeCouplingPortProps]:
        """Specifies properties for the usage of the CouplingPort in the scope of Global Time Sync."""
        return self.globalTimeProps

    def setGlobalTimeProps(self, value: Optional[GlobalTimeCouplingPortProps]) -> CouplingPortDetails:
        """
        Specifies properties for the usage of the CouplingPort in the scope of Global Time Sync.
        A None value is a no-op and does not overwrite an existing globalTimeProps.
        """
        if value is not None:
            self.globalTimeProps = value
        return self

    def getLastEgressSchedulerRef(self) -> Optional[RefType]:
        """Defines which CouplingPortScheduler is the last in the egress port structure."""
        return self.lastEgressSchedulerRef

    def setLastEgressSchedulerRef(self, value: Optional[RefType]) -> CouplingPortDetails:
        """
        Defines which CouplingPortScheduler is the last in the egress port structure.
        A None value is a no-op and does not overwrite an existing lastEgressSchedulerRef.
        """
        if value is not None:
            self.lastEgressSchedulerRef = value
        return self

    def addRatePolicy(self, value: Optional[CouplingPortRatePolicy]) -> CouplingPortDetails:
        """
        Rate policies to be applied for this CouplingPort.
        A None value is a no-op and does not append to ratePolicies.
        """
        if value is not None:
            self.ratePolicies.append(value)
        return self

    def getRatePolicies(self) -> List[CouplingPortRatePolicy]:
        """Rate policies to be applied for this CouplingPort."""
        return self.ratePolicies


class VlanMembership(ARObject):
    """
    Static logical channel or VLAN binding to a switch-port. The reference to an EthernetPhysicalChannel without a VLAN defined represents the handling of untagged frames.
    """

    # VlanMembership method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.59, p.112
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDefaultPriority        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultPriority        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDhcpAddressAssignment  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDhcpAddressAssignment  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSendActivity           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSendActivity           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlanRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVlanRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Standard output-priority outgoing Frames will be tagged with. Defines the priority that received frames are assigned together with the VLAN Id (defaultVlan). The values from 0 (best effort) to 7 (highest) are allowed. In case modifyVlan and an already tagged received frame, the actual priority of the received frame is not modified.
        self.defaultPriority: Optional[PositiveInteger] = None

        # Specifies the IP Address which will be assigned to a DHCP Client at this SwitchPort. If no dhcpAddressAssignment is provided all DHCP-Discover messages received at this Port will be discarded by the DHCP Server.
        self.dhcpAddressAssignment: Optional[DhcpServerConfiguration] = None

        # Attribute denotes whether a VLAN tagged ethernet frame will be 1. sent with its VLAN tag (sentTagged) 2. sent without a VLAN tag (sentUntagged) 3. will be dropped at this port (notSent or VLAN not member of this list)
        self.sendActivity: Optional[EthernetSwitchVlanEgressTaggingEnum] = None

        # References a channel that represents a VLAN or an untagged channel.
        self.vlanRef: Optional[RefType] = None

    def getDefaultPriority(self) -> Optional[PositiveInteger]:
        """
        Standard output-priority outgoing Frames will be tagged with. Defines the priority that received frames are assigned together with the VLAN Id (defaultVlan). The values from 0 (best effort) to 7 (highest) are allowed. In case modifyVlan and an already tagged received frame, the actual priority of the received frame is not modified.
        """
        return self.defaultPriority

    def setDefaultPriority(self, value: Optional[PositiveInteger]) -> VlanMembership:
        """
        Standard output-priority outgoing Frames will be tagged with. Defines the priority that received frames are assigned together with the VLAN Id (defaultVlan). The values from 0 (best effort) to 7 (highest) are allowed. In case modifyVlan and an already tagged received frame, the actual priority of the received frame is not modified.
        A None value is a no-op and does not overwrite an existing defaultPriority.
        """
        if value is not None:
            self.defaultPriority = value
        return self

    def getDhcpAddressAssignment(self) -> Optional[DhcpServerConfiguration]:
        """
        Specifies the IP Address which will be assigned to a DHCP Client at this SwitchPort. If no dhcpAddressAssignment is provided all DHCP-Discover messages received at this Port will be discarded by the DHCP Server.
        """
        return self.dhcpAddressAssignment

    def setDhcpAddressAssignment(self, value: Optional[DhcpServerConfiguration]) -> VlanMembership:
        """
        Specifies the IP Address which will be assigned to a DHCP Client at this SwitchPort. If no dhcpAddressAssignment is provided all DHCP-Discover messages received at this Port will be discarded by the DHCP Server.
        A None value is a no-op and does not overwrite an existing dhcpAddressAssignment.
        """
        if value is not None:
            self.dhcpAddressAssignment = value
        return self

    def getSendActivity(self) -> Optional[EthernetSwitchVlanEgressTaggingEnum]:
        """
        Attribute denotes whether a VLAN tagged ethernet frame will be 1. sent with its VLAN tag (sentTagged) 2. sent without a VLAN tag (sentUntagged) 3. will be dropped at this port (notSent or VLAN not member of this list)
        """
        return self.sendActivity

    def setSendActivity(self, value: Optional[EthernetSwitchVlanEgressTaggingEnum]) -> VlanMembership:
        """
        Attribute denotes whether a VLAN tagged ethernet frame will be 1. sent with its VLAN tag (sentTagged) 2. sent without a VLAN tag (sentUntagged) 3. will be dropped at this port (notSent or VLAN not member of this list)
        A None value is a no-op and does not overwrite an existing sendActivity.
        """
        if value is not None:
            self.sendActivity = value
        return self

    def getVlanRef(self) -> Optional[RefType]:
        """
        References a channel that represents a VLAN or an untagged channel.
        """
        return self.vlanRef

    def setVlanRef(self, value: Optional[RefType]) -> VlanMembership:
        """
        References a channel that represents a VLAN or an untagged channel.
        A None value is a no-op and does not overwrite an existing vlanRef.
        """
        if value is not None:
            self.vlanRef = value
        return self


class CouplingPort(Identifiable, VariationPointCapable):
    """
    A CouplingPort is used to connect a CouplingElement with an EcuInstance or two CouplingElements with each other via a CouplingPortConnection. Optionally, the CouplingPort may also have a reference to a macMulticastGroup and a defaultVLAN.
    """

    # CouplingPort method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.54, p.110
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getConnectionNegotiationBehavior     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setConnectionNegotiationBehavior     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCouplingPortDetails               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCouplingPortDetails               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCouplingPortRole                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCouplingPortRole                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDefaultVlanRef                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultVlanRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMacLayerType                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMacLayerType                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addMacMulticastAddressRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMacMulticastAddressRefs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addMacSecProps                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMacSecProps                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPhysicalLayerType                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPhysicalLayerType                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPlcaProps                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPlcaProps                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addPncMappingRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPncMappingRefs                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getReceiveActivity                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReceiveActivity                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addVlanMembership                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlanMemberships                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getVlanModifierRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVlanModifierRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeupSleepOnDatalineConfigRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWakeupSleepOnDatalineConfigRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the connection negotiation of the CouplingPort.
        self.connectionNegotiationBehavior: Optional[EthernetConnectionNegotiationEnum] = None

        # Defines more details of a CouplingPort in case a more specific configuration is required.
        self.couplingPortDetails: Optional[CouplingPortDetails] = None

        # Defines the role this CouplingPort takes in the context of the CouplingElement.
        self.couplingPortRole: Optional[CouplingPortRoleEnum] = None

        # The vLanIdentifier of the referenced VLAN is the Default-PVID (port VLAN ID). A Port VLAN ID is a default VLAN ID that is assigned to an access CouplingPort to designate the VLAN segment to which this port is connected. Also, if a CouplingPort has not been configured with any VLAN memberships, the virtual switch's Port VLAN ID (pvid) becomes the default VLAN ID for the ports connection. This identifier/tag is added for incoming untagged messages at the port (ingress tagging). For outgoing messages with this identifier, the tag is removed at the port (egress untagging, depending on the VlanMembership.sendActivity).
        self.defaultVlanRef: Optional[RefType] = None

        # Specifies the mac layer type of the CouplingPort.
        self.macLayerType: Optional[EthernetMacLayerTypeEnum] = None

        # Assigns a set of MAC-Multicast-Addresses which are addressable via this CouplingPort. This is a static pre-configuration and further addresses may be learned during runtime.
        self.macMulticastAddressRefs: List[RefType] = []

        # Properties to configure MACsec (Media access control security) and the MKA (MACsec Key Agreement) for the CouplingPort (PHY).
        self.macSecProps: List[MacSecProps] = []

        # Specifies the physical layer type of the CouplingPort.
        self.physicalLayerType: Optional[EthernetPhysicalLayerTypeEnum] = None

        # Optional properties for configuration of PLCA (Physical Layer Collision Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the Coupling Port (PHY).
        self.plcaProps: Optional[PlcaProps] = None

        # Reference to the partial networks this CouplingPort participates in. Stereotypes: atpSplitable Tags: atp.Splitkey=pncMapping
        self.pncMappingRefs: List[RefType] = []

        # Defines the handling of frames at the ingress port.
        self.receiveActivity: Optional[EthernetSwitchVlanIngressTagEnum] = None

        # Messages of VLANs that are defined here can be communicated via the CouplingPort.
        self.vlanMemberships: List[VlanMembership] = []

        # All incoming messages at this CouplingPort shall be tagged with this VLAN Id. This tagging is performed regardless whether the message already has a VLAN tag or is untagged, an existing VLAN tag will be overwritten. This feature is XOR with CoupligPort.defaultVlan.
        self.vlanModifierRef: Optional[RefType] = None

        # Optional reference to EthernetWakeupSleepOnDatalineConfig.
        self.wakeupSleepOnDatalineConfigRef: Optional[RefType] = None

    def getConnectionNegotiationBehavior(self) -> Optional[EthernetConnectionNegotiationEnum]:
        """Specifies the connection negotiation of the CouplingPort."""
        return self.connectionNegotiationBehavior

    def setConnectionNegotiationBehavior(self, value: Optional[EthernetConnectionNegotiationEnum]) -> CouplingPort:
        """
        Specifies the connection negotiation of the CouplingPort.
        A None value is a no-op and does not overwrite an existing connectionNegotiationBehavior.
        """
        if value is not None:
            self.connectionNegotiationBehavior = value
        return self

    def getCouplingPortDetails(self) -> Optional[CouplingPortDetails]:
        """Defines more details of a CouplingPort in case a more specific configuration is required."""
        return self.couplingPortDetails

    def setCouplingPortDetails(self, value: Optional[CouplingPortDetails]) -> CouplingPort:
        """
        Defines more details of a CouplingPort in case a more specific configuration is required.
        A None value is a no-op and does not overwrite an existing couplingPortDetails.
        """
        if value is not None:
            self.couplingPortDetails = value
        return self

    def getCouplingPortRole(self) -> Optional[CouplingPortRoleEnum]:
        """Defines the role this CouplingPort takes in the context of the CouplingElement."""
        return self.couplingPortRole

    def setCouplingPortRole(self, value: Optional[CouplingPortRoleEnum]) -> CouplingPort:
        """
        Defines the role this CouplingPort takes in the context of the CouplingElement.
        A None value is a no-op and does not overwrite an existing couplingPortRole.
        """
        if value is not None:
            self.couplingPortRole = value
        return self

    def getDefaultVlanRef(self) -> Optional[RefType]:
        """The vLanIdentifier of the referenced VLAN is the Default-PVID (port VLAN ID). A Port VLAN ID is a default VLAN ID that is assigned to an access CouplingPort to designate the VLAN segment to which this port is connected. Also, if a CouplingPort has not been configured with any VLAN memberships, the virtual switch's Port VLAN ID (pvid) becomes the default VLAN ID for the ports connection. This identifier/tag is added for incoming untagged messages at the port (ingress tagging). For outgoing messages with this identifier, the tag is removed at the port (egress untagging, depending on the VlanMembership.sendActivity)."""
        return self.defaultVlanRef

    def setDefaultVlanRef(self, value: Optional[RefType]) -> CouplingPort:
        """
        The vLanIdentifier of the referenced VLAN is the Default-PVID (port VLAN ID). A Port VLAN ID is a default VLAN ID that is assigned to an access CouplingPort to designate the VLAN segment to which this port is connected. Also, if a CouplingPort has not been configured with any VLAN memberships, the virtual switch's Port VLAN ID (pvid) becomes the default VLAN ID for the ports connection. This identifier/tag is added for incoming untagged messages at the port (ingress tagging). For outgoing messages with this identifier, the tag is removed at the port (egress untagging, depending on the VlanMembership.sendActivity).
        A None value is a no-op and does not overwrite an existing defaultVlanRef.
        """
        if value is not None:
            self.defaultVlanRef = value
        return self

    def getMacLayerType(self) -> Optional[EthernetMacLayerTypeEnum]:
        """Specifies the mac layer type of the CouplingPort."""
        return self.macLayerType

    def setMacLayerType(self, value: Optional[EthernetMacLayerTypeEnum]) -> CouplingPort:
        """
        Specifies the mac layer type of the CouplingPort.
        A None value is a no-op and does not overwrite an existing macLayerType.
        """
        if value is not None:
            self.macLayerType = value
        return self

    def addMacMulticastAddressRef(self, ref: Optional[RefType]) -> CouplingPort:
        """
        Assigns a set of MAC-Multicast-Addresses which are addressable via this CouplingPort. This is a static pre-configuration and further addresses may be learned during runtime.
        A None value is a no-op and does not append to macMulticastAddressRefs.
        """
        if ref is not None:
            self.macMulticastAddressRefs.append(ref)
        return self

    def getMacMulticastAddressRefs(self) -> List[RefType]:
        """Assigns a set of MAC-Multicast-Addresses which are addressable via this CouplingPort. This is a static pre-configuration and further addresses may be learned during runtime."""
        return self.macMulticastAddressRefs

    def addMacSecProps(self, value: Optional[MacSecProps]) -> CouplingPort:
        """
        Properties to configure MACsec (Media access control security) and the MKA (MACsec Key Agreement) for the CouplingPort (PHY).
        A None value is a no-op and does not append to macSecProps.
        """
        if value is not None:
            self.macSecProps.append(value)
        return self

    def getMacSecProps(self) -> List[MacSecProps]:
        """Properties to configure MACsec (Media access control security) and the MKA (MACsec Key Agreement) for the CouplingPort (PHY)."""
        return self.macSecProps

    def getPhysicalLayerType(self) -> Optional[EthernetPhysicalLayerTypeEnum]:
        """Specifies the physical layer type of the CouplingPort."""
        return self.physicalLayerType

    def setPhysicalLayerType(self, value: Optional[EthernetPhysicalLayerTypeEnum]) -> CouplingPort:
        """
        Specifies the physical layer type of the CouplingPort.
        A None value is a no-op and does not overwrite an existing physicalLayerType.
        """
        if value is not None:
            self.physicalLayerType = value
        return self

    def getPlcaProps(self) -> Optional[PlcaProps]:
        """Optional properties for configuration of PLCA (Physical Layer Collision Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the Coupling Port (PHY)."""
        return self.plcaProps

    def setPlcaProps(self, value: Optional[PlcaProps]) -> CouplingPort:
        """
        Optional properties for configuration of PLCA (Physical Layer Collision Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the Coupling Port (PHY).
        A None value is a no-op and does not overwrite an existing plcaProps.
        """
        if value is not None:
            self.plcaProps = value
        return self

    def addPncMappingRef(self, ref: Optional[RefType]) -> CouplingPort:
        """
        Reference to the partial networks this CouplingPort participates in. Stereotypes: atpSplitable Tags: atp.Splitkey=pncMapping
        A None value is a no-op and does not append to pncMappingRefs.
        """
        if ref is not None:
            self.pncMappingRefs.append(ref)
        return self

    def getPncMappingRefs(self) -> List[RefType]:
        """Reference to the partial networks this CouplingPort participates in. Stereotypes: atpSplitable Tags: atp.Splitkey=pncMapping"""
        return self.pncMappingRefs

    def getReceiveActivity(self) -> Optional[EthernetSwitchVlanIngressTagEnum]:
        """Defines the handling of frames at the ingress port."""
        return self.receiveActivity

    def setReceiveActivity(self, value: Optional[EthernetSwitchVlanIngressTagEnum]) -> CouplingPort:
        """
        Defines the handling of frames at the ingress port.
        A None value is a no-op and does not overwrite an existing receiveActivity.
        """
        if value is not None:
            self.receiveActivity = value
        return self

    def addVlanMembership(self, value: Optional[VlanMembership]) -> CouplingPort:
        """
        Messages of VLANs that are defined here can be communicated via the CouplingPort.
        A None value is a no-op and does not append to vlanMemberships.
        """
        if value is not None:
            self.vlanMemberships.append(value)
        return self

    def getVlanMemberships(self) -> List[VlanMembership]:
        """Messages of VLANs that are defined here can be communicated via the CouplingPort."""
        return self.vlanMemberships

    def getVlanModifierRef(self) -> Optional[RefType]:
        """All incoming messages at this CouplingPort shall be tagged with this VLAN Id. This tagging is performed regardless whether the message already has a VLAN tag or is untagged, an existing VLAN tag will be overwritten. This feature is XOR with CoupligPort.defaultVlan."""
        return self.vlanModifierRef

    def setVlanModifierRef(self, value: Optional[RefType]) -> CouplingPort:
        """
        All incoming messages at this CouplingPort shall be tagged with this VLAN Id. This tagging is performed regardless whether the message already has a VLAN tag or is untagged, an existing VLAN tag will be overwritten. This feature is XOR with CoupligPort.defaultVlan.
        A None value is a no-op and does not overwrite an existing vlanModifierRef.
        """
        if value is not None:
            self.vlanModifierRef = value
        return self

    def getWakeupSleepOnDatalineConfigRef(self) -> Optional[RefType]:
        """Optional reference to EthernetWakeupSleepOnDatalineConfig."""
        return self.wakeupSleepOnDatalineConfigRef

    def setWakeupSleepOnDatalineConfigRef(self, value: Optional[RefType]) -> CouplingPort:
        """
        Optional reference to EthernetWakeupSleepOnDatalineConfig.
        A None value is a no-op and does not overwrite an existing wakeupSleepOnDatalineConfigRef.
        """
        if value is not None:
            self.wakeupSleepOnDatalineConfigRef = value
        return self


class EthernetCommunicationController(CommunicationController):
    """
    Ethernet specific communication port attributes.
    """

    # EthernetCommunicationController method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.61, p.116
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCanXlConfigRef                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCanXlConfigRef                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCouplingPorts                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createCouplingPort                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMacLayerType                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMacLayerType                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMacUnicastAddress                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMacUnicastAddress                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaximumReceiveBufferLength           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaximumReceiveBufferLength           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaximumTransmitBufferLength          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaximumTransmitBufferLength          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSlaveActAsPassiveCommunicationSlave  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSlaveActAsPassiveCommunicationSlave  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSlaveQualifiedUnexpectedLinkDownTime [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSlaveQualifiedUnexpectedLinkDownTime [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # If the Ethernet frames handled by this Ethernet CommunicationController are to be tunneled through CAN XL, then this reference shall refer to the Abstract CanCommunicationController that aggregates the Can ControllerXlConfiguration of the physical CAN XL channel to be used for tunneling.
        self.canXlConfigRef: Optional[RefType] = None

        # Optional CouplingPort that can be used to connect the ECU to a CouplingElement (e.g. a switch).
        self.couplingPorts: List[CouplingPort] = []

        # Specifies the mac layer type of the ethernet controller.
        self.macLayerType: Optional[EthernetMacLayerTypeEnum] = None

        # Media Access Control address (MAC address) that uniquely identifies each EthernetCommunication Controller in the network.
        self.macUnicastAddress: Optional[MacAddressString] = None

        # Determines the maximum receive buffer length (frame length) in bytes.
        self.maximumReceiveBufferLength: Optional[Integer] = None

        # Determines the maximum transmit buffer length (frame length) in bytes.
        self.maximumTransmitBufferLength: Optional[Integer] = None

        # This attribute specifies if the EcuInstance is acting as a passive communication slave on the connected Physical Channel. This is used for EthernetCommunication Controllers that use Ethernet hardware which supports wake-up and sleep on the network (e.g. Open Alliance TC10 compliant Ethernet hardware).
        self.slaveActAsPassiveCommunicationSlave: Optional[Boolean] = None

        # This attribute specifies time when an unexpected link down is evaluated as link down and indicated to the AUTOSAR communication stack.
        self.slaveQualifiedUnexpectedLinkDownTime: Optional[TimeValue] = None

    def getCanXlConfigRef(self) -> Optional[RefType]:
        """If the Ethernet frames handled by this Ethernet CommunicationController are to be tunneled through CAN XL, then this reference shall refer to the Abstract CanCommunicationController that aggregates the Can ControllerXlConfiguration of the physical CAN XL channel to be used for tunneling."""
        return self.canXlConfigRef

    def setCanXlConfigRef(self, value: Optional[RefType]) -> EthernetCommunicationController:
        """
        If the Ethernet frames handled by this Ethernet CommunicationController are to be tunneled through CAN XL, then this reference shall refer to the Abstract CanCommunicationController that aggregates the Can ControllerXlConfiguration of the physical CAN XL channel to be used for tunneling.
        A None value is a no-op and does not overwrite an existing canXlConfigRef.
        """
        if value is not None:
            self.canXlConfigRef = value
        return self

    def getCouplingPorts(self) -> List[CouplingPort]:
        """Optional CouplingPort that can be used to connect the ECU to a CouplingElement (e.g. a switch)."""
        return self.couplingPorts

    def createCouplingPort(self, short_name: str) -> CouplingPort:
        """Optional CouplingPort that can be used to connect the ECU to a CouplingElement (e.g. a switch)."""
        if not self.IsReferrableElementExists(short_name, CouplingPort):
            group = CouplingPort(self, short_name)
            self.addReferrableElement(group)
            self.couplingPorts.append(group)
        return cast(CouplingPort, self.getReferrableElement(short_name, CouplingPort))

    def getMacLayerType(self) -> Optional[EthernetMacLayerTypeEnum]:
        """Specifies the mac layer type of the ethernet controller."""
        return self.macLayerType

    def setMacLayerType(self, value: Optional[EthernetMacLayerTypeEnum]) -> EthernetCommunicationController:
        """
        Specifies the mac layer type of the ethernet controller.
        A None value is a no-op and does not overwrite an existing macLayerType.
        """
        if value is not None:
            self.macLayerType = value
        return self

    def getMacUnicastAddress(self) -> Optional[MacAddressString]:
        """Media Access Control address (MAC address) that uniquely identifies each EthernetCommunication Controller in the network."""
        return self.macUnicastAddress

    def setMacUnicastAddress(self, value: Optional[MacAddressString]) -> EthernetCommunicationController:
        """
        Media Access Control address (MAC address) that uniquely identifies each EthernetCommunication Controller in the network.
        A None value is a no-op and does not overwrite an existing macUnicastAddress.
        """
        if value is not None:
            self.macUnicastAddress = value
        return self

    def getMaximumReceiveBufferLength(self) -> Optional[Integer]:
        """Determines the maximum receive buffer length (frame length) in bytes."""
        return self.maximumReceiveBufferLength

    def setMaximumReceiveBufferLength(self, value: Optional[Integer]) -> EthernetCommunicationController:
        """
        Determines the maximum receive buffer length (frame length) in bytes.
        A None value is a no-op and does not overwrite an existing maximumReceiveBufferLength.
        """
        if value is not None:
            self.maximumReceiveBufferLength = value
        return self

    def getMaximumTransmitBufferLength(self) -> Optional[Integer]:
        """Determines the maximum transmit buffer length (frame length) in bytes."""
        return self.maximumTransmitBufferLength

    def setMaximumTransmitBufferLength(self, value: Optional[Integer]) -> EthernetCommunicationController:
        """
        Determines the maximum transmit buffer length (frame length) in bytes.
        A None value is a no-op and does not overwrite an existing maximumTransmitBufferLength.
        """
        if value is not None:
            self.maximumTransmitBufferLength = value
        return self

    def getSlaveActAsPassiveCommunicationSlave(self) -> Optional[Boolean]:
        """This attribute specifies if the EcuInstance is acting as a passive communication slave on the connected Physical Channel. This is used for EthernetCommunication Controllers that use Ethernet hardware which supports wake-up and sleep on the network (e.g. Open Alliance TC10 compliant Ethernet hardware)."""
        return self.slaveActAsPassiveCommunicationSlave

    def setSlaveActAsPassiveCommunicationSlave(self, value: Optional[Boolean]) -> EthernetCommunicationController:
        """
        This attribute specifies if the EcuInstance is acting as a passive communication slave on the connected Physical Channel. This is used for EthernetCommunication Controllers that use Ethernet hardware which supports wake-up and sleep on the network (e.g. Open Alliance TC10 compliant Ethernet hardware).
        A None value is a no-op and does not overwrite an existing slaveActAsPassiveCommunicationSlave.
        """
        if value is not None:
            self.slaveActAsPassiveCommunicationSlave = value
        return self

    def getSlaveQualifiedUnexpectedLinkDownTime(self) -> Optional[TimeValue]:
        """This attribute specifies time when an unexpected link down is evaluated as link down and indicated to the AUTOSAR communication stack."""
        return self.slaveQualifiedUnexpectedLinkDownTime

    def setSlaveQualifiedUnexpectedLinkDownTime(self, value: Optional[TimeValue]) -> EthernetCommunicationController:
        """
        This attribute specifies time when an unexpected link down is evaluated as link down and indicated to the AUTOSAR communication stack.
        A None value is a no-op and does not overwrite an existing slaveQualifiedUnexpectedLinkDownTime.
        """
        if value is not None:
            self.slaveQualifiedUnexpectedLinkDownTime = value
        return self


class EthernetCommunicationConnector(CommunicationConnector):
    """
    Ethernet specific attributes to the CommunicationConnector.
    """

    # EthernetCommunicationConnector method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.62, p.117
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEthIpPropsRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEthIpPropsRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMaximumTransmissionUnit  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaximumTransmissionUnit  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNeighborCacheSize        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNeighborCacheSize        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPathMtuEnabled           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPathMtuEnabled           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPathMtuTimeout           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPathMtuTimeout           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # EcuInstance specific IP attributes.
        self.ethIpPropsRef: Optional[RefType] = None

        # This attribute specifies the maximum transmission unit in bytes.
        self.maximumTransmissionUnit: Optional[PositiveInteger] = None

        # This attribute specifies the size of neighbor cache or ARP table in units of entries.
        self.neighborCacheSize: Optional[PositiveInteger] = None

        # If enabled the IPv4/IPv6 processes incoming ICMP "Packet Too Big" messages and stores a MTU value for each destination address.
        self.pathMtuEnabled: Optional[Boolean] = None

        # If this value is >0 the IPv4/IPv6 will reset the MTU value stored for each destination after n seconds.
        self.pathMtuTimeout: Optional[TimeValue] = None

    def getEthIpPropsRef(self) -> Optional[RefType]:
        """EcuInstance specific IP attributes."""
        return self.ethIpPropsRef

    def setEthIpPropsRef(self, value: Optional[RefType]) -> EthernetCommunicationConnector:
        """
        EcuInstance specific IP attributes.
        A None value is a no-op and does not overwrite an existing ethIpPropsRef.
        """
        if value is not None:
            self.ethIpPropsRef = value
        return self

    def getMaximumTransmissionUnit(self) -> Optional[PositiveInteger]:
        """This attribute specifies the maximum transmission unit in bytes."""
        return self.maximumTransmissionUnit

    def setMaximumTransmissionUnit(self, value: Optional[PositiveInteger]) -> EthernetCommunicationConnector:
        """
        This attribute specifies the maximum transmission unit in bytes.
        A None value is a no-op and does not overwrite an existing maximumTransmissionUnit.
        """
        if value is not None:
            self.maximumTransmissionUnit = value
        return self

    def getNeighborCacheSize(self) -> Optional[PositiveInteger]:
        """This attribute specifies the size of neighbor cache or ARP table in units of entries."""
        return self.neighborCacheSize

    def setNeighborCacheSize(self, value: Optional[PositiveInteger]) -> EthernetCommunicationConnector:
        """
        This attribute specifies the size of neighbor cache or ARP table in units of entries.
        A None value is a no-op and does not overwrite an existing neighborCacheSize.
        """
        if value is not None:
            self.neighborCacheSize = value
        return self

    def getPathMtuEnabled(self) -> Optional[Boolean]:
        """If enabled the IPv4/IPv6 processes incoming ICMP "Packet Too Big" messages and stores a MTU value for each destination address."""
        return self.pathMtuEnabled

    def setPathMtuEnabled(self, value: Optional[Boolean]) -> EthernetCommunicationConnector:
        """
        If enabled the IPv4/IPv6 processes incoming ICMP "Packet Too Big" messages and stores a MTU value for each destination address.
        A None value is a no-op and does not overwrite an existing pathMtuEnabled.
        """
        if value is not None:
            self.pathMtuEnabled = value
        return self

    def getPathMtuTimeout(self) -> Optional[TimeValue]:
        """If this value is >0 the IPv4/IPv6 will reset the MTU value stored for each destination after n seconds."""
        return self.pathMtuTimeout

    def setPathMtuTimeout(self, value: Optional[TimeValue]) -> EthernetCommunicationConnector:
        """
        If this value is >0 the IPv4/IPv6 will reset the MTU value stored for each destination after n seconds.
        A None value is a no-op and does not overwrite an existing pathMtuTimeout.
        """
        if value is not None:
            self.pathMtuTimeout = value
        return self


class SdServerConfig(ARObject):
    """
    Server configuration for Service-Discovery.
    """

    # SdServerConfig method parity checklist:
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.171, p.355
    # Spec verified: R4.3.1
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] addCapabilityRecord           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getCapabilityRecords          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] getInitialOfferBehavior       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setInitialOfferBehavior       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getOfferCyclicDelay           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setOfferCyclicDelay           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getRequestResponseDelay       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setRequestResponseDelay       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getServerServiceMajorVersion  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setServerServiceMajorVersion  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getServerServiceMinorVersion  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setServerServiceMinorVersion  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getTtl                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setTtl                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1

    def __init__(self):
        super().__init__()

        # A sequence of records to store arbitrary name/value pairs conveying additional information about the named service. Capability records shall only be existing if the respective SdServerConfig is composed by a ProvidedServiceInstance (see constr_3259).
        self.capabilityRecords: List[TagWithOptionalValue] = []

        # Controls offer behavior of the server.
        self.initialOfferBehavior: Optional[InitialSdDelayConfig] = None

        # Optional attribute to define cyclic offers. Cyclic offer is active, if the delay is set (in seconds).
        self.offerCyclicDelay: Optional[TimeValue] = None

        # Maximum/Minimum allowable response delay to entries received by multicast in seconds.
        self.requestResponseDelay: Optional[RequestResponseDelay] = None

        # Major version number of the Service.
        self.serverServiceMajorVersion: Optional[PositiveInteger] = None

        # Minor version number of the Service.
        self.serverServiceMinorVersion: Optional[PositiveInteger] = None

        # Time to live. Shall be a positive value (sInt32).
        self.ttl: Optional[PositiveInteger] = None

    def addCapabilityRecord(self, value: Optional[TagWithOptionalValue]) -> SdServerConfig:
        """
        A sequence of records to store arbitrary name/value pairs conveying additional information about the named service. Capability records shall only be existing if the respective SdServerConfig is composed by a ProvidedServiceInstance (see constr_3259).
        A None value is a no-op and is not appended to capabilityRecords.
        """
        if value is not None:
            self.capabilityRecords.append(value)
        return self

    def getCapabilityRecords(self) -> List[TagWithOptionalValue]:
        """
        A sequence of records to store arbitrary name/value pairs conveying additional information about the named service. Capability records shall only be existing if the respective SdServerConfig is composed by a ProvidedServiceInstance (see constr_3259).
        """
        return self.capabilityRecords

    def getInitialOfferBehavior(self) -> Optional[InitialSdDelayConfig]:
        """
        Controls offer behavior of the server.
        """
        return self.initialOfferBehavior

    def setInitialOfferBehavior(self, value: Optional[InitialSdDelayConfig]) -> SdServerConfig:
        """
        Controls offer behavior of the server.
        A None value is a no-op and does not overwrite an existing initialOfferBehavior.
        """
        if value is not None:
            self.initialOfferBehavior = value
        return self

    def getOfferCyclicDelay(self) -> Optional[TimeValue]:
        """
        Optional attribute to define cyclic offers. Cyclic offer is active, if the delay is set (in seconds).
        """
        return self.offerCyclicDelay

    def setOfferCyclicDelay(self, value: Optional[TimeValue]) -> SdServerConfig:
        """
        Optional attribute to define cyclic offers. Cyclic offer is active, if the delay is set (in seconds).
        A None value is a no-op and does not overwrite an existing offerCyclicDelay.
        """
        if value is not None:
            self.offerCyclicDelay = value
        return self

    def getRequestResponseDelay(self) -> Optional[RequestResponseDelay]:
        """
        Maximum/Minimum allowable response delay to entries received by multicast in seconds.
        """
        return self.requestResponseDelay

    def setRequestResponseDelay(self, value: Optional[RequestResponseDelay]) -> SdServerConfig:
        """
        Maximum/Minimum allowable response delay to entries received by multicast in seconds.
        A None value is a no-op and does not overwrite an existing requestResponseDelay.
        """
        if value is not None:
            self.requestResponseDelay = value
        return self

    def getServerServiceMajorVersion(self) -> Optional[PositiveInteger]:
        """
        Major version number of the Service.
        """
        return self.serverServiceMajorVersion

    def setServerServiceMajorVersion(self, value: Optional[PositiveInteger]) -> SdServerConfig:
        """
        Major version number of the Service.
        A None value is a no-op and does not overwrite an existing serverServiceMajorVersion.
        """
        if value is not None:
            self.serverServiceMajorVersion = value
        return self

    def getServerServiceMinorVersion(self) -> Optional[PositiveInteger]:
        """
        Minor version number of the Service.
        """
        return self.serverServiceMinorVersion

    def setServerServiceMinorVersion(self, value: Optional[PositiveInteger]) -> SdServerConfig:
        """
        Minor version number of the Service.
        A None value is a no-op and does not overwrite an existing serverServiceMinorVersion.
        """
        if value is not None:
            self.serverServiceMinorVersion = value
        return self

    def getTtl(self) -> Optional[PositiveInteger]:
        """
        Time to live. Shall be a positive value (sInt32).
        """
        return self.ttl

    def setTtl(self, value: Optional[PositiveInteger]) -> SdServerConfig:
        """
        Time to live. Shall be a positive value (sInt32).
        A None value is a no-op and does not overwrite an existing ttl.
        """
        if value is not None:
            self.ttl = value
        return self


class SdClientConfig(ARObject):
    """
    Client configuration for Service-Discovery.
    """

    # SdClientConfig method parity checklist:
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.172, p.356
    # Spec verified: R4.3.1
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] addCapabilityRecord           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getCapabilityRecords          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] getClientServiceMajorVersion  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setClientServiceMajorVersion  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getClientServiceMinorVersion  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setClientServiceMinorVersion  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getInitialFindBehavior        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setInitialFindBehavior        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getRequestResponseDelay       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setRequestResponseDelay       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getTtl                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setTtl                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1

    def __init__(self):
        super().__init__()

        # A sequence of records to store arbitrary name/value pairs conveying additional information about the named service. Capability records shall only be existing if the respective SdClientConfig is composed by a ConsumedServiceInstance (see constr_3260).
        self.capabilityRecords: List[TagWithOptionalValue] = []

        # Major version number of the Service.
        self.clientServiceMajorVersion: Optional[PositiveInteger] = None

        # Minor version number of the Service.
        self.clientServiceMinorVersion: Optional[PositiveInteger] = None

        # Controls initial find behavior of clients.
        self.initialFindBehavior: Optional[InitialSdDelayConfig] = None

        # Maximum/Minimum allowable response delay to entries received by multicast in seconds.
        self.requestResponseDelay: Optional[RequestResponseDelay] = None

        # TTL for Request and Subscribe messages.
        self.ttl: Optional[PositiveInteger] = None

    def addCapabilityRecord(self, value: Optional[TagWithOptionalValue]) -> SdClientConfig:
        """
        A sequence of records to store arbitrary name/value pairs conveying additional information about the named service. Capability records shall only be existing if the respective SdClientConfig is composed by a ConsumedServiceInstance (see constr_3260).
        A None value is a no-op and does not append to capabilityRecords.
        """
        if value is not None:
            self.capabilityRecords.append(value)
        return self

    def getCapabilityRecords(self) -> List[TagWithOptionalValue]:
        """A sequence of records to store arbitrary name/value pairs conveying additional information about the named service. Capability records shall only be existing if the respective SdClientConfig is composed by a ConsumedServiceInstance (see constr_3260)."""
        return self.capabilityRecords

    def getClientServiceMajorVersion(self) -> Optional[PositiveInteger]:
        """Major version number of the Service."""
        return self.clientServiceMajorVersion

    def setClientServiceMajorVersion(self, value: Optional[PositiveInteger]) -> SdClientConfig:
        """
        Major version number of the Service.
        A None value is a no-op and does not overwrite an existing clientServiceMajorVersion.
        """
        if value is not None:
            self.clientServiceMajorVersion = value
        return self

    def getClientServiceMinorVersion(self) -> Optional[PositiveInteger]:
        """Minor version number of the Service."""
        return self.clientServiceMinorVersion

    def setClientServiceMinorVersion(self, value: Optional[PositiveInteger]) -> SdClientConfig:
        """
        Minor version number of the Service.
        A None value is a no-op and does not overwrite an existing clientServiceMinorVersion.
        """
        if value is not None:
            self.clientServiceMinorVersion = value
        return self

    def getInitialFindBehavior(self) -> Optional[InitialSdDelayConfig]:
        """Controls initial find behavior of clients."""
        return self.initialFindBehavior

    def setInitialFindBehavior(self, value: Optional[InitialSdDelayConfig]) -> SdClientConfig:
        """
        Controls initial find behavior of clients.
        A None value is a no-op and does not overwrite an existing initialFindBehavior.
        """
        if value is not None:
            self.initialFindBehavior = value
        return self

    def getRequestResponseDelay(self) -> Optional[RequestResponseDelay]:
        """Maximum/Minimum allowable response delay to entries received by multicast in seconds."""
        return self.requestResponseDelay

    def setRequestResponseDelay(self, value: Optional[RequestResponseDelay]) -> SdClientConfig:
        """
        Maximum/Minimum allowable response delay to entries received by multicast in seconds.
        A None value is a no-op and does not overwrite an existing requestResponseDelay.
        """
        if value is not None:
            self.requestResponseDelay = value
        return self

    def getTtl(self) -> Optional[PositiveInteger]:
        """TTL for Request and Subscribe messages."""
        return self.ttl

    def setTtl(self, value: Optional[PositiveInteger]) -> SdClientConfig:
        """
        TTL for Request and Subscribe messages.
        A None value is a no-op and does not overwrite an existing ttl.
        """
        if value is not None:
            self.ttl = value
        return self


class Ipv4DhcpServerConfiguration(Describable):
    """
    Defines the configuration of a IPv4 DHCP server that runs on the network endpoint.
    """

    # Ipv4DhcpServerConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.80, p.132
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAddressRangeLowerBound      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAddressRangeLowerBound      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAddressRangeUpperBound      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAddressRangeUpperBound      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDefaultGateway              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultGateway              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDefaultLeaseTime            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultLeaseTime            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addDnsServerAddress            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDnsServerAddresses          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getNetworkMask                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNetworkMask                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Lower range of IP addresses to be issued to DHCP clients. IPv4 Address. Notation: 255.255.255.255.
        self.addressRangeLowerBound: Optional[Ip4AddressString] = None

        # Upper range of IP addresses to be issued to DHCP clients. Pv4 Address. Notation: 255.255.255.255.
        self.addressRangeUpperBound: Optional[Ip4AddressString] = None

        # IP address of the default gateway. Notation 255.255.255.255
        self.defaultGateway: Optional[Ip4AddressString] = None

        # Amount of time in seconds that a client may keep the IP address.
        self.defaultLeaseTime: Optional[TimeValue] = None

        # IP addresses of preconfigured DNS servers. Notation 255.255.255.255 Tags: xml.namePlural=DNS-SERVER-ADDRESSES
        self.dnsServerAddresses: List[Ip4AddressString] = []

        # Default network mask to be used by DHCP clients. Notation 255.255.255.255
        self.networkMask: Optional[Ip4AddressString] = None

    def getAddressRangeLowerBound(self) -> Optional[Ip4AddressString]:
        """Lower range of IP addresses to be issued to DHCP clients. IPv4 Address. Notation: 255.255.255.255."""
        return self.addressRangeLowerBound

    def setAddressRangeLowerBound(self, value: Optional[Ip4AddressString]) -> Ipv4DhcpServerConfiguration:
        """
        Lower range of IP addresses to be issued to DHCP clients. IPv4 Address. Notation: 255.255.255.255.
        A None value is a no-op and does not overwrite an existing addressRangeLowerBound.
        """
        if value is not None:
            self.addressRangeLowerBound = value
        return self

    def getAddressRangeUpperBound(self) -> Optional[Ip4AddressString]:
        """Upper range of IP addresses to be issued to DHCP clients. Pv4 Address. Notation: 255.255.255.255."""
        return self.addressRangeUpperBound

    def setAddressRangeUpperBound(self, value: Optional[Ip4AddressString]) -> Ipv4DhcpServerConfiguration:
        """
        Upper range of IP addresses to be issued to DHCP clients. Pv4 Address. Notation: 255.255.255.255.
        A None value is a no-op and does not overwrite an existing addressRangeUpperBound.
        """
        if value is not None:
            self.addressRangeUpperBound = value
        return self

    def getDefaultGateway(self) -> Optional[Ip4AddressString]:
        """IP address of the default gateway. Notation 255.255.255.255"""
        return self.defaultGateway

    def setDefaultGateway(self, value: Optional[Ip4AddressString]) -> Ipv4DhcpServerConfiguration:
        """
        IP address of the default gateway. Notation 255.255.255.255
        A None value is a no-op and does not overwrite an existing defaultGateway.
        """
        if value is not None:
            self.defaultGateway = value
        return self

    def getDefaultLeaseTime(self) -> Optional[TimeValue]:
        """Amount of time in seconds that a client may keep the IP address."""
        return self.defaultLeaseTime

    def setDefaultLeaseTime(self, value: Optional[TimeValue]) -> Ipv4DhcpServerConfiguration:
        """
        Amount of time in seconds that a client may keep the IP address.
        A None value is a no-op and does not overwrite an existing defaultLeaseTime.
        """
        if value is not None:
            self.defaultLeaseTime = value
        return self

    def addDnsServerAddress(self, value: Optional[Ip4AddressString]) -> Ipv4DhcpServerConfiguration:
        """
        IP addresses of preconfigured DNS servers. Notation 255.255.255.255 Tags: xml.namePlural=DNS-SERVER-ADDRESSES
        A None value is a no-op and does not append to dnsServerAddresses.
        """
        if value is not None:
            self.dnsServerAddresses.append(value)
        return self

    def getDnsServerAddresses(self) -> List[Ip4AddressString]:
        """IP addresses of preconfigured DNS servers. Notation 255.255.255.255 Tags: xml.namePlural=DNS-SERVER-ADDRESSES"""
        return self.dnsServerAddresses

    def getNetworkMask(self) -> Optional[Ip4AddressString]:
        """Default network mask to be used by DHCP clients. Notation 255.255.255.255"""
        return self.networkMask

    def setNetworkMask(self, value: Optional[Ip4AddressString]) -> Ipv4DhcpServerConfiguration:
        """
        Default network mask to be used by DHCP clients. Notation 255.255.255.255
        A None value is a no-op and does not overwrite an existing networkMask.
        """
        if value is not None:
            self.networkMask = value
        return self


class Ipv6DhcpServerConfiguration(Describable):
    """
    Defines the configuration of a IPv6 DHCP server that runs on the network endpoint.
    """

    # Ipv6DhcpServerConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.81, p.132
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAddressRangeLowerBound      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAddressRangeLowerBound      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAddressRangeUpperBound      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAddressRangeUpperBound      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDefaultGateway              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultGateway              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDefaultLeaseTime            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultLeaseTime            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addDnsServerAddress            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDnsServerAddresses          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getNetworkMask                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNetworkMask                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Lower range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF.
        self.addressRangeLowerBound: Optional[Ip6AddressString] = None

        # Upper range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF.
        self.addressRangeUpperBound: Optional[Ip6AddressString] = None

        # IP address of the default gateway. Notation 255.255.255.255
        self.defaultGateway: Optional[Ip6AddressString] = None

        # Amount of time in seconds that a client may keep the IP address.
        self.defaultLeaseTime: Optional[TimeValue] = None

        # IP addresses of preconfigured DNS servers. Notation: FFFF:...:FFFF. Tags: xml.namePlural=DNS-SERVER-ADDRESSES
        self.dnsServerAddresses: List[Ip6AddressString] = []

        # Default network mask to be used by DHCP clients. Notation 255.255.255.255
        self.networkMask: Optional[Ip6AddressString] = None

    def getAddressRangeLowerBound(self) -> Optional[Ip6AddressString]:
        """Lower range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF."""
        return self.addressRangeLowerBound

    def setAddressRangeLowerBound(self, value: Optional[Ip6AddressString]) -> Ipv6DhcpServerConfiguration:
        """
        Lower range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF.
        A None value is a no-op and does not overwrite an existing addressRangeLowerBound.
        """
        if value is not None:
            self.addressRangeLowerBound = value
        return self

    def getAddressRangeUpperBound(self) -> Optional[Ip6AddressString]:
        """Upper range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF."""
        return self.addressRangeUpperBound

    def setAddressRangeUpperBound(self, value: Optional[Ip6AddressString]) -> Ipv6DhcpServerConfiguration:
        """
        Upper range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF.
        A None value is a no-op and does not overwrite an existing addressRangeUpperBound.
        """
        if value is not None:
            self.addressRangeUpperBound = value
        return self

    def getDefaultGateway(self) -> Optional[Ip6AddressString]:
        """IP address of the default gateway. Notation 255.255.255.255"""
        return self.defaultGateway

    def setDefaultGateway(self, value: Optional[Ip6AddressString]) -> Ipv6DhcpServerConfiguration:
        """
        IP address of the default gateway. Notation 255.255.255.255
        A None value is a no-op and does not overwrite an existing defaultGateway.
        """
        if value is not None:
            self.defaultGateway = value
        return self

    def getDefaultLeaseTime(self) -> Optional[TimeValue]:
        """Amount of time in seconds that a client may keep the IP address."""
        return self.defaultLeaseTime

    def setDefaultLeaseTime(self, value: Optional[TimeValue]) -> Ipv6DhcpServerConfiguration:
        """
        Amount of time in seconds that a client may keep the IP address.
        A None value is a no-op and does not overwrite an existing defaultLeaseTime.
        """
        if value is not None:
            self.defaultLeaseTime = value
        return self

    def addDnsServerAddress(self, value: Optional[Ip6AddressString]) -> Ipv6DhcpServerConfiguration:
        """
        IP addresses of preconfigured DNS servers. Notation: FFFF:...:FFFF. Tags: xml.namePlural=DNS-SERVER-ADDRESSES
        A None value is a no-op and does not append to dnsServerAddresses.
        """
        if value is not None:
            self.dnsServerAddresses.append(value)
        return self

    def getDnsServerAddresses(self) -> List[Ip6AddressString]:
        """IP addresses of preconfigured DNS servers. Notation: FFFF:...:FFFF. Tags: xml.namePlural=DNS-SERVER-ADDRESSES"""
        return self.dnsServerAddresses

    def getNetworkMask(self) -> Optional[Ip6AddressString]:
        """Default network mask to be used by DHCP clients. Notation 255.255.255.255"""
        return self.networkMask

    def setNetworkMask(self, value: Optional[Ip6AddressString]) -> Ipv6DhcpServerConfiguration:
        """
        Default network mask to be used by DHCP clients. Notation 255.255.255.255
        A None value is a no-op and does not overwrite an existing networkMask.
        """
        if value is not None:
            self.networkMask = value
        return self


class DhcpServerConfiguration(ARObject):
    """
    Defines the configuration of DHCP servers that are running on the network endpoint. It is possible that an Ipv4DhcpServer and an Ipv6DhcpServer run on the same Ecu.
    """

    # DhcpServerConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.79, p.131
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIpv4DhcpServerConfiguration    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv4DhcpServerConfiguration    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpv6DhcpServerConfiguration    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv6DhcpServerConfiguration    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Configuration of a IPv4 DHCP server that runs on the network endpoint.
        self.ipv4DhcpServerConfiguration: Optional[Ipv4DhcpServerConfiguration] = None

        # Configuration of a IPv6 DHCP server that runs on the network endpoint.
        self.ipv6DhcpServerConfiguration: Optional[Ipv6DhcpServerConfiguration] = None

    def getIpv4DhcpServerConfiguration(self) -> Optional[Ipv4DhcpServerConfiguration]:
        """Configuration of a IPv4 DHCP server that runs on the network endpoint."""
        return self.ipv4DhcpServerConfiguration

    def setIpv4DhcpServerConfiguration(self, value: Optional[Ipv4DhcpServerConfiguration]) -> DhcpServerConfiguration:
        """
        Configuration of a IPv4 DHCP server that runs on the network endpoint.
        A None value is a no-op and does not overwrite an existing ipv4DhcpServerConfiguration.
        """
        if value is not None:
            self.ipv4DhcpServerConfiguration = value
        return self

    def getIpv6DhcpServerConfiguration(self) -> Optional[Ipv6DhcpServerConfiguration]:
        """Configuration of a IPv6 DHCP server that runs on the network endpoint."""
        return self.ipv6DhcpServerConfiguration

    def setIpv6DhcpServerConfiguration(self, value: Optional[Ipv6DhcpServerConfiguration]) -> DhcpServerConfiguration:
        """
        Configuration of a IPv6 DHCP server that runs on the network endpoint.
        A None value is a no-op and does not overwrite an existing ipv6DhcpServerConfiguration.
        """
        if value is not None:
            self.ipv6DhcpServerConfiguration = value
        return self


class CouplingPortTrafficClassAssignment(Referrable):
    """
    Defines the assignment of Traffic Class to a frame.
    """

    # CouplingPortTrafficClassAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.75, p.128
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addPriority               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPriorities             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getTrafficClass           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTrafficClass           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Defines a priority which is mapped onto a Traffic Class.
        self.priorities: List[PositiveInteger] = []

        # Defines the Traffic Class which is assigned. range: 0-7
        self.trafficClass: Optional[PositiveInteger] = None

    def addPriority(self, value: Optional[PositiveInteger]) -> CouplingPortTrafficClassAssignment:
        """
        Defines a priority which is mapped onto a Traffic Class.
        A None value is a no-op and does not append to priorities.
        """
        if value is not None:
            self.priorities.append(value)
        return self

    def getPriorities(self) -> List[PositiveInteger]:
        """Defines a priority which is mapped onto a Traffic Class."""
        return self.priorities

    def getTrafficClass(self) -> Optional[PositiveInteger]:
        """Defines the Traffic Class which is assigned. range: 0-7"""
        return self.trafficClass

    def setTrafficClass(self, value: Optional[PositiveInteger]) -> CouplingPortTrafficClassAssignment:
        """
        Defines the Traffic Class which is assigned. range: 0-7
        A None value is a no-op and does not overwrite an existing trafficClass.
        """
        if value is not None:
            self.trafficClass = value
        return self


class ApplicationEndpoint(Identifiable):
    """An application endpoint is the endpoint on an Ecu in terms of application addressing (e.g. socket). The application endpoint represents e.g. the listen socket in client-server-based communication."""

    # ApplicationEndpoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.124, p.458
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createConsumedServiceInstance        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConsumedServiceInstances          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getMaxNumberOfConnections            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxNumberOfConnections            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkEndpointRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNetworkEndpointRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPriority                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPriority                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createProvidedServiceInstance        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProvidedServiceInstances          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getTlsCryptoMappingRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTlsCryptoMappingRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTpConfiguration                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTpConfiguration                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Consumed service instances.
        self.consumedServiceInstances: List[ConsumedServiceInstance] = []

        # This attribute defines the maximal number of clients the Server is able to deal with in case of Service Discovery.
        self.maxNumberOfConnections: Optional[PositiveInteger] = None

        # Reference to the network address.
        self.networkEndpointRef: Optional[RefType] = None

        # Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        self.priority: Optional[PositiveInteger] = None

        # Provided service instances.
        self.providedServiceInstances: List[ProvidedServiceInstance] = []

        # This reference identifies the applicable TlsCryptoServiceMapping that adds the ability for TLS-based encryption on the enclosing ApplicationEndpoint.
        self.tlsCryptoMappingRef: Optional[RefType] = None

        # Configuration of the used transport protocol.
        self.tpConfiguration: Optional[TransportProtocolConfiguration] = None

    def createConsumedServiceInstance(self, short_name: str) -> ConsumedServiceInstance:
        """Consumed service instances."""
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ConsumedServiceInstance

        if not self.IsReferrableElementExists(short_name, ConsumedServiceInstance):
            instance = ConsumedServiceInstance(self, short_name)
            self.addReferrableElement(instance)
            self.consumedServiceInstances.append(instance)
        return cast(ConsumedServiceInstance, self.getReferrableElement(short_name, ConsumedServiceInstance))

    def getConsumedServiceInstances(self) -> List[ConsumedServiceInstance]:
        """Consumed service instances."""
        return self.consumedServiceInstances

    def getMaxNumberOfConnections(self) -> Optional[PositiveInteger]:
        """This attribute defines the maximal number of clients the Server is able to deal with in case of Service Discovery."""
        return self.maxNumberOfConnections

    def setMaxNumberOfConnections(self, value: Optional[PositiveInteger]) -> ApplicationEndpoint:
        """
        This attribute defines the maximal number of clients the Server is able to deal with in case of Service Discovery.
        A None value is a no-op and does not overwrite an existing maxNumberOfConnections.
        """
        if value is not None:
            self.maxNumberOfConnections = value
        return self

    def getNetworkEndpointRef(self) -> Optional[RefType]:
        """Reference to the network address."""
        return self.networkEndpointRef

    def setNetworkEndpointRef(self, value: Optional[RefType]) -> ApplicationEndpoint:
        """
        Reference to the network address.
        A None value is a no-op and does not overwrite an existing networkEndpointRef.
        """
        if value is not None:
            self.networkEndpointRef = value
        return self

    def getPriority(self) -> Optional[PositiveInteger]:
        """Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed."""
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> ApplicationEndpoint:
        """
        Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def createProvidedServiceInstance(self, short_name: str) -> ProvidedServiceInstance:
        """Provided service instances."""
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ProvidedServiceInstance

        if not self.IsReferrableElementExists(short_name, ProvidedServiceInstance):
            instance = ProvidedServiceInstance(self, short_name)
            self.addReferrableElement(instance)
            self.providedServiceInstances.append(instance)
        return cast(ProvidedServiceInstance, self.getReferrableElement(short_name, ProvidedServiceInstance))

    def getProvidedServiceInstances(self) -> List[ProvidedServiceInstance]:
        """Provided service instances."""
        return self.providedServiceInstances

    def getTlsCryptoMappingRef(self) -> Optional[RefType]:
        """This reference identifies the applicable TlsCryptoServiceMapping that adds the ability for TLS-based encryption on the enclosing ApplicationEndpoint."""
        return self.tlsCryptoMappingRef

    def setTlsCryptoMappingRef(self, value: Optional[RefType]) -> ApplicationEndpoint:
        """
        This reference identifies the applicable TlsCryptoServiceMapping that adds the ability for TLS-based encryption on the enclosing ApplicationEndpoint.
        A None value is a no-op and does not overwrite an existing tlsCryptoMappingRef.
        """
        if value is not None:
            self.tlsCryptoMappingRef = value
        return self

    def getTpConfiguration(self) -> Optional[TransportProtocolConfiguration]:
        """Configuration of the used transport protocol."""
        return self.tpConfiguration

    def setTpConfiguration(self, value: Optional[TransportProtocolConfiguration]) -> ApplicationEndpoint:
        """
        Configuration of the used transport protocol.
        A None value is a no-op and does not overwrite an existing tpConfiguration.
        """
        if value is not None:
            self.tpConfiguration = value
        return self


class NetworkEndpointAddress(ARObject, ABC):
    """
    To build a valid network endpoint address there has to be either one MAC multicast group reference or an ipv4 configuration or an ipv6 configuration.
    """

    # NetworkEndpointAddress method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.135, p.464
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is NetworkEndpointAddress:
            raise TypeError("NetworkEndpointAddress is an abstract class.")

        super().__init__()


class Ipv4AddressSourceEnum(AREnum):
    """
    Defines how the node obtains its IPv4-Address.
    """

    # Ipv4AddressSourceEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.137, p.465
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Ipv4Configuration.ipv4AddressSource
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # AutoIP is used to dynamically assign IP addresses at device startup. Tags: atp.EnumerationLiteralIndex=0
    AUTO_IP = "AUTO-IP"

    # Linklocal IPv4 Address Assignment using DoIP Parameters Tags: atp.EnumerationLiteralIndex=2 xml.name=AUTO-IP-DOIP
    AUTO_IP_DOIP = "AUTO-IP--DOIP"

    # DHCP is a service for the automatic IP configuration of a client. Tags: atp.EnumerationLiteralIndex=3
    DHCPV4 = "DHCPV-4"

    # The IP Address shall be declared manually. Tags: atp.EnumerationLiteralIndex=4
    FIXED = "FIXED"

    def __init__(self):
        super().__init__([Ipv4AddressSourceEnum.AUTO_IP, Ipv4AddressSourceEnum.AUTO_IP_DOIP, Ipv4AddressSourceEnum.DHCPV4, Ipv4AddressSourceEnum.FIXED])


class Ipv4Configuration(NetworkEndpointAddress):
    """
    Internet Protocol version 4 (IPv4) configuration.
    """

    # Ipv4Configuration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.136, p.465
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAssignmentPriority     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAssignmentPriority     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDefaultGateway         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultGateway         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addDnsServerAddress       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDnsServerAddresses     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getIpAddressKeepBehavior  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpAddressKeepBehavior  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpv4Address            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv4Address            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpv4AddressSource      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv4AddressSource      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNetworkMask            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNetworkMask            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTtl                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTtl                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority.
        self.assignmentPriority: Optional[PositiveInteger] = None

        # IP address of the default gateway.
        self.defaultGateway: Optional[Ip4AddressString] = None

        # IP addresses of preconfigured DNS servers. Tags: xml.namePlural=DNS-SERVER-ADDRESSES
        self.dnsServerAddresses: List[Ip4AddressString] = []

        # Defines the lifetime of a dynamically fetched IP address.
        self.ipAddressKeepBehavior: Optional[IpAddressKeepEnum] = None

        # IPv4 Address. Notation: 255.255.255.255. The IP Address shall be declared in case the ipv4AddressSource is FIXED and thus no auto-configuration mechanism is used.
        self.ipv4Address: Optional[Ip4AddressString] = None

        # Defines how the node obtains its IP address.
        self.ipv4AddressSource: Optional[Ipv4AddressSourceEnum] = None

        # Network mask. Notation 255.255.255.255
        self.networkMask: Optional[Ip4AddressString] = None

        # Lifespan of data (0..255). The purpose of the TimeToLive field is to avoid a situation in which an undeliverable datagram keeps circulating on a system.
        self.ttl: Optional[PositiveInteger] = None

    def getAssignmentPriority(self) -> Optional[PositiveInteger]:
        """
        Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority.
        """
        return self.assignmentPriority

    def setAssignmentPriority(self, value: Optional[PositiveInteger]) -> Ipv4Configuration:
        """
        Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority.
        A None value is a no-op and does not overwrite an existing assignmentPriority.
        """
        if value is not None:
            self.assignmentPriority = value
        return self

    def getDefaultGateway(self) -> Optional[Ip4AddressString]:
        """
        IP address of the default gateway.
        """
        return self.defaultGateway

    def setDefaultGateway(self, value: Optional[Ip4AddressString]) -> Ipv4Configuration:
        """
        IP address of the default gateway.
        A None value is a no-op and does not overwrite an existing defaultGateway.
        """
        if value is not None:
            self.defaultGateway = value
        return self

    def addDnsServerAddress(self, value: Optional[Ip4AddressString]) -> Ipv4Configuration:
        """
        IP addresses of preconfigured DNS servers. Tags: xml.namePlural=DNS-SERVER-ADDRESSES
        A None value is a no-op and is not appended to dnsServerAddresses.
        """
        if value is not None:
            self.dnsServerAddresses.append(value)
        return self

    def getDnsServerAddresses(self) -> List[Ip4AddressString]:
        """
        IP addresses of preconfigured DNS servers. Tags: xml.namePlural=DNS-SERVER-ADDRESSES
        """
        return self.dnsServerAddresses

    def getIpAddressKeepBehavior(self) -> Optional[IpAddressKeepEnum]:
        """
        Defines the lifetime of a dynamically fetched IP address.
        """
        return self.ipAddressKeepBehavior

    def setIpAddressKeepBehavior(self, value: Optional[IpAddressKeepEnum]) -> Ipv4Configuration:
        """
        Defines the lifetime of a dynamically fetched IP address.
        A None value is a no-op and does not overwrite an existing ipAddressKeepBehavior.
        """
        if value is not None:
            self.ipAddressKeepBehavior = value
        return self

    def getIpv4Address(self) -> Optional[Ip4AddressString]:
        """
        IPv4 Address. Notation: 255.255.255.255. The IP Address shall be declared in case the ipv4AddressSource is FIXED and thus no auto-configuration mechanism is used.
        """
        return self.ipv4Address

    def setIpv4Address(self, value: Optional[Ip4AddressString]) -> Ipv4Configuration:
        """
        IPv4 Address. Notation: 255.255.255.255. The IP Address shall be declared in case the ipv4AddressSource is FIXED and thus no auto-configuration mechanism is used.
        A None value is a no-op and does not overwrite an existing ipv4Address.
        """
        if value is not None:
            self.ipv4Address = value
        return self

    def getIpv4AddressSource(self) -> Optional[Ipv4AddressSourceEnum]:
        """
        Defines how the node obtains its IP address.
        """
        return self.ipv4AddressSource

    def setIpv4AddressSource(self, value: Optional[Ipv4AddressSourceEnum]) -> Ipv4Configuration:
        """
        Defines how the node obtains its IP address.
        A None value is a no-op and does not overwrite an existing ipv4AddressSource.
        """
        if value is not None:
            self.ipv4AddressSource = value
        return self

    def getNetworkMask(self) -> Optional[Ip4AddressString]:
        """
        Network mask. Notation 255.255.255.255
        """
        return self.networkMask

    def setNetworkMask(self, value: Optional[Ip4AddressString]) -> Ipv4Configuration:
        """
        Network mask. Notation 255.255.255.255
        A None value is a no-op and does not overwrite an existing networkMask.
        """
        if value is not None:
            self.networkMask = value
        return self

    def getTtl(self) -> Optional[PositiveInteger]:
        """
        Lifespan of data (0..255). The purpose of the TimeToLive field is to avoid a situation in which an undeliverable datagram keeps circulating on a system.
        """
        return self.ttl

    def setTtl(self, value: Optional[PositiveInteger]) -> Ipv4Configuration:
        """
        Lifespan of data (0..255). The purpose of the TimeToLive field is to avoid a situation in which an undeliverable datagram keeps circulating on a system.
        A None value is a no-op and does not overwrite an existing ttl.
        """
        if value is not None:
            self.ttl = value
        return self


class IpAddressKeepEnum(AREnum):
    """
    Defines the behavior after a dynamic IP address has been assigned.
    """

    # IpAddressKeepEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.138, p.466
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Ipv4Configuration/Ipv6Configuration.ipAddressKeepBehavior
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # After a dynamic IP address has been assigned just use it for this session. Tags: atp.EnumerationLiteralIndex=0
    FORGET = "FORGET"

    # After a dynamic IP address has been assigned store the address persistently. Tags: atp.EnumerationLiteralIndex=1
    STORE_PERSISTENTLY = "STORE-PERSISTENTLY"

    def __init__(self):
        super().__init__(
            [
                IpAddressKeepEnum.FORGET,
                IpAddressKeepEnum.STORE_PERSISTENTLY,
            ]
        )


class Ipv6AddressSourceEnum(AREnum):
    """
    Defines how the node obtains its IPv6-Address.
    """

    # Ipv6AddressSourceEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.140, p.467
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Ipv6Configuration.ipv6AddressSource
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # DHCP is a service for the automatic IP configuration of a client. Tags: atp.EnumerationLiteralIndex=0
    DHCPV6 = "DHCPV-6"

    # The IP Address shall be declared manually. Tags: atp.EnumerationLiteralIndex=1
    FIXED = "FIXED"

    # LinkLocal is intended only for communications within the segment of a local network (a link) or a point-to-point connection that a host is connected to. Tags: atp.EnumerationLiteralIndex=2
    LINK_LOCAL = "LINK-LOCAL"

    # Linklocal IPv6 Address Assignment using DoIP Parameters Tags: atp.EnumerationLiteralIndex=3 xml.name=LINK-LOCAL-DOIP
    LINK_LOCAL_DOIP = "LINK-LOCAL--DOIP"

    # IPv6 Stateless Autoconfiguration. Tags: atp.EnumerationLiteralIndex=4
    ROUTER_ADVERTISEMENT = "ROUTER-ADVERTISEMENT"

    def __init__(self):
        super().__init__(
            [
                Ipv6AddressSourceEnum.DHCPV6,
                Ipv6AddressSourceEnum.FIXED,
                Ipv6AddressSourceEnum.LINK_LOCAL,
                Ipv6AddressSourceEnum.LINK_LOCAL_DOIP,
                Ipv6AddressSourceEnum.ROUTER_ADVERTISEMENT,
            ]
        )


class CouplingElementEnum(AREnum):
    """
    Identifies the Coupling type.
    """

    # CouplingElementEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.53, p.108
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingElement.couplingType
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # A device that is used to connect segments of a LAN. In Hubs frames are "broadcasted" to every one of its ports. Tags: atp.EnumerationLiteralIndex=0
    HUB = "HUB"

    # A device that routes frames between different networks. Tags: atp.EnumerationLiteralIndex=1
    ROUTER = "ROUTER"

    # A device that filters and forwards frames between different LAN segments. Tags: atp.EnumerationLiteralIndex=2
    SWITCH = "SWITCH"

    def __init__(self):
        super().__init__(
            [
                CouplingElementEnum.HUB,
                CouplingElementEnum.ROUTER,
                CouplingElementEnum.SWITCH,
            ]
        )


class EthernetConnectionNegotiationEnum(AREnum):
    """
    Specifies connection negotiation types of Ethernet transceiver links.
    """

    # EthernetConnectionNegotiationEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.55, p.110
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPort.connectionNegotiationBehavior
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Automatic Negotiation Tags: atp.EnumerationLiteralIndex=0
    AUTO = "AUTO"

    # Master Tags: atp.EnumerationLiteralIndex=1
    MASTER = "MASTER"

    # Slave Tags: atp.EnumerationLiteralIndex=2
    SLAVE = "SLAVE"

    def __init__(self):
        super().__init__(
            [
                EthernetConnectionNegotiationEnum.AUTO,
                EthernetConnectionNegotiationEnum.MASTER,
                EthernetConnectionNegotiationEnum.SLAVE,
            ]
        )


class CouplingPortRoleEnum(AREnum):
    """
    Defines the role a CouplingPort takes in the context of a CouplingElement.
    """

    # CouplingPortRoleEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.38, p.2013
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPort.couplingPortRole

    # The hostPort is connected to an ECU (host ecu). The host ECU controls the connected Coupling Element (e.g. Ethernet switch). Tags: atp.EnumerationLiteralIndex=0
    HOST_PORT = "HOST-PORT"

    # A CoupingPort can be a standardPort that is used to connect the CouplingElement with Coupling Ports outside the ECU. Tags: atp.EnumerationLiteralIndex=2
    STANDARD_PORT = "STANDARD-PORT"

    # A CouplingPort can be connected to another CouplingPort of a CouplingElement located on the same ECU (CouplingElement.ecuInstance) using the CouplingPortConnection. This is used to model a cascaded switch. Tags: atp.EnumerationLiteralIndex=1
    UP_LINK_PORT = "UP-LINK-PORT"

    def __init__(self):
        super().__init__(
            [
                CouplingPortRoleEnum.HOST_PORT,
                CouplingPortRoleEnum.STANDARD_PORT,
                CouplingPortRoleEnum.UP_LINK_PORT,
            ]
        )


class EthernetMacLayerTypeEnum(AREnum):
    """
    Specifies MAC (Media Access Control) Layer types.
    """

    # EthernetMacLayerTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.56, p.110
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPort.macLayerType, EthernetCommunicationController.macLayerType
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Mac layer interface (data) bandwith class 100Mbit/s and 10Mbit/s (e.g. RMII, RvMII, SMII, RvMII) Tags: atp.EnumerationLiteralIndex=0 xml.name=X-MII
    XMII = "X-MII"

    # Mac layer interface (data) bandwith class 1Gbit/s (e.g. GMII, RGMII, SGMII, RvGMII, USGMII) Tags: atp.EnumerationLiteralIndex=1 xml.name=XG-MII
    XGMII = "XG-MII"

    # Mac layer interface (data) bandwith class 10Gbit/s Tags: atp.EnumerationLiteralIndex=2 xml.name=XXG-MII
    XXGMII = "XXG-MII"

    def __init__(self):
        super().__init__(
            [
                EthernetMacLayerTypeEnum.XMII,
                EthernetMacLayerTypeEnum.XGMII,
                EthernetMacLayerTypeEnum.XXGMII,
            ]
        )


class EthernetCouplingPortSchedulerEnum(AREnum):
    """
    Defines the schedule algorithm to be used.
    """

    # EthernetCouplingPortSchedulerEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.66, p.123
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPortScheduler.portScheduler
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Schedule algorithm "deficit round robin" Tags: atp.EnumerationLiteralIndex=0
    DEFICIT_ROUND_ROBIN = "DEFICIT-ROUND-ROBIN"

    # Schedule algorithm "strict priority" Tags: atp.EnumerationLiteralIndex=1
    STRICT_PRIORITY = "STRICT-PRIORITY"

    # Schedule algorithm "weighted round robin" Tags: atp.EnumerationLiteralIndex=2
    WEIGHTED_ROUND_ROBIN = "WEIGHTED-ROUND-ROBIN"

    def __init__(self):
        super().__init__(
            [
                EthernetCouplingPortSchedulerEnum.DEFICIT_ROUND_ROBIN,
                EthernetCouplingPortSchedulerEnum.STRICT_PRIORITY,
                EthernetCouplingPortSchedulerEnum.WEIGHTED_ROUND_ROBIN,
            ]
        )


class EthernetSwitchVlanEgressTaggingEnum(AREnum):
    """
    Defines the VLAN tag sending behavior.
    """

    # EthernetSwitchVlanEgressTaggingEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.78, p.130
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on VlanMembership.sendActivity
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # will not be sent Tags: atp.EnumerationLiteralIndex=0
    NOT_SENT = "NOT-SENT"

    # sent with its VLAN tag Tags: atp.EnumerationLiteralIndex=1
    SENT_TAGGED = "SENT-TAGGED"

    # sent without a VLAN tag Tags: atp.EnumerationLiteralIndex=2
    SENT_UNTAGGED = "SENT-UNTAGGED"

    def __init__(self):
        super().__init__(
            [
                EthernetSwitchVlanEgressTaggingEnum.NOT_SENT,
                EthernetSwitchVlanEgressTaggingEnum.SENT_TAGGED,
                EthernetSwitchVlanEgressTaggingEnum.SENT_UNTAGGED,
            ]
        )


class Ipv6Configuration(NetworkEndpointAddress):
    """
    Internet Protocol version 6 (IPv6) configuration.
    """

    # Ipv6Configuration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.139, p.466
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAssignmentPriority        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAssignmentPriority        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDefaultRouter             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultRouter             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDnsServerAddresses        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addDnsServerAddress          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEnableAnycast             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEnableAnycast             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHopCount                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHopCount                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIpAddressKeepBehavior     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIpAddressKeepBehavior     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIpAddressPrefixLength     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIpAddressPrefixLength     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIpv6Address               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIpv6Address               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIpv6AddressSource         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIpv6AddressSource         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority.
        self.assignmentPriority: Optional[PositiveInteger] = None

        # IP address of the default router.
        self.defaultRouter: Optional[Ip6AddressString] = None

        # IP addresses of pre configured DNS servers.
        self.dnsServerAddresses: List[Ip6AddressString] = []

        # This attribute is used to enable anycast addressing (i.e. to one of multiple receivers).
        self.enableAnycast: Optional[Boolean] = None

        # The distance between two hosts. The hop count n means that n gateways separate the source host from the destination host (Range 0..255)
        self.hopCount: Optional[PositiveInteger] = None

        # Defines the lifetime of a dynamically fetched IP address.
        self.ipAddressKeepBehavior: Optional[IpAddressKeepEnum] = None

        # IPv6 prefix length defines the part of the IPv6 address that is the network prefix.
        self.ipAddressPrefixLength: Optional[PositiveInteger] = None

        # IPv6 Address. Notation: FFFF:...:FFFF. The IP Address shall be declared in case the ipv6AddressSource is FIXED and thus no auto-configuration mechanism is used.
        self.ipv6Address: Optional[Ip6AddressString] = None

        # Defines how the node obtains its IP address.
        self.ipv6AddressSource: Optional[Ipv6AddressSourceEnum] = None

    def getAssignmentPriority(self) -> Optional[PositiveInteger]:
        """Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority."""
        return self.assignmentPriority

    def setAssignmentPriority(self, value: Optional[PositiveInteger]) -> Ipv6Configuration:
        """
        Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority.
        A None value is a no-op and does not overwrite an existing assignmentPriority.
        """
        if value is not None:
            self.assignmentPriority = value
        return self

    def getDefaultRouter(self) -> Optional[Ip6AddressString]:
        """IP address of the default router."""
        return self.defaultRouter

    def setDefaultRouter(self, value: Optional[Ip6AddressString]) -> Ipv6Configuration:
        """
        IP address of the default router.
        A None value is a no-op and does not overwrite an existing defaultRouter.
        """
        if value is not None:
            self.defaultRouter = value
        return self

    def getDnsServerAddresses(self) -> List[Ip6AddressString]:
        """IP addresses of pre configured DNS servers."""
        return self.dnsServerAddresses

    def addDnsServerAddress(self, value: Optional[Ip6AddressString]) -> Ipv6Configuration:
        """
        IP addresses of pre configured DNS servers.
        A None value is a no-op and does not append to dnsServerAddresses.
        """
        if value is not None:
            self.dnsServerAddresses.append(value)
        return self

    def getEnableAnycast(self) -> Optional[Boolean]:
        """This attribute is used to enable anycast addressing (i.e. to one of multiple receivers)."""
        return self.enableAnycast

    def setEnableAnycast(self, value: Optional[Boolean]) -> Ipv6Configuration:
        """
        This attribute is used to enable anycast addressing (i.e. to one of multiple receivers).
        A None value is a no-op and does not overwrite an existing enableAnycast.
        """
        if value is not None:
            self.enableAnycast = value
        return self

    def getHopCount(self) -> Optional[PositiveInteger]:
        """The distance between two hosts. The hop count n means that n gateways separate the source host from the destination host (Range 0..255)"""
        return self.hopCount

    def setHopCount(self, value: Optional[PositiveInteger]) -> Ipv6Configuration:
        """
        The distance between two hosts. The hop count n means that n gateways separate the source host from the destination host (Range 0..255)
        A None value is a no-op and does not overwrite an existing hopCount.
        """
        if value is not None:
            self.hopCount = value
        return self

    def getIpAddressKeepBehavior(self) -> Optional[IpAddressKeepEnum]:
        """Defines the lifetime of a dynamically fetched IP address."""
        return self.ipAddressKeepBehavior

    def setIpAddressKeepBehavior(self, value: Optional[IpAddressKeepEnum]) -> Ipv6Configuration:
        """
        Defines the lifetime of a dynamically fetched IP address.
        A None value is a no-op and does not overwrite an existing ipAddressKeepBehavior.
        """
        if value is not None:
            self.ipAddressKeepBehavior = value
        return self

    def getIpAddressPrefixLength(self) -> Optional[PositiveInteger]:
        """IPv6 prefix length defines the part of the IPv6 address that is the network prefix."""
        return self.ipAddressPrefixLength

    def setIpAddressPrefixLength(self, value: Optional[PositiveInteger]) -> Ipv6Configuration:
        """
        IPv6 prefix length defines the part of the IPv6 address that is the network prefix.
        A None value is a no-op and does not overwrite an existing ipAddressPrefixLength.
        """
        if value is not None:
            self.ipAddressPrefixLength = value
        return self

    def getIpv6Address(self) -> Optional[Ip6AddressString]:
        """IPv6 Address. Notation: FFFF:...:FFFF. The IP Address shall be declared in case the ipv6AddressSource is FIXED and thus no auto-configuration mechanism is used."""
        return self.ipv6Address

    def setIpv6Address(self, value: Optional[Ip6AddressString]) -> Ipv6Configuration:
        """
        IPv6 Address. Notation: FFFF:...:FFFF. The IP Address shall be declared in case the ipv6AddressSource is FIXED and thus no auto-configuration mechanism is used.
        A None value is a no-op and does not overwrite an existing ipv6Address.
        """
        if value is not None:
            self.ipv6Address = value
        return self

    def getIpv6AddressSource(self) -> Optional[Ipv6AddressSourceEnum]:
        """Defines how the node obtains its IP address."""
        return self.ipv6AddressSource

    def setIpv6AddressSource(self, value: Optional[Ipv6AddressSourceEnum]) -> Ipv6Configuration:
        """
        Defines how the node obtains its IP address.
        A None value is a no-op and does not overwrite an existing ipv6AddressSource.
        """
        if value is not None:
            self.ipv6AddressSource = value
        return self


class DoIpEntity(ARObject):
    """
    ECU providing this infrastructure service is a DoIP-Entity.
    """

    # DoIpEntity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.150, p.471
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDoIpEntityRole    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDoIpEntityRole    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Identifies the role in terms of DoIP this network-node has.
        self.doIpEntityRole: Optional[DoIpEntityRoleEnum] = None

    def getDoIpEntityRole(self) -> Optional[DoIpEntityRoleEnum]:
        """
        Identifies the role in terms of DoIP this network-node has.
        """
        return self.doIpEntityRole

    def setDoIpEntityRole(self, value: Optional[DoIpEntityRoleEnum]) -> DoIpEntity:
        """
        Identifies the role in terms of DoIP this network-node has.
        A None value is a no-op and does not overwrite an existing doIpEntityRole.
        """
        if value is not None:
            self.doIpEntityRole = value
        return self


class OrderedMaster(ARObject):
    """Element in the network endpoint list."""

    # OrderedMaster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.148, p.470
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getIndex                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] setIndex                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeSyncServerRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] setTimeSyncServerRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Defines the order of the network endpoint list (e.g. 0, 1, 2, ...).
        self.index: Optional[PositiveInteger] = None

        # Reference to a master (Time Sync Server).
        self.timeSyncServerRef: Optional[RefType] = None

    def getIndex(self) -> Optional[PositiveInteger]:
        """Defines the order of the network endpoint list (e.g. 0, 1, 2, ...)."""
        return self.index

    def setIndex(self, value: Optional[PositiveInteger]) -> OrderedMaster:
        """
        Defines the order of the network endpoint list (e.g. 0, 1, 2, ...).
        A None value is a no-op and does not overwrite an existing index.
        """
        if value is not None:
            self.index = value
        return self

    def getTimeSyncServerRef(self) -> Optional[RefType]:
        """Reference to a master (Time Sync Server)."""
        return self.timeSyncServerRef

    def setTimeSyncServerRef(self, value: Optional[RefType]) -> OrderedMaster:
        """
        Reference to a master (Time Sync Server).
        A None value is a no-op and does not overwrite an existing timeSyncServerRef.
        """
        if value is not None:
            self.timeSyncServerRef = value
        return self


class TimeSyncClientConfiguration(ARObject):
    """
    Defines the configuration of the time synchronisation client.
    """

    # TimeSyncClientConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.146, p.470
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOrderedMasters       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addOrderedMaster        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeSyncTechnology   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeSyncTechnology   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Defines a list of ordered NetworkEndpoints. Tags: xml.namePlural=ORDERED-MASTER-LIST
        self.orderedMasters: List[OrderedMaster] = []

        # Defines the time synchronisation technology used.
        self.timeSyncTechnology: Optional[TimeSyncTechnologyEnum] = None

    def getOrderedMasters(self) -> List[OrderedMaster]:
        """
        Defines a list of ordered NetworkEndpoints. Tags: xml.namePlural=ORDERED-MASTER-LIST
        """
        return self.orderedMasters

    def addOrderedMaster(self, value: Optional[OrderedMaster]) -> TimeSyncClientConfiguration:
        """
        Defines a list of ordered NetworkEndpoints. Tags: xml.namePlural=ORDERED-MASTER-LIST
        A None value is a no-op and does not extend the orderedMaster list.
        """
        if value is not None:
            self.orderedMasters.append(value)
        return self

    def getTimeSyncTechnology(self) -> Optional[TimeSyncTechnologyEnum]:
        """
        Defines the time synchronisation technology used.
        """
        return self.timeSyncTechnology

    def setTimeSyncTechnology(self, value: Optional[TimeSyncTechnologyEnum]) -> TimeSyncClientConfiguration:
        """
        Defines the time synchronisation technology used.
        A None value is a no-op and does not overwrite an existing timeSyncTechnology.
        """
        if value is not None:
            self.timeSyncTechnology = value
        return self


class TimeSyncServerConfiguration(Referrable):
    """
    Defines the configuration of the time synchronisation server.
    """

    # TimeSyncServerConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.147, p.470
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPriority                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPriority                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSyncInterval                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSyncInterval                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeSyncServerIdentifier    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeSyncServerIdentifier    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeSyncTechnology          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeSyncTechnology          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Server Priority.
        self.priority: Optional[PositiveInteger] = None

        # Synchronisation interval used by the time synchronisation server (in seconds).
        self.syncInterval: Optional[TimeValue] = None

        # Identifier of the TimeSyncServer.
        self.timeSyncServerIdentifier: Optional[String] = None

        # Defines the time synchronisation technology used. Possible values are: NTP_RFC958, PTP_ IEEE1588_2002, PTP_IEEE1588_2008, AVB_ IEEE802_1AS and others.
        self.timeSyncTechnology: Optional[TimeSyncTechnologyEnum] = None

    def getPriority(self) -> Optional[PositiveInteger]:
        """
        Server Priority.
        """
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> TimeSyncServerConfiguration:
        """
        Server Priority.
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def getSyncInterval(self) -> Optional[TimeValue]:
        """
        Synchronisation interval used by the time synchronisation server (in seconds).
        """
        return self.syncInterval

    def setSyncInterval(self, value: Optional[TimeValue]) -> TimeSyncServerConfiguration:
        """
        Synchronisation interval used by the time synchronisation server (in seconds).
        A None value is a no-op and does not overwrite an existing syncInterval.
        """
        if value is not None:
            self.syncInterval = value
        return self

    def getTimeSyncServerIdentifier(self) -> Optional[String]:
        """
        Identifier of the TimeSyncServer.
        """
        return self.timeSyncServerIdentifier

    def setTimeSyncServerIdentifier(self, value: Optional[String]) -> TimeSyncServerConfiguration:
        """
        Identifier of the TimeSyncServer.
        A None value is a no-op and does not overwrite an existing timeSyncServerIdentifier.
        """
        if value is not None:
            self.timeSyncServerIdentifier = value
        return self

    def getTimeSyncTechnology(self) -> Optional[TimeSyncTechnologyEnum]:
        """
        Defines the time synchronisation technology used. Possible values are: NTP_RFC958, PTP_ IEEE1588_2002, PTP_IEEE1588_2008, AVB_ IEEE802_1AS and others.
        """
        return self.timeSyncTechnology

    def setTimeSyncTechnology(self, value: Optional[TimeSyncTechnologyEnum]) -> TimeSyncServerConfiguration:
        """
        Defines the time synchronisation technology used. Possible values are: NTP_RFC958, PTP_ IEEE1588_2002, PTP_IEEE1588_2008, AVB_ IEEE802_1AS and others.
        A None value is a no-op and does not overwrite an existing timeSyncTechnology.
        """
        if value is not None:
            self.timeSyncTechnology = value
        return self


class TimeSynchronization(ARObject):
    """
    Defines the servers / clients in a time synchronised network.
    """

    # TimeSynchronization method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.145, p.469
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTimeSyncClient         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeSyncClient         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createTimeSyncServer      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeSyncServer         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Configuration of the time synchronisation client.
        self.timeSyncClient: Optional[TimeSyncClientConfiguration] = None

        # Configuration of the time synchronisation server.
        self.timeSyncServer: Optional[TimeSyncServerConfiguration] = None

    def getTimeSyncClient(self) -> Optional[TimeSyncClientConfiguration]:
        """
        Configuration of the time synchronisation client.
        """
        return self.timeSyncClient

    def setTimeSyncClient(self, value: Optional[TimeSyncClientConfiguration]) -> TimeSynchronization:
        """
        Configuration of the time synchronisation client.
        A None value is a no-op and does not overwrite an existing timeSyncClient.
        """
        if value is not None:
            self.timeSyncClient = value
        return self

    def createTimeSyncServer(self, short_name: str) -> TimeSyncServerConfiguration:
        """
        Configuration of the time synchronisation server.
        """
        if self.timeSyncServer is not None and self.timeSyncServer.getShortName() == short_name:
            return self.timeSyncServer
        server = TimeSyncServerConfiguration(self, short_name)
        self.timeSyncServer = server
        return server

    def getTimeSyncServer(self) -> Optional[TimeSyncServerConfiguration]:
        """
        Configuration of the time synchronisation server.
        """
        return self.timeSyncServer


class InfrastructureServices(ARObject):
    """
    Defines the network infrastructure services provided or consumed.
    """

    # InfrastructureServices method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.144, p.469
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDoIpEntity                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDoIpEntity                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeSynchronization       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeSynchronization       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Defines whether a infrastructure service that runs on the network endpoint is a DoIP-Entity.
        self.doIpEntity: Optional[DoIpEntity] = None

        # Defines the servers / clients in a time synchronised network.
        self.timeSynchronization: Optional[TimeSynchronization] = None

    def getDoIpEntity(self) -> Optional[DoIpEntity]:
        """Defines whether a infrastructure service that runs on the network endpoint is a DoIP-Entity."""
        return self.doIpEntity

    def setDoIpEntity(self, value: Optional[DoIpEntity]) -> InfrastructureServices:
        """
        Defines whether a infrastructure service that runs on the network endpoint is a DoIP-Entity.
        A None value is a no-op and does not overwrite an existing doIpEntity.
        """
        if value is not None:
            self.doIpEntity = value
        return self

    def getTimeSynchronization(self) -> Optional[TimeSynchronization]:
        """Defines the servers / clients in a time synchronised network."""
        return self.timeSynchronization

    def setTimeSynchronization(self, value: Optional[TimeSynchronization]) -> InfrastructureServices:
        """
        Defines the servers / clients in a time synchronised network.
        A None value is a no-op and does not overwrite an existing timeSynchronization.
        """
        if value is not None:
            self.timeSynchronization = value
        return self


class NetworkEndpoint(Identifiable):
    """
    The network endpoint defines the network addressing (e.g. IP-Address or MAC multicast address).
    """

    # NetworkEndpoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.134, p.463
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFullyQualifiedDomainName [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFullyQualifiedDomainName [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInfrastructureServices   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInfrastructureServices   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpSecConfig              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpSecConfig              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addNetworkEndpointAddress   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNetworkEndpointAddresses [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPriority                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPriority                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the fully qualified domain name (FQDN) e.g. some.example.host.
        self.fullyQualifiedDomainName: Optional[String] = None

        # Defines the network infrastructure services provided or consumed.
        self.infrastructureServices: Optional[InfrastructureServices] = None

        # Optional IPSec configuration that provides security services for IP packets.
        self.ipSecConfig: Optional[IPSecConfig] = None

        # Definition of a Network Address.
        self.networkEndpointAddresses: List[NetworkEndpointAddress] = []

        # Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        self.priority: Optional[PositiveInteger] = None

    def getFullyQualifiedDomainName(self) -> Optional[String]:
        """
        Defines the fully qualified domain name (FQDN) e.g. some.example.host.
        """
        return self.fullyQualifiedDomainName

    def setFullyQualifiedDomainName(self, value: Optional[String]) -> NetworkEndpoint:
        """
        Defines the fully qualified domain name (FQDN) e.g. some.example.host.
        A None value is a no-op and does not overwrite an existing fullyQualifiedDomainName.
        """
        if value is not None:
            self.fullyQualifiedDomainName = value
        return self

    def getInfrastructureServices(self) -> Optional[InfrastructureServices]:
        """
        Defines the network infrastructure services provided or consumed.
        """
        return self.infrastructureServices

    def setInfrastructureServices(self, value: Optional[InfrastructureServices]) -> NetworkEndpoint:
        """
        Defines the network infrastructure services provided or consumed.
        A None value is a no-op and does not overwrite an existing infrastructureServices.
        """
        if value is not None:
            self.infrastructureServices = value
        return self

    def getIpSecConfig(self) -> Optional[IPSecConfig]:
        """
        Optional IPSec configuration that provides security services for IP packets.
        """
        return self.ipSecConfig

    def setIpSecConfig(self, value: Optional[IPSecConfig]) -> NetworkEndpoint:
        """
        Optional IPSec configuration that provides security services for IP packets.
        A None value is a no-op and does not overwrite an existing ipSecConfig.
        """
        if value is not None:
            self.ipSecConfig = value
        return self

    def addNetworkEndpointAddress(self, value: Optional[NetworkEndpointAddress]) -> NetworkEndpoint:
        """
        Definition of a Network Address.
        A None value is a no-op and is not appended to networkEndpointAddresses.
        """
        if value is not None:
            self.networkEndpointAddresses.append(value)
        return self

    def getNetworkEndpointAddresses(self) -> List[NetworkEndpointAddress]:
        """
        Definition of a Network Address.
        """
        return self.networkEndpointAddresses

    def getPriority(self) -> Optional[PositiveInteger]:
        """
        Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        """
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> NetworkEndpoint:
        """
        Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self


class EthernetPhysicalLayerTypeEnum(AREnum):
    """
    Specifies physical layer types of Ethernet transceiver links.
    """

    # EthernetPhysicalLayerTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.57, p.111
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPort.physicalLayerType
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Ethernet Standard (IEEE 802.3ab) to support 1Gbit/s over 4 twisted pairs. Tags: atp.EnumerationLiteralIndex=6 xml.name=1000BASE-T
    _1000BASE_T = "1000BASE-T"

    # Ethernet Standard (IEEE 802.3bp) to support 1Gbit/s over a single twisted pair cable. Tags: atp.EnumerationLiteralIndex=8 xml.name=1000BASE-T1
    _1000BASE_T1 = "1000BASE-T1"

    # Ethernet Standard (IEEE 802.3bw) to support 100Mbit/s over a single twisted pair cable. 100BASE-T1 is the IEEE Standardized version of BroadRReach. Tags: atp.EnumerationLiteralIndex=7 xml.name=100BASE-T1
    _100BASE_T1 = "100BASE-T1"

    # Ethernet Standard (IEEE 802.3u) to support 100Mbit/s over two twisted pairs. Tags: atp.EnumerationLiteralIndex=5 xml.name=100BASE-TX
    _100BASE_TX = "100BASE-TX"

    # Physical layer interface 10BASE-T1S (10Mbit/s, 2 pairs). Used for automotive. Tags: atp.EnumerationLiteralIndex=10 atp.Status=draft xml.name=10BASE-T1S
    _10BASE_T1S = "10BASE-T1S"

    # Ethernet Standard (IEEE 802.11p) to support wireless communication in vehicular environments. Tags: atp.EnumerationLiteralIndex=9 xml.name=IEEE802-11P
    IEEE802_11P = "IEEE802-11P"

    def __init__(self):
        super().__init__(
            [
                EthernetPhysicalLayerTypeEnum._1000BASE_T,
                EthernetPhysicalLayerTypeEnum._1000BASE_T1,
                EthernetPhysicalLayerTypeEnum._100BASE_T1,
                EthernetPhysicalLayerTypeEnum._100BASE_TX,
                EthernetPhysicalLayerTypeEnum._10BASE_T1S,
                EthernetPhysicalLayerTypeEnum.IEEE802_11P,
            ]
        )


class EthernetSwitchVlanIngressTagEnum(AREnum):
    """
    Defines the possible tagging behavior at an ingress port.
    """

    # EthernetSwitchVlanIngressTagEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.58, p.111
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPort.receiveActivity
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Drop if untagged. Tags: atp.EnumerationLiteralIndex=1
    DROP_UNTAGGED = "DROP-UNTAGGED"

    # Forward with the same VLAN as received. Also untagged frames will be forwarded as untagged. Tags: atp.EnumerationLiteralIndex=0
    FORWARD_AS_IS = "FORWARD-AS-IS"

    def __init__(self):
        super().__init__(
            [
                EthernetSwitchVlanIngressTagEnum.DROP_UNTAGGED,
                EthernetSwitchVlanIngressTagEnum.FORWARD_AS_IS,
            ]
        )


class TimeSyncTechnologyEnum(AREnum):
    """
    Timesynchronization. Server/Client configuration.
    """

    # TimeSyncTechnologyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.149, p.471
    # Spec verified: R23-11
    # (no methods) — enum value form serialized on consuming attribute

    # Ethernet AVB compliant IEEE802.1AS Precision Time Protocol Tags: atp.EnumerationLiteralIndex=0
    AVB_IEEE802_1AS = "AVB--IEEE-802--1-AS"

    # Network Time Protocol (NTP) Tags: atp.EnumerationLiteralIndex=1
    NTP_RFC958 = "NTP--RFC-958"

    # Precision Time Protocol (PTP) IEEE 1588-2002 Tags: atp.EnumerationLiteralIndex=2
    PTP_IEEE1588_2002 = "PTP--IEEE-1588--2002"

    # Precision Time Protocol (PTP) IEEE 1588-2008 Tags: atp.EnumerationLiteralIndex=3
    PTP_IEEE1588_2008 = "PTP--IEEE-1588--2008"

    def __init__(self):
        super().__init__(
            [
                TimeSyncTechnologyEnum.AVB_IEEE802_1AS,
                TimeSyncTechnologyEnum.NTP_RFC958,
                TimeSyncTechnologyEnum.PTP_IEEE1588_2002,
                TimeSyncTechnologyEnum.PTP_IEEE1588_2008,
            ]
        )


class DoIpEntityRoleEnum(AREnum):
    """
    DoIP role a network-node has.
    """

    # DoIpEntityRoleEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.151, p.471
    # Spec verified: R23-11
    # (no methods) — enum value form serialized on DoIpEntity.doIpEntityRole

    # Network node is a DoIP gateway that accepts external connections. Tags: atp.EnumerationLiteralIndex=0
    EDGE_NODE = "EDGE-NODE"

    # Network node is a Gateway between the DoIP network and other networks. Tags: atp.EnumerationLiteralIndex=1
    GATEWAY = "GATEWAY"

    # Network node is a DoIp node. Tags: atp.EnumerationLiteralIndex=2
    NODE = "NODE"

    def __init__(self):
        super().__init__(
            [
                DoIpEntityRoleEnum.EDGE_NODE,
                DoIpEntityRoleEnum.GATEWAY,
                DoIpEntityRoleEnum.NODE,
            ]
        )


class EthernetWakeupSleepOnDatalineConfig(Identifiable):
    """
    EthernetWakeupSleepOnDatalineConfigSet is the main element that aggregates different config set regarding the wakeup and sleep on data line. An EthernetWakeupSleepOnDatalineConfigSet could aggregate multiple different configurations regarding the wakeup and sleep on dataline (EthernetWakeupSleepOnDatalineConfig).

    [constr_3601] Mandatory attributes of EthernetWakeupSleepOnDatalineConfig: The following attributes of EthernetWakeupSleepOnDatalineConfig shall be defined at the time when the Ecu Extract is complete:
    - wakeupLocalEnabled
    - wakeupRemoteEnabled
    """

    # EthernetWakeupSleepOnDatalineConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.115, p.159
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSleepModeExecutionDelay                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSleepModeExecutionDelay                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSleepRepetitionDelayOfSleepRequest      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSleepRepetitionDelayOfSleepRequest      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSleepRepetitionsOfSleepRequest          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSleepRepetitionsOfSleepRequest          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeupForwardLocalEnabled               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWakeupForwardLocalEnabled               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeupForwardRemoteEnabled              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWakeupForwardRemoteEnabled              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeupLocalDetectionTime                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWakeupLocalDetectionTime                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeupLocalDurationTime                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWakeupLocalDurationTime                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeupLocalEnabled                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWakeupLocalEnabled                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeupRemoteEnabled                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWakeupRemoteEnabled                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeupRepetitionDelayOfWakeupRequest    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWakeupRepetitionDelayOfWakeupRequest    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWakeupRepetitionsOfWakeupRequest        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWakeupRepetitionsOfWakeupRequest        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Delay in seconds to perform a sleep request if the Ethernet hardware (PHY) detect a pending wake-up. This is used to avoid the race condition, if a sleep was requested while a wake-up of a neighboring PHY was received via a local wake-up connection (e.g. I/O pin).
        self.sleepModeExecutionDelay: Optional[TimeValue] = None

        # Delay in seconds for a repetition of a sleep request. This is used to retry a synchronized shutdown of the connected Ethernet hardware (PHY) of the link partner. (see constr_3607).
        self.sleepRepetitionDelayOfSleepRequest: Optional[TimeValue] = None

        # Count of repetitions for a sleep on dataline. If a sleep is rejected by the linked communication partner, the sleep is repeated until the count of repetitions exceed. If count of repetitions exceed, the Ethernet hardware (PHY) transit to sleep without acknowledgement of the connected link partner.
        self.sleepRepetitionsOfSleepRequest: Optional[PositiveInteger] = None

        # If enabled, then a remote wake-up received on the physical dataline (e.g. 100BASE-T1) is forwarded as local wake-up (e.g. via an I/O pin). If disabled, then a remote wake-up is not forwarded as local wake-up. (see constr_3602).
        self.wakeupForwardLocalEnabled: Optional[Boolean] = None

        # If enabled, then a local wake-up is forwarded to the physical dataline (e.g. 100BASE-T1). If disabled, then a local wake-up is not forwarded to the physical dataline. (see constr_3604).
        self.wakeupForwardRemoteEnabled: Optional[Boolean] = None

        # Specify the detection time if a local wake-up in seconds is present on the local wake-up connection (e.g. I/O pin). A local wake-up has to be present at least for wakeupLocalDetectionTime to be detected a valid local wake-up. (see constr_3605, constr_3606, constr_3610).
        self.wakeupLocalDetectionTime: Optional[TimeValue] = None

        # Specify the duration of a local wake-up in seconds to be present on the local wake-up connection (e.g. I/O pin). (see constr_3603, constr_3606, constr_3609).
        self.wakeupLocalDurationTime: Optional[TimeValue] = None

        # If enabled, then a local wake-up received via a local connection (e.g. I/O pin) shall be detected by the Ethernet hardware (PHY). If disabled, Ethernet hardware is not reacting on a local wake-up.
        self.wakeupLocalEnabled: Optional[Boolean] = None

        # If enabled, then a remote wake-up received via the physical dataline (e.g. 100BASE-T1) shall be detected by the Ethernet hardware (PHY). If disabled, Ethernet hardware is not reaction on a remote wake-up.
        self.wakeupRemoteEnabled: Optional[Boolean] = None

        # Delay in seconds for a repetition of a wake-up. This is used to increase the reliability in the network, such that an ECU which initiates the wake-up does repeat the wake-up and increase the probability that affected ECUs receive the wake-up. (see constr_3608).
        self.wakeupRepetitionDelayOfWakeupRequest: Optional[TimeValue] = None

        # Count of repetitions for a wake-up. This is used to increase the reliability in the network, such that an ECU which initiates the wake-up does repeat the wake-up and increase the probability that affected ECUs receive the wake-up.
        self.wakeupRepetitionsOfWakeupRequest: Optional[PositiveInteger] = None

    def getSleepModeExecutionDelay(self) -> Optional[TimeValue]:
        """
        Delay in seconds to perform a sleep request if the Ethernet hardware (PHY) detect a pending wake-up. This is used to avoid the race condition, if a sleep was requested while a wake-up of a neighboring PHY was received via a local wake-up connection (e.g. I/O pin).
        """
        return self.sleepModeExecutionDelay

    def setSleepModeExecutionDelay(self, value: Optional[TimeValue]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Delay in seconds to perform a sleep request if the Ethernet hardware (PHY) detect a pending wake-up. This is used to avoid the race condition, if a sleep was requested while a wake-up of a neighboring PHY was received via a local wake-up connection (e.g. I/O pin).

        A None value is a no-op and does not overwrite an existing sleepModeExecutionDelay.
        """
        if value is not None:
            self.sleepModeExecutionDelay = value
        return self

    def getSleepRepetitionDelayOfSleepRequest(self) -> Optional[TimeValue]:
        """
        Delay in seconds for a repetition of a sleep request. This is used to retry a synchronized shutdown of the connected Ethernet hardware (PHY) of the link partner. (see constr_3607).
        """
        return self.sleepRepetitionDelayOfSleepRequest

    def setSleepRepetitionDelayOfSleepRequest(self, value: Optional[TimeValue]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Delay in seconds for a repetition of a sleep request. This is used to retry a synchronized shutdown of the connected Ethernet hardware (PHY) of the link partner. (see constr_3607).

        A None value is a no-op and does not overwrite an existing sleepRepetitionDelayOfSleepRequest.
        """
        if value is not None:
            self.sleepRepetitionDelayOfSleepRequest = value
        return self

    def getSleepRepetitionsOfSleepRequest(self) -> Optional[PositiveInteger]:
        """
        Count of repetitions for a sleep on dataline. If a sleep is rejected by the linked communication partner, the sleep is repeated until the count of repetitions exceed. If count of repetitions exceed, the Ethernet hardware (PHY) transit to sleep without acknowledgement of the connected link partner.
        """
        return self.sleepRepetitionsOfSleepRequest

    def setSleepRepetitionsOfSleepRequest(self, value: Optional[PositiveInteger]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Count of repetitions for a sleep on dataline. If a sleep is rejected by the linked communication partner, the sleep is repeated until the count of repetitions exceed. If count of repetitions exceed, the Ethernet hardware (PHY) transit to sleep without acknowledgement of the connected link partner.

        A None value is a no-op and does not overwrite an existing sleepRepetitionsOfSleepRequest.
        """
        if value is not None:
            self.sleepRepetitionsOfSleepRequest = value
        return self

    def getWakeupForwardLocalEnabled(self) -> Optional[Boolean]:
        """
        If enabled, then a remote wake-up received on the physical dataline (e.g. 100BASE-T1) is forwarded as local wake-up (e.g. via an I/O pin). If disabled, then a remote wake-up is not forwarded as local wake-up. (see constr_3602).
        """
        return self.wakeupForwardLocalEnabled

    def setWakeupForwardLocalEnabled(self, value: Optional[Boolean]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        If enabled, then a remote wake-up received on the physical dataline (e.g. 100BASE-T1) is forwarded as local wake-up (e.g. via an I/O pin). If disabled, then a remote wake-up is not forwarded as local wake-up. (see constr_3602).

        A None value is a no-op and does not overwrite an existing wakeupForwardLocalEnabled.
        """
        if value is not None:
            self.wakeupForwardLocalEnabled = value
        return self

    def getWakeupForwardRemoteEnabled(self) -> Optional[Boolean]:
        """
        If enabled, then a local wake-up is forwarded to the physical dataline (e.g. 100BASE-T1). If disabled, then a local wake-up is not forwarded to the physical dataline. (see constr_3604).
        """
        return self.wakeupForwardRemoteEnabled

    def setWakeupForwardRemoteEnabled(self, value: Optional[Boolean]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        If enabled, then a local wake-up is forwarded to the physical dataline (e.g. 100BASE-T1). If disabled, then a local wake-up is not forwarded to the physical dataline. (see constr_3604).

        A None value is a no-op and does not overwrite an existing wakeupForwardRemoteEnabled.
        """
        if value is not None:
            self.wakeupForwardRemoteEnabled = value
        return self

    def getWakeupLocalDetectionTime(self) -> Optional[TimeValue]:
        """
        Specify the detection time if a local wake-up in seconds is present on the local wake-up connection (e.g. I/O pin). A local wake-up has to be present at least for wakeupLocalDetectionTime to be detected a valid local wake-up. (see constr_3605, constr_3606, constr_3610).
        """
        return self.wakeupLocalDetectionTime

    def setWakeupLocalDetectionTime(self, value: Optional[TimeValue]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Specify the detection time if a local wake-up in seconds is present on the local wake-up connection (e.g. I/O pin). A local wake-up has to be present at least for wakeupLocalDetectionTime to be detected a valid local wake-up. (see constr_3605, constr_3606, constr_3610).

        A None value is a no-op and does not overwrite an existing wakeupLocalDetectionTime.
        """
        if value is not None:
            self.wakeupLocalDetectionTime = value
        return self

    def getWakeupLocalDurationTime(self) -> Optional[TimeValue]:
        """
        Specify the duration of a local wake-up in seconds to be present on the local wake-up connection (e.g. I/O pin). (see constr_3603, constr_3606, constr_3609).
        """
        return self.wakeupLocalDurationTime

    def setWakeupLocalDurationTime(self, value: Optional[TimeValue]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Specify the duration of a local wake-up in seconds to be present on the local wake-up connection (e.g. I/O pin). (see constr_3603, constr_3606, constr_3609).

        A None value is a no-op and does not overwrite an existing wakeupLocalDurationTime.
        """
        if value is not None:
            self.wakeupLocalDurationTime = value
        return self

    def getWakeupLocalEnabled(self) -> Optional[Boolean]:
        """
        If enabled, then a local wake-up received via a local connection (e.g. I/O pin) shall be detected by the Ethernet hardware (PHY). If disabled, Ethernet hardware is not reacting on a local wake-up.
        """
        return self.wakeupLocalEnabled

    def setWakeupLocalEnabled(self, value: Optional[Boolean]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        If enabled, then a local wake-up received via a local connection (e.g. I/O pin) shall be detected by the Ethernet hardware (PHY). If disabled, Ethernet hardware is not reacting on a local wake-up.

        A None value is a no-op and does not overwrite an existing wakeupLocalEnabled.
        """
        if value is not None:
            self.wakeupLocalEnabled = value
        return self

    def getWakeupRemoteEnabled(self) -> Optional[Boolean]:
        """
        If enabled, then a remote wake-up received via the physical dataline (e.g. 100BASE-T1) shall be detected by the Ethernet hardware (PHY). If disabled, Ethernet hardware is not reaction on a remote wake-up.
        """
        return self.wakeupRemoteEnabled

    def setWakeupRemoteEnabled(self, value: Optional[Boolean]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        If enabled, then a remote wake-up received via the physical dataline (e.g. 100BASE-T1) shall be detected by the Ethernet hardware (PHY). If disabled, Ethernet hardware is not reaction on a remote wake-up.

        A None value is a no-op and does not overwrite an existing wakeupRemoteEnabled.
        """
        if value is not None:
            self.wakeupRemoteEnabled = value
        return self

    def getWakeupRepetitionDelayOfWakeupRequest(self) -> Optional[TimeValue]:
        """
        Delay in seconds for a repetition of a wake-up. This is used to increase the reliability in the network, such that an ECU which initiates the wake-up does repeat the wake-up and increase the probability that affected ECUs receive the wake-up. (see constr_3608).
        """
        return self.wakeupRepetitionDelayOfWakeupRequest

    def setWakeupRepetitionDelayOfWakeupRequest(self, value: Optional[TimeValue]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Delay in seconds for a repetition of a wake-up. This is used to increase the reliability in the network, such that an ECU which initiates the wake-up does repeat the wake-up and increase the probability that affected ECUs receive the wake-up. (see constr_3608).

        A None value is a no-op and does not overwrite an existing wakeupRepetitionDelayOfWakeupRequest.
        """
        if value is not None:
            self.wakeupRepetitionDelayOfWakeupRequest = value
        return self

    def getWakeupRepetitionsOfWakeupRequest(self) -> Optional[PositiveInteger]:
        """
        Count of repetitions for a wake-up. This is used to increase the reliability in the network, such that an ECU which initiates the wake-up does repeat the wake-up and increase the probability that affected ECUs receive the wake-up.
        """
        return self.wakeupRepetitionsOfWakeupRequest

    def setWakeupRepetitionsOfWakeupRequest(self, value: Optional[PositiveInteger]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Count of repetitions for a wake-up. This is used to increase the reliability in the network, such that an ECU which initiates the wake-up does repeat the wake-up and increase the probability that affected ECUs receive the wake-up.

        A None value is a no-op and does not overwrite an existing wakeupRepetitionsOfWakeupRequest.
        """
        if value is not None:
            self.wakeupRepetitionsOfWakeupRequest = value
        return self


class PlcaProps(ARObject):
    """
    This meta-class allows to configure the PLCA (Physical Layer Collision Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the CouplingPort (PHY).
    """

    # PlcaProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.117, p.169
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPlcaLocalNodeId             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPlcaLocalNodeId             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPlcaMaxBurstCount           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPlcaMaxBurstCount           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPlcaMaxBurstTimer           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPlcaMaxBurstTimer           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute defines the node ID when the PLCA mode for 10BASE-T1S is used.
        self.plcaLocalNodeId: Optional[PositiveInteger] = None

        # Defines maximum packets allowed to be transmitted within a TO. This configuration can be different from one ECU to another within the PLCA mixed segment.
        self.plcaMaxBurstCount: Optional[PositiveInteger] = None

        # Limits the burst frames in bit time. This configuration can be different from one ECU to another within the PLCA mixed segment. For PLCA burst mode to work properly this timer should be set greater than one IPG.
        self.plcaMaxBurstTimer: Optional[PositiveInteger] = None

    def getPlcaLocalNodeId(self) -> Optional[PositiveInteger]:
        """This attribute defines the node ID when the PLCA mode for 10BASE-T1S is used."""
        return self.plcaLocalNodeId

    def setPlcaLocalNodeId(self, value: Optional[PositiveInteger]) -> PlcaProps:
        """
        This attribute defines the node ID when the PLCA mode for 10BASE-T1S is used.
        A None value is a no-op and does not overwrite an existing plcaLocalNodeId.
        """
        if value is not None:
            self.plcaLocalNodeId = value
        return self

    def getPlcaMaxBurstCount(self) -> Optional[PositiveInteger]:
        """Defines maximum packets allowed to be transmitted within a TO. This configuration can be different from one ECU to another within the PLCA mixed segment."""
        return self.plcaMaxBurstCount

    def setPlcaMaxBurstCount(self, value: Optional[PositiveInteger]) -> PlcaProps:
        """
        Defines maximum packets allowed to be transmitted within a TO. This configuration can be different from one ECU to another within the PLCA mixed segment.
        A None value is a no-op and does not overwrite an existing plcaMaxBurstCount.
        """
        if value is not None:
            self.plcaMaxBurstCount = value
        return self

    def getPlcaMaxBurstTimer(self) -> Optional[PositiveInteger]:
        """Limits the burst frames in bit time. This configuration can be different from one ECU to another within the PLCA mixed segment. For PLCA burst mode to work properly this timer should be set greater than one IPG."""
        return self.plcaMaxBurstTimer

    def setPlcaMaxBurstTimer(self, value: Optional[PositiveInteger]) -> PlcaProps:
        """
        Limits the burst frames in bit time. This configuration can be different from one ECU to another within the PLCA mixed segment. For PLCA burst mode to work properly this timer should be set greater than one IPG.
        A None value is a no-op and does not overwrite an existing plcaMaxBurstTimer.
        """
        if value is not None:
            self.plcaMaxBurstTimer = value
        return self


class CouplingPortConnection(ARObject, VariationPointCapable):
    """
    Connection between two CouplingPorts (firstPort and secondPort) or between a collection of Ports that are all referenced by the portCollection reference.
    """

    # CouplingPortConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.60, p.113
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFirstPortRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstPortRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addNodePortRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNodePortRefs                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPlcaLocalNodeCount             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPlcaLocalNodeCount             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPlcaTransmitOpportunityTimer   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPlcaTransmitOpportunityTimer   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondPortRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecondPortRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to the first CouplingPort that is connected via the CouplingPortConnection.
        self.firstPortRef: Optional[RefType] = None

        # Reference to a number of CouplingPorts that are connected via the CouplingPortConnection. This reference shall be used to describe a 10BASE-T1S topology architecture where several CouplingPorts of EthernetCommunicationControllers are connected via one CouplingPortConnection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nodePort.couplingPort, nodePort.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.nodePortRefs: List[RefType] = []

        # Defines the number of communication participants in case 10BASE-T1S and the nodePort reference is used.
        self.plcaLocalNodeCount: Optional[PositiveInteger] = None

        # Timer for the transmission in bit time to evaluate if a Transmission Opportunity is yield or not.
        self.plcaTransmitOpportunityTimer: Optional[PositiveInteger] = None

        # Reference to the second CouplingPort that is connected via the CouplingPortConnection.
        self.secondPortRef: Optional[RefType] = None

    def getFirstPortRef(self) -> Optional[RefType]:
        """Reference to the first CouplingPort that is connected via the CouplingPortConnection."""
        return self.firstPortRef

    def setFirstPortRef(self, value: Optional[RefType]) -> CouplingPortConnection:
        """
        Reference to the first CouplingPort that is connected via the CouplingPortConnection.
        A None value is a no-op and does not overwrite an existing firstPortRef.
        """
        if value is not None:
            self.firstPortRef = value
        return self

    def addNodePortRef(self, value: Optional[RefType]) -> CouplingPortConnection:
        """
        Reference to a number of CouplingPorts that are connected via the CouplingPortConnection. This reference shall be used to describe a 10BASE-T1S topology architecture where several CouplingPorts of EthernetCommunicationControllers are connected via one CouplingPortConnection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nodePort.couplingPort, nodePort.variation Point.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and does not append to nodePortRefs.
        """
        if value is not None:
            self.nodePortRefs.append(value)
        return self

    def getNodePortRefs(self) -> List[RefType]:
        """Reference to a number of CouplingPorts that are connected via the CouplingPortConnection. This reference shall be used to describe a 10BASE-T1S topology architecture where several CouplingPorts of EthernetCommunicationControllers are connected via one CouplingPortConnection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nodePort.couplingPort, nodePort.variation Point.shortLabel vh.latestBindingTime=postBuild"""
        return self.nodePortRefs

    def getPlcaLocalNodeCount(self) -> Optional[PositiveInteger]:
        """Defines the number of communication participants in case 10BASE-T1S and the nodePort reference is used."""
        return self.plcaLocalNodeCount

    def setPlcaLocalNodeCount(self, value: Optional[PositiveInteger]) -> CouplingPortConnection:
        """
        Defines the number of communication participants in case 10BASE-T1S and the nodePort reference is used.
        A None value is a no-op and does not overwrite an existing plcaLocalNodeCount.
        """
        if value is not None:
            self.plcaLocalNodeCount = value
        return self

    def getPlcaTransmitOpportunityTimer(self) -> Optional[PositiveInteger]:
        """Timer for the transmission in bit time to evaluate if a Transmission Opportunity is yield or not."""
        return self.plcaTransmitOpportunityTimer

    def setPlcaTransmitOpportunityTimer(self, value: Optional[PositiveInteger]) -> CouplingPortConnection:
        """
        Timer for the transmission in bit time to evaluate if a Transmission Opportunity is yield or not.
        A None value is a no-op and does not overwrite an existing plcaTransmitOpportunityTimer.
        """
        if value is not None:
            self.plcaTransmitOpportunityTimer = value
        return self

    def getSecondPortRef(self) -> Optional[RefType]:
        """Reference to the second CouplingPort that is connected via the CouplingPortConnection."""
        return self.secondPortRef

    def setSecondPortRef(self, value: Optional[RefType]) -> CouplingPortConnection:
        """
        Reference to the second CouplingPort that is connected via the CouplingPortConnection.
        A None value is a no-op and does not overwrite an existing secondPortRef.
        """
        if value is not None:
            self.secondPortRef = value
        return self


class GlobalTimeCouplingPortProps(ARObject):
    """
    Defines properties for the usage of the CouplingPort in the scope of Global Time Sync.
    """

    # GlobalTimeCouplingPortProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.18, p.875
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPropagationDelay            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPropagationDelay            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # If cyclic propagation delay measurement is enabled, this parameter represents the default value of the propagation delay until the first actually measured propagation delay is available. If cyclic propagation delay measurement is disabled, this parameter defines a fixed value for the propagation delay.
        self.propagationDelay: Optional[TimeValue] = None

    def getPropagationDelay(self) -> Optional[TimeValue]:
        """If cyclic propagation delay measurement is enabled, this parameter represents the default value of the propagation delay until the first actually measured propagation delay is available. If cyclic propagation delay measurement is disabled, this parameter defines a fixed value for the propagation delay."""
        return self.propagationDelay

    def setPropagationDelay(self, value: Optional[TimeValue]) -> GlobalTimeCouplingPortProps:
        """
        If cyclic propagation delay measurement is enabled, this parameter represents the default value of the propagation delay until the first actually measured propagation delay is available. If cyclic propagation delay measurement is disabled, this parameter defines a fixed value for the propagation delay.
        A None value is a no-op and does not overwrite an existing propagationDelay.
        """
        if value is not None:
            self.propagationDelay = value
        return self


class CouplingPortRatePolicyActionEnum(AREnum):
    """
    Defines the action to be performed when a rate policy is violated.
    """

    # CouplingPortRatePolicyActionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.70, p.125
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPortRatePolicy.policyAction
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # If the rate policy is violated the frame shall be dropped. Tags: atp.EnumerationLiteralIndex=0
    DROP_FRAME = "DROP-FRAME"

    # If the rate policy is violated the CouplingPort this CouplingPortRatePolicy is defined on shall block all frames from the MAC-Address the violation was caused by. Tags: atp.EnumerationLiteralIndex=1
    BLOCK_SOURCE = "BLOCK-SOURCE"

    def __init__(self):
        super().__init__(
            [
                CouplingPortRatePolicyActionEnum.DROP_FRAME,
                CouplingPortRatePolicyActionEnum.BLOCK_SOURCE,
            ]
        )


class CouplingPortRatePolicy(ARObject):
    """
    Defines a rate policy on a CouplingPort.
    """

    # CouplingPortRatePolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.69, p.124
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataLength       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataLength       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPolicyAction     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPolicyAction     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPriority         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPriority         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeInterval     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeInterval     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addVlanRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlanRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Amount of data in bytes (excluding header information) that can be received to define the rate policy.
        self.dataLength: Optional[PositiveInteger] = None

        # Defines the action to be performed when this rate policy is violated.
        self.policyAction: Optional[CouplingPortRatePolicyActionEnum] = None

        # Defines the priority which this rate policy shall be limited on. If no priority is given this rate policy is not considering priority.
        self.priority: Optional[PositiveInteger] = None

        # Time interval used to define the base of the rate policy.
        self.timeInterval: Optional[TimeValue] = None

        # Defines the VLANs this rate policy shall be limited on. If no VLAN is given this rate policy is not considering VLAN tags.
        self.vLanRefs: List[RefType] = []

    def getDataLength(self) -> Optional[PositiveInteger]:
        """Amount of data in bytes (excluding header information) that can be received to define the rate policy."""
        return self.dataLength

    def setDataLength(self, value: Optional[PositiveInteger]) -> CouplingPortRatePolicy:
        """
        Amount of data in bytes (excluding header information) that can be received to define the rate policy.
        A None value is a no-op and does not overwrite an existing dataLength.
        """
        if value is not None:
            self.dataLength = value
        return self

    def getPolicyAction(self) -> Optional[CouplingPortRatePolicyActionEnum]:
        """Defines the action to be performed when this rate policy is violated."""
        return self.policyAction

    def setPolicyAction(self, value: Optional[CouplingPortRatePolicyActionEnum]) -> CouplingPortRatePolicy:
        """
        Defines the action to be performed when this rate policy is violated.
        A None value is a no-op and does not overwrite an existing policyAction.
        """
        if value is not None:
            self.policyAction = value
        return self

    def getPriority(self) -> Optional[PositiveInteger]:
        """Defines the priority which this rate policy shall be limited on. If no priority is given this rate policy is not considering priority."""
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> CouplingPortRatePolicy:
        """
        Defines the priority which this rate policy shall be limited on. If no priority is given this rate policy is not considering priority.
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def getTimeInterval(self) -> Optional[TimeValue]:
        """Time interval used to define the base of the rate policy."""
        return self.timeInterval

    def setTimeInterval(self, value: Optional[TimeValue]) -> CouplingPortRatePolicy:
        """
        Time interval used to define the base of the rate policy.
        A None value is a no-op and does not overwrite an existing timeInterval.
        """
        if value is not None:
            self.timeInterval = value
        return self

    def addVlanRef(self, value: Optional[RefType]) -> CouplingPortRatePolicy:
        """
        Defines the VLANs this rate policy shall be limited on. If no VLAN is given this rate policy is not considering VLAN tags.
        A None value is a no-op and does not append to vLanRefs.
        """
        if value is not None:
            self.vLanRefs.append(value)
        return self

    def getVlanRefs(self) -> List[RefType]:
        """Defines the VLANs this rate policy shall be limited on. If no VLAN is given this rate policy is not considering VLAN tags."""
        return self.vLanRefs


class TransportProtocolConfiguration(ARObject, ABC):
    """
    Transport Protocol configuration.
    """

    # TransportProtocolConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.125, p.459
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is TransportProtocolConfiguration:
            raise TypeError("TransportProtocolConfiguration is an abstract class.")

        super().__init__()


class GenericTp(TransportProtocolConfiguration):
    """
    Content Model for a generic transport protocol.
    """

    # GenericTp method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.126, p.459
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTpAddress     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTpAddress     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpTechnology  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTpTechnology  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Transport Protocol dependent Address.
        self.tpAddress: Optional[String] = None

        # Name of the used Transport Protocol.
        self.tpTechnology: Optional[String] = None

    def getTpAddress(self) -> Optional[String]:
        """
        Transport Protocol dependent Address.
        """
        return self.tpAddress

    def setTpAddress(self, value: Optional[String]) -> GenericTp:
        """
        Transport Protocol dependent Address.
        A None value is a no-op and does not overwrite an existing tpAddress.
        """
        if value is not None:
            self.tpAddress = value
        return self

    def getTpTechnology(self) -> Optional[String]:
        """
        Name of the used Transport Protocol.
        """
        return self.tpTechnology

    def setTpTechnology(self, value: Optional[String]) -> GenericTp:
        """
        Name of the used Transport Protocol.
        A None value is a no-op and does not overwrite an existing tpTechnology.
        """
        if value is not None:
            self.tpTechnology = value
        return self


class TcpUdpConfig(TransportProtocolConfiguration, ABC):
    """
    Tcp or Udp Transport Protocol Configuration.
    """

    # TcpUdpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.127, p.459
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is TcpUdpConfig:
            raise TypeError("TcpUdpConfig is an abstract class.")

        super().__init__()


class TpPort(ARObject):
    """
    Dynamic or direct assignment of a PortNumber.
    """

    # TpPort method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.133, p.461
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDynamicallyAssigned [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDynamicallyAssigned [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPortNumber          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPortNumber          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Indicates whether the source port is dynamically assigned. Tags: atp.Status=obsolete
        self.dynamicallyAssigned: Optional[Boolean] = None

        # Port Number.
        self.portNumber: Optional[PositiveInteger] = None

    def getDynamicallyAssigned(self) -> Optional[Boolean]:
        """
        Indicates whether the source port is dynamically assigned. Tags: atp.Status=obsolete
        """
        return self.dynamicallyAssigned

    def setDynamicallyAssigned(self, value: Optional[Boolean]) -> TpPort:
        """
        Indicates whether the source port is dynamically assigned. Tags: atp.Status=obsolete
        A None value is a no-op and does not overwrite an existing dynamicallyAssigned.
        """
        if value is not None:
            self.dynamicallyAssigned = value
        return self

    def getPortNumber(self) -> Optional[PositiveInteger]:
        """
        Port Number.
        """
        return self.portNumber

    def setPortNumber(self, value: Optional[PositiveInteger]) -> TpPort:
        """
        Port Number.
        A None value is a no-op and does not overwrite an existing portNumber.
        """
        if value is not None:
            self.portNumber = value
        return self


class UdpTp(TcpUdpConfig):
    """
    Content Model for UDP configuration.
    """

    # UdpTp method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.128, p.459
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getUdpTpPort     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUdpTpPort     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Udp Port configuration.
        self.udpTpPort: Optional[TpPort] = None

    def getUdpTpPort(self) -> Optional[TpPort]:
        """
        Udp Port configuration.
        """
        return self.udpTpPort

    def setUdpTpPort(self, value: Optional[TpPort]) -> UdpTp:
        """
        Udp Port configuration.
        A None value is a no-op and does not overwrite an existing udpTpPort.
        """
        if value is not None:
            self.udpTpPort = value
        return self


class TcpTp(TcpUdpConfig):
    """
    Content Model for TCP configuration.
    """

    # TcpTp method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.129, p.460
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getKeepAliveInterval         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setKeepAliveInterval         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getKeepAliveProbesMax        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setKeepAliveProbesMax        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getKeepAlives                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setKeepAlives                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getKeepAliveTime             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setKeepAliveTime             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNaglesAlgorithm           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNaglesAlgorithm           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReceiveWindowMin          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReceiveWindowMin          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpRetransmissionTimeout  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpRetransmissionTimeout  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpTpPort                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpTpPort                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Specifies the interval in seconds between subsequent keepalive probes.
        self.keepAliveInterval: Optional[TimeValue] = None

        # Maximum number of times that TCP retransmits an individual data segment before aborting the connection.
        self.keepAliveProbesMax: Optional[PositiveInteger] = None

        # Indicates if Keep-Alive messages are sent.
        self.keepAlives: Optional[Boolean] = None

        # Specifies the time in seconds between the last data packet sent and the first keepalive probe.
        self.keepAliveTime: Optional[TimeValue] = None

        # Indicates if Nagle's Algorithm is used.
        self.naglesAlgorithm: Optional[Boolean] = None

        # Minimum size of the TCP receive window in bytes.
        self.receiveWindowMin: Optional[PositiveInteger] = None

        # Defines the timeout in seconds before an unacknowledged TCP segment is sent again. If the tcp RetransmissionTimeout is not defined or set to "INF", no TCP segments shall be re-transmitted.
        self.tcpRetransmissionTimeout: Optional[TimeValue] = None

        # TCP Port configuration.
        self.tcpTpPort: Optional[TpPort] = None

    def getKeepAliveInterval(self) -> Optional[TimeValue]:
        """
        Specifies the interval in seconds between subsequent keepalive probes.
        """
        return self.keepAliveInterval

    def setKeepAliveInterval(self, value: Optional[TimeValue]) -> TcpTp:
        """
        Specifies the interval in seconds between subsequent keepalive probes.
        A None value is a no-op and does not overwrite an existing keepAliveInterval.
        """
        if value is not None:
            self.keepAliveInterval = value
        return self

    def getKeepAliveProbesMax(self) -> Optional[PositiveInteger]:
        """
        Maximum number of times that TCP retransmits an individual data segment before aborting the connection.
        """
        return self.keepAliveProbesMax

    def setKeepAliveProbesMax(self, value: Optional[PositiveInteger]) -> TcpTp:
        """
        Maximum number of times that TCP retransmits an individual data segment before aborting the connection.
        A None value is a no-op and does not overwrite an existing keepAliveProbesMax.
        """
        if value is not None:
            self.keepAliveProbesMax = value
        return self

    def getKeepAlives(self) -> Optional[Boolean]:
        """
        Indicates if Keep-Alive messages are sent.
        """
        return self.keepAlives

    def setKeepAlives(self, value: Optional[Boolean]) -> TcpTp:
        """
        Indicates if Keep-Alive messages are sent.
        A None value is a no-op and does not overwrite an existing keepAlives.
        """
        if value is not None:
            self.keepAlives = value
        return self

    def getKeepAliveTime(self) -> Optional[TimeValue]:
        """
        Specifies the time in seconds between the last data packet sent and the first keepalive probe.
        """
        return self.keepAliveTime

    def setKeepAliveTime(self, value: Optional[TimeValue]) -> TcpTp:
        """
        Specifies the time in seconds between the last data packet sent and the first keepalive probe.
        A None value is a no-op and does not overwrite an existing keepAliveTime.
        """
        if value is not None:
            self.keepAliveTime = value
        return self

    def getNaglesAlgorithm(self) -> Optional[Boolean]:
        """
        Indicates if Nagle's Algorithm is used.
        """
        return self.naglesAlgorithm

    def setNaglesAlgorithm(self, value: Optional[Boolean]) -> TcpTp:
        """
        Indicates if Nagle's Algorithm is used.
        A None value is a no-op and does not overwrite an existing naglesAlgorithm.
        """
        if value is not None:
            self.naglesAlgorithm = value
        return self

    def getReceiveWindowMin(self) -> Optional[PositiveInteger]:
        """
        Minimum size of the TCP receive window in bytes.
        """
        return self.receiveWindowMin

    def setReceiveWindowMin(self, value: Optional[PositiveInteger]) -> TcpTp:
        """
        Minimum size of the TCP receive window in bytes.
        A None value is a no-op and does not overwrite an existing receiveWindowMin.
        """
        if value is not None:
            self.receiveWindowMin = value
        return self

    def getTcpRetransmissionTimeout(self) -> Optional[TimeValue]:
        """
        Defines the timeout in seconds before an unacknowledged TCP segment is sent again. If the tcp RetransmissionTimeout is not defined or set to "INF", no TCP segments shall be re-transmitted.
        """
        return self.tcpRetransmissionTimeout

    def setTcpRetransmissionTimeout(self, value: Optional[TimeValue]) -> TcpTp:
        """
        Defines the timeout in seconds before an unacknowledged TCP segment is sent again. If the tcp RetransmissionTimeout is not defined or set to "INF", no TCP segments shall be re-transmitted.
        A None value is a no-op and does not overwrite an existing tcpRetransmissionTimeout.
        """
        if value is not None:
            self.tcpRetransmissionTimeout = value
        return self

    def getTcpTpPort(self) -> Optional[TpPort]:
        """
        TCP Port configuration.
        """
        return self.tcpTpPort

    def setTcpTpPort(self, value: Optional[TpPort]) -> TcpTp:
        """
        TCP Port configuration.
        A None value is a no-op and does not overwrite an existing tcpTpPort.
        """
        if value is not None:
            self.tcpTpPort = value
        return self


class VlanConfig(Identifiable):
    """
    VLAN Configuration attributes
    """

    # VlanConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.50, p.106
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getVlanIdentifier    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVlanIdentifier    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # A VLAN is identified by this attribute according to IEEE 802.1Q. The allowed values range is from 0..4095.
        self.vlanIdentifier: Optional[PositiveInteger] = None

    def getVlanIdentifier(self) -> Optional[PositiveInteger]:
        """
        A VLAN is identified by this attribute according to IEEE 802.1Q. The allowed values range is from 0..4095.
        """
        return self.vlanIdentifier

    def setVlanIdentifier(self, value: Optional[PositiveInteger]) -> VlanConfig:
        """
        A VLAN is identified by this attribute according to IEEE 802.1Q. The allowed values range is from 0..4095.
        A None value is a no-op and does not overwrite an existing vlanIdentifier.
        """
        if value is not None:
            self.vlanIdentifier = value
        return self


class EthernetPhysicalChannel(PhysicalChannel):
    """
    The EthernetPhysicalChannel represents a VLAN or an untagged channel. An untagged channel is modeled as an EthernetPhysicalChannel without an aggregated VLAN.

    [constr_3333] Standardized values for the attribute category of meta-class EthernetPhysicalChannel: The following values of the attribute category of metaclass EthernetPhysicalChannel are reserved by the AUTOSAR standard:
    - WIRED: This represents the usage of the EthernetPhysicalChannel in case of a wired ethernet connection
    - WIRELESS: This represents the usage of the EthernetPhysicalChannel in case of a wireless ethernet connection

    [constr_3334] Allowed references between EthernetPhysicalChannel and EthernetCommunicationConnector: An EthernetPhysicalChannel is only allowed to reference EthernetCommunicationConnectors in the role commConnector that have the same category value as the referencing EthernetPhysicalChannel.

    [constr_3365] EthernetPhysicalChannels with different category values are not allowed within an EthernetCluster: A mix of EthernetPhysicalChannels with different category values within an EthernetCluster is currently not supported by AUTOSAR.

    [constr_3336] EthernetPhysicalChannel.soAdConfig in case of WIRELESS EthernetPhysicalChannel: If EthernetPhysicalChannel has the category WIRELESS then the EthernetPhysicalChannel shall not aggregate the SoAdConfig.
    """

    # EthernetPhysicalChannel method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.49, p.105 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createNetworkEndpoint  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNetworkEndpoints    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSoAdConfig          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSoAdConfig          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createVlanConfig       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlan                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of NetworkEndpoints that are used in the VLan.
        self.networkEndpoints: List[NetworkEndpoint] = []

        # SoAd Configuration for one specific Physical Channel.
        self.soAdConfig: Optional[SoAdConfig] = None

        # VLAN Configuration.
        self.vlan: Optional[VlanConfig] = None

    def createNetworkEndpoint(self, short_name: str) -> NetworkEndpoint:
        """Collection of NetworkEndpoints that are used in the VLan."""
        if not self.IsReferrableElementExists(short_name, NetworkEndpoint):
            end_point = NetworkEndpoint(self, short_name)
            self.addReferrableElement(end_point)
            self.networkEndpoints.append(end_point)
        return cast(NetworkEndpoint, self.getReferrableElement(short_name, NetworkEndpoint))

    def getNetworkEndpoints(self) -> List[NetworkEndpoint]:
        """Collection of NetworkEndpoints that are used in the VLan."""
        return self.networkEndpoints

    def getSoAdConfig(self) -> Optional[SoAdConfig]:
        """SoAd Configuration for one specific Physical Channel."""
        return self.soAdConfig

    def setSoAdConfig(self, value: Optional[SoAdConfig]) -> EthernetPhysicalChannel:
        """
        SoAd Configuration for one specific Physical Channel.
        A None value is a no-op and does not overwrite an existing soAdConfig.
        """
        if value is not None:
            self.soAdConfig = value
        return self

    def createVlanConfig(self, short_name: str) -> VlanConfig:
        """VLAN Configuration."""
        if not self.IsReferrableElementExists(short_name, VlanConfig):
            config = VlanConfig(self, short_name)
            self.addReferrableElement(config)
            self.vlan = config
        return cast(VlanConfig, self.getReferrableElement(short_name, VlanConfig))

    def getVlan(self) -> Optional[VlanConfig]:
        """VLAN Configuration."""
        return self.vlan


class EthIpProps(ARElement):
    """This meta-class is used to configure the EcuInstance specific IP attributes. Tags: atp.recommendedPackage=EthIpProps"""

    # EthIpProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.100, p.146
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIpv4Props    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv4Props    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpv6Props    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv6Props    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # The IPV-4-PROPS child fully round-trips via readIpv4Props/writeIpv4Props since the
    # Ipv4Props sync (Table 3.101); the IPV-6-PROPS child fully round-trips via
    # readIpv6Props/writeIpv6Props since the Ipv6Props sync (Table 3.105) — its children
    # Dhcpv6Props (Table 3.107), Ipv6FragmentationProps (Table 3.106) and Ipv6NdpProps
    # (Table 3.108) fully round-trip since their syncs.

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Configuration options for IPv4.
        self.ipv4Props: Optional[Ipv4Props] = None

        # Configuration options for IPv6.
        self.ipv6Props: Optional[Ipv6Props] = None

    def getIpv4Props(self) -> Optional[Ipv4Props]:
        """
        Configuration options for IPv4.
        """
        return self.ipv4Props

    def setIpv4Props(self, value: Optional[Ipv4Props]) -> EthIpProps:
        """
        Configuration options for IPv4.

        A None value is a no-op and does not overwrite an existing ipv4Props.
        """
        if value is not None:
            self.ipv4Props = value
        return self

    def getIpv6Props(self) -> Optional[Ipv6Props]:
        """
        Configuration options for IPv6.
        """
        return self.ipv6Props

    def setIpv6Props(self, value: Optional[Ipv6Props]) -> EthIpProps:
        """
        Configuration options for IPv6.

        A None value is a no-op and does not overwrite an existing ipv6Props.
        """
        if value is not None:
            self.ipv6Props = value
        return self


class Ipv4Props(ARObject):
    """This meta-class specifies the configuration options for IPv4."""

    # Ipv4Props method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.101, p.146
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArpProps           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArpProps           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAutoIpProps        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAutoIpProps        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFragmentationProps [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFragmentationProps [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # All three children fully round-trip via readIpv4ArpProps/writeIpv4ArpProps,
    # readIpv4AutoIpProps/writeIpv4AutoIpProps and
    # readIpv4FragmentationProps/writeIpv4FragmentationProps since the Ipv4ArpProps
    # (Table 3.102), Ipv4AutoIpProps (Table 3.103) and Ipv4FragmentationProps
    # (Table 3.104) syncs.

    def __init__(self):
        super().__init__()

        # Configuration properties for the ARP (Address Resolution Protocol).
        self.arpProps: Optional[Ipv4ArpProps] = None

        # Configuration options for Auto-IP (automatic private IP addressing).
        self.autoIpProps: Optional[Ipv4AutoIpProps] = None

        # Configuration options for IPv4 packet fragmentation/reassembly.
        self.fragmentationProps: Optional[Ipv4FragmentationProps] = None

    def getArpProps(self) -> Optional[Ipv4ArpProps]:
        """Configuration properties for the ARP (Address Resolution Protocol)."""
        return self.arpProps

    def setArpProps(self, value: Optional[Ipv4ArpProps]) -> Ipv4Props:
        """
        Configuration properties for the ARP (Address Resolution Protocol).

        A None value is a no-op and does not overwrite an existing arpProps.
        """
        if value is not None:
            self.arpProps = value
        return self

    def getAutoIpProps(self) -> Optional[Ipv4AutoIpProps]:
        """Configuration options for Auto-IP (automatic private IP addressing)."""
        return self.autoIpProps

    def setAutoIpProps(self, value: Optional[Ipv4AutoIpProps]) -> Ipv4Props:
        """
        Configuration options for Auto-IP (automatic private IP addressing).

        A None value is a no-op and does not overwrite an existing autoIpProps.
        """
        if value is not None:
            self.autoIpProps = value
        return self

    def getFragmentationProps(self) -> Optional[Ipv4FragmentationProps]:
        """Configuration options for IPv4 packet fragmentation/reassembly."""
        return self.fragmentationProps

    def setFragmentationProps(self, value: Optional[Ipv4FragmentationProps]) -> Ipv4Props:
        """
        Configuration options for IPv4 packet fragmentation/reassembly.

        A None value is a no-op and does not overwrite an existing fragmentationProps.
        """
        if value is not None:
            self.fragmentationProps = value
        return self


class Ipv4ArpProps(ARObject):
    """Specifies the configuration options for the ARP (Address Resolution Protocol)."""

    # Ipv4ArpProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.102, p.146
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpIpArpNumGratuitousArpOnStartup  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpArpNumGratuitousArpOnStartup  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpArpPacketQueueEnabled         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpArpPacketQueueEnabled         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpArpRequestTimeout             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpArpRequestTimeout             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpArpTableEntryTimeout          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpArpTableEntryTimeout          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute specifies the number of gratuitous ARP replies which shall be sent on assignment of a new IP address.
        self.tcpIpArpNumGratuitousArpOnStartup: Optional[PositiveInteger] = None

        # This attribute enables (TRUE) or disables (FALSE) support of the ARP Packet Queue according to IETF RFC 1122, section 2.3.2.2.
        self.tcpIpArpPacketQueueEnabled: Optional[Boolean] = None

        # This attribute specifies a timeout in seconds for the validity of ARP requests. After the transmission of an ARP request the TcpIp shall skip the transmission of any further ARP requests to the same destination within a duration of tcpIpArpRequestTimeout seconds. (IETF RFC 1122, section 2.3.2.1).
        self.tcpIpArpRequestTimeout: Optional[TimeValue] = None

        # This attribute specifies the timeout in seconds after which an unused ARP entry is removed.
        self.tcpIpArpTableEntryTimeout: Optional[TimeValue] = None

    def getTcpIpArpNumGratuitousArpOnStartup(self) -> Optional[PositiveInteger]:
        """This attribute specifies the number of gratuitous ARP replies which shall be sent on assignment of a new IP address."""
        return self.tcpIpArpNumGratuitousArpOnStartup

    def setTcpIpArpNumGratuitousArpOnStartup(self, value: Optional[PositiveInteger]) -> Ipv4ArpProps:
        """
        This attribute specifies the number of gratuitous ARP replies which shall be sent on assignment of a new IP address.

        A None value is a no-op and does not overwrite an existing tcpIpArpNumGratuitousArpOnStartup.
        """
        if value is not None:
            self.tcpIpArpNumGratuitousArpOnStartup = value
        return self

    def getTcpIpArpPacketQueueEnabled(self) -> Optional[Boolean]:
        """This attribute enables (TRUE) or disables (FALSE) support of the ARP Packet Queue according to IETF RFC 1122, section 2.3.2.2."""
        return self.tcpIpArpPacketQueueEnabled

    def setTcpIpArpPacketQueueEnabled(self, value: Optional[Boolean]) -> Ipv4ArpProps:
        """
        This attribute enables (TRUE) or disables (FALSE) support of the ARP Packet Queue according to IETF RFC 1122, section 2.3.2.2.

        A None value is a no-op and does not overwrite an existing tcpIpArpPacketQueueEnabled.
        """
        if value is not None:
            self.tcpIpArpPacketQueueEnabled = value
        return self

    def getTcpIpArpRequestTimeout(self) -> Optional[TimeValue]:
        """This attribute specifies a timeout in seconds for the validity of ARP requests. After the transmission of an ARP request the TcpIp shall skip the transmission of any further ARP requests to the same destination within a duration of tcpIpArpRequestTimeout seconds. (IETF RFC 1122, section 2.3.2.1)."""
        return self.tcpIpArpRequestTimeout

    def setTcpIpArpRequestTimeout(self, value: Optional[TimeValue]) -> Ipv4ArpProps:
        """
        This attribute specifies a timeout in seconds for the validity of ARP requests. After the transmission of an ARP request the TcpIp shall skip the transmission of any further ARP requests to the same destination within a duration of tcpIpArpRequestTimeout seconds. (IETF RFC 1122, section 2.3.2.1).

        A None value is a no-op and does not overwrite an existing tcpIpArpRequestTimeout.
        """
        if value is not None:
            self.tcpIpArpRequestTimeout = value
        return self

    def getTcpIpArpTableEntryTimeout(self) -> Optional[TimeValue]:
        """This attribute specifies the timeout in seconds after which an unused ARP entry is removed."""
        return self.tcpIpArpTableEntryTimeout

    def setTcpIpArpTableEntryTimeout(self, value: Optional[TimeValue]) -> Ipv4ArpProps:
        """
        This attribute specifies the timeout in seconds after which an unused ARP entry is removed.

        A None value is a no-op and does not overwrite an existing tcpIpArpTableEntryTimeout.
        """
        if value is not None:
            self.tcpIpArpTableEntryTimeout = value
        return self


class Ipv4AutoIpProps(ARObject):
    """Specifies the configuration options for Auto-IP (automatic private IP addressing)."""

    # Ipv4AutoIpProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.103, p.147
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpIpAutoIpInitTimeout  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpAutoIpInitTimeout  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute specifies the time in seconds Auto-IP waits at startup, before beginning with ARP probing. This delay is used to give DHCP time to acquire a lease in case a DHCP server is present.
        self.tcpIpAutoIpInitTimeout: Optional[TimeValue] = None

    def getTcpIpAutoIpInitTimeout(self) -> Optional[TimeValue]:
        """This attribute specifies the time in seconds Auto-IP waits at startup, before beginning with ARP probing. This delay is used to give DHCP time to acquire a lease in case a DHCP server is present."""
        return self.tcpIpAutoIpInitTimeout

    def setTcpIpAutoIpInitTimeout(self, value: Optional[TimeValue]) -> Ipv4AutoIpProps:
        """
        This attribute specifies the time in seconds Auto-IP waits at startup, before beginning with ARP probing. This delay is used to give DHCP time to acquire a lease in case a DHCP server is present.

        A None value is a no-op and does not overwrite an existing tcpIpAutoIpInitTimeout.
        """
        if value is not None:
            self.tcpIpAutoIpInitTimeout = value
        return self


class Ipv4FragmentationProps(ARObject):
    """Specifies the configuration options for IPv4 packet fragmentation/reassembly."""

    # Ipv4FragmentationProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.104, p.147
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpIpIpFragmentationRxEnabled [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIpFragmentationRxEnabled [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIpNumFragments           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIpNumFragments           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIpNumReassDgrams         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIpNumReassDgrams         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIpReassTimeout           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIpReassTimeout           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Enables (TRUE) or disables (FALSE) support for reassembling of incoming datagrams that are fragmented according to IETF RFC 815 (IP Datagram Reassembly Algorithms).
        self.tcpIpIpFragmentationRxEnabled: Optional[Boolean] = None

        # Specifies the maximum number of IP fragments per datagram.
        self.tcpIpIpNumFragments: Optional[PositiveInteger] = None

        # Specifies the maximum number of fragmented IP datagrams that can be reassembled in parallel.
        self.tcpIpIpNumReassDgrams: Optional[PositiveInteger] = None

        # Specifies the timeout in [s] after which an incomplete datagram gets discarded.
        self.tcpIpIpReassTimeout: Optional[TimeValue] = None

    def getTcpIpIpFragmentationRxEnabled(self) -> Optional[Boolean]:
        """Enables (TRUE) or disables (FALSE) support for reassembling of incoming datagrams that are fragmented according to IETF RFC 815 (IP Datagram Reassembly Algorithms)."""
        return self.tcpIpIpFragmentationRxEnabled

    def setTcpIpIpFragmentationRxEnabled(self, value: Optional[Boolean]) -> Ipv4FragmentationProps:
        """
        Enables (TRUE) or disables (FALSE) support for reassembling of incoming datagrams that are fragmented according to IETF RFC 815 (IP Datagram Reassembly Algorithms).

        A None value is a no-op and does not overwrite an existing tcpIpIpFragmentationRxEnabled.
        """
        if value is not None:
            self.tcpIpIpFragmentationRxEnabled = value
        return self

    def getTcpIpIpNumFragments(self) -> Optional[PositiveInteger]:
        """Specifies the maximum number of IP fragments per datagram."""
        return self.tcpIpIpNumFragments

    def setTcpIpIpNumFragments(self, value: Optional[PositiveInteger]) -> Ipv4FragmentationProps:
        """
        Specifies the maximum number of IP fragments per datagram.

        A None value is a no-op and does not overwrite an existing tcpIpIpNumFragments.
        """
        if value is not None:
            self.tcpIpIpNumFragments = value
        return self

    def getTcpIpIpNumReassDgrams(self) -> Optional[PositiveInteger]:
        """Specifies the maximum number of fragmented IP datagrams that can be reassembled in parallel."""
        return self.tcpIpIpNumReassDgrams

    def setTcpIpIpNumReassDgrams(self, value: Optional[PositiveInteger]) -> Ipv4FragmentationProps:
        """
        Specifies the maximum number of fragmented IP datagrams that can be reassembled in parallel.

        A None value is a no-op and does not overwrite an existing tcpIpIpNumReassDgrams.
        """
        if value is not None:
            self.tcpIpIpNumReassDgrams = value
        return self

    def getTcpIpIpReassTimeout(self) -> Optional[TimeValue]:
        """Specifies the timeout in [s] after which an incomplete datagram gets discarded."""
        return self.tcpIpIpReassTimeout

    def setTcpIpIpReassTimeout(self, value: Optional[TimeValue]) -> Ipv4FragmentationProps:
        """
        Specifies the timeout in [s] after which an incomplete datagram gets discarded.

        A None value is a no-op and does not overwrite an existing tcpIpIpReassTimeout.
        """
        if value is not None:
            self.tcpIpIpReassTimeout = value
        return self


class Dhcpv6Props(ARObject):
    """This meta-class specifies the configuration options for DHCPv6."""

    # Dhcpv6Props method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.107, p.149
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpIpDhcpV6CnfDelayMax   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpDhcpV6CnfDelayMax   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpDhcpV6CnfDelayMin   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpDhcpV6CnfDelayMin   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpDhcpV6InfDelayMax   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpDhcpV6InfDelayMax   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpDhcpV6InfDelayMin   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpDhcpV6InfDelayMin   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpDhcpV6SolDelayMax   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpDhcpV6SolDelayMax   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpDhcpV6SolDelayMin   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpDhcpV6SolDelayMin   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Maximum delay in seconds before sending the first Confirm message. If this value is bigger than the previous minimum delay value a random delay will be chosen from the interval.
        self.tcpIpDhcpV6CnfDelayMax: Optional[TimeValue] = None

        # Minimum delay in seconds before the first Confirm message will be sent.
        self.tcpIpDhcpV6CnfDelayMin: Optional[TimeValue] = None

        # Maximum delay in seconds before sending the first Information Request message. If this value is bigger than the previous minimum delay value a random delay will be chosen from the interval.
        self.tcpIpDhcpV6InfDelayMax: Optional[TimeValue] = None

        # Minimum delay (s) before the first Information Request message will be sent.
        self.tcpIpDhcpV6InfDelayMin: Optional[TimeValue] = None

        # Maximum delay in seconds before sending the first Solicit message. If this value is bigger than the previous minimum delay value a random delay will be chosen from the interval.
        self.tcpIpDhcpV6SolDelayMax: Optional[TimeValue] = None

        # Minimum delay (s) before the first Solicit message will be sent.
        self.tcpIpDhcpV6SolDelayMin: Optional[TimeValue] = None

    def getTcpIpDhcpV6CnfDelayMax(self) -> Optional[TimeValue]:
        """Maximum delay in seconds before sending the first Confirm message. If this value is bigger than the previous minimum delay value a random delay will be chosen from the interval."""
        return self.tcpIpDhcpV6CnfDelayMax

    def setTcpIpDhcpV6CnfDelayMax(self, value: Optional[TimeValue]) -> Dhcpv6Props:
        """
        Maximum delay in seconds before sending the first Confirm message. If this value is bigger than the previous minimum delay value a random delay will be chosen from the interval.

        A None value is a no-op and does not overwrite an existing tcpIpDhcpV6CnfDelayMax.
        """
        if value is not None:
            self.tcpIpDhcpV6CnfDelayMax = value
        return self

    def getTcpIpDhcpV6CnfDelayMin(self) -> Optional[TimeValue]:
        """Minimum delay in seconds before the first Confirm message will be sent."""
        return self.tcpIpDhcpV6CnfDelayMin

    def setTcpIpDhcpV6CnfDelayMin(self, value: Optional[TimeValue]) -> Dhcpv6Props:
        """
        Minimum delay in seconds before the first Confirm message will be sent.

        A None value is a no-op and does not overwrite an existing tcpIpDhcpV6CnfDelayMin.
        """
        if value is not None:
            self.tcpIpDhcpV6CnfDelayMin = value
        return self

    def getTcpIpDhcpV6InfDelayMax(self) -> Optional[TimeValue]:
        """Maximum delay in seconds before sending the first Information Request message. If this value is bigger than the previous minimum delay value a random delay will be chosen from the interval."""
        return self.tcpIpDhcpV6InfDelayMax

    def setTcpIpDhcpV6InfDelayMax(self, value: Optional[TimeValue]) -> Dhcpv6Props:
        """
        Maximum delay in seconds before sending the first Information Request message. If this value is bigger than the previous minimum delay value a random delay will be chosen from the interval.

        A None value is a no-op and does not overwrite an existing tcpIpDhcpV6InfDelayMax.
        """
        if value is not None:
            self.tcpIpDhcpV6InfDelayMax = value
        return self

    def getTcpIpDhcpV6InfDelayMin(self) -> Optional[TimeValue]:
        """Minimum delay (s) before the first Information Request message will be sent."""
        return self.tcpIpDhcpV6InfDelayMin

    def setTcpIpDhcpV6InfDelayMin(self, value: Optional[TimeValue]) -> Dhcpv6Props:
        """
        Minimum delay (s) before the first Information Request message will be sent.

        A None value is a no-op and does not overwrite an existing tcpIpDhcpV6InfDelayMin.
        """
        if value is not None:
            self.tcpIpDhcpV6InfDelayMin = value
        return self

    def getTcpIpDhcpV6SolDelayMax(self) -> Optional[TimeValue]:
        """Maximum delay in seconds before sending the first Solicit message. If this value is bigger than the previous minimum delay value a random delay will be chosen from the interval."""
        return self.tcpIpDhcpV6SolDelayMax

    def setTcpIpDhcpV6SolDelayMax(self, value: Optional[TimeValue]) -> Dhcpv6Props:
        """
        Maximum delay in seconds before sending the first Solicit message. If this value is bigger than the previous minimum delay value a random delay will be chosen from the interval.

        A None value is a no-op and does not overwrite an existing tcpIpDhcpV6SolDelayMax.
        """
        if value is not None:
            self.tcpIpDhcpV6SolDelayMax = value
        return self

    def getTcpIpDhcpV6SolDelayMin(self) -> Optional[TimeValue]:
        """Minimum delay (s) before the first Solicit message will be sent."""
        return self.tcpIpDhcpV6SolDelayMin

    def setTcpIpDhcpV6SolDelayMin(self, value: Optional[TimeValue]) -> Dhcpv6Props:
        """
        Minimum delay (s) before the first Solicit message will be sent.

        A None value is a no-op and does not overwrite an existing tcpIpDhcpV6SolDelayMin.
        """
        if value is not None:
            self.tcpIpDhcpV6SolDelayMin = value
        return self


class Ipv6FragmentationProps(ARObject):
    """This meta-class specifies the configuration options for IPv6 packet fragmentation/reassembly."""

    # Ipv6FragmentationProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.106, p.148
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpIpIpReassemblyBufferCount  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIpReassemblyBufferCount  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIpReassemblyBufferSize   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIpReassemblyBufferSize   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIpReassemblySegmentCount [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIpReassemblySegmentCount [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIpReassemblyTimeout      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIpReassemblyTimeout      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIpTxFragmentBufferCount  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIpTxFragmentBufferCount  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIpTxFragmentBufferSize   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIpTxFragmentBufferSize   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Number of buffers that can be used for fragment reassembly. In case of a reassembly error or if not all fragments are received in time this buffer will be blocked until the specified "Fragment Reassembly Timeout" has been exceeded. A value of 0 disables fragment reassembly.
        self.tcpIpIpReassemblyBufferCount: Optional[PositiveInteger] = None

        # Size of each fragment tx buffer in bytes.
        self.tcpIpIpReassemblyBufferSize: Optional[PositiveInteger] = None

        # Specifies the maximum number of consecutive data segments that can be managed in each reassembly buffer. If all fragments are received in order, only one segment will be needed. To deal with fragments received out of order this value should be configured bigger than 1.
        self.tcpIpIpReassemblySegmentCount: Optional[PositiveInteger] = None

        # Specifies the timeout in seconds after which an incomplete datagram gets discarded.
        self.tcpIpIpReassemblyTimeout: Optional[TimeValue] = None

        # These buffers will be used if the IpV6 receives packets from the upper layer that do not fit into the MTU and thus must be fragmented. A value of 0 disables tx fragmentation.
        self.tcpIpIpTxFragmentBufferCount: Optional[PositiveInteger] = None

        # Size of each fragment tx buffer in bytes.
        self.tcpIpIpTxFragmentBufferSize: Optional[PositiveInteger] = None

    def getTcpIpIpReassemblyBufferCount(self) -> Optional[PositiveInteger]:
        """Number of buffers that can be used for fragment reassembly. In case of a reassembly error or if not all fragments are received in time this buffer will be blocked until the specified "Fragment Reassembly Timeout" has been exceeded. A value of 0 disables fragment reassembly."""
        return self.tcpIpIpReassemblyBufferCount

    def setTcpIpIpReassemblyBufferCount(self, value: Optional[PositiveInteger]) -> Ipv6FragmentationProps:
        """
        Number of buffers that can be used for fragment reassembly. In case of a reassembly error or if not all fragments are received in time this buffer will be blocked until the specified "Fragment Reassembly Timeout" has been exceeded. A value of 0 disables fragment reassembly.

        A None value is a no-op and does not overwrite an existing tcpIpIpReassemblyBufferCount.
        """
        if value is not None:
            self.tcpIpIpReassemblyBufferCount = value
        return self

    def getTcpIpIpReassemblyBufferSize(self) -> Optional[PositiveInteger]:
        """Size of each fragment tx buffer in bytes."""
        return self.tcpIpIpReassemblyBufferSize

    def setTcpIpIpReassemblyBufferSize(self, value: Optional[PositiveInteger]) -> Ipv6FragmentationProps:
        """
        Size of each fragment tx buffer in bytes.

        A None value is a no-op and does not overwrite an existing tcpIpIpReassemblyBufferSize.
        """
        if value is not None:
            self.tcpIpIpReassemblyBufferSize = value
        return self

    def getTcpIpIpReassemblySegmentCount(self) -> Optional[PositiveInteger]:
        """Specifies the maximum number of consecutive data segments that can be managed in each reassembly buffer. If all fragments are received in order, only one segment will be needed. To deal with fragments received out of order this value should be configured bigger than 1."""
        return self.tcpIpIpReassemblySegmentCount

    def setTcpIpIpReassemblySegmentCount(self, value: Optional[PositiveInteger]) -> Ipv6FragmentationProps:
        """
        Specifies the maximum number of consecutive data segments that can be managed in each reassembly buffer. If all fragments are received in order, only one segment will be needed. To deal with fragments received out of order this value should be configured bigger than 1.

        A None value is a no-op and does not overwrite an existing tcpIpIpReassemblySegmentCount.
        """
        if value is not None:
            self.tcpIpIpReassemblySegmentCount = value
        return self

    def getTcpIpIpReassemblyTimeout(self) -> Optional[TimeValue]:
        """Specifies the timeout in seconds after which an incomplete datagram gets discarded."""
        return self.tcpIpIpReassemblyTimeout

    def setTcpIpIpReassemblyTimeout(self, value: Optional[TimeValue]) -> Ipv6FragmentationProps:
        """
        Specifies the timeout in seconds after which an incomplete datagram gets discarded.

        A None value is a no-op and does not overwrite an existing tcpIpIpReassemblyTimeout.
        """
        if value is not None:
            self.tcpIpIpReassemblyTimeout = value
        return self

    def getTcpIpIpTxFragmentBufferCount(self) -> Optional[PositiveInteger]:
        """These buffers will be used if the IpV6 receives packets from the upper layer that do not fit into the MTU and thus must be fragmented. A value of 0 disables tx fragmentation."""
        return self.tcpIpIpTxFragmentBufferCount

    def setTcpIpIpTxFragmentBufferCount(self, value: Optional[PositiveInteger]) -> Ipv6FragmentationProps:
        """
        These buffers will be used if the IpV6 receives packets from the upper layer that do not fit into the MTU and thus must be fragmented. A value of 0 disables tx fragmentation.

        A None value is a no-op and does not overwrite an existing tcpIpIpTxFragmentBufferCount.
        """
        if value is not None:
            self.tcpIpIpTxFragmentBufferCount = value
        return self

    def getTcpIpIpTxFragmentBufferSize(self) -> Optional[PositiveInteger]:
        """Size of each fragment tx buffer in bytes."""
        return self.tcpIpIpTxFragmentBufferSize

    def setTcpIpIpTxFragmentBufferSize(self, value: Optional[PositiveInteger]) -> Ipv6FragmentationProps:
        """
        Size of each fragment tx buffer in bytes.

        A None value is a no-op and does not overwrite an existing tcpIpIpTxFragmentBufferSize.
        """
        if value is not None:
            self.tcpIpIpTxFragmentBufferSize = value
        return self


class Ipv6NdpProps(ARObject):
    """This meta-class specifies the configuration options for the Neighbor Discovery Protocol for IPv6."""

    # Ipv6NdpProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.108, p.151
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpIpNdpDefaultReachableTime                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpDefaultReachableTime                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpDefaultRetransTimer                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpDefaultRetransTimer                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpDefaultRouterListSize                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpDefaultRouterListSize                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpDefensiveProcessing                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpDefensiveProcessing                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpDelayFirstProbeTimeValue                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpDelayFirstProbeTimeValue                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpDestinationCacheSize                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpDestinationCacheSize                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpDynamicHopLimitEnabled                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpDynamicHopLimitEnabled                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpDynamicMtuEnabled                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpDynamicMtuEnabled                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpDynamicReachableTimeEnabled             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpDynamicReachableTimeEnabled             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpDynamicRetransTimeEnabled               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpDynamicRetransTimeEnabled               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpMaxRandomFactor                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpMaxRandomFactor                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpMaxRtrSolicitationDelay                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpMaxRtrSolicitationDelay                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpMaxRtrSolicitations                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpMaxRtrSolicitations                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpMinRandomFactor                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpMinRandomFactor                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpNeighborUnreachabilityDetectionEnabled  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpNeighborUnreachabilityDetectionEnabled  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpNumMulticastSolicitations               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpNumMulticastSolicitations               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpNumUnicastSolicitations                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpNumUnicastSolicitations                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpPacketQueueEnabled                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpPacketQueueEnabled                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpPrefixListSize                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpPrefixListSize                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpRandomReachableTimeEnabled              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpRandomReachableTimeEnabled              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpRndRtrSolicitationDelayEnabled          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpRndRtrSolicitationDelayEnabled          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpRtrSolicitationInterval                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpRtrSolicitationInterval                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpSlaacDadNumberOfTransmissions           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpSlaacDadNumberOfTransmissions           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpSlaacDadRetransmissionDelay             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpSlaacDadRetransmissionDelay             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpSlaacDelayEnabled                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpSlaacDelayEnabled                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpNdpSlaacOptimisticDadEnabled               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpNdpSlaacOptimisticDadEnabled               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Configuration of the ReachableTime (s) specified in [RFC4861 6.3.2. Host Variables].
        self.tcpIpNdpDefaultReachableTime: Optional[TimeValue] = None

        # Configures the default value (s) for the RetransTimer variable specified in [RFC4861 6.3.2. Host Variables].
        self.tcpIpNdpDefaultRetransTimer: Optional[TimeValue] = None

        # Maximum number of default router entries.
        self.tcpIpNdpDefaultRouterListSize: Optional[PositiveInteger] = None

        # If enabled the NDP shall only process Neighbor Advertisements which are received in reaction to a previously transmitted Neighbor Solicitation as well as skipping updates to the Neighbor Cache based on received Neighbor Solicitations. If disabled all Neighbor Advertisements and Solicitations shall be processed as specified in RFC4861.
        self.tcpIpNdpDefensiveProcessing: Optional[Boolean] = None

        # Delay before sending the first NUD probe in (s).
        self.tcpIpNdpDelayFirstProbeTimeValue: Optional[TimeValue] = None

        # Maximum number of entries in the destination cache.
        self.tcpIpNdpDestinationCacheSize: Optional[PositiveInteger] = None

        # If enabled the default hop limit may be reconfigured based on received Router Advertisements.
        self.tcpIpNdpDynamicHopLimitEnabled: Optional[Boolean] = None

        # Allow dynamic reconfiguration of link MTU via Router Advertisements.
        self.tcpIpNdpDynamicMtuEnabled: Optional[Boolean] = None

        # If enabled the default Reachable Time value may be reconfigured based on received Router Advertisements.
        self.tcpIpNdpDynamicReachableTimeEnabled: Optional[Boolean] = None

        # If enabled the default Retransmit Timer value may be reconfigured based on received Router Advertisements.
        self.tcpIpNdpDynamicRetransTimeEnabled: Optional[Boolean] = None

        # Maximum random factor used for randomization
        self.tcpIpNdpMaxRandomFactor: Optional[PositiveInteger] = None

        # Maximum delay before the first Router Solicitation will be sent after interface initialization in (s).
        self.tcpIpNdpMaxRtrSolicitationDelay: Optional[TimeValue] = None

        # Maximum number of Router Solicitations that will be sent before the first Router Advertisement has been received.
        self.tcpIpNdpMaxRtrSolicitations: Optional[PositiveInteger] = None

        # Minimum random factor used for randomization
        self.tcpIpNdpMinRandomFactor: Optional[PositiveInteger] = None

        # Neighbor Unreachability Detection is used to remove unused entries from the neighbor cache. This feature is a basic feature of NDP and should be turned on.
        self.tcpIpNdpNeighborUnreachabilityDetectionEnabled: Optional[Boolean] = None

        # Maximum number of multicast solicitations that will be sent when performing address resolution.
        self.tcpIpNdpNumMulticastSolicitations: Optional[PositiveInteger] = None

        # Maximum number of unicast solicitations that will be sent when performig Neighbor Unreachability Detection.
        self.tcpIpNdpNumUnicastSolicitations: Optional[PositiveInteger] = None

        # Enables (TRUE) or disables (FALSE) support of a NDP Packet Queue according to IETF RFC 4861, section 7.2.2.
        self.tcpIpNdpPacketQueueEnabled: Optional[Boolean] = None

        # Maximum number of entries in the on-link prefix list.
        self.tcpIpNdpPrefixListSize: Optional[PositiveInteger] = None

        # If enabled the value of ReachableTime will be multiplied with a random value between MIN_RANDOM_FACTOR and MAX_RANDOM_FACTOR in order to prevent multiple nodes from transmitting at exactly the same time.
        self.tcpIpNdpRandomReachableTimeEnabled: Optional[Boolean] = None

        # If enabled the first router solicitation will be delayed randomly from [0...MAX_RTR_SOLICITATION_DELAY]. Otherwise the first router solicitation will be sent after exactly MAX_RTR_SOLICITATION_DELAY milliseconds.
        self.tcpIpNdpRndRtrSolicitationDelayEnabled: Optional[Boolean] = None

        # Interval between consecutive Router Solicitations in (s).
        self.tcpIpNdpRtrSolicitationInterval: Optional[TimeValue] = None

        # Number of Neighbor Solicitations that have to be unanswered in order to set an autoconfigurated address to PREFERRED (usable) state.
        self.tcpIpNdpSlaacDadNumberOfTransmissions: Optional[PositiveInteger] = None

        # Sets the maximum value for the address configuration delay (s).
        self.tcpIpNdpSlaacDadRetransmissionDelay: Optional[TimeValue] = None

        # If enabled transmission of the first DAD Neighbor Solicitation will be delayed by a random value from [0...MAX_DAD_DELAY].
        self.tcpIpNdpSlaacDelayEnabled: Optional[Boolean] = None

        # Enable Optimistic Duplicate Address Detection (DAD) according to RFC4429.
        self.tcpIpNdpSlaacOptimisticDadEnabled: Optional[Boolean] = None

    def getTcpIpNdpDefaultReachableTime(self) -> Optional[TimeValue]:
        """Configuration of the ReachableTime (s) specified in [RFC4861 6.3.2. Host Variables]."""
        return self.tcpIpNdpDefaultReachableTime

    def setTcpIpNdpDefaultReachableTime(self, value: Optional[TimeValue]) -> Ipv6NdpProps:
        """
        Configuration of the ReachableTime (s) specified in [RFC4861 6.3.2. Host Variables].

        A None value is a no-op and does not overwrite an existing tcpIpNdpDefaultReachableTime.
        """
        if value is not None:
            self.tcpIpNdpDefaultReachableTime = value
        return self

    def getTcpIpNdpDefaultRetransTimer(self) -> Optional[TimeValue]:
        """Configures the default value (s) for the RetransTimer variable specified in [RFC4861 6.3.2. Host Variables]."""
        return self.tcpIpNdpDefaultRetransTimer

    def setTcpIpNdpDefaultRetransTimer(self, value: Optional[TimeValue]) -> Ipv6NdpProps:
        """
        Configures the default value (s) for the RetransTimer variable specified in [RFC4861 6.3.2. Host Variables].

        A None value is a no-op and does not overwrite an existing tcpIpNdpDefaultRetransTimer.
        """
        if value is not None:
            self.tcpIpNdpDefaultRetransTimer = value
        return self

    def getTcpIpNdpDefaultRouterListSize(self) -> Optional[PositiveInteger]:
        """Maximum number of default router entries."""
        return self.tcpIpNdpDefaultRouterListSize

    def setTcpIpNdpDefaultRouterListSize(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Maximum number of default router entries.

        A None value is a no-op and does not overwrite an existing tcpIpNdpDefaultRouterListSize.
        """
        if value is not None:
            self.tcpIpNdpDefaultRouterListSize = value
        return self

    def getTcpIpNdpDefensiveProcessing(self) -> Optional[Boolean]:
        """
        If enabled the NDP shall only process Neighbor Advertisements which are received in reaction to a previously transmitted Neighbor Solicitation as well as skipping updates to the Neighbor Cache based on received Neighbor Solicitations. If disabled all Neighbor Advertisements and Solicitations shall be processed as specified in RFC4861.
        """
        return self.tcpIpNdpDefensiveProcessing

    def setTcpIpNdpDefensiveProcessing(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        If enabled the NDP shall only process Neighbor Advertisements which are received in reaction to a previously transmitted Neighbor Solicitation as well as skipping updates to the Neighbor Cache based on received Neighbor Solicitations. If disabled all Neighbor Advertisements and Solicitations shall be processed as specified in RFC4861.

        A None value is a no-op and does not overwrite an existing tcpIpNdpDefensiveProcessing.
        """
        if value is not None:
            self.tcpIpNdpDefensiveProcessing = value
        return self

    def getTcpIpNdpDelayFirstProbeTimeValue(self) -> Optional[TimeValue]:
        """Delay before sending the first NUD probe in (s)."""
        return self.tcpIpNdpDelayFirstProbeTimeValue

    def setTcpIpNdpDelayFirstProbeTimeValue(self, value: Optional[TimeValue]) -> Ipv6NdpProps:
        """
        Delay before sending the first NUD probe in (s).

        A None value is a no-op and does not overwrite an existing tcpIpNdpDelayFirstProbeTimeValue.
        """
        if value is not None:
            self.tcpIpNdpDelayFirstProbeTimeValue = value
        return self

    def getTcpIpNdpDestinationCacheSize(self) -> Optional[PositiveInteger]:
        """Maximum number of entries in the destination cache."""
        return self.tcpIpNdpDestinationCacheSize

    def setTcpIpNdpDestinationCacheSize(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Maximum number of entries in the destination cache.

        A None value is a no-op and does not overwrite an existing tcpIpNdpDestinationCacheSize.
        """
        if value is not None:
            self.tcpIpNdpDestinationCacheSize = value
        return self

    def getTcpIpNdpDynamicHopLimitEnabled(self) -> Optional[Boolean]:
        """If enabled the default hop limit may be reconfigured based on received Router Advertisements."""
        return self.tcpIpNdpDynamicHopLimitEnabled

    def setTcpIpNdpDynamicHopLimitEnabled(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        If enabled the default hop limit may be reconfigured based on received Router Advertisements.

        A None value is a no-op and does not overwrite an existing tcpIpNdpDynamicHopLimitEnabled.
        """
        if value is not None:
            self.tcpIpNdpDynamicHopLimitEnabled = value
        return self

    def getTcpIpNdpDynamicMtuEnabled(self) -> Optional[Boolean]:
        """Allow dynamic reconfiguration of link MTU via Router Advertisements."""
        return self.tcpIpNdpDynamicMtuEnabled

    def setTcpIpNdpDynamicMtuEnabled(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        Allow dynamic reconfiguration of link MTU via Router Advertisements.

        A None value is a no-op and does not overwrite an existing tcpIpNdpDynamicMtuEnabled.
        """
        if value is not None:
            self.tcpIpNdpDynamicMtuEnabled = value
        return self

    def getTcpIpNdpDynamicReachableTimeEnabled(self) -> Optional[Boolean]:
        """If enabled the default Reachable Time value may be reconfigured based on received Router Advertisements."""
        return self.tcpIpNdpDynamicReachableTimeEnabled

    def setTcpIpNdpDynamicReachableTimeEnabled(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        If enabled the default Reachable Time value may be reconfigured based on received Router Advertisements.

        A None value is a no-op and does not overwrite an existing tcpIpNdpDynamicReachableTimeEnabled.
        """
        if value is not None:
            self.tcpIpNdpDynamicReachableTimeEnabled = value
        return self

    def getTcpIpNdpDynamicRetransTimeEnabled(self) -> Optional[Boolean]:
        """If enabled the default Retransmit Timer value may be reconfigured based on received Router Advertisements."""
        return self.tcpIpNdpDynamicRetransTimeEnabled

    def setTcpIpNdpDynamicRetransTimeEnabled(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        If enabled the default Retransmit Timer value may be reconfigured based on received Router Advertisements.

        A None value is a no-op and does not overwrite an existing tcpIpNdpDynamicRetransTimeEnabled.
        """
        if value is not None:
            self.tcpIpNdpDynamicRetransTimeEnabled = value
        return self

    def getTcpIpNdpMaxRandomFactor(self) -> Optional[PositiveInteger]:
        """Maximum random factor used for randomization"""
        return self.tcpIpNdpMaxRandomFactor

    def setTcpIpNdpMaxRandomFactor(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Maximum random factor used for randomization

        A None value is a no-op and does not overwrite an existing tcpIpNdpMaxRandomFactor.
        """
        if value is not None:
            self.tcpIpNdpMaxRandomFactor = value
        return self

    def getTcpIpNdpMaxRtrSolicitationDelay(self) -> Optional[TimeValue]:
        """Maximum delay before the first Router Solicitation will be sent after interface initialization in (s)."""
        return self.tcpIpNdpMaxRtrSolicitationDelay

    def setTcpIpNdpMaxRtrSolicitationDelay(self, value: Optional[TimeValue]) -> Ipv6NdpProps:
        """
        Maximum delay before the first Router Solicitation will be sent after interface initialization in (s).

        A None value is a no-op and does not overwrite an existing tcpIpNdpMaxRtrSolicitationDelay.
        """
        if value is not None:
            self.tcpIpNdpMaxRtrSolicitationDelay = value
        return self

    def getTcpIpNdpMaxRtrSolicitations(self) -> Optional[PositiveInteger]:
        """Maximum number of Router Solicitations that will be sent before the first Router Advertisement has been received."""
        return self.tcpIpNdpMaxRtrSolicitations

    def setTcpIpNdpMaxRtrSolicitations(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Maximum number of Router Solicitations that will be sent before the first Router Advertisement has been received.

        A None value is a no-op and does not overwrite an existing tcpIpNdpMaxRtrSolicitations.
        """
        if value is not None:
            self.tcpIpNdpMaxRtrSolicitations = value
        return self

    def getTcpIpNdpMinRandomFactor(self) -> Optional[PositiveInteger]:
        """Minimum random factor used for randomization"""
        return self.tcpIpNdpMinRandomFactor

    def setTcpIpNdpMinRandomFactor(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Minimum random factor used for randomization

        A None value is a no-op and does not overwrite an existing tcpIpNdpMinRandomFactor.
        """
        if value is not None:
            self.tcpIpNdpMinRandomFactor = value
        return self

    def getTcpIpNdpNeighborUnreachabilityDetectionEnabled(self) -> Optional[Boolean]:
        """Neighbor Unreachability Detection is used to remove unused entries from the neighbor cache. This feature is a basic feature of NDP and should be turned on."""
        return self.tcpIpNdpNeighborUnreachabilityDetectionEnabled

    def setTcpIpNdpNeighborUnreachabilityDetectionEnabled(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        Neighbor Unreachability Detection is used to remove unused entries from the neighbor cache. This feature is a basic feature of NDP and should be turned on.

        A None value is a no-op and does not overwrite an existing tcpIpNdpNeighborUnreachabilityDetectionEnabled.
        """
        if value is not None:
            self.tcpIpNdpNeighborUnreachabilityDetectionEnabled = value
        return self

    def getTcpIpNdpNumMulticastSolicitations(self) -> Optional[PositiveInteger]:
        """Maximum number of multicast solicitations that will be sent when performing address resolution."""
        return self.tcpIpNdpNumMulticastSolicitations

    def setTcpIpNdpNumMulticastSolicitations(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Maximum number of multicast solicitations that will be sent when performing address resolution.

        A None value is a no-op and does not overwrite an existing tcpIpNdpNumMulticastSolicitations.
        """
        if value is not None:
            self.tcpIpNdpNumMulticastSolicitations = value
        return self

    def getTcpIpNdpNumUnicastSolicitations(self) -> Optional[PositiveInteger]:
        """Maximum number of unicast solicitations that will be sent when performig Neighbor Unreachability Detection."""
        return self.tcpIpNdpNumUnicastSolicitations

    def setTcpIpNdpNumUnicastSolicitations(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Maximum number of unicast solicitations that will be sent when performig Neighbor Unreachability Detection.

        A None value is a no-op and does not overwrite an existing tcpIpNdpNumUnicastSolicitations.
        """
        if value is not None:
            self.tcpIpNdpNumUnicastSolicitations = value
        return self

    def getTcpIpNdpPacketQueueEnabled(self) -> Optional[Boolean]:
        """Enables (TRUE) or disables (FALSE) support of a NDP Packet Queue according to IETF RFC 4861, section 7.2.2."""
        return self.tcpIpNdpPacketQueueEnabled

    def setTcpIpNdpPacketQueueEnabled(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        Enables (TRUE) or disables (FALSE) support of a NDP Packet Queue according to IETF RFC 4861, section 7.2.2.

        A None value is a no-op and does not overwrite an existing tcpIpNdpPacketQueueEnabled.
        """
        if value is not None:
            self.tcpIpNdpPacketQueueEnabled = value
        return self

    def getTcpIpNdpPrefixListSize(self) -> Optional[PositiveInteger]:
        """Maximum number of entries in the on-link prefix list."""
        return self.tcpIpNdpPrefixListSize

    def setTcpIpNdpPrefixListSize(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Maximum number of entries in the on-link prefix list.

        A None value is a no-op and does not overwrite an existing tcpIpNdpPrefixListSize.
        """
        if value is not None:
            self.tcpIpNdpPrefixListSize = value
        return self

    def getTcpIpNdpRandomReachableTimeEnabled(self) -> Optional[Boolean]:
        """
        If enabled the value of ReachableTime will be multiplied with a random value between MIN_RANDOM_FACTOR and MAX_RANDOM_FACTOR in order to prevent multiple nodes from transmitting at exactly the same time.
        """
        return self.tcpIpNdpRandomReachableTimeEnabled

    def setTcpIpNdpRandomReachableTimeEnabled(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        If enabled the value of ReachableTime will be multiplied with a random value between MIN_RANDOM_FACTOR and MAX_RANDOM_FACTOR in order to prevent multiple nodes from transmitting at exactly the same time.

        A None value is a no-op and does not overwrite an existing tcpIpNdpRandomReachableTimeEnabled.
        """
        if value is not None:
            self.tcpIpNdpRandomReachableTimeEnabled = value
        return self

    def getTcpIpNdpRndRtrSolicitationDelayEnabled(self) -> Optional[Boolean]:
        """
        If enabled the first router solicitation will be delayed randomly from [0...MAX_RTR_SOLICITATION_DELAY]. Otherwise the first router solicitation will be sent after exactly MAX_RTR_SOLICITATION_DELAY milliseconds.
        """
        return self.tcpIpNdpRndRtrSolicitationDelayEnabled

    def setTcpIpNdpRndRtrSolicitationDelayEnabled(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        If enabled the first router solicitation will be delayed randomly from [0...MAX_RTR_SOLICITATION_DELAY]. Otherwise the first router solicitation will be sent after exactly MAX_RTR_SOLICITATION_DELAY milliseconds.

        A None value is a no-op and does not overwrite an existing tcpIpNdpRndRtrSolicitationDelayEnabled.
        """
        if value is not None:
            self.tcpIpNdpRndRtrSolicitationDelayEnabled = value
        return self

    def getTcpIpNdpRtrSolicitationInterval(self) -> Optional[TimeValue]:
        """Interval between consecutive Router Solicitations in (s)."""
        return self.tcpIpNdpRtrSolicitationInterval

    def setTcpIpNdpRtrSolicitationInterval(self, value: Optional[TimeValue]) -> Ipv6NdpProps:
        """
        Interval between consecutive Router Solicitations in (s).

        A None value is a no-op and does not overwrite an existing tcpIpNdpRtrSolicitationInterval.
        """
        if value is not None:
            self.tcpIpNdpRtrSolicitationInterval = value
        return self

    def getTcpIpNdpSlaacDadNumberOfTransmissions(self) -> Optional[PositiveInteger]:
        """Number of Neighbor Solicitations that have to be unanswered in order to set an autoconfigurated address to PREFERRED (usable) state."""
        return self.tcpIpNdpSlaacDadNumberOfTransmissions

    def setTcpIpNdpSlaacDadNumberOfTransmissions(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Number of Neighbor Solicitations that have to be unanswered in order to set an autoconfigurated address to PREFERRED (usable) state.

        A None value is a no-op and does not overwrite an existing tcpIpNdpSlaacDadNumberOfTransmissions.
        """
        if value is not None:
            self.tcpIpNdpSlaacDadNumberOfTransmissions = value
        return self

    def getTcpIpNdpSlaacDadRetransmissionDelay(self) -> Optional[TimeValue]:
        """Sets the maximum value for the address configuration delay (s)."""
        return self.tcpIpNdpSlaacDadRetransmissionDelay

    def setTcpIpNdpSlaacDadRetransmissionDelay(self, value: Optional[TimeValue]) -> Ipv6NdpProps:
        """
        Sets the maximum value for the address configuration delay (s).

        A None value is a no-op and does not overwrite an existing tcpIpNdpSlaacDadRetransmissionDelay.
        """
        if value is not None:
            self.tcpIpNdpSlaacDadRetransmissionDelay = value
        return self

    def getTcpIpNdpSlaacDelayEnabled(self) -> Optional[Boolean]:
        """If enabled transmission of the first DAD Neighbor Solicitation will be delayed by a random value from [0...MAX_DAD_DELAY]."""
        return self.tcpIpNdpSlaacDelayEnabled

    def setTcpIpNdpSlaacDelayEnabled(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        If enabled transmission of the first DAD Neighbor Solicitation will be delayed by a random value from [0...MAX_DAD_DELAY].

        A None value is a no-op and does not overwrite an existing tcpIpNdpSlaacDelayEnabled.
        """
        if value is not None:
            self.tcpIpNdpSlaacDelayEnabled = value
        return self

    def getTcpIpNdpSlaacOptimisticDadEnabled(self) -> Optional[Boolean]:
        """Enable Optimistic Duplicate Address Detection (DAD) according to RFC4429."""
        return self.tcpIpNdpSlaacOptimisticDadEnabled

    def setTcpIpNdpSlaacOptimisticDadEnabled(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        Enable Optimistic Duplicate Address Detection (DAD) according to RFC4429.

        A None value is a no-op and does not overwrite an existing tcpIpNdpSlaacOptimisticDadEnabled.
        """
        if value is not None:
            self.tcpIpNdpSlaacOptimisticDadEnabled = value
        return self


class Ipv6Props(ARObject):
    """This meta-class specifies the configuration options for IPv6."""

    # Ipv6Props method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.105, p.148
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDhcpProps          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDhcpProps          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFragmentationProps [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFragmentationProps [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNdpProps           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNdpProps           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    #
    # The FRAGMENTATION-PROPS child fully round-trips via the readIpv6FragmentationProps/
    # writeIpv6FragmentationProps level since the Ipv6FragmentationProps sync (Table 3.106),
    # the DHCP-PROPS child via the readDhcpv6Props/writeDhcpv6Props level since the
    # Dhcpv6Props sync (Table 3.107) and the NDP-PROPS child via the
    # readIpv6NdpProps/writeIpv6NdpProps level since the Ipv6NdpProps sync (Table 3.108).

    def __init__(self):
        super().__init__()

        # Configuration properties for DHCPv6.
        self.dhcpProps: Optional[Dhcpv6Props] = None

        # Configuration properties for IPv6 packet fragmentation/reassembly.
        self.fragmentationProps: Optional[Ipv6FragmentationProps] = None

        # Configuration properties for the Neighbor Discovery Protocol for IPv6.
        self.ndpProps: Optional[Ipv6NdpProps] = None

    def getDhcpProps(self) -> Optional[Dhcpv6Props]:
        """Configuration properties for DHCPv6."""
        return self.dhcpProps

    def setDhcpProps(self, value: Optional[Dhcpv6Props]) -> Ipv6Props:
        """
        Configuration properties for DHCPv6.

        A None value is a no-op and does not overwrite an existing dhcpProps.
        """
        if value is not None:
            self.dhcpProps = value
        return self

    def getFragmentationProps(self) -> Optional[Ipv6FragmentationProps]:
        """Configuration properties for IPv6 packet fragmentation/reassembly."""
        return self.fragmentationProps

    def setFragmentationProps(self, value: Optional[Ipv6FragmentationProps]) -> Ipv6Props:
        """
        Configuration properties for IPv6 packet fragmentation/reassembly.

        A None value is a no-op and does not overwrite an existing fragmentationProps.
        """
        if value is not None:
            self.fragmentationProps = value
        return self

    def getNdpProps(self) -> Optional[Ipv6NdpProps]:
        """Configuration properties for the Neighbor Discovery Protocol for IPv6."""
        return self.ndpProps

    def setNdpProps(self, value: Optional[Ipv6NdpProps]) -> Ipv6Props:
        """
        Configuration properties for the Neighbor Discovery Protocol for IPv6.

        A None value is a no-op and does not overwrite an existing ndpProps.
        """
        if value is not None:
            self.ndpProps = value
        return self


class EthTcpIpProps(ARElement):
    """This meta-class is used to configure the EcuInstance specific TcpIp Stack attributes. Tags: atp.recommendedPackage=EthTcpIpProps"""

    # EthTcpIpProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.109, p.153 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpProps     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpProps     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUdpProps     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUdpProps     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # Aggregated by ARPackage.element (XSD L5284) → ARPackage.createEthTcpIpProps factory.

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # TCP configuration properties
        self.tcpProps: Optional[TcpProps] = None

        # UDP configuration properties
        self.udpProps: Optional[UdpProps] = None

    def getTcpProps(self) -> Optional[TcpProps]:
        """TCP configuration properties"""
        return self.tcpProps

    def setTcpProps(self, value: Optional[TcpProps]) -> EthTcpIpProps:
        """TCP configuration properties
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpProps = value
        return self

    def getUdpProps(self) -> Optional[UdpProps]:
        """UDP configuration properties"""
        return self.udpProps

    def setUdpProps(self, value: Optional[UdpProps]) -> EthTcpIpProps:
        """UDP configuration properties
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.udpProps = value
        return self


class UdpProps(ARObject):
    """This meta-class specifies the configuration options for UDP (User Datagram Protocol).

    [constr_5118] Value range of UdpProps.udpTtl: If defined, the value of UdpProps.udpTtl shall be in the range of 1..255.
    """

    # UdpProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.110, p.154 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getUdpTtl     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUdpTtl     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Default Time-to-live value of outgoing UDP packets.
        self.udpTtl: Optional[PositiveInteger] = None

    def getUdpTtl(self) -> Optional[PositiveInteger]:
        """Default Time-to-live value of outgoing UDP packets."""
        return self.udpTtl

    def setUdpTtl(self, value: Optional[PositiveInteger]) -> UdpProps:
        """Default Time-to-live value of outgoing UDP packets.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.udpTtl = value
        return self


class TcpProps(ARObject):
    """This meta-class specifies the configuration options for TCP (Transmission Control Protocol).

    [constr_5119] Value range of TcpProps.tcpTtl: If defined, the value of TcpProps.tcpTtl shall be in the range of 1..255.

    [constr_5120] Value range of TcpProps.tcpDelayedAckTimeout: If defined, the value of TcpProps.tcpDelayedAckTimeout shall be in the range of 0..0.5.

    [constr_5121] Value range of TcpProps.tcpSynMaxRtx: If defined, the value of TcpProps.tcpSynMaxRtx shall be in the range of 0..255.

    [constr_5122] Value range of TcpProps.tcpMaxRtx: If defined, the value of TcpProps.tcpMaxRtx shall be in the range of 0..255.

    [constr_5123] Value range of TcpProps.tcpKeepAliveProbesMax: If defined, the value of TcpProps.tcpKeepAliveProbesMax shall be in the range of 0..65535.

    [constr_5124] Value range of TcpProps.tcpReceiveWindowMax: If defined, the value of TcpProps.tcpReceiveWindowMax shall be in the range of 0..65535.
    """

    # TcpProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.111, p.155 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpCongestionAvoidanceEnabled     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpCongestionAvoidanceEnabled     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpDelayedAckTimeout              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpDelayedAckTimeout              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpFastRecoveryEnabled            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpFastRecoveryEnabled            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpFastRetransmitEnabled          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpFastRetransmitEnabled          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpFinWait2Timeout                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpFinWait2Timeout                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpKeepAliveEnabled               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpKeepAliveEnabled               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpKeepAliveInterval              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpKeepAliveInterval              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpKeepAliveProbesMax             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpKeepAliveProbesMax             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpKeepAliveTime                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpKeepAliveTime                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpMaxRtx                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpMaxRtx                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpMsl                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpMsl                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpNagleEnabled                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpNagleEnabled                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpReceiveWindowMax               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpReceiveWindowMax               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpRetransmissionTimeout          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpRetransmissionTimeout          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpSlowStartEnabled               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpSlowStartEnabled               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpSynMaxRtx                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpSynMaxRtx                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpSynReceivedTimeout             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpSynReceivedTimeout             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpTtl                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpTtl                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Enables (TRUE) or disables (FALSE) support of TCP congestion avoidance algorithm according to IETF RFC 5681.
        self.tcpCongestionAvoidanceEnabled: Optional[Boolean] = None

        # The maximal time an acknowledgement is delayed for transmission in seconds.
        self.tcpDelayedAckTimeout: Optional[TimeValue] = None

        # Enables (TRUE) or disables (FALSE) support of TCP Fast Recovery according to IETF RFC 5681.
        self.tcpFastRecoveryEnabled: Optional[Boolean] = None

        # Enables (TRUE) or disables (FALSE) support of TCP Fast Retransmission according to IETF RFC 5681.
        self.tcpFastRetransmitEnabled: Optional[Boolean] = None

        # Timeout in [s] to receive a FIN from the remote node (after this node has initiated connection termination), i.e. maximum time waiting in FINWAIT-2 for a connection termination request from the remote TCP.
        self.tcpFinWait2Timeout: Optional[TimeValue] = None

        # Enables (TRUE) or disables (FALSE) TCP Keep Alive Probes according to IETF RFC 1122 chapter 4.2.3.6.
        self.tcpKeepAliveEnabled: Optional[Boolean] = None

        # Specifies the interval in seconds between subsequent keepalive probes.
        self.tcpKeepAliveInterval: Optional[TimeValue] = None

        # Maximum number of times that a TCP Keep Alive is retransmitted before the connection is closed.
        self.tcpKeepAliveProbesMax: Optional[PositiveInteger] = None

        # Specifies the time in [s] between the last data packet sent (simple ACKs are not considered data) and the first keepalive probe.
        self.tcpKeepAliveTime: Optional[TimeValue] = None

        # Maximum number of times that a TCP segment is retransmitted before the TCP connection is closed. This parameter is only valid if tcpRetransmissionTimeout is configured. Note: This parameter also applies for FIN retransmissions.
        self.tcpMaxRtx: Optional[PositiveInteger] = None

        # Maximum segment lifetime in [s].
        self.tcpMsl: Optional[TimeValue] = None

        # Enables (TRUE) or disables (FALSE) support of Nagle's algorithm according to IETF RFC 1122 (chapter 4.2.3.4 When to Send Data). If enabled the Nagle's algorithm is activated per default for all TCP sockets, but can be deactivated per Socket (with the attribute TcpTp.nagleAlgorithm).
        self.tcpNagleEnabled: Optional[Boolean] = None

        # Default value of maximum receive window in bytes.
        self.tcpReceiveWindowMax: Optional[PositiveInteger] = None

        # Timeout in [s] before an unacknowledged TCP segment is sent again. If the timeout is disabled, no TCP segments shall be retransmitted.
        self.tcpRetransmissionTimeout: Optional[TimeValue] = None

        # Enables (TRUE) or disables (FALSE) support of TCP slow start algorithm according to IETF RFC 5681.
        self.tcpSlowStartEnabled: Optional[Boolean] = None

        # Maximum number of times that a TCP SYN is retransmitted.
        self.tcpSynMaxRtx: Optional[PositiveInteger] = None

        # Timeout in [s] to complete a remotely initiated TCP connection establishment, i.e. maximum time waiting in SYN-RECEIVED for a confirming connection request acknowledgement after having both received and sent a connection request.
        self.tcpSynReceivedTimeout: Optional[TimeValue] = None

        # Default Time-to-live value of outgoing TCP packets.
        self.tcpTtl: Optional[PositiveInteger] = None

    def getTcpCongestionAvoidanceEnabled(self) -> Optional[Boolean]:
        """Enables (TRUE) or disables (FALSE) support of TCP congestion avoidance algorithm according to IETF RFC 5681."""
        return self.tcpCongestionAvoidanceEnabled

    def setTcpCongestionAvoidanceEnabled(self, value: Optional[Boolean]) -> TcpProps:
        """Enables (TRUE) or disables (FALSE) support of TCP congestion avoidance algorithm according to IETF RFC 5681.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpCongestionAvoidanceEnabled = value
        return self

    def getTcpDelayedAckTimeout(self) -> Optional[TimeValue]:
        """The maximal time an acknowledgement is delayed for transmission in seconds."""
        return self.tcpDelayedAckTimeout

    def setTcpDelayedAckTimeout(self, value: Optional[TimeValue]) -> TcpProps:
        """The maximal time an acknowledgement is delayed for transmission in seconds.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpDelayedAckTimeout = value
        return self

    def getTcpFastRecoveryEnabled(self) -> Optional[Boolean]:
        """Enables (TRUE) or disables (FALSE) support of TCP Fast Recovery according to IETF RFC 5681."""
        return self.tcpFastRecoveryEnabled

    def setTcpFastRecoveryEnabled(self, value: Optional[Boolean]) -> TcpProps:
        """Enables (TRUE) or disables (FALSE) support of TCP Fast Recovery according to IETF RFC 5681.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpFastRecoveryEnabled = value
        return self

    def getTcpFastRetransmitEnabled(self) -> Optional[Boolean]:
        """Enables (TRUE) or disables (FALSE) support of TCP Fast Retransmission according to IETF RFC 5681."""
        return self.tcpFastRetransmitEnabled

    def setTcpFastRetransmitEnabled(self, value: Optional[Boolean]) -> TcpProps:
        """Enables (TRUE) or disables (FALSE) support of TCP Fast Retransmission according to IETF RFC 5681.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpFastRetransmitEnabled = value
        return self

    def getTcpFinWait2Timeout(self) -> Optional[TimeValue]:
        """Timeout in [s] to receive a FIN from the remote node (after this node has initiated connection termination), i.e. maximum time waiting in FINWAIT-2 for a connection termination request from the remote TCP."""
        return self.tcpFinWait2Timeout

    def setTcpFinWait2Timeout(self, value: Optional[TimeValue]) -> TcpProps:
        """Timeout in [s] to receive a FIN from the remote node (after this node has initiated connection termination), i.e. maximum time waiting in FINWAIT-2 for a connection termination request from the remote TCP.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpFinWait2Timeout = value
        return self

    def getTcpKeepAliveEnabled(self) -> Optional[Boolean]:
        """Enables (TRUE) or disables (FALSE) TCP Keep Alive Probes according to IETF RFC 1122 chapter 4.2.3.6."""
        return self.tcpKeepAliveEnabled

    def setTcpKeepAliveEnabled(self, value: Optional[Boolean]) -> TcpProps:
        """Enables (TRUE) or disables (FALSE) TCP Keep Alive Probes according to IETF RFC 1122 chapter 4.2.3.6.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpKeepAliveEnabled = value
        return self

    def getTcpKeepAliveInterval(self) -> Optional[TimeValue]:
        """Specifies the interval in seconds between subsequent keepalive probes."""
        return self.tcpKeepAliveInterval

    def setTcpKeepAliveInterval(self, value: Optional[TimeValue]) -> TcpProps:
        """Specifies the interval in seconds between subsequent keepalive probes.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpKeepAliveInterval = value
        return self

    def getTcpKeepAliveProbesMax(self) -> Optional[PositiveInteger]:
        """Maximum number of times that a TCP Keep Alive is retransmitted before the connection is closed."""
        return self.tcpKeepAliveProbesMax

    def setTcpKeepAliveProbesMax(self, value: Optional[PositiveInteger]) -> TcpProps:
        """Maximum number of times that a TCP Keep Alive is retransmitted before the connection is closed.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpKeepAliveProbesMax = value
        return self

    def getTcpKeepAliveTime(self) -> Optional[TimeValue]:
        """Specifies the time in [s] between the last data packet sent (simple ACKs are not considered data) and the first keepalive probe."""
        return self.tcpKeepAliveTime

    def setTcpKeepAliveTime(self, value: Optional[TimeValue]) -> TcpProps:
        """Specifies the time in [s] between the last data packet sent (simple ACKs are not considered data) and the first keepalive probe.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpKeepAliveTime = value
        return self

    def getTcpMaxRtx(self) -> Optional[PositiveInteger]:
        """Maximum number of times that a TCP segment is retransmitted before the TCP connection is closed. This parameter is only valid if tcpRetransmissionTimeout is configured. Note: This parameter also applies for FIN retransmissions."""
        return self.tcpMaxRtx

    def setTcpMaxRtx(self, value: Optional[PositiveInteger]) -> TcpProps:
        """Maximum number of times that a TCP segment is retransmitted before the TCP connection is closed. This parameter is only valid if tcpRetransmissionTimeout is configured. Note: This parameter also applies for FIN retransmissions.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpMaxRtx = value
        return self

    def getTcpMsl(self) -> Optional[TimeValue]:
        """Maximum segment lifetime in [s]."""
        return self.tcpMsl

    def setTcpMsl(self, value: Optional[TimeValue]) -> TcpProps:
        """Maximum segment lifetime in [s].
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpMsl = value
        return self

    def getTcpNagleEnabled(self) -> Optional[Boolean]:
        """Enables (TRUE) or disables (FALSE) support of Nagle's algorithm according to IETF RFC 1122 (chapter 4.2.3.4 When to Send Data). If enabled the Nagle's algorithm is activated per default for all TCP sockets, but can be deactivated per Socket (with the attribute TcpTp.nagleAlgorithm)."""
        return self.tcpNagleEnabled

    def setTcpNagleEnabled(self, value: Optional[Boolean]) -> TcpProps:
        """Enables (TRUE) or disables (FALSE) support of Nagle's algorithm according to IETF RFC 1122 (chapter 4.2.3.4 When to Send Data). If enabled the Nagle's algorithm is activated per default for all TCP sockets, but can be deactivated per Socket (with the attribute TcpTp.nagleAlgorithm).
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpNagleEnabled = value
        return self

    def getTcpReceiveWindowMax(self) -> Optional[PositiveInteger]:
        """Default value of maximum receive window in bytes."""
        return self.tcpReceiveWindowMax

    def setTcpReceiveWindowMax(self, value: Optional[PositiveInteger]) -> TcpProps:
        """Default value of maximum receive window in bytes.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpReceiveWindowMax = value
        return self

    def getTcpRetransmissionTimeout(self) -> Optional[TimeValue]:
        """Timeout in [s] before an unacknowledged TCP segment is sent again. If the timeout is disabled, no TCP segments shall be retransmitted."""
        return self.tcpRetransmissionTimeout

    def setTcpRetransmissionTimeout(self, value: Optional[TimeValue]) -> TcpProps:
        """Timeout in [s] before an unacknowledged TCP segment is sent again. If the timeout is disabled, no TCP segments shall be retransmitted.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpRetransmissionTimeout = value
        return self

    def getTcpSlowStartEnabled(self) -> Optional[Boolean]:
        """Enables (TRUE) or disables (FALSE) support of TCP slow start algorithm according to IETF RFC 5681."""
        return self.tcpSlowStartEnabled

    def setTcpSlowStartEnabled(self, value: Optional[Boolean]) -> TcpProps:
        """Enables (TRUE) or disables (FALSE) support of TCP slow start algorithm according to IETF RFC 5681.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpSlowStartEnabled = value
        return self

    def getTcpSynMaxRtx(self) -> Optional[PositiveInteger]:
        """Maximum number of times that a TCP SYN is retransmitted."""
        return self.tcpSynMaxRtx

    def setTcpSynMaxRtx(self, value: Optional[PositiveInteger]) -> TcpProps:
        """Maximum number of times that a TCP SYN is retransmitted.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpSynMaxRtx = value
        return self

    def getTcpSynReceivedTimeout(self) -> Optional[TimeValue]:
        """Timeout in [s] to complete a remotely initiated TCP connection establishment, i.e. maximum time waiting in SYN-RECEIVED for a confirming connection request acknowledgement after having both received and sent a connection request."""
        return self.tcpSynReceivedTimeout

    def setTcpSynReceivedTimeout(self, value: Optional[TimeValue]) -> TcpProps:
        """Timeout in [s] to complete a remotely initiated TCP connection establishment, i.e. maximum time waiting in SYN-RECEIVED for a confirming connection request acknowledgement after having both received and sent a connection request.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpSynReceivedTimeout = value
        return self

    def getTcpTtl(self) -> Optional[PositiveInteger]:
        """Default Time-to-live value of outgoing TCP packets."""
        return self.tcpTtl

    def setTcpTtl(self, value: Optional[PositiveInteger]) -> TcpProps:
        """Default Time-to-live value of outgoing TCP packets.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpTtl = value
        return self


class TcpIpIcmpv4Props(ARObject):
    """This meta-class specifies the configuration options for ICMPv4 (Internet Control Message Protocol).

    [constr_5125] Value range of TcpIpIcmpv4Props.tcpIpIcmpV4Ttl: If defined, the value of TcpIpIcmpv4Props.tcpIpIcmpV4Ttl shall be in the range of 1..255.
    """

    # TcpIpIcmpv4Props method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.113, p.156 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpIpIcmpV4EchoReplyEnabled [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIcmpV4EchoReplyEnabled [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIcmpV4Ttl              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIcmpV4Ttl              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute enables or disables transmission of ICMP echo reply message in case of a ICMP echo reception.
        self.tcpIpIcmpV4EchoReplyEnabled: Optional[Boolean] = None

        # This attribute is only relevant in case that ICMP (Internet Control Message Protocol) is used. It specifies the default Time-to-live value of outgoing ICMP packets.
        self.tcpIpIcmpV4Ttl: Optional[PositiveInteger] = None

    def getTcpIpIcmpV4EchoReplyEnabled(self) -> Optional[Boolean]:
        """This attribute enables or disables transmission of ICMP echo reply message in case of a ICMP echo reception."""
        return self.tcpIpIcmpV4EchoReplyEnabled

    def setTcpIpIcmpV4EchoReplyEnabled(self, value: Optional[Boolean]) -> TcpIpIcmpv4Props:
        """This attribute enables or disables transmission of ICMP echo reply message in case of a ICMP echo reception.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpIpIcmpV4EchoReplyEnabled = value
        return self

    def getTcpIpIcmpV4Ttl(self) -> Optional[PositiveInteger]:
        """This attribute is only relevant in case that ICMP (Internet Control Message Protocol) is used. It specifies the default Time-to-live value of outgoing ICMP packets."""
        return self.tcpIpIcmpV4Ttl

    def setTcpIpIcmpV4Ttl(self, value: Optional[PositiveInteger]) -> TcpIpIcmpv4Props:
        """This attribute is only relevant in case that ICMP (Internet Control Message Protocol) is used. It specifies the default Time-to-live value of outgoing ICMP packets.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpIpIcmpV4Ttl = value
        return self


class TcpIpIcmpv6Props(ARObject):
    """This meta-class specifies the configuration options for ICMPv6 (Internet Control Message Protocol).

    [constr_5154] Value range of TcpIpIcmpv6Props.tcpIpIcmpV6HopLimit: If defined, the value of TcpIpIcmpv6Props.tcpIpIcmpV6HopLimit shall be in the range of 1..255.
    """

    # TcpIpIcmpv6Props method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.114, p.157 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTcpIpIcmpV6EchoReplyAvoidFragmentation      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIcmpV6EchoReplyAvoidFragmentation      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIcmpV6EchoReplyEnabled                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIcmpV6EchoReplyEnabled                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIcmpV6HopLimit                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIcmpV6HopLimit                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIcmpV6MsgDestinationUnreachableEnabled [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIcmpV6MsgDestinationUnreachableEnabled [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpIpIcmpV6MsgParameterProblemEnabled       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTcpIpIcmpV6MsgParameterProblemEnabled       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute defines whether the echo reply is only transmitted in case that the incoming ICMPv6 Echo Request (Pings) fits the MTU of the respective interface, i.e. can be transmitted without IPv6 fragmentation.
        self.tcpIpIcmpV6EchoReplyAvoidFragmentation: Optional[Boolean] = None

        # This attribute enables or disables transmission of ICMP echo reply message in case of a ICMP echo reception.
        self.tcpIpIcmpV6EchoReplyEnabled: Optional[Boolean] = None

        # Default Hop-Limit value of outgoing ICMPv6 packets.
        self.tcpIpIcmpV6HopLimit: Optional[PositiveInteger] = None

        # This attribute Enables/Disables the transmission of Destination Unreachable Messages.
        self.tcpIpIcmpV6MsgDestinationUnreachableEnabled: Optional[Boolean] = None

        # If enabled an ICMPv6 parameter problem message will be sent if a received packet has been dropped due to unknown options or headers that are found in the packet.
        self.tcpIpIcmpV6MsgParameterProblemEnabled: Optional[Boolean] = None

    def getTcpIpIcmpV6EchoReplyAvoidFragmentation(self) -> Optional[Boolean]:
        """This attribute defines whether the echo reply is only transmitted in case that the incoming ICMPv6 Echo Request (Pings) fits the MTU of the respective interface, i.e. can be transmitted without IPv6 fragmentation."""
        return self.tcpIpIcmpV6EchoReplyAvoidFragmentation

    def setTcpIpIcmpV6EchoReplyAvoidFragmentation(self, value: Optional[Boolean]) -> TcpIpIcmpv6Props:
        """This attribute defines whether the echo reply is only transmitted in case that the incoming ICMPv6 Echo Request (Pings) fits the MTU of the respective interface, i.e. can be transmitted without IPv6 fragmentation.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpIpIcmpV6EchoReplyAvoidFragmentation = value
        return self

    def getTcpIpIcmpV6EchoReplyEnabled(self) -> Optional[Boolean]:
        """This attribute enables or disables transmission of ICMP echo reply message in case of a ICMP echo reception."""
        return self.tcpIpIcmpV6EchoReplyEnabled

    def setTcpIpIcmpV6EchoReplyEnabled(self, value: Optional[Boolean]) -> TcpIpIcmpv6Props:
        """This attribute enables or disables transmission of ICMP echo reply message in case of a ICMP echo reception.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpIpIcmpV6EchoReplyEnabled = value
        return self

    def getTcpIpIcmpV6HopLimit(self) -> Optional[PositiveInteger]:
        """Default Hop-Limit value of outgoing ICMPv6 packets."""
        return self.tcpIpIcmpV6HopLimit

    def setTcpIpIcmpV6HopLimit(self, value: Optional[PositiveInteger]) -> TcpIpIcmpv6Props:
        """Default Hop-Limit value of outgoing ICMPv6 packets.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpIpIcmpV6HopLimit = value
        return self

    def getTcpIpIcmpV6MsgDestinationUnreachableEnabled(self) -> Optional[Boolean]:
        """This attribute Enables/Disables the transmission of Destination Unreachable Messages."""
        return self.tcpIpIcmpV6MsgDestinationUnreachableEnabled

    def setTcpIpIcmpV6MsgDestinationUnreachableEnabled(self, value: Optional[Boolean]) -> TcpIpIcmpv6Props:
        """This attribute Enables/Disables the transmission of Destination Unreachable Messages.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpIpIcmpV6MsgDestinationUnreachableEnabled = value
        return self

    def getTcpIpIcmpV6MsgParameterProblemEnabled(self) -> Optional[Boolean]:
        """If enabled an ICMPv6 parameter problem message will be sent if a received packet has been dropped due to unknown options or headers that are found in the packet."""
        return self.tcpIpIcmpV6MsgParameterProblemEnabled

    def setTcpIpIcmpV6MsgParameterProblemEnabled(self, value: Optional[Boolean]) -> TcpIpIcmpv6Props:
        """If enabled an ICMPv6 parameter problem message will be sent if a received packet has been dropped due to unknown options or headers that are found in the packet.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.tcpIpIcmpV6MsgParameterProblemEnabled = value
        return self


class EthTcpIpIcmpProps(ARElement):
    """This meta-class is used to configure the EcuInstance specific ICMP (Internet Control Message Protocol) attributes Tags: atp.recommendedPackage=EthTcpIcmpProps"""

    # EthTcpIpIcmpProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.112, p.156 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIcmpV4Props  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIcmpV4Props  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIcmpV6Props  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIcmpV6Props  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # Aggregated by ARPackage.element (XSD L5283) → ARPackage.createEthTcpIpIcmpProps factory.

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # ICMPv4 configuration properties
        self.icmpV4Props: Optional[TcpIpIcmpv4Props] = None

        # ICMPv6 configuration properties
        self.icmpV6Props: Optional[TcpIpIcmpv6Props] = None

    def getIcmpV4Props(self) -> Optional[TcpIpIcmpv4Props]:
        """ICMPv4 configuration properties"""
        return self.icmpV4Props

    def setIcmpV4Props(self, value: Optional[TcpIpIcmpv4Props]) -> EthTcpIpIcmpProps:
        """ICMPv4 configuration properties
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.icmpV4Props = value
        return self

    def getIcmpV6Props(self) -> Optional[TcpIpIcmpv6Props]:
        """ICMPv6 configuration properties"""
        return self.icmpV6Props

    def setIcmpV6Props(self, value: Optional[TcpIpIcmpv6Props]) -> EthTcpIpIcmpProps:
        """ICMPv6 configuration properties
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.icmpV6Props = value
        return self


class HttpTp(TransportProtocolConfiguration):
    pass


class Ieee1722Tp(TransportProtocolConfiguration):
    pass


class MacMulticastConfiguration(NetworkEndpointAddress):
    pass


class RtpTp(TransportProtocolConfiguration):
    pass


# Runtime import breaking the EthernetTopology <-> ServiceInstances cycle: InitialSdDelayConfig and RequestResponseDelay
# are referenced by annotations in this module and must resolve in its runtime globals for typing.get_type_hints
# (Rule 0003). ServiceInstances defines both before its own import of this module (Rule 0005).
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import InitialSdDelayConfig, RequestResponseDelay  # noqa: E402
