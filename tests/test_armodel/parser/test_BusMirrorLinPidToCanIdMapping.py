"""Reader tests for BusMirrorLinPidToCanIdMapping (SystemTemplate TPS Table 6.331, p.702).

readBusMirrorLinPidToCanIdMapping populates the model via setRemappedCanId /
setSourceLinPidRef per the XSD group BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING
(AUTOSAR_00052.xsd).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BusMirrorLinPidToCanIdMapping
from tests.test_armodel.parser._helpers import _snip


class TestBusMirrorLinPidToCanIdMappingReader:
    def test_read_full_field_values(self, parser):
        mapping = BusMirrorLinPidToCanIdMapping()
        element = _snip(
            """
            <REMAPPED-CAN-ID>768</REMAPPED-CAN-ID>
            <SOURCE-LIN-PID-REF DEST="LIN-FRAME-TRIGGERING">/Lin/FrameTriggering</SOURCE-LIN-PID-REF>
            """,
            root_tag="BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING",
        )

        parser.readBusMirrorLinPidToCanIdMapping(element, mapping)

        assert mapping.getRemappedCanId().getValue() == 768
        assert mapping.getSourceLinPidRef().getValue() == "/Lin/FrameTriggering"
        assert mapping.getSourceLinPidRef().getDest() == "LIN-FRAME-TRIGGERING"

    def test_read_empty(self, parser):
        mapping = BusMirrorLinPidToCanIdMapping()
        element = _snip("", root_tag="BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING")

        parser.readBusMirrorLinPidToCanIdMapping(element, mapping)

        assert mapping.getRemappedCanId() is None
        assert mapping.getSourceLinPidRef() is None
