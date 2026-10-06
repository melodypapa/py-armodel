"""Reader tests for ForbiddenSignalPath (Table 5.40, p.255).

XML group FORBIDDEN-SIGNAL-PATH (AUTOSAR_00052.xsd l.62809):
OPERATIONS wrapper (SWC-TO-SWC-OPERATION-ARGUMENTS items), PHYSICAL-CHANNEL-REFS
wrapper (PHYSICAL-CHANNEL-REF items) and SIGNALS wrapper (SWC-TO-SWC-SIGNAL items),
after the inherited SIGNAL-PATH-CONSTRAINT group.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import ForbiddenSignalPath
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


class TestReadForbiddenSignalPath:
    def test_read_full(self):
        xml = (
            """
        <FORBIDDEN-SIGNAL-PATH xmlns="%s">
            <OPERATIONS>
                <SWC-TO-SWC-OPERATION-ARGUMENTS>
                    <DIRECTION>OUT</DIRECTION>
                </SWC-TO-SWC-OPERATION-ARGUMENTS>
            </OPERATIONS>
            <PHYSICAL-CHANNEL-REFS>
                <PHYSICAL-CHANNEL-REF DEST="CAN-PHYSICAL-CHANNEL">/Topology/Cluster/Can1</PHYSICAL-CHANNEL-REF>
            </PHYSICAL-CHANNEL-REFS>
            <SIGNALS>
                <SWC-TO-SWC-SIGNAL>
                    <DATA-ELEMENT-IREFS>
                        <DATA-ELEMENT-IREF>
                            <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Root/SwcA/Vdp1</TARGET-DATA-PROTOTYPE-REF>
                        </DATA-ELEMENT-IREF>
                    </DATA-ELEMENT-IREFS>
                </SWC-TO-SWC-SIGNAL>
            </SIGNALS>
        </FORBIDDEN-SIGNAL-PATH>
        """
            % NS
        )
        element = _parse(xml)
        path = ForbiddenSignalPath()
        ARXMLParser().readForbiddenSignalPath(element, path)

        operations = path.getOperations()
        assert len(operations) == 1
        assert operations[0].getDirection().getValue() == "OUT"
        refs = path.getPhysicalChannelRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/Topology/Cluster/Can1"
        assert refs[0].getDest() == "CAN-PHYSICAL-CHANNEL"
        signals = path.getSignals()
        assert len(signals) == 1
        assert signals[0].getDataElementIRefs()[0].getTargetDataPrototypeRef().getValue() == "/Root/SwcA/Vdp1"

    def test_read_empty(self):
        xml = '<FORBIDDEN-SIGNAL-PATH xmlns="%s"/>' % NS
        element = _parse(xml)
        path = ForbiddenSignalPath()
        ARXMLParser().readForbiddenSignalPath(element, path)

        assert path.getOperations() == []
        assert path.getPhysicalChannelRefs() == []
        assert path.getSignals() == []

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <SIGNAL-PATH-CONSTRAINTS>
                <FORBIDDEN-SIGNAL-PATH>
                    <PHYSICAL-CHANNEL-REFS>
                        <PHYSICAL-CHANNEL-REF DEST="CAN-PHYSICAL-CHANNEL">/Topology/Cluster/Can1</PHYSICAL-CHANNEL-REF>
                    </PHYSICAL-CHANNEL-REFS>
                </FORBIDDEN-SIGNAL-PATH>
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
        assert isinstance(constraints[0], ForbiddenSignalPath)
        assert constraints[0].getPhysicalChannelRefs()[0].getValue() == "/Topology/Cluster/Can1"
