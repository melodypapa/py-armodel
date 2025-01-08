import filecmp

from ....models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import InternalBehavior
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AtomicSwComponentType, CompositionSwComponentType
from ....writer.arxml_writer import ARXMLWriter
from ....parser.arxml_parser import ARXMLParser
from ....models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

class TestSWComponents:
    def setup_method(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/SoftwareComponents.arxml", document)

    def test_ar_packages(self):
        document = AUTOSAR.getInstance()
        root_pkgs = sorted(document.getARPackages(), key = lambda pkg: pkg.getShortName())

        assert(len(root_pkgs) == 1)
        assert("DemoApplication" == root_pkgs[0].getShortName())

    def test_sw_component(self):
        document = AUTOSAR.getInstance()
        sw_component = document.find("/DemoApplication/SwComponentTypes/SWC_CyclicCounter")
        assert(sw_component.getShortName() == 'SWC_CyclicCounter')
        assert(isinstance(sw_component, AtomicSwComponentType))

    def test_get_implementation(self):
        document = AUTOSAR.getInstance()
        impl = document.getImplementation("/DemoApplication/SwComponentTypes/SWC_CyclicCounter/IB_SWC_CyclicCounter")
        assert(impl.getFullName() == "/DemoApplication/SwcImplementations/Impl_SWC_CyclicCounter")
        assert(isinstance(impl, SwcImplementation))

    def test_get_behavior(self):
        document = AUTOSAR.getInstance()
        behavior = document.getBehavior("/DemoApplication/SwcImplementations/Impl_SWC_CyclicCounter")
        assert(behavior.getFullName() == "/DemoApplication/SwComponentTypes/SWC_CyclicCounter/IB_SWC_CyclicCounter")
        assert(isinstance(behavior, InternalBehavior))

    def test_composition_sw_component_types(self):
        document = AUTOSAR.getInstance()
        sw_component = document.find("/DemoApplication/SwComponentTypes/TopLevelComposition")  
        assert(sw_component.short_name == "TopLevelComposition")
        assert(isinstance(sw_component, CompositionSwComponentType))
        prototypes = sw_component.getPortPrototypes()
        assert(len(prototypes) == 2)

    def test_composition_sw_component_types_sw_connectors(self):
        document = AUTOSAR.getInstance()
        sw_component = document.find("/DemoApplication/SwComponentTypes/TopLevelComposition")  
        assert(isinstance(sw_component, CompositionSwComponentType))
        assert(len(sw_component.getSwConnectors()) == 6)
        assert(len(sw_component.getAssemblySwConnectors()) == 3)
        assert(len(sw_component.getDelegationSwConnectors()) == 3)

        connector_name_list = set()
        for sw_connector in sw_component.getAssemblySwConnectors():
            connector_name_list.add(sw_connector.short_name)

        assert(connector_name_list == set(['a6a18805580c94537a4c82f6c289a4d', 'ac681652833fb4b12b920adab33a73b', 'ac681652833fb4b12b920adab33a73c']))

        sw_component.removeElement("a6a18805580c94537a4c82f6c289a4d")
        assert(len(sw_component.getAssemblySwConnectors()) == 2)

        # remove all the AssemblySwConnector
        sw_component.removeAllAssemblySwConnector()
        assert(len(sw_component.getAssemblySwConnectors()) == 0)
        assert(len(sw_component.getDelegationSwConnectors()) == 3)
        
        # remove all the DelegationSwConnector
        sw_component.removeAllDelegationSwConnector()
        assert(len(sw_component.getAssemblySwConnectors()) == 0)
        assert(len(sw_component.getDelegationSwConnectors()) == 0)
        
    def test_bswm_mode_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/BswMMode.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_Datatypes.arxml", document)

        assert(filecmp.cmp("src/armodel/tests/test_files/BswMMode.arxml", "data/generated_AUTOSAR_Datatypes.arxml", shallow = False) == True)

    def test_sw_record_demo_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/SwRecordDemo.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_SwRecordDemo.arxml", document)

        assert(filecmp.cmp("src/armodel/tests/test_files/SwRecordDemo.arxml", "data/generated_SwRecordDemo.arxml", shallow = False) == True)

    def test_application_data_type_blueprint_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml", document)

        assert(filecmp.cmp("test_files/AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml", "data/generated_AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml", shallow = False) == True)

    
        
        
