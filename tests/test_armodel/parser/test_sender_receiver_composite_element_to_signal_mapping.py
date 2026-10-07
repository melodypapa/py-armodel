"""Reader tests for SenderReceiverCompositeElementToSignalMapping (Table 5.34, p.247).

XML group SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING (AUTOSAR_00052.xsd
l.104633): DATA-ELEMENT-IREF (VARIABLE-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF) +
SYSTEM-SIGNAL-REF + TYPE-MAPPING (choice of SENDER-REC-ARRAY-TYPE-MAPPING /
SENDER-REC-RECORD-TYPE-MAPPING), after the inherited DATA-MAPPING group.
Dispatched from SystemMapping DATA-MAPPINGS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderRecArrayTypeMapping,
    SenderReceiverCompositeElementToSignalMapping,
    SenderRecRecordTypeMapping,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _parse(xml: str) -> ET.Element:
    return ET.fromstring(xml)


class TestReadSenderReceiverCompositeElementToSignalMapping:
    def test_read_full(self):
        xml = (
            """
        <SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING xmlns="%s">
            <DATA-ELEMENT-IREF>
                <CONTEXT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/Root</CONTEXT-COMPOSITION-REF>
                <CONTEXT-PORT-REF DEST="R-PORT-PROTOTYPE">/Root/SwcA/DataPort</CONTEXT-PORT-REF>
                <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Root/SwcA/DataPort/Elem</TARGET-DATA-PROTOTYPE-REF>
            </DATA-ELEMENT-IREF>
            <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/System/Signal</SYSTEM-SIGNAL-REF>
            <TYPE-MAPPING>
                <SENDER-REC-RECORD-TYPE-MAPPING/>
            </TYPE-MAPPING>
        </SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = SenderReceiverCompositeElementToSignalMapping()
        ARXMLParser().readSenderReceiverCompositeElementToSignalMapping(element, mapping)

        iref = mapping.getDataElementIRef()
        assert iref is not None
        assert iref.getContextCompositionRef().getValue() == "/Root"
        assert iref.getContextPortRef().getValue() == "/Root/SwcA/DataPort"
        assert iref.getTargetDataPrototypeRef().getValue() == "/Root/SwcA/DataPort/Elem"
        assert mapping.getSystemSignalRef().getValue() == "/System/Signal"
        assert mapping.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"
        assert isinstance(mapping.getTypeMapping(), SenderRecRecordTypeMapping)

    def test_read_with_array_type_mapping(self):
        xml = (
            """
        <SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING xmlns="%s">
            <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/System/Signal</SYSTEM-SIGNAL-REF>
            <TYPE-MAPPING>
                <SENDER-REC-ARRAY-TYPE-MAPPING/>
            </TYPE-MAPPING>
        </SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = SenderReceiverCompositeElementToSignalMapping()
        ARXMLParser().readSenderReceiverCompositeElementToSignalMapping(element, mapping)

        assert isinstance(mapping.getTypeMapping(), SenderRecArrayTypeMapping)
        assert mapping.getDataElementIRef() is None

    def test_read_empty(self):
        xml = '<SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING xmlns="%s"/>' % NS
        element = _parse(xml)
        mapping = SenderReceiverCompositeElementToSignalMapping()
        ARXMLParser().readSenderReceiverCompositeElementToSignalMapping(element, mapping)

        assert mapping.getDataElementIRef() is None
        assert mapping.getSystemSignalRef() is None
        assert mapping.getTypeMapping() is None

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <DATA-MAPPINGS>
                <SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/System/Signal</SYSTEM-SIGNAL-REF>
                </SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING>
            </DATA-MAPPINGS>
        </PARENT>
        """
            % NS
        )
        element = _parse(xml)
        system = System(parent=None, short_name="sys")
        mapping = system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingDataMappings(element, mapping)

        data_mappings = mapping.getDataMappings()
        assert len(data_mappings) == 1
        assert isinstance(data_mappings[0], SenderReceiverCompositeElementToSignalMapping)
        assert data_mappings[0].getSystemSignalRef().getValue() == "/System/Signal"
