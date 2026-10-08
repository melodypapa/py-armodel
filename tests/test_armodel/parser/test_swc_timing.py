"""
Reader tests for SwcTiming (CP_TPS_TimingExtensions Table 3.2, p.25, R23-11).

SwcTiming is an ARPackage-level ARElement (dispatched via the SWC-TIMING tag of the
ARPackage.element aggregate), so the tests exercise readSwcTiming on a standalone
SWC-TIMING subtree: the IDENTIFIABLE level (readIdentifiable), the base TIMING-EXTENSION
group (readTimingExtension) and the own group member BEHAVIOR-REF
(AUTOSAR_00052.xsd group SWC-TIMING).

Round-trip counterpart: tests/test_armodel/writer/test_swc_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import SwcTiming

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<SWC-TIMING xmlns='%s'>%s</SWC-TIMING>" % (NS, inner))


class TestReadSwcTiming:
    def _read(self, parser, inner):
        timing = SwcTiming(AUTOSAR.getInstance(), "SwcTiming1")
        parser.readSwcTiming(_snip(inner), timing)
        return timing

    def test_read_sets_behavior_ref(self, parser):
        timing = self._read(parser, '<BEHAVIOR-REF DEST="SWC-INTERNAL-BEHAVIOR">/Swc/InternalBehavior/Behav1</BEHAVIOR-REF>')

        assert timing.getBehaviorRef() is not None
        assert timing.getBehaviorRef().getDest() == "SWC-INTERNAL-BEHAVIOR"
        assert timing.getBehaviorRef().getValue() == "/Swc/InternalBehavior/Behav1"

    def test_read_empty_element(self, parser):
        timing = self._read(parser, "")

        assert timing.getBehaviorRef() is None

    def test_read_identifiable_level(self, parser):
        element = ET.fromstring("<SWC-TIMING xmlns='%s' UUID='1234-5678'/>" % NS)
        timing = SwcTiming(AUTOSAR.getInstance(), "SwcTiming1")
        parser.readSwcTiming(element, timing)

        assert timing.getUuid() is not None
        assert timing.getUuid().getValue() == "1234-5678"
