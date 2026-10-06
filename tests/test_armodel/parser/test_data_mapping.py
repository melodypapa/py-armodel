"""Parser tests for the abstract DataMapping base (Table 5.22, p.217).

Abstract XML-bearing base: the XSD group DATA-MAPPING (AUTOSAR_00052.xsd line 27249)
carries COMMUNICATION-DIRECTION followed by the class-own INTRODUCTION element plus a
VARIATION-POINT element; the remaining atp.Status="removed" members (EVENT-GROUP-REFS,
EVENT-HANDLER-REFS, SERVICE-INSTANCE-REFS) are deliberately not read.
COMMUNICATION-DIRECTION is a Rule 0019 legacy member (R4.3.1 Table 5.14, removed in
R23-11) kept because authentic R22-11 SystemMapping fixtures carry it. The helper is
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

    def test_read_communication_direction(self):
        element = _snip("<COMMUNICATION-DIRECTION>IN</COMMUNICATION-DIRECTION>")
        mapping = _ConcreteDataMapping()

        ARXMLParser().readDataMapping(element, mapping)

        direction = mapping.getCommunicationDirection()
        assert direction is not None
        assert direction.getValue() == "IN"

    def test_read_ref_lists(self):
        element = _snip(
            "<EVENT-GROUP-REFS>"
            "<EVENT-GROUP-REF DEST='CONSUMED-EVENT-GROUP'>/eg</EVENT-GROUP-REF>"
            "</EVENT-GROUP-REFS>"
            "<EVENT-HANDLER-REFS>"
            "<EVENT-HANDLER-REF DEST='EVENT-HANDLER'>/eh</EVENT-HANDLER-REF>"
            "</EVENT-HANDLER-REFS>"
            "<SERVICE-INSTANCE-REFS>"
            "<SERVICE-INSTANCE-REF DEST='SERVICE-INSTANCE'>/si</SERVICE-INSTANCE-REF>"
            "</SERVICE-INSTANCE-REFS>"
        )
        mapping = _ConcreteDataMapping()

        ARXMLParser().readDataMapping(element, mapping)

        assert [r.getValue() for r in mapping.getEventGroupRefs()] == ["/eg"]
        assert [r.getValue() for r in mapping.getEventHandlerRefs()] == ["/eh"]
        assert [r.getValue() for r in mapping.getServiceInstanceRefs()] == ["/si"]

    def test_read_without_introduction(self):
        element = _snip("")
        mapping = _ConcreteDataMapping()

        ARXMLParser().readDataMapping(element, mapping)

        assert mapping.getCommunicationDirection() is None
        assert mapping.getEventGroupRefs() == []
        assert mapping.getEventHandlerRefs() == []
        assert mapping.getIntroduction() is None
        assert mapping.getServiceInstanceRefs() == []
        assert mapping.getVariationPoint() is None

    def test_read_variation_point(self):
        element = _snip("<INTRODUCTION><P><L-1 L='en'>Mapping intro</L-1></P></INTRODUCTION>" "<VARIATION-POINT><SHORT-LABEL>varLbl</SHORT-LABEL></VARIATION-POINT>")
        mapping = _ConcreteDataMapping()

        ARXMLParser().readDataMapping(element, mapping)

        assert mapping.getIntroduction() is not None
        variation_point = mapping.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel().getValue() == "varLbl"
