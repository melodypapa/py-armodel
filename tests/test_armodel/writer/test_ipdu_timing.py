"""Writer round-trip tests for IPduTiming (Table 6.30, p.348).

Serialized through setISignalIPduIPduTimingSpecification inside writeISignalIPdu;
the I-PDU-TIMING complexType of AUTOSAR_00052.xsd (l.66581) sequences the
AR-OBJECT group (S/T attributes), the DESCRIBABLE group (DESC, CATEGORY,
INTRODUCTION, ADMIN-DATA) and the I-PDU-TIMING group (MINIMUM-DELAY,
TRANSMISSION-MODE-DECLARATION, VARIATION-POINT with xml.sequenceOffset=10000).
The wrapper I-PDU-TIMING-SPECIFICATIONS is emitted only when the timing exists.
The tests exercise setISignalIPduIPduTimingSpecification, which must dispatch to
writeDescribable (Base = Describable, owning writeARObject) and
writeVariationPointCapable for the inherited levels.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter, DataFilterTypeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    DateTime,
    Identifier,
    Integer,
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    IPduTiming,
    ISignalIPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    EventControlledTiming,
    TransmissionModeCondition,
    TransmissionModeDeclaration,
    TransmissionModeTiming,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "DESC",
    "CATEGORY",
    "INTRODUCTION",
    "ADMIN-DATA",
    "MINIMUM-DELAY",
    "TRANSMISSION-MODE-DECLARATION",
    "VARIATION-POINT",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<I-SIGNAL-I-PDU>", "<I-SIGNAL-I-PDU xmlns='%s'>" % NS, 1))


def _populate_timing() -> IPduTiming:
    timing = IPduTiming()

    checksum = String()
    checksum.setValue("5")
    timing.setChecksum(checksum)

    timestamp = DateTime()
    timestamp.setValue("2025-04-04T00:00:00Z")
    timing.setTimestamp(timestamp)

    l2 = LOverviewParagraph()
    l2.setL("EN")
    l2.setValue("timing overview")
    timing.setDesc(MultiLanguageOverviewParagraph().addL2(l2))

    category = CategoryString()
    category.setValue("VARIANTS")
    timing.setCategory(category)

    minimum_delay = TimeValue()
    minimum_delay.setValue("0.005")
    timing.setMinimumDelay(minimum_delay)

    decl = TransmissionModeDeclaration()
    condition = TransmissionModeCondition()
    data_filter = DataFilter()
    filter_type = DataFilterTypeEnum()
    filter_type.setValue(DataFilterTypeEnum.ALWAYS)
    data_filter.setDataFilterType(filter_type)
    condition.setDataFilter(data_filter)
    ref = RefType()
    ref.setValue("/CanSystem/PDUS/Pdu1/Map1")
    ref.setDest("I-SIGNAL-TO-I-PDU-MAPPING")
    condition.setISignalInIPduRef(ref)
    decl.addTransmissionModeCondition(condition)
    true_timing = TransmissionModeTiming()
    event_timing = EventControlledTiming()
    repetitions = Integer()
    repetitions.setValue("1")
    event_timing.setNumberOfRepetitions(repetitions)
    true_timing.setEventControlledTiming(event_timing)
    decl.setTransmissionModeTrueTiming(true_timing)
    timing.setTransmissionModeDeclaration(decl)

    return timing


def _write(ipdu: ISignalIPdu) -> ET.Element:
    parent = ET.Element("AR-PACKAGE")
    ARXMLWriter().writeISignalIPdu(parent, ipdu)
    return parent.find("I-SIGNAL-I-PDU")


class TestWriteIPduTiming:
    def test_write_absent_timing_omits_wrapper(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")

        node = _write(ipdu)
        assert node.find("I-PDU-TIMING-SPECIFICATIONS") is None

    def test_write_full_child_order_matches_xsd(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        ipdu.setIPduTimingSpecification(_populate_timing())

        node = _write(ipdu)
        timing_node = node.find("I-PDU-TIMING-SPECIFICATIONS/I-PDU-TIMING")
        tags = [child.tag for child in timing_node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == ["DESC", "CATEGORY", "MINIMUM-DELAY", "TRANSMISSION-MODE-DECLARATION"]

    def test_write_full_field_values(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        ipdu.setIPduTimingSpecification(_populate_timing())

        node = _write(ipdu)
        timing_node = node.find("I-PDU-TIMING-SPECIFICATIONS/I-PDU-TIMING")
        assert timing_node.attrib["S"] == "5"
        assert timing_node.attrib["T"] == "2025-04-04T00:00:00Z"
        desc_node = timing_node.find("DESC/L-2")
        assert desc_node.text == "timing overview"
        assert desc_node.attrib["L"] == "EN"
        assert timing_node.find("CATEGORY").text == "VARIANTS"
        assert timing_node.find("MINIMUM-DELAY").text == "0.005"
        condition_node = timing_node.find("TRANSMISSION-MODE-DECLARATION/TRANSMISSION-MODE-CONDITIONS/TRANSMISSION-MODE-CONDITION")
        assert condition_node.find("DATA-FILTER/DATA-FILTER-TYPE").text == "ALWAYS"
        assert condition_node.find("I-SIGNAL-IN-I-PDU-REF").text == "/CanSystem/PDUS/Pdu1/Map1"
        assert condition_node.find("I-SIGNAL-IN-I-PDU-REF").attrib["DEST"] == "I-SIGNAL-TO-I-PDU-MAPPING"

    def test_round_trip_full(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        ipdu.setIPduTimingSpecification(_populate_timing())

        node = _write(ipdu)
        reloaded = ISignalIPdu(None, "ISignalIPdu1")
        ARXMLParser().readISignalIPdu(_with_ns(node), reloaded)

        timing = reloaded.getIPduTimingSpecification()
        assert isinstance(timing, IPduTiming)
        assert timing.getChecksum().getValue() == "5"
        assert timing.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert timing.getDesc().getL2s()[0].getValue() == "timing overview"
        assert timing.getCategory().getValue() == "VARIANTS"
        assert timing.getMinimumDelay().getValue() == 0.005

        decl = timing.getTransmissionModeDeclaration()
        conditions = decl.getTransmissionModeConditions()
        assert len(conditions) == 1
        assert conditions[0].getDataFilter().getDataFilterType().getValue() == "ALWAYS"
        assert conditions[0].getISignalInIPduRef().getValue() == "/CanSystem/PDUS/Pdu1/Map1"
        assert decl.getTransmissionModeTrueTiming().getEventControlledTiming().getNumberOfRepetitions().getValue() == 1

    def test_round_trip_variation_point(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        timing = _populate_timing()
        variation_point = VariationPoint()
        label = Identifier()
        label.setValue("VP1")
        variation_point.setShortLabel(label)
        timing.setVariationPoint(variation_point)
        ipdu.setIPduTimingSpecification(timing)

        node = _write(ipdu)
        timing_node = node.find("I-PDU-TIMING-SPECIFICATIONS/I-PDU-TIMING")
        assert timing_node.find("VARIATION-POINT/SHORT-LABEL").text == "VP1"

        reloaded = ISignalIPdu(None, "ISignalIPdu1")
        ARXMLParser().readISignalIPdu(_with_ns(node), reloaded)
        assert reloaded.getIPduTimingSpecification().getVariationPoint().getShortLabel().getValue() == "VP1"
