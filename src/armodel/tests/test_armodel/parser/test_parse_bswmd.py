import filecmp

from ....models.M2.autosar_templates.generic_structure.ar_package import ARPackage

from .... import AUTOSAR
from .... import ARXMLParser, ARXMLWriter

import logging

class TestBswMD:
    def setup_method(self):
        logger = logging.getLogger()
        formatter = logging.Formatter('[%(levelname)s] : %(message)s')
        logging.basicConfig(format='[%(levelname)s] : %(message)s', level = logging.DEBUG)
        log_file = 'pytest_armodel.log'

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/BswM_Bswmd.arxml", document)

    def test_ar_packages(self):
        document = AUTOSAR.getInstance()
        root_pkgs = sorted(document.getARPackages(), key = lambda pkg: pkg.short_name)
        assert(len(root_pkgs) == 2)
        assert(root_pkgs[0].short_name == "AUTOSAR_BswM")
        assert(root_pkgs[1].short_name == "EB_BswM_TxDxM1I14R0")

        root_pkg_0_pkgs = sorted(root_pkgs[0].getARPackages(), key = lambda pkg: pkg.short_name)
        assert(len(root_pkg_0_pkgs) == 3)

        bsw_module_desc_pkg = root_pkg_0_pkgs[0]   # type：ARPackage  
        assert(bsw_module_desc_pkg.short_name == "BswModuleDescriptions")

        root_pkg_1_pkgs = root_pkgs[1].getARPackages()
        assert(len(root_pkg_1_pkgs) == 1)

    def test_bsw_module_description(self):
        document = AUTOSAR.getInstance()

        pkg = document.find("/AUTOSAR_BswM/BswModuleDescriptions")     # type: ARPackage
        bsw_module_descs = pkg.getBswModuleDescriptions()
        assert(len(bsw_module_descs) == 1)

        bsw_module_desc = bsw_module_descs[0]
        assert(bsw_module_desc.short_name == "BswM")
        assert(bsw_module_desc.module_id.getText() == "34")
        assert(bsw_module_desc.module_id.getValue() == 34)

        # verify the provided entries
        assert(len(bsw_module_desc._implementedEntryRefs) == 2)
        assert(bsw_module_desc._implementedEntryRefs[0].dest == "BSW-MODULE-ENTRY")
        assert(bsw_module_desc._implementedEntryRefs[0].value == "/AUTOSAR_BswM/BswModuleEntrys/BswM_Init")
        assert(bsw_module_desc._implementedEntryRefs[1].dest == "BSW-MODULE-ENTRY")
        assert(bsw_module_desc._implementedEntryRefs[1].value == "/AUTOSAR_BswM/BswModuleEntrys/BswM_MainFunction")

        assert(len(bsw_module_desc.getBswInternalBehaviors()) == 1)
        behavior = bsw_module_desc.getBswInternalBehaviors()[0]
        assert(behavior.short_name == "InternalBehavior_0")

        assert(len(behavior.getDataTypeMappingRefs()) == 1)
        data_type_mapping_ref = behavior.getDataTypeMappingRefs()[0]
        assert(data_type_mapping_ref.dest == "DATA-TYPE-MAPPING-SET")
        assert(data_type_mapping_ref.value == "/BswMMode/DataTypeMappingSets/BswMModeMapping")

        assert(len(behavior.getExclusiveAreas()) == 1)
        assert(behavior.getExclusiveAreas()[0].short_name == "SCHM_BSWM_EXCLUSIVE_AREA")

        assert(len(behavior.getBswSchedulableEntities()) == 1)
        entity = behavior.getBswSchedulableEntities()[0]
        assert(entity.short_name == "BswM_MainFunction")
        assert(entity.minimumStartInterval is not None)
        assert(entity.minimumStartIntervalMs is not None)
        assert(len(entity.getCanEnterExclusiveAreaRefs()) == 1) 
        assert(entity.getCanEnterExclusiveAreaRefs()[0].dest == "EXCLUSIVE-AREA")
        assert(entity.getCanEnterExclusiveAreaRefs()[0].value == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0/SCHM_BSWM_EXCLUSIVE_AREA")
        assert(entity.implementedEntryRef.dest == "BSW-MODULE-ENTRY")
        assert(entity.implementedEntryRef.value == "/AUTOSAR_BswM/BswModuleEntrys/BswM_MainFunction")

        assert(len(behavior.getBswTimingEvents()) == 1)
        event = behavior.getBswTimingEvents()[0]
        assert(event.short_name == "TimingEvent_MainFunction")
        assert(event.startsOnEventRef.dest == "BSW-SCHEDULABLE-ENTITY")
        assert(event.startsOnEventRef.value == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0/BswM_MainFunction")
        assert(event.period.getValue() == 0.02)
        assert(event.period.getText() == "0.02")
        assert(event.periodMs == 20)

    def test_bsw_module_entries(self):
        document = AUTOSAR.getInstance()

        pkg = document.find("/AUTOSAR_BswM/BswModuleEntrys")     # type: ARPackage
        entries = sorted(pkg.getBswModuleEntries(), key= lambda entry: entry.short_name)
        assert(len(entries) == 2)

        assert(entries[0].short_name == "BswM_Init")
        assert(entries[0].service_id._value == 0)
        assert(entries[0].is_reentrant.value == False)
        assert(entries[0].is_synchronous.value == True)
        assert(entries[0].call_type.getText() == "REGULAR")
        assert(entries[0].execution_context.getText() == "UNSPECIFIED")
        assert(entries[0].sw_service_impl_policy.getText() == "STANDARD")

        assert(entries[1].short_name == "BswM_MainFunction")
        assert(entries[1].service_id._value == 3)
        assert(entries[1].is_reentrant.value == False)
        assert(entries[1].is_synchronous.value == True)
        assert(entries[1].call_type.getText() == "SCHEDULED")
        assert(entries[1].execution_context.getText() == "TASK")
        assert(entries[1].sw_service_impl_policy.getText() == "STANDARD")

    def test_bsw_module_swc_bsw_mapping(self):
        document = AUTOSAR.getInstance()

        pkg = document.find("/AUTOSAR_BswM/SwcBswMappings")     # type: ARPackage
        mappings = pkg.getSwcBswMappings()
        assert(len(mappings) == 1)

        assert(mappings[0].bswBehaviorRef.dest == "BSW-INTERNAL-BEHAVIOR")
        assert(mappings[0].bswBehaviorRef.value == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0")
        
        assert(len(mappings[0].getRunnableMappings()) == 1)
        runnable_mapping = mappings[0].getRunnableMappings()[0]
        assert(runnable_mapping.bswEntityRef.dest == "BSW-SCHEDULABLE-ENTITY")
        assert(runnable_mapping.bswEntityRef.value == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0/BswM_MainFunction")
        assert(runnable_mapping.swcRunnableRef.dest == "RUNNABLE-ENTITY")
        assert(runnable_mapping.swcRunnableRef.value == "/AUTOSAR_BswM/SwComponentTypes/BswM/BswMInternalBehavior/RES_MainFunction")

    def test_bsw_module_implementation(self):
        document = AUTOSAR.getInstance()

        pkg = document.find("/EB_BswM_TxDxM1I14R0/Implementations")     # type: ARPackage
        assert(len(pkg.getBswImplementations()) == 1)
        impl = pkg.getBswImplementations()[0]
        assert(impl.short_name == "BswImplementation_0")
        assert(len(impl.getCodeDescriptors()) == 1)
        
        code_desc = impl.getCodeDescriptors()[0]
        assert(code_desc.short_name == "Files")
        assert(len(code_desc.getArtifactDescriptors()) == 21)
        assert(len(code_desc.getArtifactDescriptors("SWSRC")) == 4)
        assert(len(code_desc.getArtifactDescriptors("SWHDR")) == 15)
        assert(len(code_desc.getArtifactDescriptors("SWMAKE")) == 2)

        artifact_descs = sorted(code_desc.getArtifactDescriptors("SWMAKE"), key = lambda o: o.getShortLabel().getValue())
        assert(artifact_descs[0].getShortLabel().getValue() == "make::BswM_defs.mak")
        assert(artifact_descs[0].getCategory().getValue() == "SWMAKE")
        assert(artifact_descs[1].getShortLabel().getValue() == "make::BswM_rules.mak")
        assert(artifact_descs[1].getCategory().getValue() == "SWMAKE")

        assert(impl.programming_language.getValue() == "C")

        assert(impl.resource_consumption.short_name == "ResourceConsumption")
        assert(len(impl.resource_consumption.getMemorySections()) == 8)

        section = impl.resource_consumption.getMemorySection("CODE")
        assert(section.short_name == "CODE")
        assert(section.alignment == None)
        assert(section.swAddrMethodRef.dest == "SW-ADDR-METHOD")
        assert(section.swAddrMethodRef.value == "/AUTOSAR_MemMap/SwAddrMethods/CODE")

        section = impl.resource_consumption.getMemorySection("VAR_NO_INIT_UNSPECIFIED")
        assert(section.short_name == "VAR_NO_INIT_UNSPECIFIED")
        assert(section.alignment.getText() == "UNSPECIFIED")
        assert(section.swAddrMethodRef.dest == "SW-ADDR-METHOD")
        assert(section.swAddrMethodRef.value == "/AUTOSAR_MemMap/SwAddrMethods/VAR_NOINIT")

        assert(impl.vendor_id.getValue() == 1)
        assert(impl.sw_version.getValue() == "1.14.1")
        assert(impl.swc_bsw_mapping_ref.dest == "SWC-BSW-MAPPING")
        assert(impl.swc_bsw_mapping_ref.value == "/AUTOSAR_BswM/SwcBswMappings/SwcBswMapping_0")
        assert(impl.ar_release_version.getValue() == "4.0.3")
        assert(impl.behavior_ref.dest == "BSW-INTERNAL-BEHAVIOR")
        assert(impl.behavior_ref.value == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0")

    
    def test_load_save(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/SoftwareComponents.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated.arxml", document)

        assert(filecmp.cmp("src/armodel/tests/test_files/SoftwareComponents.arxml", "data/generated.arxml", shallow = False) == True)
    
    def test_bswm_bswmd_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/BswM_Bswmd.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_BswM_Bswmd.arxml", document)

        assert(filecmp.cmp("src/armodel/tests/test_files/BswM_Bswmd.arxml", "data/generated_BswM_Bswmd.arxml", shallow = False) == True)
