"""Writer/reader round-trip tests for UserDefinedTransformationDescription (Table 7.7, p.771).

Zero own attributes; the emitted USER-DEFINED-TRANSFORMATION-DESCRIPTION element
carries only the Describable content and the TRANSFORMATION-DESCRIPTION group
(VARIATION-POINT), per the XSD complexType sequence.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    TransformationTechnology,
    UserDefinedTransformationDescription,
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


def _full_desc() -> UserDefinedTransformationDescription:
    desc = UserDefinedTransformationDescription()
    desc.setCategory(CategoryString().setValue("custom"))
    return desc


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


class TestUserDefinedTransformationDescriptionWriter:
    def test_write_user_defined_transformation_description(self, writer):
        parent = ET.Element("PARENT")
        writer.writeUserDefinedTransformationDescription(parent, _full_desc())
        el = parent[0]

        assert el.tag == "USER-DEFINED-TRANSFORMATION-DESCRIPTION"
        assert el.find("CATEGORY").text == "custom"

    def test_write_user_defined_transformation_description_empty(self, writer):
        parent = ET.Element("PARENT")
        writer.writeUserDefinedTransformationDescription(parent, UserDefinedTransformationDescription())
        el = parent[0]

        assert el.tag == "USER-DEFINED-TRANSFORMATION-DESCRIPTION"
        assert len(el) == 0

    def test_write_technology_dispatch_user_defined(self, writer):
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        tech.setTransformationDescription(_full_desc())

        parent = ET.Element("PARENT")
        writer.writeTransformationTechnology(parent, tech)

        wrapper = parent.find("TRANSFORMATION-TECHNOLOGY/TRANSFORMATION-DESCRIPTIONS")
        assert wrapper is not None
        desc_el = wrapper.find("USER-DEFINED-TRANSFORMATION-DESCRIPTION")
        assert desc_el is not None
        assert desc_el.find("CATEGORY").text == "custom"


class TestUserDefinedTransformationDescriptionRoundTrip:
    def test_round_trip_preserves_user_defined_attributes(self, writer, parser, tmp_path):
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        tech.setTransformationDescription(_full_desc())

        parent = ET.Element("TRANSFORMATION-TECHNOLOGY")
        writer.writeTransformationTechnology(parent, tech)

        out_file = str(tmp_path / "user_defined_transformation_description.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent[0]), encoding="unicode"))

        recovered_tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        tree = ET.parse(out_file)
        parser.readTransformationTechnology(tree.getroot()[0], recovered_tech)

        recovered = recovered_tech.getTransformationDescription()
        assert isinstance(recovered, UserDefinedTransformationDescription)
        assert recovered.getCategory() is not None
        assert recovered.getCategory().getValue() == "custom"
