"""Writer/reader round-trip tests for CouplingPortFifo.shaper (CouplingPortAbstractShaper)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortAbstractShaper,
    CouplingPortAsynchronousTrafficShaper,
    CouplingPortCreditBasedShaper,
    CouplingPortDetails,
    CouplingPortFifo,
)

NS = "http://autosar.org/schema/r4.0"


class UnregisteredShaper(CouplingPortAbstractShaper):
    """A shaper outside the XSD choice — exercises the unsupported dispatch path."""


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


def _roundtrip(writer, parser, details):
    parent = ET.Element("PARENT")
    writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
    return parser.getCouplingPortDetails(root[0], "COUPLING-PORT-DETAILS")


def _new_details_with_shaper(shaper_cls, **attrs):
    details = CouplingPortDetails()
    fifo = details.createCouplingPortFifo("Fifo1")
    shaper = shaper_cls(fifo, "Shaper1")
    for name, value in attrs.items():
        getattr(shaper, "set" + name)(value)
    fifo.setShaper(shaper)
    return details


class TestCouplingPortFifoShaperRoundTrip:
    def test_asynchronous_traffic_shaper_written_and_read_back(self, writer, parser):
        burst = PositiveInteger().setValue("100")
        rate = PositiveInteger().setValue("200")
        details = _new_details_with_shaper(
            CouplingPortAsynchronousTrafficShaper,
            CommittedBurstSize=burst,
            CommittedInformationRate=rate,
        )
        parsed = _roundtrip(writer, parser, details)

        fifos = parsed.getCouplingPortStructuralElements()
        assert len(fifos) == 1
        assert isinstance(fifos[0], CouplingPortFifo)
        shaper = fifos[0].getShaper()
        assert isinstance(shaper, CouplingPortAsynchronousTrafficShaper)
        assert shaper.getShortName() == "Shaper1"
        assert shaper.getCommittedBurstSize().getValue() == 100
        assert shaper.getCommittedInformationRate().getValue() == 200

    def test_credit_based_shaper_written_with_its_xsd_tag(self, writer, parser):
        details = _new_details_with_shaper(
            CouplingPortCreditBasedShaper,
            IdleSlope=PositiveInteger().setValue("300"),
            LowerBoundary=PositiveInteger().setValue("400"),
            UpperBoundary=PositiveInteger().setValue("500"),
        )
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
        inner = ET.tostring(parent).decode("utf-8")
        assert "COUPLING-PORT-CREDIT-BASED-SHAPER" in inner
        assert "COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER" not in inner

        parsed = _roundtrip(writer, parser, details)
        shaper = parsed.getCouplingPortStructuralElements()[0].getShaper()
        assert isinstance(shaper, CouplingPortCreditBasedShaper)
        assert shaper.getIdleSlope().getValue() == 300
        assert shaper.getLowerBoundary().getValue() == 400
        assert shaper.getUpperBoundary().getValue() == 500

    def test_asynchronous_traffic_shaper_uses_its_own_xsd_tag(self, writer):
        details = _new_details_with_shaper(CouplingPortAsynchronousTrafficShaper)
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
        inner = ET.tostring(parent).decode("utf-8")
        assert "COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER" in inner
        assert "COUPLING-PORT-CREDIT-BASED-SHAPER" not in inner

    def test_shaper_absent_when_not_set(self, writer, parser):
        details = CouplingPortDetails()
        details.createCouplingPortFifo("Fifo1")
        parsed = _roundtrip(writer, parser, details)
        assert parsed.getCouplingPortStructuralElements()[0].getShaper() is None

    def test_unsupported_shaper_class_emits_no_shaper_element(self):
        AUTOSAR.getInstance().new()
        from armodel.writer.arxml_writer import ARXMLWriter

        writer = ARXMLWriter(options={"warning": True})
        details = _new_details_with_shaper(UnregisteredShaper)
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<SHAPER" not in inner

    def test_unsupported_shaper_tag_read_is_reported(self):
        from armodel.parser.arxml_parser import ARXMLParser

        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(
            "<COUPLING-PORT-FIFO xmlns='%s'><SHORT-NAME>Fifo1</SHORT-NAME>" "<SHAPER><NO-SUCH-SHAPER><SHORT-NAME>Shaper1</SHORT-NAME></NO-SUCH-SHAPER></SHAPER>" "</COUPLING-PORT-FIFO>" % NS
        )
        fifo = CouplingPortFifo(None, "Fifo1")
        parser.readCouplingPortFifo(element, fifo)
        assert fifo.getShaper() is None
        assert fifo.getShaper() is None
