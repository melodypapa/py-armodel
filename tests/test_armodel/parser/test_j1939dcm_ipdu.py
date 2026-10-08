"""Parser tests for J1939DcmIPdu (Table 6.24, p.344).

The J-1939-DCM-I-PDU group of AUTOSAR_00052.xsd (l.75299) adds one own child,
DIAGNOSTIC-MESSAGE-TYPE (POSITIVE-INTEGER, minOccurs=0, maxOccurs=1); the
J-1939-DCM-I-PDU complexType (l.75315) stacks the inherited groups AR-OBJECT ..
PDU, I-PDU, J-1939-DCM-I-PDU. The tests exercise readJ1939DcmIPdu, which must
dispatch to readIPdu (Base = IPdu) exactly once for the inherited levels — the
Pdu level (HAS-DYNAMIC-LENGTH, LENGTH), the IPdu level (CONTAINED-I-PDU-PROPS)
and the ARObject/Identifiable base attributes (S/T, UUID) — and read the own
DIAGNOSTIC-MESSAGE-TYPE child.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduProps,
    J1939DcmIPdu,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

UUID_VALUE = "5f4a5b6c-7d8e-49a0-b1c2-3d4e5f6a7b8e"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadJ1939DcmIPdu:
    def test_read_full(self):
        xml = f"""<J-1939-DCM-I-PDU xmlns='{NS}' UUID='{UUID_VALUE}'>
            <SHORT-NAME>J1939DcmIPdu1</SHORT-NAME>
            <HAS-DYNAMIC-LENGTH>true</HAS-DYNAMIC-LENGTH>
            <LENGTH>8</LENGTH>
            <CONTAINED-I-PDU-PROPS>
                <COLLECTION-SEMANTICS>QUEUED</COLLECTION-SEMANTICS>
                <HEADER-ID-SHORT-HEADER>4</HEADER-ID-SHORT-HEADER>
            </CONTAINED-I-PDU-PROPS>
            <DIAGNOSTIC-MESSAGE-TYPE>1</DIAGNOSTIC-MESSAGE-TYPE>
        </J-1939-DCM-I-PDU>"""
        pdu = J1939DcmIPdu(None, "J1939DcmIPdu1")
        ARXMLParser().readJ1939DcmIPdu(ET.fromstring(xml), pdu)

        assert pdu.getShortName() == "J1939DcmIPdu1"
        assert isinstance(pdu.getHasDynamicLength(), Boolean)
        assert pdu.getHasDynamicLength().getValue() is True
        assert isinstance(pdu.getLength(), UnlimitedInteger)
        assert pdu.getLength().getValue() == 8

        props = pdu.getContainedIPduProps()
        assert isinstance(props, ContainedIPduProps)
        assert props.getCollectionSemantics().getValue() == "QUEUED"
        assert props.getHeaderIdShortHeader().getValue() == 4

        assert pdu.getDiagnosticMessageType() is not None
        assert pdu.getDiagnosticMessageType().getValue() == 1

    def test_read_base_level_attributes(self):
        xml = f"""<J-1939-DCM-I-PDU xmlns='{NS}' UUID='{UUID_VALUE}' S='5' T='2025-04-04T00:00:00Z'>
            <SHORT-NAME>J1939DcmIPdu1</SHORT-NAME>
        </J-1939-DCM-I-PDU>"""
        pdu = J1939DcmIPdu(None, "J1939DcmIPdu1")
        ARXMLParser().readJ1939DcmIPdu(ET.fromstring(xml), pdu)

        assert pdu.getUuid().getValue() == UUID_VALUE
        assert pdu.getChecksum().getValue() == "5"
        assert pdu.getTimestamp().getValue() == "2025-04-04T00:00:00Z"

    def test_read_minimal(self):
        element = ET.fromstring(f"<J-1939-DCM-I-PDU xmlns='{NS}'><SHORT-NAME>J1939DcmIPdu1</SHORT-NAME></J-1939-DCM-I-PDU>")
        pdu = J1939DcmIPdu(None, "J1939DcmIPdu1")
        ARXMLParser().readJ1939DcmIPdu(element, pdu)

        assert pdu.getShortName() == "J1939DcmIPdu1"
        assert pdu.getDiagnosticMessageType() is None
        assert pdu.getHasDynamicLength() is None
        assert pdu.getLength() is None
        assert pdu.getContainedIPduProps() is None


class TestReadJ1939DcmIPduDispatch:
    def test_read_arpackage_elements_dispatch(self):
        xml = f"""<AR-PACKAGE xmlns='{NS}'>
            <SHORT-NAME>Pdus</SHORT-NAME>
            <ELEMENTS>
                <J-1939-DCM-I-PDU>
                    <SHORT-NAME>J1939DcmIPdu1</SHORT-NAME>
                    <DIAGNOSTIC-MESSAGE-TYPE>57</DIAGNOSTIC-MESSAGE-TYPE>
                </J-1939-DCM-I-PDU>
            </ELEMENTS>
        </AR-PACKAGE>"""
        package = ARPackage(None, "Pdus")
        ARXMLParser().readARPackageElements(ET.fromstring(xml), package)

        pdu = package.getReferrableElement("J1939DcmIPdu1", J1939DcmIPdu)
        assert isinstance(pdu, J1939DcmIPdu)
        assert pdu.getDiagnosticMessageType().getValue() == 57
