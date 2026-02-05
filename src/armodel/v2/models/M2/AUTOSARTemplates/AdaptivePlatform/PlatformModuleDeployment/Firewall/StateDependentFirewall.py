from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class StateDependentFirewall(ARObject):
    """
    Represents a state-dependent firewall in AUTOSAR Adaptive Platform PlatformModuleDeployment.
    Defines firewall rules that depend on system states.
    """

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
