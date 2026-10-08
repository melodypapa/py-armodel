"""Writer/reader round-trip tests for SOMEIPTransformationDescription (Table 7.10, p.777).

Element order per the XSD complexType SOMEIP-TRANSFORMATION-DESCRIPTION:
DESCRIBABLE content, TRANSFORMATION-DESCRIPTION (VARIATION-POINT), then
ALIGNMENT, BYTE-ORDER, INTERFACE-VERSION.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ByteOrderEnum, CategoryString, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    SOMEIPTransformationDescription,
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


def _full_desc() -> SOMEIPTransformationDescription:
    desc = SOMEIPTransformationDescription()
    desc.setCategory(CategoryString().setValue("someipCategory"))
    desc.setAlignment(PositiveInteger().setValue("8"))
    desc.setByteOrder(ByteOrderEnum().setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST))
    desc.setInterfaceVersion(PositiveInteger().setValue("4"))
    return desc


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


class TestSOMEIPTransformationDescriptionWriter:
    def test_write_someip_transformation_description_full(self, writer):
        parent = ET.Element("PARENT")
        writer.writeSOMEIPTransformationDescription(parent, _full_desc())
        el = parent[0]

        assert el.tag == "SOMEIP-TRANSFORMATION-DESCRIPTION"
        assert el.find("ALIGNMENT").text == "8"
        assert el.find("BYTE-ORDER").text == "MOST-SIGNIFICANT-BYTE-FIRST"
        assert el.find("INTERFACE-VERSION").text == "4"
        assert el.find("CATEGORY").text == "someipCategory"

        children = [child.tag for child in el]
        assert children.index("CATEGORY") < children.index("ALIGNMENT")
        assert children.index("ALIGNMENT") < children.index("BYTE-ORDER")
        assert children.index("BYTE-ORDER") < children.index("INTERFACE-VERSION")

    def test_write_someip_transformation_description_empty(self, writer):
        parent = ET.Element("PARENT")
        writer.writeSOMEIPTransformationDescription(parent, SOMEIPTransformationDescription())
        el = parent[0]

        assert el.tag == "SOMEIP-TRANSFORMATION-DESCRIPTION"
        assert el.find("ALIGNMENT") is None
        assert el.find("BYTE-ORDER") is None
        assert el.find("INTERFACE-VERSION") is None

    def test_write_technology_dispatch_someip(self, writer):
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        tech.setTransformationDescription(_full_desc())

        parent = ET.Element("PARENT")
        writer.writeTransformationTechnology(parent, tech)

        wrapper = parent.find("TRANSFORMATION-TECHNOLOGY/TRANSFORMATION-DESCRIPTIONS")
        assert wrapper is not None
        desc_el = wrapper.find("SOMEIP-TRANSFORMATION-DESCRIPTION")
        assert desc_el is not None
        assert desc_el.find("ALIGNMENT").text == "8"


class TestSOMEIPTransformationDescriptionRoundTrip:
    def test_round_trip_preserves_someip_attributes(self, writer, parser, tmp_path):
        tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        tech.setTransformationDescription(_full_desc())

        parent = ET.Element("TRANSFORMATION-TECHNOLOGY")
        writer.writeTransformationTechnology(parent, tech)

        out_file = str(tmp_path / "someip_transformation_description.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent[0]), encoding="unicode"))

        recovered_tech = TransformationTechnology(AUTOSAR.getInstance(), "tech1")
        tree = ET.parse(out_file)
        parser.readTransformationTechnology(tree.getroot()[0], recovered_tech)

        recovered = recovered_tech.getTransformationDescription()
        assert isinstance(recovered, SOMEIPTransformationDescription)
        assert recovered.getCategory() is not None
        assert recovered.getCategory().getValue() == "someipCategory"
        assert recovered.getAlignment() is not None
        assert recovered.getAlignment().getValue() == 8
        assert recovered.getByteOrder() is not None
        assert recovered.getByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-FIRST"
        assert recovered.getInterfaceVersion() is not None
        assert recovered.getInterfaceVersion().getValue() == 4
