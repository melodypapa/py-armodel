"""
Writer/reader round-trip tests for MacSecParticipantSet (Table 3.121, p.174).

MacSecParticipantSet is an ARElement consumed by ARPackage.element (serialized as
MAC-SEC-PARTICIPANT-SET). It carries the attributes ethernetCluster (0..1 ref,
ETHERNET-CLUSTER-REF) and mkaParticipant (* aggr, wrapper MKA-PARTICIPANTS holding
unbounded MAC-SEC-KAY-PARTICIPANT items per AUTOSAR_00052.xsd group
MAC-SEC-PARTICIPANT-SET).

Reader counterpart: tests/test_armodel/parser/test_mac_sec_participant_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecParticipantSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class MockPackage(MockParent):
    def getShortName(self):
        return "Pkg"


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    ref.setDest("ETHERNET-CLUSTER")
    return ref


def _new_participant_set(short_name="MPS1", with_participants=True):
    participant_set = MacSecParticipantSet(MockPackage(), short_name)
    participant_set.setEthernetClusterRef(_ref("/Clusters/EthernetCluster"))
    if with_participants:
        participant = participant_set.createMacSecKayParticipant("MKA1")
        ckn = RefType()
        ckn.setValue("/Keys/CknKey")
        ckn.setDest("CRYPTO-SERVICE-KEY")
        participant.setCknRef(ckn)
        sak = RefType()
        sak.setValue("/Keys/SakKey")
        sak.setDest("CRYPTO-SERVICE-KEY")
        participant.setSakRef(sak)
        participant_set.createMacSecKayParticipant("MKA2")
    return participant_set


class TestWriteMacSecParticipantSet:
    def test_write_all_fields(self, writer):
        participant_set = _new_participant_set()
        parent = ET.Element("ELEMENTS")
        writer.writeMacSecParticipantSet(parent, participant_set)

        node = parent.find("MAC-SEC-PARTICIPANT-SET")
        assert node is not None
        assert node.find("SHORT-NAME").text == "MPS1"
        assert [child.tag for child in node] == ["SHORT-NAME", "ETHERNET-CLUSTER-REF", "MKA-PARTICIPANTS"]
        cluster_ref = node.find("ETHERNET-CLUSTER-REF")
        assert cluster_ref.text == "/Clusters/EthernetCluster"
        assert cluster_ref.get("DEST") == "ETHERNET-CLUSTER"
        participants_wrapper = node.find("MKA-PARTICIPANTS")
        assert participants_wrapper is not None
        participant_nodes = participants_wrapper.findall("MAC-SEC-KAY-PARTICIPANT")
        assert len(participant_nodes) == 2
        assert participant_nodes[0].find("SHORT-NAME").text == "MKA1"
        assert participant_nodes[0].find("CKN-REF").text == "/Keys/CknKey"
        assert participant_nodes[0].find("SAK-REF").text == "/Keys/SakKey"
        assert participant_nodes[1].find("SHORT-NAME").text == "MKA2"

    def test_write_empty_omits_wrapper(self, writer):
        participant_set = _new_participant_set(with_participants=False)
        parent = ET.Element("ELEMENTS")
        writer.writeMacSecParticipantSet(parent, participant_set)

        node = parent.find("MAC-SEC-PARTICIPANT-SET")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME", "ETHERNET-CLUSTER-REF"]
        assert node.find("MKA-PARTICIPANTS") is None


class TestMacSecParticipantSetThroughArPackage:
    def test_ar_package_save_load_round_trip(self):
        """The full ARPackage ELEMENTS path: writeARPackageElement emits the set and the parser dispatch reads it back."""
        document = AUTOSAR.getInstance()
        document.new()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Sec")
        participant_set = pkg.createMacSecParticipantSet("ParticipantSet")
        participant_set.setEthernetClusterRef(_ref("/Clusters/EthernetCluster"))
        participant = participant_set.createMacSecKayParticipant("MKA1")
        ckn = RefType()
        ckn.setValue("/Keys/CknKey")
        ckn.setDest("CRYPTO-SERVICE-KEY")
        participant.setCknRef(ckn)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser(options={"warning": True}).load(file_path, reloaded)

            loaded_pkg = reloaded.getARPackages()[0]
            sets = [e for e in loaded_pkg.getReferrableElements() if isinstance(e, MacSecParticipantSet)]
            assert len(sets) == 1
            recovered = sets[0]
            assert recovered.getShortName() == "ParticipantSet"
            assert recovered.getEthernetClusterRef().getValue() == "/Clusters/EthernetCluster"
            participants = recovered.getMkaParticipants()
            assert len(participants) == 1
            assert participants[0].getShortName() == "MKA1"
            assert participants[0].getCknRef().getValue() == "/Keys/CknKey"
        finally:
            os.remove(file_path)

    def test_ar_package_save_load_empty_set(self):
        """An ARElement with an empty aggr list serializes no wrapper and re-parses to an empty list."""
        document = AUTOSAR.getInstance()
        document.new()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Sec")
        pkg.createMacSecParticipantSet("EmptyParticipantSet")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser(options={"warning": True}).load(file_path, reloaded)

            loaded_pkg = reloaded.getARPackages()[0]
            sets = [e for e in loaded_pkg.getReferrableElements() if isinstance(e, MacSecParticipantSet)]
            assert len(sets) == 1
            recovered = sets[0]
            assert recovered.getShortName() == "EmptyParticipantSet"
            assert recovered.getEthernetClusterRef() is None
            assert recovered.getMkaParticipants() == []
        finally:
            os.remove(file_path)


class TestMacSecParticipantSetRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        participant_set = _new_participant_set()

        parent = ET.Element("ELEMENTS")
        writer.writeMacSecParticipantSet(parent, participant_set)

        out_file = str(tmp_path / "mac_sec_participant_set.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = MacSecParticipantSet(MockParent(), "MPS1")
        parser.readMacSecParticipantSet(tree.getroot()[0][0], recovered)

        assert recovered.getShortName() == "MPS1"
        assert recovered.getEthernetClusterRef().getValue() == "/Clusters/EthernetCluster"
        participants = recovered.getMkaParticipants()
        assert len(participants) == 2
        assert participants[0].getShortName() == "MKA1"
        assert participants[0].getCknRef().getValue() == "/Keys/CknKey"
        assert participants[0].getSakRef().getValue() == "/Keys/SakKey"
        assert participants[1].getShortName() == "MKA2"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<MAC-SEC-PARTICIPANT-SET xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></MAC-SEC-PARTICIPANT-SET>" % NS)
        recovered = MacSecParticipantSet(MockParent(), "Empty")
        parser.readMacSecParticipantSet(element, recovered)

        assert recovered.getEthernetClusterRef() is None
        assert recovered.getMkaParticipants() == []
