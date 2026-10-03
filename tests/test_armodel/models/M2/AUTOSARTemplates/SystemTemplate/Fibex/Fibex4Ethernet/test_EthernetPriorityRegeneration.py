import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetPriorityRegeneration,
)

CLASS_NOTE = """Defines a priority regeneration where the ingressPriority is replaced by regeneratedPriority. The ethernetPriorityRegeneration is optional in case no priority regeneration shall be performed. In case a ethernetPriorityRegeneration is defined it shall have 8 mappings, one for each priority."""


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


class TestEthernetPriorityRegeneration:
    """Test cases for EthernetPriorityRegeneration (Table 3.74, p.128)."""

    def _obj(self):
        return EthernetPriorityRegeneration(None, "Obj")

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getIngressPriority() is None
        assert obj.getRegeneratedPriority() is None

    def test_ingress_priority_round_trip_and_none_noop(self):
        obj = self._obj()
        assert obj.setIngressPriority(_pos_int("7")) is obj
        assert isinstance(obj.getIngressPriority(), PositiveInteger)
        assert obj.getIngressPriority().getValue() == 7
        assert obj.setIngressPriority(None) is obj
        assert obj.getIngressPriority().getValue() == 7

    def test_regenerated_priority_round_trip_and_none_noop(self):
        obj = self._obj()
        assert obj.setRegeneratedPriority(_pos_int("7")) is obj
        assert isinstance(obj.getRegeneratedPriority(), PositiveInteger)
        assert obj.getRegeneratedPriority().getValue() == 7
        assert obj.setRegeneratedPriority(None) is obj
        assert obj.getRegeneratedPriority().getValue() == 7

    def test_scalar_pairs_are_getter_first_in_source_order(self):
        src = inspect.getsource(EthernetPriorityRegeneration)
        assert src.index("def getIngressPriority") < src.index("def setIngressPriority")
        assert src.index("def setIngressPriority") < src.index("def getRegeneratedPriority")
        assert src.index("def getRegeneratedPriority") < src.index("def setRegeneratedPriority")

    def test_class_docstring_note(self):
        assert inspect.cleandoc(EthernetPriorityRegeneration.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getIngressPriority.__doc__) == "Message priority of the incoming message. range: 0-7"
        assert inspect.cleandoc(obj.setIngressPriority.__doc__).split("\n")[0] == "Message priority of the incoming message. range: 0-7"
        assert inspect.cleandoc(obj.getRegeneratedPriority.__doc__) == "Regenerated message priority. range: 0-7"
        assert inspect.cleandoc(obj.setRegeneratedPriority.__doc__).split("\n")[0] == "Regenerated message priority. range: 0-7"
