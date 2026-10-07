"""Parser tests for SwcToApplicationPartitionMapping (Table 5.4, p.200).

Identifiable aggregated through the SWC-TO-APPLICATION-PARTITION-MAPPINGS wrapper
(XSD group SWC-TO-APPLICATION-PARTITION-MAPPING, AUTOSAR_00052.xsd l.117837:
APPLICATION-PARTITION-REF, SW-COMPONENT-PROTOTYPE-IREF, VARIATION-POINT).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterMappingSet
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import SwcToApplicationPartitionMapping
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


SWC_MAPPING = (
    "<SWC-TO-APPLICATION-PARTITION-MAPPING UUID='2b2b2b2b-3c3c-4d4d-5e5e-6f6f6f6f6f6f'>"
    "<SHORT-NAME>SwcPartitionMapping</SHORT-NAME>"
    "<APPLICATION-PARTITION-REF DEST='APPLICATION-PARTITION'>/System/ApplicationPartitions/AP1</APPLICATION-PARTITION-REF>"
    "<SW-COMPONENT-PROTOTYPE-IREF>"
    "<CONTEXT-COMPOSITION-REF DEST='COMPOSITION-SW-COMPONENT-TYPE'>/System/Composition</CONTEXT-COMPOSITION-REF>"
    "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/System/Composition/Swc1</TARGET-COMPONENT-REF>"
    "</SW-COMPONENT-PROTOTYPE-IREF>"
    "</SWC-TO-APPLICATION-PARTITION-MAPPING>"
)


class TestReadSwcToApplicationPartitionMapping:
    def test_read_field_values_via_system_mapping(self):
        """Test that applicationPartitionRef and swComponentPrototypeIRef field values survive the reader"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip(
            "<SYSTEM-MAPPING>" "<SHORT-NAME>SystemMapping</SHORT-NAME>" "<SWC-TO-APPLICATION-PARTITION-MAPPINGS>" + SWC_MAPPING + "</SWC-TO-APPLICATION-PARTITION-MAPPINGS>" "</SYSTEM-MAPPING>"
        )
        ARXMLParser().readSystemMapping(root[0], mapping)

        swc_mappings = mapping.getSwcToApplicationPartitionMappings()
        assert len(swc_mappings) == 1
        swc_mapping = swc_mappings[0]
        assert isinstance(swc_mapping, SwcToApplicationPartitionMapping)
        assert swc_mapping.getShortName() == "SwcPartitionMapping"
        assert swc_mapping.getUuid().getValue() == "2b2b2b2b-3c3c-4d4d-5e5e-6f6f6f6f6f6f"

        partition_ref = swc_mapping.getApplicationPartitionRef()
        assert partition_ref.getValue() == "/System/ApplicationPartitions/AP1"
        assert partition_ref.getDest() == "APPLICATION-PARTITION"

        iref = swc_mapping.getSwComponentPrototypeIRef()
        assert iref.getContextCompositionRef().getValue() == "/System/Composition"
        assert iref.getContextCompositionRef().getDest() == "COMPOSITION-SW-COMPONENT-TYPE"
        assert iref.getTargetComponentRef().getValue() == "/System/Composition/Swc1"
        assert iref.getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"

    def test_read_via_cp_software_cluster_mapping_set(self):
        """Test that the CpSoftwareClusterMappingSet aggregator dispatch reaches the same reader level"""
        mapping_set = CpSoftwareClusterMappingSet(AUTOSAR.getInstance(), "MappingSet")
        root = _snip(
            "<CP-SOFTWARE-CLUSTER-MAPPING-SET>"
            "<SHORT-NAME>MappingSet</SHORT-NAME>"
            "<SWC-TO-APPLICATION-PARTITION-MAPPINGS>" + SWC_MAPPING + "</SWC-TO-APPLICATION-PARTITION-MAPPINGS>"
            "</CP-SOFTWARE-CLUSTER-MAPPING-SET>"
        )
        ARXMLParser().readCpSoftwareClusterMappingSet(root[0], mapping_set)

        swc_mappings = mapping_set.getSwcToApplicationPartitionMappings()
        assert len(swc_mappings) == 1
        swc_mapping = swc_mappings[0]
        assert swc_mapping.getShortName() == "SwcPartitionMapping"
        assert swc_mapping.getApplicationPartitionRef().getValue() == "/System/ApplicationPartitions/AP1"
        assert swc_mapping.getSwComponentPrototypeIRef().getTargetComponentRef().getValue() == "/System/Composition/Swc1"

    def test_read_empty_wrapper(self):
        """Test that an empty wrapper leaves the list empty and both fields None"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip("<SYSTEM-MAPPING>" "<SHORT-NAME>SystemMapping</SHORT-NAME>" "<SWC-TO-APPLICATION-PARTITION-MAPPINGS/>" "</SYSTEM-MAPPING>")
        ARXMLParser().readSystemMapping(root[0], mapping)

        assert mapping.getSwcToApplicationPartitionMappings() == []
