"""Parser tests for the LOG-AND-TRACE-MESSAGE-COLLECTION-SET element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import LogAndTraceMessageCollectionSet
from armodel.parser.arxml_parser import ARXMLParser


def _parent():
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document.createARPackage("AUTOSAR")


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    xml_str = re.sub(r"^(<[A-Za-z][\w.-]*)", r'\1 xmlns="http://autosar.org/schema/r4.0"', xml_str)
    return ET.fromstring(xml_str)


class TestReadLogAndTraceMessageCollectionSet:
    def test_read_with_items(self):
        element = ET.Element("LOG-AND-TRACE-MESSAGE-COLLECTION-SET")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "ValueSet"
        wrapper_tag = ET.SubElement(element, "DLT-MESSAGES")
        dlt_message = ET.SubElement(wrapper_tag, "DLT-MESSAGE")
        ET.SubElement(dlt_message, "SHORT-NAME").text = "Message"

        parent = _parent()
        obj = ARXMLParser().readLogAndTraceMessageCollectionSet(_round_trip(element), parent.createLogAndTraceMessageCollectionSet("ValueSet"))
        assert obj.getShortName() == "ValueSet"
        assert len(obj.getDltMessages()) == 1

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("LOG-AND-TRACE-MESSAGE-COLLECTION-SET")

        obj = ARXMLParser().readLogAndTraceMessageCollectionSet(_round_trip(element), parent.createLogAndTraceMessageCollectionSet("ValueSet"))
        assert obj.getDltMessages() == []
