import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import InitialSdDelayConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import InitialSdDelayConfig as CanonicalViaServiceInstances

CLASS_NOTE = """This element is used to configure the offer behavior of the server and the find behavior on the client."""


class TestInitialSdDelayConfig:
    """Test cases for InitialSdDelayConfig (Table 6.170, p.514)."""

    def test_single_canonical_class(self):
        assert InitialSdDelayConfig is CanonicalViaServiceInstances

    def test_initialization_defaults(self):
        obj = InitialSdDelayConfig()
        assert obj.getInitialDelayMaxValue() is None
        assert obj.getInitialDelayMinValue() is None
        assert obj.getInitialRepetitionsBaseDelay() is None
        assert obj.getInitialRepetitionsMax() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = InitialSdDelayConfig()
        item = TimeValue()
        assert obj.setInitialDelayMaxValue(item) is obj
        assert obj.getInitialDelayMaxValue() is item
        obj.setInitialDelayMaxValue(None)
        assert obj.getInitialDelayMaxValue() is item
        item = TimeValue()
        assert obj.setInitialDelayMinValue(item) is obj
        assert obj.getInitialDelayMinValue() is item
        obj.setInitialDelayMinValue(None)
        assert obj.getInitialDelayMinValue() is item
        item = TimeValue()
        assert obj.setInitialRepetitionsBaseDelay(item) is obj
        assert obj.getInitialRepetitionsBaseDelay() is item
        obj.setInitialRepetitionsBaseDelay(None)
        assert obj.getInitialRepetitionsBaseDelay() is item
        assert obj.setInitialRepetitionsMax(3) is obj
        assert obj.getInitialRepetitionsMax() == 3
        obj.setInitialRepetitionsMax(None)
        assert obj.getInitialRepetitionsMax() == 3

    def test_class_docstring_note(self):
        assert inspect.cleandoc(InitialSdDelayConfig.__doc__).split("\n\n")[0] == CLASS_NOTE

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
