"""Writer round-trip tests for CpSoftwareClusterToApplicationPartitionMapping (Table 5.50, p.287).

Serialized through the CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING element
(AUTOSAR_00052.xsd l.24698) and the SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPINGS
wrapper of SystemMapping (l.119647).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterToApplicationPartitionMapping
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


class TestWriteCpSoftwareClusterToApplicationPartitionMapping:
    def test_empty(self):
        mapping = CpSoftwareClusterToApplicationPartitionMapping(None, "mapping")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterToApplicationPartitionMapping(parent, mapping)

        node = parent.find("CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING")
        assert node is not None
        assert node.find("APPLICATION-PARTITION-REFS") is None
        assert node.find("SOFTWARE-CLUSTER-REF") is None

    def test_full(self):
        mapping = CpSoftwareClusterToApplicationPartitionMapping(None, "mapping")
        mapping.addApplicationPartitionRef(_ref("/Partitions/Partition1", "APPLICATION-PARTITION"))
        mapping.addApplicationPartitionRef(_ref("/Partitions/Partition2", "APPLICATION-PARTITION"))
        mapping.setSoftwareClusterRef(_ref("/Clusters/MyCluster", "CP-SOFTWARE-CLUSTER"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterToApplicationPartitionMapping(parent, mapping)

        node = parent.find("CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING")
        children = [child.tag for child in node]
        assert children[-2:] == ["APPLICATION-PARTITION-REFS", "SOFTWARE-CLUSTER-REF"]
        refs = node.findall("APPLICATION-PARTITION-REFS/APPLICATION-PARTITION-REF")
        assert [ref.text for ref in refs] == ["/Partitions/Partition1", "/Partitions/Partition2"]
        assert refs[0].get("DEST") == "APPLICATION-PARTITION"
        assert node.find("SOFTWARE-CLUSTER-REF").get("DEST") == "CP-SOFTWARE-CLUSTER"

    def test_round_trip_full(self):
        mapping = CpSoftwareClusterToApplicationPartitionMapping(None, "mapping")
        mapping.addApplicationPartitionRef(_ref("/Partitions/Partition1", "APPLICATION-PARTITION"))
        mapping.setSoftwareClusterRef(_ref("/Clusters/MyCluster", "CP-SOFTWARE-CLUSTER"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterToApplicationPartitionMapping(parent, mapping)

        reloaded = CpSoftwareClusterToApplicationPartitionMapping(None, "mapping")
        ARXMLParser().readCpSoftwareClusterToApplicationPartitionMapping(_with_ns(parent)[0], reloaded)

        assert len(reloaded.getApplicationPartitionRefs()) == 1
        assert reloaded.getApplicationPartitionRefs()[0].getValue() == "/Partitions/Partition1"
        assert reloaded.getSoftwareClusterRef().getValue() == "/Clusters/MyCluster"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = CpSoftwareClusterToApplicationPartitionMapping(system_mapping, "mapping")
        mapping.setSoftwareClusterRef(_ref("/Clusters/MyCluster", "CP-SOFTWARE-CLUSTER"))
        system_mapping.addSoftwareClusterToApplicationPartitionMapping(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSoftwareClusterToApplicationPartitionMappings(parent, system_mapping)

        wrapper = parent.find("SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPINGS")
        assert wrapper is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSoftwareClusterToApplicationPartitionMappings(_with_ns(parent), reloaded_mapping)
        mappings = reloaded_mapping.getSoftwareClusterToApplicationPartitionMappings()
        assert len(mappings) == 1
        assert mappings[0].getSoftwareClusterRef().getValue() == "/Clusters/MyCluster"
