"""Parser tests for the abstract DataMapping base (Table 5.22, p.217).

Abstract XML-bearing base: the XSD group DATA-MAPPING (AUTOSAR_00052.xsd line 27249)
carries the class-own INTRODUCTION element plus a VARIATION-POINT element; the
atp.Status="removed" members (COMMUNICATION-DIRECTION, EVENT-GROUP-REFS,
EVENT-HANDLER-REFS, SERVICE-INSTANCE-REFS) are deliberately not read. The helper is
exercised through a test-local concrete subclass because DataMapping itself has no
standalone element and no dispatch branch until its concrete subtypes are synced.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class _ConcreteDataMapping(DataMapping):
    pass


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<CONCRETE-MAPPING xmlns='%s'>%s</CONCRETE-MAPPING>" % (NS, inner))


class TestReadDataMapping:
    def test_read_introduction(self):
        element = _snip("<INTRODUCTION><P><L-1 L='en'>Mapping intro</L-1></P></INTRODUCTION>")
        mapping = _ConcreteDataMapping()

        ARXMLParser().readDataMapping(element, mapping)

        block = mapping.getIntroduction()
        assert block is not None
        assert block.getPs()[0].getL1s()[0].getValue() == "Mapping intro"

    def test_read_without_introduction(self):
        element = _snip("")
        mapping = _ConcreteDataMapping()

        ARXMLParser().readDataMapping(element, mapping)

        assert mapping.getIntroduction() is None
        assert mapping.getVariationPoint() is None

    def test_read_variation_point(self):
        element = _snip("<INTRODUCTION><P><L-1 L='en'>Mapping intro</L-1></P></INTRODUCTION>" "<VARIATION-POINT><SHORT-LABEL>varLbl</SHORT-LABEL></VARIATION-POINT>")
        mapping = _ConcreteDataMapping()

        ARXMLParser().readDataMapping(element, mapping)

        assert mapping.getIntroduction() is not None
        variation_point = mapping.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel().getValue() == "varLbl"
