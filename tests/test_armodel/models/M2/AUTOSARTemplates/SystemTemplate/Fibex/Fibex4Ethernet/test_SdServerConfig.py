import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    InitialSdDelayConfig,
    RequestResponseDelay,
    SdServerConfig,
    TagWithOptionalValue,
)

CLASS_NOTE = """Server configuration for Service-Discovery."""


class TestSdServerConfig:
    """Test cases for SdServerConfig (R4.3.1 Table 6.171, p.355)."""

    def test_initialization_defaults(self):
        obj = SdServerConfig()
        assert obj.getCapabilityRecords() == []
        assert obj.getInitialOfferBehavior() is None
        assert obj.getOfferCyclicDelay() is None
        assert obj.getRequestResponseDelay() is None
        assert obj.getServerServiceMajorVersion() is None
        assert obj.getServerServiceMinorVersion() is None
        assert obj.getTtl() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = SdServerConfig()
        record = TagWithOptionalValue()
        assert obj.addCapabilityRecord(record) is obj
        assert obj.getCapabilityRecords() == [record]
        obj.addCapabilityRecord(None)
        assert len(obj.getCapabilityRecords()) == 1
        item = InitialSdDelayConfig()
        assert obj.setInitialOfferBehavior(item) is obj
        assert obj.getInitialOfferBehavior() is item
        obj.setInitialOfferBehavior(None)
        assert obj.getInitialOfferBehavior() is item
        delay = RequestResponseDelay()
        assert obj.setRequestResponseDelay(delay) is obj
        assert obj.getRequestResponseDelay() is delay
        assert obj.setOfferCyclicDelay(2.0) is obj
        assert obj.getOfferCyclicDelay() == 2.0
        assert obj.setServerServiceMajorVersion(1) is obj
        assert obj.getServerServiceMajorVersion() == 1
        assert obj.setServerServiceMinorVersion(2) is obj
        assert obj.getServerServiceMinorVersion() == 2
        assert obj.setTtl(10) is obj
        assert obj.getTtl() == 10

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SdServerConfig.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = SdServerConfig()
        assert (
            inspect.cleandoc(obj.getCapabilityRecords.__doc__)
            == "A sequence of records to store arbitrary name/value pairs conveying additional information about the named service. Capability records shall only be existing if the respective SdServerConfig is composed by a ProvidedServiceInstance (see constr_3259)."
        )
        assert inspect.cleandoc(obj.getInitialOfferBehavior.__doc__) == "Controls offer behavior of the server."
        assert inspect.cleandoc(obj.setInitialOfferBehavior.__doc__).split("\n")[0] == "Controls offer behavior of the server."
        assert inspect.cleandoc(obj.getOfferCyclicDelay.__doc__) == "Optional attribute to define cyclic offers. Cyclic offer is active, if the delay is set (in seconds)."
        assert inspect.cleandoc(obj.setOfferCyclicDelay.__doc__).split("\n")[0] == "Optional attribute to define cyclic offers. Cyclic offer is active, if the delay is set (in seconds)."
        assert inspect.cleandoc(obj.getRequestResponseDelay.__doc__) == "Maximum/Minimum allowable response delay to entries received by multicast in seconds."
        assert inspect.cleandoc(obj.setRequestResponseDelay.__doc__).split("\n")[0] == "Maximum/Minimum allowable response delay to entries received by multicast in seconds."
        assert inspect.cleandoc(obj.getServerServiceMajorVersion.__doc__) == "Major version number of the Service."
        assert inspect.cleandoc(obj.setServerServiceMajorVersion.__doc__).split("\n")[0] == "Major version number of the Service."
        assert inspect.cleandoc(obj.getServerServiceMinorVersion.__doc__) == "Minor version number of the Service."
        assert inspect.cleandoc(obj.setServerServiceMinorVersion.__doc__).split("\n")[0] == "Minor version number of the Service."
        assert inspect.cleandoc(obj.getTtl.__doc__) == "Time to live. Shall be a positive value (sInt32)."
        assert inspect.cleandoc(obj.setTtl.__doc__).split("\n")[0] == "Time to live. Shall be a positive value (sInt32)."
