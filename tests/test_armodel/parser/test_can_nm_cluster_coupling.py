import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmClusterCoupling, NmConfig
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


class TestParseCanNmClusterCoupling:
    def test_parse_can_nm_cluster_coupling_field_values(self):
        xml = (
            "<NmConfig xmlns='%s'>"
            "<NM-CLUSTER-COUPLINGS>"
            "<CAN-NM-CLUSTER-COUPLING>"
            "<COUPLED-CLUSTER-REFS>"
            "<COUPLED-CLUSTER-REF DEST='CAN-CLUSTER'>/Clusters/Can1</COUPLED-CLUSTER-REF>"
            "<COUPLED-CLUSTER-REF DEST='CAN-CLUSTER'>/Clusters/Can2</COUPLED-CLUSTER-REF>"
            "</COUPLED-CLUSTER-REFS>"
            "<NM-BUSLOAD-REDUCTION-ENABLED>true</NM-BUSLOAD-REDUCTION-ENABLED>"
            "<NM-IMMEDIATE-RESTART-ENABLED>false</NM-IMMEDIATE-RESTART-ENABLED>"
            "</CAN-NM-CLUSTER-COUPLING>"
            "</NM-CLUSTER-COUPLINGS>"
            "</NmConfig>" % NS
        )
        config = NmConfig(MockParent(), "NmConfig")
        ARXMLParser().readNmConfigNmClusterCouplings(ET.fromstring(xml), config)
        couplings = config.getNmClusterCouplings()
        assert len(couplings) == 1
        coupling = couplings[0]
        assert isinstance(coupling, CanNmClusterCoupling)
        refs = coupling.getCoupledClusterRefs()
        assert [ref.getValue() for ref in refs] == ["/Clusters/Can1", "/Clusters/Can2"]
        assert all(ref.getDest() == "CAN-CLUSTER" for ref in refs)
        assert coupling.getNmBusloadReductionEnabled().getValue() is True
        assert coupling.getNmImmediateRestartEnabled().getValue() is False
