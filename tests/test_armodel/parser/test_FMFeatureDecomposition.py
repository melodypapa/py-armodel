"""Parser tests for the FM-FEATURE-DECOMPOSITION element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FMFeatureDecomposition
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


class TestReadFMFeatureDecomposition:
    def test_read_all_members(self):
        element = ET.Element("FM-FEATURE-DECOMPOSITION")
        category = ET.SubElement(element, "CATEGORY")
        category.text = "MULTIPLEFEATURE"
        refs_tag = ET.SubElement(element, "FEATURE-REFS")
        feature_ref = ET.SubElement(refs_tag, "FEATURE-REF")
        feature_ref.attrib["DEST"] = "FM-FEATURE"
        feature_ref.text = "/Pkg/Feature"
        max_element = ET.SubElement(element, "MAX")
        max_element.text = "5"
        min_element = ET.SubElement(element, "MIN")
        min_element.text = "2"

        obj = ARXMLParser().readFMFeatureDecomposition(_round_trip(element), FMFeatureDecomposition())
        assert obj.getCategory() is not None
        assert obj.getCategory().getValue() == "MULTIPLEFEATURE"
        assert len(obj.getFeatureRefs()) == 1
        assert obj.getFeatureRefs()[0].getValue() == "/Pkg/Feature"
        assert obj.getFeatureRefs()[0].getDest() == "FM-FEATURE"
        assert obj.getMax().getValue() == 5
        assert obj.getMin().getValue() == 2

    def test_read_minimal(self):
        element = ET.Element("FM-FEATURE-DECOMPOSITION")

        obj = ARXMLParser().readFMFeatureDecomposition(_round_trip(element), FMFeatureDecomposition())
        assert obj.getCategory() is None
        assert obj.getFeatureRefs() == []
        assert obj.getMax() is None
        assert obj.getMin() is None


class TestFMFeatureDecompositionSTAttributes:
    def test_round_trip_preserves_s_t_attributes(self):
        """The reader/writer must call readARObject/writeARObject (Rule 0025) so the AR-OBJECT
        attributeGroup S/T checksum/timestamp attributes survive a write→parse round-trip."""
        element = ET.Element("FM-FEATURE-DECOMPOSITION")
        element.attrib["S"] = "CHECKSUM-1"
        element.attrib["T"] = "2026-10-09T12:00:00+01:00"

        from armodel.writer.arxml_writer import ARXMLWriter

        parsed = ARXMLParser().readFMFeatureDecomposition(_round_trip(element), FMFeatureDecomposition())
        assert parsed.getChecksum() is not None
        assert parsed.getChecksum().getValue() == "CHECKSUM-1"
        assert parsed.getTimestamp() is not None

        container = ET.Element("DECOMPOSITIONS")
        ARXMLWriter().writeFMFeatureDecomposition(container, parsed)
        child = container.find("FM-FEATURE-DECOMPOSITION")
        assert child.attrib["S"] == "CHECKSUM-1"
        assert child.attrib["T"] == "2026-10-09T12:00:00+01:00"
