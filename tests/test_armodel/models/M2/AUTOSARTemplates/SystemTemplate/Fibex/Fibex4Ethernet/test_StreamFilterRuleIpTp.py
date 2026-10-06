"""
Test suite for StreamFilterRuleIpTp (CP_TPS_SystemTemplate Table 3.88, p.138, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the StreamFilterRuleIpTp model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    StreamFilterIpv4Address,
    StreamFilterIpv6Address,
    StreamFilterPortRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterRuleIpTp

CLASS_NOTE = "Configuration of filter rules for IP and TP. Tags: atp.Status=candidate"

DESTINATION_IPV4_ADDRESS_NOTE = "Filter to match packets with the destination IPv4 address range. Tags: atp.Status=candidate"
DESTINATION_IPV6_ADDRESS_NOTE = "Filter to match packets with the destination IPv6 address range. Tags: atp.Status=candidate"
DESTINATION_PORT_NOTE = "Filter to match packets with the set of destination UDP/TCP port ranges. Tags: atp.Status=candidate"
SOURCE_IPV4_ADDRESS_NOTE = "Filter to match packets with the source IPv4 address range. Tags: atp.Status=candidate"
SOURCE_IPV6_ADDRESS_NOTE = "Filter to match packets with the source IPv6 address range. Tags: atp.Status=candidate"
SOURCE_PORT_NOTE = "Filter to match packets with the set of source UDP/TCP port ranges. Tags: atp.Status=candidate"


class TestStreamFilterRuleIpTp:
    def test_inheritance(self):
        assert issubclass(StreamFilterRuleIpTp, ARObject)

    def test_concrete_class_instantiable(self):
        rule = StreamFilterRuleIpTp()
        assert isinstance(rule, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(StreamFilterRuleIpTp.__doc__) == CLASS_NOTE

    def test_initialization(self):
        rule = StreamFilterRuleIpTp()

        assert rule.getDestinationIpv4Address() is None
        assert rule.getDestinationIpv6Address() is None
        assert rule.getDestinationPorts() == []
        assert rule.getSourceIpv4Address() is None
        assert rule.getSourceIpv6Address() is None
        assert rule.getSourcePorts() == []

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "StreamFilterRuleIpTp")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("destinationIpv4Address", "Optional[StreamFilterIpv4Address]"),
            ("destinationIpv6Address", "Optional[StreamFilterIpv6Address]"),
            ("destinationPorts", "List[StreamFilterPortRange]"),
            ("sourceIpv4Address", "Optional[StreamFilterIpv4Address]"),
            ("sourceIpv6Address", "Optional[StreamFilterIpv6Address]"),
            ("sourcePorts", "List[StreamFilterPortRange]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(StreamFilterRuleIpTp.getDestinationIpv4Address).get("return") == typing.Optional[StreamFilterIpv4Address]
        assert typing.get_type_hints(StreamFilterRuleIpTp.setDestinationIpv4Address).get("value") == typing.Optional[StreamFilterIpv4Address]
        assert typing.get_type_hints(StreamFilterRuleIpTp.setDestinationIpv4Address).get("return") is StreamFilterRuleIpTp
        assert typing.get_type_hints(StreamFilterRuleIpTp.getDestinationIpv6Address).get("return") == typing.Optional[StreamFilterIpv6Address]
        assert typing.get_type_hints(StreamFilterRuleIpTp.setDestinationIpv6Address).get("value") == typing.Optional[StreamFilterIpv6Address]
        assert typing.get_type_hints(StreamFilterRuleIpTp.setDestinationIpv6Address).get("return") is StreamFilterRuleIpTp
        assert typing.get_type_hints(StreamFilterRuleIpTp.addDestinationPort).get("value") == typing.Optional[StreamFilterPortRange]
        assert typing.get_type_hints(StreamFilterRuleIpTp.addDestinationPort).get("return") is StreamFilterRuleIpTp
        assert typing.get_type_hints(StreamFilterRuleIpTp.getDestinationPorts).get("return") == typing.List[StreamFilterPortRange]
        assert typing.get_type_hints(StreamFilterRuleIpTp.getSourceIpv4Address).get("return") == typing.Optional[StreamFilterIpv4Address]
        assert typing.get_type_hints(StreamFilterRuleIpTp.setSourceIpv4Address).get("value") == typing.Optional[StreamFilterIpv4Address]
        assert typing.get_type_hints(StreamFilterRuleIpTp.setSourceIpv4Address).get("return") is StreamFilterRuleIpTp
        assert typing.get_type_hints(StreamFilterRuleIpTp.getSourceIpv6Address).get("return") == typing.Optional[StreamFilterIpv6Address]
        assert typing.get_type_hints(StreamFilterRuleIpTp.setSourceIpv6Address).get("value") == typing.Optional[StreamFilterIpv6Address]
        assert typing.get_type_hints(StreamFilterRuleIpTp.setSourceIpv6Address).get("return") is StreamFilterRuleIpTp
        assert typing.get_type_hints(StreamFilterRuleIpTp.addSourcePort).get("value") == typing.Optional[StreamFilterPortRange]
        assert typing.get_type_hints(StreamFilterRuleIpTp.addSourcePort).get("return") is StreamFilterRuleIpTp
        assert typing.get_type_hints(StreamFilterRuleIpTp.getSourcePorts).get("return") == typing.List[StreamFilterPortRange]

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(StreamFilterRuleIpTp.getDestinationIpv4Address.__doc__) == DESTINATION_IPV4_ADDRESS_NOTE
        assert (
            inspect.cleandoc(StreamFilterRuleIpTp.setDestinationIpv4Address.__doc__)
            == DESTINATION_IPV4_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing destinationIpv4Address."
        )
        assert inspect.cleandoc(StreamFilterRuleIpTp.getDestinationIpv6Address.__doc__) == DESTINATION_IPV6_ADDRESS_NOTE
        assert (
            inspect.cleandoc(StreamFilterRuleIpTp.setDestinationIpv6Address.__doc__)
            == DESTINATION_IPV6_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing destinationIpv6Address."
        )
        assert inspect.cleandoc(StreamFilterRuleIpTp.addDestinationPort.__doc__) == DESTINATION_PORT_NOTE + "\n\nA None value is a no-op and does not add to destinationPorts."
        assert inspect.cleandoc(StreamFilterRuleIpTp.getDestinationPorts.__doc__) == DESTINATION_PORT_NOTE
        assert inspect.cleandoc(StreamFilterRuleIpTp.getSourceIpv4Address.__doc__) == SOURCE_IPV4_ADDRESS_NOTE
        assert inspect.cleandoc(StreamFilterRuleIpTp.setSourceIpv4Address.__doc__) == SOURCE_IPV4_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing sourceIpv4Address."
        assert inspect.cleandoc(StreamFilterRuleIpTp.getSourceIpv6Address.__doc__) == SOURCE_IPV6_ADDRESS_NOTE
        assert inspect.cleandoc(StreamFilterRuleIpTp.setSourceIpv6Address.__doc__) == SOURCE_IPV6_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing sourceIpv6Address."
        assert inspect.cleandoc(StreamFilterRuleIpTp.addSourcePort.__doc__) == SOURCE_PORT_NOTE + "\n\nA None value is a no-op and does not add to sourcePorts."
        assert inspect.cleandoc(StreamFilterRuleIpTp.getSourcePorts.__doc__) == SOURCE_PORT_NOTE

    def test_get_set_destination_ipv4_address(self):
        rule = StreamFilterRuleIpTp()

        value = StreamFilterIpv4Address()
        assert rule.setDestinationIpv4Address(value) is rule
        assert rule.getDestinationIpv4Address() is value

        assert rule.setDestinationIpv4Address(None) is rule
        assert rule.getDestinationIpv4Address() is value

    def test_get_set_destination_ipv6_address(self):
        rule = StreamFilterRuleIpTp()

        value = StreamFilterIpv6Address()
        assert rule.setDestinationIpv6Address(value) is rule
        assert rule.getDestinationIpv6Address() is value

        assert rule.setDestinationIpv6Address(None) is rule
        assert rule.getDestinationIpv6Address() is value

    def test_add_destination_port(self):
        rule = StreamFilterRuleIpTp()

        first = StreamFilterPortRange()
        second = StreamFilterPortRange()
        assert rule.addDestinationPort(first) is rule
        assert rule.addDestinationPort(second) is rule
        assert rule.getDestinationPorts() == [first, second]

        assert rule.addDestinationPort(None) is rule
        assert rule.getDestinationPorts() == [first, second]

    def test_get_set_source_ipv4_address(self):
        rule = StreamFilterRuleIpTp()

        value = StreamFilterIpv4Address()
        assert rule.setSourceIpv4Address(value) is rule
        assert rule.getSourceIpv4Address() is value

        assert rule.setSourceIpv4Address(None) is rule
        assert rule.getSourceIpv4Address() is value

    def test_get_set_source_ipv6_address(self):
        rule = StreamFilterRuleIpTp()

        value = StreamFilterIpv6Address()
        assert rule.setSourceIpv6Address(value) is rule
        assert rule.getSourceIpv6Address() is value

        assert rule.setSourceIpv6Address(None) is rule
        assert rule.getSourceIpv6Address() is value

    def test_add_source_port(self):
        rule = StreamFilterRuleIpTp()

        first = StreamFilterPortRange()
        second = StreamFilterPortRange()
        assert rule.addSourcePort(first) is rule
        assert rule.addSourcePort(second) is rule
        assert rule.getSourcePorts() == [first, second]

        assert rule.addSourcePort(None) is rule
        assert rule.getSourcePorts() == [first, second]
