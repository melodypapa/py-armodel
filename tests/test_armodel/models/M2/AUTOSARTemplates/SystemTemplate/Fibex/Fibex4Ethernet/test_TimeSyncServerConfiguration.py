import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSyncServerConfiguration,
    TimeSyncTechnologyEnum,
)

CLASS_NOTE = """Defines the configuration of the time synchronisation server."""


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
        assert obj.setPriority(7) is obj
        assert obj.getPriority() == 7
        obj.setPriority(None)
        assert obj.getPriority() == 7
        item = TimeValue()
        assert obj.setSyncInterval(item) is obj
        assert obj.getSyncInterval() is item
        obj.setSyncInterval(None)
        assert obj.getSyncInterval() is item
        assert obj.setTimeSyncServerIdentifier("x") is obj
        assert obj.getTimeSyncServerIdentifier() == "x"
        obj.setTimeSyncServerIdentifier(None)
        assert obj.getTimeSyncServerIdentifier() == "x"
        item = TimeSyncTechnologyEnum()
        assert obj.setTimeSyncTechnology(item) is obj
        assert obj.getTimeSyncTechnology() is item
        obj.setTimeSyncTechnology(None)
        assert obj.getTimeSyncTechnology() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TimeSyncServerConfiguration.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getPriority.__doc__) == "Server Priority."
        assert inspect.cleandoc(obj.setPriority.__doc__).split("\n")[0] == "Server Priority."
        assert inspect.cleandoc(obj.getSyncInterval.__doc__) == "Synchronisation interval used by the time synchronisation server (in seconds)."
        assert inspect.cleandoc(obj.setSyncInterval.__doc__).split("\n")[0] == "Synchronisation interval used by the time synchronisation server (in seconds)."
        assert inspect.cleandoc(obj.getTimeSyncServerIdentifier.__doc__) == "Identifier of the TimeSyncServer."
        assert inspect.cleandoc(obj.setTimeSyncServerIdentifier.__doc__).split("\n")[0] == "Identifier of the TimeSyncServer."
        assert (
            inspect.cleandoc(obj.getTimeSyncTechnology.__doc__)
            == "Defines the time synchronisation technology used. Possible values are: NTP_RFC958, PTP_ IEEE1588_2002, PTP_IEEE1588_2008, AVB_ IEEE802_1AS and others."
        )
        assert (
            inspect.cleandoc(obj.setTimeSyncTechnology.__doc__).split("\n")[0]
            == "Defines the time synchronisation technology used. Possible values are: NTP_RFC958, PTP_ IEEE1588_2002, PTP_IEEE1588_2008, AVB_ IEEE802_1AS and others."
        )
