import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import (
    DataLinkLayerRule,
    DdsRule,
    DoIpRule,
    FirewallActionEnum,
    FirewallRule,
    FirewallRuleProps,
    NetworkLayerRule,
    PayloadBytePatternRule,
    SomeipProtocolRule,
    SomeipSdRule,
    StateDependentFirewall,
    TransportLayerRule,
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestFirewallRulePlaceholders:
    def test_placeholder_members_instantiable(self):
        for cls in (DoIpRule, NetworkLayerRule, PayloadBytePatternRule, SomeipProtocolRule, SomeipSdRule, TransportLayerRule):
            assert cls() is not None


class TestFirewallRule:
    def _create_rule(self) -> FirewallRule:
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return FirewallRule(ar_root, "TestFirewallRule")

    def test_initialization(self):
        obj = self._create_rule()
        assert obj.getShortName() == "TestFirewallRule"
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

    def test_get_set_bucket_size(self):
        obj = self._create_rule()
        value = PositiveInteger()
        value.setValue(10)
        assert obj.setBucketSize(value) is obj
        assert obj.getBucketSize() is value
        obj.setBucketSize(None)
        assert obj.getBucketSize() is value

    def test_get_set_refill_amount(self):
        obj = self._create_rule()
        value = PositiveInteger()
        value.setValue(100)
        assert obj.setRefillAmount(value) is obj
        assert obj.getRefillAmount() is value
        obj.setRefillAmount(None)
        assert obj.getRefillAmount() is value

    def test_get_set_data_link_layer_rule(self):
        obj = self._create_rule()
        rule = DataLinkLayerRule()
        assert obj.setDataLinkLayerRule(rule) is obj
        assert obj.getDataLinkLayerRule() is rule
        obj.setDataLinkLayerRule(None)
        assert obj.getDataLinkLayerRule() is rule

    def test_get_set_dds_rule(self):
        obj = self._create_rule()
        rule = DdsRule()
        assert obj.setDdsRule(rule) is obj
        assert obj.getDdsRule() is rule

    def test_get_set_do_ip_rule(self):
        obj = self._create_rule()
        rule = DoIpRule()
        assert obj.setDoIpRule(rule) is obj
        assert obj.getDoIpRule() is rule

    def test_get_set_network_layer_rule(self):
        obj = self._create_rule()
        rule = NetworkLayerRule()
        assert obj.setNetworkLayerRule(rule) is obj
        assert obj.getNetworkLayerRule() is rule

    def test_get_set_someip_rule(self):
        obj = self._create_rule()
        rule = SomeipProtocolRule()
        assert obj.setSomeipRule(rule) is obj
        assert obj.getSomeipRule() is rule

    def test_get_set_someip_sd_rule(self):
        obj = self._create_rule()
        rule = SomeipSdRule()
        assert obj.setSomeipSdRule(rule) is obj
        assert obj.getSomeipSdRule() is rule

    def test_get_set_transport_layer_rule(self):
        obj = self._create_rule()
        rule = TransportLayerRule()
        assert obj.setTransportLayerRule(rule) is obj
        assert obj.getTransportLayerRule() is rule

    def test_add_get_payload_byte_pattern_rules(self):
        obj = self._create_rule()
        rule1 = PayloadBytePatternRule()
        rule2 = PayloadBytePatternRule()
        assert obj.addPayloadBytePatternRule(rule1) is obj
        assert obj.addPayloadBytePatternRule(rule2) is obj
        assert obj.getPayloadBytePatternRules() == [rule1, rule2]

    def test_class_docstring_is_spec_note_verbatim(self):
        assert FirewallRule.__doc__ == "Firewall Rule that defines the control information in individual packets."


class TestFirewallRuleReadWrite:
    def _create_rule(self) -> FirewallRule:
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        rule = FirewallRule(ar_root, "FirewallRule")
        bucket_size = PositiveInteger()
        bucket_size.setValue(10)
        rule.setBucketSize(bucket_size)
        refill_amount = PositiveInteger()
        refill_amount.setValue(20)
        rule.setRefillAmount(refill_amount)
        rule.setDataLinkLayerRule(DataLinkLayerRule())
        rule.setDdsRule(DdsRule())
        rule.setDoIpRule(DoIpRule())
        rule.setNetworkLayerRule(NetworkLayerRule())
        rule.addPayloadBytePatternRule(PayloadBytePatternRule())
        rule.addPayloadBytePatternRule(PayloadBytePatternRule())
        rule.setSomeipRule(SomeipProtocolRule())
        rule.setSomeipSdRule(SomeipSdRule())
        rule.setTransportLayerRule(TransportLayerRule())
        return rule

    def test_write(self):
        rule = self._create_rule()
        parent = ET.Element("PARENT")
        writer = ARXMLWriter()
        writer.writeFirewallRule(parent, rule)
        rule_tag = parent.find("FIREWALL-RULE")
        assert rule_tag is not None
        assert rule_tag.find("BUCKET-SIZE") is not None
        assert rule_tag.find("DATA-LINK-LAYER-RULE") is not None
        assert rule_tag.find("DDS-RULE") is not None
        assert rule_tag.find("DO-IP-RULE") is not None
        assert rule_tag.find("NETWORK-LAYER-RULE") is not None
        assert rule_tag.find("PAYLOAD-BYTE-PATTERN-RULES/PAYLOAD-BYTE-PATTERN-RULE") is not None
        assert len(rule_tag.findall("PAYLOAD-BYTE-PATTERN-RULES/PAYLOAD-BYTE-PATTERN-RULE")) == 2
        assert rule_tag.find("REFILL-AMOUNT") is not None
        assert rule_tag.find("SOMEIP-RULE") is not None
        assert rule_tag.find("SOMEIP-SD-RULE") is not None
        assert rule_tag.find("TRANSPORT-LAYER-RULE") is not None

    def test_round_trip(self):
        rule = self._create_rule()
        parent = ET.Element("PARENT")
        writer = ARXMLWriter()
        writer.writeFirewallRule(parent, rule)

        inner = ET.tostring(parent).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='http://autosar.org/schema/r4.0'>{inner}</AUTOSAR>")[0][0]

        recovered = FirewallRule(ET.Element("DUMMY"), "FirewallRule")
        parser = ARXMLParser()
        parser.readFirewallRule(element, recovered)

        assert recovered.getShortName() == "FirewallRule"
        assert recovered.getBucketSize() is not None and recovered.getBucketSize().getValue() == 10
        assert recovered.getRefillAmount() is not None and recovered.getRefillAmount().getValue() == 20
        assert isinstance(recovered.getDataLinkLayerRule(), DataLinkLayerRule)
        assert isinstance(recovered.getDdsRule(), DdsRule)
        assert isinstance(recovered.getDoIpRule(), DoIpRule)
        assert isinstance(recovered.getNetworkLayerRule(), NetworkLayerRule)
        assert len(recovered.getPayloadBytePatternRules()) == 2
        assert all(isinstance(r, PayloadBytePatternRule) for r in recovered.getPayloadBytePatternRules())
        assert isinstance(recovered.getSomeipRule(), SomeipProtocolRule)
        assert isinstance(recovered.getSomeipSdRule(), SomeipSdRule)
        assert isinstance(recovered.getTransportLayerRule(), TransportLayerRule)


class TestStateDependentFirewallReadWrite:
    def _create_firewall(self) -> StateDependentFirewall:
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        fw = StateDependentFirewall(ar_root, "StateDependentFirewall")
        fw.setDefaultAction(FirewallActionEnum().setValue(FirewallActionEnum.BLOCK))
        props = FirewallRuleProps()
        props.setAction(FirewallActionEnum().setValue(FirewallActionEnum.ALLOW))
        ref = RefType()
        ref.setValue("/AUTOSAR/FirewallRules/Rule")
        props.addMatchingEgressRuleRef(ref)
        fw.addFirewallRuleProps(props)
        mode_ref = RefType()
        mode_ref.setValue("/AUTOSAR/Modes/State")
        fw.addFirewallStateModeDeclarationRef(mode_ref)
        return fw

    def test_round_trip(self):
        fw = self._create_firewall()
        parent = ET.Element("PARENT")
        writer = ARXMLWriter()
        writer.writeStateDependentFirewall(parent, fw)

        inner = ET.tostring(parent).decode("utf-8")
        element = ET.fromstring(f"<AUTOSAR xmlns='http://autosar.org/schema/r4.0'>{inner}</AUTOSAR>")[0][0]

        recovered = StateDependentFirewall(ET.Element("DUMMY"), "StateDependentFirewall")
        parser = ARXMLParser()
        parser.readStateDependentFirewall(element, recovered)

        assert recovered.getShortName() == "StateDependentFirewall"
        assert recovered.getDefaultAction() is not None and recovered.getDefaultAction().getValue() == FirewallActionEnum.BLOCK
        props_list = recovered.getFirewallRuleProps()
        assert len(props_list) == 1
        assert props_list[0].getAction() is not None and props_list[0].getAction().getValue() == FirewallActionEnum.ALLOW
        assert len(props_list[0].getMatchingEgressRuleRefs()) == 1
        assert props_list[0].getMatchingEgressRuleRefs()[0].getValue() == "/AUTOSAR/FirewallRules/Rule"
        assert len(recovered.getFirewallStateModeDeclarationRefs()) == 1
        assert recovered.getFirewallStateModeDeclarationRefs()[0].getValue() == "/AUTOSAR/Modes/State"
