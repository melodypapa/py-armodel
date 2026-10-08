import inspect
import typing

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

    def test_allow_round_trip(self):
        obj = FirewallActionEnum()
        assert obj.setValue(FirewallActionEnum.ALLOW) is obj
        assert obj.getValue() == "ALLOW"

    def test_literal_order_matches_xsd_index_tags(self):
        """BLOCK is EnumerationLiteralIndex=0 and ALLOW=1 per AUTOSAR_00052.xsd l.136694/136688 (arbitrated 2026-09-22: tags outrank --SIMPLE document order)."""
        obj = FirewallActionEnum()
        assert obj.getEnumValues() == ("BLOCK", "ALLOW")

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
    Spec text pins are verbatim from the markdown, Tags tails kept per Rule 0012.2.5.3.
    """

    CLASS_NOTE = "Firewall rules that are defined in a firewall state Tags: atp.Status=candidate atp.recommendedPackage=StateDependentFirewallRules"
    DEFAULT_ACTION_NOTE = "This attribute defines a defaultAction in case that the VehicleMode is not yet set. Tags: atp.Status=candidate"
    RULE_PROPS_NOTE = "Collection of firewall rules that apply in the vehicle mode Tags: atp.Status=candidate"
    MODE_REFS_NOTE = "Reference to firewall states in which the Firewall is active. If one of the referenced ModeDeclarations is the current firewall state then the firewall rule shall be considered as active. Tags: atp.Status=candidate"
    MEMBERS = ["defaultAction", "firewallRuleProps", "firewallStateModeDeclarationRefs"]

    def _create(self, short_name: str) -> StateDependentFirewall:
        return StateDependentFirewall(_parent(), short_name)

    def test_initialization(self):
        obj = self._create("TestStateDependentFirewall")
        assert obj.getShortName() == "TestStateDependentFirewall"
        assert obj.getDefaultAction() is None
        assert obj.getFirewallRuleProps() == []
        assert obj.getFirewallStateModeDeclarationRefs() == []

    def test_member_order(self):
        obj = self._create("TestStateDependentFirewall")
        members = [k for k in vars(obj) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_class_docstring_note(self):
        assert inspect.cleandoc(StateDependentFirewall.__doc__) == self.CLASS_NOTE

    def test_init_docstring_is_none(self):
        assert StateDependentFirewall.__init__.__doc__ is None

    def test_pep526_annotations(self):
        source = inspect.getsource(StateDependentFirewall)
        assert "self.defaultAction: Optional[FirewallActionEnum] = None" in source
        assert "self.firewallRuleProps: List[FirewallRuleProps] = []" in source
        assert "self.firewallStateModeDeclarationRefs: List[RefType] = []" in source

    def test_type_hints(self):
        hints = typing.get_type_hints(StateDependentFirewall.getDefaultAction)
        assert hints["return"] == typing.Optional[FirewallActionEnum]
        hints = typing.get_type_hints(StateDependentFirewall.setDefaultAction)
        assert hints["value"] == typing.Optional[FirewallActionEnum]
        assert hints["return"] == StateDependentFirewall
        hints = typing.get_type_hints(StateDependentFirewall.addFirewallRuleProps)
        assert hints["value"] == typing.Optional[FirewallRuleProps]
        assert hints["return"] == StateDependentFirewall
        hints = typing.get_type_hints(StateDependentFirewall.getFirewallRuleProps)
        assert hints["return"] == typing.List[FirewallRuleProps]
        hints = typing.get_type_hints(StateDependentFirewall.addFirewallStateModeDeclarationRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] == StateDependentFirewall
        hints = typing.get_type_hints(StateDependentFirewall.getFirewallStateModeDeclarationRefs)
        assert hints["return"] == typing.List[RefType]

    def test_set_get_default_action(self):
        obj = self._create("TestStateDependentFirewall")
        assert obj.setDefaultAction(FirewallActionEnum().setValue(FirewallActionEnum.ALLOW)) is obj
        assert obj.getDefaultAction() is not None and obj.getDefaultAction().getValue() == FirewallActionEnum.ALLOW
        obj.setDefaultAction(None)
        assert obj.getDefaultAction() is not None and obj.getDefaultAction().getValue() == FirewallActionEnum.ALLOW

    def test_default_action_docstrings(self):
        assert StateDependentFirewall.getDefaultAction.__doc__ == self.DEFAULT_ACTION_NOTE
        expected = self.DEFAULT_ACTION_NOTE + "\nA None value is a no-op and does not overwrite an existing defaultAction."
        assert inspect.cleandoc(StateDependentFirewall.setDefaultAction.__doc__) == expected

    def test_add_get_firewall_rule_props(self):
        obj = self._create("TestStateDependentFirewall")
        props1 = FirewallRuleProps()
        props2 = FirewallRuleProps()
        assert obj.addFirewallRuleProps(props1) is obj
        assert obj.addFirewallRuleProps(props2) is obj
        assert obj.getFirewallRuleProps() == [props1, props2]

    def test_add_firewall_rule_props_none_no_op(self):
        obj = self._create("TestStateDependentFirewall")
        props = FirewallRuleProps()
        assert obj.addFirewallRuleProps(props) is obj
        obj.addFirewallRuleProps(None)
        assert obj.getFirewallRuleProps() == [props]

    def test_firewall_rule_props_docstrings(self):
        assert StateDependentFirewall.addFirewallRuleProps.__doc__ is not None
        expected = self.RULE_PROPS_NOTE + "\nA None value is a no-op and does not overwrite an existing firewallRuleProps."
        assert inspect.cleandoc(StateDependentFirewall.addFirewallRuleProps.__doc__) == expected
        assert StateDependentFirewall.getFirewallRuleProps.__doc__ == self.RULE_PROPS_NOTE

    def test_add_get_firewall_state_mode_declaration_refs(self):
        obj = self._create("TestStateDependentFirewall")
        ref = RefType()
        ref.setValue("/AUTOSAR/Modes/State")
        assert obj.addFirewallStateModeDeclarationRef(ref) is obj
        assert obj.getFirewallStateModeDeclarationRefs() == [ref]

    def test_add_firewall_state_mode_declaration_ref_none_no_op(self):
        obj = self._create("TestStateDependentFirewall")
        ref = RefType()
        ref.setValue("/AUTOSAR/Modes/State")
        assert obj.addFirewallStateModeDeclarationRef(ref) is obj
        obj.addFirewallStateModeDeclarationRef(None)
        assert obj.getFirewallStateModeDeclarationRefs() == [ref]

    def test_firewall_state_mode_declaration_refs_docstrings(self):
        expected = self.MODE_REFS_NOTE + "\nA None value is a no-op and does not overwrite an existing firewallStateModeDeclarationRefs."
        assert inspect.cleandoc(StateDependentFirewall.addFirewallStateModeDeclarationRef.__doc__) == expected
        assert StateDependentFirewall.getFirewallStateModeDeclarationRefs.__doc__ == self.MODE_REFS_NOTE
