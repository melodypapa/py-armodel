"""Parser tests for CpSwClusterToDiagRoutineSubfunctionMapping (Table 5.48, p.274).

XSD group CP-SW-CLUSTER-TO-DIAG-ROUTINE-SUBFUNCTION-MAPPING element order (AUTOSAR_00052.xsd): CP-SOFTWARE-CLUSTER-RESOURCE-REF, ROUTINE-SUBFUNCTION-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSwClusterToDiagRoutineSubfunctionMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "CP-SW-CLUSTER-TO-DIAG-ROUTINE-SUBFUNCTION-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadCpSwClusterToDiagRoutineSubfunctionMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = CpSwClusterToDiagRoutineSubfunctionMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<CP-SOFTWARE-CLUSTER-RESOURCE-REF DEST='DEST'>/AUTOSAR/CpSoftwareClusterResource1</CP-SOFTWARE-CLUSTER-RESOURCE-REF><ROUTINE-SUBFUNCTION-REF DEST='DEST'>/AUTOSAR/RoutineSubfunction1</ROUTINE-SUBFUNCTION-REF>"
        )
        parser.readCpSwClusterToDiagRoutineSubfunctionMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getCpSoftwareClusterResourceRef() is not None
        assert mapping.getCpSoftwareClusterResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResource1"
        assert mapping.getRoutineSubfunctionRef() is not None
        assert mapping.getRoutineSubfunctionRef().getValue() == "/AUTOSAR/RoutineSubfunction1"

    def test_read_empty(self, parser):
        mapping = CpSwClusterToDiagRoutineSubfunctionMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readCpSwClusterToDiagRoutineSubfunctionMapping(element, mapping)
        assert mapping.getCpSoftwareClusterResourceRef() is None
        assert mapping.getRoutineSubfunctionRef() is None
