import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSyncClientConfiguration,
    TimeSynchronization,
    TimeSyncServerConfiguration,
)

CLASS_NOTE = """Defines the servers / clients in a time synchronised network."""
CLIENT_NOTE = "Configuration of the time synchronisation client."
SERVER_NOTE = "Configuration of the time synchronisation server."


class TestTimeSynchronization:
    """Test cases for TimeSynchronization (Table 6.145, p.469)."""

    def _obj(self):
        return TimeSynchronization()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getTimeSyncClient() is None
        assert obj.getTimeSyncServer() is None

    def test_set_time_sync_client_round_trip_and_none_noop(self):
        obj = self._obj()
        item = TimeSyncClientConfiguration()
        assert obj.setTimeSyncClient(item) is obj
        assert obj.getTimeSyncClient() is item
        obj.setTimeSyncClient(None)
        assert obj.getTimeSyncClient() is item

    def test_get_time_sync_server_default(self):
        assert self._obj().getTimeSyncServer() is None

    def test_create_time_sync_server(self):
        obj = self._obj()
        server = obj.createTimeSyncServer("Server")
        assert isinstance(server, TimeSyncServerConfiguration)
        assert server.getShortName() == "Server"
        assert obj.getTimeSyncServer() is server

    def test_create_time_sync_server_duplicate_short_name_returns_existing(self):
        obj = self._obj()
        first = obj.createTimeSyncServer("Server")
        second = obj.createTimeSyncServer("Server")
        assert second is first
        assert obj.getTimeSyncServer() is first

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TimeSynchronization.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getTimeSyncClient.__doc__) == CLIENT_NOTE
        assert inspect.cleandoc(obj.setTimeSyncClient.__doc__).split("\n")[0] == CLIENT_NOTE
        assert inspect.cleandoc(obj.getTimeSyncServer.__doc__) == SERVER_NOTE
        assert inspect.cleandoc(obj.createTimeSyncServer.__doc__).split("\n")[0] == SERVER_NOTE
