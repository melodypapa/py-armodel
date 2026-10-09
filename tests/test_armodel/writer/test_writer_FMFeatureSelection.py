"""Writer tests for the FM-FEATURE-SELECTION element (XSD emission order per xml.sequenceOffset)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FMAttributeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureSelection
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import FMFeatureSelectionState, Numerical, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeatureSelection:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        selection = FMFeatureSelection(self._parent(), "Selection")
        selection.setFeatureRef(RefType().setValue("/Pkg/Feature").setDest("FM-FEATURE"))
        state = FMFeatureSelectionState()
        state.setValue(FMFeatureSelectionState.SELECTED)
        selection.setState(state)
        minimum = BindingTimeEnum()
        minimum.setValue("PRE-COMPILE-TIME")
        selection.setMinimumSelectedBindingTime(minimum)
        maximum = BindingTimeEnum()
        maximum.setValue("SYSTEM-DESIGN-TIME")
        selection.setMaximumSelectedBindingTime(maximum)
        value = FMAttributeValue()
        numerical = Numerical()
        numerical.setValue(1.5)
        value.setValue(numerical)
        selection.addAttributeValue(value)
        return selection

    def test_write_all_members(self):
        selection = self._build_full()

        container = ET.Element("SELECTIONS")
        ARXMLWriter().writeFMFeatureSelection(container, selection)
        element = container.find("FM-FEATURE-SELECTION")

        assert element.find("SHORT-NAME").text == "Selection"
        feature_ref = element.find("FEATURE-REF")
        assert feature_ref.text == "/Pkg/Feature"
        assert feature_ref.attrib["DEST"] == "FM-FEATURE"
        assert element.find("STATE").text == "SELECTED"
        assert element.find("MINIMUM-SELECTED-BINDING-TIME").text == "PRE-COMPILE-TIME"
        assert element.find("MAXIMUM-SELECTED-BINDING-TIME").text == "SYSTEM-DESIGN-TIME"
        assert element.find("ATTRIBUTE-VALUES/FM-ATTRIBUTE-VALUE") is not None
        # xml.sequenceOffset emission order: FEATURE-REF, STATE, MIN-, MAX-, ATTRIBUTE-VALUES
        tags = [child.tag for child in element]
        assert tags.index("FEATURE-REF") < tags.index("STATE") < tags.index("MINIMUM-SELECTED-BINDING-TIME") < tags.index("MAXIMUM-SELECTED-BINDING-TIME") < tags.index("ATTRIBUTE-VALUES")

    def test_write_minimal(self):
        selection = FMFeatureSelection(self._parent(), "Selection")

        container = ET.Element("SELECTIONS")
        ARXMLWriter().writeFMFeatureSelection(container, selection)
        element = container.find("FM-FEATURE-SELECTION")

        assert element.find("FEATURE-REF") is None
        assert element.find("STATE") is None
        assert element.find("ATTRIBUTE-VALUES") is None

    def test_round_trip(self):
        selection = self._build_full()

        container = ET.Element("SELECTIONS")
        ARXMLWriter().writeFMFeatureSelection(container, selection)
        element = container.find("FM-FEATURE-SELECTION")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readFMFeatureSelection(parsed_element, FMFeatureSelection(self._parent(), "Selection"))
        assert parsed.getFeatureRef().getValue() == "/Pkg/Feature"
        assert parsed.getState().getValue() == "SELECTED"
        assert parsed.getMinimumSelectedBindingTime().getValue() == "PRE-COMPILE-TIME"
        assert parsed.getMaximumSelectedBindingTime().getValue() == "SYSTEM-DESIGN-TIME"
        assert len(parsed.getAttributeValues()) == 1
        assert parsed.getAttributeValues()[0].getValue().getValue() == 1.5
