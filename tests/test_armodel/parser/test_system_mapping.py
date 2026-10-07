"""Parser tests for SystemMapping (Table 5.1, p.193).

Identifiable aggregated by System.mapping through the MAPPINGS wrapper
(XSD group SYSTEM-MAPPING, AUTOSAR_00052.xsd l.119431: 24 child wrappers in
sequenceOffset order followed by VARIATION-POINT).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ComponentClustering,
    ComponentSeparation,
    J1939ControllerApplicationToJ1939NmNodeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    PortElementToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System, SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import SwcToApplicationPartitionMapping, SwcToEcuMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


class TestReadSystemMapping:
    def test_read_new_dispatch_branches(self):
        """Test the four wrappers missing reader coverage: J1939, MAPPING-CONSTRAINTS, PORT-ELEMENT, SWC-TO-APPLICATION-PARTITION"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip(
            "<SYSTEM-MAPPING>"
            "<SHORT-NAME>SystemMapping</SHORT-NAME>"
            "<J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS>"
            "<J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPING S='5' T='2024-01-01T00:00:00Z'/>"
            "</J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS>"
            "<MAPPING-CONSTRAINTS>"
            "<COMPONENT-CLUSTERING/>"
            "<COMPONENT-SEPARATION/>"
            "</MAPPING-CONSTRAINTS>"
            "<PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS>"
            "<PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING>"
            "<SHORT-NAME>PortElementMapping</SHORT-NAME>"
            "</PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING>"
            "</PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS>"
            "<SWC-TO-APPLICATION-PARTITION-MAPPINGS>"
            "<SWC-TO-APPLICATION-PARTITION-MAPPING>"
            "<SHORT-NAME>SwcPartitionMapping</SHORT-NAME>"
            "</SWC-TO-APPLICATION-PARTITION-MAPPING>"
            "</SWC-TO-APPLICATION-PARTITION-MAPPINGS>"
            "</SYSTEM-MAPPING>"
        )
        ARXMLParser().readSystemMapping(root[0], mapping)

        j1939_mappings = mapping.getJ1939ControllerApplicationToJ1939NmNodeMappings()
        assert len(j1939_mappings) == 1
        assert isinstance(j1939_mappings[0], J1939ControllerApplicationToJ1939NmNodeMapping)
        assert j1939_mappings[0].getChecksum().getValue() == "5"
        assert j1939_mappings[0].getTimestamp().getValue() == "2024-01-01T00:00:00Z"

        constraints = mapping.getMappingConstraints()
        assert len(constraints) == 2
        assert isinstance(constraints[0], ComponentClustering)
        assert isinstance(constraints[1], ComponentSeparation)

        port_mappings = mapping.getPortElementToComResourceMappings()
        assert len(port_mappings) == 1
        assert isinstance(port_mappings[0], PortElementToCommunicationResourceMapping)
        assert port_mappings[0].getShortName() == "PortElementMapping"

        swc_mappings = mapping.getSwcToApplicationPartitionMappings()
        assert len(swc_mappings) == 1
        assert isinstance(swc_mappings[0], SwcToApplicationPartitionMapping)
        assert swc_mappings[0].getShortName() == "SwcPartitionMapping"

    def test_read_swc_to_ecu_mapping_field_values(self):
        """Test that nested SwcToEcuMapping field values survive the SystemMapping reader"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip(
            "<SYSTEM-MAPPING>"
            "<SHORT-NAME>SystemMapping</SHORT-NAME>"
            "<SW-MAPPINGS>"
            "<SWC-TO-ECU-MAPPING>"
            "<SHORT-NAME>EcuTestNodeMapping</SHORT-NAME>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/CanSystem/ECUINSTANCES/EcuTestNode</ECU-INSTANCE-REF>"
            "</SWC-TO-ECU-MAPPING>"
            "</SW-MAPPINGS>"
            "</SYSTEM-MAPPING>"
        )
        ARXMLParser().readSystemMapping(root[0], mapping)

        sw_mappings = mapping.getSwMappings()
        assert len(sw_mappings) == 1
        assert isinstance(sw_mappings[0], SwcToEcuMapping)
        assert sw_mappings[0].getShortName() == "EcuTestNodeMapping"
        assert sw_mappings[0].getEcuInstanceRef().getValue() == "/CanSystem/ECUINSTANCES/EcuTestNode"
        assert sw_mappings[0].getEcuInstanceRef().getDest() == "ECU-INSTANCE"

    def test_read_identifiable_level_once(self):
        """Test that the inherited Identifiable level (SHORT-NAME, UUID, CATEGORY) is read exactly once"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip("<SYSTEM-MAPPING UUID='1e1a1a1a-2b2b-3c3c-4d4d-5e5e5e5e5e5e'>" "<SHORT-NAME>SystemMapping</SHORT-NAME>" "<CATEGORY>SOME_CATEGORY</CATEGORY>" "</SYSTEM-MAPPING>")
        ARXMLParser().readSystemMapping(root[0], mapping)

        assert mapping.getShortName() == "SystemMapping"
        assert mapping.getUuid().getValue() == "1e1a1a1a-2b2b-3c3c-4d4d-5e5e5e5e5e5e"
        assert mapping.getCategory().getValue() == "SOME_CATEGORY"
        assert len(mapping.getMappingConstraints()) == 0

    def test_read_empty_wrapper(self):
        """Test that empty child wrappers leave every list empty"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip("<SYSTEM-MAPPING>" "<SHORT-NAME>SystemMapping</SHORT-NAME>" "<MAPPING-CONSTRAINTS/>" "<SW-MAPPINGS/>" "<SWC-TO-APPLICATION-PARTITION-MAPPINGS/>" "</SYSTEM-MAPPING>")
        ARXMLParser().readSystemMapping(root[0], mapping)

        assert mapping.getMappingConstraints() == []
        assert mapping.getSwMappings() == []
        assert mapping.getSwcToApplicationPartitionMappings() == []

    def test_read_system_mappings_dispatch(self):
        """Test the System aggregator dispatch creates a SystemMapping from MAPPINGS/SYSTEM-MAPPING"""
        system = System(AUTOSAR.getInstance(), "CanSystem")
        root = _snip("<SYSTEM>" "<SHORT-NAME>CanSystem</SHORT-NAME>" "<MAPPINGS>" "<SYSTEM-MAPPING>" "<SHORT-NAME>SystemMapping</SHORT-NAME>" "</SYSTEM-MAPPING>" "</MAPPINGS>" "</SYSTEM>")
        ARXMLParser().readSystemMappings(root[0], system)

        mappings = system.getMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], SystemMapping)
        assert mappings[0].getShortName() == "SystemMapping"
