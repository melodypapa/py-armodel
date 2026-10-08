"""Writer tests for the FM-FEATURE-MODEL element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import FMFeatureModel
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeatureModel:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        feature_model = FMFeatureModel(self._parent(), "FeatureModel")
        feature_model.addFeatureRef(RefType().setValue("/Pkg/Feature").setDest("FM-FEATURE"))
        feature_model.setRootRef(RefType().setValue("/Pkg/Root").setDest("FM-FEATURE"))
        return feature_model

    def test_write_all_members(self):
        feature_model = self._build_full()

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeatureModel(container, feature_model)
        element = container.find("FM-FEATURE-MODEL")

        assert element.find("SHORT-NAME").text == "FeatureModel"
        feature_ref = element.find("FEATURE-REFS/FEATURE-REF")
        assert feature_ref.text == "/Pkg/Feature"
        assert feature_ref.attrib["DEST"] == "FM-FEATURE"
        root_ref = element.find("ROOT-REF")
        assert root_ref.text == "/Pkg/Root"
        assert root_ref.attrib["DEST"] == "FM-FEATURE"

    def test_write_minimal(self):
        feature_model = FMFeatureModel(self._parent(), "FeatureModel")

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeatureModel(container, feature_model)
        element = container.find("FM-FEATURE-MODEL")

        assert element.find("FEATURE-REFS") is None
        assert element.find("ROOT-REF") is None

    def test_round_trip(self):
        feature_model = self._build_full()

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeatureModel(container, feature_model)
        element = container.find("FM-FEATURE-MODEL")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed_parent = self._parent()
        parsed = ARXMLParser().readFMFeatureModel(parsed_element, parsed_parent.createFMFeatureModel("FeatureModel"))
        assert parsed.getFeatureRefs()[0].getValue() == "/Pkg/Feature"
        assert parsed.getRootRef().getValue() == "/Pkg/Root"
