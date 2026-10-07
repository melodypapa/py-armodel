"""Reader tests for InitialSdDelayConfig (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table 6.170, p.514).

InitialSdDelayConfig has no standalone XML element: it is read inline from its
aggregators through the shared ``getInitialSdDelayConfig`` helper. XSD group
``INITIAL-SD-DELAY-CONFIG`` (AUTOSAR_00052.xsd l.72399) element order:
INITIAL-DELAY-MAX-VALUE, INITIAL-DELAY-MIN-VALUE, INITIAL-REPETITIONS-BASE-DELAY,
INITIAL-REPETITIONS-MAX. The class is an ``ARObject``, so the element also carries the
``AR:AR-OBJECT`` attribute group (``S`` checksum / ``T`` timestamp, XSD l.4900).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    InitialSdDelayConfig,
    SomeipSdClientServiceInstanceConfig,
)
from tests.test_armodel.parser._helpers import _snip

FOUR_ATTRIBUTES = (
    "<INITIAL-DELAY-MAX-VALUE>0.1</INITIAL-DELAY-MAX-VALUE>"
    "<INITIAL-DELAY-MIN-VALUE>0.01</INITIAL-DELAY-MIN-VALUE>"
    "<INITIAL-REPETITIONS-BASE-DELAY>0.05</INITIAL-REPETITIONS-BASE-DELAY>"
    "<INITIAL-REPETITIONS-MAX>3</INITIAL-REPETITIONS-MAX>"
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestInitialSdDelayConfigReader:
    def test_reads_all_four_attributes(self, parser):
        element = _snip("<INITIAL-FIND-BEHAVIOR>%s</INITIAL-FIND-BEHAVIOR>" % FOUR_ATTRIBUTES)
        config = parser.getInitialSdDelayConfig(element, "INITIAL-FIND-BEHAVIOR")
        assert isinstance(config, InitialSdDelayConfig)
        assert config.getInitialDelayMaxValue().getValue() == 0.1
        assert config.getInitialDelayMinValue().getValue() == 0.01
        assert config.getInitialRepetitionsBaseDelay().getValue() == 0.05
        assert config.getInitialRepetitionsMax().getValue() == 3

    def test_absent_element_returns_none(self, parser):
        element = _snip("<OTHER/>")
        assert parser.getInitialSdDelayConfig(element, "INITIAL-FIND-BEHAVIOR") is None

    def test_empty_element_leaves_all_defaults(self, parser):
        element = _snip("<INITIAL-FIND-BEHAVIOR/>")
        config = parser.getInitialSdDelayConfig(element, "INITIAL-FIND-BEHAVIOR")
        assert isinstance(config, InitialSdDelayConfig)
        assert config.getInitialDelayMaxValue() is None
        assert config.getInitialDelayMinValue() is None
        assert config.getInitialRepetitionsBaseDelay() is None
        assert config.getInitialRepetitionsMax() is None

    def test_reads_arobject_checksum_and_timestamp(self, parser):
        element = _snip('<INITIAL-FIND-BEHAVIOR S="1234" T="2024-01-01T00:00:00Z"/>')
        config = parser.getInitialSdDelayConfig(element, "INITIAL-FIND-BEHAVIOR")
        assert config.getChecksum().getValue() == "1234"
        assert config.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_sd_client_config_aggregator_reads_initial_find_behavior(self, parser):
        element = _snip("<SD-CLIENT-CONFIG><INITIAL-FIND-BEHAVIOR>%s</INITIAL-FIND-BEHAVIOR></SD-CLIENT-CONFIG>" % FOUR_ATTRIBUTES)
        config = parser.getSdClientConfig(element, "SD-CLIENT-CONFIG")
        behavior = config.getInitialFindBehavior()
        assert isinstance(behavior, InitialSdDelayConfig)
        assert behavior.getInitialDelayMaxValue().getValue() == 0.1
        assert behavior.getInitialDelayMinValue().getValue() == 0.01
        assert behavior.getInitialRepetitionsBaseDelay().getValue() == 0.05
        assert behavior.getInitialRepetitionsMax().getValue() == 3

    def test_sd_server_config_aggregator_reads_initial_offer_behavior(self, parser):
        element = _snip("<SD-SERVER-CONFIG><INITIAL-OFFER-BEHAVIOR>%s</INITIAL-OFFER-BEHAVIOR></SD-SERVER-CONFIG>" % FOUR_ATTRIBUTES)
        config = parser.getSdServerConfig(element, "SD-SERVER-CONFIG")
        behavior = config.getInitialOfferBehavior()
        assert isinstance(behavior, InitialSdDelayConfig)
        assert behavior.getInitialDelayMaxValue().getValue() == 0.1
        assert behavior.getInitialDelayMinValue().getValue() == 0.01
        assert behavior.getInitialRepetitionsBaseDelay().getValue() == 0.05
        assert behavior.getInitialRepetitionsMax().getValue() == 3

    def test_someip_sd_client_aggregator_reads_initial_find_behavior(self, parser):
        config = SomeipSdClientServiceInstanceConfig(MockParent(), "cfg")
        element = _snip("<SHORT-NAME>cfg</SHORT-NAME><INITIAL-FIND-BEHAVIOR>%s</INITIAL-FIND-BEHAVIOR>" % FOUR_ATTRIBUTES, root_tag="SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG")
        parser.readSomeipSdClientServiceInstanceConfig(element, config)
        behavior = config.getInitialFindBehavior()
        assert isinstance(behavior, InitialSdDelayConfig)
        assert behavior.getInitialDelayMaxValue().getValue() == 0.1
        assert behavior.getInitialDelayMinValue().getValue() == 0.01
        assert behavior.getInitialRepetitionsBaseDelay().getValue() == 0.05
        assert behavior.getInitialRepetitionsMax().getValue() == 3
