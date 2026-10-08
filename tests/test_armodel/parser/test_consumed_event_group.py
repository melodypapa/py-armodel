"""Reader tests for ConsumedEventGroup (R23-11 CP_TPS_SystemTemplate, Table 6.168, p.505).

XSD group CONSUMED-EVENT-GROUP (AUTOSAR_00052.xsd l.22376) element order:
APPLICATION-ENDPOINT-REF, AUTO-REQUIRE, EVENT-GROUP-IDENTIFIER, EVENT-MULTICAST-ADDRESSS,
PDU-ACTIVATION-ROUTING-GROUPS, PRIORITY, ROUTING-GROUP-REFS, SD-CLIENT-CONFIG,
SD-CLIENT-TIMER-CONFIGS, VARIATION-POINT. instanceIdentifier is atp.Status=removed
and absent from the PDF table - not modeled (Rule 0015).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import SdClientConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ConsumedEventGroup,
    PduActivationRoutingGroup,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<CONSUMED-EVENT-GROUP xmlns='{NS}'>{inner}</CONSUMED-EVENT-GROUP>")


ALL_ATTRS = (
    "<SHORT-NAME>ceg1</SHORT-NAME>"
    "<APPLICATION-ENDPOINT-REF DEST='APPLICATION-ENDPOINT'>/ae1</APPLICATION-ENDPOINT-REF>"
    "<AUTO-REQUIRE>true</AUTO-REQUIRE>"
    "<EVENT-GROUP-IDENTIFIER>42</EVENT-GROUP-IDENTIFIER>"
    "<EVENT-MULTICAST-ADDRESSS>"
    "<APPLICATION-ENDPOINT-REF-CONDITIONAL>"
    "<APPLICATION-ENDPOINT-REF DEST='APPLICATION-ENDPOINT'>/mc1</APPLICATION-ENDPOINT-REF>"
    "</APPLICATION-ENDPOINT-REF-CONDITIONAL>"
    "<APPLICATION-ENDPOINT-REF-CONDITIONAL>"
    "<APPLICATION-ENDPOINT-REF DEST='APPLICATION-ENDPOINT'>/mc2</APPLICATION-ENDPOINT-REF>"
    "</APPLICATION-ENDPOINT-REF-CONDITIONAL>"
    "</EVENT-MULTICAST-ADDRESSS>"
    "<PDU-ACTIVATION-ROUTING-GROUPS>"
    "<PDU-ACTIVATION-ROUTING-GROUP><SHORT-NAME>parg1</SHORT-NAME></PDU-ACTIVATION-ROUTING-GROUP>"
    "</PDU-ACTIVATION-ROUTING-GROUPS>"
    "<PRIORITY>5</PRIORITY>"
    "<ROUTING-GROUP-REFS>"
    "<ROUTING-GROUP-REF DEST='SO-AD-ROUTING-GROUP'>/rg1</ROUTING-GROUP-REF>"
    "</ROUTING-GROUP-REFS>"
    "<SD-CLIENT-CONFIG><TTL>10</TTL></SD-CLIENT-CONFIG>"
    "<SD-CLIENT-TIMER-CONFIGS>"
    "<SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL>"
    "<SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF DEST='SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG'>/timing1</SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF>"
    "</SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL>"
    "</SD-CLIENT-TIMER-CONFIGS>"
)


class TestReadConsumedEventGroup:
    def test_read_all_attrs(self, parser):
        group = ConsumedEventGroup(parser, "ceg1")
        element = _snip(ALL_ATTRS)
        parser.readConsumedEventGroup(element, group)

        assert group.getShortName() == "ceg1"
        assert group.getApplicationEndpointRef().getValue() == "/ae1"
        assert group.getApplicationEndpointRef().getDest() == "APPLICATION-ENDPOINT"
        assert group.getAutoRequire().getValue() is True
        assert group.getEventGroupIdentifier().getValue() == 42
        assert [r.getValue() for r in group.getEventMulticastAddressRefs()] == ["/mc1", "/mc2"]
        groups = group.getPduActivationRoutingGroups()
        assert len(groups) == 1
        assert isinstance(groups[0], PduActivationRoutingGroup)
        assert groups[0].getShortName() == "parg1"
        assert group.getPriority().getValue() == 5
        assert [r.getValue() for r in group.getRoutingGroupRefs()] == ["/rg1"]
        config = group.getSdClientConfig()
        assert isinstance(config, SdClientConfig)
        assert config.getTtl().getValue() == 10
        assert group.getSdClientTimerConfigRef().getValue() == "/timing1"
        assert group.getSdClientTimerConfigRef().getDest() == "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG"

    def test_read_empty_element_leaves_defaults(self, parser):
        group = ConsumedEventGroup(parser, "ceg1")
        element = _snip("<SHORT-NAME>ceg1</SHORT-NAME>")
        parser.readConsumedEventGroup(element, group)

        assert group.getApplicationEndpointRef() is None
        assert group.getAutoRequire() is None
        assert group.getEventGroupIdentifier() is None
        assert group.getEventMulticastAddressRefs() == []
        assert group.getPduActivationRoutingGroups() == []
        assert group.getPriority() is None
        assert group.getRoutingGroupRefs() == []
        assert group.getSdClientConfig() is None
        assert group.getSdClientTimerConfigRef() is None

    def test_removed_instance_identifier_not_read(self, parser):
        """instanceIdentifier is atp.Status=removed (Rule 0015) - the reader must not model it."""
        group = ConsumedEventGroup(parser, "ceg1")
        element = _snip("<SHORT-NAME>ceg1</SHORT-NAME><INSTANCE-IDENTIFIER>7</INSTANCE-IDENTIFIER>")
        parser.readConsumedEventGroup(element, group)

        assert not hasattr(group, "instanceIdentifier")
