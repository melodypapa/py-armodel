"""Parser tests for CpSwClusterResourceToDiagFunctionIdMapping (Table 5.49, p.275).

XSD group CP-SW-CLUSTER-RESOURCE-TO-DIAG-FUNCTION-ID-MAPPING element order (AUTOSAR_00052.xsd): CP-SOFTWARE-CLUSTER-RESOURCE-REF, FUNCTION-IDENTIFIER-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSwClusterResourceToDiagFunctionIdMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "CP-SW-CLUSTER-RESOURCE-TO-DIAG-FUNCTION-ID-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadCpSwClusterResourceToDiagFunctionIdMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = CpSwClusterResourceToDiagFunctionIdMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<CP-SOFTWARE-CLUSTER-RESOURCE-REF DEST='DEST'>/AUTOSAR/CpSoftwareClusterResource1</CP-SOFTWARE-CLUSTER-RESOURCE-REF><FUNCTION-IDENTIFIER-REF DEST='DEST'>/AUTOSAR/FunctionIdentifier1</FUNCTION-IDENTIFIER-REF>"
        )
        parser.readCpSwClusterResourceToDiagFunctionIdMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getCpSoftwareClusterResourceRef() is not None
        assert mapping.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"
        assert mapping.getFunctionIdentifierRef() is not None
        assert mapping.getFunctionIdentifierRef().getValue() == "/AUTOSAR/FunctionIdentifier1"

    def test_read_empty(self, parser):
        mapping = CpSwClusterResourceToDiagFunctionIdMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readCpSwClusterResourceToDiagFunctionIdMapping(element, mapping)
        assert mapping.getCpSoftwareClusterResourceRef() is None
        assert mapping.getFunctionIdentifierRef() is None
