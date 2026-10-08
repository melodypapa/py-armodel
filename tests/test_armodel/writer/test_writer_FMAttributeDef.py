"""Writer tests for the FM-ATTRIBUTE-DEF element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMAttributeDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Limit, Numerical
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMAttributeDef:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        attribute_def = FMAttributeDef(self._parent(), "AttrDef")
        numerical = Numerical()
        numerical.setValue(1.5)
        attribute_def.setDefaultValue(numerical)
        max_limit = Limit()
        max_limit.setValue("10")
        attribute_def.setMax(max_limit)
        min_limit = Limit()
        min_limit.setValue("1")
        attribute_def.setMin(min_limit)
        return attribute_def

    def test_write_all_members(self):
        attribute_def = self._build_full()

        container = ET.Element("ATTRIBUTE-DEFS")
        ARXMLWriter().writeFMAttributeDef(container, attribute_def)
        element = container.find("FM-ATTRIBUTE-DEF")

        assert element.find("SHORT-NAME").text == "AttrDef"
        assert element.find("DEFAULT-VALUE").text == "1.5"
        assert element.find("MAX").text == "10"
        assert element.find("MIN").text == "1"

    def test_write_minimal(self):
        attribute_def = FMAttributeDef(self._parent(), "AttrDef")

        container = ET.Element("ATTRIBUTE-DEFS")
        ARXMLWriter().writeFMAttributeDef(container, attribute_def)
        element = container.find("FM-ATTRIBUTE-DEF")

        assert element.find("DEFAULT-VALUE") is None
        assert element.find("MAX") is None
        assert element.find("MIN") is None

    def test_round_trip(self):
        attribute_def = self._build_full()

        container = ET.Element("ATTRIBUTE-DEFS")
        ARXMLWriter().writeFMAttributeDef(container, attribute_def)
        element = container.find("FM-ATTRIBUTE-DEF")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readFMAttributeDef(parsed_element, FMAttributeDef(self._parent(), "AttrDef"))
        assert parsed.getShortName() == "AttrDef"
        assert parsed.getDefaultValue().getValue() == 1.5
        assert parsed.getMax().getValue() == "10"
        assert parsed.getMin().getValue() == "1"
