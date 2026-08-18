import filecmp
import logging
from pathlib import Path

from armodel import AUTOSAR, ARXMLParser, ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalBehavior
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import BswImplementation


def get_test_file_path(filename: str) -> str:
    """Get absolute path to test file in integration_tests/test_files/."""
    return str(Path(__file__).parent.parent.parent / "integration_tests" / "test_files" / filename)


class TestBswMD:
    def setup_method(self):
        logger = logging.getLogger()
        formatter = logging.Formatter("[%(levelname)s] : %(message)s")
        logging.basicConfig(format="[%(levelname)s] : %(message)s", level=logging.DEBUG)
        log_file = "pytest_armodel.log"

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load(get_test_file_path("BswM_Bswmd.arxml"), document)

    def test_ar_packages(self):
        document = AUTOSAR.getInstance()
        root_pkgs = sorted(document.getARPackages(), key=lambda pkg: pkg.short_name)
        assert len(root_pkgs) == 2
        assert root_pkgs[0].getShortName() == "AUTOSAR_BswM"
        assert root_pkgs[1].getShortName() == "EB_BswM_TxDxM1I14R0"

        root_pkg_0_pkgs = sorted(root_pkgs[0].getARPackages(), key=lambda pkg: pkg.short_name)
        assert len(root_pkg_0_pkgs) == 3

        bsw_module_desc_pkg = root_pkg_0_pkgs[0]  # type：ARPackage
        assert bsw_module_desc_pkg.getShortName() == "BswModuleDescriptions"

        root_pkg_1_pkgs = root_pkgs[1].getARPackages()
        assert len(root_pkg_1_pkgs) == 1

    def test_bsw_module_description(self):
        document = AUTOSAR.getInstance()

        pkg = document.find("/AUTOSAR_BswM/BswModuleDescriptions")  # type: ARPackage
        bsw_module_descs = pkg.getBswModuleDescriptions()
        assert len(bsw_module_descs) == 1

        bsw_module_desc = bsw_module_descs[0]
        assert bsw_module_desc.getShortName() == "BswM"
        assert bsw_module_desc.moduleId.getText() == "34"
        assert bsw_module_desc.moduleId.getValue() == 34

        # verify the provided entries
        assert len(bsw_module_desc.implementedEntryRefs) == 2
        assert bsw_module_desc.implementedEntryRefs[0].getDest() == "BSW-MODULE-ENTRY"
        assert bsw_module_desc.implementedEntryRefs[0].getValue() == "/AUTOSAR_BswM/BswModuleEntrys/BswM_Init"
        assert bsw_module_desc.implementedEntryRefs[1].getDest() == "BSW-MODULE-ENTRY"
        assert bsw_module_desc.implementedEntryRefs[1].getValue() == "/AUTOSAR_BswM/BswModuleEntrys/BswM_MainFunction"

        assert len(bsw_module_desc.getInternalBehaviors()) == 1
        behavior = bsw_module_desc.getInternalBehaviors()[0]
        assert behavior.short_name == "InternalBehavior_0"

        assert len(behavior.getDataTypeMappingRefs()) == 1
        data_type_mapping_ref = behavior.getDataTypeMappingRefs()[0]
        assert data_type_mapping_ref.getDest() == "DATA-TYPE-MAPPING-SET"
        assert data_type_mapping_ref.getValue() == "/BswMMode/DataTypeMappingSets/BswMModeMapping"

        assert len(behavior.getExclusiveAreas()) == 1
        assert behavior.getExclusiveAreas()[0].short_name == "SCHM_BSWM_EXCLUSIVE_AREA"

        assert len(behavior.getBswSchedulableEntities()) == 1
        entity = behavior.getBswSchedulableEntities()[0]
        assert entity.short_name == "BswM_MainFunction"
        assert entity.minimumStartInterval is not None
        assert entity.minimumStartIntervalMs is not None
        assert len(entity.getCanEnterRefs()) == 1
        assert entity.getCanEnterRefs()[0].getDest() == "EXCLUSIVE-AREA"
        assert entity.getCanEnterRefs()[0].getValue() == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0/SCHM_BSWM_EXCLUSIVE_AREA"  # noqa E501
        assert entity.implementedEntryRef.getDest() == "BSW-MODULE-ENTRY"
        assert entity.implementedEntryRef.getValue() == "/AUTOSAR_BswM/BswModuleEntrys/BswM_MainFunction"

        assert len(behavior.getBswTimingEvents()) == 1
        event = behavior.getBswTimingEvents()[0]
        assert event.short_name == "TimingEvent_MainFunction"
        assert event.startsOnEventRef.getDest() == "BSW-SCHEDULABLE-ENTITY"
        assert event.startsOnEventRef.getValue() == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0/BswM_MainFunction"
        assert event.period.getValue() == 0.02
        assert event.period.getText() == "0.02"
        assert event.periodMs == 20

    def test_bsw_module_entries(self):
        document = AUTOSAR.getInstance()

        pkg = document.find("/AUTOSAR_BswM/BswModuleEntrys")  # type: ARPackage
        entries = sorted(pkg.getBswModuleEntries(), key=lambda entry: entry.short_name)
        assert len(entries) == 2

        assert entries[0].getShortName() == "BswM_Init"
        assert entries[0].getServiceId().getValue() == 0
        assert entries[0].getIsReentrant().getValue() is False
        assert entries[0].getIsSynchronous().getValue() is True
        assert entries[0].getCallType().getText() == "REGULAR"
        assert entries[0].getExecutionContext().getText() == "UNSPECIFIED"
        assert entries[0].getSwServiceImplPolicy().getText() == "STANDARD"

        assert entries[1].getShortName() == "BswM_MainFunction"
        assert entries[1].getServiceId().getValue() == 3
        assert entries[1].getIsReentrant().getValue() is False
        assert entries[1].getIsSynchronous().getValue() is True
        assert entries[1].getCallType().getText() == "SCHEDULED"
        assert entries[1].getExecutionContext().getText() == "TASK"
        assert entries[1].getSwServiceImplPolicy().getText() == "STANDARD"

    def test_bsw_module_swc_bsw_mapping(self):
        document = AUTOSAR.getInstance()

        pkg = document.find("/AUTOSAR_BswM/SwcBswMappings")  # type: ARPackage
        mappings = pkg.getSwcBswMappings()
        assert len(mappings) == 1

        assert mappings[0].bswBehaviorRef.getDest() == "BSW-INTERNAL-BEHAVIOR"
        assert mappings[0].bswBehaviorRef.getValue() == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0"

        assert len(mappings[0].getRunnableMappings()) == 1
        runnable_mapping = mappings[0].getRunnableMappings()[0]
        assert runnable_mapping.getBswEntityRef().getDest() == "BSW-SCHEDULABLE-ENTITY"
        assert runnable_mapping.getBswEntityRef().getValue() == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0/BswM_MainFunction"
        assert runnable_mapping.getSwcRunnableRef().getDest() == "RUNNABLE-ENTITY"
        assert runnable_mapping.getSwcRunnableRef().getValue() == "/AUTOSAR_BswM/SwComponentTypes/BswM/BswMInternalBehavior/RES_MainFunction"

    def test_bsw_module_implementation(self):
        document = AUTOSAR.getInstance()

        pkg = document.find("/EB_BswM_TxDxM1I14R0/Implementations")  # type: ARPackage
        assert len(pkg.getBswImplementations()) == 1
        impl = pkg.getBswImplementations()[0]
        assert impl.short_name == "BswImplementation_0"
        assert len(impl.getCodeDescriptors()) == 1

        code_desc = impl.getCodeDescriptors()[0]
        assert code_desc.short_name == "Files"
        assert len(code_desc.getArtifactDescriptors()) == 21
        assert len(code_desc.getArtifactDescriptors("SWSRC")) == 4
        assert len(code_desc.getArtifactDescriptors("SWHDR")) == 15
        assert len(code_desc.getArtifactDescriptors("SWMAKE")) == 2

        artifact_descs = sorted(code_desc.getArtifactDescriptors("SWMAKE"), key=lambda o: o.getShortLabel().getValue())  # type: List[AutosarEngineeringObject]    # noqa E501
        assert artifact_descs[0].getShortLabel().getValue() == "make::BswM_defs.mak"
        assert artifact_descs[0].getCategory().getValue() == "SWMAKE"
        assert artifact_descs[1].getShortLabel().getValue() == "make::BswM_rules.mak"
        assert artifact_descs[1].getCategory().getValue() == "SWMAKE"

        assert impl.programmingLanguage.getValue() == "C"

        assert impl.resourceConsumption.short_name == "ResourceConsumption"
        assert len(impl.resourceConsumption.getMemorySections()) == 8

        section = impl.resourceConsumption.getMemorySection("CODE")
        assert section.short_name == "CODE"
        assert section.alignment is None
        assert section.swAddrMethodRef.getDest() == "SW-ADDR-METHOD"
        assert section.swAddrMethodRef.getValue() == "/AUTOSAR_MemMap/SwAddrMethods/CODE"

        section = impl.resourceConsumption.getMemorySection("VAR_NO_INIT_UNSPECIFIED")
        assert section.short_name == "VAR_NO_INIT_UNSPECIFIED"
        assert section.alignment.getText() == "UNSPECIFIED"
        assert section.swAddrMethodRef.getDest() == "SW-ADDR-METHOD"
        assert section.swAddrMethodRef.getValue() == "/AUTOSAR_MemMap/SwAddrMethods/VAR_NOINIT"

        assert impl.vendorId.getValue() == 1
        assert impl.swVersion.getValue() == "1.14.1"
        assert impl.swcBswMappingRef.getDest() == "SWC-BSW-MAPPING"
        assert impl.swcBswMappingRef.getValue() == "/AUTOSAR_BswM/SwcBswMappings/SwcBswMapping_0"
        assert impl.arReleaseVersion.getValue() == "4.0.3"
        assert impl.behaviorRef.getDest() == "BSW-INTERNAL-BEHAVIOR"
        assert impl.behaviorRef.getValue() == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0"

    def test_get_implementation(self):
        document = AUTOSAR.getInstance()
        impl = document.getImplementation("/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0")
        assert impl.getFullName() == "/EB_BswM_TxDxM1I14R0/Implementations/BswImplementation_0"
        assert isinstance(impl, BswImplementation)

    def test_get_behavior(self):
        document = AUTOSAR.getInstance()
        behavior = document.getBehavior("/EB_BswM_TxDxM1I14R0/Implementations/BswImplementation_0")
        assert behavior.getFullName() == "/AUTOSAR_BswM/BswModuleDescriptions/BswM/InternalBehavior_0"
        assert isinstance(behavior, BswInternalBehavior)

    def test_load_save(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load(get_test_file_path("SoftwareComponents.arxml"), document)

        writer = ARXMLWriter()
        writer.save("data/generated.arxml", document)

        assert filecmp.cmp(get_test_file_path("SoftwareComponents.arxml"), "data/generated.arxml", shallow=False) is True

    def test_bswm_bswmd_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load(get_test_file_path("BswM_Bswmd.arxml"), document)

        writer = ARXMLWriter()
        writer.save("data/generated_BswM_Bswmd.arxml", document)

        assert filecmp.cmp(get_test_file_path("BswM_Bswmd.arxml"), "data/generated_BswM_Bswmd.arxml", shallow=False) is True


class TestReadBswModuleEntry:
    def test_read_entry_attributes(self):
        from xml.etree import ElementTree as ET

        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("Pkg")
        parser = ARXMLParser()
        xml = (
            "<BSW-MODULE-ENTRY xmlns='http://autosar.org/schema/r4.0'>"
            "<SHORT-NAME>Entry</SHORT-NAME>"
            "<ROLE>theRole</ROLE>"
            "<FUNCTION-PROTOTYPE-EMITTER>RTE</FUNCTION-PROTOTYPE-EMITTER>"
            "<CALL-TYPE>scheduled</CALL-TYPE>"
            "<BSW-ENTRY-KIND>concrete</BSW-ENTRY-KIND>"
            "<SERVICE-ID>42</SERVICE-ID>"
            "</BSW-MODULE-ENTRY>"
        )
        elem = ET.fromstring(xml)
        entry = pkg.createBswModuleEntry("Entry")
        parser.readBswModuleEntry(elem, entry)

        assert entry.getRole().getText() == "theRole"
        assert entry.getFunctionPrototypeEmitter().getText() == "RTE"
        assert entry.getCallType().getText() == "scheduled"
        assert entry.getBswEntryKind().getText() == "concrete"
        assert entry.getServiceId().getValue() == 42


class TestReadWriteBswModuleEntryRoundTrip:
    def test_round_trip_entry_attributes(self, tmp_path):
        from xml.etree import ElementTree as ET

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

        ET.register_namespace("", "http://autosar.org/schema/r4.0")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("Pkg")
        entry = pkg.createBswModuleEntry("Entry")
        entry.setRole(ARLiteral().setValue("theRole"))
        entry.setFunctionPrototypeEmitter(ARLiteral().setValue("RTE"))
        entry.setCallType(ARLiteral().setValue("scheduled"))
        entry.setBswEntryKind(ARLiteral().setValue("concrete"))

        writer = ARXMLWriter()
        root = ET.Element("{http://autosar.org/schema/r4.0}AR-PACKAGES")
        writer.writeBswModuleEntry(root, entry)
        reparsed = ET.fromstring(ET.tostring(root))
        reparsed_entry = reparsed.find("{http://autosar.org/schema/r4.0}BSW-MODULE-ENTRY")
        entry2 = pkg.createBswModuleEntry("Entry2")
        parser = ARXMLParser()
        parser.readBswModuleEntry(reparsed_entry, entry2)

        assert entry2.getRole().getText() == "theRole"
        assert entry2.getFunctionPrototypeEmitter().getText() == "RTE"
        assert entry2.getCallType().getText() == "scheduled"
        assert entry2.getBswEntryKind().getText() == "concrete"


class TestReadWriteBswModuleDescriptionRoundTrip:
    def test_round_trip_new_attributes(self, tmp_path):
        from xml.etree import ElementTree as ET

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import SwComponentDocumentation

        ET.register_namespace("", "http://autosar.org/schema/r4.0")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("Pkg")
        desc = pkg.createBswModuleDescription("Desc")

        dependency = desc.createBswModuleDependency("dep1")
        dependency.setTargetModuleId(PositiveInteger().setValue("7"))
        dependency.setTargetModuleRef(RefType().setValue("/Target/Module"))

        doc = SwComponentDocumentation()
        desc.setBswModuleDocumentation(doc)

        desc.addExpectedEntryRef(RefType().setValue("/Expected/Entry"))

        desc.createRequiredModeGroup("rmg1")

        writer = ARXMLWriter()
        root = ET.Element("{http://autosar.org/schema/r4.0}AR-PACKAGES")
        writer.writeBswModuleDescription(root, desc)
        reparsed = ET.fromstring(ET.tostring(root))

        desc2 = pkg.createBswModuleDescription("Desc2")
        parser = ARXMLParser()
        reparsed_desc = reparsed.find("{http://autosar.org/schema/r4.0}BSW-MODULE-DESCRIPTION")
        parser.readBswModuleDescription(reparsed_desc, desc2)

        assert len(desc2.getBswModuleDependencies()) == 1
        dep2 = desc2.getBswModuleDependencies()[0]
        assert dep2.getShortName() == "dep1"
        assert dep2.getTargetModuleId().getValue() == 7
        assert dep2.getTargetModuleRef().getValue() == "/Target/Module"

        assert desc2.getBswModuleDocumentation() is not None

        assert len(desc2.getExpectedEntryRefs()) == 1
        assert desc2.getExpectedEntryRefs()[0].getValue() == "/Expected/Entry"

        # requiredModeGroup must be routed to the required list, not the provided list
        assert len(desc2.getRequiredModeGroups()) == 1
        assert desc2.getRequiredModeGroups()[0].getShortName() == "rmg1"
        assert desc2.getProvidedModeGroups() == []
