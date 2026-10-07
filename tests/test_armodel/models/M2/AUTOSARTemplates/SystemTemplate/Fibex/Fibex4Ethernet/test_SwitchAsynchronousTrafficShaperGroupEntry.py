"""
Test suite for SwitchAsynchronousTrafficShaperGroupEntry (CP_TPS_SystemTemplate Table 3.96, p.142, R23-11).

Validates the member defaults, setter semantics (None no-ops), getter/setter
round-trips, the verbatim class-level spec Note and the member declaration
order (markdown displayed row order) of the SwitchAsynchronousTrafficShaperGroupEntry
model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    SwitchAsynchronousTrafficShaperGroupEntry,
)

CLASS_NOTE = "Defines an Asynchronous Traffic Shapter (ATS) Group for a switch. Tags: atp.Status=candidate"

MAXIMUM_RESIDENCE_TIME_NOTE = "Defines the maximum duration limit for which frames can reside in a switch (in seconds). Tags: atp.Status=candidate"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSwitchAsynchronousTrafficShaperGroupEntry:
    def test_inheritance(self):
        assert issubclass(SwitchAsynchronousTrafficShaperGroupEntry, Identifiable)

    def test_concrete_class_instantiable(self):
        traffic_shaper_group = SwitchAsynchronousTrafficShaperGroupEntry(MockParent(), "AtsGroup1")
        assert isinstance(traffic_shaper_group, Identifiable)
        assert traffic_shaper_group.getShortName() == "AtsGroup1"
        assert traffic_shaper_group.getParent() is not None

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SwitchAsynchronousTrafficShaperGroupEntry.__doc__) == CLASS_NOTE

    def test_initialization(self):
        traffic_shaper_group = SwitchAsynchronousTrafficShaperGroupEntry(MockParent(), "AtsGroup1")

        assert traffic_shaper_group.getShortName() == "AtsGroup1"
        assert traffic_shaper_group.getMaximumResidenceTime() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "SwitchAsynchronousTrafficShaperGroupEntry")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("maximumResidenceTime", "Optional[PositiveInteger]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(SwitchAsynchronousTrafficShaperGroupEntry.getMaximumResidenceTime).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchAsynchronousTrafficShaperGroupEntry.setMaximumResidenceTime).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchAsynchronousTrafficShaperGroupEntry.setMaximumResidenceTime).get("return") is SwitchAsynchronousTrafficShaperGroupEntry

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(SwitchAsynchronousTrafficShaperGroupEntry.getMaximumResidenceTime.__doc__) == MAXIMUM_RESIDENCE_TIME_NOTE
        assert (
            inspect.cleandoc(SwitchAsynchronousTrafficShaperGroupEntry.setMaximumResidenceTime.__doc__)
            == MAXIMUM_RESIDENCE_TIME_NOTE + "\n\nA None value is a no-op and does not overwrite an existing maximumResidenceTime."
        )

    def test_get_set_maximum_residence_time(self):
        traffic_shaper_group = SwitchAsynchronousTrafficShaperGroupEntry(MockParent(), "AtsGroup1")

        value = PositiveInteger().setValue("10")
        assert traffic_shaper_group.setMaximumResidenceTime(value) is traffic_shaper_group
        assert traffic_shaper_group.getMaximumResidenceTime() is value
        assert traffic_shaper_group.getMaximumResidenceTime().getValue() == 10

        assert traffic_shaper_group.setMaximumResidenceTime(None) is traffic_shaper_group
        assert traffic_shaper_group.getMaximumResidenceTime() is value
