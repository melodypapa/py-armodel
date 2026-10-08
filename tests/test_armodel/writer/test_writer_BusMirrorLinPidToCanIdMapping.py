"""Writer tests for BusMirrorLinPidToCanIdMapping (SystemTemplate TPS Table 6.331, p.702).

The expected XML uses the XSD-valid element order from the group
BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING in ``autosar/R23-11/xsd/AUTOSAR_00052.xsd``:
REMAPPED-CAN-ID, then SOURCE-LIN-PID-REF.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BusMirrorLinPidToCanIdMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.writer.arxml_writer import ARXMLWriter


class TestBusMirrorLinPidToCanIdMappingWriter:
    def test_write_full_element_order_and_values(self):
        writer = ARXMLWriter()
        mapping = BusMirrorLinPidToCanIdMapping()
        mapping.setRemappedCanId(PositiveInteger().setValue("768"))
        ref = RefType().setValue("/Lin/FrameTriggering")
        ref.setDest("LIN-FRAME-TRIGGERING")
        mapping.setSourceLinPidRef(ref)

        parent = ET.Element("PARENT")
        writer.writeBusMirrorLinPidToCanIdMapping(parent, mapping)

        child = parent[0]
        assert child.tag == "BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING"
        tags = [element.tag for element in child]
        assert tags == ["REMAPPED-CAN-ID", "SOURCE-LIN-PID-REF"]
        assert child.find("REMAPPED-CAN-ID").text == "768"
        assert child.find("SOURCE-LIN-PID-REF").text == "/Lin/FrameTriggering"
        assert child.find("SOURCE-LIN-PID-REF").attrib["DEST"] == "LIN-FRAME-TRIGGERING"

    def test_write_empty_omits_all_elements(self):
        writer = ARXMLWriter()
        mapping = BusMirrorLinPidToCanIdMapping()

        parent = ET.Element("PARENT")
        writer.writeBusMirrorLinPidToCanIdMapping(parent, mapping)

        child = parent[0]
        assert child.find("REMAPPED-CAN-ID") is None
        assert child.find("SOURCE-LIN-PID-REF") is None
