"""Writer tests for BusMirrorChannel (SystemTemplate TPS Table 6.327, p.698).

The expected XML uses the XSD-valid element order from the group
BUS-MIRROR-CHANNEL in ``autosar/R23-11/xsd/AUTOSAR_00052.xsd``:
BUS-MIRROR-NETWORK-ID, CHANNELS.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannel
from armodel.writer.arxml_writer import ARXMLWriter


class TestBusMirrorChannelWriter:
    def test_write_full_element_order_and_values(self):
        writer = ARXMLWriter()
        channel = BusMirrorChannel()
        channel.setBusMirrorNetworkId(PositiveInteger().setValue("512"))
        ref = RefType().setValue("/BusMirror/CanPhysicalChannel")
        ref.setDest("CAN-PHYSICAL-CHANNEL")
        channel.setChannelRef(ref)

        parent = ET.Element("PARENT")
        writer.setBusMirrorChannel(parent, "SOURCE-CHANNEL", channel)

        source_channel = parent.find("SOURCE-CHANNEL")
        assert source_channel is not None
        tags = [element.tag for element in source_channel]
        assert tags.index("BUS-MIRROR-NETWORK-ID") < tags.index("CHANNELS")
        assert source_channel.find("BUS-MIRROR-NETWORK-ID").text == "512"
        ref_element = source_channel.find("CHANNELS/PHYSICAL-CHANNEL-REF-CONDITIONAL/PHYSICAL-CHANNEL-REF")
        assert ref_element.text == "/BusMirror/CanPhysicalChannel"
        assert ref_element.attrib["DEST"] == "CAN-PHYSICAL-CHANNEL"

    def test_write_none_channel_omitted(self):
        writer = ARXMLWriter()

        parent = ET.Element("PARENT")
        writer.setBusMirrorChannel(parent, "SOURCE-CHANNEL", None)

        assert parent.find("SOURCE-CHANNEL") is None

    def test_write_channels_wrapper_omitted_when_ref_unset(self):
        writer = ARXMLWriter()
        channel = BusMirrorChannel()
        channel.setBusMirrorNetworkId(PositiveInteger().setValue("1"))

        parent = ET.Element("PARENT")
        writer.setBusMirrorChannel(parent, "TARGET-CHANNEL", channel)

        target_channel = parent.find("TARGET-CHANNEL")
        assert target_channel is not None
        assert target_channel.find("BUS-MIRROR-NETWORK-ID").text == "1"
        assert target_channel.find("CHANNELS") is None
