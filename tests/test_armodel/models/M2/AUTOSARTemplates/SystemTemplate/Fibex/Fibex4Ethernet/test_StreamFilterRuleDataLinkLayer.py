"""
Test suite for StreamFilterRuleDataLinkLayer (CP_TPS_SystemTemplate Table 3.86, p.137, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the StreamFilterRuleDataLinkLayer model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    StreamFilterMACAddress,
    StreamFilterRuleDataLinkLayer,
)

CLASS_NOTE = "Configuration of filter rules on the DataLink layer Tags: atp.Status=candidate"

DESTINATION_MAC_ADDRESS_NOTE = "Filter to match packets with the destination MAC address/ mask. Tags: atp.Status=candidate"
ETHER_TYPE_NOTE = "Filter to match packets based on the EtherType field in the Ethernet frame. Tags: atp.Status=candidate"
SOURCE_MAC_ADDRESS_NOTE = "Filter to match packets with the source MAC address/ mask. Tags: atp.Status=candidate"
VLAN_ID_NOTE = "Filter of packets with a VlanId. Tags: atp.Status=candidate"
VLAN_PRIORITY_NOTE = "Filter of packets with a Vlan priority. Tags: atp.Status=candidate"


class TestStreamFilterRuleDataLinkLayer:
    def test_inheritance(self):
        assert issubclass(StreamFilterRuleDataLinkLayer, ARObject)

    def test_concrete_class_instantiable(self):
        rule = StreamFilterRuleDataLinkLayer()
        assert isinstance(rule, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(StreamFilterRuleDataLinkLayer.__doc__) == CLASS_NOTE

    def test_initialization(self):
        rule = StreamFilterRuleDataLinkLayer()

        assert rule.getDestinationMacAddress() is None
        assert rule.getEtherType() is None
        assert rule.getSourceMacAddress() is None
        assert rule.getVlanId() is None
        assert rule.getVlanPriority() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "StreamFilterRuleDataLinkLayer")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("destinationMacAddress", "Optional[StreamFilterMACAddress]"),
            ("etherType", "Optional[PositiveInteger]"),
            ("sourceMacAddress", "Optional[StreamFilterMACAddress]"),
            ("vlanId", "Optional[PositiveInteger]"),
            ("vlanPriority", "Optional[PositiveInteger]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.getDestinationMacAddress).get("return") == typing.Optional[StreamFilterMACAddress]
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.setDestinationMacAddress).get("value") == typing.Optional[StreamFilterMACAddress]
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.setDestinationMacAddress).get("return") is StreamFilterRuleDataLinkLayer
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.getEtherType).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.setEtherType).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.setEtherType).get("return") is StreamFilterRuleDataLinkLayer
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.getSourceMacAddress).get("return") == typing.Optional[StreamFilterMACAddress]
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.setSourceMacAddress).get("value") == typing.Optional[StreamFilterMACAddress]
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.setSourceMacAddress).get("return") is StreamFilterRuleDataLinkLayer
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.getVlanId).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.setVlanId).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.setVlanId).get("return") is StreamFilterRuleDataLinkLayer
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.getVlanPriority).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.setVlanPriority).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(StreamFilterRuleDataLinkLayer.setVlanPriority).get("return") is StreamFilterRuleDataLinkLayer

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(StreamFilterRuleDataLinkLayer.getDestinationMacAddress.__doc__) == DESTINATION_MAC_ADDRESS_NOTE
        assert (
            inspect.cleandoc(StreamFilterRuleDataLinkLayer.setDestinationMacAddress.__doc__)
            == DESTINATION_MAC_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing destinationMacAddress."
        )
        assert inspect.cleandoc(StreamFilterRuleDataLinkLayer.getEtherType.__doc__) == ETHER_TYPE_NOTE
        assert inspect.cleandoc(StreamFilterRuleDataLinkLayer.setEtherType.__doc__) == ETHER_TYPE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing etherType."
        assert inspect.cleandoc(StreamFilterRuleDataLinkLayer.getSourceMacAddress.__doc__) == SOURCE_MAC_ADDRESS_NOTE
        assert (
            inspect.cleandoc(StreamFilterRuleDataLinkLayer.setSourceMacAddress.__doc__) == SOURCE_MAC_ADDRESS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing sourceMacAddress."
        )
        assert inspect.cleandoc(StreamFilterRuleDataLinkLayer.getVlanId.__doc__) == VLAN_ID_NOTE
        assert inspect.cleandoc(StreamFilterRuleDataLinkLayer.setVlanId.__doc__) == VLAN_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing vlanId."
        assert inspect.cleandoc(StreamFilterRuleDataLinkLayer.getVlanPriority.__doc__) == VLAN_PRIORITY_NOTE
        assert inspect.cleandoc(StreamFilterRuleDataLinkLayer.setVlanPriority.__doc__) == VLAN_PRIORITY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing vlanPriority."

    def test_get_set_destination_mac_address(self):
        rule = StreamFilterRuleDataLinkLayer()

        value = StreamFilterMACAddress()
        value.setMacAddress(MacAddressString().setValue("02:00:00:00:00:01"))
        value.setMacAddressMask(MacAddressString().setValue("FF:FF:FF:FF:FF:FF"))
        assert rule.setDestinationMacAddress(value) is rule
        assert rule.getDestinationMacAddress() is value
        assert rule.getDestinationMacAddress().getMacAddress().getValue() == "02:00:00:00:00:01"
        assert rule.getDestinationMacAddress().getMacAddressMask().getValue() == "FF:FF:FF:FF:FF:FF"

        assert rule.setDestinationMacAddress(None) is rule
        assert rule.getDestinationMacAddress() is value

    def test_get_set_ether_type(self):
        rule = StreamFilterRuleDataLinkLayer()

        value = PositiveInteger().setValue("2048")
        assert rule.setEtherType(value) is rule
        assert rule.getEtherType() is value
        assert rule.getEtherType().getValue() == 2048

        assert rule.setEtherType(None) is rule
        assert rule.getEtherType() is value

    def test_get_set_source_mac_address(self):
        rule = StreamFilterRuleDataLinkLayer()

        value = StreamFilterMACAddress()
        value.setMacAddress(MacAddressString().setValue("02:00:00:00:00:02"))
        assert rule.setSourceMacAddress(value) is rule
        assert rule.getSourceMacAddress() is value
        assert rule.getSourceMacAddress().getMacAddress().getValue() == "02:00:00:00:00:02"

        assert rule.setSourceMacAddress(None) is rule
        assert rule.getSourceMacAddress() is value

    def test_get_set_vlan_id(self):
        rule = StreamFilterRuleDataLinkLayer()

        value = PositiveInteger().setValue("10")
        assert rule.setVlanId(value) is rule
        assert rule.getVlanId() is value
        assert rule.getVlanId().getValue() == 10

        assert rule.setVlanId(None) is rule
        assert rule.getVlanId() is value

    def test_get_set_vlan_priority(self):
        rule = StreamFilterRuleDataLinkLayer()

        value = PositiveInteger().setValue("5")
        assert rule.setVlanPriority(value) is rule
        assert rule.getVlanPriority() is value
        assert rule.getVlanPriority().getValue() == 5

        assert rule.setVlanPriority(None) is rule
        assert rule.getVlanPriority() is value
