"""
Test suite for SwitchFlowMeteringEntry (CP_TPS_SystemTemplate Table 3.98, p.143, R23-11).

Validates the member defaults, setter semantics (None no-ops), getter/setter
round-trips, the verbatim class-level spec Note and the member declaration
order (markdown displayed row order) of the SwitchFlowMeteringEntry
model class.

The colorMode member is typed with the FlowMeteringColorModeEnum stub
(PrimitiveTypes.py); that enum is queued after this class (Table 3.99), so the
tests below use an instantiable local test double pinned to the XSD facets
(COLOR-AWARE / COLOR-BLIND). When the enum's own sync lands, replace the test
double with the enum constants (FlowMeteringColorModeEnum.COLOR_AWARE /
COLOR_BLIND) and its facet-order __init__.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    FlowMeteringColorModeEnum,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    SwitchFlowMeteringEntry,
)

CLASS_NOTE = "Defines a Flow Metering Entry for a switch. Tags: atp.Status=candidate"

COLOR_MODE_NOTE = "Defines whether color-aware or color-blind mode shall be used. Tags: atp.Status=candidate"

COMMITTED_BURST_SIZE_NOTE = "Committed Burst Size (CBS) (accepted burst size in green token bucket). Tags: atp.Status=candidate"

COMMITTED_INFORMATION_RATE_NOTE = "Committed Information Rate (CIR) (accepted rate in green token bucket) in bits per second. Tags: atp.Status=candidate"

COUPLING_FLAG_NOTE = 'Coupling Flag that defines if unused "green" tokens in the first bucket are transferred to the second bucket as "yellow" tokens. Tags: atp.Status=candidate'

EXCESS_BURST_SIZE_NOTE = "Excess burst size (EBS) (accepted burst size in yellow token bucket). Tags: atp.Status=candidate"

EXCESS_INFORMATION_RATE_NOTE = "Excess Information Rate (EIR) (accepted rate in yellow token bucket) in bits per second. Tags: atp.Status=candidate"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class _ColorModeTestDouble(FlowMeteringColorModeEnum):
    def __init__(self):
        super().__init__(["COLOR-AWARE", "COLOR-BLIND"])


class TestSwitchFlowMeteringEntry:
    def test_inheritance(self):
        assert issubclass(SwitchFlowMeteringEntry, Identifiable)

    def test_concrete_class_instantiable(self):
        flow_metering = SwitchFlowMeteringEntry(MockParent(), "Metering1")
        assert isinstance(flow_metering, Identifiable)
        assert flow_metering.getShortName() == "Metering1"
        assert flow_metering.getParent() is not None

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SwitchFlowMeteringEntry.__doc__) == CLASS_NOTE

    def test_initialization(self):
        flow_metering = SwitchFlowMeteringEntry(MockParent(), "Metering1")

        assert flow_metering.getShortName() == "Metering1"
        assert flow_metering.getColorMode() is None
        assert flow_metering.getCommittedBurstSize() is None
        assert flow_metering.getCommittedInformationRate() is None
        assert flow_metering.getCouplingFlag() is None
        assert flow_metering.getExcessBurstSize() is None
        assert flow_metering.getExcessInformationRate() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "SwitchFlowMeteringEntry")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("colorMode", "Optional[FlowMeteringColorModeEnum]"),
            ("committedBurstSize", "Optional[PositiveInteger]"),
            ("committedInformationRate", "Optional[PositiveInteger]"),
            ("couplingFlag", "Optional[Boolean]"),
            ("excessBurstSize", "Optional[PositiveInteger]"),
            ("excessInformationRate", "Optional[PositiveInteger]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(SwitchFlowMeteringEntry.getColorMode).get("return") == typing.Optional[FlowMeteringColorModeEnum]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setColorMode).get("value") == typing.Optional[FlowMeteringColorModeEnum]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setColorMode).get("return") is SwitchFlowMeteringEntry
        assert typing.get_type_hints(SwitchFlowMeteringEntry.getCommittedBurstSize).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setCommittedBurstSize).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setCommittedBurstSize).get("return") is SwitchFlowMeteringEntry
        assert typing.get_type_hints(SwitchFlowMeteringEntry.getCommittedInformationRate).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setCommittedInformationRate).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setCommittedInformationRate).get("return") is SwitchFlowMeteringEntry
        assert typing.get_type_hints(SwitchFlowMeteringEntry.getCouplingFlag).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setCouplingFlag).get("value") == typing.Optional[Boolean]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setCouplingFlag).get("return") is SwitchFlowMeteringEntry
        assert typing.get_type_hints(SwitchFlowMeteringEntry.getExcessBurstSize).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setExcessBurstSize).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setExcessBurstSize).get("return") is SwitchFlowMeteringEntry
        assert typing.get_type_hints(SwitchFlowMeteringEntry.getExcessInformationRate).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setExcessInformationRate).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchFlowMeteringEntry.setExcessInformationRate).get("return") is SwitchFlowMeteringEntry

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(SwitchFlowMeteringEntry.getColorMode.__doc__) == COLOR_MODE_NOTE
        assert inspect.cleandoc(SwitchFlowMeteringEntry.setColorMode.__doc__) == COLOR_MODE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing colorMode."
        assert inspect.cleandoc(SwitchFlowMeteringEntry.getCommittedBurstSize.__doc__) == COMMITTED_BURST_SIZE_NOTE
        assert (
            inspect.cleandoc(SwitchFlowMeteringEntry.setCommittedBurstSize.__doc__) == COMMITTED_BURST_SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing committedBurstSize."
        )
        assert inspect.cleandoc(SwitchFlowMeteringEntry.getCommittedInformationRate.__doc__) == COMMITTED_INFORMATION_RATE_NOTE
        assert (
            inspect.cleandoc(SwitchFlowMeteringEntry.setCommittedInformationRate.__doc__)
            == COMMITTED_INFORMATION_RATE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing committedInformationRate."
        )
        assert inspect.cleandoc(SwitchFlowMeteringEntry.getCouplingFlag.__doc__) == COUPLING_FLAG_NOTE
        assert inspect.cleandoc(SwitchFlowMeteringEntry.setCouplingFlag.__doc__) == COUPLING_FLAG_NOTE + "\n\nA None value is a no-op and does not overwrite an existing couplingFlag."
        assert inspect.cleandoc(SwitchFlowMeteringEntry.getExcessBurstSize.__doc__) == EXCESS_BURST_SIZE_NOTE
        assert inspect.cleandoc(SwitchFlowMeteringEntry.setExcessBurstSize.__doc__) == EXCESS_BURST_SIZE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing excessBurstSize."
        assert inspect.cleandoc(SwitchFlowMeteringEntry.getExcessInformationRate.__doc__) == EXCESS_INFORMATION_RATE_NOTE
        assert (
            inspect.cleandoc(SwitchFlowMeteringEntry.setExcessInformationRate.__doc__)
            == EXCESS_INFORMATION_RATE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing excessInformationRate."
        )

    def test_get_set_color_mode(self):
        flow_metering = SwitchFlowMeteringEntry(MockParent(), "Metering1")

        value = _ColorModeTestDouble().setValue("COLOR-AWARE")
        assert flow_metering.setColorMode(value) is flow_metering
        assert flow_metering.getColorMode() is value
        assert flow_metering.getColorMode().getValue() == "COLOR-AWARE"

        assert flow_metering.setColorMode(None) is flow_metering
        assert flow_metering.getColorMode() is value

    def test_get_set_committed_burst_size(self):
        flow_metering = SwitchFlowMeteringEntry(MockParent(), "Metering1")

        value = PositiveInteger().setValue("1000")
        assert flow_metering.setCommittedBurstSize(value) is flow_metering
        assert flow_metering.getCommittedBurstSize() is value
        assert flow_metering.getCommittedBurstSize().getValue() == 1000

        assert flow_metering.setCommittedBurstSize(None) is flow_metering
        assert flow_metering.getCommittedBurstSize() is value

    def test_get_set_committed_information_rate(self):
        flow_metering = SwitchFlowMeteringEntry(MockParent(), "Metering1")

        value = PositiveInteger().setValue("2000")
        assert flow_metering.setCommittedInformationRate(value) is flow_metering
        assert flow_metering.getCommittedInformationRate() is value
        assert flow_metering.getCommittedInformationRate().getValue() == 2000

        assert flow_metering.setCommittedInformationRate(None) is flow_metering
        assert flow_metering.getCommittedInformationRate() is value

    def test_get_set_coupling_flag(self):
        flow_metering = SwitchFlowMeteringEntry(MockParent(), "Metering1")

        value = Boolean().setValue(True)
        assert flow_metering.setCouplingFlag(value) is flow_metering
        assert flow_metering.getCouplingFlag() is value
        assert flow_metering.getCouplingFlag().getValue() is True

        assert flow_metering.setCouplingFlag(None) is flow_metering
        assert flow_metering.getCouplingFlag() is value

    def test_get_set_excess_burst_size(self):
        flow_metering = SwitchFlowMeteringEntry(MockParent(), "Metering1")

        value = PositiveInteger().setValue("3000")
        assert flow_metering.setExcessBurstSize(value) is flow_metering
        assert flow_metering.getExcessBurstSize() is value
        assert flow_metering.getExcessBurstSize().getValue() == 3000

        assert flow_metering.setExcessBurstSize(None) is flow_metering
        assert flow_metering.getExcessBurstSize() is value

    def test_get_set_excess_information_rate(self):
        flow_metering = SwitchFlowMeteringEntry(MockParent(), "Metering1")

        value = PositiveInteger().setValue("4000")
        assert flow_metering.setExcessInformationRate(value) is flow_metering
        assert flow_metering.getExcessInformationRate() is value
        assert flow_metering.getExcessInformationRate().getValue() == 4000

        assert flow_metering.setExcessInformationRate(None) is flow_metering
        assert flow_metering.getExcessInformationRate() is value
