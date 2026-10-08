import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    DoIpEntity,
    InfrastructureServices,
    TimeSynchronization,
)

CLASS_NOTE = "Defines the network infrastructure services provided or consumed."


class TestInfrastructureServices:
    """Test cases for InfrastructureServices (Table 6.144, p.469)."""

    def _obj(self):
        return InfrastructureServices()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getDoIpEntity() is None
        assert obj.getTimeSynchronization() is None

    def test_get_set_do_ip_entity(self):
        obj = self._obj()
        value = DoIpEntity()
        assert obj.setDoIpEntity(value) is obj
        assert obj.getDoIpEntity() is value
        obj.setDoIpEntity(None)
        assert obj.getDoIpEntity() is value

    def test_get_set_time_synchronization(self):
        obj = self._obj()
        value = TimeSynchronization()
        assert obj.setTimeSynchronization(value) is obj
        assert obj.getTimeSynchronization() is value
        obj.setTimeSynchronization(None)
        assert obj.getTimeSynchronization() is value

    def test_inheritance(self):
        assert isinstance(self._obj(), ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(InfrastructureServices.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getDoIpEntity.__doc__) == "Defines whether a infrastructure service that runs on the network endpoint is a DoIP-Entity."
        assert inspect.cleandoc(obj.setDoIpEntity.__doc__).split("\n")[0] == "Defines whether a infrastructure service that runs on the network endpoint is a DoIP-Entity."
        assert inspect.cleandoc(obj.getTimeSynchronization.__doc__) == "Defines the servers / clients in a time synchronised network."
        assert inspect.cleandoc(obj.setTimeSynchronization.__doc__).split("\n")[0] == "Defines the servers / clients in a time synchronised network."
