"""Writer/round-trip tests for BusMirrorChannelMappingCan (SystemTemplate TPS Table 6.328, p.701).

The expected XML uses the XSD-valid element order from the complexType
BUS-MIRROR-CHANNEL-MAPPING-CAN in ``autosar/R23-11/xsd/AUTOSAR_00052.xsd``:
the base group BUS-MIRROR-CHANNEL-MAPPING content, then the three wrapper
lists and the two scalars. The class is aggregated by ARPackage.element, so
the save/load round-trip goes through the ARPackage dispatch on both sides.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    BusMirrorCanIdRangeMapping,
    BusMirrorCanIdToCanIdMapping,
    BusMirrorChannel,
    BusMirrorLinPidToCanIdMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import MirroringProtocolEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import BusMirrorChannelMappingCan
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

    range_mapping = BusMirrorCanIdRangeMapping()
    range_mapping.setDestinationBaseId(PositiveInteger().setValue("16"))
    range_mapping.setSourceCanIdCode(PositiveInteger().setValue("40"))
    range_mapping.setSourceCanIdMask(PositiveInteger().setValue("7"))
    mapping.addCanIdRangeMapping(range_mapping)

    id_mapping = BusMirrorCanIdToCanIdMapping()
    id_mapping.setRemappedCanId(PositiveInteger().setValue("512"))
    souce_ref = RefType().setValue("/Can/FrameTriggering")
    souce_ref.setDest("CAN-FRAME-TRIGGERING")
    id_mapping.setSouceCanIdRef(souce_ref)
    mapping.addCanIdToCanIdMapping(id_mapping)

    lin_mapping = BusMirrorLinPidToCanIdMapping()
    lin_mapping.setRemappedCanId(PositiveInteger().setValue("768"))
    lin_ref = RefType().setValue("/Lin/FrameTriggering")
    lin_ref.setDest("LIN-FRAME-TRIGGERING")
    lin_mapping.setSourceLinPidRef(lin_ref)
    mapping.addLinPidToCanIdMapping(lin_mapping)

    mapping.setMirrorSourceLinToCanRangeBaseId(PositiveInteger().setValue("512"))
    mapping.setMirrorStatusCanId(PositiveInteger().setValue("2048"))


class TestBusMirrorChannelMappingCanWriter:
    def test_write_full_element_order_and_values(self):
        writer = ARXMLWriter()
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(BusMirrorChannelMappingCan(package, "CanMapping"))
        mapping = package.getReferrableElement("CanMapping", BusMirrorChannelMappingCan)
        _populate(mapping)

        parent = ET.Element("PARENT")
        writer.writeARPackageElement(parent, mapping)

        child = parent[0]
        assert child.tag == "BUS-MIRROR-CHANNEL-MAPPING-CAN"
        tags = [element.tag for element in child]
        assert tags.index("TARGET-PDU-TRIGGERINGS") < tags.index("CAN-ID-RANGE-MAPPINGS")
        assert tags.index("CAN-ID-RANGE-MAPPINGS") < tags.index("CAN-ID-TO-CAN-ID-MAPPINGS")
        assert tags.index("CAN-ID-TO-CAN-ID-MAPPINGS") < tags.index("LIN-PID-TO-CAN-ID-MAPPINGS")
        assert tags.index("LIN-PID-TO-CAN-ID-MAPPINGS") < tags.index("MIRROR-SOURCE-LIN-TO-CAN-RANGE-BASE-ID")
        assert tags.index("MIRROR-SOURCE-LIN-TO-CAN-RANGE-BASE-ID") < tags.index("MIRROR-STATUS-CAN-ID")
        assert child.find("CAN-ID-RANGE-MAPPINGS/BUS-MIRROR-CAN-ID-RANGE-MAPPING/DESTINATION-BASE-ID").text == "16"
        assert child.find("CAN-ID-TO-CAN-ID-MAPPINGS/BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING/SOUCE-CAN-ID-REF").text == "/Can/FrameTriggering"
        assert child.find("LIN-PID-TO-CAN-ID-MAPPINGS/BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING/SOURCE-LIN-PID-REF").text == "/Lin/FrameTriggering"
        assert child.find("MIRROR-SOURCE-LIN-TO-CAN-RANGE-BASE-ID").text == "512"
        assert child.find("MIRROR-STATUS-CAN-ID").text == "2048"

    def test_write_empty_wrappers_omitted(self):
        writer = ARXMLWriter()
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(BusMirrorChannelMappingCan(package, "CanMapping"))

        parent = ET.Element("PARENT")
        for ar_element in package.getReferrableElements():
            writer.writeARPackageElement(parent, ar_element)

        child = parent[0]
        assert child.find("CAN-ID-RANGE-MAPPINGS") is None
        assert child.find("CAN-ID-TO-CAN-ID-MAPPINGS") is None
        assert child.find("LIN-PID-TO-CAN-ID-MAPPINGS") is None
        assert child.find("MIRROR-SOURCE-LIN-TO-CAN-RANGE-BASE-ID") is None
        assert child.find("MIRROR-STATUS-CAN-ID") is None


class TestBusMirrorChannelMappingCanRoundTrip:
    def _round_trip(self, writer, parser, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        package = document.createARPackage("Pkg")
        mapping = BusMirrorChannelMappingCan(package, "CanMapping")
        package.addReferrableElement(mapping)
        _populate(mapping)
        checksum = String()
        checksum.setValue("abcd")
        mapping.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T00:00:00Z")
        mapping.setTimestamp(timestamp)

        out_file = str(tmp_path / "bus_mirror_channel_mapping_can.arxml")
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
        mappings = [element for element in reloaded_pkg.getReferrableElements() if isinstance(element, BusMirrorChannelMappingCan)]
        assert len(mappings) == 1
        mapping = mappings[0]
        assert mapping.getShortName() == "CanMapping"
        assert mapping.getChecksum().getValue() == "abcd"
        assert mapping.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        assert mapping.getMirroringProtocol().getValue() == "VERSION-1"
        assert mapping.getSourceChannel() is not None
        assert mapping.getTargetChannel() is not None
        assert len(mapping.getTargetPduTriggeringRefs()) == 1
        range_mappings = mapping.getCanIdRangeMappings()
        assert len(range_mappings) == 1
        assert range_mappings[0].getDestinationBaseId().getValue() == 16
        assert range_mappings[0].getSourceCanIdCode().getValue() == 40
        assert range_mappings[0].getSourceCanIdMask().getValue() == 7

        id_mappings = mapping.getCanIdToCanIdMappings()
        assert len(id_mappings) == 1
        assert id_mappings[0].getRemappedCanId().getValue() == 512
        assert id_mappings[0].getSouceCanIdRef().getValue() == "/Can/FrameTriggering"
        assert id_mappings[0].getSouceCanIdRef().getDest() == "CAN-FRAME-TRIGGERING"

        lin_mappings = mapping.getLinPidToCanIdMappings()
        assert len(lin_mappings) == 1
        assert lin_mappings[0].getRemappedCanId().getValue() == 768
        assert lin_mappings[0].getSourceLinPidRef().getValue() == "/Lin/FrameTriggering"

        assert mapping.getMirrorSourceLinToCanRangeBaseId().getValue() == 512
        assert mapping.getMirrorStatusCanId().getValue() == 2048
