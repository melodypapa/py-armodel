"""Reader/writer round-trip tests for ConstantSpecification (Table 5.108)."""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ConstantSpecification, NumericalValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


def _parent():
    return ET.Element("ELEMENTS")


def _make_document() -> AUTOSAR:
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document


def _fill_value_spec(spec: ConstantSpecification):
    value_spec = NumericalValueSpecification()
    numerical = ARNumerical()
    numerical.setValue("3.14")
    value_spec.setValue(numerical)
    spec.setValueSpec(value_spec)


def test_write_constant_specification(writer):
    document = _make_document()
    spec = document.createARPackage("Pkg").createConstantSpecification("MyConstant")
    _fill_value_spec(spec)

    parent = _parent()
    writer.writeConstantSpecification(parent, spec)

    tag = parent.find("CONSTANT-SPECIFICATION")
    assert tag is not None
    children = list(tag)
    assert [child.tag for child in children] == ["SHORT-NAME", "VALUE-SPEC"]
    assert children[0].text == "MyConstant"
    assert children[1].find("NUMERICAL-VALUE-SPECIFICATION") is not None


def test_write_constant_specification_empty(writer):
    document = _make_document()
    spec = document.createARPackage("Pkg").createConstantSpecification("EmptyConstant")

    parent = _parent()
    writer.writeConstantSpecification(parent, spec)

    tag = parent.find("CONSTANT-SPECIFICATION")
    assert tag is not None
    assert tag.find("VALUE-SPEC") is None


def test_constant_specification_round_trip(writer):
    document = _make_document()
    spec = document.createARPackage("Pkg").createConstantSpecification("MyConstant")
    _fill_value_spec(spec)

    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        writer.save(file_path, document)

        document_2 = _make_document()
        ARXMLParser().load(file_path, document_2)

        constants = document_2.getARPackages()[0].getConstantSpecifications()
        assert len(constants) == 1
        reloaded = constants[0]
        assert isinstance(reloaded, ConstantSpecification)
        assert reloaded.getShortName() == "MyConstant"
        value_spec = reloaded.getValueSpec()
        assert isinstance(value_spec, NumericalValueSpecification)
        assert value_spec.getValue().getValue() == 3.14
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
