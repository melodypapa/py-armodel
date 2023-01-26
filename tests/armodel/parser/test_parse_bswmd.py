from armodel import AUTOSAR, ARPackage
from armodel import ARXMLParser

import sys

class TestARPackage:
    def setup_method(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("tests/test_files/BswM_Bswmd.arxml", document)

    def test_ar_packages(self):
        document = AUTOSAR.getInstance()
        root_pkgs = document.getARPackages()
        assert(len(root_pkgs) == 2)
        assert(root_pkgs[0].short_name == "AUTOSAR_BswM")
        assert(root_pkgs[1].short_name == "EB_BswM_TxDxM1I14R0")

        root_pkg_0_pkgs = root_pkgs[0].getARPackages()
        assert(len(root_pkg_0_pkgs) == 3)

        bsw_module_desc_pkg = root_pkg_0_pkgs[0]   # type：ARPackage  
        assert(bsw_module_desc_pkg.short_name == "BswModuleDescriptions")

        root_pkg_1_pkgs = root_pkgs[1].getARPackages()
        assert(len(root_pkg_1_pkgs) == 1)

    def test_bsw_module_description(self):
        document = AUTOSAR.getInstance()

        bsw_module_descs = document.getARPackages()[0].getARPackages()[0].getBswModuleDescriptions()
        assert(len(bsw_module_descs) == 1)

        bsw_module_desc = bsw_module_descs[0]
        assert(bsw_module_desc.short_name == "BswM")
        assert(bsw_module_desc.module_id == 42)

        # verify the provided entries
        assert(len(bsw_module_desc.implemented_entry_refs) == 2)
        assert(bsw_module_desc.implemented_entry_refs[0].dest == "BSW-MODULE-ENTRY")
        assert(bsw_module_desc.implemented_entry_refs[0].value == "/AUTOSAR_BswM/BswModuleEntrys/BswM_MainFunction")
        assert(bsw_module_desc.implemented_entry_refs[1].dest == "BSW-MODULE-ENTRY")
        assert(bsw_module_desc.implemented_entry_refs[1].value == "/AUTOSAR_BswM/BswModuleEntrys/BswM_Init")

        assert(len(bsw_module_desc.getBswInternalBehaviors()) == 1)
        behavior = bsw_module_desc.getBswInternalBehaviors()[0]
        assert(behavior.short_name == "InternalBehavior_0")


        