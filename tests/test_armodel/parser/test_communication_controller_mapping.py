"""Parser tests for CommunicationControllerMapping (Table 3.134, p.183).

XML element order per XSD group COMMUNICATION-CONTROLLER-MAPPING:
COMMUNICATION-CONTROLLER-REF, HW-COMMUNICATION-CONTROLLER-REF.
"""

import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import CommunicationControllerMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FRAGMENT = """
<COMMUNICATION-CONTROLLER-MAPPING>
    <COMMUNICATION-CONTROLLER-REF DEST="COMMUNICATION-CONTROLLER">/System/Controllers/Ctrl1</COMMUNICATION-CONTROLLER-REF>
    <HW-COMMUNICATION-CONTROLLER-REF DEST="HW-ELEMENT">/EcuResource/HwElements/Mcu</HW-COMMUNICATION-CONTROLLER-REF>
</COMMUNICATION-CONTROLLER-MAPPING>
"""


def _parse_fragment():
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, FRAGMENT))
    return ARXMLParser().readCommunicationControllerMapping(root[0])


def test_read_communication_controller_mapping():
    AUTOSAR.getInstance().new()
    mapping = _parse_fragment()
    assert isinstance(mapping, CommunicationControllerMapping)
    assert mapping.getCommunicationControllerRef().getValue() == "/System/Controllers/Ctrl1"
    assert mapping.getCommunicationControllerRef().getDest() == "COMMUNICATION-CONTROLLER"
    assert mapping.getHwCommunicationControllerRef().getValue() == "/EcuResource/HwElements/Mcu"
    assert mapping.getHwCommunicationControllerRef().getDest() == "HW-ELEMENT"


def test_read_empty_communication_controller_mapping():
    AUTOSAR.getInstance().new()
    root = ET.fromstring("<ROOT xmlns='%s'><COMMUNICATION-CONTROLLER-MAPPING/></ROOT>" % NS)
    mapping = ARXMLParser().readCommunicationControllerMapping(root[0])
    assert mapping.getCommunicationControllerRef() is None
    assert mapping.getHwCommunicationControllerRef() is None
