"""
Tests for reading the DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL element —
DiagnosticComControlSpecificChannel, Table 4.65 (p.109, R23-11).

DiagnosticComControlSpecificChannel (Base most-derived ARObject) carries three
0..1 attributes — specificChannel (ref, DEST COMMUNICATION-CLUSTER--SUBTYPES-ENUM),
specificPhysicalChannel (ref, DEST ETHERNET-PHYSICAL-CHANNEL--SUBTYPES-ENUM) and
subnetNumber (PositiveInteger) — XSD group DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL,
AUTOSAR_00052.xsd l.32704. Its aggregator DiagnosticComControlClass.specificChannel
(Table 4.66) is not modeled yet, so the reusable readDiagnosticComControlSpecificChannel
helper is verified directly here (Rule 0001.7); the aggregator will dispatch it when synced.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_com_control_specific_channel.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticComControlSpecificChannel:
    """Tests for readDiagnosticComControlSpecificChannel — own element field values (Table 4.65)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticComControlSpecificChannel

        channel = DiagnosticComControlSpecificChannel()
        element = _snip(inner, root_tag="DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL")
        parser.readDiagnosticComControlSpecificChannel(element, channel)
        return channel

    def test_specific_channel_ref_read(self, parser):
        """Test that the SPECIFIC-CHANNEL-REF is read with its DEST attribute."""
        inner = '<SPECIFIC-CHANNEL-REF DEST="COMMUNICATION-CLUSTER">/System/Clusters/Cluster1</SPECIFIC-CHANNEL-REF>'
        channel = self._read(parser, inner)
        assert channel.getSpecificChannel() is not None
        assert channel.getSpecificChannel().getValue() == "/System/Clusters/Cluster1"
        assert channel.getSpecificChannel().getDest() == "COMMUNICATION-CLUSTER"

    def test_specific_physical_channel_ref_read(self, parser):
        """Test that the SPECIFIC-PHYSICAL-CHANNEL-REF is read with its DEST attribute."""
        inner = '<SPECIFIC-PHYSICAL-CHANNEL-REF DEST="ETHERNET-PHYSICAL-CHANNEL">/System/EthernetClusters/Cluster1/Vlan1</SPECIFIC-PHYSICAL-CHANNEL-REF>'
        channel = self._read(parser, inner)
        assert channel.getSpecificPhysicalChannel() is not None
        assert channel.getSpecificPhysicalChannel().getValue() == "/System/EthernetClusters/Cluster1/Vlan1"
        assert channel.getSpecificPhysicalChannel().getDest() == "ETHERNET-PHYSICAL-CHANNEL"

    def test_subnet_number_read(self, parser):
        """Test that the SUBNET-NUMBER is read as a PositiveInteger value."""
        inner = "<SUBNET-NUMBER>3</SUBNET-NUMBER>"
        channel = self._read(parser, inner)
        assert channel.getSubnetNumber() is not None
        assert channel.getSubnetNumber().getValue() == 3

    def test_empty_element_reads_nothing(self, parser):
        """Test that an empty element leaves all attributes None."""
        inner = ""
        channel = self._read(parser, inner)
        assert channel.getSpecificChannel() is None
        assert channel.getSpecificPhysicalChannel() is None
        assert channel.getSubnetNumber() is None
