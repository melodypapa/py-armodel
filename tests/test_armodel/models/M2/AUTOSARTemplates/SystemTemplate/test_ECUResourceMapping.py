from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import CommunicationControllerMapping, ECUMapping, HwPortMapping


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
ECU_NOTE = "ECUMapping allows to assign an ECU hardware type (defined in the ECU Resource " "Template) to an ECUInstance used in a physical topology."


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
    """Test cases for ECUMapping class (Table 3.133, p.182)."""

    def _mapping(self):
        return ECUMapping(MockParent(), "test_ecu_mapping")

    def test_is_identifiable_variation_point_capable_subclass(self):
        assert issubclass(ECUMapping, Identifiable)
        assert issubclass(ECUMapping, VariationPointCapable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert ECUMapping.__doc__ == ECU_NOTE

    def test_init_has_no_docstring(self):
        assert ECUMapping.__init__.__doc__ is None

    def test_defaults_in_spec_displayed_order(self):
        mapping = self._mapping()
        assert list(mapping.__dict__)[-4:] == ["commControllerMappings", "ecuRef", "ecuInstanceRef", "hwPortMappings"]
        assert mapping.getCommControllerMappings() == []
        assert mapping.getEcuRef() is None
        assert mapping.getEcuInstanceRef() is None
        assert mapping.getHwPortMappings() == []

    def test_ecu_ref_round_trip(self):
        mapping = self._mapping()
        ref = _ref("HW-ELEMENT", "/EcuResource/HwElements/Ecu1")
        assert mapping.setEcuRef(ref) is mapping
        assert mapping.getEcuRef() is ref

    def test_ecu_instance_ref_round_trip(self):
        mapping = self._mapping()
        ref = _ref("ECU-INSTANCE", "/System/EcuInstances/EcuInst1")
        assert mapping.setEcuInstanceRef(ref) is mapping
        assert mapping.getEcuInstanceRef() is ref

    def test_ref_setter_none_is_no_op(self):
        mapping = self._mapping()
        ecu_ref = _ref("HW-ELEMENT", "/EcuResource/HwElements/Ecu1")
        ecu_instance_ref = _ref("ECU-INSTANCE", "/System/EcuInstances/EcuInst1")
        mapping.setEcuRef(ecu_ref)
        mapping.setEcuInstanceRef(ecu_instance_ref)
        assert mapping.setEcuRef(None) is mapping
        assert mapping.setEcuInstanceRef(None) is mapping
        assert mapping.getEcuRef() is ecu_ref
        assert mapping.getEcuInstanceRef() is ecu_instance_ref

    def test_aggregation_list_setters_round_trip(self):
        mapping = self._mapping()
        ccm = CommunicationControllerMapping()
        hpm = HwPortMapping()
        assert mapping.setCommControllerMappings([ccm]) is mapping
        assert mapping.getCommControllerMappings() == [ccm]
        assert mapping.setHwPortMappings([hpm]) is mapping
        assert mapping.getHwPortMappings() == [hpm]

    def test_add_comm_controller_mapping_appends_none_no_op_returns_self(self):
        mapping = self._mapping()
        ccm1 = CommunicationControllerMapping()
        ccm2 = CommunicationControllerMapping()
        assert mapping.addCommControllerMapping(ccm1) is mapping
        assert mapping.addCommControllerMapping(ccm2) is mapping
        assert mapping.getCommControllerMappings() == [ccm1, ccm2]
        assert mapping.addCommControllerMapping(None) is mapping
        assert mapping.getCommControllerMappings() == [ccm1, ccm2]

    def test_add_hw_port_mapping_appends_none_no_op_returns_self(self):
        mapping = self._mapping()
        hpm1 = HwPortMapping()
        hpm2 = HwPortMapping()
        assert mapping.addHwPortMapping(hpm1) is mapping
        assert mapping.addHwPortMapping(hpm2) is mapping
        assert mapping.getHwPortMappings() == [hpm1, hpm2]
        assert mapping.addHwPortMapping(None) is mapping
        assert mapping.getHwPortMappings() == [hpm1, hpm2]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        def norm(doc):
            return " ".join(doc.split())

        comm_note = "The ECUMapping contains the mapping of all CommunicationControllers of the ECU."
        port_note = "The ECUMapping contains the mapping of all HW Communication Ports of the ECU."
        ecu_note = "Reference to a HwElement of category ECU in the ECU Resource Template."
        ecu_instance_note = "Reference to the EcuInstance in the System Template"
        assert norm(ECUMapping.getEcuRef.__doc__) == ecu_note
        assert norm(ECUMapping.setEcuRef.__doc__) == (ecu_note + " A None value is a no-op and does not overwrite an existing ecuRef.")
        assert norm(ECUMapping.getEcuInstanceRef.__doc__) == ecu_instance_note
        assert norm(ECUMapping.setEcuInstanceRef.__doc__) == (ecu_instance_note + " A None value is a no-op and does not overwrite an existing ecuInstanceRef.")
        assert norm(ECUMapping.getCommControllerMappings.__doc__) == comm_note
        assert norm(ECUMapping.setCommControllerMappings.__doc__) == (comm_note + " A None value is a no-op and does not overwrite an existing commControllerMappings list.")
        assert norm(ECUMapping.addCommControllerMapping.__doc__) == (comm_note + " A None value does not extend the commControllerMappings list.")
        assert norm(ECUMapping.getHwPortMappings.__doc__) == port_note
        assert norm(ECUMapping.setHwPortMappings.__doc__) == (port_note + " A None value is a no-op and does not overwrite an existing hwPortMappings list.")
        assert norm(ECUMapping.addHwPortMapping.__doc__) == (port_note + " A None value does not extend the hwPortMappings list.")


HPM_NOTE = "HWPortMapping specifies the hwCommunicationPort (defined in the ECU Resource " "Template) to realize the specified CommunicationConnector in a physical topology."
HPM_CONNECTOR_NOTE = "Reference to the CommunicationConnector in the System Template"
HPM_PORT_NOTE = "Reference to the HwPinPortGroup of category CommunicationPort. " "The connection to the HwCommunicationController is described in the Ecu Resource Description."


class Test_HwPortMapping:
    """Test cases for HwPortMapping class (Table 3.135, p.183)."""

    def test_is_concrete_ar_object_subclass(self):
        assert issubclass(HwPortMapping, ARObject)
        assert not issubclass(HwPortMapping, Identifiable)
        mapping = HwPortMapping()
        assert isinstance(mapping, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert HwPortMapping.__doc__ == HPM_NOTE

    def test_init_has_no_docstring(self):
        assert HwPortMapping.__init__.__doc__ is None

    def test_defaults(self):
        mapping = HwPortMapping()
        assert mapping.getCommunicationConnectorRef() is None
        assert mapping.getHwCommunicationPortRef() is None

    def test_communication_connector_ref_round_trip(self):
        mapping = HwPortMapping()
        ref = _ref("COMMUNICATION-CONNECTOR", "/System/Connectors/Conn1")
        assert mapping.setCommunicationConnectorRef(ref) is mapping
        assert mapping.getCommunicationConnectorRef() is ref

    def test_hw_communication_port_ref_round_trip(self):
        mapping = HwPortMapping()
        ref = _ref("HW-PIN-GROUP", "/EcuResource/HwPinGroups/Port1")
        assert mapping.setHwCommunicationPortRef(ref) is mapping
        assert mapping.getHwCommunicationPortRef() is ref

    def test_setter_none_is_no_op(self):
        mapping = HwPortMapping()
        connector_ref = _ref("COMMUNICATION-CONNECTOR", "/System/Connectors/Conn1")
        port_ref = _ref("HW-PIN-GROUP", "/EcuResource/HwPinGroups/Port1")
        mapping.setCommunicationConnectorRef(connector_ref)
        mapping.setHwCommunicationPortRef(port_ref)
        assert mapping.setCommunicationConnectorRef(None) is mapping
        assert mapping.setHwCommunicationPortRef(None) is mapping
        assert mapping.getCommunicationConnectorRef() is connector_ref
        assert mapping.getHwCommunicationPortRef() is port_ref

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        def norm(doc):
            return " ".join(doc.split())

        assert norm(HwPortMapping.getCommunicationConnectorRef.__doc__) == HPM_CONNECTOR_NOTE
        assert norm(HwPortMapping.setCommunicationConnectorRef.__doc__) == (HPM_CONNECTOR_NOTE + " A None value is a no-op and does not overwrite an existing communicationConnectorRef.")
        assert norm(HwPortMapping.getHwCommunicationPortRef.__doc__) == HPM_PORT_NOTE
        assert norm(HwPortMapping.setHwCommunicationPortRef.__doc__) == (HPM_PORT_NOTE + " A None value is a no-op and does not overwrite an existing hwCommunicationPortRef.")
