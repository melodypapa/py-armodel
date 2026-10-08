"""Writer tests for the LOG-AND-TRACE-MESSAGE-COLLECTION-SET element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import LogAndTraceMessageCollectionSet
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import DltMessage
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteLogAndTraceMessageCollectionSet:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_with_items(self):
        value_set = LogAndTraceMessageCollectionSet(self._parent(), "ValueSet")
        value_set.addDltMessage(DltMessage(value_set, "Message"))

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeLogAndTraceMessageCollectionSet(container, value_set)
        element = container.find("LOG-AND-TRACE-MESSAGE-COLLECTION-SET")

        assert element.find("SHORT-NAME").text == "ValueSet"
        assert element.find("DLT-MESSAGES/DLT-MESSAGE") is not None

    def test_write_minimal(self):
        value_set = LogAndTraceMessageCollectionSet(self._parent(), "ValueSet")

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeLogAndTraceMessageCollectionSet(container, value_set)
        element = container.find("LOG-AND-TRACE-MESSAGE-COLLECTION-SET")

        assert element.find("DLT-MESSAGES") is None

    def test_round_trip(self):
        value_set = LogAndTraceMessageCollectionSet(self._parent(), "ValueSet")
        value_set.addDltMessage(DltMessage(value_set, "Message"))

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeLogAndTraceMessageCollectionSet(container, value_set)
        element = container.find("LOG-AND-TRACE-MESSAGE-COLLECTION-SET")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed_parent = self._parent()
        parsed = ARXMLParser().readLogAndTraceMessageCollectionSet(parsed_element, parsed_parent.createLogAndTraceMessageCollectionSet("ValueSet"))
        assert len(parsed.getDltMessages()) == 1
