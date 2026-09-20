import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import AbstractDoIpLogicAddressProps, DoIpLogicTargetAddressProps, DoIpLogicTesterAddressProps, DoIpRoutingActivation


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_DoIp:
    """Test cases for DoIP-related classes."""

    def test_AbstractDoIpLogicAddressProps(self):
        """Test AbstractDoIpLogicAddressProps abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
            AbstractDoIpLogicAddressProps(parent, "test_abstract")

    def test_DoIpLogicTargetAddressProps(self):
        """Test DoIpLogicTargetAddressProps class functionality."""
        parent = MockParent()
        props = DoIpLogicTargetAddressProps(parent, "test_target_addr")

        assert isinstance(props, Identifiable)
        assert isinstance(props, AbstractDoIpLogicAddressProps)

        # Test default values
        assert props.getShortName() == "test_target_addr"

    def test_DoIpLogicTesterAddressProps(self):
        """Test DoIpLogicTesterAddressProps class functionality."""
        parent = MockParent()
        props = DoIpLogicTesterAddressProps(parent, "test_tester_addr")

        assert isinstance(props, Identifiable)
        assert isinstance(props, AbstractDoIpLogicAddressProps)

        # Test default values
        assert props.getDoIpTesterRoutingActivationRef() is None

        # Test setter/getter
        mock_ref = "mock_ref"
        props.setDoIpTesterRoutingActivationRef(mock_ref)
        assert props.getDoIpTesterRoutingActivationRef() == mock_ref


@pytest.fixture(autouse=True)
def reset_autosar_for_doip_routing_activation():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class Test_DoIpRoutingActivation:
    """Test cases for DoIpRoutingActivation (Table 6.204, p.553)."""

    MEMBERS = [
        "doIpTargetAddressRefs",
    ]

    def _create(self, short_name: str) -> DoIpRoutingActivation:
        parent = AUTOSAR.getInstance().createARPackage("DoIpRoutingActivationPkg")
        return DoIpRoutingActivation(parent, short_name)

    def test_inheritance(self):
        assert issubclass(DoIpRoutingActivation, Identifiable)

    def test_class_docstring_note(self):
        expected = "This meta-class defines a DoIP routing activation possibility that activates the routing to the referenced doIPTargetAddress. This means that the diagnostic request messages related to the specified doIPTargetAddress received by socketConnections that are referenced by the same DoIpInterface that aggregates this DoIpRoutingActivation are activated."
        assert inspect.cleandoc(DoIpRoutingActivation.__doc__) == expected

    def test_initialization_defaults(self):
        activation = self._create("Activation1")
        assert activation.getShortName() == "Activation1"
        assert activation.getDoIpTargetAddressRefs() == []

    def test_member_order(self):
        activation = self._create("Activation1")
        members = [k for k in vars(activation) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_do_ip_target_address_ref(self):
        activation = self._create("Activation1")
        ref = RefType()
        ref.setValue("/DoIp/DoIpLogicTargetAddressProps1")
        ref.setDest("DO-IP-LOGIC-TARGET-ADDRESS-PROPS")
        result = activation.addDoIpTargetAddressRef(ref)
        assert result is activation
        assert activation.getDoIpTargetAddressRefs() == [ref]
        activation.addDoIpTargetAddressRef(None)
        assert activation.getDoIpTargetAddressRefs() == [ref]
