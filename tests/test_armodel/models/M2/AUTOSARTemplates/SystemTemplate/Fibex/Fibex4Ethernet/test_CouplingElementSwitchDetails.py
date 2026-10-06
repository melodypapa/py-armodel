"""
Test suite for CouplingElementSwitchDetails (CP_TPS_SystemTemplate Table 3.83, p.133, R23-11).

Validates the member defaults, factory semantics (duplicate short name returns
the existing element), getter round-trips, the verbatim class-level spec Note
and the member declaration order (markdown displayed row order) of the
CouplingElementSwitchDetails model class.
"""

import ast
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    SwitchAsynchronousTrafficShaperGroupEntry,
    SwitchFlowMeteringEntry,
    SwitchStreamGateEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElementAbstractDetails,
    CouplingElementSwitchDetails,
    SwitchStreamFilterEntry,
    SwitchStreamIdentification,
)

CLASS_NOTE = "Collection of specific details for the CouplingElement of couplingType switch. " "Tags: atp.Status=candidate atp.recommendedPackage=SwitchStreamIdentificationTables"

MEMBER_NOTES = {
    "flowMetering": "Collection of Flow Metering Entries. Tags: atp.Status=candidate",
    "streamFilter": "Collection of Stream Filter Entries. Tags: atp.Status=candidate",
    "streamGate": "Collection of Stream Gate Entries. Tags: atp.Status=candidate",
    "switchStreamIdentification": "Collection of switch stream identification entries. Tags: atp.Status=candidate",
    "trafficShaperGroup": "Collection of Traffic Shaper Groups. Tags: atp.Status=candidate",
}


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestCouplingElementSwitchDetails:
    def test_inheritance(self):
        assert issubclass(CouplingElementSwitchDetails, CouplingElementAbstractDetails)

    def test_concrete_class_instantiable(self):
        details = CouplingElementSwitchDetails(MockParent(), "SwitchDetails")
        assert isinstance(details, CouplingElementAbstractDetails)
        assert details.getShortName() == "SwitchDetails"
        assert details.getParent() is not None

    def test_class_docstring_note(self):
        assert inspect.cleandoc(CouplingElementSwitchDetails.__doc__) == CLASS_NOTE

    def test_initialization(self):
        details = CouplingElementSwitchDetails(MockParent(), "SwitchDetails")

        assert details.getShortName() == "SwitchDetails"
        assert details.getFlowMeterings() == []
        assert details.getStreamFilters() == []
        assert details.getStreamGates() == []
        assert details.getSwitchStreamIdentifications() == []
        assert details.getTrafficShaperGroups() == []

    def test_member_annotations_and_declaration_order(self):
        import importlib

        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "CouplingElementSwitchDetails")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("flowMeterings", "List[SwitchFlowMeteringEntry]"),
            ("streamFilters", "List[SwitchStreamFilterEntry]"),
            ("streamGates", "List[SwitchStreamGateEntry]"),
            ("switchStreamIdentifications", "List[SwitchStreamIdentification]"),
            ("trafficShaperGroups", "List[SwitchAsynchronousTrafficShaperGroupEntry]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(CouplingElementSwitchDetails.createFlowMetering).get("return") is SwitchFlowMeteringEntry
        assert typing.get_type_hints(CouplingElementSwitchDetails.getFlowMeterings).get("return") == typing.List[SwitchFlowMeteringEntry]
        assert typing.get_type_hints(CouplingElementSwitchDetails.createStreamFilter).get("return") is SwitchStreamFilterEntry
        assert typing.get_type_hints(CouplingElementSwitchDetails.getStreamFilters).get("return") == typing.List[SwitchStreamFilterEntry]
        assert typing.get_type_hints(CouplingElementSwitchDetails.createStreamGate).get("return") is SwitchStreamGateEntry
        assert typing.get_type_hints(CouplingElementSwitchDetails.getStreamGates).get("return") == typing.List[SwitchStreamGateEntry]
        assert typing.get_type_hints(CouplingElementSwitchDetails.createSwitchStreamIdentification).get("return") is SwitchStreamIdentification
        assert typing.get_type_hints(CouplingElementSwitchDetails.getSwitchStreamIdentifications).get("return") == typing.List[SwitchStreamIdentification]
        assert typing.get_type_hints(CouplingElementSwitchDetails.createTrafficShaperGroup).get("return") is SwitchAsynchronousTrafficShaperGroupEntry
        assert typing.get_type_hints(CouplingElementSwitchDetails.getTrafficShaperGroups).get("return") == typing.List[SwitchAsynchronousTrafficShaperGroupEntry]

    def test_member_docstrings_are_verbatim_spec_notes(self):
        for attr, note in MEMBER_NOTES.items():
            factory = "create%s%s" % (attr[0].upper(), attr[1:])
            getter = "get%s%ss" % (attr[0].upper(), attr[1:])
            assert inspect.cleandoc(getattr(CouplingElementSwitchDetails, factory).__doc__).startswith(note), attr
            assert inspect.cleandoc(getattr(CouplingElementSwitchDetails, getter).__doc__) == note, attr

    def test_create_flow_metering(self):
        details = CouplingElementSwitchDetails(MockParent(), "SwitchDetails")

        entry = details.createFlowMetering("Metering1")
        assert isinstance(entry, SwitchFlowMeteringEntry)
        assert entry.getShortName() == "Metering1"
        assert details.getFlowMeterings() == [entry]

        duplicate = details.createFlowMetering("Metering1")
        assert duplicate is entry
        assert len(details.getFlowMeterings()) == 1

        second = details.createFlowMetering("Metering2")
        assert details.getFlowMeterings() == [entry, second]

    def test_create_stream_filter(self):
        details = CouplingElementSwitchDetails(MockParent(), "SwitchDetails")

        entry = details.createStreamFilter("Filter1")
        assert isinstance(entry, SwitchStreamFilterEntry)
        assert entry.getShortName() == "Filter1"
        assert details.getStreamFilters() == [entry]

        duplicate = details.createStreamFilter("Filter1")
        assert duplicate is entry
        assert len(details.getStreamFilters()) == 1

        second = details.createStreamFilter("Filter2")
        assert details.getStreamFilters() == [entry, second]

    def test_create_stream_gate(self):
        details = CouplingElementSwitchDetails(MockParent(), "SwitchDetails")

        entry = details.createStreamGate("Gate1")
        assert isinstance(entry, SwitchStreamGateEntry)
        assert entry.getShortName() == "Gate1"
        assert details.getStreamGates() == [entry]

        duplicate = details.createStreamGate("Gate1")
        assert duplicate is entry
        assert len(details.getStreamGates()) == 1

        second = details.createStreamGate("Gate2")
        assert details.getStreamGates() == [entry, second]

    def test_create_switch_stream_identification(self):
        details = CouplingElementSwitchDetails(MockParent(), "SwitchDetails")

        entry = details.createSwitchStreamIdentification("Stream1")
        assert isinstance(entry, SwitchStreamIdentification)
        assert entry.getShortName() == "Stream1"
        assert details.getSwitchStreamIdentifications() == [entry]

        duplicate = details.createSwitchStreamIdentification("Stream1")
        assert duplicate is entry
        assert len(details.getSwitchStreamIdentifications()) == 1

        second = details.createSwitchStreamIdentification("Stream2")
        assert details.getSwitchStreamIdentifications() == [entry, second]

    def test_create_traffic_shaper_group(self):
        details = CouplingElementSwitchDetails(MockParent(), "SwitchDetails")

        entry = details.createTrafficShaperGroup("Group1")
        assert isinstance(entry, SwitchAsynchronousTrafficShaperGroupEntry)
        assert entry.getShortName() == "Group1"
        assert details.getTrafficShaperGroups() == [entry]

        duplicate = details.createTrafficShaperGroup("Group1")
        assert duplicate is entry
        assert len(details.getTrafficShaperGroups()) == 1

        second = details.createTrafficShaperGroup("Group2")
        assert details.getTrafficShaperGroups() == [entry, second]

    def test_inherited_base_accessors_round_trip_and_none_noop(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        details = CouplingElementSwitchDetails(MockParent(), "SwitchDetails")

        category = CategoryString().setValue("switch")
        assert details.setCategory(category) is details
        assert details.getCategory() is category

        assert details.setCategory(None) is details
        assert details.getCategory() is category

        variation_point = VariationPoint()
        assert details.setVariationPoint(variation_point) is details
        assert details.getVariationPoint() is variation_point

        assert details.setVariationPoint(None) is details
        assert details.getVariationPoint() is variation_point
