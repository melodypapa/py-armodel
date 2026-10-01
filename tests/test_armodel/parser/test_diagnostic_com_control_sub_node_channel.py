"""
Tests for reading the DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL element —
DiagnosticComControlSubNodeChannel, Table 4.67 (p.110, R23-11).

DiagnosticComControlSubNodeChannel (Base most-derived ARObject) carries three
0..1 attributes — subNodeChannel (ref, DEST COMMUNICATION-CLUSTER--SUBTYPES-ENUM),
subNodeNumber (PositiveInteger) and subNodePhysicalChannel (ref, DEST
ETHERNET-PHYSICAL-CHANNEL--SUBTYPES-ENUM) — XSD group
DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL, AUTOSAR_00052.xsd l.32759. Its aggregator
DiagnosticComControlClass.subNodeChannel (Table 4.66) is not modeled yet, so the
reusable readDiagnosticComControlSubNodeChannel helper is verified directly here
(Rule 0001.7); the aggregator will dispatch it when synced.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_com_control_sub_node_channel.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticComControlSubNodeChannel:
    """Tests for readDiagnosticComControlSubNodeChannel — own element field values (Table 4.67)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticComControlSubNodeChannel

        channel = DiagnosticComControlSubNodeChannel()
        element = _snip(inner, root_tag="DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL")
        parser.readDiagnosticComControlSubNodeChannel(element, channel)
        return channel

    def test_sub_node_channel_ref_read(self, parser):
        """Test that the SUB-NODE-CHANNEL-REF is read with its DEST attribute."""
        inner = '<SUB-NODE-CHANNEL-REF DEST="COMMUNICATION-CLUSTER">/System/Clusters/Cluster1</SUB-NODE-CHANNEL-REF>'
        channel = self._read(parser, inner)
        assert channel.getSubNodeChannel() is not None
        assert channel.getSubNodeChannel().getValue() == "/System/Clusters/Cluster1"
        assert channel.getSubNodeChannel().getDest() == "COMMUNICATION-CLUSTER"

    def test_sub_node_number_read(self, parser):
        """Test that the SUB-NODE-NUMBER is read as a PositiveInteger value."""
        inner = "<SUB-NODE-NUMBER>7</SUB-NODE-NUMBER>"
        channel = self._read(parser, inner)
        assert channel.getSubNodeNumber() is not None
        assert channel.getSubNodeNumber().getValue() == 7

    def test_sub_node_physical_channel_ref_read(self, parser):
        """Test that the SUB-NODE-PHYSICAL-CHANNEL-REF is read with its DEST attribute."""
        inner = '<SUB-NODE-PHYSICAL-CHANNEL-REF DEST="ETHERNET-PHYSICAL-CHANNEL">/System/EthernetClusters/Cluster1/Vlan2</SUB-NODE-PHYSICAL-CHANNEL-REF>'
        channel = self._read(parser, inner)
        assert channel.getSubNodePhysicalChannel() is not None
        assert channel.getSubNodePhysicalChannel().getValue() == "/System/EthernetClusters/Cluster1/Vlan2"
        assert channel.getSubNodePhysicalChannel().getDest() == "ETHERNET-PHYSICAL-CHANNEL"

    def test_empty_element_reads_nothing(self, parser):
        """Test that an empty element leaves all attributes None."""
        inner = ""
        channel = self._read(parser, inner)
        assert channel.getSubNodeChannel() is None
        assert channel.getSubNodeNumber() is None
        assert channel.getSubNodePhysicalChannel() is None
