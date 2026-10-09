"""Parser tests for IPduTiming (Table 6.30, p.348).

Serialized inside the I-PDU-TIMING-SPECIFICATIONS wrapper of ISignalIPdu; the
I-PDU-TIMING complexType of AUTOSAR_00052.xsd (l.66581) sequences the AR-OBJECT
group (S/T attributes), the DESCRIBABLE group (DESC, CATEGORY, INTRODUCTION,
ADMIN-DATA) and the I-PDU-TIMING group (MINIMUM-DELAY, TRANSMISSION-MODE-
DECLARATION, VARIATION-POINT with xml.sequenceOffset=10000). The tests exercise
readISignalIPdu, whose getISignalIPduIPduTimingSpecification entry must dispatch
to readDescribable (Base = Describable, owning readARObject) and
readVariationPointCapable for the inherited levels.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    IPduTiming,
    ISignalIPdu,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_XML = f"""<I-SIGNAL-I-PDU xmlns='{NS}'>
    <SHORT-NAME>ISignalIPdu1</SHORT-NAME>
    <I-PDU-TIMING-SPECIFICATIONS>
        <I-PDU-TIMING S="5" T="2025-04-04T00:00:00Z">
            <DESC>
                <L-2 L="EN">timing overview</L-2>
            </DESC>
            <CATEGORY>VARIANTS</CATEGORY>
            <MINIMUM-DELAY>0.005</MINIMUM-DELAY>
            <TRANSMISSION-MODE-DECLARATION>
                <TRANSMISSION-MODE-CONDITIONS>
                    <TRANSMISSION-MODE-CONDITION>
                        <DATA-FILTER>
                            <DATA-FILTER-TYPE>ALWAYS</DATA-FILTER-TYPE>
                        </DATA-FILTER>
                        <I-SIGNAL-IN-I-PDU-REF DEST="I-SIGNAL-TO-I-PDU-MAPPING">/CanSystem/PDUS/Pdu1/Map1</I-SIGNAL-IN-I-PDU-REF>
                    </TRANSMISSION-MODE-CONDITION>
                </TRANSMISSION-MODE-CONDITIONS>
                <TRANSMISSION-MODE-TRUE-TIMING>
                    <EVENT-CONTROLLED-TIMING>
                        <NUMBER-OF-REPETITIONS>1</NUMBER-OF-REPETITIONS>
                        <REPETITION-PERIOD>
                            <VALUE>1.0</VALUE>
                        </REPETITION-PERIOD>
                    </EVENT-CONTROLLED-TIMING>
                </TRANSMISSION-MODE-TRUE-TIMING>
            </TRANSMISSION-MODE-DECLARATION>
            <VARIATION-POINT>
                <SHORT-LABEL>VP1</SHORT-LABEL>
            </VARIATION-POINT>
        </I-PDU-TIMING>
    </I-PDU-TIMING-SPECIFICATIONS>
</I-SIGNAL-I-PDU>"""

EMPTY_TIMING_XML = f"""<I-SIGNAL-I-PDU xmlns='{NS}'>
    <SHORT-NAME>ISignalIPdu1</SHORT-NAME>
    <I-PDU-TIMING-SPECIFICATIONS>
        <I-PDU-TIMING/>
    </I-PDU-TIMING-SPECIFICATIONS>
</I-SIGNAL-I-PDU>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadIPduTiming:
    def test_read_full_field_values(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        ARXMLParser().readISignalIPdu(ET.fromstring(FULL_XML), ipdu)

        timing = ipdu.getIPduTimingSpecification()
        assert isinstance(timing, IPduTiming)
        assert timing.getMinimumDelay().getValue() == 0.005

        decl = timing.getTransmissionModeDeclaration()
        assert decl is not None
        conditions = decl.getTransmissionModeConditions()
        assert len(conditions) == 1
        assert conditions[0].getDataFilter().getDataFilterType().getValue() == "ALWAYS"
        assert conditions[0].getISignalInIPduRef().getValue() == "/CanSystem/PDUS/Pdu1/Map1"
        assert conditions[0].getISignalInIPduRef().getDest() == "I-SIGNAL-TO-I-PDU-MAPPING"
        true_timing = decl.getTransmissionModeTrueTiming()
        assert true_timing is not None
        event_timing = true_timing.getEventControlledTiming()
        assert event_timing.getNumberOfRepetitions().getValue() == 1
        assert event_timing.getRepetitionPeriod().getValue().getValue() == 1.0

    def test_read_describable_level(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        ARXMLParser().readISignalIPdu(ET.fromstring(FULL_XML), ipdu)

        timing = ipdu.getIPduTimingSpecification()
        assert timing.getChecksum().getValue() == "5"
        assert timing.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        desc = timing.getDesc()
        assert desc is not None
        assert desc.getL2s()[0].getValue() == "timing overview"
        assert desc.getL2s()[0].getL() == "EN"
        assert timing.getCategory().getValue() == "VARIANTS"
        assert timing.getIntroduction() is None
        assert timing.getAdminData() is None

    def test_read_variation_point(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        ARXMLParser().readISignalIPdu(ET.fromstring(FULL_XML), ipdu)

        timing = ipdu.getIPduTimingSpecification()
        variation_point = timing.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel().getValue() == "VP1"

    def test_read_empty_timing(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        ARXMLParser().readISignalIPdu(ET.fromstring(EMPTY_TIMING_XML), ipdu)

        timing = ipdu.getIPduTimingSpecification()
        assert isinstance(timing, IPduTiming)
        assert timing.getMinimumDelay() is None
        assert timing.getTransmissionModeDeclaration() is None
        assert timing.getDesc() is None
        assert timing.getCategory() is None
        assert timing.getVariationPoint() is None
        assert timing.getChecksum() is None

    def test_read_absent_timing(self):
        xml = f"""<I-SIGNAL-I-PDU xmlns='{NS}'>
    <SHORT-NAME>ISignalIPdu1</SHORT-NAME>
</I-SIGNAL-I-PDU>"""
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        ARXMLParser().readISignalIPdu(ET.fromstring(xml), ipdu)

        assert ipdu.getIPduTimingSpecification() is None
