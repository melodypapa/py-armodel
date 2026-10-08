"""
Reader tests for MacSecParticipantSet (CP_TPS_SystemTemplate Table 3.121, p.174, R23-11).

Covers the IDENTIFIABLE base level (SHORT-NAME/UUID round-trip plus the S/T attributes
carried by readIdentifiable's chain down to readARObjectAttributes), the optional
ETHERNET-CLUSTER-REF and the MKA-PARTICIPANTS wrapper (holding unbounded
MAC-SEC-KAY-PARTICIPANT items per AUTOSAR_00052.xsd group MAC-SEC-PARTICIPANT-SET),
the partial and absent-wrapper cases and the ARPackage ELEMENTS dispatch (aggregated by
ARPackage.element).

Round-trip counterpart: tests/test_armodel/writer/test_mac_sec_participant_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as AutosarDocument
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecParticipantSet
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-PARTICIPANT-SET xmlns='{NS}'>{inner}</MAC-SEC-PARTICIPANT-SET>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-PARTICIPANT-SET xmlns='{NS}' {attrs}>{inner}</MAC-SEC-PARTICIPANT-SET>")


def _full_inner() -> str:
    return (
        "<SHORT-NAME>MPS1</SHORT-NAME>"
        "<ETHERNET-CLUSTER-REF DEST='ETHERNET-CLUSTER'>/Clusters/EthernetCluster</ETHERNET-CLUSTER-REF>"
        "<MKA-PARTICIPANTS>"
        "<MAC-SEC-KAY-PARTICIPANT>"
        "<SHORT-NAME>MKA1</SHORT-NAME>"
        "<CKN-REF DEST='CRYPTO-SERVICE-KEY'>/Keys/CknKey</CKN-REF>"
        "<SAK-REF DEST='CRYPTO-SERVICE-KEY'>/Keys/SakKey</SAK-REF>"
        "</MAC-SEC-KAY-PARTICIPANT>"
        "<MAC-SEC-KAY-PARTICIPANT>"
        "<SHORT-NAME>MKA2</SHORT-NAME>"
        "<CKN-REF DEST='CRYPTO-SERVICE-KEY'>/Keys/CknKey2</CKN-REF>"
        "</MAC-SEC-KAY-PARTICIPANT>"
        "</MKA-PARTICIPANTS>"
    )


class TestReadMacSecParticipantSet:
    def test_read_identifiable_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs(
            "UUID='5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab2' S='chk-2' T='2009-07-23T13:38:00Z'",
            "<SHORT-NAME>MPS1</SHORT-NAME>",
        )
        participant_set = MacSecParticipantSet(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecParticipantSet(element, participant_set)

        assert participant_set.getUuid().getValue() == "5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab2"
        assert participant_set.getChecksum().getValue() == "chk-2"
        assert participant_set.getTimestamp().getValue() == "2009-07-23T13:38:00Z"
        assert participant_set.getEthernetClusterRef() is None
        assert participant_set.getMkaParticipants() == []

    def test_read_ref_and_participants(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        participant_set = MacSecParticipantSet(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecParticipantSet(element, participant_set)

        assert participant_set.getEthernetClusterRef().getValue() == "/Clusters/EthernetCluster"
        participants = participant_set.getMkaParticipants()
        assert len(participants) == 2
        assert participants[0].getShortName() == "MKA1"
        assert participants[0].getCknRef().getValue() == "/Keys/CknKey"
        assert participants[0].getSakRef().getValue() == "/Keys/SakKey"
        assert participants[1].getShortName() == "MKA2"
        assert participants[1].getCknRef().getValue() == "/Keys/CknKey2"

    def test_read_partial(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>MPS1</SHORT-NAME><ETHERNET-CLUSTER-REF DEST='ETHERNET-CLUSTER'>/Clusters/Only</ETHERNET-CLUSTER-REF>")
        participant_set = MacSecParticipantSet(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecParticipantSet(element, participant_set)

        assert participant_set.getEthernetClusterRef().getValue() == "/Clusters/Only"
        assert participant_set.getMkaParticipants() == []

    def test_read_empty_wrapper(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>MPS1</SHORT-NAME>" "<MKA-PARTICIPANTS></MKA-PARTICIPANTS>")
        participant_set = MacSecParticipantSet(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecParticipantSet(element, participant_set)

        assert participant_set.getEthernetClusterRef() is None
        assert participant_set.getMkaParticipants() == []

    def test_load_via_ar_package(self):
        """The ARPackage ELEMENTS dispatch reads a MAC-SEC-PARTICIPANT-SET element."""
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <MAC-SEC-PARTICIPANT-SET>
                    <SHORT-NAME>ParticipantSet</SHORT-NAME>
                    <ETHERNET-CLUSTER-REF DEST="ETHERNET-CLUSTER">/Clusters/EthernetCluster</ETHERNET-CLUSTER-REF>
                    <MKA-PARTICIPANTS>
                        <MAC-SEC-KAY-PARTICIPANT>
                            <SHORT-NAME>MKA1</SHORT-NAME>
                            <CKN-REF DEST='CRYPTO-SERVICE-KEY'>/Keys/CknKey</CKN-REF>
                        </MAC-SEC-KAY-PARTICIPANT>
                    </MKA-PARTICIPANTS>
                </MAC-SEC-PARTICIPANT-SET>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            document = AUTOSAR.getInstance()
            document.clear()
            parser = ARXMLParser(options={"warning": True})
            parser.load(file_path, document)

            pkg = document.getARPackages()[0]
            sets = [e for e in pkg.getReferrableElements() if isinstance(e, MacSecParticipantSet)]
            assert len(sets) == 1
            participant_set = sets[0]
            assert participant_set.getShortName() == "ParticipantSet"
            assert participant_set.getEthernetClusterRef().getValue() == "/Clusters/EthernetCluster"
            participants = participant_set.getMkaParticipants()
            assert len(participants) == 1
            assert participants[0].getShortName() == "MKA1"
            assert participants[0].getCknRef().getValue() == "/Keys/CknKey"
        finally:
            os.remove(file_path)
