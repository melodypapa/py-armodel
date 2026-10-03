import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import SdClientConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import InitialSdDelayConfig

CLASS_NOTE = """This element is used to configure the offer behavior of the server and the find behavior on the client."""

SPEC_MODULE = "armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances"


class TestInitialSdDelayConfig:
    """Test cases for InitialSdDelayConfig (Table 6.170, p.514)."""

    def test_defined_in_spec_package(self):
        assert InitialSdDelayConfig.__module__ == SPEC_MODULE

    def test_initialization(self):
        obj = InitialSdDelayConfig()
        assert obj.getInitialDelayMaxValue() is None
        assert obj.getInitialDelayMinValue() is None
        assert obj.getInitialRepetitionsBaseDelay() is None
        assert obj.getInitialRepetitionsMax() is None

    def test_get_set_initialDelayMaxValue(self):
        obj = InitialSdDelayConfig()
        value = TimeValue()
        assert obj.setInitialDelayMaxValue(value) is obj
        assert obj.getInitialDelayMaxValue() is value
        obj.setInitialDelayMaxValue(None)
        assert obj.getInitialDelayMaxValue() is value

    def test_get_set_initialDelayMinValue(self):
        obj = InitialSdDelayConfig()
        value = TimeValue()
        assert obj.setInitialDelayMinValue(value) is obj
        assert obj.getInitialDelayMinValue() is value
        obj.setInitialDelayMinValue(None)
        assert obj.getInitialDelayMinValue() is value

    def test_get_set_initialRepetitionsBaseDelay(self):
        obj = InitialSdDelayConfig()
        value = TimeValue()
        assert obj.setInitialRepetitionsBaseDelay(value) is obj
        assert obj.getInitialRepetitionsBaseDelay() is value
        obj.setInitialRepetitionsBaseDelay(None)
        assert obj.getInitialRepetitionsBaseDelay() is value

    def test_get_set_initialRepetitionsMax(self):
        obj = InitialSdDelayConfig()
        value = PositiveInteger()
        value.setValue("3")
        assert obj.setInitialRepetitionsMax(value) is obj
        assert obj.getInitialRepetitionsMax() is value
        obj.setInitialRepetitionsMax(None)
        assert obj.getInitialRepetitionsMax() is value

    def test_class_docstring_note(self):
        assert inspect.cleandoc(InitialSdDelayConfig.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_type_hints_resolve(self):
        hints = typing.get_type_hints(InitialSdDelayConfig.getInitialDelayMaxValue)
        assert hints["return"] == typing.Optional[TimeValue]
        hints = typing.get_type_hints(InitialSdDelayConfig.setInitialDelayMaxValue)
        assert hints["value"] == typing.Optional[TimeValue]
        assert hints["return"] is InitialSdDelayConfig
        hints = typing.get_type_hints(InitialSdDelayConfig.getInitialDelayMinValue)
        assert hints["return"] == typing.Optional[TimeValue]
        hints = typing.get_type_hints(InitialSdDelayConfig.setInitialDelayMinValue)
        assert hints["value"] == typing.Optional[TimeValue]
        hints = typing.get_type_hints(InitialSdDelayConfig.getInitialRepetitionsBaseDelay)
        assert hints["return"] == typing.Optional[TimeValue]
        hints = typing.get_type_hints(InitialSdDelayConfig.setInitialRepetitionsBaseDelay)
        assert hints["value"] == typing.Optional[TimeValue]
        hints = typing.get_type_hints(InitialSdDelayConfig.getInitialRepetitionsMax)
        assert hints["return"] == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(InitialSdDelayConfig.setInitialRepetitionsMax)
        assert hints["value"] == typing.Optional[PositiveInteger]

    def test_aggregator_annotation_still_resolves_after_relocation(self):
        # Rule 0003: the name must exist in the defining module's RUNTIME globals, not only under
        # TYPE_CHECKING -- a TYPE_CHECKING-only import breaks typing.get_type_hints on Python 3.8.
        hints = typing.get_type_hints(SdClientConfig.getInitialFindBehavior)
        assert hints["return"] == typing.Optional[InitialSdDelayConfig]
        hints = typing.get_type_hints(SdClientConfig.setInitialFindBehavior)
        assert hints["value"] == typing.Optional[InitialSdDelayConfig]
        assert hints["return"] is SdClientConfig

    def test_accessor_docstrings_verbatim(self):
        obj = InitialSdDelayConfig()
        assert (
            inspect.cleandoc(obj.getInitialDelayMaxValue.__doc__)
            == "Max Value in seconds to delay randomly the first offer (if aggregated by SdServerConfig) or the transmission of a find message (if aggregated by SdClientConfig)."
        )
        assert (
            inspect.cleandoc(obj.setInitialDelayMaxValue.__doc__).split("\n")[0]
            == "Max Value in seconds to delay randomly the first offer (if aggregated by SdServerConfig) or the transmission of a find message (if aggregated by SdClientConfig)."
        )
        assert (
            inspect.cleandoc(obj.getInitialDelayMinValue.__doc__) == "Min Value in seconds to delay randomly the first offer or the transmission of a find message (if aggregated by Sd ClientConfig)."
        )
        assert (
            inspect.cleandoc(obj.setInitialDelayMinValue.__doc__).split("\n")[0]
            == "Min Value in seconds to delay randomly the first offer or the transmission of a find message (if aggregated by Sd ClientConfig)."
        )
        assert (
            inspect.cleandoc(obj.getInitialRepetitionsBaseDelay.__doc__)
            == "The base delay for offer repetitions (if aggregated by Sd ServerConfig) or find repetitions (if aggregated by Sd ClientConfig). Successive find messages have an exponential back off delay."
        )
        assert (
            inspect.cleandoc(obj.setInitialRepetitionsBaseDelay.__doc__).split("\n")[0]
            == "The base delay for offer repetitions (if aggregated by Sd ServerConfig) or find repetitions (if aggregated by Sd ClientConfig). Successive find messages have an exponential back off delay."
        )
        assert (
            inspect.cleandoc(obj.getInitialRepetitionsMax.__doc__)
            == "Describes the maximum amount of offer repetitions (if aggregated by SdServerConfig) or the maximum amount of find repetitions (if aggregated by SdClientConfig)."
        )
        assert (
            inspect.cleandoc(obj.setInitialRepetitionsMax.__doc__).split("\n")[0]
            == "Describes the maximum amount of offer repetitions (if aggregated by SdServerConfig) or the maximum amount of find repetitions (if aggregated by SdClientConfig)."
        )
