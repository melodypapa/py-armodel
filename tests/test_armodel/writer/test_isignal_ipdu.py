"""Writer round-trip tests for ISignalIPdu (Table 6.19, p.342).

Serialized through writeISignalIPdu; own child set and order per the
I-SIGNAL-I-PDU group of AUTOSAR_00052.xsd (l.66972), sequenced after the PDU and
I-PDU groups in the I-SIGNAL-I-PDU complexType (l.67054). PDU-COUNTERS and
PDU-REPLICATIONS carry atp.Status="removed" in the XSD and are not modeled
(Rule 0015). The tests exercise writeISignalIPdu, which must dispatch to
writeIPdu (Base = IPdu) exactly once for the inherited levels.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduCollectionSemanticsEnum,
    ContainedIPduProps,
    IPduTiming,
    ISignalIPdu,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "HAS-DYNAMIC-LENGTH",
    "LENGTH",
    "CONTAINED-I-PDU-PROPS",
    "I-PDU-TIMING-SPECIFICATIONS",
    "I-SIGNAL-TO-PDU-MAPPINGS",
    "UNUSED-BIT-PATTERN",
]

OWN_CHILD_ORDER = [
    "I-PDU-TIMING-SPECIFICATIONS",
    "I-SIGNAL-TO-PDU-MAPPINGS",
    "UNUSED-BIT-PATTERN",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<I-SIGNAL-I-PDU>", "<I-SIGNAL-I-PDU xmlns='%s'>" % NS, 1))


def _populate(ipdu: ISignalIPdu):
    value = Boolean()
    value.setValue(True)
    ipdu.setHasDynamicLength(value)

    length = UnlimitedInteger()
    length.setValue("8")
    ipdu.setLength(length)

    props = ContainedIPduProps()
    semantics = ContainedIPduCollectionSemanticsEnum()
    semantics.setValue(ContainedIPduCollectionSemanticsEnum.QUEUED)
    props.setCollectionSemantics(semantics)
    ipdu.setContainedIPduProps(props)

    timing = IPduTiming()
    minimum_delay = TimeValue()
    minimum_delay.setValue("0.01")
    timing.setMinimumDelay(minimum_delay)
    ipdu.setIPduTimingSpecification(timing)

    mapping = ipdu.createISignalToPduMapping("mapping1")
    start_position = UnlimitedInteger()
    start_position.setValue("0")
    mapping.setStartPosition(start_position)

    pattern = Integer()
    pattern.setValue("255")
    ipdu.setUnusedBitPattern(pattern)


def _write(ipdu: ISignalIPdu) -> ET.Element:
    parent = ET.Element("AR-PACKAGE")
    ARXMLWriter().writeISignalIPdu(parent, ipdu)
    return parent.find("I-SIGNAL-I-PDU")


class TestWriteISignalIPdu:
    def test_write_empty(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        node = _write(ipdu)

        for tag in OWN_CHILD_ORDER:
            assert node.find(tag) is None, tag

    def test_write_full_child_order_matches_xsd(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        _populate(ipdu)

        node = _write(ipdu)
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        _populate(ipdu)

        node = _write(ipdu)
        assert node.find("HAS-DYNAMIC-LENGTH").text == "true"
        assert node.find("LENGTH").text == "8"

        props_node = node.find("CONTAINED-I-PDU-PROPS")
        assert props_node.find("COLLECTION-SEMANTICS").text == "QUEUED"

        timing_node = node.find("I-PDU-TIMING-SPECIFICATIONS/I-PDU-TIMING")
        assert timing_node.find("MINIMUM-DELAY").text == "0.01"

        mapping_node = node.find("I-SIGNAL-TO-PDU-MAPPINGS/I-SIGNAL-TO-I-PDU-MAPPING")
        assert mapping_node.find("SHORT-NAME").text == "mapping1"

        assert node.find("UNUSED-BIT-PATTERN").text == "255"

    def test_round_trip_full(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        _populate(ipdu)

        node = _write(ipdu)
        reloaded = ISignalIPdu(None, "ISignalIPdu1")
        ARXMLParser().readISignalIPdu(_with_ns(node), reloaded)

        assert reloaded.getShortName() == "ISignalIPdu1"
        assert reloaded.getHasDynamicLength().getValue() is True
        assert reloaded.getLength().getValue() == 8

        props = reloaded.getContainedIPduProps()
        assert isinstance(props, ContainedIPduProps)
        assert props.getCollectionSemantics().getValue() == "QUEUED"

        timing = reloaded.getIPduTimingSpecification()
        assert isinstance(timing, IPduTiming)
        assert timing.getMinimumDelay().getValue() == 0.01

        mappings = reloaded.getISignalToPduMappings()
        assert len(mappings) == 1
        assert mappings[0].getShortName() == "mapping1"
        assert mappings[0].getStartPosition().getValue() == 0

        assert reloaded.getUnusedBitPattern().getValue() == 255

    def test_round_trip_empty_wrapper_list(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        value = Boolean()
        value.setValue(True)
        ipdu.setHasDynamicLength(value)

        node = _write(ipdu)
        assert node.find("I-SIGNAL-TO-PDU-MAPPINGS") is None

        reloaded = ISignalIPdu(None, "ISignalIPdu1")
        ARXMLParser().readISignalIPdu(_with_ns(node), reloaded)

        assert reloaded.getISignalToPduMappings() == []
        assert reloaded.getIPduTimingSpecification() is None
        assert reloaded.getUnusedBitPattern() is None
        assert reloaded.getContainedIPduProps() is None
