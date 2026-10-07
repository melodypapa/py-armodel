"""Reader tests for RteEventInSystemSeparation (Table 5.21, p.214).

XML group RTE-EVENT-IN-SYSTEM-SEPARATION (AUTOSAR_00052.xsd l.100676):
RTE-EVENT-IREFS wrapper with a choice of RTE-EVENT-IREF items
(type RTE-EVENT-IN-SYSTEM-INSTANCE-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInSystemSeparation
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


class TestReadRteEventInSystemSeparation:
    def test_read_full(self):
        xml = (
            """
        <RTE-EVENT-IN-SYSTEM-SEPARATION xmlns="%s">
            <SHORT-NAME>Sep1</SHORT-NAME>
            <RTE-EVENT-IREFS>
                <RTE-EVENT-IREF>
                    <CONTEXT-ROOT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/Root</CONTEXT-ROOT-COMPOSITION-REF>
                    <TARGET-RTE-EVENT-REF DEST="RTE-EVENT">/Root/SwcA/Ev1</TARGET-RTE-EVENT-REF>
                </RTE-EVENT-IREF>
                <RTE-EVENT-IREF>
                    <TARGET-RTE-EVENT-REF DEST="RTE-EVENT">/Root/SwcB/Ev2</TARGET-RTE-EVENT-REF>
                </RTE-EVENT-IREF>
            </RTE-EVENT-IREFS>
        </RTE-EVENT-IN-SYSTEM-SEPARATION>
        """
            % NS
        )
        element = _parse(xml)
        separation = RteEventInSystemSeparation(None, "Sep1")
        ARXMLParser().readRteEventInSystemSeparation(element, separation)

        assert separation.getShortName() == "Sep1"
        irefs = separation.getRteEventIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextRootCompositionRef().getValue() == "/Root"
        assert irefs[0].getTargetRteEventRef().getValue() == "/Root/SwcA/Ev1"
        assert irefs[1].getTargetRteEventRef().getValue() == "/Root/SwcB/Ev2"

    def test_read_empty(self):
        xml = (
            """
        <RTE-EVENT-IN-SYSTEM-SEPARATION xmlns="%s">
            <SHORT-NAME>Sep1</SHORT-NAME>
        </RTE-EVENT-IN-SYSTEM-SEPARATION>
        """
            % NS
        )
        element = _parse(xml)
        separation = RteEventInSystemSeparation(None, "Sep1")
        ARXMLParser().readRteEventInSystemSeparation(element, separation)

        assert separation.getRteEventIRefs() == []
