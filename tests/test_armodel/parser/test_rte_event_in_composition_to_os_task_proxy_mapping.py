"""Reader tests for RteEventInCompositionToOsTaskProxyMapping (Table 5.18, p.212).

XML group RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING (AUTOSAR_00052.xsd l.100501):
OFFSET, OS-TASK-PROXY-REF, RTE-EVENT-IREF (type RTE-EVENT-IN-COMPOSITION-INSTANCE-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInCompositionToOsTaskProxyMapping
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


class TestReadRteEventInCompositionToOsTaskProxyMapping:
    def test_read_full(self):
        xml = (
            """
        <RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING xmlns="%s">
            <SHORT-NAME>Map1</SHORT-NAME>
            <OFFSET>4</OFFSET>
            <OS-TASK-PROXY-REF DEST="OS-TASK-PROXY">/OsTaskProxies/TaskProxy1</OS-TASK-PROXY-REF>
            <RTE-EVENT-IREF>
                <CONTEXT-SW-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/Comps/SwcA</CONTEXT-SW-COMPONENT-REF>
                <TARGET-RTE-EVENT-REF DEST="RTE-EVENT">/Comps/SwcA/Ev1</TARGET-RTE-EVENT-REF>
            </RTE-EVENT-IREF>
        </RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = RteEventInCompositionToOsTaskProxyMapping(None, "Map1")
        ARXMLParser().readRteEventInCompositionToOsTaskProxyMapping(element, mapping)

        assert mapping.getShortName() == "Map1"
        assert mapping.getOffset().getValue() == 4
        assert mapping.getOsTaskProxyRef().getValue() == "/OsTaskProxies/TaskProxy1"
        assert mapping.getOsTaskProxyRef().getDest() == "OS-TASK-PROXY"
        iref = mapping.getRteEventIRef()
        assert iref is not None
        assert len(iref.getContextSwComponentRefs()) == 1
        assert iref.getContextSwComponentRefs()[0].getValue() == "/Comps/SwcA"
        assert iref.getTargetRteEventRef().getValue() == "/Comps/SwcA/Ev1"
        assert iref.getTargetRteEventRef().getDest() == "RTE-EVENT"

    def test_read_empty(self):
        xml = (
            """
        <RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING xmlns="%s">
            <SHORT-NAME>Map1</SHORT-NAME>
        </RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = RteEventInCompositionToOsTaskProxyMapping(None, "Map1")
        ARXMLParser().readRteEventInCompositionToOsTaskProxyMapping(element, mapping)

        assert mapping.getOffset() is None
        assert mapping.getOsTaskProxyRef() is None
        assert mapping.getRteEventIRef() is None
