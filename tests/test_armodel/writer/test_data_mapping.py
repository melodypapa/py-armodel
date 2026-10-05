"""Writer round-trip tests for the abstract DataMapping base (Table 5.22, p.217).

XML element order per XSD group DATA-MAPPING: COMMUNICATION-DIRECTION, INTRODUCTION,
then VARIATION-POINT (the remaining group members carry atp.Status="removed" and are
not modeled). COMMUNICATION-DIRECTION is a Rule 0019 legacy member (R4.3.1 Table 5.14,
removed in R23-11) kept because authentic R22-11 SystemMapping fixtures carry it.
The helper is exercised through a test-local concrete subclass because DataMapping
itself has no standalone element and no dispatch branch until its concrete
subtypes are synced.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import CommunicationDirectionType
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class _ConcreteDataMapping(DataMapping):
    pass


def _communication_direction(value="in") -> CommunicationDirectionType:
    direction = CommunicationDirectionType()
    direction.setValue(value)
    return direction


def _new_mapping_with_introduction() -> DataMapping:
    mapping = _ConcreteDataMapping()
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue("Mapping intro")
    paragraph.addL1(l1)
    block = DocumentationBlock()
    block.addP(paragraph)
    mapping.setIntroduction(block)
    return mapping


def _new_mapping_full() -> DataMapping:
    mapping = _new_mapping_with_introduction()
    mapping.setCommunicationDirection(_communication_direction("in"))
    return mapping


def _write(mapping: DataMapping) -> ET.Element:
    element = ET.Element("CONCRETE-MAPPING")
    ARXMLWriter().writeDataMapping(element, mapping)
    return element


class TestWriteDataMapping:
    def test_write_introduction(self):
        element = _write(_new_mapping_with_introduction())

        introduction = element.find("INTRODUCTION")
        assert introduction is not None
        assert introduction.find("P/L-1").text == "Mapping intro"

    def test_write_communication_direction(self):
        element = _write(_new_mapping_full())

        direction = element.find("COMMUNICATION-DIRECTION")
        assert direction is not None
        assert direction.text == "in"

    def test_write_empty_mapping_omits_elements(self):
        element = _write(_ConcreteDataMapping())

        assert element.find("COMMUNICATION-DIRECTION") is None
        assert element.find("INTRODUCTION") is None
        assert element.find("VARIATION-POINT") is None
        assert len(element) == 0

    def test_write_xsd_order(self):
        element = _write(_new_mapping_full())

        assert [child.tag for child in element] == ["COMMUNICATION-DIRECTION", "INTRODUCTION"]

    def test_round_trip_field_values(self):
        source = ET.Element("CONCRETE-MAPPING")
        ARXMLWriter().writeDataMapping(source, _new_mapping_full())

        # namespaced reparse, as a file load provides (children inherit the root xmlns)
        wrapped = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(source, encoding="unicode")))
        mapping = _ConcreteDataMapping()
        ARXMLParser().readDataMapping(wrapped[0], mapping)

        assert mapping.getCommunicationDirection().getValue() == "in"

        target = ET.Element("CONCRETE-MAPPING")
        ARXMLWriter().writeDataMapping(target, mapping)

        assert target.find("COMMUNICATION-DIRECTION").text == "in"
        assert target.find("INTRODUCTION/P/L-1").text == "Mapping intro"
        assert len(target) == 2
