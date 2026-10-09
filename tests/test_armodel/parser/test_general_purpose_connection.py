"""Parser tests for GeneralPurposeConnection (Table 6.58, p.388).

The GENERAL-PURPOSE-CONNECTION group of AUTOSAR_00052.xsd (l.63807) holds the
single optional wrapper PDU-TRIGGERING-REFS over an unbounded choice of
PDU-TRIGGERING-REF (DEST = PDU-TRIGGERING-SUBTYPES-ENUM); the complexType
(l.63836) stacks the base groups AR-OBJECT .. AR-ELEMENT in front of it. The
tests exercise readGeneralPurposeConnection, which must call readIdentifiable
for the base level (UUID/CATEGORY/S/T) and read the wrapper list via the
addPduTriggeringRef mutator.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import GeneralPurposeConnection
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

UUID_VALUE = "3c2b1a0f-9e8d-4c7b-a6f5-1e2d3c4b5a69"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadGeneralPurposeConnection:
    def test_read_full(self):
        xml = f"""<GENERAL-PURPOSE-CONNECTION xmlns='{NS}'>
            <SHORT-NAME>GeneralPurposeConnection1</SHORT-NAME>
            <PDU-TRIGGERING-REFS>
                <PDU-TRIGGERING-REF DEST='PDU-TRIGGERING-SUBTYPES-ENUM'>/PduTriggerings/RequestTriggering</PDU-TRIGGERING-REF>
                <PDU-TRIGGERING-REF DEST='PDU-TRIGGERING-SUBTYPES-ENUM'>/PduTriggerings/ResponseTriggering</PDU-TRIGGERING-REF>
            </PDU-TRIGGERING-REFS>
        </GENERAL-PURPOSE-CONNECTION>"""
        connection = GeneralPurposeConnection(None, "GeneralPurposeConnection1")
        ARXMLParser().readGeneralPurposeConnection(ET.fromstring(xml), connection)

        assert connection.getShortName() == "GeneralPurposeConnection1"
        refs = connection.getPduTriggeringRefs()
        assert len(refs) == 2
        assert refs[0].getDest() == "PDU-TRIGGERING-SUBTYPES-ENUM"
        assert refs[0].getValue() == "/PduTriggerings/RequestTriggering"
        assert refs[1].getDest() == "PDU-TRIGGERING-SUBTYPES-ENUM"
        assert refs[1].getValue() == "/PduTriggerings/ResponseTriggering"

    def test_read_base_level_attributes(self):
        xml = f"""<GENERAL-PURPOSE-CONNECTION xmlns='{NS}' UUID='{UUID_VALUE}' S='5' T='2025-04-04T00:00:00Z'>
            <SHORT-NAME>GeneralPurposeConnection1</SHORT-NAME>
            <CATEGORY>CONN</CATEGORY>
        </GENERAL-PURPOSE-CONNECTION>"""
        connection = GeneralPurposeConnection(None, "GeneralPurposeConnection1")
        ARXMLParser().readGeneralPurposeConnection(ET.fromstring(xml), connection)

        assert connection.getUuid().getValue() == UUID_VALUE
        assert connection.getChecksum().getValue() == "5"
        assert connection.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert connection.getCategory().getValue() == "CONN"

    def test_read_empty(self):
        element = ET.fromstring(f"<GENERAL-PURPOSE-CONNECTION xmlns='{NS}'><SHORT-NAME>GeneralPurposeConnection1</SHORT-NAME></GENERAL-PURPOSE-CONNECTION>")
        connection = GeneralPurposeConnection(None, "GeneralPurposeConnection1")
        ARXMLParser().readGeneralPurposeConnection(element, connection)

        assert connection.getShortName() == "GeneralPurposeConnection1"
        assert connection.getPduTriggeringRefs() == []

    def test_read_empty_wrapper_list(self):
        xml = f"""<GENERAL-PURPOSE-CONNECTION xmlns='{NS}'>
            <SHORT-NAME>GeneralPurposeConnection1</SHORT-NAME>
            <PDU-TRIGGERING-REFS/>
        </GENERAL-PURPOSE-CONNECTION>"""
        connection = GeneralPurposeConnection(None, "GeneralPurposeConnection1")
        ARXMLParser().readGeneralPurposeConnection(ET.fromstring(xml), connection)

        assert connection.getPduTriggeringRefs() == []
