"""Writer round-trip tests for ConstantSpecificationMapping (Table 5.118)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ConstantSpecificationMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def test_write_constant_specification_mapping(writer):
    parent = _parent()
    mapping = ConstantSpecificationMapping()
    mapping.setApplConstantRef(RefType().setValue("/Appl/Const"))
    mapping.setImplConstantRef(RefType().setValue("/Impl/Const"))

    writer.writeConstantSpecificationMapping(parent, mapping)

    tag = parent.find("CONSTANT-SPECIFICATION-MAPPING")
    assert tag is not None
    appl = tag.find("APPL-CONSTANT-REF")
    assert appl is not None
    assert appl.text == "/Appl/Const"
    impl = tag.find("IMPL-CONSTANT-REF")
    assert impl is not None
    assert impl.text == "/Impl/Const"


def test_write_constant_specification_mapping_empty(writer):
    parent = _parent()
    writer.writeConstantSpecificationMapping(parent, ConstantSpecificationMapping())

    tag = parent.find("CONSTANT-SPECIFICATION-MAPPING")
    assert tag is not None
    assert tag.find("APPL-CONSTANT-REF") is None
    assert tag.find("IMPL-CONSTANT-REF") is None


def test_constant_specification_mapping_round_trip(writer):
    mapping = ConstantSpecificationMapping()
    mapping.setApplConstantRef(RefType().setValue("/Appl/Const"))
    mapping.setImplConstantRef(RefType().setValue("/Impl/Const"))

    parent = _parent()
    writer.writeConstantSpecificationMapping(parent, mapping)

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getConstantSpecificationMapping(reparsed[0])
    assert reloaded is not None
    assert reloaded.getApplConstantRef().getValue() == "/Appl/Const"
    assert reloaded.getImplConstantRef().getValue() == "/Impl/Const"
