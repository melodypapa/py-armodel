"""Reader tests for ClientServerToSignalMapping (Table 5.33, p.242).

XML group CLIENT-SERVER-TO-SIGNAL-MAPPING (AUTOSAR_00052.xsd l.17964):
CALL-SIGNAL-REF + CLIENT-SERVER-OPERATION-IREF (OPERATION-IN-SYSTEM-INSTANCE-REF)
+ RETURN-SIGNAL-REF, after the inherited DATA-MAPPING group. Dispatched from
SystemMapping DATA-MAPPINGS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import ClientServerToSignalMapping
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


class TestReadClientServerToSignalMapping:
    def test_read_full(self):
        xml = (
            """
        <CLIENT-SERVER-TO-SIGNAL-MAPPING xmlns="%s">
            <CALL-SIGNAL-REF DEST="SYSTEM-SIGNAL">/System/CallSignal</CALL-SIGNAL-REF>
            <CLIENT-SERVER-OPERATION-IREF>
                <CONTEXT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/Root</CONTEXT-COMPOSITION-REF>
                <CONTEXT-COMPONENT-REF DEST="SW-COMPOSITION-PROTOTYPE">/Root/SwcA</CONTEXT-COMPONENT-REF>
                <CONTEXT-PORT-REF DEST="P-PORT-PROTOTYPE">/Root/SwcA/CSPort</CONTEXT-PORT-REF>
                <TARGET-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/Root/SwcA/CSPort/Op</TARGET-OPERATION-REF>
            </CLIENT-SERVER-OPERATION-IREF>
            <RETURN-SIGNAL-REF DEST="SYSTEM-SIGNAL">/System/ReturnSignal</RETURN-SIGNAL-REF>
        </CLIENT-SERVER-TO-SIGNAL-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = ClientServerToSignalMapping()
        ARXMLParser().readClientServerToSignalMapping(element, mapping)

        assert mapping.getCallSignalRef().getValue() == "/System/CallSignal"
        assert mapping.getCallSignalRef().getDest() == "SYSTEM-SIGNAL"
        iref = mapping.getClientServerOperationIRef()
        assert iref is not None
        assert iref.getContextCompositionRef().getValue() == "/Root"
        assert iref.getContextComponentRefs()[0].getValue() == "/Root/SwcA"
        assert iref.getContextPortRef().getValue() == "/Root/SwcA/CSPort"
        assert iref.getTargetOperationRef().getValue() == "/Root/SwcA/CSPort/Op"
        assert mapping.getReturnSignalRef().getValue() == "/System/ReturnSignal"
        assert mapping.getReturnSignalRef().getDest() == "SYSTEM-SIGNAL"

    def test_read_empty(self):
        xml = '<CLIENT-SERVER-TO-SIGNAL-MAPPING xmlns="%s"/>' % NS
        element = _parse(xml)
        mapping = ClientServerToSignalMapping()
        ARXMLParser().readClientServerToSignalMapping(element, mapping)

        assert mapping.getCallSignalRef() is None
        assert mapping.getClientServerOperationIRef() is None
        assert mapping.getReturnSignalRef() is None

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <DATA-MAPPINGS>
                <CLIENT-SERVER-TO-SIGNAL-MAPPING>
                    <CALL-SIGNAL-REF DEST="SYSTEM-SIGNAL">/System/CallSignal</CALL-SIGNAL-REF>
                    <RETURN-SIGNAL-REF DEST="SYSTEM-SIGNAL">/System/ReturnSignal</RETURN-SIGNAL-REF>
                </CLIENT-SERVER-TO-SIGNAL-MAPPING>
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
        assert isinstance(data_mappings[0], ClientServerToSignalMapping)
        assert data_mappings[0].getCallSignalRef().getValue() == "/System/CallSignal"
        assert data_mappings[0].getReturnSignalRef().getValue() == "/System/ReturnSignal"
