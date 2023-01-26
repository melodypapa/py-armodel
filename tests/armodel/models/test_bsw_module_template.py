import pytest

from armodel.models.bsw_module_template import BswModuleDescription, BswModuleEntry, BswModuleEntity, BswCalledEntity
from armodel import AUTOSAR

class TestBswModuleDescription:
    def test_construct(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        bsw_module_description = BswModuleDescription(ar_root, "bsw_module")
        assert(bsw_module_description != None)
        assert(bsw_module_description.short_name == "bsw_module")

    def test_category(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        bsw_module_description = BswModuleDescription(ar_root, "bsw_module")
        with pytest.raises(ValueError) as err:
            bsw_module_description.category = "invalid"
        assert(str(err.value) == "Invalid category <invalid> of BswModuleDescription <bsw_module>")

        bsw_module_description.category = "BSW_MODULE"
        assert(bsw_module_description.category == "BSW_MODULE")

class Test_M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces:
    def test_BswModuleEntry(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "bsw_entry")
        assert(entry != None)
        assert(entry.short_name == "bsw_entry")
 
class Test_M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior:
    def test_BswModuleEntity(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(NotImplementedError) as err:
            BswModuleEntity(ar_root, "BswModuleEntity")
        assert(str(err.value) == "BswModuleEntity is an abstract class.")

    def test_BswCalledEntity(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entity = BswCalledEntity(ar_root, "bsw_called_entity")
        assert(entity != None)
        assert(entity.short_name == "bsw_called_entity")