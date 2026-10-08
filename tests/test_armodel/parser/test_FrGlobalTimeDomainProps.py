"""Reader tests for FrGlobalTimeDomainProps (Table 9.22, p.878)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FrGlobalTimeDomainProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadFrGlobalTimeDomainProps:
    def test_read_wrapper_lists_and_variation_point(self, parser):
        """
        The two ordered DataIDList wrappers are read item by item and the VARIATION-POINT of
        the inherited ABSTRACT-GLOBAL-TIME-DOMAIN-PROPS group is read into the mixin slot.
        """
        element = ET.fromstring(
            "<FR-GLOBAL-TIME-DOMAIN-PROPS xmlns='%s' S='13'>"
            "<VARIATION-POINT><SHORT-LABEL>frVpLabel</SHORT-LABEL></VARIATION-POINT>"
            "<OFS-DATA-ID-LISTS>"
            "<OFS-DATA-ID-LIST>3</OFS-DATA-ID-LIST>"
            "<OFS-DATA-ID-LIST>4</OFS-DATA-ID-LIST>"
            "</OFS-DATA-ID-LISTS>"
            "<SYNC-DATA-ID-LISTS><SYNC-DATA-ID-LIST>5</SYNC-DATA-ID-LIST></SYNC-DATA-ID-LISTS>"
            "</FR-GLOBAL-TIME-DOMAIN-PROPS>" % NS
        )

        props = FrGlobalTimeDomainProps()
        parser.readFrGlobalTimeDomainProps(element, props)

        assert props.getChecksum().getValue() == "13"
        assert props.getVariationPoint().getShortLabel().getValue() == "frVpLabel"

        ofs = props.getOfsDataIDLists()
        assert len(ofs) == 2
        assert ofs[0].getValue() == 3
        assert ofs[1].getValue() == 4
        assert props.getSyncDataIDLists()[0].getValue() == 5

    def test_read_empty_element(self, parser):
        """
        An element without wrapper content leaves the lists empty and the variation point unset.
        """
        element = ET.fromstring("<FR-GLOBAL-TIME-DOMAIN-PROPS xmlns='%s'></FR-GLOBAL-TIME-DOMAIN-PROPS>" % NS)

        props = FrGlobalTimeDomainProps()
        parser.readFrGlobalTimeDomainProps(element, props)

        assert props.getVariationPoint() is None
        assert props.getOfsDataIDLists() == []
        assert props.getSyncDataIDLists() == []
