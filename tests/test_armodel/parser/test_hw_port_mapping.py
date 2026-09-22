"""Parser tests for HwPortMapping (Table 3.135, p.183).

XML element order per XSD group HW-PORT-MAPPING:
COMMUNICATION-CONNECTOR-REF, HW-COMMUNICATION-PORT-REF.
"""

import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import HwPortMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FRAGMENT = """
<HW-PORT-MAPPING>
    <COMMUNICATION-CONNECTOR-REF DEST="COMMUNICATION-CONNECTOR">/System/Connectors/Conn1</COMMUNICATION-CONNECTOR-REF>
    <HW-COMMUNICATION-PORT-REF DEST="HW-PIN-GROUP">/EcuResource/HwPinGroups/Port1</HW-COMMUNICATION-PORT-REF>
</HW-PORT-MAPPING>
"""


def test_read_hw_port_mapping():
    AUTOSAR.getInstance().new()
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, FRAGMENT))
    mapping = ARXMLParser().readHwPortMapping(root[0])
    assert isinstance(mapping, HwPortMapping)
    assert mapping.getCommunicationConnectorRef().getValue() == "/System/Connectors/Conn1"
    assert mapping.getCommunicationConnectorRef().getDest() == "COMMUNICATION-CONNECTOR"
    assert mapping.getHwCommunicationPortRef().getValue() == "/EcuResource/HwPinGroups/Port1"
    assert mapping.getHwCommunicationPortRef().getDest() == "HW-PIN-GROUP"


def test_read_empty_hw_port_mapping():
    AUTOSAR.getInstance().new()
    root = ET.fromstring("<ROOT xmlns='%s'><HW-PORT-MAPPING/></ROOT>" % NS)
    mapping = ARXMLParser().readHwPortMapping(root[0])
    assert mapping.getCommunicationConnectorRef() is None
    assert mapping.getHwCommunicationPortRef() is None
