"""Parser tests for TDHeaderIdRange (Table 3.38)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDHeaderIdRange,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTDHeaderIdRange:
    def test_read_full(self):
        rng = TDHeaderIdRange()
        element = ET.fromstring(f"<TD-HEADER-ID-RANGE xmlns='{NS}'>" "<MAX-HEADER-ID>10</MAX-HEADER-ID>" "<MIN-HEADER-ID>5</MIN-HEADER-ID>" "</TD-HEADER-ID-RANGE>")
        ARXMLParser().readTDHeaderIdRange(element, rng)
        assert rng.getMaxHeaderId().getValue() == 10
        assert rng.getMinHeaderId().getValue() == 5

    def test_read_minimal(self):
        rng = TDHeaderIdRange()
        element = ET.fromstring(f"<TD-HEADER-ID-RANGE xmlns='{NS}'></TD-HEADER-ID-RANGE>")
        ARXMLParser().readTDHeaderIdRange(element, rng)
        assert rng.getMaxHeaderId() is None
        assert rng.getMinHeaderId() is None
