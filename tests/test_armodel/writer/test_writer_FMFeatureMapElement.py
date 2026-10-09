"""Writer tests for the FM-FEATURE-MAP-ELEMENT element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureMapAssertion, FMFeatureMapCondition, FMFeatureMapElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeatureMapElement:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        map_element = FMFeatureMapElement(self._parent(), "MapElement")
        assertion = FMFeatureMapAssertion(map_element, "Assertion")
        map_element.addAssertion(assertion)
        condition = FMFeatureMapCondition(map_element, "Condition")
        map_element.addCondition(condition)
        map_element.addPostBuildVariantCriterionValueSetRef(RefType().setValue("/Pkg/PostBuildValueSet").setDest("POST-BUILD-VARIANT-CRITERION-VALUE-SET"))
        map_element.addSwSystemconstantValueSetRef(RefType().setValue("/Pkg/SwSystemconstantValueSet").setDest("SW-SYSTEMCONSTANT-VALUE-SET"))
        return map_element

    def test_write_all_members(self):
        map_element = self._build_full()

        container = ET.Element("MAPPINGS")
        ARXMLWriter().writeFMFeatureMapElement(container, map_element)
        element = container.find("FM-FEATURE-MAP-ELEMENT")

        assert element.find("SHORT-NAME").text == "MapElement"
        assert element.find("ASSERTIONS/FM-FEATURE-MAP-ASSERTION/SHORT-NAME").text == "Assertion"
        assert element.find("CONDITIONS/FM-FEATURE-MAP-CONDITION/SHORT-NAME").text == "Condition"
        pb_ref = element.find("POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS/POST-BUILD-VARIANT-CRITERION-VALUE-SET-REF")
        assert pb_ref.text == "/Pkg/PostBuildValueSet"
        assert pb_ref.attrib["DEST"] == "POST-BUILD-VARIANT-CRITERION-VALUE-SET"
        sw_ref = element.find("SW-SYSTEMCONSTANT-VALUE-SET-REFS/SW-SYSTEMCONSTANT-VALUE-SET-REF")
        assert sw_ref.text == "/Pkg/SwSystemconstantValueSet"
        assert sw_ref.attrib["DEST"] == "SW-SYSTEMCONSTANT-VALUE-SET"

    def test_write_minimal(self):
        map_element = FMFeatureMapElement(self._parent(), "MapElement")

        container = ET.Element("MAPPINGS")
        ARXMLWriter().writeFMFeatureMapElement(container, map_element)
        element = container.find("FM-FEATURE-MAP-ELEMENT")

        assert element.find("ASSERTIONS") is None
        assert element.find("CONDITIONS") is None
        assert element.find("POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS") is None
        assert element.find("SW-SYSTEMCONSTANT-VALUE-SET-REFS") is None

    def test_round_trip(self):
        map_element = self._build_full()

        container = ET.Element("MAPPINGS")
        ARXMLWriter().writeFMFeatureMapElement(container, map_element)
        element = container.find("FM-FEATURE-MAP-ELEMENT")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readFMFeatureMapElement(parsed_element, FMFeatureMapElement(self._parent(), "MapElement"))
        assert len(parsed.getAssertions()) == 1
        assert parsed.getAssertions()[0].getShortName() == "Assertion"
        assert len(parsed.getConditions()) == 1
        assert parsed.getConditions()[0].getShortName() == "Condition"
        assert parsed.getPostBuildVariantCriterionValueSetRefs()[0].getValue() == "/Pkg/PostBuildValueSet"
        assert parsed.getSwSystemconstantValueSetRefs()[0].getValue() == "/Pkg/SwSystemconstantValueSet"
