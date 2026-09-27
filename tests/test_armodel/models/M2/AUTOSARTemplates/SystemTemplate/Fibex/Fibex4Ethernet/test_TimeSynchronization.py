import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSyncClientConfiguration,
    TimeSynchronization,
    TimeSyncServerConfiguration,
)

CLASS_NOTE = """Defines the servers / clients in a time synchronised network."""


class TestTimeSynchronization:
    """Test cases for TimeSynchronization (Table 6.145, p.469)."""

    def _obj(self):
        return TimeSynchronization()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getTimeSyncClient() is None
        assert obj.getTimeSyncServer() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        item = TimeSyncClientConfiguration()
        assert obj.setTimeSyncClient(item) is obj
        assert obj.getTimeSyncClient() is item
        obj.setTimeSyncClient(None)
        assert obj.getTimeSyncClient() is item
        item = TimeSyncServerConfiguration(None, "Tssc")
        assert obj.setTimeSyncServer(item) is obj
        assert obj.getTimeSyncServer() is item
        obj.setTimeSyncServer(None)
        assert obj.getTimeSyncServer() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TimeSynchronization.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getTimeSyncClient.__doc__) == "Configuration of the time synchronisation client."
        assert inspect.cleandoc(obj.setTimeSyncClient.__doc__).split("\n")[0] == "Configuration of the time synchronisation client."
        assert inspect.cleandoc(obj.getTimeSyncServer.__doc__) == "Configuration of the time synchronisation server."
        assert inspect.cleandoc(obj.setTimeSyncServer.__doc__).split("\n")[0] == "Configuration of the time synchronisation server."
