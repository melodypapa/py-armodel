import filecmp
import xml.etree.ElementTree as ET

from src.armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior
from src.armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import InternalBehavior
from src.armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation
from src.armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AtomicSwComponentType, CompositionSwComponentType
from src.armodel.writer.arxml_writer import ARXMLWriter
from src.armodel.parser.arxml_parser import ARXMLParser
from src.armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR, AUTOSARDoc


class TestSWComponents:
    def setup_method(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/SoftwareComponents.arxml", document)

    def test_ar_packages(self):
        document = AUTOSAR.getInstance()
        root_pkgs = sorted(document.getARPackages(), key=lambda pkg: pkg.getShortName())

        assert (len(root_pkgs) == 1)
        assert ("DemoApplication" == root_pkgs[0].getShortName())

    def test_sw_component(self):
        document = AUTOSAR.getInstance()
        sw_component = document.find("/DemoApplication/SwComponentTypes/SWC_CyclicCounter")
        assert (sw_component.getShortName() == 'SWC_CyclicCounter')
        assert (isinstance(sw_component, AtomicSwComponentType))

    def test_get_implementation(self):
        document = AUTOSAR.getInstance()
        impl = document.getImplementation("/DemoApplication/SwComponentTypes/SWC_CyclicCounter/IB_SWC_CyclicCounter")
        assert (impl.getFullName() == "/DemoApplication/SwcImplementations/Impl_SWC_CyclicCounter")
        assert (isinstance(impl, SwcImplementation))

    def test_get_behavior(self):
        document = AUTOSAR.getInstance()
        behavior = document.getBehavior("/DemoApplication/SwcImplementations/Impl_SWC_CyclicCounter")
        assert (behavior.getFullName() == "/DemoApplication/SwComponentTypes/SWC_CyclicCounter/IB_SWC_CyclicCounter")
        assert (isinstance(behavior, InternalBehavior))

    def test_composition_sw_component_types(self):
        document = AUTOSAR.getInstance()
        sw_component = document.find("/DemoApplication/SwComponentTypes/TopLevelComposition")
        assert (sw_component.short_name == "TopLevelComposition")
        assert (isinstance(sw_component, CompositionSwComponentType))
        ports = sw_component.getPorts()
        assert (len(ports) == 2)

    def test_composition_sw_component_types_sw_connectors(self):
        document = AUTOSAR.getInstance()
        sw_component = document.find("/DemoApplication/SwComponentTypes/TopLevelComposition")
        assert (isinstance(sw_component, CompositionSwComponentType))
        assert (len(sw_component.getSwConnectors()) == 6)
        assert (len(sw_component.getAssemblySwConnectors()) == 3)
        assert (len(sw_component.getDelegationSwConnectors()) == 3)

        connector_name_list = set()
        for sw_connector in sw_component.getAssemblySwConnectors():
            connector_name_list.add(sw_connector.short_name)

        assert (connector_name_list == set(['a6a18805580c94537a4c82f6c289a4d', 'ac681652833fb4b12b920adab33a73b', 'ac681652833fb4b12b920adab33a73c']))

        sw_component.removeElement("a6a18805580c94537a4c82f6c289a4d")
        assert (len(sw_component.getAssemblySwConnectors()) == 2)

        # remove all the AssemblySwConnector
        sw_component.removeAllAssemblySwConnector()
        assert (len(sw_component.getAssemblySwConnectors()) == 0)
        assert (len(sw_component.getDelegationSwConnectors()) == 3)
        
        # remove all the DelegationSwConnector
        sw_component.removeAllDelegationSwConnector()
        assert (len(sw_component.getAssemblySwConnectors()) == 0)
        assert (len(sw_component.getDelegationSwConnectors()) == 0)
        
    def test_bswm_mode_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/BswMMode.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_Datatypes.arxml", document)

        assert (filecmp.cmp("test_files/BswMMode.arxml", "data/generated_AUTOSAR_Datatypes.arxml", shallow=False) is True)

    def test_sw_record_demo_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/SwRecordDemo.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_SwRecordDemo.arxml", document)

        assert (filecmp.cmp("test_files/SwRecordDemo.arxml", "data/generated_SwRecordDemo.arxml", shallow=False) is True)

    def test_application_data_type_blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml", document)

        # Store some key properties before saving
        original_packages = len(document.getARPackages())
        # Verify we loaded something meaningful
        assert original_packages > 0

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml", document)

        # Verify the file was created
        import os
        assert os.path.exists("data/generated_AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml")

        # Try to reload the generated file to ensure it's valid
        new_document = AUTOSAR.getInstance()
        new_document.clear()
        new_parser = ARXMLParser()
        new_parser.load("data/generated_AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml", new_document)
        # Verify the reloaded document also has packages
        assert len(new_document.getARPackages()) > 0

    def test_application_data_type_life_cycle_standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_ApplicationDataType_LifeCycle_Standard.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_ApplicationDataType_LifeCycle_Standard.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_ApplicationDataType_LifeCycle_Standard.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_ApplicationDataType_LifeCycle_Standard.arxml", shallow=False) is True)
        
    def test_autosar_mod_ai_specification_basetypes_standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml", shallow=False) is True)
        
    def test_autosar_mod_ai_specification_collection_body_blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_Collection_Body_Blueprint.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_Collection_Body_Blueprint.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_Collection_Body_Blueprint.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_Collection_Body_Blueprint.arxml", shallow=False) is True)
        
    def test_autosar_mod_ai_specification_collection_chassis_blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_Collection_Chassis_Blueprint.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_Collection_Chassis_Blueprint.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_Collection_Chassis_Blueprint.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_Collection_Chassis_Blueprint.arxml", shallow=False) is True)
        
    def test_autosar_mod_ai_specification_collection_mmedtelmhmi_blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_Collection_MmedTelmHmi_Blueprint.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_Collection_MmedTelmHmi_Blueprint.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_Collection_MmedTelmHmi_Blueprint.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_Collection_MmedTelmHmi_Blueprint.arxml", shallow=False) is True)
        
    def test_autosar_mod_ai_specification_collection_occptpedsfty_blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_Collection_OccptPedSfty_Blueprint.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_Collection_OccptPedSfty_Blueprint.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_Collection_OccptPedSfty_Blueprint.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_Collection_OccptPedSfty_Blueprint.arxml", shallow=False) is True)
        
    def test_autosar_mod_ai_specification_collection_pt_blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_Collection_Pt_Blueprint.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_Collection_Pt_Blueprint.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_Collection_Pt_Blueprint.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_Collection_Pt_Blueprint.arxml", shallow=False) is True)
        
    def test_autosar_mod_ai_specification_compumethod_blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml", document)

        # Store some key properties before saving
        original_packages = len(document.getARPackages())
        # Verify we loaded something meaningful
        assert original_packages > 0

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml", document)

        # Verify the file was created
        import os
        assert os.path.exists("data/generated_AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml")

        # Try to reload the generated file to ensure it's valid
        new_document = AUTOSAR.getInstance()
        new_document.clear()
        new_parser = ARXMLParser()
        new_parser.load("data/generated_AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml", new_document)
        # Verify the reloaded document also has packages
        assert len(new_document.getARPackages()) > 0
        
    def test_AUTOSAR_MOD_AISpecification_DataConstr_Blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_DataConstr_Blueprint.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_DataConstr_Blueprint.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_DataConstr_Blueprint.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_DataConstr_Blueprint.arxml", shallow=False) is True)
    
    def test_AUTOSAR_MOD_AISpecification_CompuMethod_LifeCycle_Standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_CompuMethod_LifeCycle_Standard.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_CompuMethod_LifeCycle_Standard.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_CompuMethod_LifeCycle_Standard.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_CompuMethod_LifeCycle_Standard.arxml", shallow=False) is True)
        
    def test_AUTOSAR_MOD_AISpecification_Keyword_LifeCycle_Standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_Keyword_LifeCycle_Standard.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_Keyword_LifeCycle_Standard.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_Keyword_LifeCycle_Standard.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_Keyword_LifeCycle_Standard.arxml", shallow=False) is True)
        
    def test_AUTOSAR_MOD_AISpecification_KeywordSet_Blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_KeywordSet_Blueprint.arxml", document)

        # Store some key properties before saving
        original_packages = len(document.getARPackages())
        # Verify we loaded something meaningful
        assert original_packages > 0

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_KeywordSet_Blueprint.arxml", document)

        # Verify the file was created
        import os
        assert os.path.exists("data/generated_AUTOSAR_MOD_AISpecification_KeywordSet_Blueprint.arxml")

        # Try to reload the generated file to ensure it's valid
        new_document = AUTOSAR.getInstance()
        new_document.clear()
        new_parser = ARXMLParser()
        new_parser.load("data/generated_AUTOSAR_MOD_AISpecification_KeywordSet_Blueprint.arxml", new_document)
        # Verify the reloaded document also has packages
        assert len(new_document.getARPackages()) > 0

    def test_AUTOSAR_MOD_AISpecification_PhysicalDimension_LifeCycle_Standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_PhysicalDimension_LifeCycle_Standard.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_PhysicalDimension_LifeCycle_Standard.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_PhysicalDimension_LifeCycle_Standard.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_PhysicalDimension_LifeCycle_Standard.arxml", shallow=False) is True)
        
    def test_AUTOSAR_MOD_AISpecification_PhysicalDimension_Standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_PhysicalDimension_Standard.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_PhysicalDimension_Standard.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_PhysicalDimension_Standard.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_PhysicalDimension_Standard.arxml", shallow=False) is True)

    def test_AUTOSAR_MOD_AISpecification_PortInterface_Blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_PortInterface_Blueprint.arxml", document)

        # Store some key properties before saving
        original_packages = len(document.getARPackages())
        # Verify we loaded something meaningful
        assert original_packages > 0

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_PortInterface_Blueprint.arxml", document)

        # Verify the file was created
        import os
        assert os.path.exists("data/generated_AUTOSAR_MOD_AISpecification_PortInterface_Blueprint.arxml")

        # Try to reload the generated file to ensure it's valid
        new_document = AUTOSAR.getInstance()
        new_document.clear()
        new_parser = ARXMLParser()
        new_parser.load("data/generated_AUTOSAR_MOD_AISpecification_PortInterface_Blueprint.arxml", new_document)
        # Verify the reloaded document also has packages
        assert len(new_document.getARPackages()) > 0

    def test_AUTOSAR_MOD_AISpecification_PortInterface_LifeCycle_Standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_PortInterface_LifeCycle_Standard.arxml", document)

        # Store some key properties before saving
        original_packages = len(document.getARPackages())
        # Verify we loaded something meaningful
        assert original_packages > 0

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_PortInterface_LifeCycle_Standard.arxml", document)

        # Verify the file was created
        import os
        assert os.path.exists("data/generated_AUTOSAR_MOD_AISpecification_PortInterface_LifeCycle_Standard.arxml")

        # Try to reload the generated file to ensure it's valid
        new_document = AUTOSAR.getInstance()
        new_document.clear()
        new_parser = ARXMLParser()
        new_parser.load("data/generated_AUTOSAR_MOD_AISpecification_PortInterface_LifeCycle_Standard.arxml", new_document)
        # Verify the reloaded document also has packages
        assert len(new_document.getARPackages()) > 0

    def test_AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_Blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_Blueprint.arxml", document)

        # Store some key properties before saving
        original_packages = len(document.getARPackages())
        # Verify we loaded something meaningful
        assert original_packages > 0

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_Blueprint.arxml", document)

        # Verify the file was created
        import os
        assert os.path.exists("data/generated_AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_Blueprint.arxml")

        # Try to reload the generated file to ensure it's valid
        new_document = AUTOSAR.getInstance()
        new_document.clear()
        new_parser = ARXMLParser()
        new_parser.load("data/generated_AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_Blueprint.arxml", new_document)
        # Verify the reloaded document also has packages
        assert len(new_document.getARPackages()) > 0
        
    def test_AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_LifeCycle_Standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_LifeCycle_Standard.arxml", document)

        # Store some key properties before saving
        original_packages = len(document.getARPackages())
        # Verify we loaded something meaningful
        assert original_packages > 0

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_LifeCycle_Standard.arxml", document)

        # Verify the file was created
        import os
        assert os.path.exists("data/generated_AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_LifeCycle_Standard.arxml")

        # Try to reload the generated file to ensure it's valid
        new_document = AUTOSAR.getInstance()
        new_document.clear()
        new_parser = ARXMLParser()
        new_parser.load("data/generated_AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_LifeCycle_Standard.arxml", new_document)
        # Verify the reloaded document also has packages
        assert len(new_document.getARPackages()) > 0
        
    def test_AUTOSAR_MOD_AISpecification_SwComponentTypes_Blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_SwComponentTypes_Blueprint.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_SwComponentTypes_Blueprint.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_SwComponentTypes_Blueprint.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_SwComponentTypes_Blueprint.arxml", shallow=False) is True)

    def test_AUTOSAR_MOD_AISpecification_Unit_LifeCycle_Standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_Unit_LifeCycle_Standard.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_Unit_LifeCycle_Standard.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_Unit_LifeCycle_Standard.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_Unit_LifeCycle_Standard.arxml", shallow=False) is True)

    def test_AUTOSAR_MOD_AISpecification_Unit_Standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_Unit_Standard.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_Unit_Standard.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_Unit_Standard.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_Unit_Standard.arxml", shallow=False) is True)

    def test_AUTOSAR_MOD_AISpecification_DataConstr_LifeCycle_Standard_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_DataConstr_LifeCycle_Standard.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_DataConstr_LifeCycle_Standard.arxml", document)

        assert (filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_DataConstr_LifeCycle_Standard.arxml",
                            "data/generated_AUTOSAR_MOD_AISpecification_DataConstr_LifeCycle_Standard.arxml", shallow=False) is True)


