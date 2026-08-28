from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBsw,
    TDEventBswModeDeclaration,
    TDEventBswModeDeclarationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TestTDEventBswModeDeclaration:
    def test_construct(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(ar_root, "BswMode1")
        assert event is not None
        assert event.short_name == "BswMode1"

    def test_not_abstract(self):
        assert issubclass(TDEventBswModeDeclaration, TDEventBsw)

    def test_get_set_entry_mode_declaration_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(ar_root, "BswMode1")
        ref = RefType()
        ref.setValue("/AUTOSAR/EntryMode")
        assert event.getEntryModeDeclarationRef() is None
        assert event.setEntryModeDeclarationRef(ref) is event
        assert event.getEntryModeDeclarationRef() is ref

    def test_set_entry_mode_declaration_ref_none_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(ar_root, "BswMode1")
        ref = RefType()
        ref.setValue("/AUTOSAR/EntryMode")
        event.setEntryModeDeclarationRef(ref)
        assert event.setEntryModeDeclarationRef(None) is event
        assert event.getEntryModeDeclarationRef() is ref

    def test_get_set_exit_mode_declaration_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(ar_root, "BswMode1")
        ref = RefType()
        ref.setValue("/AUTOSAR/ExitMode")
        assert event.getExitModeDeclarationRef() is None
        assert event.setExitModeDeclarationRef(ref) is event
        assert event.getExitModeDeclarationRef() is ref

    def test_set_exit_mode_declaration_ref_none_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(ar_root, "BswMode1")
        ref = RefType()
        ref.setValue("/AUTOSAR/ExitMode")
        event.setExitModeDeclarationRef(ref)
        assert event.setExitModeDeclarationRef(None) is event
        assert event.getExitModeDeclarationRef() is ref

    def test_get_set_mode_declaration_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(ar_root, "BswMode1")
        ref = RefType()
        ref.setValue("/AUTOSAR/ModeDeclarationGroupPrototype")
        assert event.getModeDeclarationRef() is None
        assert event.setModeDeclarationRef(ref) is event
        assert event.getModeDeclarationRef() is ref

    def test_set_mode_declaration_ref_none_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(ar_root, "BswMode1")
        ref = RefType()
        ref.setValue("/AUTOSAR/ModeDeclarationGroupPrototype")
        event.setModeDeclarationRef(ref)
        assert event.setModeDeclarationRef(None) is event
        assert event.getModeDeclarationRef() is ref

    def test_get_set_td_event_bsw_mode_declaration_type(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(ar_root, "BswMode1")
        enum = TDEventBswModeDeclarationTypeEnum()
        enum.setValue(TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_REQUESTED)
        assert event.getTdEventBswModeDeclarationType() is None
        assert event.setTdEventBswModeDeclarationType(enum) is event
        assert event.getTdEventBswModeDeclarationType() is enum

    def test_set_td_event_bsw_mode_declaration_type_none_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(ar_root, "BswMode1")
        enum = TDEventBswModeDeclarationTypeEnum()
        enum.setValue(TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_INITIATED)
        event.setTdEventBswModeDeclarationType(enum)
        assert event.setTdEventBswModeDeclarationType(None) is event
        assert event.getTdEventBswModeDeclarationType() is enum
