"""Writer tests for BusMirrorCanIdToCanIdMapping (SystemTemplate TPS Table 6.330, p.702).

The expected XML uses the XSD-valid element order from the group
BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING in ``autosar/R23-11/xsd/AUTOSAR_00052.xsd``:
REMAPPED-CAN-ID, then SOUCE-CAN-ID-REF (spec typo spelling kept on the wire).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BusMirrorCanIdToCanIdMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.writer.arxml_writer import ARXMLWriter


class TestBusMirrorCanIdToCanIdMappingWriter:
    def test_write_full_element_order_and_values(self):
        writer = ARXMLWriter()
        mapping = BusMirrorCanIdToCanIdMapping()
        mapping.setRemappedCanId(PositiveInteger().setValue("512"))
        ref = RefType().setValue("/Can/FrameTriggering")
        ref.setDest("CAN-FRAME-TRIGGERING")
        mapping.setSouceCanIdRef(ref)

        parent = ET.Element("PARENT")
        writer.writeBusMirrorCanIdToCanIdMapping(parent, mapping)

        child = parent[0]
        assert child.tag == "BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING"
        tags = [element.tag for element in child]
        assert tags == ["REMAPPED-CAN-ID", "SOUCE-CAN-ID-REF"]
        assert child.find("REMAPPED-CAN-ID").text == "512"
        assert child.find("SOUCE-CAN-ID-REF").text == "/Can/FrameTriggering"
        assert child.find("SOUCE-CAN-ID-REF").attrib["DEST"] == "CAN-FRAME-TRIGGERING"

    def test_write_empty_omits_all_elements(self):
        writer = ARXMLWriter()
        mapping = BusMirrorCanIdToCanIdMapping()

        parent = ET.Element("PARENT")
        writer.writeBusMirrorCanIdToCanIdMapping(parent, mapping)

        child = parent[0]
        assert child.find("REMAPPED-CAN-ID") is None
        assert child.find("SOUCE-CAN-ID-REF") is None
