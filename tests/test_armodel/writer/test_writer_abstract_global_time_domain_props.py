"""Writer/reader round-trip tests for the AbstractGlobalTimeDomainProps reusable helper (Table 9.2, p.859)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class ConcreteAbstractGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_props():
    props = ConcreteAbstractGlobalTimeDomainProps()
    props.setChecksum(String().setValue("42"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(Identifier().setValue("vpLabel"))
    props.setVariationPoint(variation_point)
    return props


class TestWriteAbstractGlobalTimeDomainProps:
    def test_write_variation_point(self, writer):
        """
        The helper writes the mixin-provided VARIATION-POINT and the AR-OBJECT S attribute onto
        the concrete subclass element passed by the caller.
        """
        element = ET.Element("CAN-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeAbstractGlobalTimeDomainProps(element, _new_props())

        assert element.attrib["S"] == "42"
        variation_point_element = element.find("VARIATION-POINT")
        assert variation_point_element is not None
        short_label_element = variation_point_element.find("SHORT-LABEL")
        assert short_label_element is not None
        assert short_label_element.text == "vpLabel"

    def test_write_without_variation_point(self, writer):
        """
        An unset variation point emits no VARIATION-POINT element.
        """
        element = ET.Element("FR-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeAbstractGlobalTimeDomainProps(element, ConcreteAbstractGlobalTimeDomainProps())

        assert element.find("VARIATION-POINT") is None


class TestAbstractGlobalTimeDomainPropsRoundTrip:
    def test_round_trip_preserves_variation_point(self, writer, parser):
        """
        Write -> serialize -> parse keeps the variation point and the AR-OBJECT attribute.
        """
        element = ET.Element("CAN-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeAbstractGlobalTimeDomainProps(element, _new_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readAbstractGlobalTimeDomainProps(parsed_element, ConcreteAbstractGlobalTimeDomainProps())

        assert props.getChecksum().getValue() == "42"
        variation_point = props.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel().getValue() == "vpLabel"
