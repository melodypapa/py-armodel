"""Writer/reader round-trip tests for TransformationDescription (Table 4.89, p.199).

Abstract class (Base = ARObject, Describable) — exercised through its concrete
subclass EndToEndTransformationDescription. VARIATION-POINT is serialized between
the Describable content and the subclass's own fields (XSD complexType sequence:
AR-OBJECT, DESCRIBABLE, TRANSFORMATION-DESCRIPTION, subclass group).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString, Identifier, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationDescription,
    TransformationTechnology,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _full_desc():
    desc = EndToEndTransformationDescription()
    desc.setCategory(CategoryString().setValue("myCategory"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(Identifier().setValue("vp1"))
    desc.setVariationPoint(variation_point)
    desc.setCounterOffset(PositiveInteger().setValue("8"))
    return desc


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


class TestTransformationDescriptionWriter:
    def test_write_transformation_description_with_variation_point(self, writer):
        parent = ET.Element("PARENT")
        writer.writeEndToEndTransformationDescription(parent, _full_desc())
        el = parent[0]

        vp_element = el.find("VARIATION-POINT")
        assert vp_element is not None
        assert vp_element.find("SHORT-LABEL") is not None
        assert vp_element.find("SHORT-LABEL").text == "vp1"

        children = [child.tag for child in el]
        assert children.index("CATEGORY") < children.index("VARIATION-POINT")
        assert children.index("VARIATION-POINT") < children.index("COUNTER-OFFSET")

    def test_write_transformation_description_without_variation_point(self, writer):
        desc = EndToEndTransformationDescription()
        desc.setCategory(CategoryString().setValue("myCategory"))
        desc.setCounterOffset(PositiveInteger().setValue("8"))

        parent = ET.Element("PARENT")
        writer.writeEndToEndTransformationDescription(parent, desc)
        el = parent[0]

        assert el.find("VARIATION-POINT") is None
        assert el.find("CATEGORY") is not None
        assert el.find("COUNTER-OFFSET").text == "8"

    def test_write_technology_without_transformation_description(self, writer):
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")

        parent = ET.Element("PARENT")
        writer.writeTransformationTechnology(parent, tech)

        assert parent.find("TRANSFORMATION-DESCRIPTIONS") is None


class TestTransformationDescriptionRoundTrip:
    def test_round_trip_preserves_variation_point(self, writer, parser, tmp_path):
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        tech.setTransformationDescription(_full_desc())

        parent = ET.Element("TRANSFORMATION-TECHNOLOGY")
        writer.writeTransformationTechnology(parent, tech)

        out_file = str(tmp_path / "transformation_description.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent[0]), encoding="unicode"))

        recovered_tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        tree = ET.parse(out_file)
        parser.readTransformationTechnology(tree.getroot()[0], recovered_tech)

        recovered = recovered_tech.getTransformationDescription()
        assert isinstance(recovered, EndToEndTransformationDescription)
        assert recovered.getCategory() is not None
        assert recovered.getCategory().getValue() == "myCategory"
        assert recovered.getCounterOffset() is not None
        assert recovered.getCounterOffset().getValue() == 8

        variation_point = recovered.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel() is not None
        assert variation_point.getShortLabel().getValue() == "vp1"
