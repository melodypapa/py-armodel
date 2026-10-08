"""Parser tests for NmPdu (Table 6.20, p.343).

Own child set and order per the NM-PDU group of AUTOSAR_00052.xsd (l.85128),
sequenced after the PDU group in the NM-PDU complexType (l.85172). The
I-SIGNAL-TO-I-PDU-MAPPINGS aggregation carries a variation point that "shall not
exist in models" (XSD doc, constr_2638) and is not modeled. The tests exercise
readNmPdu, which must dispatch to readPdu (Base = Pdu) exactly once for the
inherited levels.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignalToIPduMapping,
    NmPdu,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_XML = f"""<NM-PDU xmlns='{NS}' UUID='4f4a5b6c-7d8e-49a0-b1c2-3d4e5f6a7b8d'>
    <SHORT-NAME>NmPdu1</SHORT-NAME>
    <HAS-DYNAMIC-LENGTH>false</HAS-DYNAMIC-LENGTH>
    <LENGTH>8</LENGTH>
    <I-SIGNAL-TO-I-PDU-MAPPINGS>
        <I-SIGNAL-TO-I-PDU-MAPPING>
            <SHORT-NAME>mapping1</SHORT-NAME>
            <START-POSITION>0</START-POSITION>
        </I-SIGNAL-TO-I-PDU-MAPPING>
    </I-SIGNAL-TO-I-PDU-MAPPINGS>
    <NM-DATA-INFORMATION>true</NM-DATA-INFORMATION>
    <NM-VOTE-INFORMATION>false</NM-VOTE-INFORMATION>
    <UNUSED-BIT-PATTERN>255</UNUSED-BIT-PATTERN>
</NM-PDU>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadNmPdu:
    def test_read_full(self):
        pdu = NmPdu(None, "NmPdu1")
        ARXMLParser().readNmPdu(ET.fromstring(FULL_XML), pdu)

        assert pdu.getShortName() == "NmPdu1"
        assert isinstance(pdu.getHasDynamicLength(), Boolean)
        assert pdu.getHasDynamicLength().getValue() is False
        assert isinstance(pdu.getLength(), UnlimitedInteger)
        assert pdu.getLength().getValue() == 8

        mappings = pdu.getISignalToIPduMappings()
        assert len(mappings) == 1
        mapping = mappings[0]
        assert isinstance(mapping, ISignalToIPduMapping)
        assert mapping.getShortName() == "mapping1"
        assert mapping.getStartPosition().getValue() == 0

        assert isinstance(pdu.getNmDataInformation(), Boolean)
        assert pdu.getNmDataInformation().getValue() is True
        assert isinstance(pdu.getNmVoteInformation(), Boolean)
        assert pdu.getNmVoteInformation().getValue() is False

        assert isinstance(pdu.getUnusedBitPattern(), Integer)
        assert pdu.getUnusedBitPattern().getValue() == 255

    def test_read_minimal(self):
        pdu = NmPdu(None, "NmPdu1")
        element = ET.fromstring(f"<NM-PDU xmlns='{NS}'><SHORT-NAME>NmPdu1</SHORT-NAME></NM-PDU>")
        ARXMLParser().readNmPdu(element, pdu)

        assert pdu.getShortName() == "NmPdu1"
        assert pdu.getHasDynamicLength() is None
        assert pdu.getLength() is None
        assert pdu.getISignalToIPduMappings() == []
        assert pdu.getNmDataInformation() is None
        assert pdu.getNmVoteInformation() is None
        assert pdu.getUnusedBitPattern() is None
