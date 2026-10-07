"""
Test suite for StreamFilterIpv4Address (CP_TPS_SystemTemplate Table 3.89, p.138, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the StreamFilterIpv4Address model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip4AddressString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    StreamFilterIpv4Address,
)

CLASS_NOTE = "IPv4 address range definition. Tags: atp.Status=candidate"

IPV4_ADDRESS_NOTE = "Filter to match packets with the IPv4 address. Tags: atp.Status=candidate"
IPV4_ADDRESS_MASK_NOTE = "Filter to match packets with the IPv4 address range. Tags: atp.Status=candidate"


class TestStreamFilterIpv4Address:
    def test_inheritance(self):
        assert issubclass(StreamFilterIpv4Address, ARObject)

    def test_concrete_class_instantiable(self):
        ipv4_address = StreamFilterIpv4Address()
        assert isinstance(ipv4_address, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(StreamFilterIpv4Address.__doc__) == CLASS_NOTE

    def test_initialization(self):
        ipv4_address = StreamFilterIpv4Address()

        assert ipv4_address.getIpv4Address() is None
        assert ipv4_address.getIpv4AddressMask() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "StreamFilterIpv4Address")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("ipv4Address", "Optional[Ip4AddressString]"),
            ("ipv4AddressMask", "Optional[Ip4AddressString]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(StreamFilterIpv4Address.getIpv4Address).get("return") == typing.Optional[Ip4AddressString]
        assert typing.get_type_hints(StreamFilterIpv4Address.setIpv4Address).get("value") == typing.Optional[Ip4AddressString]
        assert typing.get_type_hints(StreamFilterIpv4Address.setIpv4Address).get("return") is StreamFilterIpv4Address
        assert typing.get_type_hints(StreamFilterIpv4Address.getIpv4AddressMask).get("return") == typing.Optional[Ip4AddressString]
        assert typing.get_type_hints(StreamFilterIpv4Address.setIpv4AddressMask).get("value") == typing.Optional[Ip4AddressString]
        assert typing.get_type_hints(StreamFilterIpv4Address.setIpv4AddressMask).get("return") is StreamFilterIpv4Address

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(StreamFilterIpv4Address.getIpv4Address.__doc__) == IPV4_ADDRESS_NOTE
        assert inspect.cleandoc(StreamFilterIpv4Address.setIpv4Address.__doc__) == IPV4_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ipv4Address."
        assert inspect.cleandoc(StreamFilterIpv4Address.getIpv4AddressMask.__doc__) == IPV4_ADDRESS_MASK_NOTE
        assert inspect.cleandoc(StreamFilterIpv4Address.setIpv4AddressMask.__doc__) == IPV4_ADDRESS_MASK_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ipv4AddressMask."

    def test_get_set_ipv4_address(self):
        ipv4_address = StreamFilterIpv4Address()

        value = Ip4AddressString().setValue("192.168.0.1")
        assert ipv4_address.setIpv4Address(value) is ipv4_address
        assert ipv4_address.getIpv4Address() is value
        assert ipv4_address.getIpv4Address().getValue() == "192.168.0.1"

        assert ipv4_address.setIpv4Address(None) is ipv4_address
        assert ipv4_address.getIpv4Address() is value

    def test_get_set_ipv4_address_mask(self):
        ipv4_address = StreamFilterIpv4Address()

        value = Ip4AddressString().setValue("255.255.0.0")
        assert ipv4_address.setIpv4AddressMask(value) is ipv4_address
        assert ipv4_address.getIpv4AddressMask() is value
        assert ipv4_address.getIpv4AddressMask().getValue() == "255.255.0.0"

        assert ipv4_address.setIpv4AddressMask(None) is ipv4_address
        assert ipv4_address.getIpv4AddressMask() is value
