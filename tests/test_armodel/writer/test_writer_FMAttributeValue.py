"""Writer tests for the FM-ATTRIBUTE-VALUE element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FMAttributeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMAttributeValue:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        value = FMAttributeValue()
        value.setDefinitionRef(RefType().setValue("/Pkg/AttrDef").setDest("FM-ATTRIBUTE-DEF"))
        numerical = Numerical()
        numerical.setValue(1.5)
        value.setValue(numerical)
        return value

    def test_write_all_members(self):
        self._parent()
        value = self._build_full()

        container = ET.Element("ATTRIBUTE-VALUES")
        ARXMLWriter().writeFMAttributeValue(container, value)
        element = container.find("FM-ATTRIBUTE-VALUE")

        definition_ref = element.find("DEFINITION-REF")
        assert definition_ref is not None
        assert definition_ref.text == "/Pkg/AttrDef"
        assert definition_ref.attrib["DEST"] == "FM-ATTRIBUTE-DEF"
        assert element.find("VALUE").text == "1.5"

    def test_write_minimal(self):
        self._parent()
        value = FMAttributeValue()

        container = ET.Element("ATTRIBUTE-VALUES")
        ARXMLWriter().writeFMAttributeValue(container, value)
        element = container.find("FM-ATTRIBUTE-VALUE")

        assert element.find("DEFINITION-REF") is None
        assert element.find("VALUE") is None

    def test_round_trip(self):
        self._parent()
        value = self._build_full()

        container = ET.Element("ATTRIBUTE-VALUES")
        ARXMLWriter().writeFMAttributeValue(container, value)
        element = container.find("FM-ATTRIBUTE-VALUE")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readFMAttributeValue(parsed_element, FMAttributeValue())
        assert parsed.getDefinitionRef().getValue() == "/Pkg/AttrDef"
        assert parsed.getDefinitionRef().getDest() == "FM-ATTRIBUTE-DEF"
        assert parsed.getValue().getValue() == 1.5
