"""Writer/reader round-trip tests for CanGlobalTimeDomainProps (Table 9.10, p.864)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import CanGlobalTimeDomainProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


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
    props = CanGlobalTimeDomainProps()
    props.setChecksum(String().setValue("11"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(Identifier().setValue("vpLabel"))
    props.setVariationPoint(variation_point)
    props.addFupDataIDList(PositiveInteger().setValue("1"))
    props.addFupDataIDList(PositiveInteger().setValue("2"))
    props.addOfnsDataIDList(PositiveInteger().setValue("3"))
    props.addOfsDataIDList(PositiveInteger().setValue("4"))
    props.addSyncDataIDList(PositiveInteger().setValue("5"))
    return props


class TestWriteCanGlobalTimeDomainProps:
    def test_write_wrapper_lists_in_xsd_order(self, writer):
        """
        The helper writes the VARIATION-POINT (inherited abstract group) first and then the four
        <...-DATA-ID-LISTS> wrappers, each emitted only when non-empty.
        """
        element = ET.Element("CAN-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeCanGlobalTimeDomainProps(element, _new_props())

        assert element.attrib["S"] == "11"
        assert [child.tag for child in element] == [
            "VARIATION-POINT",
            "FUP-DATA-ID-LISTS",
            "OFNS-DATA-ID-LISTS",
            "OFS-DATA-ID-LISTS",
            "SYNC-DATA-ID-LISTS",
        ]
        fup_wrapper = element.find("FUP-DATA-ID-LISTS")
        fup_items = fup_wrapper.findall("FUP-DATA-ID-LIST")
        assert [item.text for item in fup_items] == ["1", "2"]
        assert element.find("OFNS-DATA-ID-LISTS").find("OFNS-DATA-ID-LIST").text == "3"
        assert element.find("OFS-DATA-ID-LISTS").find("OFS-DATA-ID-LIST").text == "4"
        assert element.find("SYNC-DATA-ID-LISTS").find("SYNC-DATA-ID-LIST").text == "5"

    def test_write_empty_wrappers_omitted(self, writer):
        """
        With no DataIDLists and no variation point, no wrapper elements are emitted.
        """
        element = ET.Element("CAN-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeCanGlobalTimeDomainProps(element, CanGlobalTimeDomainProps())

        assert len(element) == 0


class TestCanGlobalTimeDomainPropsRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps the variation point and every DataIDList value.
        """
        element = ET.Element("CAN-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeCanGlobalTimeDomainProps(element, _new_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readCanGlobalTimeDomainProps(parsed_element, CanGlobalTimeDomainProps())

        assert props.getChecksum().getValue() == "11"
        assert props.getVariationPoint().getShortLabel().getValue() == "vpLabel"

        fup = props.getFupDataIDLists()
        assert len(fup) == 2
        assert fup[0].getValue() == 1
        assert fup[1].getValue() == 2
        assert props.getOfnsDataIDLists()[0].getValue() == 3
        assert props.getOfsDataIDLists()[0].getValue() == 4
        assert props.getSyncDataIDLists()[0].getValue() == 5

    def test_round_trip_empty_wrapper_lists(self, writer, parser):
        """
        A props object without DataIDLists round-trips to empty lists (no wrapper tags emitted).
        """
        element = ET.Element("CAN-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeCanGlobalTimeDomainProps(element, CanGlobalTimeDomainProps())
        xml = ET.tostring(element, encoding="unicode")

        assert "DATA-ID-LISTS" not in xml

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readCanGlobalTimeDomainProps(parsed_element, CanGlobalTimeDomainProps())

        assert props.getFupDataIDLists() == []
        assert props.getOfnsDataIDLists() == []
        assert props.getOfsDataIDLists() == []
        assert props.getSyncDataIDLists() == []
