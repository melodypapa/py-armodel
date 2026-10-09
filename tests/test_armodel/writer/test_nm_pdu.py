"""Writer round-trip tests for NmPdu (Table 6.20, p.343).

Serialized through writeNmPdu; own child set and order per the NM-PDU group of
AUTOSAR_00052.xsd (l.85128), sequenced after the PDU group in the NM-PDU
complexType (l.85172). The I-SIGNAL-TO-I-PDU-MAPPINGS aggregation carries a
variation point that "shall not exist in models" (XSD doc, constr_2638) and is
not modeled. The tests exercise writeNmPdu, which must dispatch to writePdu
(Base = Pdu) exactly once for the inherited levels.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    NmPdu,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "HAS-DYNAMIC-LENGTH",
    "LENGTH",
    "I-SIGNAL-TO-I-PDU-MAPPINGS",
    "NM-DATA-INFORMATION",
    "NM-VOTE-INFORMATION",
    "UNUSED-BIT-PATTERN",
]

OWN_CHILD_ORDER = [
    "I-SIGNAL-TO-I-PDU-MAPPINGS",
    "NM-DATA-INFORMATION",
    "NM-VOTE-INFORMATION",
    "UNUSED-BIT-PATTERN",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<NM-PDU>", "<NM-PDU xmlns='%s'>" % NS, 1))


def _populate(pdu: NmPdu):
    has_dynamic_length = Boolean()
    has_dynamic_length.setValue(False)
    pdu.setHasDynamicLength(has_dynamic_length)

    length = UnlimitedInteger()
    length.setValue("8")
    pdu.setLength(length)

    mapping = pdu.createISignalToIPduMapping("mapping1")
    start_position = UnlimitedInteger()
    start_position.setValue("0")
    mapping.setStartPosition(start_position)

    nm_data_information = Boolean()
    nm_data_information.setValue(True)
    pdu.setNmDataInformation(nm_data_information)

    nm_vote_information = Boolean()
    nm_vote_information.setValue(False)
    pdu.setNmVoteInformation(nm_vote_information)

    pattern = Integer()
    pattern.setValue("255")
    pdu.setUnusedBitPattern(pattern)


def _write(pdu: NmPdu) -> ET.Element:
    parent = ET.Element("AR-PACKAGE")
    ARXMLWriter().writeNmPdu(parent, pdu)
    return parent.find("NM-PDU")


class TestWriteNmPdu:
    def test_write_empty(self):
        pdu = NmPdu(None, "NmPdu1")
        node = _write(pdu)

        for tag in OWN_CHILD_ORDER:
            assert node.find(tag) is None, tag

    def test_write_full_child_order_matches_xsd(self):
        pdu = NmPdu(None, "NmPdu1")
        _populate(pdu)

        node = _write(pdu)
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        pdu = NmPdu(None, "NmPdu1")
        _populate(pdu)

        node = _write(pdu)
        assert node.find("HAS-DYNAMIC-LENGTH").text == "false"
        assert node.find("LENGTH").text == "8"

        mapping_node = node.find("I-SIGNAL-TO-I-PDU-MAPPINGS/I-SIGNAL-TO-I-PDU-MAPPING")
        assert mapping_node.find("SHORT-NAME").text == "mapping1"

        assert node.find("NM-DATA-INFORMATION").text == "true"
        assert node.find("NM-VOTE-INFORMATION").text == "false"
        assert node.find("UNUSED-BIT-PATTERN").text == "255"

    def test_round_trip_full(self):
        pdu = NmPdu(None, "NmPdu1")
        _populate(pdu)

        node = _write(pdu)
        reloaded = NmPdu(None, "NmPdu1")
        ARXMLParser().readNmPdu(_with_ns(node), reloaded)

        assert reloaded.getShortName() == "NmPdu1"
        assert reloaded.getHasDynamicLength().getValue() is False
        assert reloaded.getLength().getValue() == 8

        mappings = reloaded.getISignalToIPduMappings()
        assert len(mappings) == 1
        assert mappings[0].getShortName() == "mapping1"
        assert mappings[0].getStartPosition().getValue() == 0

        assert reloaded.getNmDataInformation().getValue() is True
        assert reloaded.getNmVoteInformation().getValue() is False
        assert reloaded.getUnusedBitPattern().getValue() == 255

    def test_round_trip_empty_wrapper_list(self):
        pdu = NmPdu(None, "NmPdu1")
        nm_data_information = Boolean()
        nm_data_information.setValue(True)
        pdu.setNmDataInformation(nm_data_information)

        node = _write(pdu)
        assert node.find("I-SIGNAL-TO-I-PDU-MAPPINGS") is None

        reloaded = NmPdu(None, "NmPdu1")
        ARXMLParser().readNmPdu(_with_ns(node), reloaded)

        assert reloaded.getISignalToIPduMappings() == []
        assert reloaded.getNmDataInformation().getValue() is True
        assert reloaded.getNmVoteInformation() is None
        assert reloaded.getUnusedBitPattern() is None
