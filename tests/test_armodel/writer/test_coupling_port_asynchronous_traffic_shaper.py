"""Writer/reader round-trip tests for CouplingPortAsynchronousTrafficShaper (CouplingPortFifo.shaper ATS choice)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortAsynchronousTrafficShaper,
    CouplingPortDetails,
    CouplingPortFifo,
)

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    from armodel.writer.arxml_writer import ARXMLWriter

    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    from armodel.parser.arxml_parser import ARXMLParser

    return ARXMLParser()


def _new_details_with_ats_shaper():
    details = CouplingPortDetails()
    fifo = details.createCouplingPortFifo("Fifo1")
    shaper = CouplingPortAsynchronousTrafficShaper(fifo, "AtsShaper")
    shaper.setCommittedBurstSize(PositiveInteger().setValue("12500"))
    shaper.setCommittedInformationRate(PositiveInteger().setValue("1000000"))
    shaper.setTrafficShaperGroupRef(RefType().setValue("/Cluster/SwitchAsynchronousTrafficShaperGroupEntry").setDest("SWITCH-ASYNCHRONOUS-TRAFFIC-SHAPER-GROUP-ENTRY"))
    fifo.setShaper(shaper)
    return details


class TestCouplingPortAsynchronousTrafficShaperRoundTrip:
    def test_ats_shaper_fields_round_trip(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", _new_details_with_ats_shaper())
        inner = ET.tostring(parent).decode("utf-8")
        assert "<COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER>" in inner
        assert "<COMMITTED-BURST-SIZE>12500</COMMITTED-BURST-SIZE>" in inner
        assert "<COMMITTED-INFORMATION-RATE>1000000</COMMITTED-INFORMATION-RATE>" in inner
        assert 'DEST="SWITCH-ASYNCHRONOUS-TRAFFIC-SHAPER-GROUP-ENTRY"' in inner

        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getCouplingPortDetails(root[0], "COUPLING-PORT-DETAILS")
        fifo = parsed.getCouplingPortStructuralElements()[0]
        assert isinstance(fifo, CouplingPortFifo)
        shaper = fifo.getShaper()
        assert isinstance(shaper, CouplingPortAsynchronousTrafficShaper)
        assert shaper.getShortName() == "AtsShaper"
        assert shaper.getCommittedBurstSize().getValue() == 12500
        assert shaper.getCommittedInformationRate().getValue() == 1000000
        ref = shaper.getTrafficShaperGroupRef()
        assert ref is not None
        assert ref.getValue() == "/Cluster/SwitchAsynchronousTrafficShaperGroupEntry"
        assert ref.getDest() == "SWITCH-ASYNCHRONOUS-TRAFFIC-SHAPER-GROUP-ENTRY"

    def test_ats_shaper_empty_fields_round_trip(self, writer, parser):
        details = CouplingPortDetails()
        fifo = details.createCouplingPortFifo("Fifo1")
        fifo.setShaper(CouplingPortAsynchronousTrafficShaper(fifo, "EmptyAts"))
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
        inner = ET.tostring(parent).decode("utf-8")
        assert "COMMITTED-BURST-SIZE" not in inner

        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getCouplingPortDetails(root[0], "COUPLING-PORT-DETAILS")
        shaper = parsed.getCouplingPortStructuralElements()[0].getShaper()
        assert isinstance(shaper, CouplingPortAsynchronousTrafficShaper)
        assert shaper.getCommittedBurstSize() is None
        assert shaper.getCommittedInformationRate() is None
        assert shaper.getTrafficShaperGroupRef() is None
