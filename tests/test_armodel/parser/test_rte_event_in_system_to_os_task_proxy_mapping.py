"""Reader tests for RteEventInSystemToOsTaskProxyMapping (Table 5.20, p.214).

XML group RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING (AUTOSAR_00052.xsd l.100713):
OFFSET, OS-TASK-PROXY-REF, RTE-EVENT-IREF (type RTE-EVENT-IN-SYSTEM-INSTANCE-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInSystemToOsTaskProxyMapping
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


class TestReadRteEventInSystemToOsTaskProxyMapping:
    def test_read_full(self):
        xml = (
            """
        <RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING xmlns="%s">
            <SHORT-NAME>Map1</SHORT-NAME>
            <OFFSET>2</OFFSET>
            <OS-TASK-PROXY-REF DEST="OS-TASK-PROXY">/OsTaskProxies/TaskProxy2</OS-TASK-PROXY-REF>
            <RTE-EVENT-IREF>
                <CONTEXT-ROOT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/Root</CONTEXT-ROOT-COMPOSITION-REF>
                <CONTEXT-SW-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/Root/SwcA</CONTEXT-SW-COMPONENT-REF>
                <TARGET-RTE-EVENT-REF DEST="RTE-EVENT">/Root/SwcA/Ev1</TARGET-RTE-EVENT-REF>
            </RTE-EVENT-IREF>
        </RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = RteEventInSystemToOsTaskProxyMapping(None, "Map1")
        ARXMLParser().readRteEventInSystemToOsTaskProxyMapping(element, mapping)

        assert mapping.getShortName() == "Map1"
        assert mapping.getOffset().getValue() == 2
        assert mapping.getOsTaskProxyRef().getValue() == "/OsTaskProxies/TaskProxy2"
        assert mapping.getOsTaskProxyRef().getDest() == "OS-TASK-PROXY"
        iref = mapping.getRteEventIRef()
        assert iref is not None
        assert iref.getContextRootCompositionRef().getValue() == "/Root"
        assert iref.getContextSwComponentRefs()[0].getValue() == "/Root/SwcA"
        assert iref.getTargetRteEventRef().getValue() == "/Root/SwcA/Ev1"

    def test_read_empty(self):
        xml = (
            """
        <RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING xmlns="%s">
            <SHORT-NAME>Map1</SHORT-NAME>
        </RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = RteEventInSystemToOsTaskProxyMapping(None, "Map1")
        ARXMLParser().readRteEventInSystemToOsTaskProxyMapping(element, mapping)

        assert mapping.getOffset() is None
        assert mapping.getOsTaskProxyRef() is None
        assert mapping.getRteEventIRef() is None
