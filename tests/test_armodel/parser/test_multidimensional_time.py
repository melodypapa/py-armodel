"""Parser tests for the MultidimensionalTime helper (MULTIDIMENSIONAL-TIME: CSE-CODE + CSE-CODE-FACTOR)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CseCodeType, Integer
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadMultidimensionalTime:
    def test_read_cse_code(self, parser):
        """Test that CSE-CODE is read into a CseCodeType-typed cseCode."""
        time = MultidimensionalTime()
        element = ET.fromstring(f"<MAXIMUM xmlns='{NS}'>" "<CSE-CODE>100</CSE-CODE>" "<CSE-CODE-FACTOR>360</CSE-CODE-FACTOR>" "</MAXIMUM>")
        parser.readMultidimensionalTime(element, time)
        assert time.getCseCode() is not None
        assert isinstance(time.getCseCode(), CseCodeType)
        assert time.getCseCode().getValue() == "100"

    def test_read_cse_code_factor(self, parser):
        """Test that CSE-CODE-FACTOR is read into an Integer-typed cseCodeFactor."""
        time = MultidimensionalTime()
        element = ET.fromstring(f"<MAXIMUM xmlns='{NS}'>" "<CSE-CODE>100</CSE-CODE>" "<CSE-CODE-FACTOR>360</CSE-CODE-FACTOR>" "</MAXIMUM>")
        parser.readMultidimensionalTime(element, time)
        assert time.getCseCodeFactor() is not None
        assert isinstance(time.getCseCodeFactor(), Integer)
        assert time.getCseCodeFactor().getValue() == 360

    def test_read_absent_elements(self, parser):
        """Test that an empty wrapper element leaves both fields None."""
        time = MultidimensionalTime()
        element = ET.fromstring(f"<MAXIMUM xmlns='{NS}'/>")
        parser.readMultidimensionalTime(element, time)
        assert time.getCseCode() is None
        assert time.getCseCodeFactor() is None
