"""Reader tests for SwcToSwcSignal (Table 5.37, p.253).

XML group SWC-TO-SWC-SIGNAL (AUTOSAR_00052.xsd l.118172):
DATA-ELEMENT-IREFS wrapper with a choice of DATA-ELEMENT-IREF items
(type VARIABLE-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SwcToSwcSignal
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


class TestReadSwcToSwcSignal:
    def test_read_full(self):
        xml = (
            """
        <SWC-TO-SWC-SIGNAL xmlns="%s">
            <DATA-ELEMENT-IREFS>
                <DATA-ELEMENT-IREF>
                    <CONTEXT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/Root</CONTEXT-COMPOSITION-REF>
                    <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Root/SwcA/Vdp1</TARGET-DATA-PROTOTYPE-REF>
                </DATA-ELEMENT-IREF>
                <DATA-ELEMENT-IREF>
                    <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Root/SwcB/Vdp2</TARGET-DATA-PROTOTYPE-REF>
                </DATA-ELEMENT-IREF>
            </DATA-ELEMENT-IREFS>
        </SWC-TO-SWC-SIGNAL>
        """
            % NS
        )
        element = _parse(xml)
        signal = SwcToSwcSignal()
        ARXMLParser().readSwcToSwcSignal(element, signal)

        irefs = signal.getDataElementIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextCompositionRef().getValue() == "/Root"
        assert irefs[0].getTargetDataPrototypeRef().getValue() == "/Root/SwcA/Vdp1"
        assert irefs[1].getTargetDataPrototypeRef().getValue() == "/Root/SwcB/Vdp2"

    def test_read_empty(self):
        xml = '<SWC-TO-SWC-SIGNAL xmlns="%s"/>' % NS
        element = _parse(xml)
        signal = SwcToSwcSignal()
        ARXMLParser().readSwcToSwcSignal(element, signal)

        assert signal.getDataElementIRefs() == []
