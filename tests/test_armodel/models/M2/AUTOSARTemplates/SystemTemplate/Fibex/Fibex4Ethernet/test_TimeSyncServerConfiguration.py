import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSyncServerConfiguration,
    TimeSyncTechnologyEnum,
)

CLASS_NOTE = "Defines the configuration of the time synchronisation server."

PRIORITY_NOTE = "Server Priority."
SYNC_INTERVAL_NOTE = "Synchronisation interval used by the time synchronisation server (in seconds)."
SERVER_IDENTIFIER_NOTE = "Identifier of the TimeSyncServer."
TECHNOLOGY_NOTE = "Defines the time synchronisation technology used. Possible values are: NTP_RFC958, PTP_ IEEE1588_2002, PTP_IEEE1588_2008, AVB_ IEEE802_1AS and others."


class TestTimeSyncServerConfiguration:
    """Test cases for TimeSyncServerConfiguration (Table 6.147, p.470)."""

    def _obj(self):
        return TimeSyncServerConfiguration(None, "Obj")

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getPriority() is None
        assert obj.getSyncInterval() is None
        assert obj.getTimeSyncServerIdentifier() is None
        assert obj.getTimeSyncTechnology() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()

        priority = PositiveInteger()
        priority.setValue("7")
        assert obj.setPriority(priority) is obj
        assert obj.getPriority() is priority
        obj.setPriority(None)
        assert obj.getPriority() is priority

        interval = TimeValue()
        interval.setValue("1.0")
        assert obj.setSyncInterval(interval) is obj
        assert obj.getSyncInterval() is interval
        obj.setSyncInterval(None)
        assert obj.getSyncInterval() is interval

        identifier = String()
        identifier.setValue("srv-1")
        assert obj.setTimeSyncServerIdentifier(identifier) is obj
        assert obj.getTimeSyncServerIdentifier() is identifier
        obj.setTimeSyncServerIdentifier(None)
        assert obj.getTimeSyncServerIdentifier() is identifier

        technology = TimeSyncTechnologyEnum()
        technology.setValue(TimeSyncTechnologyEnum.NTP_RFC958)
        assert obj.setTimeSyncTechnology(technology) is obj
        assert obj.getTimeSyncTechnology() is technology
        obj.setTimeSyncTechnology(None)
        assert obj.getTimeSyncTechnology() is technology

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TimeSyncServerConfiguration.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getPriority.__doc__) == PRIORITY_NOTE
        assert inspect.cleandoc(obj.setPriority.__doc__).split("\n")[0] == PRIORITY_NOTE
        assert inspect.cleandoc(obj.getSyncInterval.__doc__) == SYNC_INTERVAL_NOTE
        assert inspect.cleandoc(obj.setSyncInterval.__doc__).split("\n")[0] == SYNC_INTERVAL_NOTE
        assert inspect.cleandoc(obj.getTimeSyncServerIdentifier.__doc__) == SERVER_IDENTIFIER_NOTE
        assert inspect.cleandoc(obj.setTimeSyncServerIdentifier.__doc__).split("\n")[0] == SERVER_IDENTIFIER_NOTE
        assert inspect.cleandoc(obj.getTimeSyncTechnology.__doc__) == TECHNOLOGY_NOTE
        assert inspect.cleandoc(obj.setTimeSyncTechnology.__doc__).split("\n")[0] == TECHNOLOGY_NOTE

    def test_scalar_pair_order_getter_first(self):
        source = inspect.getsource(TimeSyncServerConfiguration)
        for getter, setter in (
            ("getPriority", "setPriority"),
            ("getSyncInterval", "setSyncInterval"),
            ("getTimeSyncServerIdentifier", "setTimeSyncServerIdentifier"),
            ("getTimeSyncTechnology", "setTimeSyncTechnology"),
        ):
            assert source.index("def %s" % getter) < source.index("def %s" % setter), "%s must precede %s" % (getter, setter)
