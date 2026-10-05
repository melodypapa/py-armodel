"""
Writer tests for PHYSICAL-DIMENSION-MAPPING-SET — SWCT Table 5.78 (p.399, R23-11).

Builds a fully populated PhysicalDimensionMappingSet on an ARPackage, saves (the writer
validates every save against the bundled XSD), reloads and asserts every field value
round-trips — including the nested PHYSICAL-DIMENSION-MAPPING items of Table 5.77. The
PHYSICAL-DIMENSION-MAPPINGS wrapper is emitted only when non-empty (XSD minOccurs=0).

Round-trip counterpart: tests/test_armodel/parser/test_physical_dimension_mapping_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import PhysicalDimensionMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import PhysicalDimensionMappingSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


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


def _build_set(document):
    ar_package = document.createARPackage("PhysicalDimensionMappingSets")
    mapping_set = ar_package.createPhysicalDimensionMappingSet("EnergyTorqueMappings")

    mapping = PhysicalDimensionMapping()
    mapping.setFirstPhysicalDimensionRef(RefType().setDest("PHYSICAL-DIMENSION").setValue("/PhysicalDimensions/Energy"))
    mapping.setSecondPhysicalDimensionRef(RefType().setDest("PHYSICAL-DIMENSION").setValue("/PhysicalDimensions/Torque"))
    mapping_set.addPhysicalDimensionMapping(mapping)

    second = PhysicalDimensionMapping()
    second.setFirstPhysicalDimensionRef(RefType().setDest("PHYSICAL-DIMENSION").setValue("/PhysicalDimensions/Work"))
    second.setSecondPhysicalDimensionRef(RefType().setDest("PHYSICAL-DIMENSION").setValue("/PhysicalDimensions/Energy"))
    mapping_set.addPhysicalDimensionMapping(second)
    return mapping_set


def _write_set_element(mapping_set):
    writer = ARXMLWriter()
    writer.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    parent = ET.Element("ELEMENTS")
    writer.writePhysicalDimensionMappingSet(parent, mapping_set)
    return parent.find("PHYSICAL-DIMENSION-MAPPING-SET")


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


class TestPhysicalDimensionMappingSetWriter:
    """Writer coverage for the PHYSICAL-DIMENSION-MAPPING-SET content (Table 5.78)."""

    def test_write_physical_dimension_mapping_set_wrapper_and_items(self):
        child = _write_set_element(_build_set(_make_document()))
        wrapper = child.find("PHYSICAL-DIMENSION-MAPPINGS")
        assert wrapper is not None
        items = list(wrapper)
        assert [item.tag for item in items] == ["PHYSICAL-DIMENSION-MAPPING", "PHYSICAL-DIMENSION-MAPPING"]
        first_refs = [item.find("FIRST-PHYSICAL-DIMENSION-REF").text for item in items]
        assert first_refs == ["/PhysicalDimensions/Energy", "/PhysicalDimensions/Work"]
        second_refs = [item.find("SECOND-PHYSICAL-DIMENSION-REF").text for item in items]
        assert second_refs == ["/PhysicalDimensions/Torque", "/PhysicalDimensions/Energy"]

    def test_write_physical_dimension_mapping_set_empty_omits_wrapper(self):
        """A set without mappings emits no PHYSICAL-DIMENSION-MAPPINGS wrapper (XSD minOccurs=0)."""
        document = _make_document()
        document.createARPackage("PhysicalDimensionMappingSets").createPhysicalDimensionMappingSet("EmptyMappings")

        child = _write_set_element(document.getARPackages()[0].getPhysicalDimensionMappingSets()[0])
        assert child.find("PHYSICAL-DIMENSION-MAPPINGS") is None

    def test_physical_dimension_mapping_set_round_trip(self):
        """Save (XSD-validated) -> reload -> every field value survives, including nested mappings."""
        document = _make_document()
        _build_set(document)

        document_2 = _save_and_reload(document)
        sets = document_2.getARPackages()[0].getPhysicalDimensionMappingSets()
        assert len(sets) == 1
        reloaded = sets[0]
        assert isinstance(reloaded, PhysicalDimensionMappingSet)
        assert reloaded.getShortName() == "EnergyTorqueMappings"

        mappings = reloaded.getPhysicalDimensionMappings()
        assert len(mappings) == 2
        assert all(isinstance(m, PhysicalDimensionMapping) for m in mappings)
        assert mappings[0].getFirstPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Energy"
        assert mappings[0].getFirstPhysicalDimensionRef().getDest() == "PHYSICAL-DIMENSION"
        assert mappings[0].getSecondPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Torque"
        assert mappings[1].getFirstPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Work"
        assert mappings[1].getSecondPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Energy"

    def test_physical_dimension_mapping_set_round_trip_empty(self):
        """A set without mappings round-trips to an empty list."""
        document = _make_document()
        document.createARPackage("PhysicalDimensionMappingSets").createPhysicalDimensionMappingSet("EmptyMappings")

        document_2 = _save_and_reload(document)
        sets = document_2.getARPackages()[0].getPhysicalDimensionMappingSets()
        assert len(sets) == 1
        assert sets[0].getShortName() == "EmptyMappings"
        assert sets[0].getPhysicalDimensionMappings() == []
