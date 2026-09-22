"""Writer round-trip tests for ECUMapping (Table 3.133, p.182).

Child order per XSD group ECU-MAPPING (AUTOSAR_00052.xsd l.50699):
COMM-CONTROLLER-MAPPINGS, ECU-INSTANCE-REF, ECU-REF, HW-PORT-MAPPINGS,
VARIATION-POINT (atpIdentityContributor, sequenceOffset=10000).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import CommunicationControllerMapping, ECUMapping, HwPortMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _new_mapping():
    mapping = ECUMapping(MockParent(), "EcuMap1")

    ccm1 = CommunicationControllerMapping()
    ccm1.setCommunicationControllerRef(_ref("COMMUNICATION-CONTROLLER", "/System/Controllers/Ctrl1"))
    ccm1.setHwCommunicationControllerRef(_ref("HW-ELEMENT", "/EcuResource/HwElements/Mcu"))
    ccm2 = CommunicationControllerMapping()
    ccm2.setCommunicationControllerRef(_ref("COMMUNICATION-CONTROLLER", "/System/Controllers/Ctrl2"))
    mapping.addCommControllerMapping(ccm1)
    mapping.addCommControllerMapping(ccm2)

    mapping.setEcuInstanceRef(_ref("ECU-INSTANCE", "/System/EcuInstances/EcuInst1"))
    mapping.setEcuRef(_ref("HW-ELEMENT", "/EcuResource/HwElements/Ecu1"))

    hpm1 = HwPortMapping()
    hpm1.setCommunicationConnectorRef(_ref("COMMUNICATION-CONNECTOR", "/System/Connectors/Conn1"))
    hpm1.setHwCommunicationPortRef(_ref("HW-PIN-GROUP", "/EcuResource/HwPinGroups/Port1"))
    mapping.addHwPortMapping(hpm1)
    return mapping


class TestWriteEcuMapping:
    def test_write_all_fields(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcuMapping(parent, _new_mapping())
        node = parent.find("ECU-MAPPING")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["SHORT-NAME", "COMM-CONTROLLER-MAPPINGS", "ECU-INSTANCE-REF", "ECU-REF", "HW-PORT-MAPPINGS"]
        assert node.find("SHORT-NAME").text == "EcuMap1"

        ccms = node.find("COMM-CONTROLLER-MAPPINGS")
        assert [child.tag for child in ccms] == ["COMMUNICATION-CONTROLLER-MAPPING", "COMMUNICATION-CONTROLLER-MAPPING"]
        ccm_refs = ccms.findall("COMMUNICATION-CONTROLLER-MAPPING/COMMUNICATION-CONTROLLER-REF")
        assert [ref.text for ref in ccm_refs] == ["/System/Controllers/Ctrl1", "/System/Controllers/Ctrl2"]
        assert ccm_refs[0].attrib["DEST"] == "COMMUNICATION-CONTROLLER"
        hw_cc_ref = ccms.find("COMMUNICATION-CONTROLLER-MAPPING/HW-COMMUNICATION-CONTROLLER-REF")
        assert hw_cc_ref.text == "/EcuResource/HwElements/Mcu"
        assert hw_cc_ref.attrib["DEST"] == "HW-ELEMENT"

        ecu_instance_ref = node.find("ECU-INSTANCE-REF")
        assert ecu_instance_ref.text == "/System/EcuInstances/EcuInst1"
        assert ecu_instance_ref.attrib["DEST"] == "ECU-INSTANCE"
        ecu_ref = node.find("ECU-REF")
        assert ecu_ref.text == "/EcuResource/HwElements/Ecu1"
        assert ecu_ref.attrib["DEST"] == "HW-ELEMENT"

        hpms = node.find("HW-PORT-MAPPINGS")
        assert [child.tag for child in hpms] == ["HW-PORT-MAPPING"]
        connector_ref = hpms.find("HW-PORT-MAPPING/COMMUNICATION-CONNECTOR-REF")
        assert connector_ref.text == "/System/Connectors/Conn1"
        assert connector_ref.attrib["DEST"] == "COMMUNICATION-CONNECTOR"
        port_ref = hpms.find("HW-PORT-MAPPING/HW-COMMUNICATION-PORT-REF")
        assert port_ref.text == "/EcuResource/HwPinGroups/Port1"
        assert port_ref.attrib["DEST"] == "HW-PIN-GROUP"

    def test_write_empty_fields_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcuMapping(parent, ECUMapping(MockParent(), "EcuMap1"))
        node = parent.find("ECU-MAPPING")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]

    def test_round_trip_preserves_all_values(self):
        mapping = _new_mapping()
        variation_point = VariationPoint()
        short_label = ARLiteral()
        short_label.setValue("vp1")
        variation_point.setShortLabel(short_label)
        mapping.setVariationPoint(variation_point)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcuMapping(parent, mapping)
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        node = root[0]
        assert [child.tag.split("}")[-1] for child in node] == [
            "SHORT-NAME",
            "COMM-CONTROLLER-MAPPINGS",
            "ECU-INSTANCE-REF",
            "ECU-REF",
            "HW-PORT-MAPPINGS",
            "VARIATION-POINT",
        ]

        parsed = ECUMapping(MockParent(), "EcuMap1")
        ARXMLParser().readEcuMapping(node, parsed)
        assert parsed.getCommControllerMappings()[0].getCommunicationControllerRef().getValue() == "/System/Controllers/Ctrl1"
        assert parsed.getCommControllerMappings()[0].getHwCommunicationControllerRef().getDest() == "HW-ELEMENT"
        assert parsed.getEcuInstanceRef().getValue() == "/System/EcuInstances/EcuInst1"
        assert parsed.getEcuRef().getValue() == "/EcuResource/HwElements/Ecu1"
        assert parsed.getHwPortMappings()[0].getCommunicationConnectorRef().getValue() == "/System/Connectors/Conn1"
        assert parsed.getHwPortMappings()[0].getHwCommunicationPortRef().getValue() == "/EcuResource/HwPinGroups/Port1"
        assert parsed.getVariationPoint().getShortLabel().getValue() == "vp1"
