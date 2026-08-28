"""Writer tests for TDHeaderIdRange (Table 3.38)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDHeaderIdRange,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _build_range():
    rng = TDHeaderIdRange()
    rng.setMaxHeaderId(Integer().setValue("10"))
    rng.setMinHeaderId(Integer().setValue("5"))
    return rng


class TestWriteTDHeaderIdRange:
    def test_write_full(self):
        rng = _build_range()
        element = ET.Element("TD-HEADER-ID-RANGE", xmlns=NS)
        ARXMLWriter().writeTDHeaderIdRange(element, rng)
        out = ET.tostring(element, encoding="unicode")
        assert "MAX-HEADER-ID" in out
        assert "MIN-HEADER-ID" in out
        assert "10" in out
        assert "5" in out

    def test_round_trip(self):
        rng = _build_range()
        element = ET.Element("TD-HEADER-ID-RANGE", xmlns=NS)
        ARXMLWriter().writeTDHeaderIdRange(element, rng)
        reparsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
        read_back = TDHeaderIdRange()
        ARXMLParser().readTDHeaderIdRange(reparsed, read_back)
        assert read_back.getMaxHeaderId().getValue() == 10
        assert read_back.getMinHeaderId().getValue() == 5

    def test_write_minimal(self):
        rng = TDHeaderIdRange()
        element = ET.Element("TD-HEADER-ID-RANGE", xmlns=NS)
        ARXMLWriter().writeTDHeaderIdRange(element, rng)
        out = ET.tostring(element, encoding="unicode")
        assert "MAX-HEADER-ID" not in out
        assert "MIN-HEADER-ID" not in out
