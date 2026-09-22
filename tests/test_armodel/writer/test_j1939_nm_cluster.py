"""Writer round-trip tests for J1939NmCluster (Table 6.319, p.691).

XML element order per XSD group J-1939-NM-CLUSTER: ADDRESS-CLAIM-ENABLED,
USES-DYNAMIC-ADDRESSING. Coverage runs through the NM-CLUSTERS wrapper
dispatch on NmConfig.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import J1939NmCluster, NmConfig
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _new_cluster(short_name="J1939Cluster1"):
    cluster = J1939NmCluster(MockParent(), short_name)
    cluster.setAddressClaimEnabled(_bool(True))
    cluster.setUsesDynamicAddressing(_bool(False))
    return cluster


class TestWriteJ1939NmCluster:
    def test_write_all_fields_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939NmCluster(parent, _new_cluster())
        node = parent.find("J-1939-NM-CLUSTER")
        assert node is not None
        tags = [child.tag for child in node]
        assert tags[tags.index("ADDRESS-CLAIM-ENABLED") :] == ["ADDRESS-CLAIM-ENABLED", "USES-DYNAMIC-ADDRESSING"]

    def test_write_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939NmCluster(parent, _new_cluster())
        node = parent.find("J-1939-NM-CLUSTER")
        assert node.find("ADDRESS-CLAIM-ENABLED").text == "true"
        assert node.find("USES-DYNAMIC-ADDRESSING").text == "false"

    def test_write_empty_cluster_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939NmCluster(parent, J1939NmCluster(MockParent(), "Empty"))
        node = parent.find("J-1939-NM-CLUSTER")
        assert node is not None
        assert node.find("ADDRESS-CLAIM-ENABLED") is None
        assert node.find("USES-DYNAMIC-ADDRESSING") is None

    def test_write_dispatch_via_nm_config(self):
        config = NmConfig(MockParent(), "Cfg")
        config.createJ1939NmCluster("J1939Cluster1")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfigNmClusters(parent, config)
        assert parent.find("NM-CLUSTERS/J-1939-NM-CLUSTER") is not None

    def test_round_trip_preserves_all_values(self):
        config = NmConfig(MockParent(), "Cfg")
        cluster = config.createJ1939NmCluster("J1939Cluster1")
        cluster.setAddressClaimEnabled(_bool(True))
        cluster.setUsesDynamicAddressing(_bool(False))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmConfigNmClusters(parent, config)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed_config = NmConfig(MockParent(), "Cfg")
        ARXMLParser().readNmConfigNmClusters(root[0], parsed_config)
        clusters = parsed_config.getNmClusters()
        assert len(clusters) == 1
        parsed = clusters[0]
        assert isinstance(parsed, J1939NmCluster)
        assert parsed.short_name == "J1939Cluster1"
        assert parsed.getAddressClaimEnabled().getValue() is True
        assert parsed.getUsesDynamicAddressing().getValue() is False
