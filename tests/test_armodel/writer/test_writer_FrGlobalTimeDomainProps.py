"""Writer/reader round-trip tests for FrGlobalTimeDomainProps (Table 9.22, p.878)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FrGlobalTimeDomainProps
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
    props = FrGlobalTimeDomainProps()
    props.setChecksum(String().setValue("13"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(Identifier().setValue("frVpLabel"))
    props.setVariationPoint(variation_point)
    props.addOfsDataIDList(PositiveInteger().setValue("3"))
    props.addOfsDataIDList(PositiveInteger().setValue("4"))
    props.addSyncDataIDList(PositiveInteger().setValue("5"))
    return props


class TestWriteFrGlobalTimeDomainProps:
    def test_write_wrapper_lists_in_xsd_order(self, writer):
        """
        The helper writes the VARIATION-POINT (inherited abstract group) first and then the two
        <...-DATA-ID-LISTS> wrappers, each emitted only when non-empty.
        """
        element = ET.Element("FR-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeFrGlobalTimeDomainProps(element, _new_props())

        assert element.attrib["S"] == "13"
        assert [child.tag for child in element] == [
            "VARIATION-POINT",
            "OFS-DATA-ID-LISTS",
            "SYNC-DATA-ID-LISTS",
        ]
        ofs_items = element.find("OFS-DATA-ID-LISTS").findall("OFS-DATA-ID-LIST")
        assert [item.text for item in ofs_items] == ["3", "4"]
        assert element.find("SYNC-DATA-ID-LISTS").find("SYNC-DATA-ID-LIST").text == "5"

    def test_write_empty_wrappers_omitted(self, writer):
        """
        With no DataIDLists and no variation point, no wrapper elements are emitted.
        """
        element = ET.Element("FR-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeFrGlobalTimeDomainProps(element, FrGlobalTimeDomainProps())

        assert len(element) == 0


class TestFrGlobalTimeDomainPropsRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps the variation point and every DataIDList value.
        """
        element = ET.Element("FR-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeFrGlobalTimeDomainProps(element, _new_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readFrGlobalTimeDomainProps(parsed_element, FrGlobalTimeDomainProps())

        assert props.getChecksum().getValue() == "13"
        assert props.getVariationPoint().getShortLabel().getValue() == "frVpLabel"

        ofs = props.getOfsDataIDLists()
        assert len(ofs) == 2
        assert ofs[0].getValue() == 3
        assert ofs[1].getValue() == 4
        assert props.getSyncDataIDLists()[0].getValue() == 5

    def test_round_trip_empty_wrapper_lists(self, writer, parser):
        """
        A props object without DataIDLists round-trips to empty lists (no wrapper tags emitted).
        """
        element = ET.Element("FR-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeFrGlobalTimeDomainProps(element, FrGlobalTimeDomainProps())
        xml = ET.tostring(element, encoding="unicode")

        assert "DATA-ID-LISTS" not in xml

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readFrGlobalTimeDomainProps(parsed_element, FrGlobalTimeDomainProps())

        assert props.getOfsDataIDLists() == []
        assert props.getSyncDataIDLists() == []
