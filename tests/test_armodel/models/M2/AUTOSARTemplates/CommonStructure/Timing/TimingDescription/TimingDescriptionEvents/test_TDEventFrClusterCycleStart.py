from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventCycleStart,
    TDEventFrClusterCycleStart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
)


class TestTDEventFrClusterCycleStart:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_base_is_tdevent_cycle_start(self):
        assert issubclass(TDEventFrClusterCycleStart, TDEventCycleStart)

    def test_defaults(self):
        parent = self._parent()
        event = TDEventFrClusterCycleStart(parent, "E1")
        assert event.getFrClusterRef() is None
        assert event.getCycleRepetition() is None
        assert event.getEcuInstanceRef() is None

    def test_set_get_fr_cluster_ref(self):
        parent = self._parent()
        event = TDEventFrClusterCycleStart(parent, "E1")
        ref = RefType()
        ref.setValue("/Path/To/FlexrayCluster")
        assert event.setFrClusterRef(ref) is event
        assert event.getFrClusterRef() is ref

    def test_set_fr_cluster_ref_none_noop(self):
        parent = self._parent()
        event = TDEventFrClusterCycleStart(parent, "E1")
        ref = RefType()
        ref.setValue("/Path/To/FlexrayCluster")
        event.setFrClusterRef(ref)
        event.setFrClusterRef(None)
        assert event.getFrClusterRef() is ref

    def test_inherited_cycle_repetition(self):
        parent = self._parent()
        event = TDEventFrClusterCycleStart(parent, "E1")
        value = Integer()
        value.setValue(4)
        event.setCycleRepetition(value)
        assert event.getCycleRepetition() is value
