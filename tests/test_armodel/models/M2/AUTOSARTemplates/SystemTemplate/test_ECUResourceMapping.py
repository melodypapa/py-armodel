from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import CommunicationControllerMapping, ECUMapping


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


CCM_NOTE = (
    "CommunicationControllerMapping specifies the CommunicationPeripheral hardware "
    "(defined in the ECU Resource Template) to realize the specified "
    "CommunicationController in a physical topology."
)
CCM_CONTROLLER_NOTE = "Reference to the CommunicationController in the System Template"
CCM_HW_NOTE = "Reference to a HwElement of category CommunicationController in the ECU Resource Template."


class Test_CommunicationControllerMapping:
    """Test cases for CommunicationControllerMapping class (Table 3.134, p.183)."""

    def test_is_concrete_ar_object_subclass(self):
        assert issubclass(CommunicationControllerMapping, ARObject)
        assert not issubclass(CommunicationControllerMapping, Identifiable)
        mapping = CommunicationControllerMapping()
        assert isinstance(mapping, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert CommunicationControllerMapping.__doc__ == CCM_NOTE

    def test_init_has_no_docstring(self):
        assert CommunicationControllerMapping.__init__.__doc__ is None

    def test_defaults(self):
        mapping = CommunicationControllerMapping()
        assert mapping.getCommunicationControllerRef() is None
        assert mapping.getHwCommunicationControllerRef() is None

    def test_communication_controller_ref_round_trip(self):
        mapping = CommunicationControllerMapping()
        ref = _ref("COMMUNICATION-CONTROLLER", "/System/Controllers/Ctrl1")
        assert mapping.setCommunicationControllerRef(ref) is mapping
        assert mapping.getCommunicationControllerRef() is ref

    def test_hw_communication_controller_ref_round_trip(self):
        mapping = CommunicationControllerMapping()
        ref = _ref("HW-ELEMENT", "/EcuResource/HwElements/Mcu")
        assert mapping.setHwCommunicationControllerRef(ref) is mapping
        assert mapping.getHwCommunicationControllerRef() is ref

    def test_setter_none_is_no_op(self):
        mapping = CommunicationControllerMapping()
        controller_ref = _ref("COMMUNICATION-CONTROLLER", "/System/Controllers/Ctrl1")
        hw_ref = _ref("HW-ELEMENT", "/EcuResource/HwElements/Mcu")
        mapping.setCommunicationControllerRef(controller_ref)
        mapping.setHwCommunicationControllerRef(hw_ref)
        assert mapping.setCommunicationControllerRef(None) is mapping
        assert mapping.setHwCommunicationControllerRef(None) is mapping
        assert mapping.getCommunicationControllerRef() is controller_ref
        assert mapping.getHwCommunicationControllerRef() is hw_ref

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        def norm(doc):
            return " ".join(doc.split())

        assert norm(CommunicationControllerMapping.getCommunicationControllerRef.__doc__) == CCM_CONTROLLER_NOTE
        assert norm(CommunicationControllerMapping.setCommunicationControllerRef.__doc__) == (
            CCM_CONTROLLER_NOTE + " A None value is a no-op and does not overwrite an existing communicationControllerRef."
        )
        assert norm(CommunicationControllerMapping.getHwCommunicationControllerRef.__doc__) == CCM_HW_NOTE
        assert norm(CommunicationControllerMapping.setHwCommunicationControllerRef.__doc__) == (
            CCM_HW_NOTE + " A None value is a no-op and does not overwrite an existing hwCommunicationControllerRef."
        )


class Test_ECUMapping:
    """Test cases for ECUMapping class."""

    def test_ECUMapping(self):
        """Test ECUMapping class functionality."""
        parent = MockParent()
        mapping = ECUMapping(parent, "test_ecu_mapping")

        assert isinstance(mapping, Identifiable)

        # Test default values
        assert mapping.getCommControllerMappings() == []
        assert mapping.getEcuRef() is None
        assert mapping.getEcuInstanceRef() is None
        assert mapping.getHwPortMappings() == []

        # Test setter/getter methods
        mock_comm_controller = "mock_comm_controller"
        mapping.setCommControllerMappings([mock_comm_controller])
        assert mapping.getCommControllerMappings() == [mock_comm_controller]

        mock_ecu_ref = "mock_ecu_ref"
        mapping.setEcuRef(mock_ecu_ref)
        assert mapping.getEcuRef() == mock_ecu_ref

        mock_ecu_instance_ref = "mock_ecu_instance_ref"
        mapping.setEcuInstanceRef(mock_ecu_instance_ref)
        assert mapping.getEcuInstanceRef() == mock_ecu_instance_ref

        mock_hw_port = "mock_hw_port"
        mapping.setHwPortMappings([mock_hw_port])
        assert mapping.getHwPortMappings() == [mock_hw_port]
