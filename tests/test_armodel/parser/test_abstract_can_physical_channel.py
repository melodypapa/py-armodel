"""Parser tests for AbstractCanPhysicalChannel (Table 3.20, p.73).

The class is abstract with no own attribute rows (Table 3.20 renders the
Attribute header only) and its XSD group ABSTRACT-CAN-PHYSICAL-CHANNEL
(AUTOSAR_00052.xsd line 218) is an empty <xsd:sequence/>: the abstract level
contributes no XML elements of its own. Coverage therefore runs through the
concrete CAN-PHYSICAL-CHANNEL path (readCanPhysicalChannel on a
CanPhysicalChannel instance, which calls the base readPhysicalChannel helper
exactly once) and asserts the instance read is an AbstractCanPhysicalChannel
whose inherited PhysicalChannel fields carry the parsed values.
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanPhysicalChannel,
    CanPhysicalChannel,
)
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _autosar_root, _snip

FULL_CHANNEL = (
    "<SHORT-NAME>ch</SHORT-NAME>"
    "<COMM-CONNECTORS>"
    "<COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
    "<COMMUNICATION-CONNECTOR-REF DEST='CAN-COMMUNICATION-CONNECTOR'>/ecu/can_conn</COMMUNICATION-CONNECTOR-REF>"
    "</COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
    "</COMM-CONNECTORS>"
    "<FRAME-TRIGGERINGS>"
    "<CAN-FRAME-TRIGGERING>"
    "<SHORT-NAME>can_ft</SHORT-NAME>"
    "<FRAME-REF DEST='CAN-FRAME'>/cluster/frames/frame1</FRAME-REF>"
    "</CAN-FRAME-TRIGGERING>"
    "</FRAME-TRIGGERINGS>"
    "<I-SIGNAL-TRIGGERINGS>"
    "<I-SIGNAL-TRIGGERING>"
    "<SHORT-NAME>ist</SHORT-NAME>"
    "</I-SIGNAL-TRIGGERING>"
    "</I-SIGNAL-TRIGGERINGS>"
    "<MANAGED-PHYSICAL-CHANNEL-REFS>"
    "<MANAGED-PHYSICAL-CHANNEL-REF DEST='FLEXRAY-PHYSICAL-CHANNEL'>/cluster/ch2</MANAGED-PHYSICAL-CHANNEL-REF>"
    "</MANAGED-PHYSICAL-CHANNEL-REFS>"
    "<PDU-TRIGGERINGS>"
    "<PDU-TRIGGERING>"
    "<SHORT-NAME>pdt</SHORT-NAME>"
    "</PDU-TRIGGERING>"
    "</PDU-TRIGGERINGS>"
)

BARE_CHANNEL = "<SHORT-NAME>ch</SHORT-NAME>"


def _read_into(inner: str, attrs: str = "") -> CanPhysicalChannel:
    channel = CanPhysicalChannel(parent=_autosar_root(), short_name="ch")
    ARXMLParser().readCanPhysicalChannel(_snip(inner, root_tag="CAN-PHYSICAL-CHANNEL", attrs=attrs), channel)
    return channel


class TestReadAbstractCanPhysicalChannel:
    def test_reads_instance_of_abstract_can_physical_channel(self):
        channel = _read_into(BARE_CHANNEL)
        assert isinstance(channel, AbstractCanPhysicalChannel)
        assert isinstance(channel, CanPhysicalChannel)

    def test_reads_inherited_fields_with_values(self, parser):
        channel = _read_into(FULL_CHANNEL, attrs=' UUID="test-uuid-320"')

        assert channel.getUuid().getValue() == "test-uuid-320"

        comm_refs = channel.getCommConnectorRefs()
        assert len(comm_refs) == 1
        assert comm_refs[0].getValue() == "/ecu/can_conn"
        assert comm_refs[0].getDest() == "CAN-COMMUNICATION-CONNECTOR"

        triggerings = channel.getFrameTriggerings()
        assert len(triggerings) == 1
        assert triggerings[0].getShortName() == "can_ft"
        assert triggerings[0].getFrameRef().getValue() == "/cluster/frames/frame1"
        assert triggerings[0].getFrameRef().getDest() == "CAN-FRAME"

        assert channel.getISignalTriggerings()[0].getShortName() == "ist"

        managed_refs = channel.getManagedPhysicalChannelRefs()
        assert len(managed_refs) == 1
        assert managed_refs[0].getValue() == "/cluster/ch2"
        assert managed_refs[0].getDest() == "FLEXRAY-PHYSICAL-CHANNEL"

        assert channel.getPduTriggerings()[0].getShortName() == "pdt"

    def test_empty_wrapper_leaves_inherited_fields_empty(self, parser):
        channel = _read_into(BARE_CHANNEL)

        assert channel.getShortName() == "ch"
        assert channel.getCommConnectorRefs() == []
        assert channel.getFrameTriggerings() == []
        assert channel.getISignalTriggerings() == []
        assert channel.getManagedPhysicalChannelRefs() == []
        assert channel.getPduTriggerings() == []
