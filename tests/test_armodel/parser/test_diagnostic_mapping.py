"""Parser tests for DiagnosticMapping (Table 5.1, p.223).

DiagnosticMapping is an abstract base: its XML group DIAGNOSTIC-MAPPING
(AUTOSAR_00052.xsd l.39242) element order is PROVIDER-SOFTWARE-CLUSTER-REF,
REQUESTER-SOFTWARE-CLUSTER-REF. The reusable readDiagnosticMapping helper is
exercised through the concrete subclass CpSwClusterToDiagEventMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSwClusterToDiagEventMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "CP-SW-CLUSTER-TO-DIAG-EVENT-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticMapping:
    def test_read_sets_both_refs(self, parser):
        mapping = CpSwClusterToDiagEventMapping(AUTOSAR.getInstance(), "Map1")
        element = _snip(
            "<SHORT-NAME>Map1</SHORT-NAME>"
            "<PROVIDER-SOFTWARE-CLUSTER-REF DEST='CP-SOFTWARE-CLUSTER'>/AUTOSAR/SoftwareClusters/ProviderCluster</PROVIDER-SOFTWARE-CLUSTER-REF>"
            "<REQUESTER-SOFTWARE-CLUSTER-REF DEST='CP-SOFTWARE-CLUSTER'>/AUTOSAR/SoftwareClusters/RequesterCluster</REQUESTER-SOFTWARE-CLUSTER-REF>"
        )
        parser.readDiagnosticMapping(element, mapping)
        assert mapping.getProviderSoftwareClusterRef().getValue() == "/AUTOSAR/SoftwareClusters/ProviderCluster"
        assert mapping.getProviderSoftwareClusterRef().getDest() == "CP-SOFTWARE-CLUSTER"
        assert mapping.getRequesterSoftwareClusterRef().getValue() == "/AUTOSAR/SoftwareClusters/RequesterCluster"
        assert mapping.getRequesterSoftwareClusterRef().getDest() == "CP-SOFTWARE-CLUSTER"

    def test_read_empty(self, parser):
        mapping = CpSwClusterToDiagEventMapping(AUTOSAR.getInstance(), "Map1")
        parser.readDiagnosticMapping(_snip("<SHORT-NAME>Map1</SHORT-NAME>"), mapping)
        assert mapping.getProviderSoftwareClusterRef() is None
        assert mapping.getRequesterSoftwareClusterRef() is None
