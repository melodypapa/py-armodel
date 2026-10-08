"""Writer tests for the POST-BUILD-VARIANT-CRITERION-VALUE-SET element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import PostBuildVariantCriterionValueSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCriterionValue
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWritePostBuildVariantCriterionValueSet:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_with_items(self):
        value_set = PostBuildVariantCriterionValueSet(self._parent(), "ValueSet")
        value_set.addPostBuildVariantCriterionValue(PostBuildVariantCriterionValue())

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writePostBuildVariantCriterionValueSet(container, value_set)
        element = container.find("POST-BUILD-VARIANT-CRITERION-VALUE-SET")

        assert element.find("SHORT-NAME").text == "ValueSet"
        assert element.find("POST-BUILD-VARIANT-CRITERION-VALUES/POST-BUILD-VARIANT-CRITERION-VALUE") is not None

    def test_write_minimal(self):
        value_set = PostBuildVariantCriterionValueSet(self._parent(), "ValueSet")

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writePostBuildVariantCriterionValueSet(container, value_set)
        element = container.find("POST-BUILD-VARIANT-CRITERION-VALUE-SET")

        assert element.find("POST-BUILD-VARIANT-CRITERION-VALUES") is None

    def test_round_trip(self):
        value_set = PostBuildVariantCriterionValueSet(self._parent(), "ValueSet")
        value_set.addPostBuildVariantCriterionValue(PostBuildVariantCriterionValue())

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writePostBuildVariantCriterionValueSet(container, value_set)
        element = container.find("POST-BUILD-VARIANT-CRITERION-VALUE-SET")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed_parent = self._parent()
        parsed = ARXMLParser().readPostBuildVariantCriterionValueSet(parsed_element, parsed_parent.createPostBuildVariantCriterionValueSet("ValueSet"))
        assert len(parsed.getPostBuildVariantCriterionValues()) == 1
