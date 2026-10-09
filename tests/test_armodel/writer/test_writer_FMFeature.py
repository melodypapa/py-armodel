"""Writer tests for the FM-FEATURE element (AR-PACKAGE element round-trip)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FMFeatureDecomposition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import FMFeature
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMAttributeDef, FMFeatureRelation, FMFeatureRestriction
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeature:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        feature = FMFeature(self._parent(), "Feature")
        feature.addAttributeDef(FMAttributeDef(feature, "AttrDef"))
        decomposition = FMFeatureDecomposition()
        category = CategoryString()
        category.setValue("MANDATORYFEATURE")
        decomposition.setCategory(category)
        feature.addDecomposition(decomposition)
        maximum = BindingTimeEnum()
        maximum.setValue("SYSTEM-DESIGN-TIME")
        feature.setMaximumIntendedBindingTime(maximum)
        minimum = BindingTimeEnum()
        minimum.setValue("PRE-COMPILE-TIME")
        feature.setMinimumIntendedBindingTime(minimum)
        feature.addRelation(FMFeatureRelation(feature, "Relation"))
        feature.addRestriction(FMFeatureRestriction(feature, "Restriction"))
        return feature

    def test_write_all_members(self):
        feature = self._build_full()

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeature(container, feature)
        element = container.find("FM-FEATURE")

        assert element.find("SHORT-NAME").text == "Feature"
        assert element.find("ATTRIBUTE-DEFS/FM-ATTRIBUTE-DEF/SHORT-NAME").text == "AttrDef"
        assert element.find("DECOMPOSITIONS/FM-FEATURE-DECOMPOSITION/CATEGORY").text == "MANDATORYFEATURE"
        assert element.find("MAXIMUM-INTENDED-BINDING-TIME").text == "SYSTEM-DESIGN-TIME"
        assert element.find("MINIMUM-INTENDED-BINDING-TIME").text == "PRE-COMPILE-TIME"
        assert element.find("RELATIONS/FM-FEATURE-RELATION/SHORT-NAME").text == "Relation"
        assert element.find("RESTRICTIONS/FM-FEATURE-RESTRICTION/SHORT-NAME").text == "Restriction"

    def test_write_minimal(self):
        feature = FMFeature(self._parent(), "Feature")

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeature(container, feature)
        element = container.find("FM-FEATURE")

        assert element.find("ATTRIBUTE-DEFS") is None
        assert element.find("DECOMPOSITIONS") is None
        assert element.find("MAXIMUM-INTENDED-BINDING-TIME") is None
        assert element.find("RELATIONS") is None
        assert element.find("RESTRICTIONS") is None

    def test_round_trip_via_ar_package(self):
        parent = self._parent()
        feature = parent.createFMFeature("Feature")
        feature.addAttributeDef(FMAttributeDef(feature, "AttrDef"))

        pkg_element = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(pkg_element, feature)
        element = pkg_element.find("FM-FEATURE")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed_parent = self._parent()
        parsed = ARXMLParser().readFMFeature(parsed_element, parsed_parent.createFMFeature("Feature"))
        assert parsed.getShortName() == "Feature"
        assert len(parsed.getAttributeDefs()) == 1
        assert parsed.getAttributeDefs()[0].getShortName() == "AttrDef"
