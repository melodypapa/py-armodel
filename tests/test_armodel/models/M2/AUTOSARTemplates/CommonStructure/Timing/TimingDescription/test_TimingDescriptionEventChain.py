import inspect
import re
import typing

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


class TestTimingDescriptionEventChainSpecContract:
    """Table 3.13 (AUTOSAR_CP_TPS_TimingExtensions, p.41) spec contract
    for TimingDescriptionEventChain."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 3.13 Note verbatim (the
        markdown's trailing italic-extraction artifact "event chain segments ."
        — space before the final period, present in both the R23-11 and R4.3.1
        markdown — normalized by dropping the artifact space; the XSD group
        documentation canonicalizes the term as ''event chain segments'').
        """
        assert TimingDescriptionEventChain.__doc__.strip() == (
            "An event chain describes the causal order for a set of functionally dependent timing events. "
            "Each event chain has a well defined stimulus and response, which describe its start and end point. "
            "Furthermore, it can be hierarchically decomposed into an arbitrary number of sub-chains, so called event chain segments."
        )

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert TimingDescriptionEventChain.__init__.__doc__ is None

    def test_base_is_timing_description(self):
        """
        Test that the Base per Table 3.13 is TimingDescription (most-derived —
        the chain aggregates into TimingExtension.timingDescription).
        """
        assert issubclass(TimingDescriptionEventChain, TimingDescription)

    def test_is_pipelining_permitted_typed_optional_boolean(self):
        """
        Test that isPipeliningPermitted (Boolean, 0..1 attr) is an
        Optional[Boolean] accessor pair.
        """
        getter_hints = typing.get_type_hints(TimingDescriptionEventChain.getIsPipeliningPermitted)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(TimingDescriptionEventChain.setIsPipeliningPermitted)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is TimingDescriptionEventChain

    def test_response_stimulus_typed_optional_refs(self):
        """
        Test that response/stimulus (TimingDescriptionEvent, 0..1 ref) are
        Optional[RefType] accessor pairs (Kind-suffix Ref per Rule 0001.5).
        """
        for getter, setter in (
            (TimingDescriptionEventChain.getResponseRef, TimingDescriptionEventChain.setResponseRef),
            (TimingDescriptionEventChain.getStimulusRef, TimingDescriptionEventChain.setStimulusRef),
        ):
            getter_hints = typing.get_type_hints(getter)
            assert getter_hints.get("return") == typing.Optional[RefType]

            setter_hints = typing.get_type_hints(setter)
            assert setter_hints.get("value") == typing.Optional[RefType]
            assert setter_hints.get("return") is TimingDescriptionEventChain

    def test_segment_typed_ref_list(self):
        """
        Test that segment (TimingDescriptionEventChain, * ref) maps to a
        dedicated List[RefType] field with add/get accessors (Kind `*` ref
        plural suffix per Rule 0001.5).
        """
        adder_hints = typing.get_type_hints(TimingDescriptionEventChain.addSegmentRef)
        assert adder_hints.get("value") == typing.Optional[RefType]
        assert adder_hints.get("return") is TimingDescriptionEventChain

        getter_hints = typing.get_type_hints(TimingDescriptionEventChain.getSegmentRefs)
        assert getter_hints.get("return") == typing.List[RefType]

    def test_member_order_matches_markdown_displayed_order(self):
        """
        Test that the __init__ field declaration order follows the Table 3.13
        markdown displayed row order (isPipeliningPermitted → response →
        segment → stimulus) — the XSD sequence order
        (IS-PIPELINING-PERMITTED → STIMULUS-REF → RESPONSE-REF → SEGMENT-REFS)
        governs only the reader/writer XML element order (Rule 0001.11).
        """
        init_source = inspect.getsource(TimingDescriptionEventChain.__init__)
        positions = {name: init_source.index("self.%s:" % name) for name in ("isPipeliningPermitted", "responseRef", "segmentRefs", "stimulusRef")}
        assert positions["isPipeliningPermitted"] < positions["responseRef"]
        assert positions["responseRef"] < positions["segmentRefs"]
        assert positions["segmentRefs"] < positions["stimulusRef"]

    def test_accessor_order_matches_markdown_displayed_order(self):
        """
        Test that the accessor definition order follows the Table 3.13 markdown
        displayed row order (isPipeliningPermitted → response → segment →
        stimulus; get/set per attribute, add/get for the `*` ref list).
        """
        class_source = inspect.getsource(TimingDescriptionEventChain)
        accessors = (
            "getIsPipeliningPermitted",
            "setIsPipeliningPermitted",
            "getResponseRef",
            "setResponseRef",
            "addSegmentRef",
            "getSegmentRefs",
            "getStimulusRef",
            "setStimulusRef",
        )
        assert re.findall(r"def (get\w+|set\w+|add\w+)\(", class_source) == list(accessors)

    def test_getter_docstrings_are_notes_verbatim(self):
        """
        Test that getter docstrings are the Table 3.13 Notes verbatim (the
        Tags tails — atp.Status=draft / xml.sequenceOffset — stay on the
        inline __init__ comments only, per the OffsetTimingConstraint family
        convention).
        """
        assert (
            TimingDescriptionEventChain.getIsPipeliningPermitted.__doc__.strip()
            == 'States whether the scheduled entities in an LET interval shall use pipelined execution or not i.e. "permitted pipelining property" If TRUE, then the scheduled entities must implement pipelining. If FALSE or undefined, no pipelining applies.'
        )
        assert TimingDescriptionEventChain.getResponseRef.__doc__.strip() == "The response event representing the point in time where the event chain is terminated."
        assert TimingDescriptionEventChain.getSegmentRefs.__doc__.strip() == "A composed event chain consists of an arbitrary number of sub-chains."
        assert TimingDescriptionEventChain.getStimulusRef.__doc__.strip() == "The stimulus event representing the point in time where the event chain is activated."

    def test_setter_docstrings_are_notes_with_none_noop(self):
        """
        Test that setter/adder docstrings are the Table 3.13 Notes verbatim
        (Tags tails dropped) plus the None-no-op sentence.
        """
        assert (
            TimingDescriptionEventChain.setIsPipeliningPermitted.__doc__.strip()
            == 'States whether the scheduled entities in an LET interval shall use pipelined execution or not i.e. "permitted pipelining property" If TRUE, then the scheduled entities must implement pipelining. If FALSE or undefined, no pipelining applies. A None value is a no-op and does not overwrite an existing isPipeliningPermitted.'
        )
        assert (
            TimingDescriptionEventChain.setResponseRef.__doc__.strip()
            == "The response event representing the point in time where the event chain is terminated. A None value is a no-op and does not overwrite an existing responseRef."
        )
        assert TimingDescriptionEventChain.addSegmentRef.__doc__.strip() == "A composed event chain consists of an arbitrary number of sub-chains. A None value is a no-op."
        assert (
            TimingDescriptionEventChain.setStimulusRef.__doc__.strip()
            == "The stimulus event representing the point in time where the event chain is activated. A None value is a no-op and does not overwrite an existing stimulusRef."
        )
