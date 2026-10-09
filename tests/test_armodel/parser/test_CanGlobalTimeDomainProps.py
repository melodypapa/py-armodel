"""Reader tests for CanGlobalTimeDomainProps (Table 9.10, p.864)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import CanGlobalTimeDomainProps
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


class TestReadCanGlobalTimeDomainProps:
    def test_read_wrapper_lists_and_variation_point(self, parser):
        """
        The four ordered DataIDList wrappers are read item by item and the VARIATION-POINT of
        the inherited ABSTRACT-GLOBAL-TIME-DOMAIN-PROPS group is read into the mixin slot.
        """
        element = ET.fromstring(
            "<CAN-GLOBAL-TIME-DOMAIN-PROPS xmlns='%s' S='11'>"
            "<VARIATION-POINT><SHORT-LABEL>vpLabel</SHORT-LABEL></VARIATION-POINT>"
            "<FUP-DATA-ID-LISTS>"
            "<FUP-DATA-ID-LIST>1</FUP-DATA-ID-LIST>"
            "<FUP-DATA-ID-LIST>2</FUP-DATA-ID-LIST>"
            "</FUP-DATA-ID-LISTS>"
            "<OFNS-DATA-ID-LISTS><OFNS-DATA-ID-LIST>3</OFNS-DATA-ID-LIST></OFNS-DATA-ID-LISTS>"
            "<OFS-DATA-ID-LISTS><OFS-DATA-ID-LIST>4</OFS-DATA-ID-LIST></OFS-DATA-ID-LISTS>"
            "<SYNC-DATA-ID-LISTS><SYNC-DATA-ID-LIST>5</SYNC-DATA-ID-LIST></SYNC-DATA-ID-LISTS>"
            "</CAN-GLOBAL-TIME-DOMAIN-PROPS>" % NS
        )

        props = CanGlobalTimeDomainProps()
        parser.readCanGlobalTimeDomainProps(element, props)

        assert props.getChecksum().getValue() == "11"
        assert props.getVariationPoint().getShortLabel().getValue() == "vpLabel"

        fup = props.getFupDataIDLists()
        assert len(fup) == 2
        assert fup[0].getValue() == 1
        assert fup[1].getValue() == 2
        assert props.getOfnsDataIDLists()[0].getValue() == 3
        assert props.getOfsDataIDLists()[0].getValue() == 4
        assert props.getSyncDataIDLists()[0].getValue() == 5

    def test_read_empty_element(self, parser):
        """
        An element without wrapper content leaves the lists empty and the variation point unset.
        """
        element = ET.fromstring("<CAN-GLOBAL-TIME-DOMAIN-PROPS xmlns='%s'></CAN-GLOBAL-TIME-DOMAIN-PROPS>" % NS)

        props = CanGlobalTimeDomainProps()
        parser.readCanGlobalTimeDomainProps(element, props)

        assert props.getVariationPoint() is None
        assert props.getFupDataIDLists() == []
        assert props.getOfnsDataIDLists() == []
        assert props.getOfsDataIDLists() == []
        assert props.getSyncDataIDLists() == []
