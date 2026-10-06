"""
Writer tests for UNIT — SWCT Table 5.79 (p.400, R23-11).

Builds a fully populated Unit on an ARPackage, saves (the writer validates every save
against the bundled XSD), reloads and asserts every field value round-trips — including
the DISPLAY-NAME mixed text. Also pins the emission order to the AUTOSAR_00052.xsd group
UNIT element order (sequenceOffset 20..50).

Round-trip counterpart: tests/test_armodel/parser/test_unit.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Float, RefType
from armodel.models.M2.MSR.AsamHdo.Units import SingleLanguageUnitNames, Unit
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_UNIT_ORDER = [
    "DISPLAY-NAME",
    "FACTOR-SI-TO-UNIT",
    "OFFSET-SI-TO-UNIT",
    "PHYSICAL-DIMENSION-REF",
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


def _build_unit(document):
    unit = document.createARPackage("Units").createUnit("KmPerHour")
    display_name = SingleLanguageUnitNames()
    display_name.setMixedString("kilometer per hour")
    unit.setDisplayName(display_name)
    unit.setFactorSiToUnit(Float().setValue("3.6"))
    unit.setOffsetSiToUnit(Float().setValue("0.0"))
    unit.setPhysicalDimensionRef(RefType().setDest("PHYSICAL-DIMENSION").setValue("/PhysicalDimensions/Velocity"))
    return unit


def _write_unit_element(unit):
    writer = ARXMLWriter()
    writer.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    parent = ET.Element("ELEMENTS")
    writer.writeUnit(parent, unit)
    return parent.find("UNIT")


def _save_and_reload(document):
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, document)
        document_2 = _make_document()
        ARXMLParser().load(file_path, document_2)
        return document_2
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


class TestUnitWriter:
    """Writer coverage for the UNIT content (Table 5.79)."""

    def test_write_unit_child_order_follows_xsd(self):
        child = _write_unit_element(_build_unit(_make_document()))
        children = [c.tag for c in child if c.tag not in ("SHORT-NAME", "CATEGORY", "DESC", "ADMIN-DATA", "INTRODUCTION", "UUID")]
        assert children == XSD_UNIT_ORDER

    def test_write_unit_values(self):
        child = _write_unit_element(_build_unit(_make_document()))
        assert child.find("DISPLAY-NAME").text == "kilometer per hour"
        assert child.find("FACTOR-SI-TO-UNIT").text == "3.6"
        assert child.find("OFFSET-SI-TO-UNIT").text == "0.0"
        ref = child.find("PHYSICAL-DIMENSION-REF")
        assert ref.text == "/PhysicalDimensions/Velocity"
        assert ref.attrib["DEST"] == "PHYSICAL-DIMENSION"

    def test_unit_round_trip(self):
        """Save (XSD-validated) -> reload -> every field value survives."""
        document = _make_document()
        _build_unit(document)

        document_2 = _save_and_reload(document)
        units = document_2.getARPackages()[0].getUnits()
        assert len(units) == 1
        reloaded = units[0]
        assert isinstance(reloaded, Unit)
        assert reloaded.getShortName() == "KmPerHour"
        assert reloaded.getDisplayName().getMixedString() == "kilometer per hour"
        assert reloaded.getFactorSiToUnit().getValue() == 3.6
        assert reloaded.getOffsetSiToUnit().getValue() == 0.0
        assert reloaded.getPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Velocity"
        assert reloaded.getPhysicalDimensionRef().getDest() == "PHYSICAL-DIMENSION"

    def test_unit_round_trip_empty(self):
        """A UNIT without content elements writes no content and reloads with all None."""
        document = _make_document()
        document.createARPackage("Units").createUnit("NoUnit")

        document_2 = _save_and_reload(document)
        reloaded = document_2.getARPackages()[0].getUnits()[0]
        assert reloaded.getShortName() == "NoUnit"
        assert reloaded.getDisplayName() is None
        assert reloaded.getFactorSiToUnit() is None
        assert reloaded.getOffsetSiToUnit() is None
        assert reloaded.getPhysicalDimensionRef() is None
