"""Parser tests for TtcanCommunicationConnector (Table 3.27, p.77).

The class has no own attribute rows and its XSD group TTCAN-COMMUNICATION-CONNECTOR
(AUTOSAR_00052.xsd line 126966) is an empty <xsd:sequence/>: the concrete level
contributes no XML elements of its own and the complexType (line 126975) is a flat
sequence of heritage groups (no VARIANTS wrapper). readTtcanCommunicationConnector
calls the base readCommunicationConnector helper exactly once. The class is consumed
as a concrete element of the EcuInstance CONNECTORS choice (line 50399, Rule 0001.7):
dispatch coverage runs through the TTCAN-COMMUNICATION-CONNECTOR branch on
readEcuInstanceConnectors.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector, TtcanCommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_TTCAN_CONNECTOR = (
    "<TTCAN-COMMUNICATION-CONNECTOR>"
    "<SHORT-NAME>ttcan_conn</SHORT-NAME>"
    "<COMM-CONTROLLER-REF DEST='TTCAN-COMMUNICATION-CONTROLLER'>/ecu/ttcan_ctl</COMM-CONTROLLER-REF>"
    "<CREATE-ECU-WAKEUP-SOURCE>true</CREATE-ECU-WAKEUP-SOURCE>"
    "<DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED>false</DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED>"
    "<ECU-COMM-PORT-INSTANCES>"
    "<FRAME-PORT><SHORT-NAME>fp</SHORT-NAME><COMMUNICATION-DIRECTION>IN</COMMUNICATION-DIRECTION></FRAME-PORT>"
    "</ECU-COMM-PORT-INSTANCES>"
    "<PNC-FILTER-ARRAY-MASKS><PNC-FILTER-ARRAY-MASK>255</PNC-FILTER-ARRAY-MASK><PNC-FILTER-ARRAY-MASK>1</PNC-FILTER-ARRAY-MASK></PNC-FILTER-ARRAY-MASKS>"
    "<PNC-GATEWAY-TYPE>active</PNC-GATEWAY-TYPE>"
    "</TTCAN-COMMUNICATION-CONNECTOR>"
)

BARE_TTCAN_CONNECTOR = "<TTCAN-COMMUNICATION-CONNECTOR>" "<SHORT-NAME>ttcan_conn</SHORT-NAME>" "</TTCAN-COMMUNICATION-CONNECTOR>"


def _read_into_instance(inner):
    root = _wrap(inner)
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    ARXMLParser().readEcuInstanceConnectors(root, instance)
    return instance


def _wrap(inner):
    from tests.test_armodel.parser._helpers import _snip

    return _snip("<CONNECTORS>%s</CONNECTORS>" % inner)


class TestReadTtcanCommunicationConnectorDispatch:
    """Table 3.27: the CONNECTORS dispatch branch constructs the concrete TtcanCommunicationConnector (Rule 0001.7)."""

    def test_dispatch_creates_ttcan_communication_connector_instance(self, parser):
        instance = _read_into_instance(BARE_TTCAN_CONNECTOR)
        connectors = instance.getConnectors()

        assert len(connectors) == 1
        connector = connectors[0]
        assert isinstance(connector, TtcanCommunicationConnector)
        assert isinstance(connector, CanCommunicationConnector) is False
        assert connector.getShortName() == "ttcan_conn"

    def test_dispatch_keeps_can_branch_disjoint(self, parser):
        mixed = BARE_TTCAN_CONNECTOR + "<CAN-COMMUNICATION-CONNECTOR><SHORT-NAME>can_conn</SHORT-NAME></CAN-COMMUNICATION-CONNECTOR>"
        connectors = _read_into_instance(mixed).getConnectors()

        assert [c.getShortName() for c in connectors] == ["ttcan_conn", "can_conn"]
        assert isinstance(connectors[0], TtcanCommunicationConnector)
        assert not isinstance(connectors[1], TtcanCommunicationConnector)
        assert isinstance(connectors[1], CanCommunicationConnector)

    def test_dispatch_reads_inherited_field_values(self, parser):
        connector = _read_into_instance(FULL_TTCAN_CONNECTOR).getConnectors()[0]

        assert isinstance(connector, TtcanCommunicationConnector)
        ref = connector.getCommControllerRef()
        assert ref.getValue() == "/ecu/ttcan_ctl"
        assert ref.getDest() == "TTCAN-COMMUNICATION-CONTROLLER"
        assert connector.getCreateEcuWakeupSource().getValue() is True
        assert connector.getDynamicPncToChannelMappingEnabled().getValue() is False

        ports = connector.getEcuCommPortInstances()
        assert len(ports) == 1
        assert ports[0].getShortName() == "fp"
        assert ports[0].getCommunicationDirection().getValue() == "IN"

        assert [mask.getValue() for mask in connector.getPncFilterArrayMasks()] == [255, 1]
        assert connector.getPncGatewayType().getValue() == "active"


class TestReadTtcanCommunicationConnector:
    """Table 3.27: the readTtcanCommunicationConnector entry helper calls readCommunicationConnector exactly once (no own elements to read)."""

    def test_entry_helper_reads_communication_connector_level(self, parser):
        from tests.test_armodel.parser._helpers import _snip

        root = _snip(FULL_TTCAN_CONNECTOR)
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        connector = TtcanCommunicationConnector(pkg, "ttcan_conn")
        parser.readTtcanCommunicationConnector(root[0], connector)

        assert connector.getShortName() == "ttcan_conn"
        assert connector.getCommControllerRef().getValue() == "/ecu/ttcan_ctl"
        assert connector.getCreateEcuWakeupSource().getValue() is True
        assert connector.getDynamicPncToChannelMappingEnabled().getValue() is False
        assert [p.getShortName() for p in connector.getEcuCommPortInstances()] == ["fp"]
        assert [mask.getValue() for mask in connector.getPncFilterArrayMasks()] == [255, 1]
        assert connector.getPncGatewayType().getValue() == "active"

    def test_entry_helper_reads_bare_connector_to_empty_fields(self, parser):
        from tests.test_armodel.parser._helpers import _snip

        root = _snip(BARE_TTCAN_CONNECTOR)
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        connector = TtcanCommunicationConnector(pkg, "ttcan_conn")
        parser.readTtcanCommunicationConnector(root[0], connector)

        assert connector.getShortName() == "ttcan_conn"
        assert connector.getCommControllerRef() is None
        assert connector.getCreateEcuWakeupSource() is None
        assert connector.getDynamicPncToChannelMappingEnabled() is None
        assert connector.getEcuCommPortInstances() == []
        assert connector.getPncFilterArrayMasks() == []
        assert connector.getPncGatewayType() is None
