"""Parser round-trip tests for NmClusterCoupling (Table 6.305, p.676).

NmClusterCoupling is abstract with zero attribute rows, so coverage runs
through its concrete subclasses via the NM-CLUSTER-COUPLINGS wrapper dispatch.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    CanNmClusterCoupling,
    NmClusterCoupling,
    NmConfig,
    UdpNmClusterCoupling,
)
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


def _parse_couplings(xml):
    root = ET.fromstring(xml)
    config = NmConfig(MockParent(), "NmConfig")
    ARXMLParser().readNmConfigNmClusterCouplings(root, config)
    return config


class TestParseNmClusterCoupling:
    def test_parse_can_nm_cluster_coupling_field_values(self):
        xml = (
            "<NmConfig xmlns='%s'>"
            "<NM-CLUSTER-COUPLINGS>"
            "<CAN-NM-CLUSTER-COUPLING>"
            "<COUPLED-CLUSTER-REFS><COUPLED-CLUSTER-REF DEST='CAN-CLUSTER'>/Clusters/Can1</COUPLED-CLUSTER-REF></COUPLED-CLUSTER-REFS>"
            "<NM-BUSLOAD-REDUCTION-ENABLED>true</NM-BUSLOAD-REDUCTION-ENABLED>"
            "<NM-IMMEDIATE-RESTART-ENABLED>false</NM-IMMEDIATE-RESTART-ENABLED>"
            "</CAN-NM-CLUSTER-COUPLING>"
            "</NM-CLUSTER-COUPLINGS>"
            "</NmConfig>" % NS
        )
        config = _parse_couplings(xml)
        couplings = config.getNmClusterCouplings()
        assert len(couplings) == 1
        coupling = couplings[0]
        assert isinstance(coupling, NmClusterCoupling)
        assert isinstance(coupling, CanNmClusterCoupling)
        refs = coupling.getCoupledClusterRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/Clusters/Can1"
        assert refs[0].getDest() == "CAN-CLUSTER"
        assert coupling.getNmBusloadReductionEnabled().getValue() is True
        assert coupling.getNmImmediateRestartEnabled().getValue() is False

    def test_parse_udp_nm_cluster_coupling_field_values(self):
        xml = (
            "<NmConfig xmlns='%s'>"
            "<NM-CLUSTER-COUPLINGS>"
            "<UDP-NM-CLUSTER-COUPLING>"
            "<COUPLED-CLUSTER-REFS><COUPLED-CLUSTER-REF DEST='ETHERNET-CLUSTER'>/Clusters/Eth1</COUPLED-CLUSTER-REF></COUPLED-CLUSTER-REFS>"
            "<NM-IMMEDIATE-RESTART-ENABLED>true</NM-IMMEDIATE-RESTART-ENABLED>"
            "</UDP-NM-CLUSTER-COUPLING>"
            "</NM-CLUSTER-COUPLINGS>"
            "</NmConfig>" % NS
        )
        config = _parse_couplings(xml)
        couplings = config.getNmClusterCouplings()
        assert len(couplings) == 1
        coupling = couplings[0]
        assert isinstance(coupling, UdpNmClusterCoupling)
        assert isinstance(coupling, NmClusterCoupling)
        assert coupling.getCoupledClusterRefs()[0].getValue() == "/Clusters/Eth1"
        assert coupling.getNmImmediateRestartEnabled().getValue() is True

    def test_parse_empty_wrapper(self):
        xml = "<NmConfig xmlns='%s'><NM-CLUSTER-COUPLINGS></NM-CLUSTER-COUPLINGS></NmConfig>" % NS
        config = _parse_couplings(xml)
        assert config.getNmClusterCouplings() == []
