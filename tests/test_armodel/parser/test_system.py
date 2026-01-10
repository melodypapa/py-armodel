import filecmp
from src.armodel.writer.arxml_writer import ARXMLWriter
from src.armodel.parser.arxml_parser import ARXMLParser
from src.armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestSystemTemplate:
    def setup_method(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/CanSystem.arxml", document)
    
    def test_can_system_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        parser.load("test_files/CanSystem.arxml", document)

        writer = ARXMLWriter()
        writer.save("data/generated_CanSystem.arxml", document)

        assert (filecmp.cmp("test_files/CanSystem.arxml", "data/generated_CanSystem.arxml", shallow=False) is True)
