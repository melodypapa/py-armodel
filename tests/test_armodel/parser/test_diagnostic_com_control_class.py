"""
Tests for reading the DIAGNOSTIC-COM-CONTROL-CLASS element —
DiagnosticComControlClass, Table 4.66 (p.109, R23-11).

DiagnosticComControlClass (Base most-derived DiagnosticServiceClass, concrete)
carries four 0..* members in XSD group DIAGNOSTIC-COM-CONTROL-CLASS
(AUTOSAR_00052.xsd l.32568 / complexType l.32642) element order:
ALL-CHANNELS-REFS (ALL-CHANNELS-REF, DEST COMMUNICATION-CLUSTER--SUBTYPES-ENUM),
ALL-PHYSICAL-CHANNELS (ALL-PHYSICAL-CHANNELS-REF, DEST
ETHERNET-PHYSICAL-CHANNEL--SUBTYPES-ENUM), SPECIFIC-CHANNELS
(DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL) and SUB-NODE-CHANNELS
(DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_com_control_class.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticComControlClass:
    """Tests for readDiagnosticComControlClass — own element field values (Table 4.66)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticComControlClass

        com_control_class = DiagnosticComControlClass(parent=MagicMock(), short_name="ComControlClass")
        element = _snip(inner, root_tag="DIAGNOSTIC-COM-CONTROL-CLASS")
        parser.readDiagnosticComControlClass(element, com_control_class)
        return com_control_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        com_control_class = self._read(parser, "<SHORT-NAME>ComControlClass</SHORT-NAME>")
        assert com_control_class.getShortName() == "ComControlClass"

    def test_read_all_channels_refs(self, parser):
        """Test that the ALL-CHANNELS-REFS wrapper is read with DEST attributes."""
        inner = (
            "<ALL-CHANNELS-REFS>"
            '<ALL-CHANNELS-REF DEST="COMMUNICATION-CLUSTER">/System/Clusters/Cluster1</ALL-CHANNELS-REF>'
            '<ALL-CHANNELS-REF DEST="COMMUNICATION-CLUSTER">/System/Clusters/Cluster2</ALL-CHANNELS-REF>'
            "</ALL-CHANNELS-REFS>"
        )
        com_control_class = self._read(parser, inner)
        channels = com_control_class.getAllChannels()
        assert len(channels) == 2
        assert channels[0].getValue() == "/System/Clusters/Cluster1"
        assert channels[0].getDest() == "COMMUNICATION-CLUSTER"
        assert channels[1].getValue() == "/System/Clusters/Cluster2"

    def test_read_all_physical_channels(self, parser):
        """Test that the ALL-PHYSICAL-CHANNELS wrapper is read with DEST attributes."""
        inner = "<ALL-PHYSICAL-CHANNELS>" '<ALL-PHYSICAL-CHANNELS-REF DEST="ETHERNET-PHYSICAL-CHANNEL">/System/EthernetClusters/Cluster1/Vlan1</ALL-PHYSICAL-CHANNELS-REF>' "</ALL-PHYSICAL-CHANNELS>"
        com_control_class = self._read(parser, inner)
        channels = com_control_class.getAllPhysicalChannels()
        assert len(channels) == 1
        assert channels[0].getValue() == "/System/EthernetClusters/Cluster1/Vlan1"
        assert channels[0].getDest() == "ETHERNET-PHYSICAL-CHANNEL"

    def test_read_specific_channels(self, parser):
        """Test that the SPECIFIC-CHANNELS wrapper is read into typed DiagnosticComControlSpecificChannel children."""
        inner = "<SPECIFIC-CHANNELS>" "<DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL>" "<SUBNET-NUMBER>3</SUBNET-NUMBER>" "</DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL>" "</SPECIFIC-CHANNELS>"
        com_control_class = self._read(parser, inner)
        channels = com_control_class.getSpecificChannels()
        assert len(channels) == 1
        assert channels[0].getSubnetNumber() is not None
        assert channels[0].getSubnetNumber().getValue() == 3

    def test_read_sub_node_channels(self, parser):
        """Test that the SUB-NODE-CHANNELS wrapper is read into typed DiagnosticComControlSubNodeChannel children."""
        inner = (
            "<SUB-NODE-CHANNELS>"
            "<DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL>"
            '<SUB-NODE-CHANNEL-REF DEST="COMMUNICATION-CLUSTER">/System/Clusters/Cluster1</SUB-NODE-CHANNEL-REF>'
            "<SUB-NODE-NUMBER>7</SUB-NODE-NUMBER>"
            "</DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL>"
            "</SUB-NODE-CHANNELS>"
        )
        com_control_class = self._read(parser, inner)
        channels = com_control_class.getSubNodeChannels()
        assert len(channels) == 1
        assert channels[0].getSubNodeChannel() is not None
        assert channels[0].getSubNodeChannel().getValue() == "/System/Clusters/Cluster1"
        assert channels[0].getSubNodeNumber().getValue() == 7

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all members empty."""
        com_control_class = self._read(parser, "")
        assert com_control_class.getShortName() == "ComControlClass"
        assert com_control_class.getAllChannels() == []
        assert com_control_class.getAllPhysicalChannels() == []
        assert com_control_class.getSpecificChannels() == []
        assert com_control_class.getSubNodeChannels() == []
