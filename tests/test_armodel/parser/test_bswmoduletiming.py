"""
Reader tests for {CLS} (CP_TPS_TimingExtensions {TBL}, R23-11).

{CLS} is an ARPackage-level ARElement (dispatched via the {TAG} tag of the
ARPackage.element aggregate), so the tests exercise read{CLS} on a standalone
{TAG} subtree: the IDENTIFIABLE level (readIdentifiable), the base TIMING-EXTENSION
group (readTimingExtension) and the own group member {REF}
(AUTOSAR_00052.xsd group {TAG}).

Round-trip counterpart: tests/test_armodel/writer/test_bswmoduletiming.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import {CLS}

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<{TAG} xmlns='%s'>%s</{TAG}>" % (NS, inner))


class TestRead{CLS}:
    def _read(self, parser, inner):
        timing = {CLS}(AUTOSAR.getInstance(), "{CLS}1")
        parser.read{CLS}(_snip(inner), timing)
        return timing

    def test_read_sets_behavior_ref(self, parser):
        timing = self._read(parser, '<{REF} DEST="{DEST}">{REF_PATH}<{REF}>'.replace("<{REF}>", "</{REF}>"))

        assert timing.getBehaviorRef() is not None
        assert timing.getBehaviorRef().getDest() == "{DEST}"
        assert timing.getBehaviorRef().getValue() == "{REF_PATH}"

    def test_read_empty_element(self, parser):
        timing = self._read(parser, "")

        assert timing.getBehaviorRef() is None

    def test_read_identifiable_level(self, parser):
        element = ET.fromstring("<{TAG} xmlns='%s' UUID='1234-5678'/>" % NS)
        timing = {CLS}(AUTOSAR.getInstance(), "{CLS}1")
        parser.read{CLS}(element, timing)

        assert timing.getUuid() is not None
        assert timing.getUuid().getValue() == "1234-5678"
