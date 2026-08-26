"""Model unit tests for OrderedMaster (Table 6.148, p.470)."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    OrderedMaster,
)


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


class TestOrderedMaster:
    def test_initialization_defaults(self):
        master = OrderedMaster()
        assert master.getIndex() is None
        assert master.getTimeSyncServer() is None

    def test_get_set_index(self):
        master = OrderedMaster()
        assert master.setIndex(_pos_int("2")) is master
        assert master.getIndex().getValue() == 2

    def test_set_index_none_no_op(self):
        master = OrderedMaster()
        master.setIndex(_pos_int("2"))
        master.setIndex(None)
        assert master.getIndex().getValue() == 2

    def test_get_set_time_sync_server(self):
        master = OrderedMaster()
        ref = RefType()
        ref.setDest("TIME-SYNC-SERVER-CONFIGURATION")
        ref.setValue("/Server/Master1")
        assert master.setTimeSyncServer(ref) is master
        assert master.getTimeSyncServer().getValue() == "/Server/Master1"
        assert master.getTimeSyncServer().getDest() == "TIME-SYNC-SERVER-CONFIGURATION"

    def test_set_time_sync_server_none_no_op(self):
        master = OrderedMaster()
        ref = RefType()
        ref.setValue("/Server/Master1")
        master.setTimeSyncServer(ref)
        master.setTimeSyncServer(None)
        assert master.getTimeSyncServer().getValue() == "/Server/Master1"
