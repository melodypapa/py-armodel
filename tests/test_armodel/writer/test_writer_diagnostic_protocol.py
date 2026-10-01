"""
Tests for writing DIAGNOSTIC-PROTOCOL elements — DiagnosticProtocol, Table 4.15 (p.58, R23-11).

DiagnosticProtocol (Base = ARElement) carries the DIAGNOSTIC-CONNECTIONS wrapper
list (DIAGNOSTIC-CONNECTION-REF-CONDITIONAL items), PRIORITY
(POSITIVE-INTEGER-VALUE-VARIATION-POINT), PROTOCOL-KIND (NMTOKEN-STRING),
SEND-RESP-PEND-ON-TRANS-TO-BOOT (BOOLEAN-VALUE-VARIATION-POINT) and the
SERVICE-TABLES wrapper (0..1 DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL) — XSD
group DIAGNOSTIC-PROTOCOL, AUTOSAR_00052.xsd l.41010. The writer reads the model
via the get* getters; the dispatch entry is writeARPackageElement →
writeDiagnosticProtocol.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_protocol.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticProtocol
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, NameToken, PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteDiagnosticProtocol:
    """Tests for writeDiagnosticProtocol — own element field values (Table 4.15)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that DIAGNOSTIC-CONNECTIONS, PRIORITY, PROTOCOL-KIND, SEND-RESP-PEND-ON-TRANS-TO-BOOT and SERVICE-TABLES are emitted with field values in XSD order."""
        protocol = DiagnosticProtocol(parent=AUTOSAR.getInstance(), short_name="Dp")
        protocol.addDiagnosticConnectionRef(_ref("DIAGNOSTIC-CONNECTION", "/AUTOSAR/DiagnosticConnections/Conn"))
        priority = PositiveInteger()
        priority.setValue("5")
        protocol.setPriority(priority)
        protocol_kind = NameToken()
        protocol_kind.setValue("UDS")
        protocol.setProtocolKind(protocol_kind)
        send_resp_pend = Boolean()
        send_resp_pend.setValue(True)
        protocol.setSendRespPendOnTransToBoot(send_resp_pend)
        protocol.setServiceTableRef(_ref("DIAGNOSTIC-SERVICE-TABLE", "/AUTOSAR/DiagnosticServiceTables/Table"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticProtocol(parent, protocol)

        child = parent.find("DIAGNOSTIC-PROTOCOL")
        assert child is not None
        connection_ref = child.find("DIAGNOSTIC-CONNECTIONS/DIAGNOSTIC-CONNECTION-REF-CONDITIONAL/DIAGNOSTIC-CONNECTION-REF")
        assert connection_ref.attrib["DEST"] == "DIAGNOSTIC-CONNECTION"
        assert connection_ref.text == "/AUTOSAR/DiagnosticConnections/Conn"
        assert child.find("PRIORITY/POSITIVE-INTEGER-VALUE-VARIATION-POINT").text == "5"
        assert child.find("PROTOCOL-KIND").text == "UDS"
        assert child.find("SEND-RESP-PEND-ON-TRANS-TO-BOOT/BOOLEAN-VALUE-VARIATION-POINT").text == "true"
        table_ref = child.find("SERVICE-TABLES/DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL/DIAGNOSTIC-SERVICE-TABLE-REF")
        assert table_ref.attrib["DEST"] == "DIAGNOSTIC-SERVICE-TABLE"
        assert table_ref.text == "/AUTOSAR/DiagnosticServiceTables/Table"
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["DIAGNOSTIC-CONNECTIONS", "PRIORITY", "PROTOCOL-KIND", "SEND-RESP-PEND-ON-TRANS-TO-BOOT", "SERVICE-TABLES"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset fields and an empty connectionRefs list emit no elements."""
        protocol = DiagnosticProtocol(parent=AUTOSAR.getInstance(), short_name="Dp")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticProtocol(parent, protocol)

        child = parent.find("DIAGNOSTIC-PROTOCOL")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("DIAGNOSTIC-CONNECTIONS") is None
        assert child.find("PRIORITY") is None
        assert child.find("PROTOCOL-KIND") is None
        assert child.find("SEND-RESP-PEND-ON-TRANS-TO-BOOT") is None
        assert child.find("SERVICE-TABLES") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticProtocol to a DIAGNOSTIC-PROTOCOL element."""
        package = AUTOSAR.getInstance().createARPackage("Protocols")
        protocol = package.createDiagnosticProtocol("Dp")
        protocol_kind = NameToken()
        protocol_kind.setValue("UDS")
        protocol.setProtocolKind(protocol_kind)

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, protocol)

        child = parent.find("DIAGNOSTIC-PROTOCOL")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Dp"
        assert child.find("PROTOCOL-KIND").text == "UDS"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Protocols")
        protocol = package.createDiagnosticProtocol("Dp")
        protocol.addDiagnosticConnectionRef(_ref("DIAGNOSTIC-CONNECTION", "/AUTOSAR/DiagnosticConnections/Conn"))
        priority = PositiveInteger()
        priority.setValue("5")
        protocol.setPriority(priority)
        protocol_kind = NameToken()
        protocol_kind.setValue("UDS")
        protocol.setProtocolKind(protocol_kind)
        send_resp_pend = Boolean()
        send_resp_pend.setValue(False)
        protocol.setSendRespPendOnTransToBoot(send_resp_pend)
        protocol.setServiceTableRef(_ref("DIAGNOSTIC-SERVICE-TABLE", "/AUTOSAR/DiagnosticServiceTables/Table"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            protocol_2 = package_2.getElement("Dp", DiagnosticProtocol)
            assert protocol_2 is not None
            refs = protocol_2.getDiagnosticConnectionRefs()
            assert len(refs) == 1
            assert refs[0].getDest() == "DIAGNOSTIC-CONNECTION"
            assert refs[0].getValue() == "/AUTOSAR/DiagnosticConnections/Conn"
            assert protocol_2.getPriority() is not None
            assert protocol_2.getPriority().getValue() == 5
            assert protocol_2.getProtocolKind() is not None
            assert protocol_2.getProtocolKind().getValue() == "UDS"
            assert protocol_2.getSendRespPendOnTransToBoot() is not None
            assert protocol_2.getSendRespPendOnTransToBoot().getValue() is False
            assert protocol_2.getServiceTableRef() is not None
            assert protocol_2.getServiceTableRef().getValue() == "/AUTOSAR/DiagnosticServiceTables/Table"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticProtocol without field values round-trips with all fields empty."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Protocols")
        package.createDiagnosticProtocol("Dp")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            protocol_2 = package_2.getElement("Dp", DiagnosticProtocol)
            assert protocol_2 is not None
            assert protocol_2.getDiagnosticConnectionRefs() == []
            assert protocol_2.getPriority() is None
            assert protocol_2.getProtocolKind() is None
            assert protocol_2.getSendRespPendOnTransToBoot() is None
            assert protocol_2.getServiceTableRef() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
