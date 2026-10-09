"""Writer tests for the FM-FEATURE-RELATION element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureRelation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeatureRelation:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        relation = FMFeatureRelation(self._parent(), "Relation")
        relation.addFeatureRef(RefType().setValue("/Pkg/Feature").setDest("FM-FEATURE"))
        condition = FMConditionByFeaturesAndAttributes()
        condition.setMixedString("feature == true")
        relation.setRestriction(condition)
        return relation

    def test_write_all_members(self):
        relation = self._build_full()

        container = ET.Element("RELATIONS")
        ARXMLWriter().writeFMFeatureRelation(container, relation)
        element = container.find("FM-FEATURE-RELATION")

        assert element.find("SHORT-NAME").text == "Relation"
        feature_ref = element.find("FEATURE-REFS/FEATURE-REF")
        assert feature_ref is not None
        assert feature_ref.text == "/Pkg/Feature"
        assert feature_ref.attrib["DEST"] == "FM-FEATURE"
        assert element.find("RESTRICTION").text == "feature == true"

    def test_write_minimal(self):
        relation = FMFeatureRelation(self._parent(), "Relation")

        container = ET.Element("RELATIONS")
        ARXMLWriter().writeFMFeatureRelation(container, relation)
        element = container.find("FM-FEATURE-RELATION")

        assert element.find("FEATURE-REFS") is None
        assert element.find("RESTRICTION") is None

    def test_round_trip(self):
        relation = self._build_full()

        container = ET.Element("RELATIONS")
        ARXMLWriter().writeFMFeatureRelation(container, relation)
        element = container.find("FM-FEATURE-RELATION")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readFMFeatureRelation(parsed_element, FMFeatureRelation(self._parent(), "Relation"))
        assert parsed.getFeatureRefs()[0].getValue() == "/Pkg/Feature"
        assert parsed.getFeatureRefs()[0].getDest() == "FM-FEATURE"
        assert parsed.getRestriction().getMixedString() == "feature == true"
