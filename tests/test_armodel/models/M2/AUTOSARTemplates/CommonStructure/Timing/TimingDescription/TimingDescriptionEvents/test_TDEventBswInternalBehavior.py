from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBswInternalBehavior import (
    TDEventBswInternalBehavior,
    TDEventBswInternalBehaviorTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TestTDEventBswInternalBehavior:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_base_is_timing_description_event(self):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
            TimingDescriptionEvent,
        )

        assert issubclass(TDEventBswInternalBehavior, TimingDescriptionEvent)

    def test_defaults(self):
        parent = self._parent()
        event = TDEventBswInternalBehavior(parent, "E1")
        assert event.getBswModuleEntityRef() is None
        assert event.getTdEventBswInternalBehaviorType() is None

    def test_set_get_bsw_module_entity_ref(self):
        parent = self._parent()
        event = TDEventBswInternalBehavior(parent, "E1")
        ref = RefType()
        ref.setValue("/Path/To/BswModuleEntity")
        assert event.setBswModuleEntityRef(ref) is event
        assert event.getBswModuleEntityRef() is ref

    def test_set_bsw_module_entity_ref_none_noop(self):
        parent = self._parent()
        event = TDEventBswInternalBehavior(parent, "E1")
        ref = RefType()
        ref.setValue("/Path/To/BswModuleEntity")
        event.setBswModuleEntityRef(ref)
        event.setBswModuleEntityRef(None)
        assert event.getBswModuleEntityRef() is ref

    def test_set_get_td_event_bsw_internal_behavior_type(self):
        parent = self._parent()
        event = TDEventBswInternalBehavior(parent, "E1")
        enum = TDEventBswInternalBehaviorTypeEnum()
        enum.setValue(TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_ACTIVATED)
        assert event.setTdEventBswInternalBehaviorType(enum) is event
        assert event.getTdEventBswInternalBehaviorType() is enum
        assert event.getTdEventBswInternalBehaviorType().getValue() == "bswModuleEntityActivated"

    def test_set_td_event_bsw_internal_behavior_type_none_noop(self):
        parent = self._parent()
        event = TDEventBswInternalBehavior(parent, "E1")
        enum = TDEventBswInternalBehaviorTypeEnum()
        enum.setValue(TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_STARTED)
        event.setTdEventBswInternalBehaviorType(enum)
        event.setTdEventBswInternalBehaviorType(None)
        assert event.getTdEventBswInternalBehaviorType() is enum
