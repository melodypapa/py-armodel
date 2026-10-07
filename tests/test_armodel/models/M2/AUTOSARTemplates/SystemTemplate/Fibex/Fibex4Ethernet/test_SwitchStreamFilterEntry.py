"""
Test suite for SwitchStreamFilterEntry (CP_TPS_SystemTemplate Table 3.95, p.142, R23-11).

Validates the member defaults, ref-list and setter semantics (None no-ops),
getter/setter round-trips, the verbatim class-level spec Note and the member
declaration order (markdown displayed row order) of the SwitchStreamFilterEntry
model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    SwitchStreamFilterEntry,
)

CLASS_NOTE = "Defines a Stream Filter Entry. Tags: atp.Status=candidate"

ASYNCHRONOUS_TRAFFIC_SHAPER_NOTE = "Reference to the Asynchronous Traffic Shaper (ATS). Tags: atp.Status=candidate"
FILTER_PRIORITY_NOTE = "Defines the Priority of this Stream Filter Entry. Tags: atp.Status=candidate"
FLOW_METERING_NOTE = "Reference to a Flow Metering Entry. Tags: atp.Status=candidate"
MAX_SDU_SIZE_NOTE = "Defines the maximum SDU size (size of an Ethernet package) which is acceptable to be processed by the Ethernet switch. Tags: atp.Status=candidate"
STREAM_GATE_NOTE = "Reference to a Stream Gate Entry. Tags: atp.Status=candidate"
STREAM_IDENTIFICATION_HANDLE_NOTE = "Reference to the SwitchStreamIdentifications this Stream FilterEntry applies to. Tags: atp.Status=candidate"
STREAM_IDENTIFICATION_WILDCARD_NOTE = "Defines whether this Stream Filter Entry includes the wildcard for SwitchStreamIdentification. Tags: atp.Status=candidate"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSwitchStreamFilterEntry:
    def test_inheritance(self):
        assert issubclass(SwitchStreamFilterEntry, Identifiable)

    def test_concrete_class_instantiable(self):
        stream_filter = SwitchStreamFilterEntry(MockParent(), "Filter1")
        assert isinstance(stream_filter, Identifiable)
        assert stream_filter.getShortName() == "Filter1"
        assert stream_filter.getParent() is not None

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SwitchStreamFilterEntry.__doc__) == CLASS_NOTE

    def test_initialization(self):
        stream_filter = SwitchStreamFilterEntry(MockParent(), "Filter1")

        assert stream_filter.getShortName() == "Filter1"
        assert stream_filter.getAsynchronousTrafficShaperRef() is None
        assert stream_filter.getFilterPriority() is None
        assert stream_filter.getFlowMeteringRef() is None
        assert stream_filter.getMaxSduSize() is None
        assert stream_filter.getStreamGateRef() is None
        assert stream_filter.getStreamIdentificationHandleRefs() == []
        assert stream_filter.getStreamIdentificationWildcard() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "SwitchStreamFilterEntry")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("asynchronousTrafficShaperRef", "Optional[RefType]"),
            ("filterPriority", "Optional[PositiveInteger]"),
            ("flowMeteringRef", "Optional[RefType]"),
            ("maxSduSize", "Optional[PositiveInteger]"),
            ("streamGateRef", "Optional[RefType]"),
            ("streamIdentificationHandleRefs", "List[RefType]"),
            ("streamIdentificationWildcard", "Optional[Boolean]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(SwitchStreamFilterEntry.getAsynchronousTrafficShaperRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(SwitchStreamFilterEntry.setAsynchronousTrafficShaperRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(SwitchStreamFilterEntry.setAsynchronousTrafficShaperRef).get("return") is SwitchStreamFilterEntry
        assert typing.get_type_hints(SwitchStreamFilterEntry.getFilterPriority).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchStreamFilterEntry.setFilterPriority).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchStreamFilterEntry.getFlowMeteringRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(SwitchStreamFilterEntry.setFlowMeteringRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(SwitchStreamFilterEntry.getMaxSduSize).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchStreamFilterEntry.setMaxSduSize).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchStreamFilterEntry.getStreamGateRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(SwitchStreamFilterEntry.setStreamGateRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(SwitchStreamFilterEntry.addStreamIdentificationHandleRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(SwitchStreamFilterEntry.addStreamIdentificationHandleRef).get("return") is SwitchStreamFilterEntry
        assert typing.get_type_hints(SwitchStreamFilterEntry.getStreamIdentificationHandleRefs).get("return") == typing.List[RefType]
        assert typing.get_type_hints(SwitchStreamFilterEntry.getStreamIdentificationWildcard).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(SwitchStreamFilterEntry.setStreamIdentificationWildcard).get("value") == typing.Optional[Boolean]

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(SwitchStreamFilterEntry.getAsynchronousTrafficShaperRef.__doc__) == ASYNCHRONOUS_TRAFFIC_SHAPER_NOTE
        assert (
            inspect.cleandoc(SwitchStreamFilterEntry.setAsynchronousTrafficShaperRef.__doc__)
            == ASYNCHRONOUS_TRAFFIC_SHAPER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing asynchronousTrafficShaperRef."
        )
        assert inspect.cleandoc(SwitchStreamFilterEntry.getFilterPriority.__doc__) == FILTER_PRIORITY_NOTE
        assert inspect.cleandoc(SwitchStreamFilterEntry.setFilterPriority.__doc__) == FILTER_PRIORITY_NOTE + "\n\nA None value is a no-op and does not overwrite an existing filterPriority."
        assert inspect.cleandoc(SwitchStreamFilterEntry.getFlowMeteringRef.__doc__) == FLOW_METERING_NOTE
        assert inspect.cleandoc(SwitchStreamFilterEntry.setFlowMeteringRef.__doc__) == FLOW_METERING_NOTE + "\n\nA None value is a no-op and does not overwrite an existing flowMeteringRef."
        assert inspect.cleandoc(SwitchStreamFilterEntry.getMaxSduSize.__doc__) == MAX_SDU_SIZE_NOTE
        assert inspect.cleandoc(SwitchStreamFilterEntry.setMaxSduSize.__doc__) == MAX_SDU_SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing maxSduSize."
        assert inspect.cleandoc(SwitchStreamFilterEntry.getStreamGateRef.__doc__) == STREAM_GATE_NOTE
        assert inspect.cleandoc(SwitchStreamFilterEntry.setStreamGateRef.__doc__) == STREAM_GATE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing streamGateRef."
        assert (
            inspect.cleandoc(SwitchStreamFilterEntry.addStreamIdentificationHandleRef.__doc__)
            == STREAM_IDENTIFICATION_HANDLE_NOTE + "\n\nA None value is a no-op and does not append a streamIdentificationHandleRef."
        )
        assert inspect.cleandoc(SwitchStreamFilterEntry.getStreamIdentificationHandleRefs.__doc__) == STREAM_IDENTIFICATION_HANDLE_NOTE
        assert inspect.cleandoc(SwitchStreamFilterEntry.getStreamIdentificationWildcard.__doc__) == STREAM_IDENTIFICATION_WILDCARD_NOTE
        assert (
            inspect.cleandoc(SwitchStreamFilterEntry.setStreamIdentificationWildcard.__doc__)
            == STREAM_IDENTIFICATION_WILDCARD_NOTE + "\n\nA None value is a no-op and does not overwrite an existing streamIdentificationWildcard."
        )

    def test_get_set_asynchronous_traffic_shaper_ref(self):
        stream_filter = SwitchStreamFilterEntry(MockParent(), "Filter1")

        ref = RefType()
        ref.setValue("/AUTOSAR/Switch/Ats1")
        ref.setDest("COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER")
        assert stream_filter.setAsynchronousTrafficShaperRef(ref) is stream_filter
        assert stream_filter.getAsynchronousTrafficShaperRef() is ref

        assert stream_filter.setAsynchronousTrafficShaperRef(None) is stream_filter
        assert stream_filter.getAsynchronousTrafficShaperRef() is ref

    def test_get_set_filter_priority(self):
        stream_filter = SwitchStreamFilterEntry(MockParent(), "Filter1")

        value = PositiveInteger().setValue("3")
        assert stream_filter.setFilterPriority(value) is stream_filter
        assert stream_filter.getFilterPriority() is value
        assert stream_filter.getFilterPriority().getValue() == 3

        assert stream_filter.setFilterPriority(None) is stream_filter
        assert stream_filter.getFilterPriority() is value

    def test_get_set_flow_metering_ref(self):
        stream_filter = SwitchStreamFilterEntry(MockParent(), "Filter1")

        ref = RefType()
        ref.setValue("/AUTOSAR/Switch/Metering1")
        ref.setDest("SWITCH-FLOW-METERING-ENTRY")
        assert stream_filter.setFlowMeteringRef(ref) is stream_filter
        assert stream_filter.getFlowMeteringRef() is ref

        assert stream_filter.setFlowMeteringRef(None) is stream_filter
        assert stream_filter.getFlowMeteringRef() is ref

    def test_get_set_max_sdu_size(self):
        stream_filter = SwitchStreamFilterEntry(MockParent(), "Filter1")

        value = PositiveInteger().setValue("1522")
        assert stream_filter.setMaxSduSize(value) is stream_filter
        assert stream_filter.getMaxSduSize() is value
        assert stream_filter.getMaxSduSize().getValue() == 1522

        assert stream_filter.setMaxSduSize(None) is stream_filter
        assert stream_filter.getMaxSduSize() is value

    def test_get_set_stream_gate_ref(self):
        stream_filter = SwitchStreamFilterEntry(MockParent(), "Filter1")

        ref = RefType()
        ref.setValue("/AUTOSAR/Switch/Gate1")
        ref.setDest("SWITCH-STREAM-GATE-ENTRY")
        assert stream_filter.setStreamGateRef(ref) is stream_filter
        assert stream_filter.getStreamGateRef() is ref

        assert stream_filter.setStreamGateRef(None) is stream_filter
        assert stream_filter.getStreamGateRef() is ref

    def test_add_get_stream_identification_handle_refs(self):
        stream_filter = SwitchStreamFilterEntry(MockParent(), "Filter1")

        ref = RefType()
        ref.setValue("/AUTOSAR/Switch/Stream1")
        ref.setDest("SWITCH-STREAM-IDENTIFICATION")
        assert stream_filter.addStreamIdentificationHandleRef(ref) is stream_filter
        assert stream_filter.getStreamIdentificationHandleRefs() == [ref]

        assert stream_filter.addStreamIdentificationHandleRef(None) is stream_filter
        assert stream_filter.getStreamIdentificationHandleRefs() == [ref]

        second = RefType()
        second.setValue("/AUTOSAR/Switch/Stream2")
        second.setDest("SWITCH-STREAM-IDENTIFICATION")
        stream_filter.addStreamIdentificationHandleRef(second)
        assert stream_filter.getStreamIdentificationHandleRefs() == [ref, second]

    def test_get_set_stream_identification_wildcard(self):
        stream_filter = SwitchStreamFilterEntry(MockParent(), "Filter1")

        value = Boolean().setValue(True)
        assert stream_filter.setStreamIdentificationWildcard(value) is stream_filter
        assert stream_filter.getStreamIdentificationWildcard() is value
        assert stream_filter.getStreamIdentificationWildcard().getValue() is True

        assert stream_filter.setStreamIdentificationWildcard(None) is stream_filter
        assert stream_filter.getStreamIdentificationWildcard() is value
