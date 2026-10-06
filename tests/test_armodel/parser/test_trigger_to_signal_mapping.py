"""Reader tests for TriggerToSignalMapping (Table 5.35, p.250) and its
TriggerInSystemInstanceRef member type (Table B.4, p.1005).

XML group TRIGGER-TO-SIGNAL-MAPPING (AUTOSAR_00052.xsd l.126726):
TRIGGER-IREF (TRIGGER-IN-SYSTEM-INSTANCE-REF) + SYSTEM-SIGNAL-REF, after the
inherited DATA-MAPPING group. Dispatched from SystemMapping DATA-MAPPINGS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import TriggerToSignalMapping
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


class TestReadTriggerToSignalMapping:
    def test_read_full(self):
        xml = (
            """
        <TRIGGER-TO-SIGNAL-MAPPING xmlns="%s">
            <TRIGGER-IREF>
                <CONTEXT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/Root</CONTEXT-COMPOSITION-REF>
                <CONTEXT-PORT-REF DEST="PORT-PROTOTYPE">/Root/SwcA/TriggerPort</CONTEXT-PORT-REF>
                <TARGET-TRIGGER-REF DEST="TRIGGER">/Root/SwcA/T1</TARGET-TRIGGER-REF>
            </TRIGGER-IREF>
            <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/System/TrigSignal</SYSTEM-SIGNAL-REF>
        </TRIGGER-TO-SIGNAL-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = TriggerToSignalMapping()
        ARXMLParser().readTriggerToSignalMapping(element, mapping)

        iref = mapping.getTriggerIRef()
        assert iref is not None
        assert iref.getContextCompositionRef().getValue() == "/Root"
        assert iref.getContextPortRef().getValue() == "/Root/SwcA/TriggerPort"
        assert iref.getTargetTriggerRef().getValue() == "/Root/SwcA/T1"
        assert mapping.getSystemSignalRef().getValue() == "/System/TrigSignal"
        assert mapping.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"

    def test_read_empty(self):
        xml = '<TRIGGER-TO-SIGNAL-MAPPING xmlns="%s"/>' % NS
        element = _parse(xml)
        mapping = TriggerToSignalMapping()
        ARXMLParser().readTriggerToSignalMapping(element, mapping)

        assert mapping.getTriggerIRef() is None
        assert mapping.getSystemSignalRef() is None

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <DATA-MAPPINGS>
                <TRIGGER-TO-SIGNAL-MAPPING>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/System/TrigSignal</SYSTEM-SIGNAL-REF>
                </TRIGGER-TO-SIGNAL-MAPPING>
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
        assert isinstance(data_mappings[0], TriggerToSignalMapping)
        assert data_mappings[0].getSystemSignalRef().getValue() == "/System/TrigSignal"
