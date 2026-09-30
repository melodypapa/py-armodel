"""
This module contains tests for the IPSecConfig class
in the AUTOSAR SystemTemplate Fibex4Ethernet EthernetTopology module.
"""

import inspect
import re
import typing

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    IPSecConfig,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPSecRule

CLASS_NOTE = """IPsec is a protocol that is designed to provide "end-to-end" cryptographically-based security for IP network connections."""

FIELD_ORDER = ["ipSecConfigPropsRef", "ipSecRules"]

METHOD_ORDER = ["__init__", "getIpSecConfigPropsRef", "setIpSecConfigPropsRef", "addIPSecRule", "getIPSecRules"]


def _parent():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document


def _rule(name):
    return IPSecRule(_parent(), name)


class TestIPSecConfig:
    """Test cases for IPSecConfig (Table 6.221, p.571)."""

    def _obj(self):
        return IPSecConfig()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getIpSecConfigPropsRef() is None
        assert obj.getIPSecRules() == []

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        item = RefType()
        assert obj.setIpSecConfigPropsRef(item) is obj
        assert obj.getIpSecConfigPropsRef() is item
        obj.setIpSecConfigPropsRef(None)
        assert obj.getIpSecConfigPropsRef() is item

    def test_add_ip_sec_rule(self):
        obj = self._obj()
        rule1 = _rule("Rule1")
        assert obj.addIPSecRule(rule1) is obj
        rule2 = _rule("Rule2")
        obj.addIPSecRule(rule2)
        assert obj.getIPSecRules() == [rule1, rule2]

    def test_add_ip_sec_rule_none_noop(self):
        obj = self._obj()
        rule = _rule("Rule1")
        obj.addIPSecRule(rule)
        obj.addIPSecRule(None)
        assert obj.getIPSecRules() == [rule]

    def test_get_ip_sec_rules_returns_list(self):
        obj = self._obj()
        rules = obj.getIPSecRules()
        assert isinstance(rules, list)
        rules.append(_rule("Rule1"))
        assert obj.getIPSecRules() == rules

    def test_class_docstring_note(self):
        assert inspect.cleandoc(IPSecConfig.__doc__) == CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert IPSecConfig.__init__.__doc__ is None

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        props_note = "Global IPsec configuration settings that are valid for all IPSecRules that are defined on the NetworkEndpoint."
        rule_note = "IPSec rules and filters that are defined in the IPSecConfig for a specific NetworkEndpoint."
        assert inspect.cleandoc(obj.getIpSecConfigPropsRef.__doc__) == props_note
        assert inspect.cleandoc(obj.setIpSecConfigPropsRef.__doc__).split("\n")[0] == props_note
        assert inspect.cleandoc(obj.setIpSecConfigPropsRef.__doc__).split("\n")[1] == "A None value is a no-op and does not overwrite an existing ipSecConfigPropsRef."
        assert inspect.cleandoc(obj.addIPSecRule.__doc__).split("\n")[0] == rule_note
        assert inspect.cleandoc(obj.addIPSecRule.__doc__).split("\n")[1] == "A None value is a no-op and does not extend the ipSecRules list."
        assert inspect.cleandoc(obj.getIPSecRules.__doc__) == rule_note

    def test_member_order_follows_spec_row_order(self):
        init_src = inspect.getsource(IPSecConfig.__init__)
        fields = re.findall(r"self\.(\w+):", init_src)
        assert fields == FIELD_ORDER

        class_src = inspect.getsource(IPSecConfig)
        methods = re.findall(r"def (\w+)\(self", class_src)
        assert methods == METHOD_ORDER

    def test_typing_pins(self):
        hints = typing.get_type_hints(IPSecConfig.getIpSecConfigPropsRef)
        assert hints.get("return") == typing.Optional[RefType]
        setter_hints = typing.get_type_hints(IPSecConfig.setIpSecConfigPropsRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is IPSecConfig
        add_hints = typing.get_type_hints(IPSecConfig.addIPSecRule)
        assert add_hints.get("value") == typing.Optional[IPSecRule]
        assert add_hints.get("return") is IPSecConfig
        get_hints = typing.get_type_hints(IPSecConfig.getIPSecRules)
        assert get_hints.get("return") == typing.List[IPSecRule]
