"""Parser tests for CanCommunicationController (Table 3.11, p.63).

The class has no own attribute rows (Table 3.11 renders the header only): its
own XSD group CAN-COMMUNICATION-CONTROLLER (AUTOSAR_00052.xsd line 14454)
carries only the atpVariation wrapper CAN-COMMUNICATION-CONTROLLER-VARIANTS
(sequenceOffset 10000) wrapping CAN-COMMUNICATION-CONTROLLER-CONDITIONAL, and
the complexType (line 14476) places the IDENTIFIABLE groups (SHORT-NAME, ...)
before that wrapper. Coverage targets the readCanCommunicationController entry
helper: readIdentifiable at the top element, then the base
readAbstractCanCommunicationController helper called once on the CONDITIONAL
element (Rule 0001.7).
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanCommunicationController,
    CanControllerConfiguration,
    CanControllerConfigurationRequirements,
)
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _read_into(inner: str, attrs: str = "") -> CanCommunicationController:
    controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
    ARXMLParser().readCanCommunicationController(_snip(inner, attrs=attrs), controller)
    return controller


class TestReadCanCommunicationController:
    def test_reads_uuid_and_configuration_with_values(self, parser):
        controller = _read_into(
            "<SHORT-NAME>can_ctrl</SHORT-NAME>"
            "<CAN-COMMUNICATION-CONTROLLER-VARIANTS>"
            "<CAN-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>"
            "<CAN-CONTROLLER-ATTRIBUTES>"
            "<CAN-CONTROLLER-CONFIGURATION>"
            "<PROP-SEG>4</PROP-SEG>"
            "<SYNC-JUMP-WIDTH>1</SYNC-JUMP-WIDTH>"
            "<TIME-SEG-1>13</TIME-SEG-1>"
            "<TIME-SEG-2>2</TIME-SEG-2>"
            "</CAN-CONTROLLER-CONFIGURATION>"
            "</CAN-CONTROLLER-ATTRIBUTES>"
            "</CAN-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "</CAN-COMMUNICATION-CONTROLLER-VARIANTS>",
            attrs=' UUID="test-uuid-311"',
        )
        assert controller.getUuid().getValue() == "test-uuid-311"
        assert controller.getWakeUpByControllerSupported() is not None
        assert controller.getWakeUpByControllerSupported().getValue() is True

        attributes = controller.getCanControllerAttributes()
        assert isinstance(attributes, CanControllerConfiguration)
        assert attributes.getPropSeg().getValue() == 4
        assert attributes.getSyncJumpWidth().getValue() == 1
        assert attributes.getTimeSeg1().getValue() == 13
        assert attributes.getTimeSeg2().getValue() == 2

    def test_reads_requirements_branch_with_values(self, parser):
        controller = _read_into(
            "<SHORT-NAME>can_ctrl</SHORT-NAME>"
            "<CAN-COMMUNICATION-CONTROLLER-VARIANTS>"
            "<CAN-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "<WAKE-UP-BY-CONTROLLER-SUPPORTED>false</WAKE-UP-BY-CONTROLLER-SUPPORTED>"
            "<CAN-CONTROLLER-ATTRIBUTES>"
            "<CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
            "<MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>32</MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "<MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>16</MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "</CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
            "</CAN-CONTROLLER-ATTRIBUTES>"
            "</CAN-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "</CAN-COMMUNICATION-CONTROLLER-VARIANTS>"
        )
        assert controller.getWakeUpByControllerSupported().getValue() is False

        attributes = controller.getCanControllerAttributes()
        assert isinstance(attributes, CanControllerConfigurationRequirements)
        assert attributes.getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert attributes.getMinNumberOfTimeQuantaPerBit().getValue() == 16

    def test_missing_variants_wrapper_leaves_fields_none(self, parser):
        controller = _read_into("<SHORT-NAME>can_ctrl</SHORT-NAME><OTHER/>")
        assert controller.getWakeUpByControllerSupported() is None
        assert controller.getCanControllerAttributes() is None
