from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement

__all__ = ["FirewallRule", "FirewallRuleProps", "StateDependentFirewall", "DataLinkLayerRule"]


class FirewallRule(ARElement):
    """
    Represents a firewall rule in AUTOSAR Adaptive Platform PlatformModuleDeployment.
    Defines rules for firewall configuration in adaptive platform modules.
    """

    # FirewallRule method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] addDestRef                   [x] impl  [x] docstring  [ ] test
    # [ ] getDestRefs                  [x] impl  [x] docstring  [ ] test
    # [ ] addSrcRef                    [x] impl  [x] docstring  [ ] test
    # [ ] getSrcRefs                   [x] impl  [x] docstring  [ ] test

    def __init__(self, parent, short_name: str):
        """
        Initializes the FirewallRule with a parent and short name.

        Args:
            parent: The parent ARObject that contains this element
            short_name: The short name of this element
        """
        super().__init__(parent, short_name)
        self.destRefs: List[RefType] = []
        self.srcRefs: List[RefType] = []

    def addDestRef(self, ref: RefType):
        """
        Adds a destination reference to this firewall rule.

        Args:
            ref: The destination reference to add

        Returns:
            self for method chaining
        """
        self.destRefs.append(ref)
        return self

    def getDestRefs(self) -> List[RefType]:
        """
        Gets the list of destination references.

        Returns:
            List of destination references
        """
        return self.destRefs

    def addSrcRef(self, ref: RefType):
        """
        Adds a source reference to this firewall rule.

        Args:
            ref: The source reference to add

        Returns:
            self for method chaining
        """
        self.srcRefs.append(ref)
        return self

    def getSrcRefs(self) -> List[RefType]:
        """
        Gets the list of source references.

        Returns:
            List of source references
        """
        return self.srcRefs


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
