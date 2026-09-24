import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AtpMixedString import AtpMixedString
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class _Parent(ARObject):
    pass


class _Mixed(AtpMixedString):
    def __init__(self):
        super().__init__()


def test_read_mixed_string_text():
    e = ET.Element("COND-BY-FORMULA")
    e.text = "A and B"
    m = _Mixed()
    ARXMLParser().readMixedStringText(e, m)
    assert m.getMixedString() == "A and B"


def test_read_none_text_noop():
    e = ET.Element("COND-BY-FORMULA")
    m = _Mixed()
    ARXMLParser().readMixedStringText(e, m)
    assert m.getMixedString() is None


def test_write_mixed_string_text_and_omit():
    m = _Mixed()
    m.setMixedString("X or Y")
    e = ET.Element("COND")
    ARXMLWriter().writeMixedStringText(e, m)
    assert e.text == "X or Y"

    m2 = _Mixed()
    e2 = ET.Element("COND")
    ARXMLWriter().writeMixedStringText(e2, m2)
    assert e2.text is None
