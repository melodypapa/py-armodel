import logging

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier
from armodel.parser.arxml_parser import ARXMLParser
from armodel.validation import PrimitivePatternError
from armodel.writer.arxml_writer import ARXMLWriter


def _build_arxml_with_type(tmp_path, type_text):
    document = AUTOSAR.getInstance()
    document.new()
    document.setARRelease("R23-11")
    package = document.createARPackage("Pkg")
    swc = package.createApplicationSwComponentType("Swc")
    behavior = swc.createSwcInternalBehavior("Ib")
    memory = behavior.createPerInstanceMemory("Pim")
    memory.setType(CIdentifier().setValue(type_text))
    filename = str(tmp_path / "pim.arxml")
    ARXMLWriter().save(filename, document)
    with open(filename) as handle:
        return handle.read(), filename


class TestParserPatternIntegration:
    def test_bad_value_raises_by_default(self, tmp_path):
        xml_text, filename = _build_arxml_with_type(tmp_path, "U8")
        bad_text = xml_text.replace("<TYPE>U8</TYPE>", "<TYPE>9BAD</TYPE>")
        assert bad_text != xml_text
        with open(filename, "w") as handle:
            handle.write(bad_text)
        AUTOSAR.getInstance().new()
        parser = ARXMLParser(options={"validate": False})
        with pytest.raises(PrimitivePatternError):
            parser.load(filename, AUTOSAR.getInstance())

    def test_bad_value_warns_with_warning_option(self, tmp_path, caplog):
        xml_text, filename = _build_arxml_with_type(tmp_path, "U8")
        bad_text = xml_text.replace("<TYPE>U8</TYPE>", "<TYPE>9BAD</TYPE>")
        with open(filename, "w") as handle:
            handle.write(bad_text)
        AUTOSAR.getInstance().new()
        parser = ARXMLParser(options={"validate": False, "warning": True})
        with caplog.at_level(logging.WARNING, logger="armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes"):
            parser.load(filename, AUTOSAR.getInstance())
        assert any("9BAD" in record.message for record in caplog.records)
