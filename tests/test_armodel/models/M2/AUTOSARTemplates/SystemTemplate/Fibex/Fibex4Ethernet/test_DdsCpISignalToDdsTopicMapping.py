import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import DdsCpISignalToDdsTopicMapping

CLASS_NOTE = "Mapping of an ISignal to a DdsTopic. Tags: atp.Status=candidate"

DDS_TOPIC_NOTE = "Reference to the DdsTopic. Tags: atp.Status=candidate"
I_SIGNAL_NOTE = "Reference to the ISignal. Tags: atp.Status=candidate"


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestDdsCpISignalToDdsTopicMapping:
    """Test cases for DdsCpISignalToDdsTopicMapping (Table 5.53, p.293)."""

    def test_initialization_defaults(self):
        mapping = DdsCpISignalToDdsTopicMapping()
        assert mapping.getDdsTopicRef() is None
        assert mapping.getISignalRef() is None

    def test_get_set_round_trip_and_none_noop(self):
        mapping = DdsCpISignalToDdsTopicMapping()

        topic_ref = _ref("/Dds/Topic", "DDS-CP-TOPIC")
        assert mapping.setDdsTopicRef(topic_ref) is mapping
        assert mapping.getDdsTopicRef() is topic_ref
        mapping.setDdsTopicRef(None)
        assert mapping.getDdsTopicRef() is topic_ref

        signal_ref = _ref("/ISignals/Signal", "I-SIGNAL")
        assert mapping.setISignalRef(signal_ref) is mapping
        assert mapping.getISignalRef() is signal_ref
        mapping.setISignalRef(None)
        assert mapping.getISignalRef() is signal_ref

    def test_class_docstring_note(self):
        assert inspect.cleandoc(DdsCpISignalToDdsTopicMapping.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        mapping = DdsCpISignalToDdsTopicMapping()
        assert inspect.cleandoc(mapping.getDdsTopicRef.__doc__) == DDS_TOPIC_NOTE
        assert inspect.cleandoc(mapping.setDdsTopicRef.__doc__).splitlines()[0] == DDS_TOPIC_NOTE
        assert inspect.cleandoc(mapping.getISignalRef.__doc__) == I_SIGNAL_NOTE
        assert inspect.cleandoc(mapping.setISignalRef.__doc__).splitlines()[0] == I_SIGNAL_NOTE
