"""Reader tests for BusMirrorCanIdToCanIdMapping (SystemTemplate TPS Table 6.330, p.702).

readBusMirrorCanIdToCanIdMapping populates the model via setRemappedCanId /
setSouceCanIdRef per the XSD group BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING
(AUTOSAR_00052.xsd) — note the XSD spelling SOUCE-CAN-ID-REF (spec typo kept).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BusMirrorCanIdToCanIdMapping
from tests.test_armodel.parser._helpers import _snip


class TestBusMirrorCanIdToCanIdMappingReader:
    def test_read_full_field_values(self, parser):
        mapping = BusMirrorCanIdToCanIdMapping()
        element = _snip(
            """
            <REMAPPED-CAN-ID>512</REMAPPED-CAN-ID>
            <SOUCE-CAN-ID-REF DEST="CAN-FRAME-TRIGGERING">/Can/FrameTriggering</SOUCE-CAN-ID-REF>
            """,
            root_tag="BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING",
        )

        parser.readBusMirrorCanIdToCanIdMapping(element, mapping)

        assert mapping.getRemappedCanId().getValue() == 512
        assert mapping.getSouceCanIdRef().getValue() == "/Can/FrameTriggering"
        assert mapping.getSouceCanIdRef().getDest() == "CAN-FRAME-TRIGGERING"

    def test_read_empty(self, parser):
        mapping = BusMirrorCanIdToCanIdMapping()
        element = _snip("", root_tag="BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING")

        parser.readBusMirrorCanIdToCanIdMapping(element, mapping)

        assert mapping.getRemappedCanId() is None
        assert mapping.getSouceCanIdRef() is None
