"""
Writer tests for PHYSICAL-DIMENSION-MAPPING — SWCT Table 5.77 (p.399, R23-11).

Builds a fully populated PhysicalDimensionMapping, writes it via the writer helper, reloads
it and asserts every field value round-trips. Also pins the emission order to the
AUTOSAR_00052.xsd group PHYSICAL-DIMENSION-MAPPING element order (FIRST-PHYSICAL-DIMENSION-REF
before SECOND-PHYSICAL-DIMENSION-REF) and the AR-OBJECT S/T attributes (Rule 0025).

Round-trip counterpart: tests/test_armodel/parser/test_physical_dimension_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import PhysicalDimensionMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_MAPPING_ORDER = [
    "FIRST-PHYSICAL-DIMENSION-REF",
    "SECOND-PHYSICAL-DIMENSION-REF",
]

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest, value):
    return RefType().setDest(dest).setValue(value)


def _build_mapping():
    mapping = PhysicalDimensionMapping()
    mapping.setChecksum(String().setValue("4321"))
    mapping.setFirstPhysicalDimensionRef(_ref("PHYSICAL-DIMENSION", "/PhysicalDimensions/Energy"))
    mapping.setSecondPhysicalDimensionRef(_ref("PHYSICAL-DIMENSION", "/PhysicalDimensions/Torque"))
    return mapping


def _write_mapping(mapping):
    writer = ARXMLWriter()
    writer.nsmap = {"xmlns": NS}
    parent = ET.Element("WRAPPER", {"xmlns": NS})
    writer.writePhysicalDimensionMapping(parent, mapping)
    return parent.find("PHYSICAL-DIMENSION-MAPPING")


def _read_mapping(child):
    parser = ARXMLParser()
    parser.nsmap = {"xmlns": NS}
    child.set("xmlns", NS)
    element = ET.fromstring(ET.tostring(child, encoding="unicode"))
    mapping = PhysicalDimensionMapping()
    parser.readPhysicalDimensionMapping(element, mapping)
    return mapping


class TestPhysicalDimensionMappingWriter:
    """Writer coverage for the PHYSICAL-DIMENSION-MAPPING content (Table 5.77)."""

    def test_write_physical_dimension_mapping_refs(self):
        child = _write_mapping(_build_mapping())
        first_ref = child.find("FIRST-PHYSICAL-DIMENSION-REF")
        second_ref = child.find("SECOND-PHYSICAL-DIMENSION-REF")
        assert first_ref.text == "/PhysicalDimensions/Energy"
        assert first_ref.attrib["DEST"] == "PHYSICAL-DIMENSION"
        assert second_ref.text == "/PhysicalDimensions/Torque"
        assert second_ref.attrib["DEST"] == "PHYSICAL-DIMENSION"

    def test_write_physical_dimension_mapping_child_order_follows_xsd(self):
        child = _write_mapping(_build_mapping())
        children = [c.tag for c in child]
        assert children == XSD_MAPPING_ORDER

    def test_write_physical_dimension_mapping_checksum(self):
        """The AR-OBJECT S attribute is emitted (Rule 0025, writer side)."""
        child = _write_mapping(_build_mapping())
        assert child.attrib["S"] == "4321"

    def test_physical_dimension_mapping_round_trip(self):
        """Write -> reload -> every field value survives."""
        reloaded = _read_mapping(_write_mapping(_build_mapping()))
        assert reloaded.getChecksum().getValue() == "4321"
        assert reloaded.getFirstPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Energy"
        assert reloaded.getFirstPhysicalDimensionRef().getDest() == "PHYSICAL-DIMENSION"
        assert reloaded.getSecondPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Torque"
        assert reloaded.getSecondPhysicalDimensionRef().getDest() == "PHYSICAL-DIMENSION"

    def test_physical_dimension_mapping_round_trip_empty(self):
        """A mapping without refs writes no ref elements and reloads with both None."""
        mapping = PhysicalDimensionMapping()
        child = _write_mapping(mapping)
        assert child.find("FIRST-PHYSICAL-DIMENSION-REF") is None
        assert child.find("SECOND-PHYSICAL-DIMENSION-REF") is None
        reloaded = _read_mapping(child)
        assert reloaded.getFirstPhysicalDimensionRef() is None
        assert reloaded.getSecondPhysicalDimensionRef() is None
