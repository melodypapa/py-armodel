"""Parser tests for DcmIPdu (Table 6.22, p.343).

The DCM-I-PDU group of AUTOSAR_00052.xsd (l.28516) adds one own child,
DIAG-PDU-TYPE (minOccurs=0, maxOccurs=1); the DCM-I-PDU complexType (l.28532)
stacks the inherited groups AR-OBJECT .. PDU, I-PDU, DCM-I-PDU. The tests
exercise readDcmIPdu, which must dispatch to readIPdu (Base = IPdu) exactly
once for the inherited levels — the Pdu level (HAS-DYNAMIC-LENGTH, LENGTH),
the IPdu level (CONTAINED-I-PDU-PROPS) and the ARObject/Identifiable base
attributes (S/T, UUID) — and read the own DIAG-PDU-TYPE child.
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
    DcmIPdu,
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


class TestReadDcmIPdu:
    def test_read_full(self):
        xml = f"""<DCM-I-PDU xmlns='{NS}' UUID='{UUID_VALUE}'>
            <SHORT-NAME>DcmIPdu1</SHORT-NAME>
            <HAS-DYNAMIC-LENGTH>true</HAS-DYNAMIC-LENGTH>
            <LENGTH>8</LENGTH>
            <CONTAINED-I-PDU-PROPS>
                <COLLECTION-SEMANTICS>QUEUED</COLLECTION-SEMANTICS>
                <HEADER-ID-SHORT-HEADER>4</HEADER-ID-SHORT-HEADER>
            </CONTAINED-I-PDU-PROPS>
            <DIAG-PDU-TYPE>DIAG-REQUEST</DIAG-PDU-TYPE>
        </DCM-I-PDU>"""
        pdu = DcmIPdu(None, "DcmIPdu1")
        ARXMLParser().readDcmIPdu(ET.fromstring(xml), pdu)

        assert pdu.getShortName() == "DcmIPdu1"
        assert isinstance(pdu.getHasDynamicLength(), Boolean)
        assert pdu.getHasDynamicLength().getValue() is True
        assert isinstance(pdu.getLength(), UnlimitedInteger)
        assert pdu.getLength().getValue() == 8

        props = pdu.getContainedIPduProps()
        assert isinstance(props, ContainedIPduProps)
        assert props.getCollectionSemantics().getValue() == "QUEUED"
        assert props.getHeaderIdShortHeader().getValue() == 4

        assert pdu.getDiagPduType() is not None
        assert pdu.getDiagPduType().getValue() == "DIAG-REQUEST"

    def test_read_base_level_attributes(self):
        xml = f"""<DCM-I-PDU xmlns='{NS}' UUID='{UUID_VALUE}' S='5' T='2025-04-04T00:00:00Z'>
            <SHORT-NAME>DcmIPdu1</SHORT-NAME>
        </DCM-I-PDU>"""
        pdu = DcmIPdu(None, "DcmIPdu1")
        ARXMLParser().readDcmIPdu(ET.fromstring(xml), pdu)

        assert pdu.getUuid().getValue() == UUID_VALUE
        assert pdu.getChecksum().getValue() == "5"
        assert pdu.getTimestamp().getValue() == "2025-04-04T00:00:00Z"

    def test_read_minimal(self):
        element = ET.fromstring(f"<DCM-I-PDU xmlns='{NS}'><SHORT-NAME>DcmIPdu1</SHORT-NAME></DCM-I-PDU>")
        pdu = DcmIPdu(None, "DcmIPdu1")
        ARXMLParser().readDcmIPdu(element, pdu)

        assert pdu.getShortName() == "DcmIPdu1"
        assert pdu.getDiagPduType() is None
        assert pdu.getHasDynamicLength() is None
        assert pdu.getLength() is None
        assert pdu.getContainedIPduProps() is None
