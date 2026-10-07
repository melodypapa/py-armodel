"""Writer round-trip tests for CpSoftwareClusterMappingSet (Table 5.49, p.285).

Serialized through the CP-SOFTWARE-CLUSTER-MAPPING-SET element
(AUTOSAR_00052.xsd l.24364) under the AR-PACKAGE ELEMENTS choice (l.5016).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterMappingSet
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


def _new_set() -> CpSoftwareClusterMappingSet:
    document = AUTOSAR.getInstance()
    pkg = document.createARPackage("pkg")
    return pkg.createCpSoftwareClusterMappingSet("mapping_set")


class TestWriteCpSoftwareClusterMappingSet:
    def test_empty(self):
        mapping_set = _new_set()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterMappingSet(parent, mapping_set)

        node = parent.find("CP-SOFTWARE-CLUSTER-MAPPING-SET")
        assert node is not None
        assert node.find("PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS") is None
        assert node.find("RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS") is None
        assert node.find("SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING") is None
        assert node.find("SOFTWARE-CLUSTER-TO-RESOURCE-MAPPINGS") is None
        assert node.find("SWC-TO-APPLICATION-PARTITION-MAPPINGS") is None

    def test_full(self):
        mapping_set = _new_set()
        mapping_set.createPortElementToComResourceMapping("port_mapping")
        res_mapping = mapping_set.createResourceToApplicationPartitionMapping("res_mapping")
        res_mapping.setResourceRef(_ref("/Resources/MyResource", "CP-SOFTWARE-CLUSTER-RESOURCE"))
        sc_mapping = mapping_set.createSoftwareClusterToApplicationPartitionMapping("sc_mapping")
        sc_mapping.setSoftwareClusterRef(_ref("/Clusters/MyCluster", "CP-SOFTWARE-CLUSTER"))
        mapping_set.createSoftwareClusterToResourceMapping("scr_mapping")
        mapping_set.createSwcToApplicationPartitionMapping("swc_mapping")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterMappingSet(parent, mapping_set)

        node = parent.find("CP-SOFTWARE-CLUSTER-MAPPING-SET")
        children = [child.tag for child in node]
        assert children[-5:] == [
            "PORT-ELEMENT-TO-COM-RESOURCE-MAPPINGS",
            "RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS",
            "SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING",
            "SOFTWARE-CLUSTER-TO-RESOURCE-MAPPINGS",
            "SWC-TO-APPLICATION-PARTITION-MAPPINGS",
        ]
        assert node.find("RESOURCE-TO-APPLICATION-PARTITION-MAPPINGS/CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING/RESOURCE-REF").text == "/Resources/MyResource"
        assert node.find("SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING/SOFTWARE-CLUSTER-REF").text == "/Clusters/MyCluster"

    def test_round_trip_full(self):
        mapping_set = _new_set()
        mapping_set.createPortElementToComResourceMapping("port_mapping")
        res_mapping = mapping_set.createResourceToApplicationPartitionMapping("res_mapping")
        res_mapping.setResourceRef(_ref("/Resources/MyResource", "CP-SOFTWARE-CLUSTER-RESOURCE"))
        sc_mapping = mapping_set.createSoftwareClusterToApplicationPartitionMapping("sc_mapping")
        sc_mapping.setSoftwareClusterRef(_ref("/Clusters/MyCluster", "CP-SOFTWARE-CLUSTER"))
        mapping_set.createSoftwareClusterToResourceMapping("scr_mapping")
        mapping_set.createSwcToApplicationPartitionMapping("swc_mapping")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterMappingSet(parent, mapping_set)

        reloaded_pkg = AUTOSAR.getInstance().createARPackage("reloaded")
        reloaded = reloaded_pkg.createCpSoftwareClusterMappingSet("mapping_set")
        ARXMLParser().readCpSoftwareClusterMappingSet(_with_ns(parent)[0], reloaded)

        assert len(reloaded.getPortElementToComResourceMappings()) == 1
        res_mappings = reloaded.getResourceToApplicationPartitionMappings()
        assert len(res_mappings) == 1
        assert res_mappings[0].getResourceRef().getValue() == "/Resources/MyResource"
        assert reloaded.getSoftwareClusterToApplicationPartitionMapping().getSoftwareClusterRef().getValue() == "/Clusters/MyCluster"
        assert len(reloaded.getSoftwareClusterToResourceMappings()) == 1
        assert len(reloaded.getSwcToApplicationPartitionMappings()) == 1
