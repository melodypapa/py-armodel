from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBsw,
    TDEventBswModule,
    TDEventBswModuleTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TestTDEventBswModule:
    def test_construct(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModule(ar_root, "BswModule1")
        assert event is not None
        assert event.short_name == "BswModule1"

    def test_not_abstract(self):
        assert issubclass(TDEventBswModule, TDEventBsw)

    def test_get_set_bsw_module_entry_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModule(ar_root, "BswModule1")
        ref = RefType()
        ref.setValue("/AUTOSAR/BswModuleEntry1")
        assert event.getBswModuleEntryRef() is None
        assert event.setBswModuleEntryRef(ref) is event
        assert event.getBswModuleEntryRef() is ref

    def test_set_bsw_module_entry_ref_none_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModule(ar_root, "BswModule1")
        ref = RefType()
        ref.setValue("/AUTOSAR/BswModuleEntry1")
        event.setBswModuleEntryRef(ref)
        assert event.setBswModuleEntryRef(None) is event
        assert event.getBswModuleEntryRef() is ref

    def test_get_set_td_event_bsw_module_type(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModule(ar_root, "BswModule1")
        enum = TDEventBswModuleTypeEnum()
        enum.setValue(TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALLED)
        assert event.getTdEventBswModuleType() is None
        assert event.setTdEventBswModuleType(enum) is event
        assert event.getTdEventBswModuleType() is enum

    def test_set_td_event_bsw_module_type_none_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TDEventBswModule(ar_root, "BswModule1")
        enum = TDEventBswModuleTypeEnum()
        enum.setValue(TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALL_RETURNED)
        event.setTdEventBswModuleType(enum)
        assert event.setTdEventBswModuleType(None) is event
        assert event.getTdEventBswModuleType() is enum
