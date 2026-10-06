"""
Tests for reading PHYSICAL-DIMENSION-MAPPING — SWCT Table 5.77 (p.399, R23-11).

PhysicalDimensionMapping (Base = ARObject) is a plain nested object aggregated by
PhysicalDimensionMappingSet.physicalDimensionMapping (Table 5.78). The reader populates
the model via its mutators in the XSD element order of the AUTOSAR_00052.xsd group
PHYSICAL-DIMENSION-MAPPING (FIRST-PHYSICAL-DIMENSION-REF, SECOND-PHYSICAL-DIMENSION-REF)
and carries the AUTOSAR_00052.xsd AR-OBJECT S/T attributes via readARObject.

Round-trip counterpart: tests/test_armodel/writer/test_writer_physical_dimension_mapping.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import PhysicalDimensionMapping
from armodel.parser.arxml_parser import ARXMLParser

MAPPING_XML = """
<PHYSICAL-DIMENSION-MAPPING xmlns="http://autosar.org/schema/r4.0" S="4321">
    <FIRST-PHYSICAL-DIMENSION-REF DEST="PHYSICAL-DIMENSION">/PhysicalDimensions/Energy</FIRST-PHYSICAL-DIMENSION-REF>
    <SECOND-PHYSICAL-DIMENSION-REF DEST="PHYSICAL-DIMENSION">/PhysicalDimensions/Torque</SECOND-PHYSICAL-DIMENSION-REF>
</PHYSICAL-DIMENSION-MAPPING>
"""

FIRST_ONLY_MAPPING_XML = """
<PHYSICAL-DIMENSION-MAPPING xmlns="http://autosar.org/schema/r4.0">
    <FIRST-PHYSICAL-DIMENSION-REF DEST="PHYSICAL-DIMENSION">/PhysicalDimensions/Energy</FIRST-PHYSICAL-DIMENSION-REF>
</PHYSICAL-DIMENSION-MAPPING>
"""

EMPTY_MAPPING_XML = """
<PHYSICAL-DIMENSION-MAPPING xmlns="http://autosar.org/schema/r4.0"/>
"""


def _load_mapping(xml_text):
    parser = ARXMLParser()
    parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    element = ET.fromstring(xml_text)
    mapping = PhysicalDimensionMapping()
    parser.readPhysicalDimensionMapping(element, mapping)
    return mapping


class TestPhysicalDimensionMappingParser:
    """Reader coverage for the PHYSICAL-DIMENSION-MAPPING content (Table 5.77)."""

    def test_read_physical_dimension_mapping_refs(self):
        mapping = _load_mapping(MAPPING_XML)
        assert mapping.getFirstPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Energy"
        assert mapping.getFirstPhysicalDimensionRef().getDest() == "PHYSICAL-DIMENSION"
        assert mapping.getSecondPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Torque"
        assert mapping.getSecondPhysicalDimensionRef().getDest() == "PHYSICAL-DIMENSION"

    def test_read_physical_dimension_mapping_checksum(self):
        """The AR-OBJECT S attribute round-trips into the checksum (Rule 0025)."""
        mapping = _load_mapping(MAPPING_XML)
        assert mapping.getChecksum() is not None
        assert mapping.getChecksum().getValue() == "4321"

    def test_read_physical_dimension_mapping_first_only(self):
        """A mapping carrying only FIRST-PHYSICAL-DIMENSION-REF leaves secondPhysicalDimensionRef None."""
        mapping = _load_mapping(FIRST_ONLY_MAPPING_XML)
        assert mapping.getFirstPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Energy"
        assert mapping.getSecondPhysicalDimensionRef() is None

    def test_read_physical_dimension_mapping_empty(self):
        """An empty PHYSICAL-DIMENSION-MAPPING leaves both refs None (both attrs 0..1)."""
        mapping = _load_mapping(EMPTY_MAPPING_XML)
        assert mapping.getFirstPhysicalDimensionRef() is None
        assert mapping.getSecondPhysicalDimensionRef() is None
