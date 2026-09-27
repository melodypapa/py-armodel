from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, MacAddressString, PositiveInteger, RefType

__all__ = [
    "FirewallActionEnum",
    "FirewallRule",
    "FirewallRuleProps",
    "StateDependentFirewall",
    "DataLinkLayerRule",
    "DdsRule",
    "DoIpRule",
    "NetworkLayerRule",
    "PayloadBytePatternRule",
    "PayloadBytePatternRulePart",
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
    #  PDF/markdown corpus — DataLinkLayerRule/DdsRule synced markdown-minimal,
    #  PayloadBytePatternRule (incl. its PayloadBytePatternRulePart part type) and
    #  SomeipProtocolRule synced XSD-only, the other 4 are attribute-name placeholders;
    #  full member attribute defs remain a deviation)
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
    # [x] addPayloadBytePatternRule    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPayloadBytePatternRules   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
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

        # This attribute defines the capacity of the queue for rate limitation (leaky-bucket Algorithm). Tags: atp.Status=candidate
        self.bucketSize: Optional[PositiveInteger] = None

        # Configuration of rules on the Data Link Layer Tags: atp.Status=candidate
        self.dataLinkLayerRule: Optional["DataLinkLayerRule"] = None

        # Configuration of firewall rules for DDS. Tags: atp.Status=candidate
        self.ddsRule: Optional["DdsRule"] = None

        # Configuration of firewall rules for DoIP messages Tags: atp.Status=candidate
        self.doIpRule: Optional["DoIpRule"] = None

        # Configuration of rules on the Network Layer Tags: atp.Status=candidate
        self.networkLayerRule: Optional["NetworkLayerRule"] = None

        # Configuration of generic firewall rules Tags: atp.Status=candidate
        self.payloadBytePatternRules: List["PayloadBytePatternRule"] = []

        # This attribute defines the output rate that describes how many packets leave the queue per second (leaky-bucket Algorithm). Tags: atp.Status=candidate
        self.refillAmount: Optional[PositiveInteger] = None

        # Configuration of firewall rules for SOME/IP messages Tags: atp.Status=candidate
        self.someipRule: Optional["SomeipProtocolRule"] = None

        # Configuration of firewall rules for SOME/IP Service Discovery messages Tags: atp.Status=candidate
        self.someipSdRule: Optional["SomeipSdRule"] = None

        # Configuration of rules on the Transport Layer Tags: atp.Status=candidate
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
    """
    Configuration of filter rules on the Network layer Tags: atp.Status=candidate
    """

    # NetworkLayerRule method parity checklist:
    # Spec: AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform), class NetworkLayerRule, AUTOSAR_00052.xsd line 84252 (XSD-only; no own table in repo corpus)
    # (abstract class: the NETWORK-LAYER-RULE group is an empty sequence with no
    #  complexType; the FirewallRule.networkLayerRule element carries a choice of
    #  the concrete subtypes Ipv4Rule/Ipv6Rule, which are not yet implemented —
    #  the class stays instantiable as the aggregation placeholder per Rule
    #  0001.10 and gains the abstract guard + five-place dispatch when they sync)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class PayloadBytePatternRule(ARObject):
    """Configuration of a generic firewall rule that defines the individual bytes of a message that shall match. Tags: atp.Status=candidate"""

    # PayloadBytePatternRule method parity checklist:
    # Spec: AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform), class PayloadBytePatternRule, AUTOSAR_00052.xsd line 88473 (XSD-only; no own table in repo corpus)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addPayloadBytePatternRulePart  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPayloadBytePatternRuleParts [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Configuration of bytes in the message,
        self.payloadBytePatternRuleParts: List["PayloadBytePatternRulePart"] = []

    def addPayloadBytePatternRulePart(self, value: Optional["PayloadBytePatternRulePart"]) -> "PayloadBytePatternRule":
        """
        Configuration of bytes in the message,
        A None value is a no-op and does not overwrite an existing payloadBytePatternRulePart.
        """
        if value is not None:
            self.payloadBytePatternRuleParts.append(value)
        return self

    def getPayloadBytePatternRuleParts(self) -> List["PayloadBytePatternRulePart"]:
        """Configuration of bytes in the message,"""
        return self.payloadBytePatternRuleParts


class PayloadBytePatternRulePart(ARObject):
    """Configuration of one byte in the datagram, Tags: atp.Status=candidate"""

    # PayloadBytePatternRulePart method parity checklist:
    # Spec: AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform), class PayloadBytePatternRulePart, AUTOSAR_00052.xsd line 88508 (XSD-only; no own table in repo corpus)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOffset  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOffset  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValue   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute defines the byte offset in the datagram (start byte of the Ethernet frame, i.e. offset 0 corresponds to the first byte of the destination MAC address).
        self.offset: Optional[PositiveInteger] = None

        # This attribute defines the byteValue (0..255) in the datagram.
        self.value: Optional[PositiveInteger] = None

    def getOffset(self) -> Optional[PositiveInteger]:
        """This attribute defines the byte offset in the datagram (start byte of the Ethernet frame, i.e. offset 0 corresponds to the first byte of the destination MAC address)."""
        return self.offset

    def setOffset(self, value: Optional[PositiveInteger]) -> "PayloadBytePatternRulePart":
        """
        This attribute defines the byte offset in the datagram (start byte of the Ethernet frame, i.e. offset 0 corresponds to the first byte of the destination MAC address).
        A None value is a no-op and does not overwrite an existing offset.
        """
        if value is not None:
            self.offset = value
        return self

    def getValue(self) -> Optional[PositiveInteger]:
        """This attribute defines the byteValue (0..255) in the datagram."""
        return self.value

    def setValue(self, value: Optional[PositiveInteger]) -> "PayloadBytePatternRulePart":
        """
        This attribute defines the byteValue (0..255) in the datagram.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self


class SomeipProtocolRule(ARObject):
    """Configuration of SOME/IP firewall rules Tags: atp.Status=candidate"""

    # SomeipProtocolRule method parity checklist:
    # Spec: AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform), class SomeipProtocolRule, AUTOSAR_00052.xsd line 110084 (XSD-only; no own table in repo corpus)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getClientId             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setClientId             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLengthVerification   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLengthVerification   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMajorVersion         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMajorVersion         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMessageType          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMessageType          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMethodId             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMethodId             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProtocolVersion      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProtocolVersion      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReturnCode           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReturnCode           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getServiceInterfaceId   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setServiceInterfaceId   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Filter for SOME/IP messages in which the clientId in the SOME/IP header matches.
        self.clientId: Optional[PositiveInteger] = None

        # Defines whether length verification is performed or not.
        self.lengthVerification: Optional[Boolean] = None

        # Filter for SOME/IP messages in which the majorVersion  in the SOME/IP header matches.
        self.majorVersion: Optional[PositiveInteger] = None

        # Filter for SOME/IP messages in which the messageType in the SOME/IP header matches.
        self.messageType: Optional[PositiveInteger] = None

        # Filter for SOME/IP messages in which the methodId in the SOME/IP header matches.
        self.methodId: Optional[PositiveInteger] = None

        # Filter for SOME/IP messages in which the protocolVersion  in the SOME/IP header matches.
        self.protocolVersion: Optional[PositiveInteger] = None

        # Filter for SOME/IP messages in which the returnCode  in the SOME/IP header matches.
        self.returnCode: Optional[PositiveInteger] = None

        # Filter for SOME/IP messages in which the serviceInterfaceId in the SOME/IP header matches.
        self.serviceInterfaceId: Optional[PositiveInteger] = None

    def getClientId(self) -> Optional[PositiveInteger]:
        """Filter for SOME/IP messages in which the clientId in the SOME/IP header matches."""
        return self.clientId

    def setClientId(self, value: Optional[PositiveInteger]) -> "SomeipProtocolRule":
        """
        Filter for SOME/IP messages in which the clientId in the SOME/IP header matches.
        A None value is a no-op and does not overwrite an existing clientId.
        """
        if value is not None:
            self.clientId = value
        return self

    def getLengthVerification(self) -> Optional[Boolean]:
        """Defines whether length verification is performed or not."""
        return self.lengthVerification

    def setLengthVerification(self, value: Optional[Boolean]) -> "SomeipProtocolRule":
        """
        Defines whether length verification is performed or not.
        A None value is a no-op and does not overwrite an existing lengthVerification.
        """
        if value is not None:
            self.lengthVerification = value
        return self

    def getMajorVersion(self) -> Optional[PositiveInteger]:
        """Filter for SOME/IP messages in which the majorVersion  in the SOME/IP header matches."""
        return self.majorVersion

    def setMajorVersion(self, value: Optional[PositiveInteger]) -> "SomeipProtocolRule":
        """
        Filter for SOME/IP messages in which the majorVersion  in the SOME/IP header matches.
        A None value is a no-op and does not overwrite an existing majorVersion.
        """
        if value is not None:
            self.majorVersion = value
        return self

    def getMessageType(self) -> Optional[PositiveInteger]:
        """Filter for SOME/IP messages in which the messageType in the SOME/IP header matches."""
        return self.messageType

    def setMessageType(self, value: Optional[PositiveInteger]) -> "SomeipProtocolRule":
        """
        Filter for SOME/IP messages in which the messageType in the SOME/IP header matches.
        A None value is a no-op and does not overwrite an existing messageType.
        """
        if value is not None:
            self.messageType = value
        return self

    def getMethodId(self) -> Optional[PositiveInteger]:
        """Filter for SOME/IP messages in which the methodId in the SOME/IP header matches."""
        return self.methodId

    def setMethodId(self, value: Optional[PositiveInteger]) -> "SomeipProtocolRule":
        """
        Filter for SOME/IP messages in which the methodId in the SOME/IP header matches.
        A None value is a no-op and does not overwrite an existing methodId.
        """
        if value is not None:
            self.methodId = value
        return self

    def getProtocolVersion(self) -> Optional[PositiveInteger]:
        """Filter for SOME/IP messages in which the protocolVersion  in the SOME/IP header matches."""
        return self.protocolVersion

    def setProtocolVersion(self, value: Optional[PositiveInteger]) -> "SomeipProtocolRule":
        """
        Filter for SOME/IP messages in which the protocolVersion  in the SOME/IP header matches.
        A None value is a no-op and does not overwrite an existing protocolVersion.
        """
        if value is not None:
            self.protocolVersion = value
        return self

    def getReturnCode(self) -> Optional[PositiveInteger]:
        """Filter for SOME/IP messages in which the returnCode  in the SOME/IP header matches."""
        return self.returnCode

    def setReturnCode(self, value: Optional[PositiveInteger]) -> "SomeipProtocolRule":
        """
        Filter for SOME/IP messages in which the returnCode  in the SOME/IP header matches.
        A None value is a no-op and does not overwrite an existing returnCode.
        """
        if value is not None:
            self.returnCode = value
        return self

    def getServiceInterfaceId(self) -> Optional[PositiveInteger]:
        """Filter for SOME/IP messages in which the serviceInterfaceId in the SOME/IP header matches."""
        return self.serviceInterfaceId

    def setServiceInterfaceId(self, value: Optional[PositiveInteger]) -> "SomeipProtocolRule":
        """
        Filter for SOME/IP messages in which the serviceInterfaceId in the SOME/IP header matches.
        A None value is a no-op and does not overwrite an existing serviceInterfaceId.
        """
        if value is not None:
            self.serviceInterfaceId = value
        return self


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
    """
    Configuration of filter rules on Transport Layer level. Tags: atp.Status=candidate
    """

    # TransportLayerRule method parity checklist:
    # Spec: AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform), class TransportLayerRule, AUTOSAR_00052.xsd line 126190 (XSD-only; no own table in repo corpus)
    # (abstract class: the TRANSPORT-LAYER-RULE group is an empty sequence with no
    #  complexType; the FirewallRule.transportLayerRule element carries a choice of
    #  the concrete subtypes TcpRule/UdpRule, which are not yet implemented —
    #  the class stays instantiable as the aggregation placeholder per Rule
    #  0001.10 and gains the abstract guard + five-place dispatch when they sync)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class DataLinkLayerRule(ARObject):
    """
    Configuration of filter rules on the DataLink layer Tags: atp.Status=candidate
    """

    # DataLinkLayerRule method parity checklist:
    # Spec: AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform), class DataLinkLayerRule, AUTOSAR_00052.xsd line 27236 (XSD-only; no own table in repo corpus)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDestinationMacAddress        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestinationMacAddress        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDestinationMacAddressMask    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestinationMacAddressMask    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEtherType                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEtherType                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceMacAddress             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceMacAddress             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceMacAddressMask         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceMacAddressMask         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlanId                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVlanId                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlanPriority                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVlanPriority                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Filter to match packets with the destination MAC address.
        self.destinationMacAddress: Optional[MacAddressString] = None

        # Filter to match packets with the destination MAC address range. The destinationMacAddress with the destinationMacAddressMask defines the MAC address range.
        self.destinationMacAddressMask: Optional[MacAddressString] = None

        # Filter to match packets based on the EtherType field in the Ethernet frame. The EtherType is used to indicate which protocol is encapsulated in the payload of the frame.
        self.etherType: Optional[PositiveInteger] = None

        # Filter to match packets with the source MAC address.
        self.sourceMacAddress: Optional[MacAddressString] = None

        # Filter to match packets with the source MAC address range. The sourceMacAddress with the sourceMacAddressMask defines the MAC address range.
        self.sourceMacAddressMask: Optional[MacAddressString] = None

        # Filter of packets with a specific VlanId.
        self.vlanId: Optional[PositiveInteger] = None

        # Filter of packets with a specific Vlan priority.
        self.vlanPriority: Optional[PositiveInteger] = None

    def getDestinationMacAddress(self) -> Optional[MacAddressString]:
        """Filter to match packets with the destination MAC address."""
        return self.destinationMacAddress

    def setDestinationMacAddress(self, value: Optional[MacAddressString]) -> "DataLinkLayerRule":
        """
        Filter to match packets with the destination MAC address.
        A None value is a no-op and does not overwrite an existing destinationMacAddress.
        """
        if value is not None:
            self.destinationMacAddress = value
        return self

    def getDestinationMacAddressMask(self) -> Optional[MacAddressString]:
        """Filter to match packets with the destination MAC address range. The destinationMacAddress with the destinationMacAddressMask defines the MAC address range."""
        return self.destinationMacAddressMask

    def setDestinationMacAddressMask(self, value: Optional[MacAddressString]) -> "DataLinkLayerRule":
        """
        Filter to match packets with the destination MAC address range. The destinationMacAddress with the destinationMacAddressMask defines the MAC address range.
        A None value is a no-op and does not overwrite an existing destinationMacAddressMask.
        """
        if value is not None:
            self.destinationMacAddressMask = value
        return self

    def getEtherType(self) -> Optional[PositiveInteger]:
        """Filter to match packets based on the EtherType field in the Ethernet frame. The EtherType is used to indicate which protocol is encapsulated in the payload of the frame."""
        return self.etherType

    def setEtherType(self, value: Optional[PositiveInteger]) -> "DataLinkLayerRule":
        """
        Filter to match packets based on the EtherType field in the Ethernet frame. The EtherType is used to indicate which protocol is encapsulated in the payload of the frame.
        A None value is a no-op and does not overwrite an existing etherType.
        """
        if value is not None:
            self.etherType = value
        return self

    def getSourceMacAddress(self) -> Optional[MacAddressString]:
        """Filter to match packets with the source MAC address."""
        return self.sourceMacAddress

    def setSourceMacAddress(self, value: Optional[MacAddressString]) -> "DataLinkLayerRule":
        """
        Filter to match packets with the source MAC address.
        A None value is a no-op and does not overwrite an existing sourceMacAddress.
        """
        if value is not None:
            self.sourceMacAddress = value
        return self

    def getSourceMacAddressMask(self) -> Optional[MacAddressString]:
        """Filter to match packets with the source MAC address range. The sourceMacAddress with the sourceMacAddressMask defines the MAC address range."""
        return self.sourceMacAddressMask

    def setSourceMacAddressMask(self, value: Optional[MacAddressString]) -> "DataLinkLayerRule":
        """
        Filter to match packets with the source MAC address range. The sourceMacAddress with the sourceMacAddressMask defines the MAC address range.
        A None value is a no-op and does not overwrite an existing sourceMacAddressMask.
        """
        if value is not None:
            self.sourceMacAddressMask = value
        return self

    def getVlanId(self) -> Optional[PositiveInteger]:
        """Filter of packets with a specific VlanId."""
        return self.vlanId

    def setVlanId(self, value: Optional[PositiveInteger]) -> "DataLinkLayerRule":
        """
        Filter of packets with a specific VlanId.
        A None value is a no-op and does not overwrite an existing vlanId.
        """
        if value is not None:
            self.vlanId = value
        return self

    def getVlanPriority(self) -> Optional[PositiveInteger]:
        """Filter of packets with a specific Vlan priority."""
        return self.vlanPriority

    def setVlanPriority(self, value: Optional[PositiveInteger]) -> "DataLinkLayerRule":
        """
        Filter of packets with a specific Vlan priority.
        A None value is a no-op and does not overwrite an existing vlanPriority.
        """
        if value is not None:
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


class FirewallActionEnum(AREnum):
    """List of actions that the Firewall is able to perform."""

    # FirewallActionEnum method parity checklist:
    # Spec: AUTOSAR_00052.xsd complexType FIREWALL-ACTION-ENUM l.136671 + --SIMPLE l.136683 (XSD-only; no markdown/PDF table); consumed by StateDependentFirewall.defaultAction (Table 6.234) and FirewallRuleProps.action (Table 6.235)
    # XSD verified: AUTOSAR_00052.xsd
    # Arbitration 2026-09-22: literal order follows the XSD EnumerationLiteralIndex tags (BLOCK=0 l.136694, ALLOW=1 l.136688); the --SIMPLE document order and the ECUC literal-mapping tables list ALLOW first, which is alphabetical ordering, not index metadata
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Firewall blocks the communication Tags: atp.EnumerationLiteralIndex=0
    BLOCK = "BLOCK"

    # Firewall allows the communication Tags: atp.EnumerationLiteralIndex=1
    ALLOW = "ALLOW"

    def __init__(self):
        super().__init__(
            (
                FirewallActionEnum.BLOCK,
                FirewallActionEnum.ALLOW,
            )
        )


class FirewallRuleProps(ARObject):
    """Firewall rule that is defined by an action that is performed if the referenced pattern matches."""

    # FirewallRuleProps method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.235, p.584 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getAction                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAction                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addMatchingEgressRuleRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getMatchingEgressRuleRefs    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addMatchingIngressRuleRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getMatchingIngressRuleRefs   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Action that is performed by the firewall if the matching Rule is fulfilled.
        self.action: Optional[FirewallActionEnum] = None

        # This element defines an egress rule expression against which the network traffic is matched.
        self.matchingEgressRuleRefs: List[RefType] = []

        # This element defines an ingress rule expression against which the network traffic is matched.
        self.matchingIngressRuleRefs: List[RefType] = []

    def getAction(self) -> Optional[FirewallActionEnum]:
        """
        Action that is performed by the firewall if the matching Rule is fulfilled.
        """
        return self.action

    def setAction(self, value: Optional[FirewallActionEnum]):
        """
        Sets the action value.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.action = value
        return self

    def addMatchingEgressRuleRef(self, value: RefType):
        """
        This element defines an egress rule expression against which the network traffic is matched.

        Returns:
            self for method chaining
        """
        self.matchingEgressRuleRefs.append(value)
        return self

    def getMatchingEgressRuleRefs(self) -> List[RefType]:
        """
        This element defines an egress rule expression against which the network traffic is matched.
        """
        return self.matchingEgressRuleRefs

    def addMatchingIngressRuleRef(self, value: RefType):
        """
        This element defines an ingress rule expression against which the network traffic is matched.

        Returns:
            self for method chaining
        """
        self.matchingIngressRuleRefs.append(value)
        return self

    def getMatchingIngressRuleRefs(self) -> List[RefType]:
        """
        This element defines an ingress rule expression against which the network traffic is matched.
        """
        return self.matchingIngressRuleRefs


class StateDependentFirewall(ARElement):
    """Firewall rules that are defined in a firewall state"""

    # StateDependentFirewall method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.234, p.584 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # Note: the XSD-only AP variant firewallState (FIREWALL-STATE-IREFS, iref type
    #  FIREWALL-STATE-IN-FIRWALL-STATE-SWITCH-INTERFACE-INSTANCE-REF) is not modeled —
    #  Rule 0015: the PDF/markdown table is authoritative and Table 6.234 (CP) lists
    #  only firewallStateModeDeclaration
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getDefaultAction                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultAction                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addFirewallRuleProps              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFirewallRuleProps              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addFirewallStateModeDeclarationRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFirewallStateModeDeclarationRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This attribute defines a defaultAction in case that the VehicleMode is not yet set.
        self.defaultAction: Optional[FirewallActionEnum] = None

        # Collection of firewall rules that apply in the vehicle mode
        self.firewallRuleProps: List[FirewallRuleProps] = []

        # Reference to firewall states in which the Firewall is active. If one of the referenced ModeDeclarations is the current firewall state then the firewall rule shall be considered as active.
        self.firewallStateModeDeclarationRefs: List[RefType] = []

    def getDefaultAction(self) -> Optional[FirewallActionEnum]:
        """
        This attribute defines a defaultAction in case that the VehicleMode is not yet set.
        """
        return self.defaultAction

    def setDefaultAction(self, value: Optional[FirewallActionEnum]):
        """
        This attribute defines a defaultAction in case that the VehicleMode is not yet set. Only sets the value if it is not None.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.defaultAction = value
        return self

    def addFirewallRuleProps(self, value: FirewallRuleProps):
        """
        Collection of firewall rules that apply in the vehicle mode

        Returns:
            self for method chaining
        """
        self.firewallRuleProps.append(value)
        return self

    def getFirewallRuleProps(self) -> List[FirewallRuleProps]:
        """
        Collection of firewall rules that apply in the vehicle mode
        """
        return self.firewallRuleProps

    def addFirewallStateModeDeclarationRef(self, value: RefType):
        """
        Reference to firewall states in which the Firewall is active. If one of the referenced ModeDeclarations is the current firewall state then the firewall rule shall be considered as active.

        Returns:
            self for method chaining
        """
        self.firewallStateModeDeclarationRefs.append(value)
        return self

    def getFirewallStateModeDeclarationRefs(self) -> List[RefType]:
        """
        Reference to firewall states in which the Firewall is active. If one of the referenced ModeDeclarations is the current firewall state then the firewall rule shall be considered as active.
        """
        return self.firewallStateModeDeclarationRefs
