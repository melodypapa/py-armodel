"""Parser tests for ISignalToIPduMapping (Table 6.14, p.326).

Child set and order per the I-SIGNAL-TO-I-PDU-MAPPING group of AUTOSAR_00052.xsd (l.67391).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import UnlimitedInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalToIPduMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_XML = f"""<I-SIGNAL-TO-I-PDU-MAPPING xmlns='{NS}' UUID='1a2b3c4d-5e6f-47a8-9b0c-1d2e3f4a5b6c'>
    <SHORT-NAME>Mapping1</SHORT-NAME>
    <I-SIGNAL-GROUP-REF DEST='I-SIGNAL-GROUP'>/AUTOSAR/ISignalGroups/Group1</I-SIGNAL-GROUP-REF>
    <I-SIGNAL-REF DEST='I-SIGNAL'>/AUTOSAR/ISignals/Signal1</I-SIGNAL-REF>
    <PACKING-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-LAST</PACKING-BYTE-ORDER>
    <START-POSITION>8</START-POSITION>
    <TRANSFER-PROPERTY>TRIGGERED</TRANSFER-PROPERTY>
    <UPDATE-INDICATION-BIT-POSITION>3</UPDATE-INDICATION-BIT-POSITION>
    <VARIATION-POINT>
        <SHORT-LABEL>vp_label</SHORT-LABEL>
    </VARIATION-POINT>
</I-SIGNAL-TO-I-PDU-MAPPING>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadISignalToIPduMapping:
    def test_read_full(self):
        mapping = ISignalToIPduMapping(None, "Mapping1")
        ARXMLParser().readISignalToIPduMapping(ET.fromstring(FULL_XML), mapping)

        assert mapping.getShortName() == "Mapping1"
        assert mapping.getUuid().getValue() == "1a2b3c4d-5e6f-47a8-9b0c-1d2e3f4a5b6c"
        assert mapping.getISignalGroupRef().getValue() == "/AUTOSAR/ISignalGroups/Group1"
        assert mapping.getISignalGroupRef().getDest() == "I-SIGNAL-GROUP"
        assert mapping.getISignalRef().getValue() == "/AUTOSAR/ISignals/Signal1"
        assert mapping.getISignalRef().getDest() == "I-SIGNAL"
        assert mapping.getPackingByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-LAST"
        assert isinstance(mapping.getStartPosition(), UnlimitedInteger)
        assert mapping.getStartPosition().getValue() == 8
        assert mapping.getTransferProperty().getValue() == "TRIGGERED"
        assert isinstance(mapping.getUpdateIndicationBitPosition(), UnlimitedInteger)
        assert mapping.getUpdateIndicationBitPosition().getValue() == 3
        assert mapping.getVariationPoint() is not None
        assert mapping.getVariationPoint().getShortLabel().getValue() == "vp_label"

    def test_read_minimal(self):
        mapping = ISignalToIPduMapping(None, "Mapping1")
        element = ET.fromstring(f"<I-SIGNAL-TO-I-PDU-MAPPING xmlns='{NS}'><SHORT-NAME>Mapping1</SHORT-NAME></I-SIGNAL-TO-I-PDU-MAPPING>")
        ARXMLParser().readISignalToIPduMapping(element, mapping)

        assert mapping.getShortName() == "Mapping1"
        assert mapping.getISignalRef() is None
        assert mapping.getISignalGroupRef() is None
        assert mapping.getPackingByteOrder() is None
        assert mapping.getStartPosition() is None
        assert mapping.getTransferProperty() is None
        assert mapping.getUpdateIndicationBitPosition() is None
        assert mapping.getVariationPoint() is None
