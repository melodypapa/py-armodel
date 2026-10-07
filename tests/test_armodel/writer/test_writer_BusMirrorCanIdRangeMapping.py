"""Writer tests for BusMirrorCanIdRangeMapping (SystemTemplate TPS Table 6.329, p.702).

The expected XML uses the XSD-valid element order from the group
BUS-MIRROR-CAN-ID-RANGE-MAPPING in ``autosar/R23-11/xsd/AUTOSAR_00052.xsd``:
DESTINATION-BASE-ID, SOURCE-CAN-ID-CODE, SOURCE-CAN-ID-MASK.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BusMirrorCanIdRangeMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.writer.arxml_writer import ARXMLWriter


class TestBusMirrorCanIdRangeMappingWriter:
    def test_write_full_element_order_and_values(self):
        writer = ARXMLWriter()
        mapping = BusMirrorCanIdRangeMapping()
        mapping.setDestinationBaseId(PositiveInteger().setValue("16"))
        mapping.setSourceCanIdCode(PositiveInteger().setValue("40"))
        mapping.setSourceCanIdMask(PositiveInteger().setValue("7"))

        parent = ET.Element("PARENT")
        writer.writeBusMirrorCanIdRangeMapping(parent, mapping)

        child = parent[0]
        assert child.tag == "BUS-MIRROR-CAN-ID-RANGE-MAPPING"
        tags = [element.tag for element in child]
        assert tags == ["DESTINATION-BASE-ID", "SOURCE-CAN-ID-CODE", "SOURCE-CAN-ID-MASK"]
        assert child.find("DESTINATION-BASE-ID").text == "16"
        assert child.find("SOURCE-CAN-ID-CODE").text == "40"
        assert child.find("SOURCE-CAN-ID-MASK").text == "7"

    def test_write_empty_omits_all_elements(self):
        writer = ARXMLWriter()
        mapping = BusMirrorCanIdRangeMapping()

        parent = ET.Element("PARENT")
        writer.writeBusMirrorCanIdRangeMapping(parent, mapping)

        child = parent[0]
        assert child.find("DESTINATION-BASE-ID") is None
        assert child.find("SOURCE-CAN-ID-CODE") is None
        assert child.find("SOURCE-CAN-ID-MASK") is None
