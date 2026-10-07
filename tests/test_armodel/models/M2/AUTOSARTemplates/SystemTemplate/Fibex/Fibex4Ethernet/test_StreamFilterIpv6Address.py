"""
Test suite for StreamFilterIpv6Address (CP_TPS_SystemTemplate Table 3.90, p.138, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the StreamFilterIpv6Address model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip6AddressString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    StreamFilterIpv6Address,
)

CLASS_NOTE = "IPv6 address range definition. Tags: atp.Status=candidate"

IPV6_ADDRESS_NOTE = "Filter to match packets with the IPv6 address. Tags: atp.Status=candidate"
IPV6_ADDRESS_MASK_NOTE = "Filter to match packets with the IPv6 address range. Tags: atp.Status=candidate"


class TestStreamFilterIpv6Address:
    def test_inheritance(self):
        assert issubclass(StreamFilterIpv6Address, ARObject)

    def test_concrete_class_instantiable(self):
        ipv6_address = StreamFilterIpv6Address()
        assert isinstance(ipv6_address, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(StreamFilterIpv6Address.__doc__) == CLASS_NOTE

    def test_initialization(self):
        ipv6_address = StreamFilterIpv6Address()

        assert ipv6_address.getIpv6Address() is None
        assert ipv6_address.getIpv6AddressMask() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "StreamFilterIpv6Address")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("ipv6Address", "Optional[Ip6AddressString]"),
            ("ipv6AddressMask", "Optional[Ip6AddressString]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(StreamFilterIpv6Address.getIpv6Address).get("return") == typing.Optional[Ip6AddressString]
        assert typing.get_type_hints(StreamFilterIpv6Address.setIpv6Address).get("value") == typing.Optional[Ip6AddressString]
        assert typing.get_type_hints(StreamFilterIpv6Address.setIpv6Address).get("return") is StreamFilterIpv6Address
        assert typing.get_type_hints(StreamFilterIpv6Address.getIpv6AddressMask).get("return") == typing.Optional[Ip6AddressString]
        assert typing.get_type_hints(StreamFilterIpv6Address.setIpv6AddressMask).get("value") == typing.Optional[Ip6AddressString]
        assert typing.get_type_hints(StreamFilterIpv6Address.setIpv6AddressMask).get("return") is StreamFilterIpv6Address

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(StreamFilterIpv6Address.getIpv6Address.__doc__) == IPV6_ADDRESS_NOTE
        assert inspect.cleandoc(StreamFilterIpv6Address.setIpv6Address.__doc__) == IPV6_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ipv6Address."
        assert inspect.cleandoc(StreamFilterIpv6Address.getIpv6AddressMask.__doc__) == IPV6_ADDRESS_MASK_NOTE
        assert inspect.cleandoc(StreamFilterIpv6Address.setIpv6AddressMask.__doc__) == IPV6_ADDRESS_MASK_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ipv6AddressMask."

    def test_get_set_ipv6_address(self):
        ipv6_address = StreamFilterIpv6Address()

        value = Ip6AddressString().setValue("2001:0DB8:0000:0000:0000:0000:0000:0001")
        assert ipv6_address.setIpv6Address(value) is ipv6_address
        assert ipv6_address.getIpv6Address() is value
        assert ipv6_address.getIpv6Address().getValue() == "2001:0DB8:0000:0000:0000:0000:0000:0001"

        assert ipv6_address.setIpv6Address(None) is ipv6_address
        assert ipv6_address.getIpv6Address() is value

    def test_get_set_ipv6_address_mask(self):
        ipv6_address = StreamFilterIpv6Address()

        value = Ip6AddressString().setValue("FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF")
        assert ipv6_address.setIpv6AddressMask(value) is ipv6_address
        assert ipv6_address.getIpv6AddressMask() is value
        assert ipv6_address.getIpv6AddressMask().getValue() == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF"

        assert ipv6_address.setIpv6AddressMask(None) is ipv6_address
        assert ipv6_address.getIpv6AddressMask() is value
