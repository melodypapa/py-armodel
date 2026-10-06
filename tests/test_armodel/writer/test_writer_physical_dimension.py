"""
Writer tests for PHYSICAL-DIMENSION — SWCT Table 5.76 (p.398, R23-11).

Builds a fully populated PhysicalDimension, saves it through an ARPackage (the writer
validates every save against the bundled XSD), reloads and asserts every field value
round-trips. Also pins the emission order to the AUTOSAR_00052.xsd group
PHYSICAL-DIMENSION element order (sequenceOffset 20..80).

Round-trip counterpart: tests/test_armodel/parser/test_physical_dimension.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical
from armodel.models.M2.MSR.AsamHdo.Units import PhysicalDimension
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_DIMENSION_ORDER = [
    "LENGTH-EXP",
    "MASS-EXP",
    "TIME-EXP",
    "CURRENT-EXP",
    "TEMPERATURE-EXP",
    "MOLAR-AMOUNT-EXP",
    "LUMINOUS-INTENSITY-EXP",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_document() -> AUTOSAR:
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document


def _build_dimension(document):
    dimension = document.createARPackage("PhysicalDimensions").createPhysicalDimension("Energy")
    dimension.setLengthExp(Numerical().setValue("2"))
    dimension.setMassExp(Numerical().setValue("1"))
    dimension.setTimeExp(Numerical().setValue("-2"))
    dimension.setCurrentExp(Numerical().setValue("0"))
    dimension.setTemperatureExp(Numerical().setValue("0"))
    dimension.setMolarAmountExp(Numerical().setValue("0"))
    dimension.setLuminousIntensityExp(Numerical().setValue("0"))
    return dimension


def _write_dimension_element(dimension):
    writer = ARXMLWriter()
    writer.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    parent = ET.Element("ELEMENTS")
    writer.writePhysicalDimension(parent, dimension)
    return parent.find("PHYSICAL-DIMENSION")


class TestPhysicalDimensionWriter:
    """Writer coverage for the PHYSICAL-DIMENSION content (Table 5.76)."""

    def test_write_physical_dimension_child_order_follows_xsd(self):
        child = _write_dimension_element(_build_dimension(_make_document()))
        children = [c.tag for c in child if c.tag not in ("SHORT-NAME", "CATEGORY", "DESC", "ADMIN-DATA", "INTRODUCTION", "UUID")]
        assert children == XSD_DIMENSION_ORDER

    def test_write_physical_dimension_values(self):
        child = _write_dimension_element(_build_dimension(_make_document()))
        assert child.find("LENGTH-EXP").text == "2"
        assert child.find("MASS-EXP").text == "1"
        assert child.find("TIME-EXP").text == "-2"
        assert child.find("CURRENT-EXP").text == "0"
        assert child.find("TEMPERATURE-EXP").text == "0"
        assert child.find("MOLAR-AMOUNT-EXP").text == "0"
        assert child.find("LUMINOUS-INTENSITY-EXP").text == "0"

    def test_physical_dimension_round_trip(self):
        """Save (XSD-validated) -> reload -> every field value survives."""
        document = _make_document()
        _build_dimension(document)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = _make_document()
            ARXMLParser().load(file_path, document_2)

            dimensions = document_2.getARPackages()[0].getEcucPhysicalDimensions()
            assert len(dimensions) == 1
            reloaded = dimensions[0]
            assert isinstance(reloaded, PhysicalDimension)
            assert reloaded.getShortName() == "Energy"
            assert reloaded.getLengthExp().getValue() == 2
            assert reloaded.getMassExp().getValue() == 1
            assert reloaded.getTimeExp().getValue() == -2
            assert reloaded.getCurrentExp().getValue() == 0
            assert reloaded.getTemperatureExp().getValue() == 0
            assert reloaded.getMolarAmountExp().getValue() == 0
            assert reloaded.getLuminousIntensityExp().getValue() == 0
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_physical_dimension_round_trip_empty(self):
        """A PHYSICAL-DIMENSION without exponents writes no exp elements and reloads with all None."""
        document = _make_document()
        document.createARPackage("PhysicalDimensions").createPhysicalDimension("NoDimension")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = _make_document()
            ARXMLParser().load(file_path, document_2)

            reloaded = document_2.getARPackages()[0].getEcucPhysicalDimensions()[0]
            assert reloaded.getShortName() == "NoDimension"
            assert reloaded.getCurrentExp() is None
            assert reloaded.getLengthExp() is None
            assert reloaded.getLuminousIntensityExp() is None
            assert reloaded.getMassExp() is None
            assert reloaded.getMolarAmountExp() is None
            assert reloaded.getTemperatureExp() is None
            assert reloaded.getTimeExp() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
