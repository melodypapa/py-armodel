"""Writer round-trip tests for SystemMapping (Table 5.1, p.193).

Serialized through the MAPPINGS wrapper when aggregated by a System
(XSD group SYSTEM-MAPPING, AUTOSAR_00052.xsd l.119431: 24 child wrappers in
sequenceOffset order followed by VARIATION-POINT).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    J1939ControllerApplicationToJ1939NmNodeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System, SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import DdsCpISignalToDdsTopicMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping import PncMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import (
    RteEventInSystemSeparation,
    RteEventInSystemToOsTaskProxyMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ComponentClustering, ComponentSeparation, EcuResourceEstimation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteSystemMapping:
    def test_empty(self):
        """Test that a childless SystemMapping emits only the SHORT-NAME, no empty wrappers"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "Map")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        node = parent.find("SYSTEM-MAPPING")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Map"
        assert node.find("SW-MAPPINGS") is None
        assert node.find("MAPPING-CONSTRAINTS") is None
        assert node.find("SWC-TO-APPLICATION-PARTITION-MAPPINGS") is None
        assert node.find("J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS") is None
        assert node.find("PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS") is None

    def test_full_wrapper_order(self):
        """Test that every populated wrapper is emitted in the XSD sequenceOffset order"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "Map")
        mapping.addAppOsTaskProxyToEcuTaskProxyMapping(mapping.createAppOsTaskProxyToEcuTaskProxyMapping("AppOsTaskProxy"))
        mapping.addApplicationPartitionToEcuPartitionMapping(mapping.createApplicationPartitionToEcuPartitionMapping("AppPartition"))
        mapping.addComManagementMapping(mapping.createComManagementMapping("ComManagement"))
        mapping.addCryptoServiceMapping(mapping.createSecOcCryptoServiceMapping("CryptoService"))
        mapping.addDdsISignalToTopicMapping(DdsCpISignalToDdsTopicMapping())
        mapping.createECUMapping("EcuResourceMapping")
        mapping.addJ1939ControllerApplicationToJ1939NmNodeMapping(J1939ControllerApplicationToJ1939NmNodeMapping())
        mapping.addMappingConstraint(ComponentClustering())
        mapping.addPncMapping(PncMapping())
        mapping.createPortElementToComResourceMapping("PortElement")
        mapping.addResourceEstimation(EcuResourceEstimation())
        mapping.addRteEventSeparation(RteEventInSystemSeparation(mapping, "RteEventSeparation"))
        mapping.addRteEventToOsTaskProxyMapping(RteEventInSystemToOsTaskProxyMapping(mapping, "RteEventToOsTaskProxy"))
        mapping.addSwcToApplicationPartitionMapping(mapping.createSwcToApplicationPartitionMapping("SwcPartition"))
        mapping.createSwcToImplMapping("SwImpl")
        swc_mapping = mapping.createSwcToEcuMapping("SwMapping")
        swc_mapping.setEcuInstanceRef(_ref("/CanSystem/ECUINSTANCES/EcuTestNode", "ECU-INSTANCE"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        node = parent.find("SYSTEM-MAPPING")
        tags = [child.tag for child in node]
        assert tags == [
            "SHORT-NAME",
            "APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS",
            "APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS",
            "COM-MANAGEMENT-MAPPINGS",
            "CRYPTO-SERVICE-MAPPINGS",
            "DDS-I-SIGNAL-TO-TOPIC-MAPPINGS",
            "ECU-RESOURCE-MAPPINGS",
            "J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS",
            "MAPPING-CONSTRAINTS",
            "PNC-MAPPINGS",
            "PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS",
            "RESOURCE-ESTIMATIONS",
            "RTE-EVENT-SEPARATIONS",
            "RTE-EVENT-TO-OS-TASK-PROXY-MAPPINGS",
            "SW-IMPL-MAPPINGS",
            "SW-MAPPINGS",
            "SWC-TO-APPLICATION-PARTITION-MAPPINGS",
        ]

        sw_mappings = node.find("SW-MAPPINGS")
        swc_node = sw_mappings.find("SWC-TO-ECU-MAPPING")
        ecu_ref = swc_node.find("ECU-INSTANCE-REF")
        assert ecu_ref.text == "/CanSystem/ECUINSTANCES/EcuTestNode"
        assert ecu_ref.attrib["DEST"] == "ECU-INSTANCE"

        constraints = node.find("MAPPING-CONSTRAINTS")
        assert constraints.find("COMPONENT-CLUSTERING") is not None
        assert [child.tag for child in constraints] == ["COMPONENT-CLUSTERING"]

    def test_round_trip_new_branches(self):
        """Test write -> re-parse round trip proves reader/writer symmetry for the four new branches"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "Map")
        mapping.addJ1939ControllerApplicationToJ1939NmNodeMapping(J1939ControllerApplicationToJ1939NmNodeMapping())
        mapping.addMappingConstraint(ComponentClustering())
        mapping.addMappingConstraint(ComponentSeparation())
        mapping.createPortElementToComResourceMapping("PortElementMapping")
        mapping.createSwcToApplicationPartitionMapping("SwcPartitionMapping")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)
        reloaded = SystemMapping(AUTOSAR.getInstance(), "Map")
        ARXMLParser().readSystemMapping(root[0], reloaded)

        assert len(reloaded.getJ1939ControllerApplicationToJ1939NmNodeMappings()) == 1
        assert isinstance(reloaded.getJ1939ControllerApplicationToJ1939NmNodeMappings()[0], J1939ControllerApplicationToJ1939NmNodeMapping)
        constraints = reloaded.getMappingConstraints()
        assert isinstance(constraints[0], ComponentClustering)
        assert isinstance(constraints[1], ComponentSeparation)
        assert reloaded.getPortElementToComResourceMappings()[0].getShortName() == "PortElementMapping"
        assert reloaded.getSwcToApplicationPartitionMappings()[0].getShortName() == "SwcPartitionMapping"
        assert reloaded.getShortName() == "Map"

    def test_write_system_mappings_wrapper(self):
        """Test the System aggregator emits MAPPINGS only when non-empty"""
        system = System(AUTOSAR.getInstance(), "CanSystem")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappings(parent, system)
        assert parent.find("MAPPINGS") is None

        system.createSystemMapping("SystemMapping")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappings(parent, system)
        mappings_tag = parent.find("MAPPINGS")
        assert mappings_tag is not None
        assert mappings_tag.find("SYSTEM-MAPPING") is not None
        assert mappings_tag.find("SYSTEM-MAPPING").find("SHORT-NAME").text == "SystemMapping"
