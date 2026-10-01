"""
Tests for writing DIAGNOSTIC-COM-CONTROL-CLASS elements —
DiagnosticComControlClass, Table 4.66 (p.109, R23-11).

DiagnosticComControlClass (Base most-derived DiagnosticServiceClass, concrete)
carries four 0..* members in XSD group DIAGNOSTIC-COM-CONTROL-CLASS
(AUTOSAR_00052.xsd l.32568 / complexType l.32642) element order:
ALL-CHANNELS-REFS (ALL-CHANNELS-REF), ALL-PHYSICAL-CHANNELS
(ALL-PHYSICAL-CHANNELS-REF), SPECIFIC-CHANNELS
(DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL) and SUB-NODE-CHANNELS
(DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL). The dispatch entry is
writeARPackageElement → writeDiagnosticComControlClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_com_control_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticComControlClass
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    DiagnosticComControlSpecificChannel,
    DiagnosticComControlSubNodeChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
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


class TestWriteDiagnosticComControlClass:
    """Tests for writeDiagnosticComControlClass — own element field values (Table 4.66)."""

    def _write(self, com_control_class: DiagnosticComControlClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticComControlClass(parent, com_control_class)
        return parent.find("DIAGNOSTIC-COM-CONTROL-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticComControlClass without members emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        package.createDiagnosticComControlClass("ComControlClass1")

        child = self._write(package.getElement("ComControlClass1", DiagnosticComControlClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "ComControlClass1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_all_channels_refs(self):
        """Test that the ALL-CHANNELS-REFS wrapper is emitted with DEST attributes."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        com_control_class = package.createDiagnosticComControlClass("ComControlClass1")
        com_control_class.addAllChannel(_ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster1"))
        com_control_class.addAllChannel(_ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster2"))

        child = self._write(com_control_class)
        wrapper = child.find("ALL-CHANNELS-REFS")
        assert wrapper is not None
        refs = wrapper.findall("ALL-CHANNELS-REF")
        assert len(refs) == 2
        assert refs[0].text == "/System/Clusters/Cluster1"
        assert refs[0].get("DEST") == "COMMUNICATION-CLUSTER"
        assert refs[1].text == "/System/Clusters/Cluster2"

    def test_write_all_physical_channels(self):
        """Test that the ALL-PHYSICAL-CHANNELS wrapper is emitted with DEST attributes."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        com_control_class = package.createDiagnosticComControlClass("ComControlClass1")
        com_control_class.addAllPhysicalChannel(_ref("ETHERNET-PHYSICAL-CHANNEL", "/System/EthernetClusters/Cluster1/Vlan1"))

        child = self._write(com_control_class)
        wrapper = child.find("ALL-PHYSICAL-CHANNELS")
        assert wrapper is not None
        ref = wrapper.find("ALL-PHYSICAL-CHANNELS-REF")
        assert ref is not None
        assert ref.text == "/System/EthernetClusters/Cluster1/Vlan1"
        assert ref.get("DEST") == "ETHERNET-PHYSICAL-CHANNEL"

    def test_write_specific_channels(self):
        """Test that the SPECIFIC-CHANNELS wrapper is emitted with the typed channel children."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        com_control_class = package.createDiagnosticComControlClass("ComControlClass1")
        channel = DiagnosticComControlSpecificChannel()
        channel.setSubnetNumber(PositiveInteger().setValue("3"))
        com_control_class.addSpecificChannel(channel)

        child = self._write(com_control_class)
        wrapper = child.find("SPECIFIC-CHANNELS")
        assert wrapper is not None
        channel_element = wrapper.find("DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL")
        assert channel_element is not None
        assert channel_element.find("SUBNET-NUMBER").text == "3"

    def test_write_sub_node_channels(self):
        """Test that the SUB-NODE-CHANNELS wrapper is emitted with the typed channel children."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        com_control_class = package.createDiagnosticComControlClass("ComControlClass1")
        channel = DiagnosticComControlSubNodeChannel()
        channel.setSubNodeChannel(_ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster1"))
        channel.setSubNodeNumber(PositiveInteger().setValue("7"))
        com_control_class.addSubNodeChannel(channel)

        child = self._write(com_control_class)
        wrapper = child.find("SUB-NODE-CHANNELS")
        assert wrapper is not None
        channel_element = wrapper.find("DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL")
        assert channel_element is not None
        assert channel_element.find("SUB-NODE-CHANNEL-REF").text == "/System/Clusters/Cluster1"
        assert channel_element.find("SUB-NODE-NUMBER").text == "7"

    def test_element_order_matches_xsd(self):
        """Test that the emitted children follow the XSD element order (ALL-CHANNELS-REFS, ALL-PHYSICAL-CHANNELS, SPECIFIC-CHANNELS, SUB-NODE-CHANNELS)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        com_control_class = package.createDiagnosticComControlClass("ComControlClass1")
        com_control_class.addAllChannel(_ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster1"))
        com_control_class.addAllPhysicalChannel(_ref("ETHERNET-PHYSICAL-CHANNEL", "/System/EthernetClusters/Cluster1/Vlan1"))
        com_control_class.addSpecificChannel(DiagnosticComControlSpecificChannel())
        com_control_class.addSubNodeChannel(DiagnosticComControlSubNodeChannel())

        child = self._write(com_control_class)
        assert [c.tag for c in child] == ["SHORT-NAME", "ALL-CHANNELS-REFS", "ALL-PHYSICAL-CHANNELS", "SPECIFIC-CHANNELS", "SUB-NODE-CHANNELS"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticComControlClass to a DIAGNOSTIC-COM-CONTROL-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticCommunicationControls")
        package.createDiagnosticComControlClass("ComControlClass1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("ComControlClass1", DiagnosticComControlClass))

        child = parent.find("DIAGNOSTIC-COM-CONTROL-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ComControlClass1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        import os
        import tempfile

        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticCommunicationControls")
        com_control_class = package.createDiagnosticComControlClass("ComControlClass1")
        com_control_class.addAllChannel(_ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster1"))
        com_control_class.addAllPhysicalChannel(_ref("ETHERNET-PHYSICAL-CHANNEL", "/System/EthernetClusters/Cluster1/Vlan1"))
        specific_channel = DiagnosticComControlSpecificChannel()
        specific_channel.setSubnetNumber(PositiveInteger().setValue("3"))
        com_control_class.addSpecificChannel(specific_channel)
        sub_node_channel = DiagnosticComControlSubNodeChannel()
        sub_node_channel.setSubNodeChannel(_ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster2"))
        sub_node_channel.setSubNodeNumber(PositiveInteger().setValue("7"))
        com_control_class.addSubNodeChannel(sub_node_channel)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            com_control_class_2 = package_2.getElement("ComControlClass1", DiagnosticComControlClass)
            assert com_control_class_2 is not None
            assert com_control_class_2.getShortName() == "ComControlClass1"
            channels = com_control_class_2.getAllChannels()
            assert len(channels) == 1
            assert channels[0].getValue() == "/System/Clusters/Cluster1"
            assert channels[0].getDest() == "COMMUNICATION-CLUSTER"
            physical_channels = com_control_class_2.getAllPhysicalChannels()
            assert len(physical_channels) == 1
            assert physical_channels[0].getValue() == "/System/EthernetClusters/Cluster1/Vlan1"
            assert physical_channels[0].getDest() == "ETHERNET-PHYSICAL-CHANNEL"
            specific_channels = com_control_class_2.getSpecificChannels()
            assert len(specific_channels) == 1
            assert specific_channels[0].getSubnetNumber().getValue() == 3
            sub_node_channels = com_control_class_2.getSubNodeChannels()
            assert len(sub_node_channels) == 1
            assert sub_node_channels[0].getSubNodeChannel().getValue() == "/System/Clusters/Cluster2"
            assert sub_node_channels[0].getSubNodeNumber().getValue() == 7
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
