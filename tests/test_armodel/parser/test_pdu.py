"""Parser tests for Pdu (Table 6.17, p.340).

Child set and order per the PDU group of AUTOSAR_00052.xsd (l.88521). Pdu is abstract:
the tests exercise the reusable readPdu helper that concrete subclasses (NmPdu, IPdu,
GeneralPurposePdu, UserDefinedPdu) call on their own wrapper element.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Pdu
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class ConcretePdu(Pdu):
    pass


FULL_XML = f"""<PDU xmlns='{NS}' UUID='1a2b3c4d-5e6f-47a8-9b0c-1d2e3f4a5b6c'>
    <SHORT-NAME>Pdu1</SHORT-NAME>
    <HAS-DYNAMIC-LENGTH>true</HAS-DYNAMIC-LENGTH>
    <LENGTH>8</LENGTH>
</PDU>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadPdu:
    def test_read_full(self):
        pdu = ConcretePdu(None, "Pdu1")
        ARXMLParser().readPdu(ET.fromstring(FULL_XML), pdu)

        assert pdu.getShortName() == "Pdu1"
        assert pdu.getUuid().getValue() == "1a2b3c4d-5e6f-47a8-9b0c-1d2e3f4a5b6c"
        assert isinstance(pdu.getHasDynamicLength(), Boolean)
        assert pdu.getHasDynamicLength().getValue() is True
        assert isinstance(pdu.getLength(), UnlimitedInteger)
        assert pdu.getLength().getValue() == 8

    def test_read_minimal(self):
        pdu = ConcretePdu(None, "Pdu1")
        element = ET.fromstring(f"<PDU xmlns='{NS}'><SHORT-NAME>Pdu1</SHORT-NAME></PDU>")
        ARXMLParser().readPdu(element, pdu)

        assert pdu.getShortName() == "Pdu1"
        assert pdu.getUuid() is None
        assert pdu.getHasDynamicLength() is None
        assert pdu.getLength() is None
