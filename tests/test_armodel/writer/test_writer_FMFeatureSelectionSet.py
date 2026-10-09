"""Writer tests for the FM-FEATURE-SELECTION-SET element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import FMFeatureSelectionSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureSelection
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeatureSelectionSet:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        selection_set = FMFeatureSelectionSet(self._parent(), "SelectionSet")
        selection_set.addFeatureModelRef(RefType().setValue("/Pkg/FeatureModel").setDest("FM-FEATURE-MODEL"))
        selection_set.addIncludeRef(RefType().setValue("/Pkg/OtherSet").setDest("FM-FEATURE-SELECTION-SET"))
        selection_set.addSelection(FMFeatureSelection(selection_set, "Selection"))
        return selection_set

    def test_write_all_members(self):
        selection_set = self._build_full()

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeatureSelectionSet(container, selection_set)
        element = container.find("FM-FEATURE-SELECTION-SET")

        assert element.find("SHORT-NAME").text == "SelectionSet"
        fm_ref = element.find("FEATURE-MODEL-REFS/FEATURE-MODEL-REF")
        assert fm_ref.text == "/Pkg/FeatureModel"
        assert fm_ref.attrib["DEST"] == "FM-FEATURE-MODEL"
        inc_ref = element.find("INCLUDE-REFS/INCLUDE-REF")
        assert inc_ref.text == "/Pkg/OtherSet"
        assert element.find("SELECTIONS/FM-FEATURE-SELECTION/SHORT-NAME").text == "Selection"

    def test_write_minimal(self):
        selection_set = FMFeatureSelectionSet(self._parent(), "SelectionSet")

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeatureSelectionSet(container, selection_set)
        element = container.find("FM-FEATURE-SELECTION-SET")

        assert element.find("FEATURE-MODEL-REFS") is None
        assert element.find("INCLUDE-REFS") is None
        assert element.find("SELECTIONS") is None

    def test_round_trip(self):
        selection_set = self._build_full()

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeatureSelectionSet(container, selection_set)
        element = container.find("FM-FEATURE-SELECTION-SET")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed_parent = self._parent()
        parsed = ARXMLParser().readFMFeatureSelectionSet(parsed_element, parsed_parent.createFMFeatureSelectionSet("SelectionSet"))
        assert parsed.getFeatureModelRefs()[0].getValue() == "/Pkg/FeatureModel"
        assert parsed.getIncludeRefs()[0].getValue() == "/Pkg/OtherSet"
        assert len(parsed.getSelections()) == 1
        assert parsed.getSelections()[0].getShortName() == "Selection"
