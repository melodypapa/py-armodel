"""Writer round-trip tests for DiagnosticMapping (Table 5.1, p.223).

DiagnosticMapping is an abstract base: its XML group DIAGNOSTIC-MAPPING
(AUTOSAR_00052.xsd l.39242) element order is PROVIDER-SOFTWARE-CLUSTER-REF,
REQUESTER-SOFTWARE-CLUSTER-REF. The reusable writeDiagnosticMapping helper is
exercised through the concrete subclass CpSwClusterToDiagEventMapping.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSwClusterToDiagEventMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_mapping() -> CpSwClusterToDiagEventMapping:
    mapping = CpSwClusterToDiagEventMapping(AUTOSAR.getInstance(), "Map1")

    provider_ref = RefType()
    provider_ref.setDest("CP-SOFTWARE-CLUSTER")
    provider_ref.setValue("/AUTOSAR/SoftwareClusters/ProviderCluster")
    mapping.setProviderSoftwareClusterRef(provider_ref)

    requester_ref = RefType()
    requester_ref.setDest("CP-SOFTWARE-CLUSTER")
    requester_ref.setValue("/AUTOSAR/SoftwareClusters/RequesterCluster")
    mapping.setRequesterSoftwareClusterRef(requester_ref)
    return mapping


class TestWriteDiagnosticMapping:
    def test_write_refs_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticMapping(parent, _new_mapping())
        assert [child.tag for child in parent] == ["SHORT-NAME", "PROVIDER-SOFTWARE-CLUSTER-REF", "REQUESTER-SOFTWARE-CLUSTER-REF"]
        provider = parent.find("PROVIDER-SOFTWARE-CLUSTER-REF")
        assert provider.attrib["DEST"] == "CP-SOFTWARE-CLUSTER"
        assert provider.text == "/AUTOSAR/SoftwareClusters/ProviderCluster"
        requester = parent.find("REQUESTER-SOFTWARE-CLUSTER-REF")
        assert requester.attrib["DEST"] == "CP-SOFTWARE-CLUSTER"
        assert requester.text == "/AUTOSAR/SoftwareClusters/RequesterCluster"

    def test_write_empty_refs_omits_optional_tags(self):
        mapping = CpSwClusterToDiagEventMapping(AUTOSAR.getInstance(), "Map2")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticMapping(parent, mapping)
        assert [child.tag for child in parent] == ["SHORT-NAME"]
        assert parent.find("PROVIDER-SOFTWARE-CLUSTER-REF") is None
        assert parent.find("REQUESTER-SOFTWARE-CLUSTER-REF") is None

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticMapping(parent, _new_mapping())
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = CpSwClusterToDiagEventMapping(AUTOSAR.getInstance(), "Map3")
        ARXMLParser().readDiagnosticMapping(root, parsed)
        assert parsed.getProviderSoftwareClusterRef().getValue() == "/AUTOSAR/SoftwareClusters/ProviderCluster"
        assert parsed.getProviderSoftwareClusterRef().getDest() == "CP-SOFTWARE-CLUSTER"
        assert parsed.getRequesterSoftwareClusterRef().getValue() == "/AUTOSAR/SoftwareClusters/RequesterCluster"
        assert parsed.getRequesterSoftwareClusterRef().getDest() == "CP-SOFTWARE-CLUSTER"
