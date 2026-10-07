"""Reader tests for RteEventInCompositionSeparation (Table 5.19, p.212).

XML group RTE-EVENT-IN-COMPOSITION-SEPARATION (AUTOSAR_00052.xsd l.100465):
RTE-EVENT-IREFS wrapper with a choice of RTE-EVENT-IREF items
(type RTE-EVENT-IN-COMPOSITION-INSTANCE-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInCompositionSeparation
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


class TestReadRteEventInCompositionSeparation:
    def test_read_full(self):
        xml = (
            """
        <RTE-EVENT-IN-COMPOSITION-SEPARATION xmlns="%s">
            <SHORT-NAME>Sep1</SHORT-NAME>
            <RTE-EVENT-IREFS>
                <RTE-EVENT-IREF>
                    <CONTEXT-SW-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/Comps/SwcA</CONTEXT-SW-COMPONENT-REF>
                    <TARGET-RTE-EVENT-REF DEST="RTE-EVENT">/Comps/SwcA/Ev1</TARGET-RTE-EVENT-REF>
                </RTE-EVENT-IREF>
                <RTE-EVENT-IREF>
                    <TARGET-RTE-EVENT-REF DEST="RTE-EVENT">/Comps/SwcB/Ev2</TARGET-RTE-EVENT-REF>
                </RTE-EVENT-IREF>
            </RTE-EVENT-IREFS>
        </RTE-EVENT-IN-COMPOSITION-SEPARATION>
        """
            % NS
        )
        element = _parse(xml)
        separation = RteEventInCompositionSeparation(None, "Sep1")
        ARXMLParser().readRteEventInCompositionSeparation(element, separation)

        assert separation.getShortName() == "Sep1"
        irefs = separation.getRteEventIRefs()
        assert len(irefs) == 2
        assert irefs[0].getTargetRteEventRef().getValue() == "/Comps/SwcA/Ev1"
        assert irefs[0].getContextSwComponentRefs()[0].getValue() == "/Comps/SwcA"
        assert irefs[1].getTargetRteEventRef().getValue() == "/Comps/SwcB/Ev2"

    def test_read_empty(self):
        xml = (
            """
        <RTE-EVENT-IN-COMPOSITION-SEPARATION xmlns="%s">
            <SHORT-NAME>Sep1</SHORT-NAME>
        </RTE-EVENT-IN-COMPOSITION-SEPARATION>
        """
            % NS
        )
        element = _parse(xml)
        separation = RteEventInCompositionSeparation(None, "Sep1")
        ARXMLParser().readRteEventInCompositionSeparation(element, separation)

        assert separation.getRteEventIRefs() == []
