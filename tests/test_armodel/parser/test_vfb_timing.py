"""
Reader tests for VfbTiming (CP_TPS_TimingExtensions Table 3.1, p.24, R23-11).

VfbTiming is an ARPackage-level ARElement (dispatched via the VFB-TIMING tag of the
ARPackage.element aggregate), so the tests exercise readVfbTiming on a standalone
VFB-TIMING subtree: the IDENTIFIABLE level (readIdentifiable), the base TIMING-EXTENSION
group (readTimingExtension) and the own group member COMPONENT-REF
(AUTOSAR_00052.xsd group VFB-TIMING).

Round-trip counterpart: tests/test_armodel/writer/test_vfb_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import VfbTiming

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<VFB-TIMING xmlns='%s'>%s</VFB-TIMING>" % (NS, inner))


class TestReadVfbTiming:
    def _read(self, parser, inner):
        timing = VfbTiming(AUTOSAR.getInstance(), "VfbTiming1")
        parser.readVfbTiming(_snip(inner), timing)
        return timing

    def test_read_sets_component_ref(self, parser):
        timing = self._read(parser, '<COMPONENT-REF DEST="SW-COMPONENT-TYPE">/SwComponentTypes/MySwc</COMPONENT-REF>')

        assert timing.getComponentRef() is not None
        assert timing.getComponentRef().getDest() == "SW-COMPONENT-TYPE"
        assert timing.getComponentRef().getValue() == "/SwComponentTypes/MySwc"

    def test_read_empty_element(self, parser):
        timing = self._read(parser, "")

        assert timing.getComponentRef() is None

    def test_read_identifiable_level(self, parser):
        element = ET.fromstring("<VFB-TIMING xmlns='%s' UUID='1234-5678'/>" % NS)
        timing = VfbTiming(AUTOSAR.getInstance(), "VfbTiming1")
        parser.readVfbTiming(element, timing)

        assert timing.getUuid() is not None
        assert timing.getUuid().getValue() == "1234-5678"
