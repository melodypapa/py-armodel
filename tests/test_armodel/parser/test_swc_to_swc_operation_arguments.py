"""Reader tests for SwcToSwcOperationArguments (Table 5.38, p.254).

XML group SWC-TO-SWC-OPERATION-ARGUMENTS (AUTOSAR_00052.xsd l.118132):
DIRECTION literal + OPERATION-IREFS wrapper with a choice of OPERATION-IREF items
(type OPERATION-IN-SYSTEM-INSTANCE-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SwcToSwcOperationArguments, SwcToSwcOperationArgumentsDirectionEnum
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


class TestReadSwcToSwcOperationArguments:
    def test_read_full(self):
        xml = (
            """
        <SWC-TO-SWC-OPERATION-ARGUMENTS xmlns="%s">
            <DIRECTION>IN</DIRECTION>
            <OPERATION-IREFS>
                <OPERATION-IREF>
                    <CONTEXT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/Root</CONTEXT-COMPOSITION-REF>
                    <TARGET-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/Root/SwcA/Cso1</TARGET-OPERATION-REF>
                </OPERATION-IREF>
                <OPERATION-IREF>
                    <TARGET-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/Root/SwcB/Cso2</TARGET-OPERATION-REF>
                </OPERATION-IREF>
            </OPERATION-IREFS>
        </SWC-TO-SWC-OPERATION-ARGUMENTS>
        """
            % NS
        )
        element = _parse(xml)
        arguments = SwcToSwcOperationArguments()
        ARXMLParser().readSwcToSwcOperationArguments(element, arguments)

        assert arguments.getDirection().getValue() == SwcToSwcOperationArgumentsDirectionEnum.IN
        irefs = arguments.getOperationIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextCompositionRef().getValue() == "/Root"
        assert irefs[0].getTargetOperationRef().getValue() == "/Root/SwcA/Cso1"
        assert irefs[1].getTargetOperationRef().getValue() == "/Root/SwcB/Cso2"

    def test_read_empty(self):
        xml = '<SWC-TO-SWC-OPERATION-ARGUMENTS xmlns="%s"/>' % NS
        element = _parse(xml)
        arguments = SwcToSwcOperationArguments()
        ARXMLParser().readSwcToSwcOperationArguments(element, arguments)

        assert arguments.getDirection() is None
        assert arguments.getOperationIRefs() == []
