"""Writer tests for BusMirrorChannelMapping (SystemTemplate TPS Table 6.325, p.697).

The expected XML uses the XSD-valid element order from the group
BUS-MIRROR-CHANNEL-MAPPING in ``autosar/R23-11/xsd/AUTOSAR_00052.xsd``:
MIRRORING-PROTOCOL, SOURCE-CHANNEL, TARGET-CHANNEL, TARGET-PDU-TRIGGERINGS.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannel, MirroringProtocolEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import BusMirrorChannelMapping
from armodel.writer.arxml_writer import ARXMLWriter


class _ConcreteMapping(BusMirrorChannelMapping):
    pass


def _populate(mapping):
    mapping.setMirroringProtocol(MirroringProtocolEnum().setValue(MirroringProtocolEnum.VERSION1))

    source_channel = BusMirrorChannel()
    source_channel.setChecksum(_checksum("1234"))
    mapping.setSourceChannel(source_channel)
    mapping.setTargetChannel(BusMirrorChannel())

    ref = RefType().setValue("/Fibex/PduTriggering")
    ref.setDest("PDU-TRIGGERING")
    mapping.addTargetPduTriggeringRef(ref)


def _checksum(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String

    checksum = String()
    checksum.setValue(value)
    return checksum


class TestBusMirrorChannelMappingWriter:
    def test_write_full_element_order_and_values(self):
        writer = ARXMLWriter()
        mapping = _ConcreteMapping(None, "Mapping")
        _populate(mapping)

        parent = ET.Element("PARENT")
        writer.writeBusMirrorChannelMapping(parent, mapping)

        tags = [element.tag for element in parent]
        assert tags.index("MIRRORING-PROTOCOL") < tags.index("SOURCE-CHANNEL")
        assert tags.index("SOURCE-CHANNEL") < tags.index("TARGET-CHANNEL")
        assert tags.index("TARGET-CHANNEL") < tags.index("TARGET-PDU-TRIGGERINGS")
        assert parent.find("MIRRORING-PROTOCOL").text == "VERSION-1"
        assert parent.find("SOURCE-CHANNEL").attrib["S"] == "1234"
        assert parent.find("TARGET-PDU-TRIGGERINGS/PDU-TRIGGERING-REF-CONDITIONAL/PDU-TRIGGERING-REF").text == "/Fibex/PduTriggering"
        assert parent.find("TARGET-PDU-TRIGGERINGS/PDU-TRIGGERING-REF-CONDITIONAL/PDU-TRIGGERING-REF").attrib["DEST"] == "PDU-TRIGGERING"

    def test_write_empty_wrappers_omitted(self):
        writer = ARXMLWriter()
        mapping = _ConcreteMapping(None, "Mapping")

        parent = ET.Element("PARENT")
        writer.writeBusMirrorChannelMapping(parent, mapping)

        assert parent.find("MIRRORING-PROTOCOL") is None
        assert parent.find("SOURCE-CHANNEL") is None
        assert parent.find("TARGET-CHANNEL") is None
        assert parent.find("TARGET-PDU-TRIGGERINGS") is None
