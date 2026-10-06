"""Reader tests for SeparateSignalPath (Table 5.42, p.257).

XML group SEPARATE-SIGNAL-PATH (AUTOSAR_00052.xsd l.104922):
OPERATIONS wrapper (SWC-TO-SWC-OPERATION-ARGUMENTS items) and SIGNALS wrapper
(SWC-TO-SWC-SIGNAL items), after the inherited SIGNAL-PATH-CONSTRAINT group.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SeparateSignalPath
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


class TestReadSeparateSignalPath:
    def test_read_full(self):
        xml = (
            """
        <SEPARATE-SIGNAL-PATH xmlns="%s">
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
        </SEPARATE-SIGNAL-PATH>
        """
            % NS
        )
        element = _parse(xml)
        path = SeparateSignalPath()
        ARXMLParser().readSeparateSignalPath(element, path)

        operations = path.getOperations()
        assert len(operations) == 1
        assert operations[0].getDirection().getValue() == "IN"
        signals = path.getSignals()
        assert len(signals) == 1
        assert signals[0].getDataElementIRefs()[0].getTargetDataPrototypeRef().getValue() == "/Root/SwcA/Vdp1"

    def test_read_empty(self):
        xml = '<SEPARATE-SIGNAL-PATH xmlns="%s"/>' % NS
        element = _parse(xml)
        path = SeparateSignalPath()
        ARXMLParser().readSeparateSignalPath(element, path)

        assert path.getOperations() == []
        assert path.getSignals() == []

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <SIGNAL-PATH-CONSTRAINTS>
                <SEPARATE-SIGNAL-PATH>
                    <SIGNALS>
                        <SWC-TO-SWC-SIGNAL/>
                    </SIGNALS>
                </SEPARATE-SIGNAL-PATH>
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
        assert isinstance(constraints[0], SeparateSignalPath)
        assert len(constraints[0].getSignals()) == 1
