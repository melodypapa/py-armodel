"""Parser tests for DiagnosticServiceTable (Table 4.16, p.59).

XSD group DIAGNOSTIC-SERVICE-TABLE (AUTOSAR_00052.xsd l.44007) element order:
DIAGNOSTIC-CONNECTIONS, ECU-INSTANCE-REF, PROTOCOL-KIND, SERVICE-INSTANCE-REFS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-SERVICE-TABLE") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticServiceTable:
    def test_read_sets_all_fields(self, parser):
        table = DiagnosticServiceTable(AUTOSAR.getInstance(), "Dst")
        element = _snip(
            "<DIAGNOSTIC-CONNECTIONS>"
            "<DIAGNOSTIC-CONNECTION-REF-CONDITIONAL>"
            '<DIAGNOSTIC-CONNECTION-REF DEST="DIAGNOSTIC-CONNECTION">/Diag/Conns/Dc1</DIAGNOSTIC-CONNECTION-REF>'
            "</DIAGNOSTIC-CONNECTION-REF-CONDITIONAL>"
            "</DIAGNOSTIC-CONNECTIONS>"
            '<ECU-INSTANCE-REF DEST="ECU-INSTANCE">/Sys/EcuInst1</ECU-INSTANCE-REF>'
            "<PROTOCOL-KIND>UDS</PROTOCOL-KIND>"
            "<SERVICE-INSTANCE-REFS>"
            '<SERVICE-INSTANCE-REF DEST="DIAGNOSTIC-ECU-RESET">/Diag/Instances/Der1</SERVICE-INSTANCE-REF>'
            '<SERVICE-INSTANCE-REF DEST="DIAGNOSTIC-SESSION-CONTROL">/Diag/Instances/Dsc1</SERVICE-INSTANCE-REF>'
            "</SERVICE-INSTANCE-REFS>"
        )
        parser.readDiagnosticServiceTable(element, table)
        conns = table.getDiagnosticConnectionRefs()
        assert len(conns) == 1
        assert conns[0].getValue() == "/Diag/Conns/Dc1"
        assert conns[0].getDest() == "DIAGNOSTIC-CONNECTION"
        assert table.getEcuInstanceRef().getValue() == "/Sys/EcuInst1"
        assert table.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        assert table.getProtocolKind().getValue() == "UDS"
        instances = table.getServiceInstanceRefs()
        assert len(instances) == 2
        assert instances[0].getValue() == "/Diag/Instances/Der1"
        assert instances[0].getDest() == "DIAGNOSTIC-ECU-RESET"
        assert instances[1].getValue() == "/Diag/Instances/Dsc1"
        assert instances[1].getDest() == "DIAGNOSTIC-SESSION-CONTROL"

    def test_read_empty(self, parser):
        table = DiagnosticServiceTable(AUTOSAR.getInstance(), "Dst")
        element = _snip("")
        parser.readDiagnosticServiceTable(element, table)
        assert table.getDiagnosticConnectionRefs() == []
        assert table.getEcuInstanceRef() is None
        assert table.getProtocolKind() is None
        assert table.getServiceInstanceRefs() == []
