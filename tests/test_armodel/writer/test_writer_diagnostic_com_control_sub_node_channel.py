"""
Tests for writing DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL elements —
DiagnosticComControlSubNodeChannel, Table 4.67 (p.110, R23-11).

DiagnosticComControlSubNodeChannel (Base most-derived ARObject) carries three
0..1 attributes — subNodeChannel (ref, DEST COMMUNICATION-CLUSTER--SUBTYPES-ENUM),
subNodeNumber (PositiveInteger) and subNodePhysicalChannel (ref, DEST
ETHERNET-PHYSICAL-CHANNEL--SUBTYPES-ENUM) — XSD group
DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL, AUTOSAR_00052.xsd l.32759. Its aggregator
DiagnosticComControlClass.subNodeChannel (Table 4.66) is not modeled yet, so the
reusable writeDiagnosticComControlSubNodeChannel helper is verified directly here
(Rule 0001.7); the aggregator will dispatch it when synced.
The writer reads the model via the get* getters in XSD element order.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_com_control_sub_node_channel.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticComControlSubNodeChannel
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _positive_integer(value: str) -> PositiveInteger:
    number = PositiveInteger()
    number.setValue(value)
    return number


class TestWriteDiagnosticComControlSubNodeChannel:
    """Tests for writeDiagnosticComControlSubNodeChannel — own element field values (Table 4.67)."""

    def _write(self, channel: DiagnosticComControlSubNodeChannel) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticComControlSubNodeChannel(parent, channel)
        return parent.find("DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL")

    def test_write_sub_node_channel_ref(self):
        """Test that the SUB-NODE-CHANNEL-REF is emitted with its DEST attribute."""
        channel = DiagnosticComControlSubNodeChannel()
        channel.setSubNodeChannel(_ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster1"))

        child = self._write(channel)
        assert child is not None
        ref = child.find("SUB-NODE-CHANNEL-REF")
        assert ref is not None
        assert ref.text == "/System/Clusters/Cluster1"
        assert ref.get("DEST") == "COMMUNICATION-CLUSTER"

    def test_write_sub_node_number(self):
        """Test that the SUB-NODE-NUMBER is emitted as the PositiveInteger value."""
        channel = DiagnosticComControlSubNodeChannel()
        channel.setSubNodeNumber(_positive_integer("7"))

        child = self._write(channel)
        assert child is not None
        number = child.find("SUB-NODE-NUMBER")
        assert number is not None
        assert number.text == "7"

    def test_write_sub_node_physical_channel_ref(self):
        """Test that the SUB-NODE-PHYSICAL-CHANNEL-REF is emitted with its DEST attribute."""
        channel = DiagnosticComControlSubNodeChannel()
        channel.setSubNodePhysicalChannel(_ref("ETHERNET-PHYSICAL-CHANNEL", "/System/EthernetClusters/Cluster1/Vlan2"))

        child = self._write(channel)
        assert child is not None
        ref = child.find("SUB-NODE-PHYSICAL-CHANNEL-REF")
        assert ref is not None
        assert ref.text == "/System/EthernetClusters/Cluster1/Vlan2"
        assert ref.get("DEST") == "ETHERNET-PHYSICAL-CHANNEL"

    def test_element_order_matches_xsd(self):
        """Test that the emitted children follow the XSD element order (SUB-NODE-CHANNEL-REF, SUB-NODE-NUMBER, SUB-NODE-PHYSICAL-CHANNEL-REF)."""
        channel = DiagnosticComControlSubNodeChannel()
        channel.setSubNodeChannel(_ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster1"))
        channel.setSubNodeNumber(_positive_integer("7"))
        channel.setSubNodePhysicalChannel(_ref("ETHERNET-PHYSICAL-CHANNEL", "/System/EthernetClusters/Cluster1/Vlan2"))

        child = self._write(channel)
        assert [c.tag for c in child] == ["SUB-NODE-CHANNEL-REF", "SUB-NODE-NUMBER", "SUB-NODE-PHYSICAL-CHANNEL-REF"]

    def test_empty_channel_omits_all_children(self):
        """Test that an empty channel emits no children."""
        channel = DiagnosticComControlSubNodeChannel()

        child = self._write(channel)
        assert child is not None
        assert len(list(child)) == 0
