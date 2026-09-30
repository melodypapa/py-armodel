"""
Tests for reading the DIAGNOSTIC-PROTOCOL element — DiagnosticProtocol, Table 4.15 (p.58, R23-11).

DiagnosticProtocol (Base = ARElement) carries the DIAGNOSTIC-CONNECTIONS wrapper
list (DIAGNOSTIC-CONNECTION-REF-CONDITIONAL items), PRIORITY
(POSITIVE-INTEGER-VALUE-VARIATION-POINT), PROTOCOL-KIND (NMTOKEN-STRING),
SEND-RESP-PEND-ON-TRANS-TO-BOOT (BOOLEAN-VALUE-VARIATION-POINT) and the
SERVICE-TABLES wrapper (0..1 DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL) — XSD
group DIAGNOSTIC-PROTOCOL, AUTOSAR_00052.xsd l.41010.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_protocol.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticProtocol:
    """Tests for readDiagnosticProtocol — own element field values (Table 4.15)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticProtocol

        protocol = DiagnosticProtocol(parent=MagicMock(), short_name="Dp")
        element = _snip(inner, root_tag="DIAGNOSTIC-PROTOCOL")
        parser.readDiagnosticProtocol(element, protocol)
        return protocol

    def test_with_diagnostic_connection_refs(self, parser):
        """Test that DIAGNOSTIC-CONNECTIONS items are read through the REF-CONDITIONAL wrapper with DEST and value."""
        inner = (
            "<SHORT-NAME>Dp</SHORT-NAME>"
            "<DIAGNOSTIC-CONNECTIONS>"
            "<DIAGNOSTIC-CONNECTION-REF-CONDITIONAL>"
            '<DIAGNOSTIC-CONNECTION-REF DEST="DIAGNOSTIC-CONNECTION">/AUTOSAR/DiagnosticConnections/Conn</DIAGNOSTIC-CONNECTION-REF>'
            "</DIAGNOSTIC-CONNECTION-REF-CONDITIONAL>"
            "</DIAGNOSTIC-CONNECTIONS>"
        )
        protocol = self._read(parser, inner)
        assert protocol.getShortName() == "Dp"
        refs = protocol.getDiagnosticConnectionRefs()
        assert len(refs) == 1
        assert refs[0].getDest() == "DIAGNOSTIC-CONNECTION"
        assert refs[0].getValue() == "/AUTOSAR/DiagnosticConnections/Conn"

    def test_without_diagnostic_connections(self, parser):
        """Test that an absent DIAGNOSTIC-CONNECTIONS wrapper leaves diagnosticConnectionRefs empty."""
        protocol = self._read(parser, "<SHORT-NAME>Dp</SHORT-NAME>")
        assert protocol.getDiagnosticConnectionRefs() == []

    def test_with_priority(self, parser):
        """Test that PRIORITY is read through the POSITIVE-INTEGER-VALUE-VARIATION-POINT wrapper."""
        protocol = self._read(
            parser,
            "<SHORT-NAME>Dp</SHORT-NAME>" "<PRIORITY><POSITIVE-INTEGER-VALUE-VARIATION-POINT>5</POSITIVE-INTEGER-VALUE-VARIATION-POINT></PRIORITY>",
        )
        assert protocol.getPriority() is not None
        assert protocol.getPriority().getValue() == 5

    def test_without_priority(self, parser):
        """Test that an absent PRIORITY element leaves priority None."""
        protocol = self._read(parser, "<SHORT-NAME>Dp</SHORT-NAME>")
        assert protocol.getPriority() is None

    def test_with_protocol_kind(self, parser):
        """Test that PROTOCOL-KIND is read as a NameToken."""
        protocol = self._read(parser, "<SHORT-NAME>Dp</SHORT-NAME>" "<PROTOCOL-KIND>UDS</PROTOCOL-KIND>")
        assert protocol.getProtocolKind() is not None
        assert protocol.getProtocolKind().getValue() == "UDS"

    def test_with_send_resp_pend_on_trans_to_boot(self, parser):
        """Test that SEND-RESP-PEND-ON-TRANS-TO-BOOT is read through the BOOLEAN-VALUE-VARIATION-POINT wrapper."""
        protocol = self._read(
            parser,
            "<SHORT-NAME>Dp</SHORT-NAME>" "<SEND-RESP-PEND-ON-TRANS-TO-BOOT><BOOLEAN-VALUE-VARIATION-POINT>true</BOOLEAN-VALUE-VARIATION-POINT></SEND-RESP-PEND-ON-TRANS-TO-BOOT>",
        )
        assert protocol.getSendRespPendOnTransToBoot() is not None
        assert protocol.getSendRespPendOnTransToBoot().getValue() is True

    def test_with_service_table_ref(self, parser):
        """Test that the 0..1 SERVICE-TABLES wrapper is read through the REF-CONDITIONAL wrapper."""
        inner = (
            "<SHORT-NAME>Dp</SHORT-NAME>"
            "<SERVICE-TABLES>"
            "<DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL>"
            '<DIAGNOSTIC-SERVICE-TABLE-REF DEST="DIAGNOSTIC-SERVICE-TABLE">/AUTOSAR/DiagnosticServiceTables/Table</DIAGNOSTIC-SERVICE-TABLE-REF>'
            "</DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL>"
            "</SERVICE-TABLES>"
        )
        protocol = self._read(parser, inner)
        ref = protocol.getServiceTableRef()
        assert ref is not None
        assert ref.getDest() == "DIAGNOSTIC-SERVICE-TABLE"
        assert ref.getValue() == "/AUTOSAR/DiagnosticServiceTables/Table"

    def test_without_service_tables(self, parser):
        """Test that an absent SERVICE-TABLES wrapper leaves serviceTableRef None."""
        protocol = self._read(parser, "<SHORT-NAME>Dp</SHORT-NAME>")
        assert protocol.getServiceTableRef() is None
