"""Parser tests for LinCommunicationController (Table 3.37, p.93).

The class is abstract with no own XML element: its XSD group
LIN-COMMUNICATION-CONTROLLER (AUTOSAR_00052.xsd line 77049) is empty and the single
attribute protocolVersion surfaces as PROTOCOL-VERSION in
LIN-COMMUNICATION-CONTROLLER-CONTENT (line 77058), carried inside the
LIN-MASTER-CONDITIONAL / LIN-SLAVE-CONDITIONAL wrappers of the concrete subclasses
LinMaster / LinSlave. Coverage therefore targets the reusable
readLinCommunicationController helper (Rule 0001.7) that concrete subclasses call on
the CONDITIONAL wrapper element; element order per XSD:
WAKE-UP-BY-CONTROLLER-SUPPORTED (COMMUNICATION-CONTROLLER-CONTENT) before
PROTOCOL-VERSION.
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinMaster
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _read_into(inner: str) -> LinMaster:
    controller = LinMaster(parent=_autosar_root(), short_name="ctrl")
    ARXMLParser().readLinCommunicationController(_snip(inner), controller)
    return controller


class TestReadLinCommunicationController:
    def test_reads_wake_up_and_protocol_version_with_values(self, parser):
        controller = _read_into("<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>" "<PROTOCOL-VERSION>LIN22</PROTOCOL-VERSION>")
        assert controller.getWakeUpByControllerSupported() is not None
        assert controller.getWakeUpByControllerSupported().getValue() is True

        assert controller.getProtocolVersion() is not None
        assert controller.getProtocolVersion().getValue() == "LIN22"

    def test_reads_protocol_version_only(self, parser):
        controller = _read_into("<PROTOCOL-VERSION>ISO17987</PROTOCOL-VERSION>")

        assert controller.getWakeUpByControllerSupported() is None
        assert controller.getProtocolVersion() is not None
        assert controller.getProtocolVersion().getValue() == "ISO17987"

    def test_empty_group_leaves_fields_none(self, parser):
        controller = _read_into("<OTHER/>")

        assert controller.getWakeUpByControllerSupported() is None
        assert controller.getProtocolVersion() is None
