"""
Tests for reading PHYSICAL-DIMENSION — SWCT Table 5.76 (p.398, R23-11).

PhysicalDimension (Base = ARElement) is aggregated by ARPackage.element. The reader
populates the model via its mutators in the XSD element order of the AUTOSAR_00052.xsd
group PHYSICAL-DIMENSION (sequenceOffset 20..80: LENGTH-EXP, MASS-EXP, TIME-EXP,
CURRENT-EXP, TEMPERATURE-EXP, MOLAR-AMOUNT-EXP, LUMINOUS-INTENSITY-EXP).

Round-trip counterpart: tests/test_armodel/writer/test_writer_physical_dimension.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical
from armodel.models.M2.MSR.AsamHdo.Units import PhysicalDimension
from armodel.parser.arxml_parser import ARXMLParser

FULL_DIMENSION_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>PhysicalDimensions</SHORT-NAME>
            <ELEMENTS>
                <PHYSICAL-DIMENSION>
                    <SHORT-NAME>Energy</SHORT-NAME>
                    <LENGTH-EXP>2</LENGTH-EXP>
                    <MASS-EXP>1</MASS-EXP>
                    <TIME-EXP>-2</TIME-EXP>
                    <CURRENT-EXP>0</CURRENT-EXP>
                    <TEMPERATURE-EXP>0</TEMPERATURE-EXP>
                    <MOLAR-AMOUNT-EXP>0</MOLAR-AMOUNT-EXP>
                    <LUMINOUS-INTENSITY-EXP>0</LUMINOUS-INTENSITY-EXP>
                </PHYSICAL-DIMENSION>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501

PARTIAL_DIMENSION_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>PhysicalDimensions</SHORT-NAME>
            <ELEMENTS>
                <PHYSICAL-DIMENSION>
                    <SHORT-NAME>Duration</SHORT-NAME>
                    <TIME-EXP>0.5</TIME-EXP>
                </PHYSICAL-DIMENSION>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501

EMPTY_DIMENSION_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>PhysicalDimensions</SHORT-NAME>
            <ELEMENTS>
                <PHYSICAL-DIMENSION>
                    <SHORT-NAME>NoDimension</SHORT-NAME>
                </PHYSICAL-DIMENSION>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501


def _load_dimension(xml_text):
    parser = ARXMLParser()
    parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    element = ET.fromstring(xml_text)
    document = AUTOSARDoc()
    parser.readARPackages(element, document)
    ar_package = document.getARPackages()[0]
    dimensions = ar_package.getEcucPhysicalDimensions()
    assert len(dimensions) == 1
    return dimensions[0]


class TestPhysicalDimensionParser:
    """Reader coverage for the PHYSICAL-DIMENSION content (Table 5.76)."""

    def test_read_physical_dimension_short_name(self):
        dimension = _load_dimension(FULL_DIMENSION_XML)
        assert isinstance(dimension, PhysicalDimension)
        assert dimension.getShortName() == "Energy"

    def test_read_physical_dimension_all_exponents(self):
        """All seven exponent field values round-trip as Numerical values."""
        dimension = _load_dimension(FULL_DIMENSION_XML)
        assert isinstance(dimension.getLengthExp(), Numerical)
        assert dimension.getLengthExp().getValue() == 2
        assert dimension.getMassExp().getValue() == 1
        assert dimension.getTimeExp().getValue() == -2
        assert dimension.getCurrentExp().getValue() == 0
        assert dimension.getTemperatureExp().getValue() == 0
        assert dimension.getMolarAmountExp().getValue() == 0
        assert dimension.getLuminousIntensityExp().getValue() == 0

    def test_read_physical_dimension_partial(self):
        """A PHYSICAL-DIMENSION carrying only TIME-EXP leaves the other exponents None (all 0..1)."""
        dimension = _load_dimension(PARTIAL_DIMENSION_XML)
        assert dimension.getTimeExp().getValue() == 0.5
        assert dimension.getLengthExp() is None
        assert dimension.getMassExp() is None
        assert dimension.getCurrentExp() is None
        assert dimension.getTemperatureExp() is None
        assert dimension.getMolarAmountExp() is None
        assert dimension.getLuminousIntensityExp() is None

    def test_read_physical_dimension_empty(self):
        """A PHYSICAL-DIMENSION without exponent elements leaves all seven None."""
        dimension = _load_dimension(EMPTY_DIMENSION_XML)
        assert dimension.getShortName() == "NoDimension"
        assert dimension.getCurrentExp() is None
        assert dimension.getLengthExp() is None
        assert dimension.getLuminousIntensityExp() is None
        assert dimension.getMassExp() is None
        assert dimension.getMolarAmountExp() is None
        assert dimension.getTemperatureExp() is None
        assert dimension.getTimeExp() is None
