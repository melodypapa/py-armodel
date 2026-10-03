import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet import ServiceInstances
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import SdServerConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventHandler,
    InitialSdDelayConfig,
    RequestResponseDelay,
)

CLASS_NOTE = """Server configuration for Service-Discovery."""

SPEC_MODULE = "armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology"


class TestSdServerConfig:
    """Test cases for SdServerConfig (R4.3.1 Table 6.171, p.355)."""

    def test_defined_in_spec_package(self):
        assert SdServerConfig.__module__ == SPEC_MODULE

    def test_initialization_defaults(self):
        obj = SdServerConfig()
        assert obj.getCapabilityRecords() == []
        assert obj.getInitialOfferBehavior() is None
        assert obj.getOfferCyclicDelay() is None
        assert obj.getRequestResponseDelay() is None
        assert obj.getServerServiceMajorVersion() is None
        assert obj.getServerServiceMinorVersion() is None
        assert obj.getTtl() is None

    def test_get_set_capabilityRecord(self):
        obj = SdServerConfig()
        record = TagWithOptionalValue()
        assert obj.addCapabilityRecord(record) is obj
        assert obj.getCapabilityRecords() == [record]
        obj.addCapabilityRecord(None)
        assert obj.getCapabilityRecords() == [record]

    def test_get_set_initialOfferBehavior(self):
        obj = SdServerConfig()
        value = InitialSdDelayConfig()
        assert obj.setInitialOfferBehavior(value) is obj
        assert obj.getInitialOfferBehavior() is value
        obj.setInitialOfferBehavior(None)
        assert obj.getInitialOfferBehavior() is value

    def test_get_set_offerCyclicDelay(self):
        obj = SdServerConfig()
        value = TimeValue().setValue("2.0")
        assert obj.setOfferCyclicDelay(value) is obj
        assert obj.getOfferCyclicDelay() is value
        obj.setOfferCyclicDelay(None)
        assert obj.getOfferCyclicDelay() is value

    def test_get_set_requestResponseDelay(self):
        obj = SdServerConfig()
        value = RequestResponseDelay()
        assert obj.setRequestResponseDelay(value) is obj
        assert obj.getRequestResponseDelay() is value
        obj.setRequestResponseDelay(None)
        assert obj.getRequestResponseDelay() is value

    def test_get_set_serverServiceMajorVersion(self):
        obj = SdServerConfig()
        value = PositiveInteger().setValue("1")
        assert obj.setServerServiceMajorVersion(value) is obj
        assert obj.getServerServiceMajorVersion() is value
        obj.setServerServiceMajorVersion(None)
        assert obj.getServerServiceMajorVersion() is value

    def test_get_set_serverServiceMinorVersion(self):
        obj = SdServerConfig()
        value = PositiveInteger().setValue("2")
        assert obj.setServerServiceMinorVersion(value) is obj
        assert obj.getServerServiceMinorVersion() is value
        obj.setServerServiceMinorVersion(None)
        assert obj.getServerServiceMinorVersion() is value

    def test_get_set_ttl(self):
        obj = SdServerConfig()
        value = PositiveInteger().setValue("10")
        assert obj.setTtl(value) is obj
        assert obj.getTtl() is value
        obj.setTtl(None)
        assert obj.getTtl() is value

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

    def test_accessor_type_hints_resolve(self):
        hints = typing.get_type_hints(SdServerConfig.getCapabilityRecords)
        assert hints["return"] == typing.List[TagWithOptionalValue]
        hints = typing.get_type_hints(SdServerConfig.addCapabilityRecord)
        assert hints["value"] == typing.Optional[TagWithOptionalValue]
        assert hints["return"] is SdServerConfig
        hints = typing.get_type_hints(SdServerConfig.getInitialOfferBehavior)
        assert hints["return"] == typing.Optional[InitialSdDelayConfig]
        hints = typing.get_type_hints(SdServerConfig.setInitialOfferBehavior)
        assert hints["value"] == typing.Optional[InitialSdDelayConfig]
        assert hints["return"] is SdServerConfig
        hints = typing.get_type_hints(SdServerConfig.getOfferCyclicDelay)
        assert hints["return"] == typing.Optional[TimeValue]
        hints = typing.get_type_hints(SdServerConfig.setOfferCyclicDelay)
        assert hints["value"] == typing.Optional[TimeValue]
        assert hints["return"] is SdServerConfig
        hints = typing.get_type_hints(SdServerConfig.getRequestResponseDelay)
        assert hints["return"] == typing.Optional[RequestResponseDelay]
        hints = typing.get_type_hints(SdServerConfig.setRequestResponseDelay)
        assert hints["value"] == typing.Optional[RequestResponseDelay]
        assert hints["return"] is SdServerConfig
        hints = typing.get_type_hints(SdServerConfig.getServerServiceMajorVersion)
        assert hints["return"] == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(SdServerConfig.setServerServiceMajorVersion)
        assert hints["value"] == typing.Optional[PositiveInteger]
        assert hints["return"] is SdServerConfig
        hints = typing.get_type_hints(SdServerConfig.getServerServiceMinorVersion)
        assert hints["return"] == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(SdServerConfig.setServerServiceMinorVersion)
        assert hints["value"] == typing.Optional[PositiveInteger]
        assert hints["return"] is SdServerConfig
        hints = typing.get_type_hints(SdServerConfig.getTtl)
        assert hints["return"] == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(SdServerConfig.setTtl)
        assert hints["value"] == typing.Optional[PositiveInteger]
        assert hints["return"] is SdServerConfig

    def test_aggregator_annotation_still_resolves_after_relocation(self):
        # Rule 0003: the name must exist in the defining module's RUNTIME globals, not only under
        # TYPE_CHECKING -- a TYPE_CHECKING-only import breaks typing.get_type_hints on Python 3.8.
        hints = typing.get_type_hints(EventHandler.getSdServerConfig)
        assert hints["return"] == typing.Optional[SdServerConfig]
        hints = typing.get_type_hints(EventHandler.setSdServerConfig)
        assert hints["value"] == typing.Optional[SdServerConfig]
        assert hints["return"] is EventHandler
        assert ServiceInstances.SdServerConfig is SdServerConfig

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
