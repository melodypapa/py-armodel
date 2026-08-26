from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescription,
    TimingDescriptionEventChain,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)


class TestTimingDescriptionEventChain:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_base_is_timing_description(self):
        assert issubclass(TimingDescriptionEventChain, TimingDescription)

    def test_initialization_defaults(self):
        chain = TimingDescriptionEventChain(self._parent(), "Chain1")
        assert chain.getShortName() == "Chain1"
        assert chain.getIsPipeliningPermitted() is None
        assert chain.getStimulusRef() is None
        assert chain.getResponseRef() is None
        assert chain.getSegmentRefs() == []

    def test_get_set_is_pipelining_permitted(self):
        chain = TimingDescriptionEventChain(self._parent(), "Chain1")
        value = Boolean().setValue(True)
        assert chain.setIsPipeliningPermitted(value) is chain
        assert chain.getIsPipeliningPermitted() is value
        assert chain.getIsPipeliningPermitted().getValue() is True
        chain.setIsPipeliningPermitted(None)
        assert chain.getIsPipeliningPermitted() is value

    def test_get_set_stimulus_ref(self):
        chain = TimingDescriptionEventChain(self._parent(), "Chain1")
        ref = RefType().setValue("/AUTOSAR/Stimulus").setDest("TD-EVENT-VFB")
        assert chain.setStimulusRef(ref) is chain
        assert chain.getStimulusRef() is ref
        chain.setStimulusRef(None)
        assert chain.getStimulusRef() is ref

    def test_get_set_response_ref(self):
        chain = TimingDescriptionEventChain(self._parent(), "Chain1")
        ref = RefType().setValue("/AUTOSAR/Response").setDest("TD-EVENT-VFB")
        assert chain.setResponseRef(ref) is chain
        assert chain.getResponseRef() is ref
        chain.setResponseRef(None)
        assert chain.getResponseRef() is ref

    def test_add_segment_ref_appends(self):
        chain = TimingDescriptionEventChain(self._parent(), "Chain1")
        ref1 = RefType().setValue("/AUTOSAR/Seg1").setDest("TIMING-DESCRIPTION-EVENT-CHAIN")
        ref2 = RefType().setValue("/AUTOSAR/Seg2").setDest("TIMING-DESCRIPTION-EVENT-CHAIN")
        assert chain.addSegmentRef(ref1) is chain
        assert chain.addSegmentRef(ref2) is chain
        assert chain.getSegmentRefs() == [ref1, ref2]

    def test_add_segment_ref_none_is_no_op(self):
        chain = TimingDescriptionEventChain(self._parent(), "Chain1")
        ref = RefType().setValue("/AUTOSAR/Seg1").setDest("TIMING-DESCRIPTION-EVENT-CHAIN")
        chain.addSegmentRef(ref)
        chain.addSegmentRef(None)
        assert len(chain.getSegmentRefs()) == 1
