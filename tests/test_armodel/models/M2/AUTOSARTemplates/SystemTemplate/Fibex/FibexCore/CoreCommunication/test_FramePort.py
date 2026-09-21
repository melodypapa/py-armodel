import inspect
import sys
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommunicationDirectionType,
    FramePort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommConnectorPort


def _get_type_hints(obj, localns=None):
    """typing.get_type_hints leaves PEP 563 self-references as ForwardRef on Python 3.8; resolve against the defining module."""
    hints = typing.get_type_hints(obj, localns=localns)
    lookup = dict(vars(sys.modules[obj.__module__]))
    if localns:
        lookup.update(localns)
    for name, hint in hints.items():
        if isinstance(hint, typing.ForwardRef):
            hints[name] = lookup.get(hint.__forward_arg__, hint)
    return hints


CLASS_NOTE = "Connectors reception or send port on the referenced channel referenced by a FrameTriggering."


class TestFramePort:
    """Test cases for FramePort (Table 6.2, p.304)."""

    def _create(self, short_name: str) -> FramePort:
        pkg = AUTOSAR.getInstance().createARPackage("FramePortPkg")
        return FramePort(pkg, short_name)

    def test_inheritance(self):
        assert issubclass(FramePort, CommConnectorPort)
        assert issubclass(FramePort, Identifiable)
        assert issubclass(FramePort, ARObject)

    def test_concrete_instantiation(self):
        port = self._create("Fp")
        assert isinstance(port, FramePort)
        assert isinstance(port, CommConnectorPort)
        assert port.getShortName() == "Fp"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(FramePort.__doc__) == CLASS_NOTE

    def test_init_docless(self):
        assert FramePort.__init__.__doc__ is None

    def test_inherited_communication_direction(self):
        port = self._create("Fp")

        assert port.getCommunicationDirection() is None

        direction = CommunicationDirectionType()
        direction.setValue(CommunicationDirectionType.ENUM_OUT)
        assert port == port.setCommunicationDirection(direction)
        assert port.getCommunicationDirection() == direction

        assert port == port.setCommunicationDirection(None)
        assert port.getCommunicationDirection() == direction

        localns = {"CommunicationDirectionType": CommunicationDirectionType}
        getter_hints = _get_type_hints(FramePort.getCommunicationDirection, localns=localns)
        assert getter_hints.get("return") == typing.Optional[CommunicationDirectionType]

        setter_hints = _get_type_hints(FramePort.setCommunicationDirection, localns=localns)
        assert setter_hints.get("value") == typing.Optional[CommunicationDirectionType]
        assert setter_hints.get("return") is CommConnectorPort
