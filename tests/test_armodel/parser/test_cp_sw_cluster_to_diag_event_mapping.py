"""Parser tests for CpSwClusterToDiagEventMapping (Table 5.46, p.272).

XSD group CP-SW-CLUSTER-TO-DIAG-EVENT-MAPPING element order (AUTOSAR_00052.xsd): CP-SOFTWARE-CLUSTER-RESOURCE-REF, DIAGNOSTIC-EVENT-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSwClusterToDiagEventMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "CP-SW-CLUSTER-TO-DIAG-EVENT-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadCpSwClusterToDiagEventMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = CpSwClusterToDiagEventMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<CP-SOFTWARE-CLUSTER-RESOURCE-REF DEST='DEST'>/AUTOSAR/CpSoftwareClusterResource1</CP-SOFTWARE-CLUSTER-RESOURCE-REF><DIAGNOSTIC-EVENT-REF DEST='DEST'>/AUTOSAR/DiagnosticEvent1</DIAGNOSTIC-EVENT-REF>"
        )
        parser.readCpSwClusterToDiagEventMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getCpSoftwareClusterResourceRef() is not None
        assert mapping.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"
        assert mapping.getDiagnosticEventRef() is not None
        assert mapping.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"

    def test_read_empty(self, parser):
        mapping = CpSwClusterToDiagEventMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readCpSwClusterToDiagEventMapping(element, mapping)
        assert mapping.getCpSoftwareClusterResourceRef() is None
        assert mapping.getDiagnosticEventRef() is None
