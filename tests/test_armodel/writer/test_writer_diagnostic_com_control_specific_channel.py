"""
Tests for writing DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL elements —
DiagnosticComControlSpecificChannel, Table 4.65 (p.109, R23-11).

DiagnosticComControlSpecificChannel (Base most-derived ARObject) carries three
0..1 attributes — specificChannel (ref, DEST COMMUNICATION-CLUSTER--SUBTYPES-ENUM),
specificPhysicalChannel (ref, DEST ETHERNET-PHYSICAL-CHANNEL--SUBTYPES-ENUM) and
subnetNumber (PositiveInteger) — XSD group DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL,
AUTOSAR_00052.xsd l.32704. Its aggregator DiagnosticComControlClass.specificChannel
(Table 4.66) is not modeled yet, so the reusable writeDiagnosticComControlSpecificChannel
helper is verified directly here (Rule 0001.7); the aggregator will dispatch it when synced.
The writer reads the model via the get* getters in XSD element order.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_com_control_specific_channel.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticComControlSpecificChannel
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
    nrc_value = PositiveInteger()
    nrc_value.setValue(value)
    return nrc_value


class TestWriteDiagnosticComControlSpecificChannel:
    """Tests for writeDiagnosticComControlSpecificChannel — own element field values (Table 4.65)."""

    def _write(self, channel: DiagnosticComControlSpecificChannel) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticComControlSpecificChannel(parent, channel)
        return parent.find("DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL")

    def test_write_specific_channel_ref(self):
        """Test that the SPECIFIC-CHANNEL-REF is emitted with its DEST attribute."""
        channel = DiagnosticComControlSpecificChannel()
        channel.setSpecificChannel(_ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster1"))

        child = self._write(channel)
        assert child is not None
        ref = child.find("SPECIFIC-CHANNEL-REF")
        assert ref is not None
        assert ref.text == "/System/Clusters/Cluster1"
        assert ref.get("DEST") == "COMMUNICATION-CLUSTER"

    def test_write_specific_physical_channel_ref(self):
        """Test that the SPECIFIC-PHYSICAL-CHANNEL-REF is emitted with its DEST attribute."""
        channel = DiagnosticComControlSpecificChannel()
        channel.setSpecificPhysicalChannel(_ref("ETHERNET-PHYSICAL-CHANNEL", "/System/EthernetClusters/Cluster1/Vlan1"))

        child = self._write(channel)
        ref = child.find("SPECIFIC-PHYSICAL-CHANNEL-REF")
        assert ref is not None
        assert ref.text == "/System/EthernetClusters/Cluster1/Vlan1"
        assert ref.get("DEST") == "ETHERNET-PHYSICAL-CHANNEL"

    def test_write_subnet_number(self):
        """Test that the SUBNET-NUMBER is emitted as the PositiveInteger value."""
        channel = DiagnosticComControlSpecificChannel()
        channel.setSubnetNumber(_positive_integer("3"))

        child = self._write(channel)
        number = child.find("SUBNET-NUMBER")
        assert number is not None
        assert number.text == "3"

    def test_element_order_matches_xsd(self):
        """Test that the emitted children follow the XSD element order (SPECIFIC-CHANNEL-REF, SPECIFIC-PHYSICAL-CHANNEL-REF, SUBNET-NUMBER)."""
        channel = DiagnosticComControlSpecificChannel()
        channel.setSpecificChannel(_ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster1"))
        channel.setSpecificPhysicalChannel(_ref("ETHERNET-PHYSICAL-CHANNEL", "/System/EthernetClusters/Cluster1/Vlan1"))
        channel.setSubnetNumber(_positive_integer("3"))

        child = self._write(channel)
        assert [c.tag for c in child] == ["SPECIFIC-CHANNEL-REF", "SPECIFIC-PHYSICAL-CHANNEL-REF", "SUBNET-NUMBER"]

    def test_empty_channel_omits_all_children(self):
        """Test that an empty channel emits no children."""
        channel = DiagnosticComControlSpecificChannel()

        child = self._write(channel)
        assert child is not None
        assert len(list(child)) == 0
