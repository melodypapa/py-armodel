"""Reader/writer round-trip tests for DataFilter (Table 4.75)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter, DataFilterTypeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, UnlimitedInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _full_filter() -> DataFilter:
    data_filter = DataFilter()
    data_filter.setDataFilterType(DataFilterTypeEnum().setValue(DataFilterTypeEnum.NEVER))
    data_filter.setMask(UnlimitedInteger().setValue(8))
    data_filter.setMax(UnlimitedInteger().setValue(1000))
    data_filter.setMin(UnlimitedInteger().setValue(0))
    data_filter.setOffset(PositiveInteger().setValue(3))
    data_filter.setPeriod(PositiveInteger().setValue(5))
    data_filter.setX(UnlimitedInteger().setValue(99))
    return data_filter


def test_write_data_filter(writer):
    parent = _parent()
    writer.setDataFilter(parent, "DATA-FILTER", _full_filter())

    tag = parent.find("DATA-FILTER")
    assert tag is not None
    children = list(tag)
    assert [child.tag for child in children] == ["DATA-FILTER-TYPE", "MASK", "MAX", "MIN", "OFFSET", "PERIOD", "X"]
    assert children[0].text == "NEVER"
    assert children[1].text == "8"
    assert children[2].text == "1000"
    assert children[3].text == "0"
    assert children[4].text == "3"
    assert children[5].text == "5"
    assert children[6].text == "99"


def test_write_data_filter_empty(writer):
    parent = _parent()
    writer.setDataFilter(parent, "DATA-FILTER", DataFilter())

    tag = parent.find("DATA-FILTER")
    assert tag is not None
    assert len(list(tag)) == 0


def test_data_filter_round_trip(writer):
    parent = _parent()
    writer.setDataFilter(parent, "DATA-FILTER", _full_filter())

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getDataFilter(reparsed, "DATA-FILTER")
    assert isinstance(reloaded, DataFilter)
    assert isinstance(reloaded.getDataFilterType(), DataFilterTypeEnum)
    assert reloaded.getDataFilterType().getValue() == "NEVER"
    assert isinstance(reloaded.getMask(), UnlimitedInteger)
    assert reloaded.getMask().getValue() == 8
    assert isinstance(reloaded.getMax(), UnlimitedInteger)
    assert reloaded.getMax().getValue() == 1000
    assert isinstance(reloaded.getMin(), UnlimitedInteger)
    assert reloaded.getMin().getValue() == 0
    assert isinstance(reloaded.getOffset(), PositiveInteger)
    assert reloaded.getOffset().getValue() == 3
    assert isinstance(reloaded.getPeriod(), PositiveInteger)
    assert reloaded.getPeriod().getValue() == 5
    assert isinstance(reloaded.getX(), UnlimitedInteger)
    assert reloaded.getX().getValue() == 99
