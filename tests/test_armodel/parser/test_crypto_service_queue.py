"""Parser tests for CryptoServiceQueue (Table 6.53, p.381).

The CRYPTO-SERVICE-QUEUE group of AUTOSAR_00052.xsd (l.26525) holds QUEUE-SIZE
(POSITIVE-INTEGER, minOccurs=0 maxOccurs=1); the CRYPTO-SERVICE-QUEUE
complexType (l.26541) stacks the base groups AR-OBJECT .. AR-ELEMENT in front
of it. The tests exercise readCryptoServiceQueue, which must call
readIdentifiable for the base level (UUID/CATEGORY/S/T) and read QUEUE-SIZE
via the setQueueSize mutator in XSD sequence order.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CryptoServiceQueue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

UUID_VALUE = "7a1b2c3d-4e5f-4a6b-8c9d-0e1f2a3b4c5d"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadCryptoServiceQueue:
    def test_read_full(self):
        xml = f"""<CRYPTO-SERVICE-QUEUE xmlns='{NS}'>
            <SHORT-NAME>CryptoServiceQueue1</SHORT-NAME>
            <QUEUE-SIZE>32</QUEUE-SIZE>
        </CRYPTO-SERVICE-QUEUE>"""
        queue = CryptoServiceQueue(None, "CryptoServiceQueue1")
        ARXMLParser().readCryptoServiceQueue(ET.fromstring(xml), queue)

        assert queue.getShortName() == "CryptoServiceQueue1"
        assert isinstance(queue.getQueueSize(), PositiveInteger)
        assert queue.getQueueSize().getValue() == 32

    def test_read_base_level_attributes(self):
        xml = f"""<CRYPTO-SERVICE-QUEUE xmlns='{NS}' UUID='{UUID_VALUE}' S='5' T='2025-04-04T00:00:00Z'>
            <SHORT-NAME>CryptoServiceQueue1</SHORT-NAME>
            <CATEGORY>CRYPTO</CATEGORY>
        </CRYPTO-SERVICE-QUEUE>"""
        queue = CryptoServiceQueue(None, "CryptoServiceQueue1")
        ARXMLParser().readCryptoServiceQueue(ET.fromstring(xml), queue)

        assert queue.getUuid().getValue() == UUID_VALUE
        assert queue.getChecksum().getValue() == "5"
        assert queue.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert queue.getCategory().getValue() == "CRYPTO"

    def test_read_empty(self):
        element = ET.fromstring(f"<CRYPTO-SERVICE-QUEUE xmlns='{NS}'><SHORT-NAME>CryptoServiceQueue1</SHORT-NAME></CRYPTO-SERVICE-QUEUE>")
        queue = CryptoServiceQueue(None, "CryptoServiceQueue1")
        ARXMLParser().readCryptoServiceQueue(element, queue)

        assert queue.getShortName() == "CryptoServiceQueue1"
        assert queue.getQueueSize() is None
