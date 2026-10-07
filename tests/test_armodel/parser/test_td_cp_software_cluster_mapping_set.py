"""
Reader tests for TDCpSoftwareClusterMappingSet (CP_TPS_TimingExtensions Table 4.5, p.157, R23-11).

The Set is an ARPackage-level ARElement (dispatched via the TD-CP-SOFTWARE-CLUSTER-MAPPING-SET
tag of the ARPackage.element aggregate); the tests exercise readTDCpSoftwareClusterMappingSet
on a standalone subtree covering both aggr wrappers and the nested mapping classes
(AUTOSAR_00052.xsd groups TD-CP-SOFTWARE-CLUSTER-MAPPING-SET / -MAPPING / -RESOURCE-MAPPING).

Round-trip counterpart: tests/test_armodel/writer/test_td_cp_software_cluster_mapping_set.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCpSoftwareCluster import (
    TDCpSoftwareClusterMapping,
    TDCpSoftwareClusterMappingSet,
    TDCpSoftwareClusterResourceMapping,
)

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<TD-CP-SOFTWARE-CLUSTER-MAPPING-SET xmlns='%s'>%s</TD-CP-SOFTWARE-CLUSTER-MAPPING-SET>" % (NS, inner))


class TestReadTDCpSoftwareClusterMappingSet:
    def _read(self, parser, inner):
        mapping_set = TDCpSoftwareClusterMappingSet(AUTOSAR.getInstance(), "Set1")
        parser.readTDCpSoftwareClusterMappingSet(_snip(inner), mapping_set)
        return mapping_set

    def test_read_nested_mappings(self, parser):
        mapping_set = self._read(
            parser,
            "<TD-CP-SOFTWARE-CLUSTER-RESOURCE-TO-TD-MAPPINGS>"
            "<TD-CP-SOFTWARE-CLUSTER-RESOURCE-MAPPING><SHORT-NAME>ResToTd1</SHORT-NAME>"
            '<RESOURCE-REF DEST="CP-SOFTWARE-CLUSTER-RESOURCE">/Resources/Res1</RESOURCE-REF>'
            '<TIMING-DESCRIPTION-REF DEST="TIMING-DESCRIPTION">/Timing/Desc1</TIMING-DESCRIPTION-REF>'
            "</TD-CP-SOFTWARE-CLUSTER-RESOURCE-MAPPING></TD-CP-SOFTWARE-CLUSTER-RESOURCE-TO-TD-MAPPINGS>"
            "<TD-CP-SOFTWARE-CLUSTER-TO-TD-MAPPINGS>"
            "<TD-CP-SOFTWARE-CLUSTER-MAPPING><SHORT-NAME>ClusterToTd1</SHORT-NAME>"
            '<PROVIDER-REF DEST="CP-SOFTWARE-CLUSTER">/Clusters/Provider</PROVIDER-REF>'
            "<REQUESTOR-REFS>"
            '<REQUESTOR-REF DEST="CP-SOFTWARE-CLUSTER">/Clusters/Requestor1</REQUESTOR-REF>'
            '<REQUESTOR-REF DEST="CP-SOFTWARE-CLUSTER">/Clusters/Requestor2</REQUESTOR-REF>'
            "</REQUESTOR-REFS>"
            '<TIMING-DESCRIPTION-REF DEST="TIMING-DESCRIPTION">/Timing/Desc2</TIMING-DESCRIPTION-REF>'
            "</TD-CP-SOFTWARE-CLUSTER-MAPPING></TD-CP-SOFTWARE-CLUSTER-TO-TD-MAPPINGS>",
        )

        resource_mappings = mapping_set.getTdCpSoftwareClusterResourceToTdMappings()
        assert len(resource_mappings) == 1
        assert isinstance(resource_mappings[0], TDCpSoftwareClusterResourceMapping)
        assert resource_mappings[0].getShortName() == "ResToTd1"
        assert resource_mappings[0].getResourceRef().getValue() == "/Resources/Res1"
        assert resource_mappings[0].getTimingDescriptionRef().getValue() == "/Timing/Desc1"

        cluster_mappings = mapping_set.getTdCpSoftwareClusterToTdMappings()
        assert len(cluster_mappings) == 1
        assert isinstance(cluster_mappings[0], TDCpSoftwareClusterMapping)
        assert cluster_mappings[0].getProviderRef().getValue() == "/Clusters/Provider"
        assert [ref.getValue() for ref in cluster_mappings[0].getRequestorRefs()] == ["/Clusters/Requestor1", "/Clusters/Requestor2"]

    def test_read_empty_element(self, parser):
        mapping_set = self._read(parser, "")

        assert mapping_set.getTdCpSoftwareClusterResourceToTdMappings() == []
        assert mapping_set.getTdCpSoftwareClusterToTdMappings() == []

    def test_read_variation_point(self, parser):
        mapping_set = self._read(
            parser,
            "<TD-CP-SOFTWARE-CLUSTER-TO-TD-MAPPINGS>"
            "<TD-CP-SOFTWARE-CLUSTER-MAPPING><SHORT-NAME>ClusterToTd1</SHORT-NAME>"
            "<VARIATION-POINT><SHORT-LABEL>vp1</SHORT-LABEL></VARIATION-POINT>"
            "</TD-CP-SOFTWARE-CLUSTER-MAPPING></TD-CP-SOFTWARE-CLUSTER-TO-TD-MAPPINGS>",
        )

        mapping = mapping_set.getTdCpSoftwareClusterToTdMappings()[0]
        assert mapping.getVariationPoint() is not None
        assert mapping.getVariationPoint().getShortLabel().getValue() == "vp1"
