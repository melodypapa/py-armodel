from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement

__all__ = [
    "FirewallRule",
    "FirewallRuleProps",
    "StateDependentFirewall",
    "DataLinkLayerRule",
    "DdsRule",
    "DoIpRule",
    "NetworkLayerRule",
    "PayloadBytePatternRule",
    "SomeipProtocolRule",
    "SomeipSdRule",
    "TransportLayerRule",
]


class FirewallRule(ARElement):
    """Firewall Rule that defines the control information in individual packets."""

    # FirewallRule method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.236, p.585 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (markdown-minimal deviation: the 8 rule member classes carry no Class table in the
    #  PDF/markdown corpus — DataLinkLayerRule/DdsRule synced markdown-minimal, the other
    #  6 are attribute-name placeholders; full member attribute defs remain a deviation)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getBucketSize                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBucketSize                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataLinkLayerRule         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataLinkLayerRule         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsRule                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsRule                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDoIpRule                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDoIpRule                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNetworkLayerRule          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNetworkLayerRule          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addPayloadBytePatternRule    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPayloadBytePatternRules   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRefillAmount              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRefillAmount              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSomeipRule                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSomeipRule                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSomeipSdRule              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSomeipSdRule              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTransportLayerRule        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTransportLayerRule        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)
        self.bucketSize: Optional[PositiveInteger] = None
        self.dataLinkLayerRule: Optional["DataLinkLayerRule"] = None
        self.ddsRule: Optional["DdsRule"] = None
        self.doIpRule: Optional["DoIpRule"] = None
        self.networkLayerRule: Optional["NetworkLayerRule"] = None
        self.payloadBytePatternRules: List["PayloadBytePatternRule"] = []
        self.refillAmount: Optional[PositiveInteger] = None
        self.someipRule: Optional["SomeipProtocolRule"] = None
        self.someipSdRule: Optional["SomeipSdRule"] = None
        self.transportLayerRule: Optional["TransportLayerRule"] = None

    def getBucketSize(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the capacity of the queue for rate limitation (leaky-bucket Algorithm).
        """
        return self.bucketSize

    def setBucketSize(self, value: Optional[PositiveInteger]):
        """
        Sets the bucketSize value.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bucketSize = value
        return self

    def getDataLinkLayerRule(self) -> Optional["DataLinkLayerRule"]:
        """
        Configuration of rules on the Data Link Layer
        """
        return self.dataLinkLayerRule

    def setDataLinkLayerRule(self, value: Optional["DataLinkLayerRule"]):
        """
        Sets the dataLinkLayerRule aggregation.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataLinkLayerRule = value
        return self

    def getDdsRule(self) -> Optional["DdsRule"]:
        """
        Configuration of firewall rules for DDS.
        """
        return self.ddsRule

    def setDdsRule(self, value: Optional["DdsRule"]):
        """
        Sets the ddsRule aggregation.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ddsRule = value
        return self

    def getDoIpRule(self) -> Optional["DoIpRule"]:
        """
        Configuration of firewall rules for DoIP messages
        """
        return self.doIpRule

    def setDoIpRule(self, value: Optional["DoIpRule"]):
        """
        Sets the doIpRule aggregation.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.doIpRule = value
        return self

    def getNetworkLayerRule(self) -> Optional["NetworkLayerRule"]:
        """
        Configuration of rules on the Network Layer
        """
        return self.networkLayerRule

    def setNetworkLayerRule(self, value: Optional["NetworkLayerRule"]):
        """
        Sets the networkLayerRule aggregation.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.networkLayerRule = value
        return self

    def addPayloadBytePatternRule(self, value: "PayloadBytePatternRule"):
        """
        Configuration of generic firewall rules

        Returns:
            self for method chaining
        """
        self.payloadBytePatternRules.append(value)
        return self

    def getPayloadBytePatternRules(self) -> List["PayloadBytePatternRule"]:
        """
        Configuration of generic firewall rules
        """
        return self.payloadBytePatternRules

    def getRefillAmount(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the output rate that describes how many packets leave the queue per second (leaky-bucket Algorithm).
        """
        return self.refillAmount

    def setRefillAmount(self, value: Optional[PositiveInteger]):
        """
        Sets the refillAmount value.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.refillAmount = value
        return self

    def getSomeipRule(self) -> Optional["SomeipProtocolRule"]:
        """
        Configuration of firewall rules for SOME/IP messages
        """
        return self.someipRule

    def setSomeipRule(self, value: Optional["SomeipProtocolRule"]):
        """
        Sets the someipRule aggregation.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.someipRule = value
        return self

    def getSomeipSdRule(self) -> Optional["SomeipSdRule"]:
        """
        Configuration of firewall rules for SOME/IP Service Discovery messages
        """
        return self.someipSdRule

    def setSomeipSdRule(self, value: Optional["SomeipSdRule"]):
        """
        Sets the someipSdRule aggregation.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.someipSdRule = value
        return self

    def getTransportLayerRule(self) -> Optional["TransportLayerRule"]:
        """
        Configuration of rules on the Transport Layer
        """
        return self.transportLayerRule

    def setTransportLayerRule(self, value: Optional["TransportLayerRule"]):
        """
        Sets the transportLayerRule aggregation.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.transportLayerRule = value
        return self


class DoIpRule(ARObject):
    """Configuration of firewall rules for DoIP messages"""

    # DoIpRule method parity checklist:
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (markdown-minimal placeholder: member attribute defs skipped per user decision
    #  2026-08-31 — no Class table in the PDF/markdown corpus; no stamp)
    # [ ] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class NetworkLayerRule(ARObject):
    """Configuration of rules on the Network Layer"""

    # NetworkLayerRule method parity checklist:
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (markdown-minimal placeholder: member attribute defs skipped per user decision
    #  2026-08-31 — no Class table in the PDF/markdown corpus; no stamp)
    # [ ] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class PayloadBytePatternRule(ARObject):
    """Configuration of generic firewall rules"""

    # PayloadBytePatternRule method parity checklist:
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (markdown-minimal placeholder: member attribute defs skipped per user decision
    #  2026-08-31 — no Class table in the PDF/markdown corpus; no stamp)
    # [ ] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class SomeipProtocolRule(ARObject):
    """Configuration of firewall rules for SOME/IP messages"""

    # SomeipProtocolRule method parity checklist:
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (markdown-minimal placeholder: member attribute defs skipped per user decision
    #  2026-08-31 — no Class table in the PDF/markdown corpus; no stamp)
    # [ ] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class SomeipSdRule(ARObject):
    """Configuration of firewall rules for SOME/IP Service Discovery messages"""

    # SomeipSdRule method parity checklist:
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (markdown-minimal placeholder: member attribute defs skipped per user decision
    #  2026-08-31 — no Class table in the PDF/markdown corpus; no stamp)
    # [ ] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class TransportLayerRule(ARObject):
    """Configuration of rules on the Transport Layer"""

    # TransportLayerRule method parity checklist:
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (markdown-minimal placeholder: member attribute defs skipped per user decision
    #  2026-08-31 — no Class table in the PDF/markdown corpus; no stamp)
    # [ ] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class DataLinkLayerRule(ARObject):
    """
    Data link layer filter rule of a FirewallRule.

    Members are modeled from the R23-11 SystemTemplate markdown
    BSW-parameter-mapping section (attribute names + Notes only);
    attribute types and cardinality are not specified by the markdown
    and are recorded as deviations (markdown-minimal sync).
    """

    # DataLinkLayerRule method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getEtherType                 [x] impl  [x] docstring  [ ] test
    # [ ] setEtherType                 [x] impl  [x] docstring  [ ] test
    # [ ] getDestinationMacAddress     [x] impl  [x] docstring  [ ] test
    # [ ] setDestinationMacAddress     [x] impl  [x] docstring  [ ] test
    # [ ] getDestinationMacAddressMask [x] impl  [x] docstring  [ ] test
    # [ ] setDestinationMacAddressMask [x] impl  [x] docstring  [ ] test
    # [ ] getSourceMacAddress          [x] impl  [x] docstring  [ ] test
    # [ ] setSourceMacAddress          [x] impl  [x] docstring  [ ] test
    # [ ] getSourceMacAddressMask      [x] impl  [x] docstring  [ ] test
    # [ ] setSourceMacAddressMask      [x] impl  [x] docstring  [ ] test
    # [ ] getVlanId                    [x] impl  [x] docstring  [ ] test
    # [ ] setVlanId                    [x] impl  [x] docstring  [ ] test
    # [ ] getVlanPriority              [x] impl  [x] docstring  [ ] test
    # [ ] setVlanPriority              [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the DataLinkLayerRule with default (None) values.
        """
        super().__init__()
        self.etherType: Optional[str] = None
        self.destinationMacAddress: Optional[str] = None
        self.destinationMacAddressMask: Optional[str] = None
        self.sourceMacAddress: Optional[str] = None
        self.sourceMacAddressMask: Optional[str] = None
        self.vlanId: Optional[str] = None
        self.vlanPriority: Optional[str] = None

    def getEtherType(self) -> Optional[str]:
        """
        Filter to match packets based on the EtherType field in the Ethernet frame. The EtherType is used to indicate which protocol is encapsulated in the payload of the frame.
        """
        return self.etherType

    def setEtherType(self, value: Optional[str]):
        """
        Sets the EtherType filter value.

        Returns:
            self for method chaining
        """
        self.etherType = value
        return self

    def getDestinationMacAddress(self) -> Optional[str]:
        """
        Filter to match packets with the destination MAC address.
        """
        return self.destinationMacAddress

    def setDestinationMacAddress(self, value: Optional[str]):
        """
        Sets the destination MAC address filter value.

        Returns:
            self for method chaining
        """
        self.destinationMacAddress = value
        return self

    def getDestinationMacAddressMask(self) -> Optional[str]:
        """
        Filter to match packets with the destination MAC address range. The destinationMacAddress with the destinationMacAddress Mask defines the MAC address range.
        """
        return self.destinationMacAddressMask

    def setDestinationMacAddressMask(self, value: Optional[str]):
        """
        Sets the destination MAC address mask filter value.

        Returns:
            self for method chaining
        """
        self.destinationMacAddressMask = value
        return self

    def getSourceMacAddress(self) -> Optional[str]:
        """
        Filter to match packets with the source MAC address.
        """
        return self.sourceMacAddress

    def setSourceMacAddress(self, value: Optional[str]):
        """
        Sets the source MAC address filter value.

        Returns:
            self for method chaining
        """
        self.sourceMacAddress = value
        return self

    def getSourceMacAddressMask(self) -> Optional[str]:
        """
        Filter to match packets with the source MAC address range. The sourceMacAddress with the sourceMacAddressMask defines the MAC address range.
        """
        return self.sourceMacAddressMask

    def setSourceMacAddressMask(self, value: Optional[str]):
        """
        Sets the source MAC address mask filter value.

        Returns:
            self for method chaining
        """
        self.sourceMacAddressMask = value
        return self

    def getVlanId(self) -> Optional[str]:
        """
        Filter of packets with a specific VlanId.
        """
        return self.vlanId

    def setVlanId(self, value: Optional[str]):
        """
        Sets the VLAN ID filter value.

        Returns:
            self for method chaining
        """
        self.vlanId = value
        return self

    def getVlanPriority(self) -> Optional[str]:
        """
        Filter of packets with a specific Vlan priority.
        """
        return self.vlanPriority

    def setVlanPriority(self, value: Optional[str]):
        """
        Sets the VLAN priority filter value.

        Returns:
            self for method chaining
        """
        self.vlanPriority = value
        return self


class DdsRule(ARObject):
    """Configuration of a DDS firewall rule"""

    # DdsRule method parity checklist:
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (markdown-minimal sync: members modeled from the R23-11 SystemTemplate markdown
    #  BSW-parameter-mapping section — attribute names + Notes only; types and
    #  cardinality not specified by the markdown are deviations (Optional[str]);
    #  no `# Spec verified:` / `# XSD verified:` stamp)
    # [ ] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] getAppId                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] setAppId                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] getHostId                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] setHostId                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] getInstanceId                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] setInstanceId                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] getMajorProtocolVersion      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] setMajorProtocolVersion      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] getMinorProtocolVersion      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] setMinorProtocolVersion      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] getProductId                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] setProductId                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] getReaderEntityId            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] setReaderEntityId            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] getSubmessageType            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] setSubmessageType            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] getVendorId                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] setVendorId                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] getWriterEntityId            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [ ] setWriterEntityId            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        """
        Initializes the DdsRule with default (None) values.
        """
        super().__init__()
        self.appId: Optional[str] = None
        self.hostId: Optional[str] = None
        self.instanceId: Optional[str] = None
        self.majorProtocolVersion: Optional[str] = None
        self.minorProtocolVersion: Optional[str] = None
        self.productId: Optional[str] = None
        self.readerEntityId: Optional[str] = None
        self.submessageType: Optional[str] = None
        self.vendorId: Optional[str] = None
        self.writerEntityId: Optional[str] = None

    def getAppId(self) -> Optional[str]:
        """
        Filter for DDSI-RTPS messages in which the appId in the DDSI-RTPS header and the INFO_DST (0x0E) submessage matches.
        """
        return self.appId

    def setAppId(self, value: Optional[str]):
        """
        Sets the appId filter value.

        Returns:
            self for method chaining
        """
        self.appId = value
        return self

    def getHostId(self) -> Optional[str]:
        """
        Filter for DDSI-RTPS messages in which the hostId in the DDSI-RTPS header and the INFO_DST (0x0E) submessage matches.
        """
        return self.hostId

    def setHostId(self, value: Optional[str]):
        """
        Sets the hostId filter value.

        Returns:
            self for method chaining
        """
        self.hostId = value
        return self

    def getInstanceId(self) -> Optional[str]:
        """
        Filter for DDSI-RTPS messages in which the instanceId in the DDSI-RTPS header and the INFO_DST (0x0E) submessage matches.
        """
        return self.instanceId

    def setInstanceId(self, value: Optional[str]):
        """
        Sets the instanceId filter value.

        Returns:
            self for method chaining
        """
        self.instanceId = value
        return self

    def getMajorProtocolVersion(self) -> Optional[str]:
        """
        Filter for DDSI-RTPS messages in which the majorProtocolVersion in the DDSI-RTPS header matches.
        """
        return self.majorProtocolVersion

    def setMajorProtocolVersion(self, value: Optional[str]):
        """
        Sets the majorProtocolVersion filter value.

        Returns:
            self for method chaining
        """
        self.majorProtocolVersion = value
        return self

    def getMinorProtocolVersion(self) -> Optional[str]:
        """
        Filter for DDSI-RTPS messages in which the minorProtocolVersion in the DDSI-RTPS header matches.
        """
        return self.minorProtocolVersion

    def setMinorProtocolVersion(self, value: Optional[str]):
        """
        Sets the minorProtocolVersion filter value.

        Returns:
            self for method chaining
        """
        self.minorProtocolVersion = value
        return self

    def getProductId(self) -> Optional[str]:
        """
        Filter for DDSI-RTPS messages in which the productId in the DDSI-RTPS header matches.
        """
        return self.productId

    def setProductId(self, value: Optional[str]):
        """
        Sets the productId filter value.

        Returns:
            self for method chaining
        """
        self.productId = value
        return self

    def getReaderEntityId(self) -> Optional[str]:
        """
        Filter for DDSI-RTPS messages in which the readerEntityID in a DDSI-RTPS submessage matches
        """
        return self.readerEntityId

    def setReaderEntityId(self, value: Optional[str]):
        """
        Sets the readerEntityId filter value.

        Returns:
            self for method chaining
        """
        self.readerEntityId = value
        return self

    def getSubmessageType(self) -> Optional[str]:
        """
        Defines the allowed submessage type in the DDSI-RTPS message
        """
        return self.submessageType

    def setSubmessageType(self, value: Optional[str]):
        """
        Sets the submessageType filter value.

        Returns:
            self for method chaining
        """
        self.submessageType = value
        return self

    def getVendorId(self) -> Optional[str]:
        """
        Filter for DDSI-RTPS messages in which the vendorId in the DDSI-RTPS header matches.
        """
        return self.vendorId

    def setVendorId(self, value: Optional[str]):
        """
        Sets the vendorId filter value.

        Returns:
            self for method chaining
        """
        self.vendorId = value
        return self

    def getWriterEntityId(self) -> Optional[str]:
        """
        Filter for DDSI-RTPS messages in which the writerEntityID in a DDSI-RTPS submessage matches
        """
        return self.writerEntityId

    def setWriterEntityId(self, value: Optional[str]):
        """
        Sets the writerEntityId filter value.

        Returns:
            self for method chaining
        """
        self.writerEntityId = value
        return self


class FirewallRuleProps(ARObject):
    """
    Represents firewall rule properties in AUTOSAR Adaptive Platform PlatformModuleDeployment.
    Defines properties for firewall rule configuration.
    """

    # FirewallRuleProps method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getAllowAny                  [x] impl  [x] docstring  [ ] test
    # [ ] setAllowAny                  [x] impl  [x] docstring  [ ] test
    # [ ] getDirection                 [x] impl  [x] docstring  [ ] test
    # [ ] setDirection                 [x] impl  [x] docstring  [ ] test
    # [ ] getProtocol                  [x] impl  [x] docstring  [ ] test
    # [ ] setProtocol                  [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the FirewallRuleProps with default values.
        """
        super().__init__()
        self.allowAny: bool = None
        self.direction: str = None
        self.protocol: str = None

    def getAllowAny(self) -> bool:
        """
        Gets the allowAny flag.

        Returns:
            Boolean value indicating if any traffic is allowed
        """
        return self.allowAny

    def setAllowAny(self, value: bool):
        """
        Sets the allowAny flag.

        Args:
            value: Boolean value to set

        Returns:
            self for method chaining
        """
        self.allowAny = value
        return self

    def getDirection(self) -> str:
        """
        Gets the direction of the firewall rule.

        Returns:
            String representing the direction
        """
        return self.direction

    def setDirection(self, value: str):
        """
        Sets the direction of the firewall rule.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.direction = value
        return self

    def getProtocol(self) -> str:
        """
        Gets the protocol of the firewall rule.

        Returns:
            String representing the protocol
        """
        return self.protocol

    def setProtocol(self, value: str):
        """
        Sets the protocol of the firewall rule.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.protocol = value
        return self


class StateDependentFirewall(ARElement):
    """
    Represents a state-dependent firewall in AUTOSAR Adaptive Platform PlatformModuleDeployment.
    Defines firewall rules that depend on system states.
    """

    # StateDependentFirewall method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] addFirewallRule              [x] impl  [x] docstring  [ ] test
    # [ ] getFirewallRules             [x] impl  [x] docstring  [ ] test
    # [ ] getStateRef                  [x] impl  [x] docstring  [ ] test
    # [ ] setStateRef                  [x] impl  [x] docstring  [ ] test

    def __init__(self, parent, short_name: str):
        """
        Initializes the StateDependentFirewall with a parent and short name.

        Args:
            parent: The parent ARObject that contains this element
            short_name: The short name of this element
        """
        super().__init__(parent, short_name)
        self.firewallRules: List[RefType] = []
        self.stateRef: RefType = None

    def addFirewallRule(self, ref: RefType):
        """
        Adds a firewall rule reference to this state-dependent firewall.

        Args:
            ref: The firewall rule reference to add

        Returns:
            self for method chaining
        """
        self.firewallRules.append(ref)
        return self

    def getFirewallRules(self) -> List[RefType]:
        """
        Gets the list of firewall rule references.

        Returns:
            List of firewall rule references
        """
        return self.firewallRules

    def getStateRef(self) -> RefType:
        """
        Gets the state reference.

        Returns:
            Reference to the state
        """
        return self.stateRef

    def setStateRef(self, value: RefType):
        """
        Sets the state reference.

        Args:
            value: The state reference to set

        Returns:
            self for method chaining
        """
        self.stateRef = value
        return self
