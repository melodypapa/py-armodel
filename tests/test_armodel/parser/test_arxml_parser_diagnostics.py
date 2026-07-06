"""Tests for diagnostic-related handler methods.

Covers:
- ``readDoIpLogicAddress`` / ``readDoIpTpConfigDoIpLogicAddresses``
- ``readDoIpTpConnection`` / ``readDoIpTpConfigTpConnections``

(DoIp = Diagnostics over IP)

Additional diagnostic tests from ``test_arxml_parser_remaining_gaps.py`` will
be merged here.

Shared fixtures (``parser``, ``warning_parser``, ``reset_autosar``) are provided
by ``conftest.py``; helper functions (``_snip``, ``_autosar_root``) live in
``_helpers.py``.
"""
from tests.test_armodel.parser._helpers import _autosar_root, _snip
import logging
from unittest.mock import MagicMock


class TestDoIpHandlers:
    """Tests for DoIpLogicAddress, DoIpTpConnection, DoIpTpConfig handlers."""

    def test_readDoIpLogicAddress_sets_address(self, parser):
        from armodel.models import DoIpLogicAddress
        address = DoIpLogicAddress(parent=_autosar_root(), short_name="doIpAddr")
        element = _snip(
            "<SHORT-NAME>doIpAddr</SHORT-NAME>"
            "<ADDRESS>0x0E80</ADDRESS>",
            root_tag="DO-IP-LOGIC-ADDRESS",
        )
        parser.readDoIpLogicAddress(element, address)
        assert address.getShortName() == "doIpAddr"
        assert address.getAddress() is not None
        assert address.getAddress().getValue() == 0x0E80

    def test_readDoIpLogicAddress_empty(self, parser):
        from armodel.models import DoIpLogicAddress
        address = DoIpLogicAddress(parent=_autosar_root(), short_name="doIpAddr")
        element = _snip(
            "<SHORT-NAME>doIpAddr</SHORT-NAME>",
            root_tag="DO-IP-LOGIC-ADDRESS",
        )
        parser.readDoIpLogicAddress(element, address)
        assert address.getAddress() is None

    def test_readDoIpTpConfigDoIpLogicAddresses_with_address(self, parser):
        from armodel.models import DoIpTpConfig
        config = DoIpTpConfig(parent=_autosar_root(), short_name="doIpConfig")
        element = _snip(
            "<DO-IP-LOGIC-ADDRESSS>"
            "<DO-IP-LOGIC-ADDRESS>"
            "<SHORT-NAME>logicAddr</SHORT-NAME>"
            "<ADDRESS>0x0E80</ADDRESS>"
            "</DO-IP-LOGIC-ADDRESS>"
            "</DO-IP-LOGIC-ADDRESSS>",
        )
        parser.readDoIpTpConfigDoIpLogicAddresses(element, config)
        addresses = config.getDoIpLogicAddresses()
        assert len(addresses) == 1
        assert addresses[0].getShortName() == "logicAddr"
        assert addresses[0].getAddress().getValue() == 0x0E80

    def test_readDoIpTpConfigDoIpLogicAddresses_unknown_warning(self, warning_parser):
        from armodel.models import DoIpTpConfig
        config = DoIpTpConfig(parent=_autosar_root(), short_name="doIpConfig")
        element = _snip(
            "<DO-IP-LOGIC-ADDRESSS>"
            "<UNKNOWN-ADDRESS>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-ADDRESS>"
            "</DO-IP-LOGIC-ADDRESSS>",
        )
        warning_parser.readDoIpTpConfigDoIpLogicAddresses(element, config)
        assert len(config.getDoIpLogicAddresses()) == 0

    def test_readDoIpTpConnection_sets_refs(self, parser):
        from armodel.models import DoIpTpConnection
        connection = DoIpTpConnection()
        element = _snip(
            '<DO-IP-SOURCE-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/doIp/srcAddr</DO-IP-SOURCE-ADDRESS-REF>'
            '<DO-IP-TARGET-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/doIp/tgtAddr</DO-IP-TARGET-ADDRESS-REF>'
            '<TP-SDU-REF DEST="I-PDU">/pdus/sdu</TP-SDU-REF>',
            root_tag="DO-IP-TP-CONNECTION",
        )
        parser.readDoIpTpConnection(element, connection)
        assert connection.getDoIpSourceAddressRef() is not None
        assert connection.getDoIpSourceAddressRef().getValue() == "/doIp/srcAddr"
        assert connection.getDoIpTargetAddressRef() is not None
        assert connection.getDoIpTargetAddressRef().getValue() == "/doIp/tgtAddr"
        assert connection.getTpSduRef() is not None
        assert connection.getTpSduRef().getValue() == "/pdus/sdu"

    def test_readDoIpTpConnection_empty(self, parser):
        from armodel.models import DoIpTpConnection
        connection = DoIpTpConnection()
        element = _snip("", root_tag="DO-IP-TP-CONNECTION")
        parser.readDoIpTpConnection(element, connection)
        assert connection.getDoIpSourceAddressRef() is None
        assert connection.getDoIpTargetAddressRef() is None
        assert connection.getTpSduRef() is None

    def test_readDoIpTpConfigTpConnections_with_connection(self, parser):
        from armodel.models import DoIpTpConfig
        config = DoIpTpConfig(parent=_autosar_root(), short_name="doIpConfig")
        element = _snip(
            "<TP-CONNECTIONS>"
            "<DO-IP-TP-CONNECTION>"
            '<DO-IP-SOURCE-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/doIp/src</DO-IP-SOURCE-ADDRESS-REF>'
            '<DO-IP-TARGET-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/doIp/tgt</DO-IP-TARGET-ADDRESS-REF>'
            "</DO-IP-TP-CONNECTION>"
            "</TP-CONNECTIONS>",
        )
        parser.readDoIpTpConfigTpConnections(element, config)
        connections = config.getTpConnections()
        assert len(connections) == 1
        assert connections[0].getDoIpSourceAddressRef().getValue() == "/doIp/src"
        assert connections[0].getDoIpTargetAddressRef().getValue() == "/doIp/tgt"

    def test_readDoIpTpConfigTpConnections_unknown_warning(self, warning_parser):
        from armodel.models import DoIpTpConfig
        config = DoIpTpConfig(parent=_autosar_root(), short_name="doIpConfig")
        element = _snip(
            "<TP-CONNECTIONS>"
            "<UNKNOWN-CONNECTION>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-CONNECTION>"
            "</TP-CONNECTIONS>",
        )
        warning_parser.readDoIpTpConfigTpConnections(element, config)
        assert len(config.getTpConnections()) == 0


# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestServiceInstanceGaps:
    def test_readConsumedServiceInstance_sets_refs(self, parser):
        from armodel.models import ApplicationEndpoint
        end_point = ApplicationEndpoint(
            parent=MagicMock(), short_name="Aep"
        )
        instance = end_point.createConsumedServiceInstance("Csi")
        element = _snip(
            '<PROVIDED-SERVICE-INSTANCE-REF DEST="PROVIDED-SERVICE-INSTANCE">/psi</PROVIDED-SERVICE-INSTANCE-REF>'
            "<SD-CLIENT-CONFIG/>"
        )
        parser.readConsumedServiceInstance(element, instance)
        assert instance.getProvidedServiceInstanceRef() is not None

    def test_readSocketAddressApplicationEndpointConsumedServiceInstances_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ApplicationEndpoint
        end_point = ApplicationEndpoint(
            parent=MagicMock(), short_name="Aep"
        )
        element = _snip(
            "<CONSUMED-SERVICE-INSTANCES><BAD/></CONSUMED-SERVICE-INSTANCES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSocketAddressApplicationEndpointConsumedServiceInstances(
                element, end_point
            )
        assert any("Unsupported ConsumedServiceInstances"
                   in r.getMessage() for r in caplog.records)

    def test_readSocketAddressApplicationEndpointConsumedServiceInstances_creates(
        self, parser
    ):
        from armodel.models import ApplicationEndpoint
        end_point = ApplicationEndpoint(
            parent=MagicMock(), short_name="Aep"
        )
        element = _snip(
            "<CONSUMED-SERVICE-INSTANCES>"
            "<CONSUMED-SERVICE-INSTANCE>"
            "<SHORT-NAME>csi</SHORT-NAME>"
            "</CONSUMED-SERVICE-INSTANCE>"
            "</CONSUMED-SERVICE-INSTANCES>"
        )
        parser.readSocketAddressApplicationEndpointConsumedServiceInstances(
            element, end_point
        )
        assert len(end_point.getConsumedServiceInstances()) == 1

    def test_readSocketAddressApplicationEndpointProvidedServiceInstances_creates(
        self, parser
    ):
        from armodel.models import ApplicationEndpoint
        end_point = ApplicationEndpoint(
            parent=MagicMock(), short_name="Aep"
        )
        element = _snip(
            "<PROVIDED-SERVICE-INSTANCES>"
            "<PROVIDED-SERVICE-INSTANCE>"
            "<SHORT-NAME>psi</SHORT-NAME>"
            "</PROVIDED-SERVICE-INSTANCE>"
            "</PROVIDED-SERVICE-INSTANCES>"
        )
        parser.readSocketAddressApplicationEndpointProvidedServiceInstance(
            element, end_point
        )
        assert len(end_point.getProvidedServiceInstances()) == 1

    def test_readEventHandler_adds_consumed_event_group_ref(
        self, parser
    ):
        from armodel.models import ProvidedServiceInstance
        instance = ProvidedServiceInstance(
            parent=MagicMock(), short_name="Psi"
        )
        handler = instance.createEventHandler("Eh")
        element = _snip(
            '<APPLICATION-ENDPOINT-REF DEST="APPLICATION-ENDPOINT">/ae</APPLICATION-ENDPOINT-REF>'
            "<CONSUMED-EVENT-GROUP-REFS>"
            '<CONSUMED-EVENT-GROUP-REF DEST="CONSUMED-EVENT-GROUP">/ceg</CONSUMED-EVENT-GROUP-REF>'
            "</CONSUMED-EVENT-GROUP-REFS>"
            "<ROUTING-GROUP-REFS>"
            '<ROUTING-GROUP-REF DEST="SO-AD-ROUTING-GROUP">/rg</ROUTING-GROUP-REF>'
            "</ROUTING-GROUP-REFS>"
        )
        parser.readEventHandler(element, handler)
        assert len(handler.getConsumedEventGroupRefs()) == 1
        assert len(handler.getRoutingGroupRefs()) == 1

    def test_readProvidedServiceInstanceEventHandlers_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ProvidedServiceInstance
        instance = ProvidedServiceInstance(
            parent=MagicMock(), short_name="Psi"
        )
        element = _snip(
            "<EVENT-HANDLERS><BAD/></EVENT-HANDLERS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readProvidedServiceInstanceEventHandlers(
                element, instance
            )
        assert any("Unsupported Event Handler" in r.getMessage()
                   for r in caplog.records)

    def test_readSocketAddressApplicationEndpointProvidedServiceInstance_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ApplicationEndpoint
        end_point = ApplicationEndpoint(
            parent=MagicMock(), short_name="Aep"
        )
        element = _snip(
            "<PROVIDED-SERVICE-INSTANCES><BAD/></PROVIDED-SERVICE-INSTANCES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSocketAddressApplicationEndpointProvidedServiceInstance(
                element, end_point
            )
        assert any("Unsupported ConsumedServiceInstances"
                   in r.getMessage() for r in caplog.records)


