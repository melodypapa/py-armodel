"""
This module contains tests for the FirewallRuleProps class in the
AUTOSAR AdaptivePlatform.PlatformModuleDeployment.Firewall module.
"""

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.FirewallRuleProps import (
    FirewallRuleProps,
)


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
