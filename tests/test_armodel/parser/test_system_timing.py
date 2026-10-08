"""
Reader tests for SystemTiming (CP_TPS_TimingExtensions Table 3.3, p.27, R23-11).

SystemTiming is an ARPackage-level ARElement (dispatched via the SYSTEM-TIMING tag of
the ARPackage.element aggregate), so the tests exercise readSystemTiming on a standalone
SYSTEM-TIMING subtree: the IDENTIFIABLE level (readIdentifiable), the base TIMING-EXTENSION
group (readTimingExtension) and the own group member SYSTEM-REF
(AUTOSAR_00052.xsd group SYSTEM-TIMING).

Round-trip counterpart: tests/test_armodel/writer/test_system_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import SystemTiming

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<SYSTEM-TIMING xmlns='%s'>%s</SYSTEM-TIMING>" % (NS, inner))


class TestReadSystemTiming:
    def _read(self, parser, inner):
        timing = SystemTiming(AUTOSAR.getInstance(), "SystemTiming1")
        parser.readSystemTiming(_snip(inner), timing)
        return timing

    def test_read_sets_system_ref(self, parser):
        timing = self._read(parser, '<SYSTEM-REF DEST="SYSTEM">/Systems/MySystem</SYSTEM-REF>')

        assert timing.getSystemRef() is not None
        assert timing.getSystemRef().getDest() == "SYSTEM"
        assert timing.getSystemRef().getValue() == "/Systems/MySystem"

    def test_read_empty_element(self, parser):
        timing = self._read(parser, "")

        assert timing.getSystemRef() is None

    def test_read_identifiable_level(self, parser):
        element = ET.fromstring("<SYSTEM-TIMING xmlns='%s' UUID='1234-5678'/>" % NS)
        timing = SystemTiming(AUTOSAR.getInstance(), "SystemTiming1")
        parser.readSystemTiming(element, timing)

        assert timing.getUuid() is not None
        assert timing.getUuid().getValue() == "1234-5678"
