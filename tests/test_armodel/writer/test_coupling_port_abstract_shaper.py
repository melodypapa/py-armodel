"""Writer/reader round-trip tests for CouplingPortFifo.shaper (CouplingPortAbstractShaper)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortAbstractShaper,
    CouplingPortDetails,
    CouplingPortFifo,
)

NS = "http://autosar.org/schema/r4.0"


class ConcreteShaper(CouplingPortAbstractShaper):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    from armodel.writer.arxml_writer import ARXMLWriter

    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    from armodel.parser.arxml_parser import ARXMLParser

    return ARXMLParser()


def _new_details_with_shaper():
    details = CouplingPortDetails()
    fifo = details.createCouplingPortFifo("Fifo1")
    CouplingPortAbstractShaper.registerShaper("CONCRETE-COUPLING-PORT-SHAPER", ConcreteShaper)
    shaper = ConcreteShaper(fifo, "Shaper1")
    fifo.setShaper(shaper)
    return details


class TestCouplingPortFifoShaperRoundTrip:
    def test_shaper_written_and_read_back(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", _new_details_with_shaper())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getCouplingPortDetails(root[0], "COUPLING-PORT-DETAILS")

        assert isinstance(parsed, CouplingPortDetails)
        fifos = parsed.getCouplingPortStructuralElements()
        assert len(fifos) == 1
        assert isinstance(fifos[0], CouplingPortFifo)
        shaper = fifos[0].getShaper()
        assert shaper is not None
        assert isinstance(shaper, CouplingPortAbstractShaper)
        assert shaper.getShortName() == "Shaper1"

    def test_shaper_absent_when_not_set(self, writer, parser):
        details = CouplingPortDetails()
        details.createCouplingPortFifo("Fifo1")
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getCouplingPortDetails(root[0], "COUPLING-PORT-DETAILS")
        assert parsed.getCouplingPortStructuralElements()[0].getShaper() is None
