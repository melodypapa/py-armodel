import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetPriorityRegeneration,
)

CLASS_NOTE = """Defines a priority regeneration where the ingressPriority is replaced by regeneratedPriority. The ethernetPriorityRegeneration is optional in case no priority regeneration shall be performed. In case a ethernetPriorityRegeneration is defined it shall have 8 mappings, one for each priority."""


class TestEthernetPriorityRegeneration:
    """Test cases for EthernetPriorityRegeneration (Table 3.74, p.128)."""

    def _obj(self):
        return EthernetPriorityRegeneration(None, "Obj")

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getIngressPriority() is None
        assert obj.getRegeneratedPriority() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        assert obj.setIngressPriority(7) is obj
        assert obj.getIngressPriority() == 7
        obj.setIngressPriority(None)
        assert obj.getIngressPriority() == 7
        assert obj.setRegeneratedPriority(7) is obj
        assert obj.getRegeneratedPriority() == 7
        obj.setRegeneratedPriority(None)
        assert obj.getRegeneratedPriority() == 7

    def test_class_docstring_note(self):
        assert inspect.cleandoc(EthernetPriorityRegeneration.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getIngressPriority.__doc__) == "Message priority of the incoming message. range: 0-7"
        assert inspect.cleandoc(obj.setIngressPriority.__doc__).split("\n")[0] == "Message priority of the incoming message. range: 0-7"
        assert inspect.cleandoc(obj.getRegeneratedPriority.__doc__) == "Regenerated message priority. range: 0-7"
        assert inspect.cleandoc(obj.setRegeneratedPriority.__doc__).split("\n")[0] == "Regenerated message priority. range: 0-7"
