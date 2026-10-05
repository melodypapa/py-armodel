"""Parser tests for AbstractCanCommunicationController (Table 3.12, p.63).

The class is abstract with no own XML element: its XSD group
ABSTRACT-CAN-COMMUNICATION-CONTROLLER (AUTOSAR_00052.xsd line 144) is empty and the
single attribute canControllerAttributes surfaces as CAN-CONTROLLER-ATTRIBUTES in
ABSTRACT-CAN-COMMUNICATION-CONTROLLER-CONTENT (line 196, element at line 203 — a
choice of CAN-CONTROLLER-CONFIGURATION / CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS).
Coverage therefore targets the reusable readAbstractCanCommunicationController helper
(Rule 0001.7) that concrete subclasses call on the CONDITIONAL wrapper element;
element order per XSD: WAKE-UP-BY-CONTROLLER-SUPPORTED (COMMUNICATION-CONTROLLER-CONTENT,
line 20421) before CAN-CONTROLLER-ATTRIBUTES.
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanCommunicationController,
    CanControllerConfiguration,
    CanControllerConfigurationRequirements,
)
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _read_into(inner: str) -> CanCommunicationController:
    controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
    ARXMLParser().readAbstractCanCommunicationController(_snip(inner), controller)
    return controller


class TestReadAbstractCanCommunicationController:
    def test_reads_wake_up_and_configuration_with_values(self, parser):
        controller = _read_into(
            "<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>"
            "<CAN-CONTROLLER-ATTRIBUTES>"
            "<CAN-CONTROLLER-CONFIGURATION>"
            "<PROP-SEG>4</PROP-SEG>"
            "<SYNC-JUMP-WIDTH>1</SYNC-JUMP-WIDTH>"
            "<TIME-SEG-1>13</TIME-SEG-1>"
            "<TIME-SEG-2>2</TIME-SEG-2>"
            "</CAN-CONTROLLER-CONFIGURATION>"
            "</CAN-CONTROLLER-ATTRIBUTES>"
        )
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
            "<WAKE-UP-BY-CONTROLLER-SUPPORTED>false</WAKE-UP-BY-CONTROLLER-SUPPORTED>"
            "<CAN-CONTROLLER-ATTRIBUTES>"
            "<CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
            "<MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>32</MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "<MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>16</MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "</CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
            "</CAN-CONTROLLER-ATTRIBUTES>"
        )
        assert controller.getWakeUpByControllerSupported().getValue() is False

        attributes = controller.getCanControllerAttributes()
        assert isinstance(attributes, CanControllerConfigurationRequirements)
        assert attributes.getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert attributes.getMinNumberOfTimeQuantaPerBit().getValue() == 16

    def test_empty_group_leaves_fields_none(self, parser):
        controller = _read_into("<OTHER/>")
        assert controller.getWakeUpByControllerSupported() is None
        assert controller.getCanControllerAttributes() is None
