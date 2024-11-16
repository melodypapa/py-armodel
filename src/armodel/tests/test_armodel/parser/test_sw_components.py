import filecmp
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import CompositionSwComponentType
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
        
    def test_software_components_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/SoftwareComponents.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated.arxml", document)

        assert(filecmp.cmp("src/armodel/tests/test_files/SoftwareComponents.arxml", "data/generated.arxml", shallow = False) == True)

    def test_software_components_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/AUTOSAR_Datatypes.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_Datatypes.arxml", document)

        assert(filecmp.cmp("src/armodel/tests/test_files/AUTOSAR_Datatypes.arxml", "data/generated_AUTOSAR_Datatypes.arxml", shallow = False) == True)

    def test_bswm_mode_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/BswMMode.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_AUTOSAR_Datatypes.arxml", document)

        assert(filecmp.cmp("src/armodel/tests/test_files/BswMMode.arxml", "data/generated_AUTOSAR_Datatypes.arxml", shallow = False) == True)

        

    
        
        
