"""Reader tests for the AbstractGlobalTimeDomainProps reusable helper (Table 9.2, p.859)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    AbstractGlobalTimeDomainProps,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class ConcreteAbstractGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadAbstractGlobalTimeDomainProps:
    def test_read_variation_point(self, parser):
        """
        The VARIATION-POINT of the XSD ABSTRACT-GLOBAL-TIME-DOMAIN-PROPS group is read into
        the mixin-provided slot; the AR-OBJECT S attribute is read into the checksum.
        """
        element = ET.fromstring("<CAN-GLOBAL-TIME-DOMAIN-PROPS xmlns='%s' S='42'>" "<VARIATION-POINT><SHORT-LABEL>vpLabel</SHORT-LABEL></VARIATION-POINT>" "</CAN-GLOBAL-TIME-DOMAIN-PROPS>" % NS)

        props = parser.readAbstractGlobalTimeDomainProps(element, ConcreteAbstractGlobalTimeDomainProps())

        assert props.getChecksum().getValue() == "42"
        variation_point = props.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel().getValue() == "vpLabel"

    def test_read_without_variation_point(self, parser):
        """
        A concrete subclass element without VARIATION-POINT leaves the variation point unset.
        """
        element = ET.fromstring("<ETH-GLOBAL-TIME-DOMAIN-PROPS xmlns='%s'></ETH-GLOBAL-TIME-DOMAIN-PROPS>" % NS)

        props = parser.readAbstractGlobalTimeDomainProps(element, ConcreteAbstractGlobalTimeDomainProps())

        assert props.getVariationPoint() is None
        assert props.getChecksum() is None
