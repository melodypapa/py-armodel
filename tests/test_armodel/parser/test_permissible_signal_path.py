"""Reader tests for PermissibleSignalPath (Table 5.41, p.256).

XML group PERMISSIBLE-SIGNAL-PATH (AUTOSAR_00052.xsd l.89163):
OPERATIONS wrapper (SWC-TO-SWC-OPERATION-ARGUMENTS items), PHYSICAL-CHANNEL-REFS
wrapper (PHYSICAL-CHANNEL-REF items) and SIGNALS wrapper (SWC-TO-SWC-SIGNAL items),
after the inherited SIGNAL-PATH-CONSTRAINT group.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import PermissibleSignalPath
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


class TestReadPermissibleSignalPath:
    def test_read_full(self):
        xml = (
            """
        <PERMISSIBLE-SIGNAL-PATH xmlns="%s">
            <OPERATIONS>
                <SWC-TO-SWC-OPERATION-ARGUMENTS>
                    <DIRECTION>IN</DIRECTION>
                </SWC-TO-SWC-OPERATION-ARGUMENTS>
            </OPERATIONS>
            <PHYSICAL-CHANNEL-REFS>
                <PHYSICAL-CHANNEL-REF DEST="CAN-PHYSICAL-CHANNEL">/Topology/Cluster/Can1</PHYSICAL-CHANNEL-REF>
                <PHYSICAL-CHANNEL-REF DEST="LIN-PHYSICAL-CHANNEL">/Topology/Cluster/Lin1</PHYSICAL-CHANNEL-REF>
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
        </PERMISSIBLE-SIGNAL-PATH>
        """
            % NS
        )
        element = _parse(xml)
        path = PermissibleSignalPath()
        ARXMLParser().readPermissibleSignalPath(element, path)

        operations = path.getOperations()
        assert len(operations) == 1
        assert operations[0].getDirection().getValue() == "IN"
        refs = path.getPhysicalChannelRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Topology/Cluster/Can1"
        assert refs[1].getDest() == "LIN-PHYSICAL-CHANNEL"
        signals = path.getSignals()
        assert len(signals) == 1
        assert signals[0].getDataElementIRefs()[0].getTargetDataPrototypeRef().getValue() == "/Root/SwcA/Vdp1"

    def test_read_empty(self):
        xml = '<PERMISSIBLE-SIGNAL-PATH xmlns="%s"/>' % NS
        element = _parse(xml)
        path = PermissibleSignalPath()
        ARXMLParser().readPermissibleSignalPath(element, path)

        assert path.getOperations() == []
        assert path.getPhysicalChannelRefs() == []
        assert path.getSignals() == []

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <SIGNAL-PATH-CONSTRAINTS>
                <PERMISSIBLE-SIGNAL-PATH>
                    <PHYSICAL-CHANNEL-REFS>
                        <PHYSICAL-CHANNEL-REF DEST="CAN-PHYSICAL-CHANNEL">/Topology/Cluster/Can1</PHYSICAL-CHANNEL-REF>
                    </PHYSICAL-CHANNEL-REFS>
                </PERMISSIBLE-SIGNAL-PATH>
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
        assert isinstance(constraints[0], PermissibleSignalPath)
        assert constraints[0].getPhysicalChannelRefs()[0].getValue() == "/Topology/Cluster/Can1"
