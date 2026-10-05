import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmCoordinator
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _parse_nm_coordinator(xml):
    root = ET.fromstring(xml)
    coordinator = NmCoordinator()
    ARXMLParser().readNmCoordinator(root, coordinator)
    return coordinator


class TestParseNmCoordinator:
    def test_parse_nm_coordinator_field_values(self):
        xml = (
            "<NM-COORDINATOR xmlns='%s'>"
            "<INDEX>1</INDEX>"
            "<NM-COORD-SYNC-SUPPORT>true</NM-COORD-SYNC-SUPPORT>"
            "<NM-GLOBAL-COORDINATOR-TIME>2.5</NM-GLOBAL-COORDINATOR-TIME>"
            "<NM-NODE-REFS>"
            "<NM-NODE-REF DEST='NM-NODE'>/Clusters/Can1/node</NM-NODE-REF>"
            "</NM-NODE-REFS>"
            "</NM-COORDINATOR>" % NS
        )
        coordinator = _parse_nm_coordinator(xml)
        assert coordinator.getIndex().getValue() == 1
        assert coordinator.getNmCoordSyncSupport().getValue() is True
        assert coordinator.getNmGlobalCoordinatorTime().getValue() == 2.5
        nodes = coordinator.getNmNodes()
        assert len(nodes) == 1
        assert nodes[0].getDest() == "NM-NODE"
        assert nodes[0].getValue() == "/Clusters/Can1/node"

    def test_parse_nm_coordinator_empty(self):
        xml = "<NM-COORDINATOR xmlns='%s'/>" % NS
        coordinator = _parse_nm_coordinator(xml)
        assert coordinator.getIndex() is None
        assert coordinator.getNmCoordSyncSupport() is None
        assert coordinator.getNmGlobalCoordinatorTime() is None
        assert coordinator.getNmNodes() == []
