from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import (
    DataLinkLayerRule,
)


class TestDataLinkLayerRule:
    def test_defaults(self):
        obj = DataLinkLayerRule()
        assert obj.getEtherType() is None
        assert obj.getDestinationMacAddress() is None
        assert obj.getDestinationMacAddressMask() is None
        assert obj.getSourceMacAddress() is None
        assert obj.getSourceMacAddressMask() is None
        assert obj.getVlanId() is None
        assert obj.getVlanPriority() is None

    def test_set_get_ether_type(self):
        obj = DataLinkLayerRule()
        assert obj.setEtherType("0x0800") is obj
        assert obj.getEtherType() == "0x0800"

    def test_set_get_mac_addresses(self):
        obj = DataLinkLayerRule()
        assert obj.setDestinationMacAddress("FF:FF:FF:FF:FF:FF") is obj
        assert obj.getDestinationMacAddress() == "FF:FF:FF:FF:FF:FF"
        assert obj.setDestinationMacAddressMask("FF:00:00:00:00:00") is obj
        assert obj.getDestinationMacAddressMask() == "FF:00:00:00:00:00"
        assert obj.setSourceMacAddress("AA:AA:AA:AA:AA:AA") is obj
        assert obj.getSourceMacAddress() == "AA:AA:AA:AA:AA:AA"
        assert obj.setSourceMacAddressMask("FF:00:00:00:00:00") is obj
        assert obj.getSourceMacAddressMask() == "FF:00:00:00:00:00"

    def test_set_get_vlan(self):
        obj = DataLinkLayerRule()
        assert obj.setVlanId("100") is obj
        assert obj.getVlanId() == "100"
        assert obj.setVlanPriority("3") is obj
        assert obj.getVlanPriority() == "3"

    def test_overwrite(self):
        obj = DataLinkLayerRule()
        obj.setEtherType("0x0800")
        obj.setEtherType("0x86DD")
        assert obj.getEtherType() == "0x86DD"