# ==================== CommunicationCluster PhysicalChannels (L3498-3505) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestDiagnosticConnectionGaps:
    def test_readDiagnosticConnectionFunctionalRequestRefs_adds_ref(
        self, parser
    ):
        from armodel.models import DiagnosticConnection
        conn = DiagnosticConnection(
            parent=MagicMock(), short_name="Dc"
        )
        element = _snip(
            "<FUNCTIONAL-REQUEST-REFS>"
            '<FUNCTIONAL-REQUEST-REF DEST="DIAGNOSTIC-CONNECTION">/fr</FUNCTIONAL-REQUEST-REF>'
            "</FUNCTIONAL-REQUEST-REFS>"
        )
        parser.readDiagnosticConnectionFunctionalRequestRefs(
            element, conn
        )
        assert len(conn.getFunctionalRequestRefs()) == 1

    def test_readDiagnosticServiceTableDiagnosticConnectionRefs_adds(
        self, parser
    ):
        from armodel.models import DiagnosticServiceTable
        table = DiagnosticServiceTable(
            parent=MagicMock(), short_name="Dst"
        )
        element = _snip(
            "<DIAGNOSTIC-CONNECTIONS>"
            "<DIAGNOSTIC-CONNECTION-REF-CONDITIONAL>"
            '<DIAGNOSTIC-CONNECTION-REF DEST="DIAGNOSTIC-CONNECTION">/dc</DIAGNOSTIC-CONNECTION-REF>'
            "</DIAGNOSTIC-CONNECTION-REF-CONDITIONAL>"
            "</DIAGNOSTIC-CONNECTIONS>"
        )
        parser.readDiagnosticServiceTableDiagnosticConnectionRefs(
            element, table
        )
        assert len(table.getDiagnosticConnectionRefs()) == 1


# ==================== HwElement / HwCategory (L3808, L3826) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestDiagEventDebounceAlgorithm:
    def test_readDiagEventDebounceAlgorithm_creates_monitor_internal(
        self, parser
    ):
        from armodel.models import DiagnosticEventNeeds
        needs = DiagnosticEventNeeds(
            parent=MagicMock(), short_name="Den"
        )
        element = _snip(
            "<DIAG-EVENT-DEBOUNCE-ALGORITHM>"
            "<DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL>"
            "<SHORT-NAME>Di</SHORT-NAME>"
            "</DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL>"
            "</DIAG-EVENT-DEBOUNCE-ALGORITHM>"
        )
        parser.readDiagEventDebounceAlgorithm(element, needs)
        assert needs.getDiagEventDebounceAlgorithm() is not None

    def test_readDiagEventDebounceAlgorithm_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import DiagnosticEventNeeds
        needs = DiagnosticEventNeeds(
            parent=MagicMock(), short_name="Den"
        )
        element = _snip(
            "<DIAG-EVENT-DEBOUNCE-ALGORITHM><BAD/></DIAG-EVENT-DEBOUNCE-ALGORITHM>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readDiagEventDebounceAlgorithm(
                element, needs
            )
        assert any("Unsupported DiagEventDebounceAlgorithm"
                   in r.getMessage() for r in caplog.records)

