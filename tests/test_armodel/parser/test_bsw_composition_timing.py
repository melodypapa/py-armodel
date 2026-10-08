"""
Reader tests for BswCompositionTiming (CP_TPS_TimingExtensions Table 3.5, p.29, R23-11).

BswCompositionTiming is an ARPackage-level ARElement (dispatched via the
BSW-COMPOSITION-TIMING tag of the ARPackage.element aggregate), so the tests exercise
readBswCompositionTiming on a standalone BSW-COMPOSITION-TIMING subtree: the
IDENTIFIABLE level (readIdentifiable), the base TIMING-EXTENSION group
(readTimingExtension) and the own group wrapper IMPLEMENTATION-REFS/IMPLEMENTATION-REF
(AUTOSAR_00052.xsd group BSW-COMPOSITION-TIMING).

Round-trip counterpart: tests/test_armodel/writer/test_bsw_composition_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import BswCompositionTiming

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<BSW-COMPOSITION-TIMING xmlns='%s'>%s</BSW-COMPOSITION-TIMING>" % (NS, inner))


class TestReadBswCompositionTiming:
    def _read(self, parser, inner):
        timing = BswCompositionTiming(AUTOSAR.getInstance(), "BswCompositionTiming1")
        parser.readBswCompositionTiming(_snip(inner), timing)
        return timing

    def test_read_sets_implementation_refs(self, parser):
        timing = self._read(
            parser,
            "<IMPLEMENTATION-REFS>"
            '<IMPLEMENTATION-REF DEST="BSW-IMPLEMENTATION">/BswImplementations/Impl1</IMPLEMENTATION-REF>'
            '<IMPLEMENTATION-REF DEST="BSW-IMPLEMENTATION">/BswImplementations/Impl2</IMPLEMENTATION-REF>'
            "</IMPLEMENTATION-REFS>",
        )

        refs = timing.getImplementationRefs()
        assert len(refs) == 2
        assert refs[0].getDest() == "BSW-IMPLEMENTATION"
        assert refs[0].getValue() == "/BswImplementations/Impl1"
        assert refs[1].getValue() == "/BswImplementations/Impl2"

    def test_read_empty_element(self, parser):
        timing = self._read(parser, "")

        assert timing.getImplementationRefs() == []

    def test_read_identifiable_level(self, parser):
        element = ET.fromstring("<BSW-COMPOSITION-TIMING xmlns='%s' UUID='1234-5678'/>" % NS)
        timing = BswCompositionTiming(AUTOSAR.getInstance(), "BswCompositionTiming1")
        parser.readBswCompositionTiming(element, timing)

        assert timing.getUuid() is not None
        assert timing.getUuid().getValue() == "1234-5678"
