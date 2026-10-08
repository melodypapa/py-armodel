"""Writer tests for the FM-FEATURE-DECOMPOSITION element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FMFeatureDecomposition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString, PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeatureDecomposition:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        decomposition = FMFeatureDecomposition()
        category = CategoryString()
        category.setValue("MULTIPLEFEATURE")
        decomposition.setCategory(category)
        decomposition.addFeatureRef(RefType().setValue("/Pkg/Feature").setDest("FM-FEATURE"))
        max_value = PositiveInteger()
        max_value.setValue(5)
        decomposition.setMax(max_value)
        min_value = PositiveInteger()
        min_value.setValue(2)
        decomposition.setMin(min_value)
        return decomposition

    def test_write_all_members(self):
        self._parent()
        decomposition = self._build_full()

        container = ET.Element("DECOMPOSITIONS")
        ARXMLWriter().writeFMFeatureDecomposition(container, decomposition)
        element = container.find("FM-FEATURE-DECOMPOSITION")

        assert element.find("CATEGORY").text == "MULTIPLEFEATURE"
        feature_ref = element.find("FEATURE-REFS/FEATURE-REF")
        assert feature_ref is not None
        assert feature_ref.text == "/Pkg/Feature"
        assert feature_ref.attrib["DEST"] == "FM-FEATURE"
        assert element.find("MAX").text == "5"
        assert element.find("MIN").text == "2"

    def test_write_minimal(self):
        self._parent()
        decomposition = FMFeatureDecomposition()

        container = ET.Element("DECOMPOSITIONS")
        ARXMLWriter().writeFMFeatureDecomposition(container, decomposition)
        element = container.find("FM-FEATURE-DECOMPOSITION")

        assert element.find("CATEGORY") is None
        assert element.find("FEATURE-REFS") is None
        assert element.find("MAX") is None
        assert element.find("MIN") is None

    def test_round_trip(self):
        self._parent()
        decomposition = self._build_full()

        container = ET.Element("DECOMPOSITIONS")
        ARXMLWriter().writeFMFeatureDecomposition(container, decomposition)
        element = container.find("FM-FEATURE-DECOMPOSITION")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readFMFeatureDecomposition(parsed_element, FMFeatureDecomposition())
        assert parsed.getCategory().getValue() == "MULTIPLEFEATURE"
        assert parsed.getFeatureRefs()[0].getValue() == "/Pkg/Feature"
        assert parsed.getMax().getValue() == 5
        assert parsed.getMin().getValue() == 2
