"""
Test suite for StreamFilterMACAddress (CP_TPS_SystemTemplate Table 3.87, p.137, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the StreamFilterMACAddress model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    StreamFilterMACAddress,
)

CLASS_NOTE = "Configuration of filter rules on the DataLink layer Tags: atp.Status=candidate"

MAC_ADDRESS_NOTE = "Filter to match packets with the MAC address. Tags: atp.Status=candidate"
MAC_ADDRESS_MASK_NOTE = "Filter to match packets with the MAC address range. Tags: atp.Status=candidate"


class TestStreamFilterMACAddress:
    def test_inheritance(self):
        assert issubclass(StreamFilterMACAddress, ARObject)

    def test_concrete_class_instantiable(self):
        mac_address = StreamFilterMACAddress()
        assert isinstance(mac_address, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(StreamFilterMACAddress.__doc__) == CLASS_NOTE

    def test_initialization(self):
        mac_address = StreamFilterMACAddress()

        assert mac_address.getMacAddress() is None
        assert mac_address.getMacAddressMask() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "StreamFilterMACAddress")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("macAddress", "Optional[MacAddressString]"),
            ("macAddressMask", "Optional[MacAddressString]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(StreamFilterMACAddress.getMacAddress).get("return") == typing.Optional[MacAddressString]
        assert typing.get_type_hints(StreamFilterMACAddress.setMacAddress).get("value") == typing.Optional[MacAddressString]
        assert typing.get_type_hints(StreamFilterMACAddress.setMacAddress).get("return") is StreamFilterMACAddress
        assert typing.get_type_hints(StreamFilterMACAddress.getMacAddressMask).get("return") == typing.Optional[MacAddressString]
        assert typing.get_type_hints(StreamFilterMACAddress.setMacAddressMask).get("value") == typing.Optional[MacAddressString]
        assert typing.get_type_hints(StreamFilterMACAddress.setMacAddressMask).get("return") is StreamFilterMACAddress

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(StreamFilterMACAddress.getMacAddress.__doc__) == MAC_ADDRESS_NOTE
        assert inspect.cleandoc(StreamFilterMACAddress.setMacAddress.__doc__) == MAC_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing macAddress."
        assert inspect.cleandoc(StreamFilterMACAddress.getMacAddressMask.__doc__) == MAC_ADDRESS_MASK_NOTE
        assert inspect.cleandoc(StreamFilterMACAddress.setMacAddressMask.__doc__) == MAC_ADDRESS_MASK_NOTE + "\n\nA None value is a no-op and does not overwrite an existing macAddressMask."

    def test_get_set_mac_address(self):
        mac_address = StreamFilterMACAddress()

        value = MacAddressString().setValue("FF:FF:FF:FF:FF:FF")
        assert mac_address.setMacAddress(value) is mac_address
        assert mac_address.getMacAddress() is value
        assert mac_address.getMacAddress().getValue() == "FF:FF:FF:FF:FF:FF"

        assert mac_address.setMacAddress(None) is mac_address
        assert mac_address.getMacAddress() is value

    def test_get_set_mac_address_mask(self):
        mac_address = StreamFilterMACAddress()

        value = MacAddressString().setValue("FF:00:00:00:00:00")
        assert mac_address.setMacAddressMask(value) is mac_address
        assert mac_address.getMacAddressMask() is value
        assert mac_address.getMacAddressMask().getValue() == "FF:00:00:00:00:00"

        assert mac_address.setMacAddressMask(None) is mac_address
        assert mac_address.getMacAddressMask() is value
