"""Model tests for EthernetWakeupSleepOnDatalineConfig (R23-11 CP_TPS_SystemTemplate, Table 3.115, p.159)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetWakeupSleepOnDatalineConfig,
)

CLASS_NOTE = (
    "EthernetWakeupSleepOnDatalineConfigSet is the main element that aggregates different config set regarding the wakeup and sleep on data line. "
    "An EthernetWakeupSleepOnDatalineConfigSet could aggregate multiple different configurations regarding the wakeup and sleep on dataline (EthernetWakeupSleepOnDatalineConfig)."
)

CLASS_DOCSTRING = (
    CLASS_NOTE
    + """

[constr_3601] Mandatory attributes of EthernetWakeupSleepOnDatalineConfig: The following attributes of EthernetWakeupSleepOnDatalineConfig shall be defined at the time when the Ecu Extract is complete:
- wakeupLocalEnabled
- wakeupRemoteEnabled"""
)

MEMBER_NOTES = {
    "sleepModeExecutionDelay": "Delay in seconds to perform a sleep request if the Ethernet hardware (PHY) detect a pending wake-up. This is used to avoid the race condition, if a sleep was requested while a wake-up of a neighboring PHY was received via a local wake-up connection (e.g. I/O pin).",
    "sleepRepetitionDelayOfSleepRequest": "Delay in seconds for a repetition of a sleep request. This is used to retry a synchronized shutdown of the connected Ethernet hardware (PHY) of the link partner. (see constr_3607).",
    "sleepRepetitionsOfSleepRequest": "Count of repetitions for a sleep on dataline. If a sleep is rejected by the linked communication partner, the sleep is repeated until the count of repetitions exceed. If count of repetitions exceed, the Ethernet hardware (PHY) transit to sleep without acknowledgement of the connected link partner.",
    "wakeupForwardLocalEnabled": "If enabled, then a remote wake-up received on the physical dataline (e.g. 100BASE-T1) is forwarded as local wake-up (e.g. via an I/O pin). If disabled, then a remote wake-up is not forwarded as local wake-up. (see constr_3602).",
    "wakeupForwardRemoteEnabled": "If enabled, then a local wake-up is forwarded to the physical dataline (e.g. 100BASE-T1). If disabled, then a local wake-up is not forwarded to the physical dataline. (see constr_3604).",
    "wakeupLocalDetectionTime": "Specify the detection time if a local wake-up in seconds is present on the local wake-up connection (e.g. I/O pin). A local wake-up has to be present at least for wakeupLocalDetectionTime to be detected a valid local wake-up. (see constr_3605, constr_3606, constr_3610).",
    "wakeupLocalDurationTime": "Specify the duration of a local wake-up in seconds to be present on the local wake-up connection (e.g. I/O pin). (see constr_3603, constr_3606, constr_3609).",
    "wakeupLocalEnabled": "If enabled, then a local wake-up received via a local connection (e.g. I/O pin) shall be detected by the Ethernet hardware (PHY). If disabled, Ethernet hardware is not reacting on a local wake-up.",
    "wakeupRemoteEnabled": "If enabled, then a remote wake-up received via the physical dataline (e.g. 100BASE-T1) shall be detected by the Ethernet hardware (PHY). If disabled, Ethernet hardware is not reaction on a remote wake-up.",
    "wakeupRepetitionDelayOfWakeupRequest": "Delay in seconds for a repetition of a wake-up. This is used to increase the reliability in the network, such that an ECU which initiates the wake-up does repeat the wake-up and increase the probability that affected ECUs receive the wake-up. (see constr_3608).",
    "wakeupRepetitionsOfWakeupRequest": "Count of repetitions for a wake-up. This is used to increase the reliability in the network, such that an ECU which initiates the wake-up does repeat the wake-up and increase the probability that affected ECUs receive the wake-up.",
}

MEMBERS = [
    "sleepModeExecutionDelay",
    "sleepRepetitionDelayOfSleepRequest",
    "sleepRepetitionsOfSleepRequest",
    "wakeupForwardLocalEnabled",
    "wakeupForwardRemoteEnabled",
    "wakeupLocalDetectionTime",
    "wakeupLocalDurationTime",
    "wakeupLocalEnabled",
    "wakeupRemoteEnabled",
    "wakeupRepetitionDelayOfWakeupRequest",
    "wakeupRepetitionsOfWakeupRequest",
]


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestEthernetWakeupSleepOnDatalineConfig:
    """Spec-sync tests for EthernetWakeupSleepOnDatalineConfig (Table 3.115, p.159)."""

    def _make(self) -> EthernetWakeupSleepOnDatalineConfig:
        return EthernetWakeupSleepOnDatalineConfig(MockParent(), "WSD_CFG")

    def _value(self, member):
        if member in ("sleepRepetitionsOfSleepRequest", "wakeupRepetitionsOfWakeupRequest"):
            value = PositiveInteger()
            value.setValue("4")
            return value
        if member in ("wakeupForwardLocalEnabled", "wakeupForwardRemoteEnabled", "wakeupLocalEnabled", "wakeupRemoteEnabled"):
            value = Boolean()
            value.setValue("true")
            return value
        value = TimeValue()
        value.setValue("0.05")
        return value

    def test_inheritance(self):
        assert issubclass(EthernetWakeupSleepOnDatalineConfig, Identifiable)
        assert issubclass(EthernetWakeupSleepOnDatalineConfig, ARObject)

    def test_initialization_defaults(self):
        obj = self._make()
        for member in MEMBERS:
            assert getattr(obj, "get%s%s" % (member[0].upper(), member[1:]))() is None

    def test_get_set_round_trip_and_none_noop(self):
        obj = self._make()
        for member in MEMBERS:
            getter = getattr(obj, "get%s%s" % (member[0].upper(), member[1:]))
            setter = getattr(obj, "set%s%s" % (member[0].upper(), member[1:]))
            value = self._value(member)
            assert setter(value) is obj
            assert getter() is value
            setter(None)
            assert getter() is value

    def test_member_order_matches_spec(self):
        source = inspect.getsource(EthernetWakeupSleepOnDatalineConfig.__init__)
        indexes = [source.index("self.%s:" % member) for member in MEMBERS]
        assert indexes == sorted(indexes)

    def test_class_docstring_is_spec_note_with_constraints(self):
        assert inspect.cleandoc(EthernetWakeupSleepOnDatalineConfig.__doc__) == CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert EthernetWakeupSleepOnDatalineConfig.__init__.__doc__ is None

    def test_accessor_docstrings_are_spec_notes(self):
        obj = self._make()
        for member in MEMBERS:
            getter = getattr(obj, "get%s%s" % (member[0].upper(), member[1:]))
            setter = getattr(obj, "set%s%s" % (member[0].upper(), member[1:]))
            noop = "A None value is a no-op and does not overwrite an existing %s." % member
            assert getter.__doc__.strip() == MEMBER_NOTES[member], member
            assert inspect.cleandoc(setter.__doc__).strip() == MEMBER_NOTES[member] + "\n\n" + noop, member
