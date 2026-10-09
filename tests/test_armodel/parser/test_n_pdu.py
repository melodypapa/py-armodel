"""Parser tests for NPdu (Table 6.21, p.343).

NPdu adds no own children: the N-PDU group of AUTOSAR_00052.xsd (l.83999) is an
empty <xsd:sequence/> and the N-PDU complexType (l.84009) stacks the inherited
groups AR-OBJECT .. PDU, I-PDU, N-PDU. The tests exercise readNPdu, which must
dispatch to readIPdu (Base = IPdu) exactly once for the inherited levels — the
Pdu level (HAS-DYNAMIC-LENGTH, LENGTH), the IPdu level (CONTAINED-I-PDU-PROPS)
and the ARObject/Identifiable base attributes (S/T, UUID).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduProps,
    NPdu,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

UUID_VALUE = "4f4a5b6c-7d8e-49a0-b1c2-3d4e5f6a7b8d"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadNPdu:
    def test_read_full(self):
        xml = f"""<N-PDU xmlns='{NS}' UUID='{UUID_VALUE}'>
            <SHORT-NAME>NPdu1</SHORT-NAME>
            <HAS-DYNAMIC-LENGTH>true</HAS-DYNAMIC-LENGTH>
            <LENGTH>8</LENGTH>
            <CONTAINED-I-PDU-PROPS>
                <COLLECTION-SEMANTICS>QUEUED</COLLECTION-SEMANTICS>
                <HEADER-ID-SHORT-HEADER>4</HEADER-ID-SHORT-HEADER>
            </CONTAINED-I-PDU-PROPS>
        </N-PDU>"""
        pdu = NPdu(None, "NPdu1")
        ARXMLParser().readNPdu(ET.fromstring(xml), pdu)

        assert pdu.getShortName() == "NPdu1"
        assert isinstance(pdu.getHasDynamicLength(), Boolean)
        assert pdu.getHasDynamicLength().getValue() is True
        assert isinstance(pdu.getLength(), UnlimitedInteger)
        assert pdu.getLength().getValue() == 8

        props = pdu.getContainedIPduProps()
        assert isinstance(props, ContainedIPduProps)
        assert props.getCollectionSemantics().getValue() == "QUEUED"
        assert props.getHeaderIdShortHeader().getValue() == 4

    def test_read_base_level_attributes(self):
        xml = f"""<N-PDU xmlns='{NS}' UUID='{UUID_VALUE}' S='5' T='2025-04-04T00:00:00Z'>
            <SHORT-NAME>NPdu1</SHORT-NAME>
        </N-PDU>"""
        pdu = NPdu(None, "NPdu1")
        ARXMLParser().readNPdu(ET.fromstring(xml), pdu)

        assert pdu.getUuid().getValue() == UUID_VALUE
        assert pdu.getChecksum().getValue() == "5"
        assert pdu.getTimestamp().getValue() == "2025-04-04T00:00:00Z"

    def test_read_minimal(self):
        element = ET.fromstring(f"<N-PDU xmlns='{NS}'><SHORT-NAME>NPdu1</SHORT-NAME></N-PDU>")
        pdu = NPdu(None, "NPdu1")
        ARXMLParser().readNPdu(element, pdu)

        assert pdu.getShortName() == "NPdu1"
        assert pdu.getHasDynamicLength() is None
        assert pdu.getLength() is None
        assert pdu.getContainedIPduProps() is None
