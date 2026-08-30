from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

__all__ = ["FirewallRule", "FirewallRuleProps", "StateDependentFirewall"]


class FirewallRule(ARObject):
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

    def __init__(self):
        """
        Initializes the FirewallRule with default values.
        """
        super().__init__()
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


class StateDependentFirewall(ARObject):
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

    def __init__(self):
        """
        Initializes the StateDependentFirewall with default values.
        """
        super().__init__()
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
