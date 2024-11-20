import filecmp
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Components import CompositionSwComponentType
from ....writer.arxml_writer import ARXMLWriter
from ....parser.arxml_parser import ARXMLParser
from ....models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

class TestSystemTemplate:
    def setup_method(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/CanSystem.arxml", document)

    
    def test_bswm_mode_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("src/armodel/tests/test_files/CanSystem.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_CanSystem.arxml", document)

        #assert(filecmp.cmp("src/armodel/tests/test_files/CanSystem.arxml", "data/generated_CanSystem.arxml", shallow = False) == True)

        

    
        
        
