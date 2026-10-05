"""
Tests for reading UNIT — SWCT Table 5.79 (p.400, R23-11).

Unit (Base = ARElement) is aggregated by ARPackage.element. The reader populates the
model via its mutators in the XSD element order of the AUTOSAR_00052.xsd group UNIT
(sequenceOffset 20..50: DISPLAY-NAME, FACTOR-SI-TO-UNIT, OFFSET-SI-TO-UNIT,
PHYSICAL-DIMENSION-REF).

Round-trip counterpart: tests/test_armodel/writer/test_writer_unit.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.models.M2.MSR.AsamHdo.Units import Unit
from armodel.parser.arxml_parser import ARXMLParser

FULL_UNIT_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>Units</SHORT-NAME>
            <ELEMENTS>
                <UNIT>
                    <SHORT-NAME>KmPerHour</SHORT-NAME>
                    <DISPLAY-NAME>kilometer per hour</DISPLAY-NAME>
                    <FACTOR-SI-TO-UNIT>3.6</FACTOR-SI-TO-UNIT>
                    <OFFSET-SI-TO-UNIT>0.0</OFFSET-SI-TO-UNIT>
                    <PHYSICAL-DIMENSION-REF DEST="PHYSICAL-DIMENSION">/PhysicalDimensions/Velocity</PHYSICAL-DIMENSION-REF>
                </UNIT>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501

PARTIAL_UNIT_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>Units</SHORT-NAME>
            <ELEMENTS>
                <UNIT>
                    <SHORT-NAME>Percent</SHORT-NAME>
                    <FACTOR-SI-TO-UNIT>1.0</FACTOR-SI-TO-UNIT>
                </UNIT>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501


def _load_unit(xml_text):
    parser = ARXMLParser()
    parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    element = ET.fromstring(xml_text)
    document = AUTOSARDoc()
    parser.readARPackages(element, document)
    ar_package = document.getARPackages()[0]
    units = ar_package.getUnits()
    assert len(units) == 1
    return units[0]


class TestUnitParser:
    """Reader coverage for the UNIT content (Table 5.79)."""

    def test_read_unit_short_name(self):
        unit = _load_unit(FULL_UNIT_XML)
        assert isinstance(unit, Unit)
        assert unit.getShortName() == "KmPerHour"

    def test_read_unit_display_name(self):
        """The DISPLAY-NAME mixed text round-trips into the SingleLanguageUnitNames aggregation."""
        unit = _load_unit(FULL_UNIT_XML)
        display_name = unit.getDisplayName()
        assert display_name is not None
        assert display_name.getMixedString() == "kilometer per hour"

    def test_read_unit_factor_and_offset(self):
        unit = _load_unit(FULL_UNIT_XML)
        assert unit.getFactorSiToUnit().getValue() == 3.6
        assert unit.getOffsetSiToUnit().getValue() == 0.0

    def test_read_unit_physical_dimension_ref(self):
        unit = _load_unit(FULL_UNIT_XML)
        assert unit.getPhysicalDimensionRef().getValue() == "/PhysicalDimensions/Velocity"
        assert unit.getPhysicalDimensionRef().getDest() == "PHYSICAL-DIMENSION"

    def test_read_unit_partial(self):
        """A UNIT carrying only FACTOR-SI-TO-UNIT leaves the other fields None (all 0..1)."""
        unit = _load_unit(PARTIAL_UNIT_XML)
        assert unit.getFactorSiToUnit().getValue() == 1.0
        assert unit.getDisplayName() is None
        assert unit.getOffsetSiToUnit() is None
        assert unit.getPhysicalDimensionRef() is None
