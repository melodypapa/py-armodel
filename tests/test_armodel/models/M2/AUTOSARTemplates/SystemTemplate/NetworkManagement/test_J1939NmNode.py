import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import J1939NmAddressConfigurationCapabilityEnum, J1939NmNode, J1939NodeName, NmNode


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_J1939NmNode:
    def test_inheritance_and_concreteness(self):
        # Base row most-derived = NmNode; concrete class per XSD (J-1939-NM-NODE abstract="false")
        node = J1939NmNode(MockParent(), "J1939NmNode")
        assert isinstance(node, NmNode)
        with pytest.raises(TypeError):
            NmNode(MockParent(), "abstract")

    def test_initialization(self):
        node = J1939NmNode(MockParent(), "J1939NmNode")
        assert node.getAddressConfigurationCapability() is None
        assert node.getNodeName() is None

    def test_get_set_address_configuration_capability(self):
        node = J1939NmNode(MockParent(), "J1939NmNode")
        capability = J1939NmAddressConfigurationCapabilityEnum()
        capability.setValue(J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA)
        assert node.setAddressConfigurationCapability(capability) is node
        assert node.getAddressConfigurationCapability() is capability
        node.setAddressConfigurationCapability(None)
        assert node.getAddressConfigurationCapability() is capability

    def test_get_set_node_name(self):
        node = J1939NmNode(MockParent(), "J1939NmNode")
        node_name = J1939NodeName()
        assert node.setNodeName(node_name) is node
        assert node.getNodeName() is node_name
        node.setNodeName(None)
        assert node.getNodeName() is node_name

    def test_docstrings_are_spec_notes_verbatim(self):
        # Table 6.320, p.691 (body rendered above the caption in the markdown)
        assert J1939NmNode.__doc__.strip() == "J1939 specific NM Node attributes."
        capability_note = "Defines the Address Configuration Capability of the J1939NmNode (corresponding to an SAE J1939 Controller Application, CA)."
        assert J1939NmNode.getAddressConfigurationCapability.__doc__.strip() == capability_note
        assert J1939NmNode.setAddressConfigurationCapability.__doc__.strip().split("\n")[0].strip() == capability_note
        # markdown Note has NO trailing period
        assert J1939NmNode.getNodeName.__doc__.strip() == "NodeName configuration"
        assert J1939NmNode.setNodeName.__doc__.strip().split("\n")[0].strip() == "NodeName configuration"
