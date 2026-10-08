"""Model unit tests for EthernetFrameTriggering (Table 6.230, p.578)."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import EthernetFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FrameTriggering

SPEC_NOTE = "Ethernet specific Frame element."


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestEthernetFrameTriggering:
    def test_initialization_defaults(self):
        parent = MockParent()
        triggering = EthernetFrameTriggering(parent, "eth_frame_triggering")
        assert triggering.getShortName() == "eth_frame_triggering"
        assert isinstance(triggering, FrameTriggering)
        assert triggering.getFrameRef() is None
        assert triggering.getFramePortRefs() == []
        assert triggering.getPduTriggeringRefs() == []

    def test_class_docstring_is_spec_note(self):
        assert EthernetFrameTriggering.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        assert EthernetFrameTriggering.__init__.__doc__ is None

    def test_inherits_frame_triggering(self):
        assert issubclass(EthernetFrameTriggering, FrameTriggering)

    def test_inherited_frame_ref_round_trip(self):
        parent = MockParent()
        triggering = EthernetFrameTriggering(parent, "eth_frame_triggering")
        ref = RefType()
        ref.setValue("/cluster/frames/eth_frame")
        result = triggering.setFrameRef(ref)
        assert result == triggering
        assert triggering.getFrameRef().getValue() == "/cluster/frames/eth_frame"
        triggering.setFrameRef(None)
        assert triggering.getFrameRef().getValue() == "/cluster/frames/eth_frame"

    def test_inherited_frame_port_refs_round_trip(self):
        parent = MockParent()
        triggering = EthernetFrameTriggering(parent, "eth_frame_triggering")
        ref = RefType()
        ref.setValue("/cluster/ecu/port")
        result = triggering.addFramePortRef(ref)
        assert result == triggering
        assert [r.getValue() for r in triggering.getFramePortRefs()] == ["/cluster/ecu/port"]
        triggering.addFramePortRef(None)
        assert len(triggering.getFramePortRefs()) == 1

    def test_inherited_pdu_triggering_refs_round_trip(self):
        parent = MockParent()
        triggering = EthernetFrameTriggering(parent, "eth_frame_triggering")
        ref = RefType()
        ref.setValue("/cluster/ch/pdu_triggering")
        result = triggering.addPduTriggeringRef(ref)
        assert result == triggering
        assert [r.getValue() for r in triggering.getPduTriggeringRefs()] == ["/cluster/ch/pdu_triggering"]
        triggering.addPduTriggeringRef(None)
        assert len(triggering.getPduTriggeringRefs()) == 1
