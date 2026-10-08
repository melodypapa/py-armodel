"""Writer/round-trip tests for BusMirrorChannelMappingIp (SystemTemplate TPS Table 6.333, p.706).

The expected XML uses the XSD-valid element order from the complexType
BUS-MIRROR-CHANNEL-MAPPING-IP in ``autosar/R23-11/xsd/AUTOSAR_00052.xsd``:
the base group BUS-MIRROR-CHANNEL-MAPPING content, then TRANSMISSION-DEADLINE.
The class is aggregated by ARPackage.element, so the save/load round-trip goes
through the ARPackage dispatch on both sides.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannel, MirroringProtocolEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import BusMirrorChannelMappingIp
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _populate(mapping):
    mapping.setMirroringProtocol(MirroringProtocolEnum().setValue(MirroringProtocolEnum.VERSION1))
    mapping.setSourceChannel(BusMirrorChannel())
    mapping.setTargetChannel(BusMirrorChannel())
    ref = RefType().setValue("/Fibex/PduTriggering")
    ref.setDest("PDU-TRIGGERING")
    mapping.addTargetPduTriggeringRef(ref)
    mapping.setTransmissionDeadline(TimeValue().setValue("0.5"))


def _checksum(value="abcd"):
    checksum = String()
    checksum.setValue(value)
    return checksum


def _timestamp(value="2024-01-01T00:00:00Z"):
    timestamp = DateTime()
    timestamp.setValue(value)
    return timestamp


class TestBusMirrorChannelMappingIpWriter:
    def test_write_full_element_order_and_values(self):
        writer = ARXMLWriter()
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(BusMirrorChannelMappingIp(package, "IpMapping"))
        mapping = package.getReferrableElement("IpMapping", BusMirrorChannelMappingIp)
        _populate(mapping)

        parent = ET.Element("PARENT")
        writer.writeARPackageElement(parent, mapping)

        child = parent[0]
        assert child.tag == "BUS-MIRROR-CHANNEL-MAPPING-IP"
        tags = [element.tag for element in child]
        assert tags.index("TARGET-PDU-TRIGGERINGS") < tags.index("TRANSMISSION-DEADLINE")
        assert child.find("MIRRORING-PROTOCOL").text == "VERSION-1"
        assert child.find("TRANSMISSION-DEADLINE").text == "0.5"

    def test_write_empty_wrappers_omitted(self):
        writer = ARXMLWriter()
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(BusMirrorChannelMappingIp(package, "IpMapping"))

        parent = ET.Element("PARENT")
        for ar_element in package.getReferrableElements():
            writer.writeARPackageElement(parent, ar_element)

        child = parent[0]
        assert child.find("MIRRORING-PROTOCOL") is None
        assert child.find("SOURCE-CHANNEL") is None
        assert child.find("TARGET-CHANNEL") is None
        assert child.find("TARGET-PDU-TRIGGERINGS") is None
        assert child.find("TRANSMISSION-DEADLINE") is None


class TestBusMirrorChannelMappingIpRoundTrip:
    def _round_trip(self, writer, parser, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        package = document.createARPackage("Pkg")
        mapping = BusMirrorChannelMappingIp(package, "IpMapping")
        package.addReferrableElement(mapping)
        _populate(mapping)
        mapping.setChecksum(_checksum())
        mapping.setTimestamp(_timestamp())

        out_file = str(tmp_path / "bus_mirror_channel_mapping_ip.arxml")
        writer.save(out_file, document)

        recovered = AUTOSAR.getInstance()
        recovered.clear()
        recovered.setARRelease("R23-11")
        parser.load(out_file, recovered)
        return recovered

    def test_round_trip_preserves_field_values(self, tmp_path):
        writer = ARXMLWriter()
        parser = ARXMLParser()
        recovered = self._round_trip(writer, parser, tmp_path)

        reloaded_pkg = recovered.getARPackages()[0]
        mappings = [element for element in reloaded_pkg.getReferrableElements() if isinstance(element, BusMirrorChannelMappingIp)]
        assert len(mappings) == 1
        mapping = mappings[0]
        assert mapping.getShortName() == "IpMapping"
        assert mapping.getChecksum().getValue() == "abcd"
        assert mapping.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        assert mapping.getMirroringProtocol().getValue() == "VERSION-1"
        assert mapping.getSourceChannel() is not None
        assert mapping.getTargetChannel() is not None
        assert len(mapping.getTargetPduTriggeringRefs()) == 1
        assert mapping.getTargetPduTriggeringRefs()[0].getValue() == "/Fibex/PduTriggering"
        assert mapping.getTransmissionDeadline().getValue() == 0.5
