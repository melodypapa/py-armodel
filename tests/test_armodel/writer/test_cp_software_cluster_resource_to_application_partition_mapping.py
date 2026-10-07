"""Writer round-trip tests for CpSoftwareClusterResourceToApplicationPartitionMapping (Table 5.48, p.284).

Serialized through the CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING
element (AUTOSAR_00052.xsd l.24578) and the RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS
wrapper of SystemMapping (l.119598).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterResourceToApplicationPartitionMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteCpSoftwareClusterResourceToApplicationPartitionMapping:
    def test_empty(self):
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(None, "mapping")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterResourceToApplicationPartitionMapping(parent, mapping)

        node = parent.find("CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING")
        assert node is not None
        assert node.find("APPLICATION-PARTITION-REF") is None
        assert node.find("RESOURCE-REF") is None

    def test_full(self):
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(None, "mapping")
        mapping.setApplicationPartitionRef(_ref("/Partitions/MyPartition", "APPLICATION-PARTITION"))
        mapping.setResourceRef(_ref("/Resources/MyResource", "CP-SOFTWARE-CLUSTER-RESOURCE"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterResourceToApplicationPartitionMapping(parent, mapping)

        node = parent.find("CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING")
        assert node.find("APPLICATION-PARTITION-REF").text == "/Partitions/MyPartition"
        assert node.find("APPLICATION-PARTITION-REF").get("DEST") == "APPLICATION-PARTITION"
        assert node.find("RESOURCE-REF").text == "/Resources/MyResource"
        assert node.find("RESOURCE-REF").get("DEST") == "CP-SOFTWARE-CLUSTER-RESOURCE"

    def test_element_order(self):
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(None, "mapping")
        mapping.setApplicationPartitionRef(_ref("/Partitions/MyPartition", "APPLICATION-PARTITION"))
        mapping.setResourceRef(_ref("/Resources/MyResource", "CP-SOFTWARE-CLUSTER-RESOURCE"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterResourceToApplicationPartitionMapping(parent, mapping)

        node = parent.find("CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING")
        children = [child.tag for child in node]
        assert children[-2:] == ["APPLICATION-PARTITION-REF", "RESOURCE-REF"]

    def test_round_trip_full(self):
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(None, "mapping")
        mapping.setApplicationPartitionRef(_ref("/Partitions/MyPartition", "APPLICATION-PARTITION"))
        mapping.setResourceRef(_ref("/Resources/MyResource", "CP-SOFTWARE-CLUSTER-RESOURCE"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterResourceToApplicationPartitionMapping(parent, mapping)

        reloaded = CpSoftwareClusterResourceToApplicationPartitionMapping(None, "mapping")
        ARXMLParser().readCpSoftwareClusterResourceToApplicationPartitionMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getApplicationPartitionRef().getValue() == "/Partitions/MyPartition"
        assert reloaded.getResourceRef().getValue() == "/Resources/MyResource"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(system_mapping, "mapping")
        mapping.setResourceRef(_ref("/Resources/MyResource", "CP-SOFTWARE-CLUSTER-RESOURCE"))
        system_mapping.addResourceToApplicationPartitionMapping(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingResourceToApplicationPartitionMappings(parent, system_mapping)

        wrapper = parent.find("RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS")
        assert wrapper is not None
        assert wrapper.find("CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING") is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingResourceToApplicationPartitionMappings(_with_ns(parent), reloaded_mapping)
        mappings = reloaded_mapping.getResourceToApplicationPartitionMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], CpSoftwareClusterResourceToApplicationPartitionMapping)
        assert mappings[0].getResourceRef().getValue() == "/Resources/MyResource"

    def test_round_trip_via_system_mapping_empty_wrapper(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingResourceToApplicationPartitionMappings(parent, system_mapping)

        assert parent.find("RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS") is None
