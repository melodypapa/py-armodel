"""Reader tests for SdServerConfig (R4.3.1 AUTOSAR_TPS_SystemTemplate, Table 6.171, p.355).

SdServerConfig has no standalone XML element: it is read inline from its aggregators
(ProvidedServiceInstance.sdServerConfig and EventHandler.sdServerConfig) through the
shared ``getSdServerConfig`` helper. XSD group ``SD-SERVER-CONFIG`` (AUTOSAR_00044.xsd
l.72991) element order: CAPABILITY-RECORDS, INITIAL-OFFER-BEHAVIOR, OFFER-CYCLIC-DELAY,
REQUEST-RESPONSE-DELAY, SERVER-SERVICE-MAJOR-VERSION, SERVER-SERVICE-MINOR-VERSION, TTL.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import SdServerConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import EventHandler, InitialSdDelayConfig, RequestResponseDelay
from tests.test_armodel.parser._helpers import _snip

SEVEN_ATTRIBUTES = (
    "<CAPABILITY-RECORDS>"
    "<TAG-WITH-OPTIONAL-VALUE><KEY>PlugIns</KEY><VALUE>JPEG,MPEG2</VALUE></TAG-WITH-OPTIONAL-VALUE>"
    "<TAG-WITH-OPTIONAL-VALUE><KEY>passreq</KEY></TAG-WITH-OPTIONAL-VALUE>"
    "</CAPABILITY-RECORDS>"
    "<INITIAL-OFFER-BEHAVIOR><INITIAL-DELAY-MAX-VALUE>0.1</INITIAL-DELAY-MAX-VALUE><INITIAL-REPETITIONS-MAX>3</INITIAL-REPETITIONS-MAX></INITIAL-OFFER-BEHAVIOR>"
    "<OFFER-CYCLIC-DELAY>2.0</OFFER-CYCLIC-DELAY>"
    "<REQUEST-RESPONSE-DELAY><MAX-VALUE>0.5</MAX-VALUE><MIN-VALUE>0.05</MIN-VALUE></REQUEST-RESPONSE-DELAY>"
    "<SERVER-SERVICE-MAJOR-VERSION>1</SERVER-SERVICE-MAJOR-VERSION>"
    "<SERVER-SERVICE-MINOR-VERSION>2</SERVER-SERVICE-MINOR-VERSION>"
    "<TTL>10</TTL>"
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSdServerConfigReader:
    def test_reads_all_seven_attributes(self, parser):
        element = _snip("<SD-SERVER-CONFIG>%s</SD-SERVER-CONFIG>" % SEVEN_ATTRIBUTES)
        config = parser.getSdServerConfig(element, "SD-SERVER-CONFIG")

        assert isinstance(config, SdServerConfig)
        records = config.getCapabilityRecords()
        assert len(records) == 2
        assert isinstance(records[0], TagWithOptionalValue)
        assert records[0].getKey().getValue() == "PlugIns"
        assert records[0].getValue().getValue() == "JPEG,MPEG2"
        assert records[1].getKey().getValue() == "passreq"
        assert records[1].getValue() is None
        behavior = config.getInitialOfferBehavior()
        assert isinstance(behavior, InitialSdDelayConfig)
        assert behavior.getInitialDelayMaxValue().getValue() == 0.1
        assert behavior.getInitialRepetitionsMax().getValue() == 3
        assert config.getOfferCyclicDelay().getValue() == 2.0
        delay = config.getRequestResponseDelay()
        assert isinstance(delay, RequestResponseDelay)
        assert delay.getMaxValue().getValue() == 0.5
        assert delay.getMinValue().getValue() == 0.05
        assert config.getServerServiceMajorVersion().getValue() == 1
        assert config.getServerServiceMinorVersion().getValue() == 2
        assert config.getTtl().getValue() == 10

    def test_absent_element_returns_none(self, parser):
        element = _snip("<OTHER/>")
        assert parser.getSdServerConfig(element, "SD-SERVER-CONFIG") is None

    def test_empty_element_leaves_all_defaults(self, parser):
        element = _snip("<SD-SERVER-CONFIG/>")
        config = parser.getSdServerConfig(element, "SD-SERVER-CONFIG")

        assert isinstance(config, SdServerConfig)
        assert config.getCapabilityRecords() == []
        assert config.getInitialOfferBehavior() is None
        assert config.getOfferCyclicDelay() is None
        assert config.getRequestResponseDelay() is None
        assert config.getServerServiceMajorVersion() is None
        assert config.getServerServiceMinorVersion() is None
        assert config.getTtl() is None

    def test_event_handler_aggregator_reads_all_seven_attributes(self, parser):
        handler = EventHandler(MockParent(), "MyHandler")
        element = _snip("<SHORT-NAME>MyHandler</SHORT-NAME><SD-SERVER-CONFIG>%s</SD-SERVER-CONFIG>" % SEVEN_ATTRIBUTES, root_tag="EVENT-HANDLER")
        parser.readEventHandler(element, handler)

        config = handler.getSdServerConfig()
        assert isinstance(config, SdServerConfig)
        records = config.getCapabilityRecords()
        assert len(records) == 2
        assert records[1].getKey().getValue() == "passreq"
        assert config.getInitialOfferBehavior().getInitialDelayMaxValue().getValue() == 0.1
        assert config.getOfferCyclicDelay().getValue() == 2.0
        assert config.getRequestResponseDelay().getMinValue().getValue() == 0.05
        assert config.getServerServiceMajorVersion().getValue() == 1
        assert config.getServerServiceMinorVersion().getValue() == 2
        assert config.getTtl().getValue() == 10
