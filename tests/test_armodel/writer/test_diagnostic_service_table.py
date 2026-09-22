"""Writer round-trip tests for DiagnosticServiceTable (Table 4.16, p.59).

Child order per XSD complexType DIAGNOSTIC-SERVICE-TABLE (AUTOSAR_00052.xsd
l.44072): SHORT-NAME (inherited), DIAGNOSTIC-CONNECTIONS, ECU-INSTANCE-REF,
PROTOCOL-KIND, SERVICE-INSTANCE-REFS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _new_table():
    pkg = AUTOSAR.getInstance().createARPackage("DiagPkg")
    table = pkg.createDiagnosticServiceTable("Dst")
    table.addDiagnosticConnectionRef(_ref("DIAGNOSTIC-CONNECTION", "/Diag/Conns/Dc1"))
    table.setEcuInstanceRef(_ref("ECU-INSTANCE", "/Sys/EcuInst1"))
    table.setProtocolKind(NameToken().setValue("UDS"))
    table.addServiceInstanceRef(_ref("DIAGNOSTIC-ECU-RESET", "/Diag/Instances/Der1"))
    table.addServiceInstanceRef(_ref("DIAGNOSTIC-SESSION-CONTROL", "/Diag/Instances/Dsc1"))
    return table


class TestWriteDiagnosticServiceTable:
    def test_write_all_fields_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticServiceTable(parent, _new_table())
        node = parent.find("DIAGNOSTIC-SERVICE-TABLE")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["SHORT-NAME", "DIAGNOSTIC-CONNECTIONS", "ECU-INSTANCE-REF", "PROTOCOL-KIND", "SERVICE-INSTANCE-REFS"]
        conn_ref = node.find("DIAGNOSTIC-CONNECTIONS/DIAGNOSTIC-CONNECTION-REF-CONDITIONAL/DIAGNOSTIC-CONNECTION-REF")
        assert conn_ref.text == "/Diag/Conns/Dc1"
        assert conn_ref.attrib["DEST"] == "DIAGNOSTIC-CONNECTION"
        ecu_ref = node.find("ECU-INSTANCE-REF")
        assert ecu_ref.text == "/Sys/EcuInst1"
        assert ecu_ref.attrib["DEST"] == "ECU-INSTANCE"
        assert node.find("PROTOCOL-KIND").text == "UDS"
        instance_refs = node.findall("SERVICE-INSTANCE-REFS/SERVICE-INSTANCE-REF")
        assert len(instance_refs) == 2
        assert instance_refs[0].text == "/Diag/Instances/Der1"
        assert instance_refs[0].attrib["DEST"] == "DIAGNOSTIC-ECU-RESET"
        assert instance_refs[1].text == "/Diag/Instances/Dsc1"
        assert instance_refs[1].attrib["DEST"] == "DIAGNOSTIC-SESSION-CONTROL"

    def test_write_empty_fields_omits_optional_tags(self):
        pkg = AUTOSAR.getInstance().createARPackage("DiagPkg")
        table = pkg.createDiagnosticServiceTable("Dst")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticServiceTable(parent, table)
        node = parent.find("DIAGNOSTIC-SERVICE-TABLE")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticServiceTable(parent, _new_table())
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = DiagnosticServiceTable(AUTOSAR.getInstance(), "Dst2")
        ARXMLParser().readDiagnosticServiceTable(root[0], parsed)
        assert parsed.getDiagnosticConnectionRefs()[0].getValue() == "/Diag/Conns/Dc1"
        assert parsed.getDiagnosticConnectionRefs()[0].getDest() == "DIAGNOSTIC-CONNECTION"
        assert parsed.getEcuInstanceRef().getValue() == "/Sys/EcuInst1"
        assert parsed.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        assert parsed.getProtocolKind().getValue() == "UDS"
        assert parsed.getServiceInstanceRefs()[0].getValue() == "/Diag/Instances/Der1"
        assert parsed.getServiceInstanceRefs()[0].getDest() == "DIAGNOSTIC-ECU-RESET"
        assert parsed.getServiceInstanceRefs()[1].getValue() == "/Diag/Instances/Dsc1"
        assert parsed.getServiceInstanceRefs()[1].getDest() == "DIAGNOSTIC-SESSION-CONTROL"
