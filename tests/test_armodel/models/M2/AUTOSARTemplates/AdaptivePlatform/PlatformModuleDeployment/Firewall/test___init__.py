from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import (
    FirewallRule,
    FirewallRuleProps,
    StateDependentFirewall,
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


def _parent():
    """Return a package to use as the parent of an Identifiable under test."""
    return AUTOSAR.getInstance().createARPackage("AUTOSAR")


"""
This module contains tests for the FirewallRule class in the
AUTOSAR AdaptivePlatform.PlatformModuleDeployment.Firewall module.
"""


class TestFirewallRule:
    """
    Test class for FirewallRule functionality.
    """

    def test_initialization(self):
        obj = FirewallRule(_parent(), "TestFirewallRule")
        assert obj.getBucketSize() is None
        assert obj.getDataLinkLayerRule() is None
        assert obj.getDdsRule() is None
        assert obj.getDoIpRule() is None
        assert obj.getNetworkLayerRule() is None
        assert obj.getPayloadBytePatternRules() == []
        assert obj.getRefillAmount() is None
        assert obj.getSomeipRule() is None
        assert obj.getSomeipSdRule() is None
        assert obj.getTransportLayerRule() is None


"""
This module contains tests for the FirewallRuleProps class in the
AUTOSAR AdaptivePlatform.PlatformModuleDeployment.Firewall module.
"""


class TestFirewallRuleProps:
    """
    Test class for FirewallRuleProps functionality.
    """

    def test_defaults(self):
        obj = FirewallRuleProps()
        assert obj.getAllowAny() is None
        assert obj.getDirection() is None
        assert obj.getProtocol() is None

    def test_set_get_allow_any(self):
        obj = FirewallRuleProps()
        assert obj.setAllowAny(True) is obj
        assert obj.getAllowAny() is True

    def test_set_get_direction(self):
        obj = FirewallRuleProps()
        assert obj.setDirection("IN") is obj
        assert obj.getDirection() == "IN"

    def test_set_get_protocol(self):
        obj = FirewallRuleProps()
        assert obj.setProtocol("TCP") is obj
        assert obj.getProtocol() == "TCP"


"""
This module contains tests for the StateDependentFirewall class in the
AUTOSAR AdaptivePlatform.PlatformModuleDeployment.Firewall module.
"""


class TestStateDependentFirewall:
    """
    Test class for StateDependentFirewall functionality.
    """

    def test_initialization(self):
        obj = StateDependentFirewall(_parent(), "TestStateDependentFirewall")
        assert obj.getFirewallRules() == []
        assert obj.getStateRef() is None

    def test_firewall_rules(self):
        obj = StateDependentFirewall(_parent(), "TestStateDependentFirewall")
        assert obj.addFirewallRule("rule") is obj
        assert obj.getFirewallRules() == ["rule"]

    def test_set_state_ref(self):
        obj = StateDependentFirewall(_parent(), "TestStateDependentFirewall")
        assert obj.setStateRef("state") is obj
        assert obj.getStateRef() == "state"
