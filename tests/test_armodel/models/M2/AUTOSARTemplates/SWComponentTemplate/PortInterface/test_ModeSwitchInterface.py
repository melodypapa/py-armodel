import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ModeSwitchInterface

SPEC_NOTE = "A mode switch interface declares a ModeDeclarationGroupPrototype to be sent and received."
MODE_GROUP_NOTE = "The ModeDeclarationGroupPrototype of this mode interface."


class TestModeSwitchInterface:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        interface = ModeSwitchInterface(ar_root, "MSI")

        assert interface.getShortName() == "MSI"
        assert interface.getModeGroup() is None

    def test_heritage(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import PortInterface

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        interface = ModeSwitchInterface(ar_root, "MSI")

        assert type(interface).__bases__ == (PortInterface,)
        for ancestor in (PortInterface, Identifiable):
            assert isinstance(interface, ancestor)

    def test_class_docstring_verbatim(self):
        assert ModeSwitchInterface.__doc__.strip() == SPEC_NOTE

    def test_create_mode_group(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        interface = ModeSwitchInterface(ar_root, "MSI")

        mode_group = interface.createModeGroup("modeGroup")
        assert isinstance(mode_group, ModeDeclarationGroupPrototype)
        assert mode_group.getShortName() == "modeGroup"
        assert interface.getModeGroup() is mode_group

    def test_create_mode_group_duplicate_returns_existing(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        interface = ModeSwitchInterface(ar_root, "MSI")

        first = interface.createModeGroup("modeGroup")
        second = interface.createModeGroup("modeGroup")
        assert second is first
        assert interface.getModeGroup() is first

    def test_docstrings_verbatim(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("Pkg")
        interface = ModeSwitchInterface(ar_root, "MSI")

        assert interface.createModeGroup.__doc__ is not None
        assert MODE_GROUP_NOTE in interface.createModeGroup.__doc__
        assert interface.getModeGroup.__doc__ is not None
        assert interface.getModeGroup.__doc__.strip() == MODE_GROUP_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(ModeSwitchInterface.getModeGroup)
        assert hints.get("return") == typing.Optional[ModeDeclarationGroupPrototype]

        hints = typing.get_type_hints(ModeSwitchInterface.createModeGroup)
        assert hints.get("return") is ModeDeclarationGroupPrototype
        assert hints.get("short_name") is str
