"""Parser tests for ECUMapping (Table 3.133, p.182).

XML element order per XSD group ECU-MAPPING (AUTOSAR_00052.xsd l.50699):
COMM-CONTROLLER-MAPPINGS, ECU-INSTANCE-REF, ECU-REF, HW-PORT-MAPPINGS,
VARIATION-POINT (atpIdentityContributor, sequenceOffset=10000).
"""

import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import ECUMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


FRAGMENT = """
<ECU-MAPPING>
    <SHORT-NAME>EcuMap1</SHORT-NAME>
    <COMM-CONTROLLER-MAPPINGS>
        <COMMUNICATION-CONTROLLER-MAPPING>
            <COMMUNICATION-CONTROLLER-REF DEST="COMMUNICATION-CONTROLLER">/System/Controllers/Ctrl1</COMMUNICATION-CONTROLLER-REF>
            <HW-COMMUNICATION-CONTROLLER-REF DEST="HW-ELEMENT">/EcuResource/HwElements/Mcu</HW-COMMUNICATION-CONTROLLER-REF>
        </COMMUNICATION-CONTROLLER-MAPPING>
        <COMMUNICATION-CONTROLLER-MAPPING>
            <COMMUNICATION-CONTROLLER-REF DEST="COMMUNICATION-CONTROLLER">/System/Controllers/Ctrl2</COMMUNICATION-CONTROLLER-REF>
        </COMMUNICATION-CONTROLLER-MAPPING>
    </COMM-CONTROLLER-MAPPINGS>
    <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/System/EcuInstances/EcuInst1</ECU-INSTANCE-REF>
    <ECU-REF DEST="HW-ELEMENT">/EcuResource/HwElements/Ecu1</ECU-REF>
    <HW-PORT-MAPPINGS>
        <HW-PORT-MAPPING>
            <COMMUNICATION-CONNECTOR-REF DEST="COMMUNICATION-CONNECTOR">/System/Connectors/Conn1</COMMUNICATION-CONNECTOR-REF>
            <HW-COMMUNICATION-PORT-REF DEST="HW-PIN-GROUP">/EcuResource/HwPinGroups/Port1</HW-COMMUNICATION-PORT-REF>
        </HW-PORT-MAPPING>
    </HW-PORT-MAPPINGS>
</ECU-MAPPING>
"""


def test_read_ecu_mapping_full():
    AUTOSAR.getInstance().new()
    mapping = ECUMapping(MockParent(), "EcuMap1")
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, FRAGMENT))
    ARXMLParser().readEcuMapping(root[0], mapping)

    assert mapping.getShortName() == "EcuMap1"
    assert len(mapping.getCommControllerMappings()) == 2
    ccm1 = mapping.getCommControllerMappings()[0]
    assert ccm1.getCommunicationControllerRef().getValue() == "/System/Controllers/Ctrl1"
    assert ccm1.getCommunicationControllerRef().getDest() == "COMMUNICATION-CONTROLLER"
    assert ccm1.getHwCommunicationControllerRef().getValue() == "/EcuResource/HwElements/Mcu"
    ccm2 = mapping.getCommControllerMappings()[1]
    assert ccm2.getCommunicationControllerRef().getValue() == "/System/Controllers/Ctrl2"
    assert ccm2.getHwCommunicationControllerRef() is None
    assert mapping.getEcuInstanceRef().getValue() == "/System/EcuInstances/EcuInst1"
    assert mapping.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
    assert mapping.getEcuRef().getValue() == "/EcuResource/HwElements/Ecu1"
    assert mapping.getEcuRef().getDest() == "HW-ELEMENT"
    assert len(mapping.getHwPortMappings()) == 1
    hpm1 = mapping.getHwPortMappings()[0]
    assert hpm1.getCommunicationConnectorRef().getValue() == "/System/Connectors/Conn1"
    assert hpm1.getHwCommunicationPortRef().getValue() == "/EcuResource/HwPinGroups/Port1"


def test_read_ecu_mapping_empty():
    AUTOSAR.getInstance().new()
    mapping = ECUMapping(MockParent(), "EcuMap1")
    root = ET.fromstring("<ROOT xmlns='%s'><ECU-MAPPING><SHORT-NAME>EcuMap1</SHORT-NAME></ECU-MAPPING></ROOT>" % NS)
    ARXMLParser().readEcuMapping(root[0], mapping)

    assert mapping.getCommControllerMappings() == []
    assert mapping.getEcuRef() is None
    assert mapping.getEcuInstanceRef() is None
    assert mapping.getHwPortMappings() == []


def test_read_system_mapping_ecu_resource_mappings_dispatch():
    AUTOSAR.getInstance().new()
    system_mapping = SystemMapping(MockParent(), "SysMapping")
    root = ET.fromstring("<ROOT xmlns='%s'><ECU-RESOURCE-MAPPINGS>%s</ECU-RESOURCE-MAPPINGS></ROOT>" % (NS, FRAGMENT))
    ARXMLParser().readSystemMappingEcuResourceMappings(root, system_mapping)

    ecu_mappings = system_mapping.getEcuResourceMappings()
    assert len(ecu_mappings) == 1
    assert isinstance(ecu_mappings[0], ECUMapping)
    assert ecu_mappings[0].getShortName() == "EcuMap1"
    assert len(ecu_mappings[0].getCommControllerMappings()) == 2
    assert len(ecu_mappings[0].getHwPortMappings()) == 1
