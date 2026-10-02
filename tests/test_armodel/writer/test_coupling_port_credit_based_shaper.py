"""Writer/reader round-trip tests for CouplingPortCreditBasedShaper (CouplingPortFifo.shaper CBS choice)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortCreditBasedShaper,
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


def _new_details_with_cbs_shaper():
    details = CouplingPortDetails()
    fifo = details.createCouplingPortFifo("Fifo1")
    shaper = CouplingPortCreditBasedShaper(fifo, "CbsShaper")
    shaper.setIdleSlope(PositiveInteger().setValue("1000000"))
    shaper.setLowerBoundary(PositiveInteger().setValue("2000"))
    shaper.setUpperBoundary(PositiveInteger().setValue("8000"))
    fifo.setShaper(shaper)
    return details


class TestCouplingPortCreditBasedShaperRoundTrip:
    def test_cbs_shaper_fields_round_trip(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", _new_details_with_cbs_shaper())
        inner = ET.tostring(parent).decode("utf-8")
        assert "<COUPLING-PORT-CREDIT-BASED-SHAPER>" in inner
        assert "<IDLE-SLOPE>1000000</IDLE-SLOPE>" in inner
        assert "<LOWER-BOUNDARY>2000</LOWER-BOUNDARY>" in inner
        assert "<UPPER-BOUNDARY>8000</UPPER-BOUNDARY>" in inner

        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getCouplingPortDetails(root[0], "COUPLING-PORT-DETAILS")
        fifo = parsed.getCouplingPortStructuralElements()[0]
        assert isinstance(fifo, CouplingPortFifo)
        shaper = fifo.getShaper()
        assert isinstance(shaper, CouplingPortCreditBasedShaper)
        assert shaper.getShortName() == "CbsShaper"
        assert shaper.getIdleSlope().getValue() == 1000000
        assert shaper.getLowerBoundary().getValue() == 2000
        assert shaper.getUpperBoundary().getValue() == 8000

    def test_cbs_shaper_empty_fields_round_trip(self, writer, parser):
        details = CouplingPortDetails()
        fifo = details.createCouplingPortFifo("Fifo1")
        fifo.setShaper(CouplingPortCreditBasedShaper(fifo, "EmptyCbs"))
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
        inner = ET.tostring(parent).decode("utf-8")
        assert "IDLE-SLOPE" not in inner

        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getCouplingPortDetails(root[0], "COUPLING-PORT-DETAILS")
        shaper = parsed.getCouplingPortStructuralElements()[0].getShaper()
        assert isinstance(shaper, CouplingPortCreditBasedShaper)
        assert shaper.getIdleSlope() is None
        assert shaper.getLowerBoundary() is None
        assert shaper.getUpperBoundary() is None
