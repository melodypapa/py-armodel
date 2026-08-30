import pytest

from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSLLET import (
    TDEventSLLET,
    TDEventSLLETPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class _ConcreteTDEventSLLET(TDEventSLLET):
    pass


class TestTDEventSLLET:
    def test_abstract_instantiation(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError) as err:
            TDEventSLLET(ar_root, "tdEventSLLET")
        assert str(err.value) == "TDEventSLLET is an abstract class."

    def test_base_is_timing_description_event(self):
        assert issubclass(TDEventSLLET, TimingDescriptionEvent)

    def test_construct_via_concrete_subclass(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = _ConcreteTDEventSLLET(ar_root, "SLLET1")
        assert event is not None
        assert event.short_name == "SLLET1"


class TestTDEventSLLETPort:
    def test_construct(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventSLLETPort(ar_root, "SLLETPort1")
        assert event is not None
        assert event.short_name == "SLLETPort1"

    def test_base_is_tdevent_sllet(self):
        assert issubclass(TDEventSLLETPort, TDEventSLLET)

    def test_initialization_default(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventSLLETPort(ar_root, "SLLETPort1")
        assert event.getPortRef() is None

    def test_get_set_port_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventSLLETPort(ar_root, "SLLETPort1")
        ref = RefType()
        ref.setDest("PORT-PROTOTYPE")
        ref.setValue("/Path/To/Port")
        event.setPortRef(ref)
        assert event.getPortRef() is ref
        assert event.getPortRef().getValue() == "/Path/To/Port"

    def test_set_port_ref_none_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventSLLETPort(ar_root, "SLLETPort1")
        ref = RefType()
        ref.setDest("PORT-PROTOTYPE")
        ref.setValue("/Path/To/Port")
        event.setPortRef(ref)
        event.setPortRef(None)
        assert event.getPortRef() is ref