class TestSwComponentsWithSameName:
    def test_read_same_package_and_sw_component_name(self):
        parser = ARXMLParser()
        parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
        xml_content = """
            <AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00049.xsd" T="2025-05-08T10:56:35+03:00">
                <AR-PACKAGES>
                    <AR-PACKAGE>
                        <SHORT-NAME>Components</SHORT-NAME>
                        <ELEMENTS>
                            <APPLICATION-SW-COMPONENT-TYPE T="2025-05-08T21:49:46+03:00">
                            <SHORT-NAME>DUPLICATE_NAME</SHORT-NAME>
                            <INTERNAL-BEHAVIORS>
                                <SWC-INTERNAL-BEHAVIOR T="2025-06-13T08:49:08+03:00">
                                <SHORT-NAME>DUPLICATE_NAME</SHORT-NAME>
                                <RUNNABLES>
                                    <RUNNABLE-ENTITY T="2025-06-13T08:49:24+03:00">
                                    <SHORT-NAME>RunnableInit</SHORT-NAME>
                                    <MINIMUM-START-INTERVAL>0.0</MINIMUM-START-INTERVAL>
                                    <CAN-BE-INVOKED-CONCURRENTLY>false</CAN-BE-INVOKED-CONCURRENTLY>
                                    <SYMBOL>RunnableInit</SYMBOL>
                                    </RUNNABLE-ENTITY>
                                </RUNNABLES>
                                </SWC-INTERNAL-BEHAVIOR>
                            </INTERNAL-BEHAVIORS>
                            </APPLICATION-SW-COMPONENT-TYPE>
                        </ELEMENTS>
                        <AR-PACKAGES>
                            <AR-PACKAGE>
                                <SHORT-NAME>DUPLICATE_NAME</SHORT-NAME>
                            </AR-PACKAGE>
                            <AR-PACKAGE>
                                <SHORT-NAME>NewPackage</SHORT-NAME>
                            </AR-PACKAGE>
                        </AR-PACKAGES>
                    </AR-PACKAGE>
                    <AR-PACKAGE>
                        <SHORT-NAME>Implementation</SHORT-NAME>
                        <ELEMENTS>
                        <SW-ADDR-METHOD>
                        <SHORT-NAME>CODE</SHORT-NAME>
                        <MEMORY-ALLOCATION-KEYWORD-POLICY>ADDR-METHOD-SHORT-NAME</MEMORY-ALLOCATION-KEYWORD-POLICY>
                        <SECTION-TYPE>CODE</SECTION-TYPE>
                        </SW-ADDR-METHOD>
                        <SWC-IMPLEMENTATION>
                        <SHORT-NAME>DUPLICATE_NAME</SHORT-NAME>
                        <CODE-DESCRIPTORS>
                            <CODE>
                            <SHORT-NAME>CODE</SHORT-NAME>
                            <ARTIFACT-DESCRIPTORS>
                                <AUTOSAR-ENGINEERING-OBJECT>
                                <SHORT-LABEL>CODE</SHORT-LABEL>
                                <CATEGORY>SWSRC</CATEGORY>
                                </AUTOSAR-ENGINEERING-OBJECT>
                            </ARTIFACT-DESCRIPTORS>
                            </CODE>
                        </CODE-DESCRIPTORS>
                        <PROGRAMMING-LANGUAGE>C</PROGRAMMING-LANGUAGE>
                        <RESOURCE-CONSUMPTION>
                            <SHORT-NAME>ResourceConsumption</SHORT-NAME>
                            <MEMORY-SECTIONS>
                                <MEMORY-SECTION>
                                    <SHORT-NAME>CODE</SHORT-NAME>
                                    <SIZE>0</SIZE>
                                    <SW-ADDRMETHOD-REF DEST="SW-ADDR-METHOD">/AUTOSAR_MemMap/SwAddrMethods/CODE</SW-ADDRMETHOD-REF>
                                </MEMORY-SECTION>
                            </MEMORY-SECTIONS>
                        </RESOURCE-CONSUMPTION>
                        <SW-VERSION>1.0.0</SW-VERSION>
                        <VENDOR-ID>0</VENDOR-ID>
                        <BEHAVIOR-REF DEST="SWC-INTERNAL-BEHAVIOR">/Components/DUPLICATE_NAME/DUPLICATE_NAME</BEHAVIOR-REF>
                        </SWC-IMPLEMENTATION>
                    </ELEMENTS>
                    </AR-PACKAGE>
                </AR-PACKAGES>
            </AUTOSAR>
        """ # noqa E501

        # prepare the XML content
        element = ET.fromstring(xml_content)

        document = AUTOSARDoc()
        parser.readARPackages(element, document)
        assert len(document.getARPackages()) == 2
        assert document.getARPackages()[0].getShortName() == "Components"
        assert document.getARPackages()[1].getShortName() == "Implementation"
        assert len(document.getARPackages()[0].getElements()) == 1
        
        sw_component: AtomicSwComponentType = document.getARPackages()[0].getElement("DUPLICATE_NAME", AtomicSwComponentType)
        assert sw_component is not None
        assert sw_component.getShortName() == "DUPLICATE_NAME"
        
        internal_behavior: SwcInternalBehavior = sw_component.getInternalBehavior()
        # Check if the internal behavior is present
        assert internal_behavior is not None
        assert internal_behavior.getShortName() == "DUPLICATE_NAME"
        
        # Check if the runnable is present
        assert len(internal_behavior.getRunnableEntities()) == 1
        runnables = internal_behavior.getRunnableEntities()

        # Check the first runnable
        runnable = runnables[0]
        assert runnable is not None
        assert runnable.getShortName() == "RunnableInit"
        
