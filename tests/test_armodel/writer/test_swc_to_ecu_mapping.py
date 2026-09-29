"""Writer round-trip tests for SwcToEcuMapping (Table 5.2, p.197).

Serialized through the SW-MAPPINGS wrapper when aggregated by a SystemMapping
(XSD group SWC-TO-ECU-MAPPING, AUTOSAR_00052.xsd l.117895: COMPONENT-IREFS,
CONTROLLED-HW-ELEMENT-REF, ECU-INSTANCE-REF, [PARTITION-REF removed],
PROCESSING-UNIT-REF, VARIATION-POINT — emitted LAST, sequenceOffset=10000).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SwcToEcuMapping, System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _iref(target: str) -> ComponentInSystemInstanceRef:
    iref = ComponentInSystemInstanceRef()
    iref.setTargetComponentRef(_ref(target, "SW-COMPONENT-PROTOTYPE"))
    return iref


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteSwcToEcuMapping:
    def test_empty(self):
        mapping = SwcToEcuMapping(MockParent(), "Map")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToEcuMapping(parent, mapping)

        node = parent.find("SWC-TO-ECU-MAPPING")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Map"
        assert node.find("COMPONENT-IREFS") is None
        assert node.find("CONTROLLED-HW-ELEMENT-REF") is None
        assert node.find("ECU-INSTANCE-REF") is None
        assert node.find("PROCESSING-UNIT-REF") is None
        assert node.find("VARIATION-POINT") is None
        assert node.find("PARTITION-REF") is None

    def test_full_element_order(self):
        mapping = SwcToEcuMapping(MockParent(), "Map")
        mapping.addComponentIRef(_iref("/DemoApplication/SWC_ModifyEcho"))
        mapping.setControlledHwElementRef(_ref("/HwElements/SensorActuator", "HW-ELEMENT"))
        mapping.setEcuInstanceRef(_ref("/CanSystem/ECUINSTANCES/EcuTestNode", "ECU-INSTANCE"))
        mapping.setProcessingUnitRef(_ref("/HwElements/Core0", "HW-ELEMENT"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToEcuMapping(parent, mapping)

        node = parent.find("SWC-TO-ECU-MAPPING")
        tags = [child.tag for child in node]
        assert tags.index("COMPONENT-IREFS") < tags.index("CONTROLLED-HW-ELEMENT-REF")
        assert tags.index("CONTROLLED-HW-ELEMENT-REF") < tags.index("ECU-INSTANCE-REF")
        assert tags.index("ECU-INSTANCE-REF") < tags.index("PROCESSING-UNIT-REF")

        ecu_ref = node.find("ECU-INSTANCE-REF")
        assert ecu_ref.text == "/CanSystem/ECUINSTANCES/EcuTestNode"
        assert ecu_ref.attrib["DEST"] == "ECU-INSTANCE"
        controlled_ref = node.find("CONTROLLED-HW-ELEMENT-REF")
        assert controlled_ref.text == "/HwElements/SensorActuator"
        assert controlled_ref.attrib["DEST"] == "HW-ELEMENT"
        processing_ref = node.find("PROCESSING-UNIT-REF")
        assert processing_ref.text == "/HwElements/Core0"
        assert processing_ref.attrib["DEST"] == "HW-ELEMENT"

    def test_variation_point_written_last(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = system_mapping.createSwcToEcuMapping("Map")
        mapping.setEcuInstanceRef(_ref("/CanSystem/ECUINSTANCES/EcuTestNode", "ECU-INSTANCE"))

        root = _with_ns(
            _parse_to_parent(
                "<SWC-TO-ECU-MAPPING>"
                "<SHORT-NAME>Map</SHORT-NAME>"
                "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/CanSystem/ECUINSTANCES/EcuTestNode</ECU-INSTANCE-REF>"
                "<VARIATION-POINT><SHORT-LABEL>vp</SHORT-LABEL></VARIATION-POINT>"
                "</SWC-TO-ECU-MAPPING>"
            )
        )
        ARXMLParser().readSwcToEcuMapping(root[0], mapping)
        assert mapping.getVariationPoint() is not None

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToEcuMapping(parent, mapping)
        node = parent.find("SWC-TO-ECU-MAPPING")
        tags = [child.tag for child in node]
        assert "VARIATION-POINT" in tags
        assert tags.index("VARIATION-POINT") == len(tags) - 1
        assert tags.index("ECU-INSTANCE-REF") < tags.index("VARIATION-POINT")

    def test_round_trip_full(self):
        mapping = SwcToEcuMapping(MockParent(), "Map")
        iref = _iref("/DemoApplication/SWC_ModifyEcho")
        iref.setContextCompositionRef(_ref("/CanSystem/TopLevelComposition", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        mapping.addComponentIRef(iref)
        mapping.addComponentIRef(_iref("/DemoApplication/SWC_CyclicCounter"))
        mapping.setControlledHwElementRef(_ref("/HwElements/SensorActuator", "HW-ELEMENT"))
        mapping.setEcuInstanceRef(_ref("/CanSystem/ECUINSTANCES/EcuTestNode", "ECU-INSTANCE"))
        mapping.setProcessingUnitRef(_ref("/HwElements/Core0", "HW-ELEMENT"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToEcuMapping(parent, mapping)

        reloaded = SwcToEcuMapping(MockParent(), "Map")
        ARXMLParser().readSwcToEcuMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "Map"
        irefs = reloaded.getComponentIRefs()
        assert len(irefs) == 2
        assert irefs[0].getTargetComponentRef().getValue() == "/DemoApplication/SWC_ModifyEcho"
        assert irefs[0].getContextCompositionRef().getValue() == "/CanSystem/TopLevelComposition"
        assert irefs[1].getTargetComponentRef().getValue() == "/DemoApplication/SWC_CyclicCounter"
        assert reloaded.getControlledHwElementRef().getValue() == "/HwElements/SensorActuator"
        assert reloaded.getControlledHwElementRef().getDest() == "HW-ELEMENT"
        assert reloaded.getEcuInstanceRef().getValue() == "/CanSystem/ECUINSTANCES/EcuTestNode"
        assert reloaded.getProcessingUnitRef().getValue() == "/HwElements/Core0"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = system_mapping.createSwcToEcuMapping("EcuTestNodeMapping")
        mapping.addComponentIRef(_iref("/DemoApplication/SWC_ModifyEcho"))
        mapping.setEcuInstanceRef(_ref("/CanSystem/ECUINSTANCES/EcuTestNode", "ECU-INSTANCE"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSwMappings(parent, system_mapping)

        wrapper = parent.find("SW-MAPPINGS")
        assert wrapper is not None
        assert len(wrapper.findall("SWC-TO-ECU-MAPPING")) == 1

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSwMappings(_with_ns(parent), reloaded_mapping)
        sw_mappings = reloaded_mapping.getSwMappings()
        assert len(sw_mappings) == 1
        assert sw_mappings[0].getShortName() == "EcuTestNodeMapping"
        assert sw_mappings[0].getEcuInstanceRef().getValue() == "/CanSystem/ECUINSTANCES/EcuTestNode"
        assert sw_mappings[0].getComponentIRefs()[0].getTargetComponentRef().getValue() == "/DemoApplication/SWC_ModifyEcho"


def _parse_to_parent(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)
