"""
This module contains tests for the StateDependentFirewall class in the
AUTOSAR AdaptivePlatform.PlatformModuleDeployment.Firewall module.
"""

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.StateDependentFirewall import (
    StateDependentFirewall,
)


class TestStateDependentFirewall:
    """
    Test class for StateDependentFirewall functionality.
    """

    def test_initialization(self):
        obj = StateDependentFirewall()
        assert obj.getFirewallRules() == []
        assert obj.getStateRef() is None

    def test_firewall_rules(self):
        obj = StateDependentFirewall()
        assert obj.addFirewallRule("rule") is obj
        assert obj.getFirewallRules() == ["rule"]

    def test_set_state_ref(self):
        obj = StateDependentFirewall()
        assert obj.setStateRef("state") is obj
        assert obj.getStateRef() == "state"
