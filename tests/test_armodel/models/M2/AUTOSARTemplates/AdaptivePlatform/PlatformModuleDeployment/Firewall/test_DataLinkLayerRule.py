import inspect
import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import DataLinkLayerRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString, PositiveInteger


def _mac(value):
    m = MacAddressString()
    m.setValue(value)
    return m


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


class TestDataLinkLayerRule:
    def test_defaults_in_spec_displayed_order(self):
        obj = DataLinkLayerRule()
        assert isinstance(obj, ARObject)
        assert obj.getDestinationMacAddress() is None
        assert obj.getDestinationMacAddressMask() is None
        assert obj.getEtherType() is None
        assert obj.getSourceMacAddress() is None
        assert obj.getSourceMacAddressMask() is None
        assert obj.getVlanId() is None
        assert obj.getVlanPriority() is None

    def test_get_set_round_trip_and_none_noop(self):
        obj = DataLinkLayerRule()
        dest = _mac("FF:FF:FF:FF:FF:FF")
        dest_mask = _mac("FF:00:00:00:00:00")
        ether_type = _pos_int(2048)
        source = _mac("AA:BB:CC:DD:EE:FF")
        source_mask = _mac("FF:FF:00:00:00:00")
        vlan_id = _pos_int(100)
        vlan_priority = _pos_int(3)

        assert obj.setDestinationMacAddress(dest) is obj
        assert obj.setDestinationMacAddressMask(dest_mask) is obj
        assert obj.setEtherType(ether_type) is obj
        assert obj.setSourceMacAddress(source) is obj
        assert obj.setSourceMacAddressMask(source_mask) is obj
        assert obj.setVlanId(vlan_id) is obj
        assert obj.setVlanPriority(vlan_priority) is obj

        assert obj.getDestinationMacAddress() is dest
        assert obj.getDestinationMacAddressMask() is dest_mask
        assert obj.getEtherType() is ether_type
        assert obj.getSourceMacAddress() is source
        assert obj.getSourceMacAddressMask() is source_mask
        assert obj.getVlanId() is vlan_id
        assert obj.getVlanPriority() is vlan_priority

        obj.setDestinationMacAddress(None)
        obj.setDestinationMacAddressMask(None)
        obj.setEtherType(None)
        obj.setSourceMacAddress(None)
        obj.setSourceMacAddressMask(None)
        obj.setVlanId(None)
        obj.setVlanPriority(None)
        assert obj.getDestinationMacAddress() is dest
        assert obj.getDestinationMacAddressMask() is dest_mask
        assert obj.getEtherType() is ether_type
        assert obj.getSourceMacAddress() is source
        assert obj.getSourceMacAddressMask() is source_mask
        assert obj.getVlanId() is vlan_id
        assert obj.getVlanPriority() is vlan_priority

    def test_overwrite(self):
        obj = DataLinkLayerRule()
        obj.setEtherType(_pos_int(2048))
        obj.setEtherType(_pos_int(34525))
        assert obj.getEtherType().getValue() == 34525

    def test_init_has_no_docstring(self):
        assert DataLinkLayerRule.__init__.__doc__ is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DataLinkLayerRule.__doc__.strip() == "Configuration of filter rules on the DataLink layer Tags: atp.Status=candidate"

    def test_docstrings_are_spec_note_verbatim(self):
        dest_note = "Filter to match packets with the destination MAC address."
        assert inspect.cleandoc(DataLinkLayerRule.getDestinationMacAddress.__doc__) == dest_note
        assert inspect.cleandoc(DataLinkLayerRule.setDestinationMacAddress.__doc__) == dest_note + "\nA None value is a no-op and does not overwrite an existing destinationMacAddress."
        dest_mask_note = "Filter to match packets with the destination MAC address range. The destinationMacAddress with the destinationMacAddressMask defines the MAC address range."
        assert inspect.cleandoc(DataLinkLayerRule.getDestinationMacAddressMask.__doc__) == dest_mask_note
        assert inspect.cleandoc(DataLinkLayerRule.setDestinationMacAddressMask.__doc__) == dest_mask_note + "\nA None value is a no-op and does not overwrite an existing destinationMacAddressMask."
        ether_note = "Filter to match packets based on the EtherType field in the Ethernet frame. The EtherType is used to indicate which protocol is encapsulated in the payload of the frame."
        assert inspect.cleandoc(DataLinkLayerRule.getEtherType.__doc__) == ether_note
        assert inspect.cleandoc(DataLinkLayerRule.setEtherType.__doc__) == ether_note + "\nA None value is a no-op and does not overwrite an existing etherType."
        source_note = "Filter to match packets with the source MAC address."
        assert inspect.cleandoc(DataLinkLayerRule.getSourceMacAddress.__doc__) == source_note
        assert inspect.cleandoc(DataLinkLayerRule.setSourceMacAddress.__doc__) == source_note + "\nA None value is a no-op and does not overwrite an existing sourceMacAddress."
        source_mask_note = "Filter to match packets with the source MAC address range. The sourceMacAddress with the sourceMacAddressMask defines the MAC address range."
        assert inspect.cleandoc(DataLinkLayerRule.getSourceMacAddressMask.__doc__) == source_mask_note
        assert inspect.cleandoc(DataLinkLayerRule.setSourceMacAddressMask.__doc__) == source_mask_note + "\nA None value is a no-op and does not overwrite an existing sourceMacAddressMask."
        vlan_id_note = "Filter of packets with a specific VlanId."
        assert inspect.cleandoc(DataLinkLayerRule.getVlanId.__doc__) == vlan_id_note
        assert inspect.cleandoc(DataLinkLayerRule.setVlanId.__doc__) == vlan_id_note + "\nA None value is a no-op and does not overwrite an existing vlanId."
        vlan_priority_note = "Filter of packets with a specific Vlan priority."
        assert inspect.cleandoc(DataLinkLayerRule.getVlanPriority.__doc__) == vlan_priority_note
        assert inspect.cleandoc(DataLinkLayerRule.setVlanPriority.__doc__) == vlan_priority_note + "\nA None value is a no-op and does not overwrite an existing vlanPriority."

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(DataLinkLayerRule.setDestinationMacAddress)
        assert hints["return"] is DataLinkLayerRule
        assert hints["value"] == Optional[MacAddressString]
        hints = typing.get_type_hints(DataLinkLayerRule.setEtherType)
        assert hints["return"] is DataLinkLayerRule
        assert hints["value"] == Optional[PositiveInteger]
