"""Parser tests for UserDefinedPhysicalChannel (Table 3.130, p.179).

XML element order per XSD USER-DEFINED-PHYSICAL-CHANNEL (AUTOSAR_00052.xsd line
128989): heritage groups (SHORT-NAME via IDENTIFIABLE) first, then the inherited
PHYSICAL-CHANNEL group content in sequenceOffset order (COMM-CONNECTORS,
FRAME-TRIGGERINGS, I-SIGNAL-TRIGGERINGS, MANAGED-PHYSICAL-CHANNEL-REFS,
PDU-TRIGGERINGS); the USER-DEFINED-PHYSICAL-CHANNEL own group (lines 128980-128988)
is an empty sequence — no atpVariation wrapper.
readUserDefinedPhysicalChannel calls readIdentifiable on the outer element and the
reusable readPhysicalChannel helper exactly once.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedPhysicalChannel
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_USER_DEFINED_PHYSICAL_CHANNEL = (
    "<USER-DEFINED-PHYSICAL-CHANNEL>"
    "<SHORT-NAME>Channel</SHORT-NAME>"
    "<COMM-CONNECTORS>"
    "<COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
    '<COMMUNICATION-CONNECTOR-REF DEST="COMMUNICATION-CONNECTOR">/EcuInst/Conn</COMMUNICATION-CONNECTOR-REF>'
    "</COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
    "</COMM-CONNECTORS>"
    "<MANAGED-PHYSICAL-CHANNEL-REFS>"
    '<MANAGED-PHYSICAL-CHANNEL-REF DEST="USER-DEFINED-PHYSICAL-CHANNEL">/Cluster/ManagedCh</MANAGED-PHYSICAL-CHANNEL-REF>'
    "</MANAGED-PHYSICAL-CHANNEL-REFS>"
    "</USER-DEFINED-PHYSICAL-CHANNEL>"
)

BARE_USER_DEFINED_PHYSICAL_CHANNEL = "<USER-DEFINED-PHYSICAL-CHANNEL>" "<SHORT-NAME>Channel</SHORT-NAME>" "</USER-DEFINED-PHYSICAL-CHANNEL>"


def _new_channel(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return UserDefinedPhysicalChannel(pkg, name)


def _read_user_defined_physical_channel(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    channel = _new_channel("Channel")
    ARXMLParser().readUserDefinedPhysicalChannel(root[0], channel)
    return channel


class TestReadUserDefinedPhysicalChannel:
    def test_reads_short_name_and_inherited_levels(self):
        channel = _read_user_defined_physical_channel(FULL_USER_DEFINED_PHYSICAL_CHANNEL)

        assert channel.getShortName() == "Channel"
        comm_connector_refs = channel.getCommConnectorRefs()
        assert len(comm_connector_refs) == 1
        assert comm_connector_refs[0].getValue() == "/EcuInst/Conn"
        assert comm_connector_refs[0].getDest() == "COMMUNICATION-CONNECTOR"

    def test_reads_managed_physical_channel_refs(self):
        channel = _read_user_defined_physical_channel(FULL_USER_DEFINED_PHYSICAL_CHANNEL)

        managed_refs = channel.getManagedPhysicalChannelRefs()
        assert len(managed_refs) == 1
        assert managed_refs[0].getValue() == "/Cluster/ManagedCh"
        assert managed_refs[0].getDest() == "USER-DEFINED-PHYSICAL-CHANNEL"

    def test_reads_bare_channel_to_empty_lists(self):
        channel = _read_user_defined_physical_channel(BARE_USER_DEFINED_PHYSICAL_CHANNEL)

        assert channel.getShortName() == "Channel"
        assert channel.getCommConnectorRefs() == []
        assert channel.getFrameTriggerings() == []
        assert channel.getISignalTriggerings() == []
        assert channel.getManagedPhysicalChannelRefs() == []
        assert channel.getPduTriggerings() == []
