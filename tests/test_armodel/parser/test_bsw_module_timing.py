"""
Reader tests for BswModuleTiming (CP_TPS_TimingExtensions Table 3.4, p.28, R23-11).

BswModuleTiming is an ARPackage-level ARElement (dispatched via the BSW-MODULE-TIMING tag of the
ARPackage.element aggregate), so the tests exercise readBswModuleTiming on a standalone
BSW-MODULE-TIMING subtree: the IDENTIFIABLE level (readIdentifiable), the base TIMING-EXTENSION
group (readTimingExtension) and the own group member BEHAVIOR-REF
(AUTOSAR_00052.xsd group BSW-MODULE-TIMING).

Round-trip counterpart: tests/test_armodel/writer/test_bsw_module_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import BswModuleTiming

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<BSW-MODULE-TIMING xmlns='%s'>%s</BSW-MODULE-TIMING>" % (NS, inner))


class TestReadBswModuleTiming:
    def _read(self, parser, inner):
        timing = BswModuleTiming(AUTOSAR.getInstance(), "BswModuleTiming1")
        parser.readBswModuleTiming(_snip(inner), timing)
        return timing

    def test_read_sets_behavior_ref(self, parser):
        timing = self._read(parser, '<BEHAVIOR-REF DEST="BSW-INTERNAL-BEHAVIOR">/BswModule/InternalBehavior/Behav1</BEHAVIOR-REF>')

        assert timing.getBehaviorRef() is not None
        assert timing.getBehaviorRef().getDest() == "BSW-INTERNAL-BEHAVIOR"
        assert timing.getBehaviorRef().getValue() == "/BswModule/InternalBehavior/Behav1"

    def test_read_empty_element(self, parser):
        timing = self._read(parser, "")

        assert timing.getBehaviorRef() is None

    def test_read_identifiable_level(self, parser):
        element = ET.fromstring("<BSW-MODULE-TIMING xmlns='%s' UUID='1234-5678'/>" % NS)
        timing = BswModuleTiming(AUTOSAR.getInstance(), "BswModuleTiming1")
        parser.readBswModuleTiming(element, timing)

        assert timing.getUuid() is not None
        assert timing.getUuid().getValue() == "1234-5678"
