import filecmp
from pathlib import Path

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestSystemTemplate:
    def setup_method(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        test_file = Path(__file__).parent.parent.parent / "integration_tests" / "test_files" / "CanSystem.arxml"
        parser.load(str(test_file), document)

    def test_can_system_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        test_file = Path(__file__).parent.parent.parent / "integration_tests" / "test_files" / "CanSystem.arxml"
        parser.load(str(test_file), document)

        writer = ARXMLWriter()
        output_file = Path(__file__).parent.parent.parent / "test_armodel" / "parser" / "data" / "generated_CanSystem.arxml"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        writer.save(str(output_file), document)

        assert (filecmp.cmp(str(test_file), str(output_file), shallow=False) is True)
