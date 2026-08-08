"""
This module contains tests for the FirewallRule class in the
AUTOSAR AdaptivePlatform.PlatformModuleDeployment.Firewall module.
"""

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.FirewallRule import (
    FirewallRule,
)


class TestFirewallRule:
    """
    Test class for FirewallRule functionality.
    """

    def test_initialization(self):
        obj = FirewallRule()
        assert obj.getDestRefs() == []
        assert obj.getSrcRefs() == []

    def test_dest_refs(self):
        obj = FirewallRule()
        assert obj.addDestRef("dest") is obj
        assert obj.getDestRefs() == ["dest"]

    def test_src_refs(self):
        obj = FirewallRule()
        assert obj.addSrcRef("src") is obj
        assert obj.getSrcRefs() == ["src"]
