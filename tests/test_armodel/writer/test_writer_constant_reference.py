"""Reader/writer round-trip tests for ConstantReference (Table 5.117)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ArrayValueSpecification, ConstantReference
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

CONST_VALUE = "/DemoApplication/ConstantSpecifications/CONST_1"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


def _ref() -> RefType:
    ref = RefType()
    ref.setDest("CONSTANT-SPECIFICATION")
    ref.setValue(CONST_VALUE)
    return ref


def _parent():
    return ET.Element("PARENT")


def test_write_constant_reference(writer):
    parent = _parent()
    spec = ConstantReference()
    spec.setShortLabel(Identifier().setValue("crs"))
    spec.setConstantRef(_ref())

    writer.setConstantReference(parent, spec)

    tag = parent.find("CONSTANT-REFERENCE")
    assert tag is not None
    children = list(tag)
    assert [child.tag for child in children] == ["SHORT-LABEL", "CONSTANT-REF"]
    assert children[0].text == "crs"
    assert children[1].attrib["DEST"] == "CONSTANT-SPECIFICATION"
    assert children[1].text == CONST_VALUE


def test_write_constant_reference_empty(writer):
    parent = _parent()
    writer.setConstantReference(parent, ConstantReference())

    tag = parent.find("CONSTANT-REFERENCE")
    assert tag is not None
    assert tag.find("CONSTANT-REF") is None


def test_constant_reference_round_trip(writer):
    spec = ConstantReference()
    spec.setShortLabel(Identifier().setValue("crs"))
    spec.setConstantRef(_ref())

    parent = _parent()
    writer.setConstantReference(parent, spec)

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getValueSpecification(reparsed[0], "CONSTANT-REFERENCE")
    assert isinstance(reloaded, ConstantReference)
    assert reloaded.getShortLabel().getValue() == "crs"
    assert isinstance(reloaded.getConstantRef(), RefType)
    assert reloaded.getConstantRef().getValue() == CONST_VALUE
    assert reloaded.getConstantRef().getDest() == "CONSTANT-SPECIFICATION"


def test_constant_reference_round_trip_in_array(writer):
    array_spec = ArrayValueSpecification()
    spec = ConstantReference()
    spec.setConstantRef(_ref())
    array_spec.addElement(spec)

    parent = _parent()
    writer.writeArrayValueSpecification(parent, array_spec)

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getValueSpecification(reparsed[0], "ARRAY-VALUE-SPECIFICATION")
    assert isinstance(reloaded, ArrayValueSpecification)
    elements = reloaded.getElements()
    assert len(elements) == 1
    assert isinstance(elements[0], ConstantReference)
    assert elements[0].getConstantRef().getValue() == CONST_VALUE
