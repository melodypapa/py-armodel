"""
Tests for reading PHYSICAL-DIMENSION-MAPPING-SET — SWCT Table 5.78 (p.399, R23-11).

PhysicalDimensionMappingSet (Base = ARElement) is aggregated by ARPackage.element. The
reader walks the PHYSICAL-DIMENSION-MAPPINGS wrapper (AUTOSAR_00052.xsd group
PHYSICAL-DIMENSION-MAPPING-SET) and populates the model via addPhysicalDimensionMapping,
reading each nested PHYSICAL-DIMENSION-MAPPING through readPhysicalDimensionMapping
(Table 5.77).

Round-trip counterpart: tests/test_armodel/writer/test_writer_physical_dimension_mapping_set.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import PhysicalDimensionMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import PhysicalDimensionMappingSet
from armodel.parser.arxml_parser import ARXMLParser

FULL_SET_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>PhysicalDimensionMappingSets</SHORT-NAME>
            <ELEMENTS>
                <PHYSICAL-DIMENSION-MAPPING-SET>
                    <SHORT-NAME>EnergyTorqueMappings</SHORT-NAME>
                    <PHYSICAL-DIMENSION-MAPPINGS>
                        <PHYSICAL-DIMENSION-MAPPING>
                            <FIRST-PHYSICAL-DIMENSION-REF DEST="PHYSICAL-DIMENSION">/PhysicalDimensions/Energy</FIRST-PHYSICAL-DIMENSION-REF>
                            <SECOND-PHYSICAL-DIMENSION-REF DEST="PHYSICAL-DIMENSION">/PhysicalDimensions/Torque</SECOND-PHYSICAL-DIMENSION-REF>
                        </PHYSICAL-DIMENSION-MAPPING>
                        <PHYSICAL-DIMENSION-MAPPING>
                            <FIRST-PHYSICAL-DIMENSION-REF DEST="PHYSICAL-DIMENSION">/PhysicalDimensions/Work</FIRST-PHYSICAL-DIMENSION-REF>
                            <SECOND-PHYSICAL-DIMENSION-REF DEST="PHYSICAL-DIMENSION">/PhysicalDimensions/Energy</SECOND-PHYSICAL-DIMENSION-REF>
                        </PHYSICAL-DIMENSION-MAPPING>
                    </PHYSICAL-DIMENSION-MAPPINGS>
                </PHYSICAL-DIMENSION-MAPPING-SET>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501

EMPTY_SET_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>PhysicalDimensionMappingSets</SHORT-NAME>
            <ELEMENTS>
                <PHYSICAL-DIMENSION-MAPPING-SET>
                    <SHORT-NAME>EmptyMappings</SHORT-NAME>
                    <PHYSICAL-DIMENSION-MAPPINGS/>
                </PHYSICAL-DIMENSION-MAPPING-SET>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501

NO_WRAPPER_SET_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>PhysicalDimensionMappingSets</SHORT-NAME>
            <ELEMENTS>
                <PHYSICAL-DIMENSION-MAPPING-SET>
                    <SHORT-NAME>NoMappings</SHORT-NAME>
                </PHYSICAL-DIMENSION-MAPPING-SET>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501


def _load_set(xml_text):
    parser = ARXMLParser()
    parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    element = ET.fromstring(xml_text)
    document = AUTOSARDoc()
    parser.readARPackages(element, document)
    ar_package = document.getARPackages()[0]
    sets = ar_package.getPhysicalDimensionMappingSets()
    assert len(sets) == 1
    return sets[0]


class TestPhysicalDimensionMappingSetParser:
    """Reader coverage for the PHYSICAL-DIMENSION-MAPPING-SET content (Table 5.78)."""

    def test_read_physical_dimension_mapping_set_short_name(self):
        mapping_set = _load_set(FULL_SET_XML)
        assert isinstance(mapping_set, PhysicalDimensionMappingSet)
        assert mapping_set.getShortName() == "EnergyTorqueMappings"

    def test_read_physical_dimension_mapping_set_mappings(self):
        """Both nested PHYSICAL-DIMENSION-MAPPING items round-trip with their field values."""
        mapping_set = _load_set(FULL_SET_XML)
        mappings = mapping_set.getPhysicalDimensionMappings()
        assert len(mappings) == 2
        assert all(isinstance(m, PhysicalDimensionMapping) for m in mappings)
        assert mappings[0].getFirstPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Energy"
        assert mappings[0].getFirstPhysicalDimensionRef().getDest() == "PHYSICAL-DIMENSION"
        assert mappings[0].getSecondPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Torque"
        assert mappings[1].getFirstPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Work"
        assert mappings[1].getSecondPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Energy"

    def test_read_physical_dimension_mapping_set_empty_wrapper(self):
        """An empty PHYSICAL-DIMENSION-MAPPINGS wrapper yields an empty list."""
        mapping_set = _load_set(EMPTY_SET_XML)
        assert mapping_set.getPhysicalDimensionMappings() == []

    def test_read_physical_dimension_mapping_set_absent_wrapper(self):
        """A PHYSICAL-DIMENSION-MAPPING-SET without the wrapper yields an empty list (0..*)."""
        mapping_set = _load_set(NO_WRAPPER_SET_XML)
        assert mapping_set.getPhysicalDimensionMappings() == []
