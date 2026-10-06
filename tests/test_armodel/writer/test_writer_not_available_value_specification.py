"""Writer round-trip tests for NotAvailableValueSpecification (Table 5.116)."""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NotAvailableValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
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


def test_write_not_available_value_specification(writer):
    parent = _parent()
    spec = NotAvailableValueSpecification()
    spec.setDefaultPattern(PositiveInteger().setValue("4"))

    writer.writeNotAvailableValueSpecification(parent, spec)

    tag = parent.find("NOT-AVAILABLE-VALUE-SPECIFICATION")
    assert tag is not None
    dp = tag.find("DEFAULT-PATTERN")
    assert dp is not None
    assert dp.text == "4"


def test_write_not_available_value_specification_empty(writer):
    parent = _parent()
    writer.writeNotAvailableValueSpecification(parent, NotAvailableValueSpecification())

    tag = parent.find("NOT-AVAILABLE-VALUE-SPECIFICATION")
    assert tag is not None
    assert tag.find("DEFAULT-PATTERN") is None


def test_not_available_value_specification_round_trip(writer):
    spec = NotAvailableValueSpecification()
    spec.setDefaultPattern(PositiveInteger().setValue("4"))

    parent = _parent()
    writer.writeNotAvailableValueSpecification(parent, spec)

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getValueSpecification(reparsed[0], "NOT-AVAILABLE-VALUE-SPECIFICATION")
    assert isinstance(reloaded, NotAvailableValueSpecification)
    assert reloaded.getDefaultPattern().getValue() == 4


class TestNotAvailableValueSpecificationDocumentRoundTrip:
    def test_round_trip_full_field_values(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"
        pkg = document.createARPackage("Consts")
        constant = pkg.createConstantSpecification("C1")
        spec = NotAvailableValueSpecification()
        spec.setDefaultPattern(PositiveInteger().setValue("255"))
        constant.setValueSpec(spec)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            constant_2 = document_2.getARPackages()[0].getConstantSpecifications()[0]
            value_spec_2 = constant_2.getValueSpec()
            assert isinstance(value_spec_2, NotAvailableValueSpecification)
            assert value_spec_2.getDefaultPattern() is not None
            assert value_spec_2.getDefaultPattern().getValue() == 255
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"
        pkg = document.createARPackage("Consts")
        constant = pkg.createConstantSpecification("C2")
        constant.setValueSpec(NotAvailableValueSpecification())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            constant_2 = document_2.getARPackages()[0].getConstantSpecifications()[0]
            value_spec_2 = constant_2.getValueSpec()
            assert isinstance(value_spec_2, NotAvailableValueSpecification)
            assert value_spec_2.getDefaultPattern() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
