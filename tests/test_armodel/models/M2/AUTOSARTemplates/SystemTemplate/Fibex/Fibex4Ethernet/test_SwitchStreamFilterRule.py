"""
Test suite for SwitchStreamFilterRule (CP_TPS_SystemTemplate Table 3.85, p.136, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the SwitchStreamFilterRule model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    StreamFilterIEEE1722Tp,
    StreamFilterRuleDataLinkLayer,
    StreamFilterRuleIpTp,
    SwitchStreamFilterRule,
)

CLASS_NOTE = "SwitchStreamIdentification Tags: atp.Status=candidate"

DATA_LINK_LAYER_RULE_NOTE = "Definition of a filter rule on the data link layer. Tags: atp.Status=candidate"
IEEE1722_TP_RULE_NOTE = "Definition of a filter rule for IEEE1722Tp. Tags: atp.Status=candidate"
IP_TP_RULE_NOTE = "Definition of a filter rule IP and TP. Tags: atp.Status=candidate"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSwitchStreamFilterRule:
    def test_inheritance(self):
        assert issubclass(SwitchStreamFilterRule, Identifiable)

    def test_concrete_class_instantiable(self):
        rule = SwitchStreamFilterRule(MockParent(), "Rule1")
        assert isinstance(rule, Identifiable)
        assert rule.getShortName() == "Rule1"
        assert rule.getParent() is not None

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SwitchStreamFilterRule.__doc__) == CLASS_NOTE

    def test_initialization(self):
        rule = SwitchStreamFilterRule(MockParent(), "Rule1")

        assert rule.getDataLinkLayerRule() is None
        assert rule.getIeee1722TpRule() is None
        assert rule.getIpTpRule() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "SwitchStreamFilterRule")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("dataLinkLayerRule", "Optional[StreamFilterRuleDataLinkLayer]"),
            ("ieee1722TpRule", "Optional[StreamFilterIEEE1722Tp]"),
            ("ipTpRule", "Optional[StreamFilterRuleIpTp]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(SwitchStreamFilterRule.getDataLinkLayerRule).get("return") == typing.Optional[StreamFilterRuleDataLinkLayer]
        assert typing.get_type_hints(SwitchStreamFilterRule.setDataLinkLayerRule).get("value") == typing.Optional[StreamFilterRuleDataLinkLayer]
        assert typing.get_type_hints(SwitchStreamFilterRule.setDataLinkLayerRule).get("return") is SwitchStreamFilterRule
        assert typing.get_type_hints(SwitchStreamFilterRule.getIeee1722TpRule).get("return") == typing.Optional[StreamFilterIEEE1722Tp]
        assert typing.get_type_hints(SwitchStreamFilterRule.setIeee1722TpRule).get("value") == typing.Optional[StreamFilterIEEE1722Tp]
        assert typing.get_type_hints(SwitchStreamFilterRule.setIeee1722TpRule).get("return") is SwitchStreamFilterRule
        assert typing.get_type_hints(SwitchStreamFilterRule.getIpTpRule).get("return") == typing.Optional[StreamFilterRuleIpTp]
        assert typing.get_type_hints(SwitchStreamFilterRule.setIpTpRule).get("value") == typing.Optional[StreamFilterRuleIpTp]
        assert typing.get_type_hints(SwitchStreamFilterRule.setIpTpRule).get("return") is SwitchStreamFilterRule

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(SwitchStreamFilterRule.getDataLinkLayerRule.__doc__) == DATA_LINK_LAYER_RULE_NOTE
        assert inspect.cleandoc(SwitchStreamFilterRule.setDataLinkLayerRule.__doc__) == DATA_LINK_LAYER_RULE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dataLinkLayerRule."
        assert inspect.cleandoc(SwitchStreamFilterRule.getIeee1722TpRule.__doc__) == IEEE1722_TP_RULE_NOTE
        assert inspect.cleandoc(SwitchStreamFilterRule.setIeee1722TpRule.__doc__) == IEEE1722_TP_RULE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ieee1722TpRule."
        assert inspect.cleandoc(SwitchStreamFilterRule.getIpTpRule.__doc__) == IP_TP_RULE_NOTE
        assert inspect.cleandoc(SwitchStreamFilterRule.setIpTpRule.__doc__) == IP_TP_RULE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ipTpRule."

    def test_get_set_data_link_layer_rule(self):
        rule = SwitchStreamFilterRule(MockParent(), "Rule1")

        value = StreamFilterRuleDataLinkLayer()
        assert rule.setDataLinkLayerRule(value) is rule
        assert rule.getDataLinkLayerRule() is value

        assert rule.setDataLinkLayerRule(None) is rule
        assert rule.getDataLinkLayerRule() is value

    def test_get_set_ieee_1722_tp_rule(self):
        rule = SwitchStreamFilterRule(MockParent(), "Rule1")

        value = StreamFilterIEEE1722Tp()
        assert rule.setIeee1722TpRule(value) is rule
        assert rule.getIeee1722TpRule() is value

        assert rule.setIeee1722TpRule(None) is rule
        assert rule.getIeee1722TpRule() is value

    def test_get_set_ip_tp_rule(self):
        rule = SwitchStreamFilterRule(MockParent(), "Rule1")

        value = StreamFilterRuleIpTp()
        assert rule.setIpTpRule(value) is rule
        assert rule.getIpTpRule() is value

        assert rule.setIpTpRule(None) is rule
        assert rule.getIpTpRule() is value
