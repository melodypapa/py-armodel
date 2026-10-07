"""Reader tests for CommonSignalPath (Table 5.36, p.253).

XML group COMMON-SIGNAL-PATH (AUTOSAR_00052.xsd l.20093):
OPERATIONS wrapper (SWC-TO-SWC-OPERATION-ARGUMENTS items) + SIGNALS wrapper
(SWC-TO-SWC-SIGNAL items), after the inherited SIGNAL-PATH-CONSTRAINT group.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import CommonSignalPath
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


class TestReadCommonSignalPath:
    def test_read_full(self):
        xml = (
            """
        <COMMON-SIGNAL-PATH xmlns="%s">
            <OPERATIONS>
                <SWC-TO-SWC-OPERATION-ARGUMENTS>
                    <DIRECTION>IN</DIRECTION>
                </SWC-TO-SWC-OPERATION-ARGUMENTS>
            </OPERATIONS>
            <SIGNALS>
                <SWC-TO-SWC-SIGNAL>
                    <DATA-ELEMENT-IREFS>
                        <DATA-ELEMENT-IREF>
                            <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Root/SwcA/Vdp1</TARGET-DATA-PROTOTYPE-REF>
                        </DATA-ELEMENT-IREF>
                    </DATA-ELEMENT-IREFS>
                </SWC-TO-SWC-SIGNAL>
            </SIGNALS>
        </COMMON-SIGNAL-PATH>
        """
            % NS
        )
        element = _parse(xml)
        path = CommonSignalPath()
        ARXMLParser().readCommonSignalPath(element, path)

        assert path.getIntroduction() is None
        operations = path.getOperations()
        assert len(operations) == 1
        assert operations[0].getDirection().getValue() == "IN"
        signals = path.getSignals()
        assert len(signals) == 1
        assert signals[0].getDataElementIRefs()[0].getTargetDataPrototypeRef().getValue() == "/Root/SwcA/Vdp1"

    def test_read_empty(self):
        xml = '<COMMON-SIGNAL-PATH xmlns="%s"/>' % NS
        element = _parse(xml)
        path = CommonSignalPath()
        ARXMLParser().readCommonSignalPath(element, path)

        assert path.getOperations() == []
        assert path.getSignals() == []

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <SIGNAL-PATH-CONSTRAINTS>
                <COMMON-SIGNAL-PATH>
                    <SIGNALS>
                        <SWC-TO-SWC-SIGNAL/>
                    </SIGNALS>
                </COMMON-SIGNAL-PATH>
            </SIGNAL-PATH-CONSTRAINTS>
        </PARENT>
        """
            % NS
        )
        element = _parse(xml)
        system = System(parent=None, short_name="sys")
        mapping = system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSignalPathConstraints(element, mapping)

        constraints = mapping.getSignalPathConstraints()
        assert len(constraints) == 1
        assert isinstance(constraints[0], CommonSignalPath)
        assert len(constraints[0].getSignals()) == 1
