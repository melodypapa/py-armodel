import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import FlexrayNmClusterCoupling, NmConfig
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestParseFlexrayNmClusterCoupling:
    def test_parse_flexray_nm_cluster_coupling_field_values(self):
        xml = (
            "<NmConfig xmlns='%s'>"
            "<NM-CLUSTER-COUPLINGS>"
            "<FLEXRAY-NM-CLUSTER-COUPLING>"
            "<COUPLED-CLUSTER-REFS>"
            "<COUPLED-CLUSTER-REF DEST='FLEXRAY-CLUSTER'>/Clusters/Fr1</COUPLED-CLUSTER-REF>"
            "<COUPLED-CLUSTER-REF DEST='FLEXRAY-CLUSTER'>/Clusters/Fr2</COUPLED-CLUSTER-REF>"
            "</COUPLED-CLUSTER-REFS>"
            "<NM-SCHEDULE-VARIANT>SCHEDULEVARIANT2</NM-SCHEDULE-VARIANT>"
            "</FLEXRAY-NM-CLUSTER-COUPLING>"
            "</NM-CLUSTER-COUPLINGS>"
            "</NmConfig>" % NS
        )
        config = NmConfig(MockParent(), "NmConfig")
        ARXMLParser().readNmConfigNmClusterCouplings(ET.fromstring(xml), config)
        couplings = config.getNmClusterCouplings()
        assert len(couplings) == 1
        coupling = couplings[0]
        assert isinstance(coupling, FlexrayNmClusterCoupling)
        refs = coupling.getCoupledClusterRefs()
        assert [ref.getValue() for ref in refs] == ["/Clusters/Fr1", "/Clusters/Fr2"]
        assert all(ref.getDest() == "FLEXRAY-CLUSTER" for ref in refs)
        assert coupling.getNmScheduleVariant().getValue() == "SCHEDULEVARIANT2"

    def test_parse_flexray_nm_cluster_coupling_without_schedule_variant(self):
        xml = "<NmConfig xmlns='%s'>" "<NM-CLUSTER-COUPLINGS>" "<FLEXRAY-NM-CLUSTER-COUPLING/>" "</NM-CLUSTER-COUPLINGS>" "</NmConfig>" % NS
        config = NmConfig(MockParent(), "NmConfig")
        ARXMLParser().readNmConfigNmClusterCouplings(ET.fromstring(xml), config)
        coupling = config.getNmClusterCouplings()[0]
        assert coupling.getCoupledClusterRefs() == []
        assert coupling.getNmScheduleVariant() is None

    def test_parse_flexray_nm_cluster_coupling_reads_checksum_and_timestamp(self):
        xml = (
            "<NmConfig xmlns='%s'>"
            "<NM-CLUSTER-COUPLINGS>"
            "<FLEXRAY-NM-CLUSTER-COUPLING S='9012' T='2024-01-01T00:00:00Z'>"
            "<NM-SCHEDULE-VARIANT>SCHEDULEVARIANT2</NM-SCHEDULE-VARIANT>"
            "</FLEXRAY-NM-CLUSTER-COUPLING>"
            "</NM-CLUSTER-COUPLINGS>"
            "</NmConfig>" % NS
        )
        config = NmConfig(MockParent(), "NmConfig")
        ARXMLParser().readNmConfigNmClusterCouplings(ET.fromstring(xml), config)
        coupling = config.getNmClusterCouplings()[0]
        assert coupling.getChecksum().getValue() == "9012"
        assert coupling.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_parse_flexray_nm_cluster_coupling_reads_variation_point(self):
        xml = (
            "<NmConfig xmlns='%s'>"
            "<NM-CLUSTER-COUPLINGS>"
            "<FLEXRAY-NM-CLUSTER-COUPLING>"
            "<NM-SCHEDULE-VARIANT>SCHEDULEVARIANT2</NM-SCHEDULE-VARIANT>"
            "<VARIATION-POINT><SHORT-LABEL>VP3</SHORT-LABEL></VARIATION-POINT>"
            "</FLEXRAY-NM-CLUSTER-COUPLING>"
            "</NM-CLUSTER-COUPLINGS>"
            "</NmConfig>" % NS
        )
        config = NmConfig(MockParent(), "NmConfig")
        ARXMLParser().readNmConfigNmClusterCouplings(ET.fromstring(xml), config)
        coupling = config.getNmClusterCouplings()[0]
        assert coupling.getVariationPoint() is not None
        assert coupling.getVariationPoint().getShortLabel().getValue() == "VP3"
