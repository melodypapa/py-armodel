"""
Reader tests for EcuTiming (CP_TPS_TimingExtensions Table 3.6, p.30, R23-11).

EcuTiming is an ARPackage-level ARElement (dispatched via the ECU-TIMING tag of the
ARPackage.element aggregate), so the tests exercise readEcuTiming on a standalone
ECU-TIMING subtree: the IDENTIFIABLE level (readIdentifiable), the base TIMING-EXTENSION
group (readTimingExtension) and the own group member ECU-CONFIGURATION-REF
(AUTOSAR_00052.xsd group ECU-TIMING).

Round-trip counterpart: tests/test_armodel/writer/test_ecu_timing.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import EcuTiming

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<ECU-TIMING xmlns='%s'>%s</ECU-TIMING>" % (NS, inner))


class TestReadEcuTiming:
    def _read(self, parser, inner):
        timing = EcuTiming(AUTOSAR.getInstance(), "EcuTiming1")
        parser.readEcuTiming(_snip(inner), timing)
        return timing

    def test_read_sets_ecu_configuration_ref(self, parser):
        timing = self._read(parser, '<ECU-CONFIGURATION-REF DEST="ECUC-VALUE-COLLECTION">/EcuExtract/EcuConfigValues</ECU-CONFIGURATION-REF>')

        assert timing.getEcuConfigurationRef() is not None
        assert timing.getEcuConfigurationRef().getDest() == "ECUC-VALUE-COLLECTION"
        assert timing.getEcuConfigurationRef().getValue() == "/EcuExtract/EcuConfigValues"

    def test_read_empty_element(self, parser):
        timing = self._read(parser, "")

        assert timing.getEcuConfigurationRef() is None

    def test_read_identifiable_level(self, parser):
        element = ET.fromstring("<ECU-TIMING xmlns='%s' UUID='1234-5678'/>" % NS)
        timing = EcuTiming(AUTOSAR.getInstance(), "EcuTiming1")
        parser.readEcuTiming(element, timing)

        assert timing.getUuid() is not None
        assert timing.getUuid().getValue() == "1234-5678"
