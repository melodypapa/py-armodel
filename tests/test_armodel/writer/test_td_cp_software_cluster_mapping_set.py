"""
Writer tests for TD-CP-SOFTWARE-CLUSTER-MAPPING-SET elements — TDCpSoftwareClusterMappingSet,
Table 4.5, p.157 (R23-11).

writeTDCpSoftwareClusterMappingSet emits <TD-CP-SOFTWARE-CLUSTER-MAPPING-SET> with the
IDENTIFIABLE level (writeIdentifiable) and both aggr wrappers in XSD sequenceOffset order
(AUTOSAR_00052.xsd group TD-CP-SOFTWARE-CLUSTER-MAPPING-SET), the nested mappings with their
own groups incl. VARIATION-POINT last.

Round-trip counterpart: tests/test_armodel/parser/test_td_cp_software_cluster_mapping_set.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCpSoftwareCluster import (
    TDCpSoftwareClusterMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_mapping_set() -> TDCpSoftwareClusterMappingSet:
    mapping_set = TDCpSoftwareClusterMappingSet(AUTOSAR.getInstance(), "Set1")

    resource_mapping = mapping_set.createTdCpSoftwareClusterResourceToTdMapping("ResToTd1")
    resource_mapping.setResourceRef(RefType().setDest("CP-SOFTWARE-CLUSTER-RESOURCE").setValue("/Resources/Res1"))
    resource_mapping.setTimingDescriptionRef(RefType().setDest("TIMING-DESCRIPTION").setValue("/Timing/Desc1"))

    cluster_mapping = mapping_set.createTdCpSoftwareClusterToTdMapping("ClusterToTd1")
    cluster_mapping.setProviderRef(RefType().setDest("CP-SOFTWARE-CLUSTER").setValue("/Clusters/Provider"))
    cluster_mapping.addRequestorRef(RefType().setDest("CP-SOFTWARE-CLUSTER").setValue("/Clusters/Requestor1"))
    cluster_mapping.setTimingDescriptionRef(RefType().setDest("TIMING-DESCRIPTION").setValue("/Timing/Desc2"))
    return mapping_set


class TestWriteTDCpSoftwareClusterMappingSet:
    def test_write_emits_wrappers_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTDCpSoftwareClusterMappingSet(parent, _new_mapping_set())
        node = parent.find("TD-CP-SOFTWARE-CLUSTER-MAPPING-SET")

        assert node is not None
        assert node.find("SHORT-NAME").text == "Set1"
        children = [child.tag for child in node]
        assert children.index("TD-CP-SOFTWARE-CLUSTER-RESOURCE-TO-TD-MAPPINGS") < children.index("TD-CP-SOFTWARE-CLUSTER-TO-TD-MAPPINGS")

        cluster_mapping_node = node.find("TD-CP-SOFTWARE-CLUSTER-TO-TD-MAPPINGS/TD-CP-SOFTWARE-CLUSTER-MAPPING")
        assert cluster_mapping_node.find("PROVIDER-REF").text == "/Clusters/Provider"
        requestor_refs = cluster_mapping_node.findall("REQUESTOR-REFS/REQUESTOR-REF")
        assert len(requestor_refs) == 1
        assert requestor_refs[0].text == "/Clusters/Requestor1"

    def test_write_empty_emits_identifiable_level_only(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTDCpSoftwareClusterMappingSet(parent, TDCpSoftwareClusterMappingSet(AUTOSAR.getInstance(), "Empty"))
        node = parent.find("TD-CP-SOFTWARE-CLUSTER-MAPPING-SET")

        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("TD-CP-SOFTWARE-CLUSTER-RESOURCE-TO-TD-MAPPINGS") is None
        assert node.find("TD-CP-SOFTWARE-CLUSTER-TO-TD-MAPPINGS") is None

    def test_round_trip_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTDCpSoftwareClusterMappingSet(parent, _new_mapping_set())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = TDCpSoftwareClusterMappingSet(AUTOSAR.getInstance(), "Set1")
        ARXMLParser().readTDCpSoftwareClusterMappingSet(root.find("{%s}TD-CP-SOFTWARE-CLUSTER-MAPPING-SET" % NS), reloaded)
        assert reloaded.getShortName() == "Set1"
        assert reloaded.getTdCpSoftwareClusterResourceToTdMappings()[0].getResourceRef().getValue() == "/Resources/Res1"
        cluster_mapping = reloaded.getTdCpSoftwareClusterToTdMappings()[0]
        assert cluster_mapping.getProviderRef().getValue() == "/Clusters/Provider"
        assert cluster_mapping.getRequestorRefs()[0].getValue() == "/Clusters/Requestor1"
        assert cluster_mapping.getTimingDescriptionRef().getValue() == "/Timing/Desc2"
