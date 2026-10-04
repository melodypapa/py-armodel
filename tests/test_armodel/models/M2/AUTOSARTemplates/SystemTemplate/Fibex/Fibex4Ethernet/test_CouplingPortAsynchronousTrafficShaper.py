"""Model unit tests for CouplingPortAsynchronousTrafficShaper (XSD-derived, atp.Status=candidate, no PDF table)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortAbstractShaper,
    CouplingPortAsynchronousTrafficShaper,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture
def shaper():
    return CouplingPortAsynchronousTrafficShaper(MockParent(), "AtsShaper")


class TestCouplingPortAsynchronousTrafficShaper:
    def test_is_coupling_port_fifo_shaper_choice_member(self):
        assert issubclass(CouplingPortAsynchronousTrafficShaper, CouplingPortAbstractShaper)

    def test_initialization_defaults(self, shaper):
        assert shaper.getShortName() == "AtsShaper"
        assert shaper.getCommittedBurstSize() is None
        assert shaper.getCommittedInformationRate() is None
        assert shaper.getTrafficShaperGroupRef() is None

    def test_get_set_committed_burst_size(self, shaper):
        value = PositiveInteger().setValue("12500")
        assert shaper.setCommittedBurstSize(value) is shaper
        assert shaper.getCommittedBurstSize() is value

    def test_set_committed_burst_size_none_no_op(self, shaper):
        shaper.setCommittedBurstSize(PositiveInteger().setValue("12500"))
        shaper.setCommittedBurstSize(None)
        assert shaper.getCommittedBurstSize().getValue() == 12500

    def test_get_set_committed_information_rate(self, shaper):
        value = PositiveInteger().setValue("1000000")
        assert shaper.setCommittedInformationRate(value) is shaper
        assert shaper.getCommittedInformationRate() is value

    def test_set_committed_information_rate_none_no_op(self, shaper):
        shaper.setCommittedInformationRate(PositiveInteger().setValue("1000000"))
        shaper.setCommittedInformationRate(None)
        assert shaper.getCommittedInformationRate().getValue() == 1000000

    def test_get_set_traffic_shaper_group_ref(self, shaper):
        ref = RefType().setValue("/Cluster/SwitchAsynchronousTrafficShaperGroupEntry").setDest("SWITCH-ASYNCHRONOUS-TRAFFIC-SHAPER-GROUP-ENTRY")
        assert shaper.setTrafficShaperGroupRef(ref) is shaper
        assert shaper.getTrafficShaperGroupRef() is ref

    def test_set_traffic_shaper_group_ref_none_no_op(self, shaper):
        ref = RefType().setValue("/Cluster/SwitchAsynchronousTrafficShaperGroupEntry")
        shaper.setTrafficShaperGroupRef(ref)
        shaper.setTrafficShaperGroupRef(None)
        assert shaper.getTrafficShaperGroupRef() is ref
