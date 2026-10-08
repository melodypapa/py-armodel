"""Reader tests for BusMirrorCanIdRangeMapping (SystemTemplate TPS Table 6.329, p.702).

readBusMirrorCanIdRangeMapping populates the model via setDestinationBaseId /
setSourceCanIdCode / setSourceCanIdMask per the XSD group
BUS-MIRROR-CAN-ID-RANGE-MAPPING (AUTOSAR_00052.xsd).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BusMirrorCanIdRangeMapping
from tests.test_armodel.parser._helpers import _snip


class TestBusMirrorCanIdRangeMappingReader:
    def test_read_full_field_values(self, parser):
        mapping = BusMirrorCanIdRangeMapping()
        element = _snip(
            """
            <DESTINATION-BASE-ID>16</DESTINATION-BASE-ID>
            <SOURCE-CAN-ID-CODE>40</SOURCE-CAN-ID-CODE>
            <SOURCE-CAN-ID-MASK>7</SOURCE-CAN-ID-MASK>
            """,
            root_tag="BUS-MIRROR-CAN-ID-RANGE-MAPPING",
        )

        parser.readBusMirrorCanIdRangeMapping(element, mapping)

        assert mapping.getDestinationBaseId().getValue() == 16
        assert mapping.getSourceCanIdCode().getValue() == 40
        assert mapping.getSourceCanIdMask().getValue() == 7

    def test_read_empty(self, parser):
        mapping = BusMirrorCanIdRangeMapping()
        element = _snip("", root_tag="BUS-MIRROR-CAN-ID-RANGE-MAPPING")

        parser.readBusMirrorCanIdRangeMapping(element, mapping)

        assert mapping.getDestinationBaseId() is None
        assert mapping.getSourceCanIdCode() is None
        assert mapping.getSourceCanIdMask() is None
