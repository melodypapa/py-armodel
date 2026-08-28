import pytest

from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBsw,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class _ConcreteTDEventBsw(TDEventBsw):
    pass


class TestTDEventBsw:
    def test_abstract_instantiation(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError) as err:
            TDEventBsw(ar_root, "tdEventBsw")
        assert str(err.value) == "TDEventBsw is an abstract class."

    def test_get_set_bsw_module_description_ref(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        obj = _ConcreteTDEventBsw(ar_root, "tdEventBsw")
        ref = RefType()
        ref.setValue("/Pkg/BswModuleDescription")
        assert obj.getBswModuleDescriptionRef() is None
        assert obj.setBswModuleDescriptionRef(ref) is obj
        assert obj.getBswModuleDescriptionRef() is ref

    def test_set_bsw_module_description_ref_none_is_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        obj = _ConcreteTDEventBsw(ar_root, "tdEventBsw")
        ref = RefType()
        ref.setValue("/Pkg/BswModuleDescription")
        obj.setBswModuleDescriptionRef(ref)
        assert obj.setBswModuleDescriptionRef(None) is obj
        assert obj.getBswModuleDescriptionRef() is ref
