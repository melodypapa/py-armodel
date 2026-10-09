"""Parser tests for CryptoServiceKey (Table 6.51, p.377).

The CRYPTO-SERVICE-KEY group of AUTOSAR_00052.xsd (l.26314) holds ALGORITHM-FAMILY
(STRING), DEVELOPMENT-VALUE (polymorphic choice of 12 ValueSpecification subtypes),
KEY-GENERATION (CRYPTO-SERVICE-KEY-GENERATION-ENUM), KEY-STORAGE-TYPE (STRING) and
LENGTH (POSITIVE-INTEGER), all minOccurs=0 maxOccurs=1; the CRYPTO-SERVICE-KEY
complexType (l.26371) stacks the base groups AR-OBJECT .. AR-ELEMENT in front of
it. The tests exercise readCryptoServiceKey, which must call readIdentifiable for
the base level (UUID/CATEGORY/S/T) and read each child via its mutator in XSD
sequence order.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CryptoServiceKey
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

UUID_VALUE = "7a1b2c3d-4e5f-4a6b-8c9d-0e1f2a3b4c5d"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadCryptoServiceKey:
    def test_read_full(self):
        xml = f"""<CRYPTO-SERVICE-KEY xmlns='{NS}'>
            <SHORT-NAME>CryptoServiceKey1</SHORT-NAME>
            <ALGORITHM-FAMILY>AES</ALGORITHM-FAMILY>
            <DEVELOPMENT-VALUE>
                <TEXT-VALUE-SPECIFICATION>
                    <SHORT-LABEL>dev</SHORT-LABEL>
                    <VALUE>0xAFFE</VALUE>
                </TEXT-VALUE-SPECIFICATION>
            </DEVELOPMENT-VALUE>
            <KEY-GENERATION>KEY-DERIVATION</KEY-GENERATION>
            <KEY-STORAGE-TYPE>LOCAL</KEY-STORAGE-TYPE>
            <LENGTH>256</LENGTH>
        </CRYPTO-SERVICE-KEY>"""
        key = CryptoServiceKey(None, "CryptoServiceKey1")
        ARXMLParser().readCryptoServiceKey(ET.fromstring(xml), key)

        assert key.getShortName() == "CryptoServiceKey1"
        assert isinstance(key.getAlgorithmFamily(), String)
        assert key.getAlgorithmFamily().getValue() == "AES"

        dev_value = key.getDevelopmentValue()
        assert dev_value is not None
        assert dev_value.getValue().getValue() == "0xAFFE"
        assert dev_value.getShortLabel().getValue() == "dev"

        assert key.getKeyGeneration() is not None
        assert key.getKeyGeneration().getValue() == "KEY-DERIVATION"

        assert isinstance(key.getKeyStorageType(), String)
        assert key.getKeyStorageType().getValue() == "LOCAL"

        assert isinstance(key.getLength(), PositiveInteger)
        assert key.getLength().getValue() == 256

    def test_read_development_value_polymorphic(self):
        xml = f"""<CRYPTO-SERVICE-KEY xmlns='{NS}'>
            <SHORT-NAME>CryptoServiceKey1</SHORT-NAME>
            <DEVELOPMENT-VALUE>
                <NUMERICAL-VALUE-SPECIFICATION>
                    <VALUE>8</VALUE>
                </NUMERICAL-VALUE-SPECIFICATION>
            </DEVELOPMENT-VALUE>
        </CRYPTO-SERVICE-KEY>"""
        key = CryptoServiceKey(None, "CryptoServiceKey1")
        ARXMLParser().readCryptoServiceKey(ET.fromstring(xml), key)

        assert key.getDevelopmentValue() is not None
        assert key.getDevelopmentValue().getValue().getValue() == 8

    def test_read_base_level_attributes(self):
        xml = f"""<CRYPTO-SERVICE-KEY xmlns='{NS}' UUID='{UUID_VALUE}' S='5' T='2025-04-04T00:00:00Z'>
            <SHORT-NAME>CryptoServiceKey1</SHORT-NAME>
            <CATEGORY>CRYPTO</CATEGORY>
        </CRYPTO-SERVICE-KEY>"""
        key = CryptoServiceKey(None, "CryptoServiceKey1")
        ARXMLParser().readCryptoServiceKey(ET.fromstring(xml), key)

        assert key.getUuid().getValue() == UUID_VALUE
        assert key.getChecksum().getValue() == "5"
        assert key.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert key.getCategory().getValue() == "CRYPTO"

    def test_read_empty(self):
        element = ET.fromstring(f"<CRYPTO-SERVICE-KEY xmlns='{NS}'><SHORT-NAME>CryptoServiceKey1</SHORT-NAME></CRYPTO-SERVICE-KEY>")
        key = CryptoServiceKey(None, "CryptoServiceKey1")
        ARXMLParser().readCryptoServiceKey(element, key)

        assert key.getShortName() == "CryptoServiceKey1"
        assert key.getAlgorithmFamily() is None
        assert key.getDevelopmentValue() is None
        assert key.getKeyGeneration() is None
        assert key.getKeyStorageType() is None
        assert key.getLength() is None
