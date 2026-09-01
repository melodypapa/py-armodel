from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import (
    FirewallActionEnum,
    FirewallRule,
    FirewallRuleProps,
    StateDependentFirewall,
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


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


class TestFirewallActionEnum:
    """
    Test class for FirewallActionEnum (XSD-only enumeration, Table 6.234/6.235 attribute type).
    """

    def test_literals(self):
        assert FirewallActionEnum.BLOCK == "BLOCK"
        assert FirewallActionEnum.ALLOW == "ALLOW"
        obj = FirewallActionEnum()
        assert obj.setValue(FirewallActionEnum.BLOCK) is obj
        assert obj.getValue() == "BLOCK"

    def test_class_docstring_is_spec_verbatim(self):
        assert FirewallActionEnum.__doc__ == "List of actions that the Firewall is able to perform."


class TestFirewallRuleProps:
    """
    Test class for FirewallRuleProps functionality (Table 6.235).
    """

    def test_defaults(self):
        obj = FirewallRuleProps()
        assert obj.getAction() is None
        assert obj.getMatchingEgressRuleRefs() == []
        assert obj.getMatchingIngressRuleRefs() == []

    def test_set_get_action(self):
        obj = FirewallRuleProps()
        assert obj.setAction(FirewallActionEnum().setValue(FirewallActionEnum.BLOCK)) is obj
        assert obj.getAction() is not None and obj.getAction().getValue() == FirewallActionEnum.BLOCK
        obj.setAction(None)
        assert obj.getAction() is not None and obj.getAction().getValue() == FirewallActionEnum.BLOCK

    def test_add_get_matching_egress_rule_refs(self):
        obj = FirewallRuleProps()
        ref = RefType()
        ref.setValue("/AUTOSAR/FirewallRules/Rule")
        assert obj.addMatchingEgressRuleRef(ref) is obj
        assert obj.getMatchingEgressRuleRefs() == [ref]

    def test_add_get_matching_ingress_rule_refs(self):
        obj = FirewallRuleProps()
        ref = RefType()
        ref.setValue("/AUTOSAR/FirewallRules/Rule")
        assert obj.addMatchingIngressRuleRef(ref) is obj
        assert obj.getMatchingIngressRuleRefs() == [ref]

    def test_class_docstring_is_spec_note_verbatim(self):
        assert FirewallRuleProps.__doc__ == "Firewall rule that is defined by an action that is performed if the referenced pattern matches."


"""
This module contains tests for the StateDependentFirewall class in the
AUTOSAR AdaptivePlatform.PlatformModuleDeployment.Firewall module.
"""


class TestStateDependentFirewall:
    """
    Test class for StateDependentFirewall functionality (Table 6.234).
    """

    def test_initialization(self):
        obj = StateDependentFirewall(_parent(), "TestStateDependentFirewall")
        assert obj.getShortName() == "TestStateDependentFirewall"
        assert obj.getDefaultAction() is None
        assert obj.getFirewallRuleProps() == []
        assert obj.getFirewallStateModeDeclarationRefs() == []

    def test_set_get_default_action(self):
        obj = StateDependentFirewall(_parent(), "TestStateDependentFirewall")
        assert obj.setDefaultAction(FirewallActionEnum().setValue(FirewallActionEnum.ALLOW)) is obj
        assert obj.getDefaultAction() is not None and obj.getDefaultAction().getValue() == FirewallActionEnum.ALLOW
        obj.setDefaultAction(None)
        assert obj.getDefaultAction() is not None and obj.getDefaultAction().getValue() == FirewallActionEnum.ALLOW

    def test_add_get_firewall_rule_props(self):
        obj = StateDependentFirewall(_parent(), "TestStateDependentFirewall")
        props1 = FirewallRuleProps()
        props2 = FirewallRuleProps()
        assert obj.addFirewallRuleProps(props1) is obj
        assert obj.addFirewallRuleProps(props2) is obj
        assert obj.getFirewallRuleProps() == [props1, props2]

    def test_add_get_firewall_state_mode_declaration_refs(self):
        obj = StateDependentFirewall(_parent(), "TestStateDependentFirewall")
        ref = RefType()
        ref.setValue("/AUTOSAR/Modes/State")
        assert obj.addFirewallStateModeDeclarationRef(ref) is obj
        assert obj.getFirewallStateModeDeclarationRefs() == [ref]

    def test_class_docstring_is_spec_note_verbatim(self):
        assert StateDependentFirewall.__doc__ == "Firewall rules that are defined in a firewall state"
