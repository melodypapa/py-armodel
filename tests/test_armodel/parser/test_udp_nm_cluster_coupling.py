import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmConfig, UdpNmClusterCoupling
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


class TestParseUdpNmClusterCoupling:
    def test_parse_udp_nm_cluster_coupling_field_values(self):
        xml = (
            "<NmConfig xmlns='%s'>"
            "<NM-CLUSTER-COUPLINGS>"
            "<UDP-NM-CLUSTER-COUPLING>"
            "<COUPLED-CLUSTER-REFS>"
            "<COUPLED-CLUSTER-REF DEST='ETHERNET-CLUSTER'>/Clusters/Eth1</COUPLED-CLUSTER-REF>"
            "</COUPLED-CLUSTER-REFS>"
            "<NM-IMMEDIATE-RESTART-ENABLED>true</NM-IMMEDIATE-RESTART-ENABLED>"
            "</UDP-NM-CLUSTER-COUPLING>"
            "</NM-CLUSTER-COUPLINGS>"
            "</NmConfig>" % NS
        )
        config = NmConfig(MockParent(), "NmConfig")
        ARXMLParser().readNmConfigNmClusterCouplings(ET.fromstring(xml), config)
        couplings = config.getNmClusterCouplings()
        assert len(couplings) == 1
        coupling = couplings[0]
        assert isinstance(coupling, UdpNmClusterCoupling)
        refs = coupling.getCoupledClusterRefs()
        assert [ref.getValue() for ref in refs] == ["/Clusters/Eth1"]
        assert refs[0].getDest() == "ETHERNET-CLUSTER"
        assert coupling.getNmImmediateRestartEnabled().getValue() is True
